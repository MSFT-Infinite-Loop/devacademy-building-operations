# ADR-00N: Caching strategy

- **Status:** Proposed
- **Date:** 2026-11-25
- **Author(s):** Petar Ivanov
- **Requirement IDs:** ARC-07, BE-C07, BE-A02, BE-A04 (backplane choice), BE-A06 (cache-hit-ratio metric), OPS-C04, ARC-10, AI-06, SEC-03
- **Supersedes:** None
- **Superseded by:** None
- **Depends on:** database ADR (proposed: PostgreSQL; relevant points: database-call evidence for BE-A02), hosting ADR (ADR-001, proposed: Azure Container Apps and Azure Container Registry; relevant points: instance count, where Valkey runs), the jobs, outbox and real-time ADR (it proposes Valkey as the BE-A04 backplane candidate), the frontend ADR (Carlos's draft; its cache layers are separate, FE-A02)

## Context

- The team is four people. The spec makes **BE Advanced mandatory for a team of four**, so BE-A02 and BE-A06 are MUST items, not options.
- BE-C07 (Core): cache at least two repeated reads with HybridCache, IMemoryCache or output caching; invalidate explicitly on writes; make hits and misses observable through logs or metrics.
- BE-A02 (Advanced): a distributed L2 cache for HybridCache using Valkey, Memcached or Dragonfly through an `IDistributedCache` implementation, with:
  - stampede protection, a documented key strategy, a TTL strategy and tag-based invalidation;
  - a load test (k6 or Azure Load Testing) comparing before and after latency percentiles and database-call counts;
  - a reproduced and then fixed connection-pool-exhaustion scenario;
  - a report in `docs/performance`.
- BE-A06 (Advanced) requires custom OpenTelemetry metrics, including **cache-hit ratio**, exported to a dashboard.
- BE-A04 (Advanced) needs a scale-out backplane for push: Azure SignalR Service, Valkey or Dragonfly. **Memcached has no pub/sub and is not an approved backplane.**
- OPS-C04 requires the one-command stack to start "database, cache and seed data included", which a real cache service now satisfies.
- Redis is not allowed. Licence policy (ARC-10): Valkey is BSD-3; Memcached is BSD; Dragonfly is BSL 1.1, an approved exception only when self-hosted, unmodified and used as the application cache.
- Cached data must never leak across buildings, roles or users (SEC-03).
- The frontend draft (Next.js, server-first) adds its own cache layers (browser, Next.js server, FE-A02). They are separate from this API cache: no keys are shared. The API sends `Cache-Control: no-store` on authenticated responses (see the API style ADR), which tells HTTP caches not to store the API response; it does not control what Next.js caches when it renders a page. **Next.js must not store personalised data or views in a shared cache** (for example, a shared My Notifications view could show one resident's notifications to the next). How that is enforced belongs to the frontend ADR, which already states the same rule; this ADR covers only what the API caches internally with HybridCache and Valkey.

## Decision drivers

1. Meet BE-C07 and BE-A02 with one coherent design, with evidence the jury can reproduce from one command.
2. Hits and misses observable as logs and as the metric BE-A06 needs.
3. Explicit invalidation on writes, with tags.
4. One licence-clean service that also covers a possible BE-A04 backplane.
5. No cross-building or cross-role leakage.

## Options considered

### Option 1: HybridCache, in-process (L1 only)

- **Advantages:** No extra service. Stampede protection and tag invalidation.
- **Disadvantages:** Does not meet BE-A02. Stampede protection is per instance, and invalidation does not reach other instances' memory. Tag invalidation is logical, not a physical delete.
- **Risks:** Only useful as the fallback inside the chosen design (L1 stays in front of L2 anyway). No hit/miss logging or metric is built in.

### Option 2: `IMemoryCache` directly, or output caching

- **Advantages:** Simple; both are allowed for BE-C07.
- **Disadvantages:** `IMemoryCache` has no stampede protection, tags or L2 path. Output caching by default stores only `200` GET/HEAD responses, skips responses that set cookies, and **skips responses to authenticated requests**, a poor fit for role-scoped data.
- **Risks:** Does not satisfy BE-A02; invalidation bugs or cross-user leaks if policies are loosened.

### Option 3: HybridCache with Valkey as L2

- **Advantages:**
  - BSD-3 licence (no special conditions to track), and the spec's own caching note says Valkey works with the standard Redis-protocol .NET client.
  - Can also serve as the BE-A04 backplane (pub/sub), so one service could cover both. The backplane use is a candidate in the jobs, outbox and real-time ADR, pending a compatibility test.
  - A single container in Compose satisfies OPS-C04.
- **Disadvantages:** Another container; a serializer is needed for L2; the load-test and pool-exhaustion work is real effort.
- **Risks:** The .NET client's package name contains "Redis" (it is the protocol client, not the Redis server). Confirm it is acceptable under ARC-10 and AI-06 (that it is the intended package, maintained, MIT) and take it to the jury if there is doubt.

### Option 4: HybridCache with Memcached as L2

- **Advantages:** BSD, simple, a reasonable cache.
- **Disadvantages:** Needs a third-party `IDistributedCache` implementation (for example EnyimMemcachedCore) that must be verified. **No pub/sub**, so a second service would be needed if the team picks a Valkey or Dragonfly backplane for BE-A04.
- **Risks:** More dependencies to check; less alignment with the rest of the design.

### Option 5: HybridCache with Dragonfly as L2

- **Advantages:** Redis-protocol compatible, high performance, and could also serve as a backplane.
- **Disadvantages:** BSL 1.1 is an approved exception only with conditions (self-hosted, unmodified, application cache only), which must be tracked and declared.
- **Risks:** Compliance overhead with no offsetting benefit over Valkey for this project.

## Decision

**Proposed decision (pending team approval):** Option 3, HybridCache with L1 in front of a Valkey L2, in the Compose stack.

1. **Service:** one Valkey container in the one-command stack (OPS-C04), with the exact image and version pinned and its licence recorded in the README dependency list.
2. **Client:** the standard Redis-protocol `IDistributedCache` implementation for .NET, registered as HybridCache's L2. Package choice and licence are verified before first use (follow-up 1).
3. **Authorize first.** The requested resource is authorized before any cache lookup. Cache only authorization-safe DTOs, and never cache authorization decisions.
4. **Keys:** module, version, building id, resource id, and every role, user or relationship dimension that changes the result. Key strategy is documented (BE-A02).
5. **TTLs:** documented per cached read, with explicit expiry, not "forever".
6. **Invalidation:** tags per building or resource, removed explicitly on every write that affects them. Because tag removal is logical, the design records that it relies on timestamps and TTLs, not physical deletes.
7. **Observability:** a `Meter` with hit and miss counters (a miss is counted when the factory delegate runs), also logged at a visible level. The cache-hit ratio is derived from these and exported for the BE-A06 dashboard.
8. **Evidence plan (BE-A02):** a k6 or Azure Load Testing run, before and after, with latency percentiles and database-call counts; a reproduced connection-pool-exhaustion scenario with its fix; the report in `docs/performance`.
9. **Candidate reads:** the cached reads are chosen from Core read endpoints once the feature specs exist, preferring slow-changing building or reference data.
10. **Failure behaviour:** if Valkey is unavailable, HybridCache is expected to log the failure and fall back to L1 and the factory (its log events cover backend read and write failures); this is **confirmed during implementation** and covered by a test (see BE-A05 on resilience).
11. **Multiple instances:** HybridCache removals propagate to L2 but **not to other instances' L1**, so a write on one instance does not clear another instance's L1 copy. L1 entries therefore get a short TTL that bounds this staleness (stated per cached read), or the API runs as a single instance. The jobs, outbox and real-time ADR also runs jobs inside the API host; both ADRs assume this until the hosting ADR says otherwise. The hosting ADR proposes Azure Container Apps, which can run several replicas, so its replica settings decide which applies.

### Open points (tracked, not decided here)

- Valkey vs Dragonfly confirmation with the team; this ADR proposes Valkey.
- Whether Valkey also becomes the BE-A04 backplane (proposed as a candidate in the jobs, outbox and real-time ADR), or Azure SignalR Service is used instead.

## Consequences

### Positive

- BE-C07, BE-A02 and the OPS-C04 cache wording are covered by one design.
- One service can also serve as the real-time backplane.
- Explicit isolation, TTL and invalidation rules.

### Negative

- An extra container to start, pin, secure and document.
- Load-testing and pool-exhaustion work consume part of the roughly 20 hours of BE Advanced.
- Custom instrumentation is required.

### Follow-up actions

1. Verify the L2 client package: exists, intended package, maintained, licence from the repository and NuGet (**NuGet not yet verified**). Check Valkey compatibility with the chosen client version.
2. Choose the two or more cached reads and write their TTL and invalidation rules.
3. Verify during implementation (**not yet done**): a hit, a miss, invalidation after a write, no cross-building leakage, and L2 failure fallback.
4. Plan the load test and the pool-exhaustion scenario with the database ADR owner.
5. Agree with the hosting ADR where Valkey runs in the hosted Preview and Release environments (a Valkey container; Redis-based managed services are not allowed).
6. Confirm with the frontend ADR how Next.js is kept from storing personalised data or views in a shared cache, and verify it during implementation with a two-user check on a personalised page (**not yet done**).

## Evidence and verification

- No code was built or run for this draft. Sources are documentation and source reading.
- Microsoft Learn (links resolve, `view=aspnetcore-10.0`):
  - https://learn.microsoft.com/en-us/aspnet/core/performance/caching/hybrid
  - https://learn.microsoft.com/en-us/aspnet/core/performance/caching/output
- Source: HybridCache log events in dotnet/extensions (`src/Libraries/Microsoft.Extensions.Caching.Hybrid/Internal/Log.cs`) cover failures and rejections only.
- Licences read from the repositories: dotnet/extensions MIT; StackExchange.Redis MIT (`LICENSE` on main); Valkey BSD 3-Clause (`COPYING` in valkey-io/valkey).
- Requirement and licence wording (BE-A02, BE-A04, BE-A06, OPS-C04, ARC-10, the Valkey / Memcached / Dragonfly matrix) from capstone requirements v1.4 as recorded in the working specification (`docs/capstone-spec/`) (`docs/capstone-spec/07-track-backend.md`, `docs/capstone-spec/10-architecture-tech-policy.md`).
- **Not verified:** NuGet package metadata (TLS failure to `api.nuget.org` on the authoring machine), the Memcached client package, and Valkey and Dragonfly versions.

## AI assistance

GitHub Copilot (Claude) researched the cited documentation and repositories and drafted this ADR. A second AI review pass critiqued earlier versions and its findings were fixed; later edits (four-person scope, alignment with the frontend, architecture, hosting and database drafts) were not separately reviewed. The claims about platform behaviour come from documentation and source reading, and no code was built or run for this ADR, so none is verified by experiment. Verification is tracked as implementation follow-up (see Follow-up actions) and is not a condition of this ADR. Human review is pending and will happen in the pull request.

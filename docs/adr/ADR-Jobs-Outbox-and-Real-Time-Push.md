# ADR-00N: Background jobs, transactional outbox and real-time push

- **Status:** Proposed
- **Date:** 2026-11-25
- **Author(s):** Petar Ivanov
- **Requirement IDs:** ARC-07, ARC-09, BE-C08, BE-C09, BE-C10, M7-01, BE-A03, BE-A04, BE-A05, BE-A06, FE-A03, M3-06, M4-10, M4-11, M5-08, M6-02, M6-04, M6-05, SEC-03, M1-05, M1-06, ARC-10, AI-06
- **Supersedes:** None
- **Superseded by:** None
- **Depends on:** application architecture ADR (proposed: seven modules M1 to M7, module-led workflows, shared audit and outbox mechanics), database ADR (proposed: PostgreSQL; relevant points: row locking, unique constraints, transaction behaviour), caching ADR (Valkey is reused as the backplane), authn/authz ADR (cookie session, deactivation, Next.js topology), hosting ADR (ADR-001, [#19](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/19), proposed: Azure Container Apps and Azure Container Registry; relevant points: instance count including at least one always-running API replica, reverse proxy, sticky sessions), frontend ADR (proposed: Next.js with targeted refreshes; FE-A03 client behaviour)

## Context

The team is four people, so BE Advanced is mandatory. This ADR covers three linked concerns that ARC-09 asks the team to decide and justify, and that BE-C08 and BE-A03 to BE-A05 constrain.

**Scheduled jobs (BE-C08, Core).** The jobs required are:
- lease expiry flagging at 30 days and moving past-end leases to Ended (M3-06);
- SLA escalation, notifying the manager exactly once per breach (M4-10);
- auto-close of Resolved work orders after 7 days (M4-11);
- moving eligible statements to Overdue (M5-08);
- scheduled announcement publish and expiry (M6-02).

Each job must be idempotent, safe if run twice, logged, and observable (last run and outcome).

**Reliable notifications (M6-05, BE-A03).** A notification is created together with the business change that triggered it, by the same transaction or a transactional outbox. BE-A03 mandates the outbox, with idempotent consumers and tests proving correct behaviour when a message is delivered more than once.

**Real-time push (BE-A04, FE-A03).** Server-to-client push by SignalR or SSE, authorised per user and per building, with a documented scale-out design (Azure SignalR Service, or a Valkey or Dragonfly backplane; Memcached is not approved). The client needs reconnection, backoff, reconciliation with the client cache and a polling fallback.

Also relevant: BE-C10 (graceful shutdown, structured logs with correlation IDs), BE-A05 (provider abstractions, resilience and a fault-injection test), BE-A06 (OpenTelemetry metrics) and ARC-10 (licences).

## Decision drivers

1. Correctness under retries, duplicate runs and crashes (idempotence over exactly-once).
2. A push channel that cannot leak data, even if a connection is wrongly authorised.
3. A one-command stack with few moving parts for a four-person team.
4. Observable jobs and queue health, for the jury and for BE-A06.
5. A clean path to more than one API instance.
6. Licence compliance (ARC-10, AI-06).

## Options considered

### A. Where jobs and the outbox dispatcher run (ARC-09)

**A1: Inside the API host (`BackgroundService`), written to be host-agnostic**
- **Advantages:** One container and one deployment. Simplest one-command start. Shares the module code and configuration.
- **Disadvantages:** Every API instance would run the jobs, so double runs must be safe. Job load competes with request handling.
- **Risks:** Scaling the API out also scales the job runners. This is covered only if the claim and lease rules below are implemented and tested.

**A2: A separate worker container (same solution, second host)**
- **Advantages:** Jobs and dispatcher scale and fail independently. A single worker replica reduces concurrent runs, but does not prevent overlap during restarts, deployments or retries, so leases and idempotence are still required. API replicas stay stateless apart from SignalR connections.
- **Disadvantages:** A second composition root and image; more Compose, CI and documentation. The worker needs its own way to reach connected clients, which means the backplane.
- **Risks:** Extra work in Weeks 1 to 4, when the walking skeleton matters most.

### B. Scheduler

**B1: `BackgroundService` with `PeriodicTimer`, our own job-run table**
- **Advantages:** No dependency. Fully testable with `TimeProvider`. A `job_runs` table gives "last run and outcome" and feeds a small admin view.
- **Disadvantages:** We write scheduling, retry and the run history ourselves. No cron expressions.
- **Risks:** Hand-rolled schedulers invite subtle bugs (overlap, drift). Mitigated by small, uniform job classes and tests.

**B2: Quartz.NET**
- **Advantages:** Apache-2.0. Cron triggers, misfire handling and clustering with a persistent store.
- **Disadvantages:** A schema and package set to adopt, which depends on the database ADR. Learning cost.
- **Risks:** More machinery than five jobs need.

**B3: Hangfire**
- **Advantages:** Built-in dashboard, retries and recurring jobs.
- **Disadvantages:** Dual-licensed: LGPL-3.0 or a paid commercial licence. The LGPL terms need checking against ARC-10 and declaring. Storage packages depend on the chosen database. The dashboard is an extra attack surface and must sit behind our authorization.
- **Risks:** Licence ambiguity; a second admin UI outside our role model.

### C. Notification reliability

**C1: Transactional outbox, polled by a dispatcher (BE-A03)**
- **Advantages:** Satisfies BE-A03 and M6-05. Business change and message commit atomically. Supports several consumers (notification rows, push, future email).
- **Disadvantages:** At-least-once delivery, so every consumer must be idempotent. Needs a dispatcher, claiming, retries and a failed-message state.
- **Risks:** Polling lag; poison messages; claim bugs causing double processing.

**C2: Create the notification in the same transaction as the change, no outbox**
- **Advantages:** Allowed by M6-05 for in-app notifications. Simple.
- **Disadvantages:** Does not meet BE-A03, which is mandatory at four people, and cannot reliably drive push or provider calls.

### D. Real-time mechanism

**D1: SignalR**
- **Advantages:** Per-user and per-group fan-out built in (`user` and `building` groups). Transport fallback and reconnect support. A documented scale-out path.
- **Disadvantages:** SignalR captures the user when a connection is made and **does not revalidate it during the connection's life**, even for cookie authentication. Role, claim or deactivation changes are not reflected on an open connection. Sticky sessions are needed when scaled out with a backplane.
- **Risks:** A deactivated or re-scoped user keeps receiving pushes unless the server acts (see Decision).

**D2: Server-Sent Events (`TypedResults.ServerSentEvents`, new in .NET 10)**
- **Advantages:** Plain HTTP, one-way, cookie authentication when the stream is established (and again on each reconnect), simple proxying.
- **Disadvantages:** No groups or backplane: we would build fan-out, per-building routing and cross-instance delivery ourselves (pub/sub on Valkey). Reconnect and resume (`Last-Event-ID`) logic is ours.
- **Risks:** More custom code for the same outcome. Like SignalR, a long-lived stream is not continuously revalidated, so it would also need explicit termination on deactivation.

### E. Scale-out design (BE-A04)

**E1: Valkey backplane (the SignalR Redis-protocol backplane package), sticky sessions or WebSockets-only with `SkipNegotiation`. A candidate until a version-pinned compatibility test passes.**
- **Advantages:** Reuses the Valkey container from the caching ADR. Works from a separate worker (the worker publishes through the backplane).
- **Disadvantages:** Microsoft's documentation describes the Redis backplane, not Valkey: compatibility is **not yet verified**. Sticky sessions are required unless clients use WebSockets only with `SkipNegotiation`. Connection count drives scaling.
- **Risks:** An unverified package and server pairing.

**E2: Azure SignalR Service**
- **Advantages:** Microsoft recommends it for apps hosted on Azure. No sticky sessions. Offloads connections.
- **Disadvantages:** An Azure dependency that does not fit the offline one-command start. Cost and credit tracking.
- **Risks:** Can only be demonstrated in a hosted environment.

## Decision

**Proposed decision (pending team approval):** A1 + B1 + C1 + D1 + E1 (E1 conditional on a compatibility test), with the rules below.

### Host and scheduler (ARC-09, BE-C08)

1. Jobs and the outbox dispatcher run inside the API host as `BackgroundService`s. Job logic lives in plain classes that do not depend on the host, so it can move to a worker container later. Revisit A2 if measurements or the hosting ADR require it.
   - **Module ownership:** following the application architecture draft (the module that owns the outcome leads the workflow), each job's code lives in its owning module: M3 (lease jobs), M4 (SLA escalation, auto-close), M5 (overdue statements) and M6 (announcement publish and expiry). The scheduler, lease, outbox and audit mechanics are shared infrastructure, not business logic. M6 creates the inbox notification after commit, as a consumer of the outbox.
   - **Instances:** the hosting ADR ([#19](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/19), proposed) uses Azure Container Apps, which can run several replicas. **Dependency on the hosting ADR:** because jobs and the outbox dispatcher run inside the API, at least one API replica must keep running when there is no traffic; scale-to-zero would stop scheduled jobs and outbox delivery. The hosting draft already proposes this (API minimum replicas: 1). Leases and idempotence keep job runs safe, and the sticky-session or WebSockets-only rule for SignalR applies when more than one replica runs.
2. Hosted services are singletons, so each run or batch creates its own DI scope (or uses a `DbContext` factory). Cancellation from the stopping token is treated as normal shutdown; only unexpected failures are logged and retried. Each loop body catches and logs exceptions, so one failing job does not stop the others. The host behaviour on an unhandled exception is confirmed during implementation.
3. **Schedule rules:** every job has a documented interval, initial-run behaviour, maximum tolerated delay and restart catch-up rule (a job that was missed while the host was down runs on start). `PeriodicTimer` gives no cron or misfire semantics, so these rules are explicit. All stored and compared times are UTC; scheduled user input (announcement publish and expiry) is converted to UTC before it is stored. Jobs use an injected `TimeProvider`, so time rules are tested with a fake clock.
4. **Run history:** a `job_runs` record (job name, start, end, outcome, counts, correlation ID) gives "last run and outcome" and feeds a read-only admin view. It is operational history only, **not** the audit trail.
5. **Audit (BE-C09, M7-01):** every job-driven change writes an audit record with actor `System`, UTC timestamp, entity, before and after values, outcome and correlation ID, in the same transaction as the change.
6. **Logs and health (BE-C10):** job diagnostics are structured JSON logs carrying correlation IDs and never payloads, personal data, tokens or exception secrets. Liveness and readiness (readiness checks the database) are separate endpoints and belong to the operations design.
7. **Idempotence by conditional update:** each job changes state with a conditional update or a concurrency check inside a transaction (for example "set Ended where status is Active and end date has passed"), never select-then-update. "Once per ..." notifications are enforced by unique keys that include the recipient (below), not by timing.
8. **Overlap and multi-instance safety:** a `JobLease` row is acquired, renewed and released using **database time** and an owner (fencing) token, and every lease and job operation matches that token. Job names are an internal allow-list, and no API endpoint may change leases. Idempotence (item 7) is the real safety net, because a lease can expire under a paused worker. Tests cover concurrent acquisition, expiry during execution and crash recovery.
9. **Job rules, as proposed readings of the requirements:**
   - **M3-06:** for active leases ending within 30 days, create one notification per eligible tenant and one for the manager, each keyed `(leaseId, notificationKind, recipientId)`. Leases past their end date move to `Ended`. Transition, audit record and outbox rows are written atomically.
   - **M4-10:** one escalation notification per breach, keyed `(workOrderId, breachId, recipientId)`.
   - **M4-11, M5-08, M6-02:** conditional state transitions as in item 7; announcement publish and expiry use UTC times.
10. **Graceful shutdown (BE-C10):** loops honour the stopping token; in-flight batches finish or release their claims. The default host shutdown timeout is 30 seconds, and batch sizes are chosen to fit within it.

### Outbox (BE-A03, M6-05)

1. The business change, its audit record and its outbox message are committed in **one transaction**.
2. The dispatcher claims a small batch, processes it and marks it done. Claims carry an expiry, so a crashed processor's messages are reclaimed. The row-locking approach depends on the database ADR (with PostgreSQL, `FOR UPDATE SKIP LOCKED` is the natural claim query).
3. Delivery is **at-least-once**. Each consumer keeps an inbox keyed `(consumerName, messageId)`.
   - For database effects, the inbox row and the resulting rows (for example the recipient's notification) are written in **one transaction**, so redelivery has no second effect.
   - For external providers (email, SMS, payment simulator), a stable idempotency key is sent where the provider supports one. Where it does not, the ADR accepts and documents at-least-once external delivery, because a crash between the call and the inbox write can repeat it.
   - Push is non-durable and is never the completion criterion.
   - Tests deliver the same message twice and simulate crashes on both sides of the provider call (BE-A03).
4. **Envelope policy:** outbox messages are versioned and carry opaque ids, timestamps and the correlation ID only. Consumers reload authorised data. Payloads and exception details are redacted from logs.
5. Failures retry with backoff and a cap, then move to a visible failed state (poison messages). Failed messages have an alert threshold and a retention rule, and retry or quarantine is a role-protected, audited action.
6. **Notification preferences (M6-06, if adopted):** the consumer evaluates preferences before creating optional notifications; critical categories cannot be disabled.
7. **Idempotency-Key (BE-A03; header defined in the API style ADR):** a store keyed `(userId, endpoint, key)` holds a hash of the request, the stored response and an expiry. A replay with the same key and the same request returns the stored response with no second effect. A reuse with a different request (for example a different amount) is rejected with `422`, never answered with the earlier result, and a repeat that arrives while the first request is still being processed gets `409` (see the API style ADR). Concurrent first requests are serialised by the unique key. Keys expire after a documented period, and the store is part of the payment transaction.
8. Consumers that call providers sit behind provider interfaces with timeouts, jittered retries and circuit breakers, plus a fault-injection test (BE-A05). Retry budgets of the outbox and the HTTP layer are limited so they do not multiply.

### Real-time (BE-A04, FE-A03)

1. **SignalR**, authenticated by the same cookie session as the API, with antiforgery and origin checks on negotiation (see the auth ADR).
2. **Recipients are resolved at dispatch.** For each event the dispatcher resolves the authorised recipients from persisted building, floor, role and relationship rules (this covers the audience targeting in M6-01). It creates a durable per-recipient notification, then signals only that recipient's `user:{id}` group. There are no building-wide groups, so a stale building membership cannot broadcast to the wrong people.
3. **Pushes are hints.** A push is a generic refresh signal. It includes a resource id only where that resource's existence is authorised for that recipient, and the client refetches through the normal authorised API, which applies object-level checks (M1-05, M1-06, SEC-03).
4. **Connect-time checks:** on connection the server loads the user's current `IsActive` state and assignments from the database and rejects inactive users, rather than trusting claims cached in the cookie.
5. **Revocation across instances.** SignalR caches the principal for the connection's life and does not revalidate it, and a process-local connection registry does not reach connections on other instances. Deactivation and scope or role changes therefore publish a revocation event to **every** API instance (through the backplane or the outbox), and each instance aborts that user's local connections. The client reconnects and is re-evaluated. A maximum connection lifetime and `CloseOnAuthenticationExpiration` bound any gap. A two-instance test proves a deactivated user with a still-valid cookie stops receiving pushes within the agreed bound.
6. **Client behaviour (FE-A03):** push is best-effort; reconnect with backoff, reconcile through a refetch, and fall back to polling. The server does not promise replay. The frontend draft's "targeted refresh" of the affected lists, counts and the notification badge is the intended consumer of a push hint, so the event catalogue (follow-up 4) maps each hint to the data it refreshes.
   - **Path:** the browser reaches the hub through the single-origin reverse proxy described in the auth ADR. Next.js itself is not relied on to proxy WebSockets.
7. **Scale-out design (documented, BE-A04):** a Valkey backplane with sticky sessions, or WebSockets-only clients with `SkipNegotiation`. It is a **candidate** until a version-pinned compatibility test and a two-instance test pass. Azure SignalR Service is documented as the hosted alternative.
8. **Observability (BE-A06):**
   - This design emits job duration and last success, outbox lag (age of the oldest pending message), failed-message count and active connections.
   - The work-order module emits `work_orders_created`, the billing module emits `billing_run_duration`, the caching ADR emits cache-hit ratio, and the auth ADR emits rate-limit rejection and lockout metrics.
   - All are exported to one dashboard with low-cardinality labels.

## Consequences

### Positive

- One coherent reliability model (state predicates, unique keys, idempotent consumers) across jobs, outbox and push.
- No new scheduler dependency or licence obligation.
- Push cannot leak data, and revocation is explicit.
- Valkey is reused rather than adding a service.

### Negative

- We maintain a small scheduler and a dispatcher ourselves.
- Revocation needs a connection registry, which is extra code and state.
- At-least-once delivery needs discipline in every consumer.
- In-host jobs mean API scaling also scales job runners (mitigated by leases and idempotence).

### Follow-up actions

1. Agree with the database ADR owner: unique-constraint approach, claim and row-locking approach, lease table, and transaction behaviour.
2. Verify during implementation (**not yet done**): double-run safety of one job (concurrent acquisition, lease expiry during execution, crash recovery); duplicate outbox delivery and a crash on each side of a provider call; a deactivated user's SignalR connection aborted across two instances; `BackgroundService` behaviour on an unhandled exception; graceful shutdown within the timeout.
3. Verify that the SignalR Redis-protocol backplane package works with Valkey (version pinned), and that its licence and maintenance pass AI-06 (**not verified**; NuGet metadata unavailable).
4. Define the notification event catalogue (which module emits what, and the push event types), and the per-job interval, delay and catch-up table, with the owners of each module.
5. Revisit A2 (worker container) at the first scale or shutdown problem, or if the hosting ADR requires it.
6. Confirm the exact job list and rules against the final M3, M4, M5 and M6 requirements and the Core feature specs. The M3-06 and M4-10 key designs above are proposed readings, not confirmed.
7. Agree metric ownership (work-order, billing and caching modules) so BE-A06's three custom metrics are all delivered.
8. Keep the hosting ADR's API minimum replica count at 1 or more while jobs run in the API host, and verify during implementation that a scheduled job and the outbox dispatcher still run with no incoming traffic (**not yet done**).

## Evidence and verification

- No code was built or run for this draft. Sources are documentation, repository licence files and the requirement pack.
- Microsoft Learn (links resolve, `view=aspnetcore-10.0` unless noted):
  - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services (the default 30-second shutdown timeout)
  - https://learn.microsoft.com/en-us/dotnet/core/extensions/workers
  - https://learn.microsoft.com/en-us/aspnet/core/signalr/authn-and-authz (SignalR caches the user for the connection's life and does not revalidate; cookie authentication; `CloseOnAuthenticationExpiration`)
  - https://learn.microsoft.com/en-us/aspnet/core/signalr/scale (sticky sessions; Azure SignalR Service; Redis backplane)
  - https://learn.microsoft.com/en-us/aspnet/core/signalr/redis-backplane
  - https://learn.microsoft.com/en-us/aspnet/core/release-notes/aspnetcore-10.0 (Server-Sent Events result in Minimal APIs)
- Licences read from repositories: Quartz.NET Apache-2.0 (`license.txt`); Hangfire LGPL-3.0 or a commercial licence (`LICENSE.md`); Polly BSD-3-Clause; dotnet/extensions (resilience packages) MIT.
- Requirement wording (BE-C08, BE-A03 to BE-A06, FE-A03, M3-06, M4-10, M4-11, M5-08, M6-02, M6-05, ARC-09) is from capstone requirements v1.4 as recorded in the working specification (`docs/capstone-spec/`). The backplane list (Azure SignalR Service, Valkey, Dragonfly; not Memcached) is from the same source.
- **Not verified:** NuGet package metadata (TLS failure to `api.nuget.org` on the authoring machine); Valkey compatibility with the SignalR Redis backplane package; `BackgroundService` unhandled-exception behaviour in .NET 10; database-specific claiming and locking.

## AI assistance

GitHub Copilot (Claude) researched the cited documentation and repositories and drafted this ADR. A second AI review pass critiqued earlier versions and its findings were fixed; later edits (four-person scope, alignment with the frontend, architecture, hosting and database drafts) were not separately reviewed. The claims about platform behaviour come from documentation and source reading, and no code was built or run for this ADR, so none is verified by experiment. Verification is tracked as implementation follow-up (see Follow-up actions) and is not a condition of this ADR. Human review is pending and will happen in the pull request.

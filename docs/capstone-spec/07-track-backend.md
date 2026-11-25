---
title: Backend track (BE) — Core and Advanced packages
source_sections: "6 (intro), 6.2, BE-related acceptance criteria"
load_when: "Owning or reviewing anything backend: API design, authN/authZ, validation, transactions, caching, jobs, audit, health/logging, backend tests, concurrency, outbox, real-time, resilience, rate limiting, telemetry."
related: [02-product-m1-m4.md, 03-product-m5-m7-px.md, 08-track-data.md, 10-architecture-tech-policy.md, 11-security-privacy.md]
---

# Backend track (BE)

**Purpose:** implement the business rules as a secure, consistent API that stays correct under concurrent requests and degrades properly when dependencies fail.

**Package rules:** every item in a required package is a MUST unless stated. Substitution needs the jury's written approval. BE Core is required for every team. BE Advanced is required for a team of 4, or when a team of 3 selects it in Week 1.

Table schema: `ID | Level | Scope | Requirement | Evidence`.

## BE Core (≈ 25 h)

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| BE-C01 | MUST | CORE | ASP.NET Core on **.NET 10 LTS** (.NET 11 only after general availability and with an ADR). Choose **controllers or Minimal APIs** and justify it in an ADR (Minimal APIs: expect route groups, endpoint filters, `TypedResults`). Structure the solution as a **modular monolith** with clear module boundaries. | ADR (API style; .NET 11 if adopted); inspectable solution structure showing module boundaries |
| BE-C02 | MUST | CORE | Resource-oriented HTTP API: correct verbs and status codes; consistent pagination, filtering, sorting; **RFC 9457 ProblemDetails for every error**; an API versioning strategy (for example `/api/v1`); **201 Created with a `Location` header** on creation. | API conventions document + code demonstrating them |
| BE-C03 | MUST | CORE | Generate an **OpenAPI document** with schemas, examples and security definitions. Interactive docs via **Scalar or Swagger UI**, **not exposed in the Release environment**. Store and version the OpenAPI file with the source. | Versioned OpenAPI file; URL of the interactive docs in a permitted environment |
| BE-C04 | MUST | CORE | Authentication via **ASP.NET Core Identity** (cookies or bearer) or an **OpenID Connect provider** (for example Microsoft Entra ID or Keycloak). Role-based and policy-based authorization; **resource-based authorization handlers** for object-level checks; **deny by default**. | Authn/authz code + automated authorization tests |
| BE-C05 | MUST | CORE | Request validation (built-in Minimal API validation, FluentValidation, DataAnnotations or equivalent permitted). **HTTP 409 or 422** for domain-rule violations. Centralised exception handling with `IExceptionHandler`. No stack traces or internals in responses. | Code and tests for validation, domain conflicts and sanitised errors |
| BE-C06 | MUST | CORE | Data access with EF Core, Dapper or the DB's official driver. **Explicit transactions** for multi-record operations (example: triage + assignment + history + audit + notification written atomically). Document **connection-pool configuration** (pool size, timeouts, DbContext pooling if used) and how each request obtains and returns a connection. | Design note in `docs/architecture` + data-access/transaction code |
| BE-C07 | MUST | CORE | Cache **at least 2 repeatedly requested reads** (for example floor layouts, tariffs, dashboard aggregates) using HybridCache, `IMemoryCache` or output caching. Explicit invalidation on writes (tags allowed). Cache hits and misses observable in logs or metrics. | Caching + invalidation code; logs/metrics showing hits and misses |
| BE-C08 | MUST | CORE | Implement every scheduled job required by **M3-06, M4-10, M4-11, M5-08, M6-02**: lease expiry, SLA escalation, work-order auto-close, overdue statements, scheduled announcement publish and expiry. Scheduler: `BackgroundService`, Hangfire, Quartz.NET or equivalent permitted. Each job **idempotent**, safe if run twice, logged and observable (last run and outcome). | Job code + job dashboard or logs showing runs and outcomes |
| BE-C09 | MUST | CORE | Capture all audit records required by M7-01, including correlation IDs. An EF Core `SaveChanges` interceptor or database triggers agreed with the DB owner are acceptable. | Audit code + a functioning audit viewer |
| BE-C10 | MUST | CORE | Separate **liveness and readiness** health endpoints (readiness checks the database). Structured **JSON logs** with correlation IDs and no sensitive data. Graceful shutdown. | Health endpoints; structured-log samples |
| BE-C11 | MUST | CORE | Unit tests for domain rules (state machines, billing allocation, lease overlap). Integration tests against a **real database** (for example `WebApplicationFactory` + Testcontainers). Authorization tests **generated from the roles-and-permissions matrix**. | All tests running in CI |

## BE Advanced (≈ 20 h) — all six are MUST when BE Advanced is in scope

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| BE-A01 | MUST | ADVANCED | **Optimistic concurrency** across the whole request flow for **work orders, leases and statements**: ETag with `If-Match`, or explicit version fields; conflicts follow HTTP **412 or 409** semantics. Tests show stale writes cannot overwrite newer data. | Automated tests + API docs describing the concurrency contract |
| BE-A02 | MUST | ADVANCED | **Distributed L2 cache** for HybridCache using **Valkey, Memcached or Dragonfly** via an `IDistributedCache` implementation. Cache-stampede protection, documented key strategy, TTL strategy, tag-based invalidation. Load-test (k6 or Azure Load Testing); compare before/after **latency percentiles and database-call counts**. Reproduce a **connection-pool exhaustion** scenario under load, then fix it. | Report in `docs/performance`: configuration, method, before/after, percentiles, DB-call evidence, exhaustion diagnosis and fix |
| BE-A03 | MUST | ADVANCED | **Transactional outbox** for notifications and integration events; idempotent consumers; payment endpoints accept an **`Idempotency-Key`** header. Tests prove correct behaviour when a message or request is delivered more than once. | Outbox + consumer code; duplicate-delivery and payment-idempotency tests |
| BE-A04 | MUST | ADVANCED | Server-to-client push via a **SignalR hub or Server-Sent Events**, authorised **per user and per building**. Document a scale-out design (Azure SignalR Service, or a Valkey or Dragonfly backplane). Memcached is **not** an approved backplane (no pub/sub). | Working demo + design note on authorization and scale-out |
| BE-A05 | MUST | ADVANCED | Put notifications, file storage and the payment simulator behind **provider abstractions**. Timeouts, retries with jitter and circuit breakers (Microsoft.Extensions.Http.Resilience, Polly or equivalent). **Fault-injection test** showing graceful degradation. | Automated tests + demo of the injected failure |
| BE-A06 | MUST | ADVANCED | **Rate limiting** on sign-in, password reset and other abuse-prone endpoints: **HTTP 429** with a **`Retry-After`** header. **OpenTelemetry** traces and metrics; custom metrics for **work orders created, billing-run duration, cache-hit ratio**; export to a dashboard. | Dashboard screenshots + rate-limit/OTel/exporter configuration |

## Quick numeric cross-check
- Runtime: .NET 10 LTS (.NET 11 only after GA + ADR). Creation response: 201 + `Location`. Domain-rule errors: 409 or 422.
- Cached repeated reads: ≥ 2. Jobs: 5 source requirements (M3-06, M4-10, M4-11, M5-08, M6-02); each job must stay correct if run twice.
- Health: liveness AND readiness; readiness checks the DB.
- Advanced: concurrency conflicts 412 or 409 over 3 record types (work orders, leases, statements); distributed cache choices Valkey/Memcached/Dragonfly; performance evidence = before/after + latency percentiles + DB-call counts + 1 corrected pool-exhaustion scenario; payments need `Idempotency-Key`; real-time authorization at 2 scopes (user, building); rate-limit response 429 + `Retry-After`; 3 custom metrics.

## Backend acceptance criteria (from Section 15 and the product modules)

**Blocking (failing any caps the Team Score at 50)**
- ASP.NET Core (controllers or Minimal APIs) on .NET 10 LTS, or .NET 11 with an ADR.
- M1–M7 implemented; both signature scenarios work end-to-end on Release.
- Four roles with object-level authorization; automated tests prove a resident cannot access another resident's records.
- Runnable release: starts locally with **one documented command** and runs in the Release environment.
- No secrets anywhere in repository history.

**Required (non-blocking)**
- OpenAPI available; all API errors are ProblemDetails; request and domain validation.
- Connection pooling documented; ≥ 2 reads cached; cache invalidation implemented.
- Scheduled jobs (lease expiry, SLA escalation, auto-close, overdue statements, announcement publish and expiry).
- Audit records for important changes; audit viewer; health checks; structured logs with correlation IDs; runbook covers the app.
- Unit, integration, database, component, E2E, authorization and accessibility tests run in CI (for BE: unit, real-database integration, authorization are central).
- Exact money and deterministic allocation proven by tests.
- Only Microsoft products, OSI open source and approved exceptions; main dependencies and licences listed in the README.
- Advanced packages required by team size complete (including BE Advanced if applicable).
- Security controls: threat model, security headers, CSRF protection, restricted CORS, safe uploads, rate-limited sign-in, no tokens in browser storage.

**Behavioural checks the BE implementation and tests must satisfy**
- Authorization: changing an ID in a URL/API call cannot expose or alter another resident's unit, lease, statement or work order; a manager cannot access an unassigned building; a deactivated user cannot sign in while history stays in the audit trail.
- Lease concurrency: activating an overlapping lease fails with a clear validation error, also when two requests race (integration test); occupancy history answers "who lived in unit X on date Y".
- Work orders: Scenario A on Release; every allowed/forbidden transition covered by table-driven tests for every role; no resident-facing endpoint returns an internal work note.
- Billing: Scenario B on Release; allocation unit tests cover leftover cents, vacant units, zero consumption, meter replacement; re-running a preview never duplicates statement lines; issued statements cannot be edited.
- Notifications/announcements: scheduled announcement visible to the intended audience at publish time and gone after expiry without manual action; tests prove residents cannot see another building's announcements.
- Audit/dashboards: dashboard values match direct DB queries on the seed data; the audit trail reconstructs both scenarios.

**Backend package completion gate**
1. Every BE Core row has an implementation and the evidence requested. 2. BE Advanced complete if in scope. 3. API enforces authentication, role checks and object-level authorization on the server. 4. Transactions, concurrency, caching, jobs, audit and connection pooling are demonstrated, not just described. 5. Unit, real-database integration and authorization tests run in CI. 6. Scenarios A and B work end-to-end on the submitted Release version. 7. Every optimization or resilience claim has evidence (logs, metrics, tests, before/after measurements).

## Related requirements outside this track
ARC-01..ARC-10 (10) · SEC-02..SEC-14 (11) · QA-02..QA-06 (12) · DB-C03, DB-C07 (08) · M3-04, M4-03..M4-11, M5-06..M5-09, M6-05, M7-01 (02, 03).

## First tasks `[PACK NOTE]`
1. API style ADR (controllers vs Minimal APIs) and solution/module structure.
2. Auth ADR + sign-in with seeded accounts for the four roles; one protected endpoint per role (M1 slice).
3. ProblemDetails + `IExceptionHandler` + correlation-ID logging from day one (retrofitting is costly).
4. Audit capture from the first write endpoint (M7 slice: "write audit records from the very beginning").
5. Health endpoints and OpenAPI generation wired into CI early.

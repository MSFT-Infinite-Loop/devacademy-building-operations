---
title: Glossary and worked examples
source_sections: "Appendix A (glossary), Appendix H (worked examples H.1–H.5), plus pointers to examples elsewhere in the spec"
load_when: "A term is unclear, or you need an example of the expected level of detail for a user story, ADR, journal entry, release notes or pull request."
related: [02-product-m1-m4.md, 13-ai-assisted-engineering.md, 14-process-git-planning.md, templates/]
---

# Glossary and worked examples

## 1. Glossary (Appendix A)

### 1.1 Domain terms

| Term | Meaning |
|---|---|
| Active work order | A work order in Submitted, Triaged, Assigned, In Progress, On Hold or Reopened status. |
| Allocation rule | How a shared expense is distributed among units: by floor area, occupant count, equal shares, or consumption. |
| Announcement | A manager- or administrator-published message for a particular audience, with publication and expiry times. |
| Audit record | An append-only record of who changed what, when and how, and the result. |
| Billing period | The calendar month for which meter readings are gathered and statements generated. |
| Billing run | The monthly workflow turning readings, tariffs and common expenses into statements: preview, approval, issue. |
| Building | A property managed by the platform, containing floors, units and common areas. |
| Common area | Shared building space (stairwell, basement, elevator, roof) that may be tied to a work order. |
| Common expense | A building-level cost for a period that must be distributed among its units. |
| Household member | Someone residing in a unit through an owner's or tenant's occupancy who may not have their own user account. |
| Lease | A contract allowing a tenant to use a unit for a period. Lifecycle: Draft, Active, Ended, Terminated, Cancelled. |
| Meter / meter reading | A meter measures utility consumption; a meter reading is the value captured from it for a billing period. |
| Notification | An event-generated message belonging to one user, with a read/unread state. |
| Occupancy | The record that a person lived in a unit during a period as owner, tenant or household member. |
| Owner | A person who owns a unit individually or jointly. |
| Resident | A tenant, owner or household member connected with a unit. |
| SLA | Service Level Agreement: the target resolution time for a work order according to its priority. |
| Statement | The monthly document of charges for a unit: totals, due date, payment status. |
| Tariff | The price per consumption unit for a utility over a date range. |
| Technician | A user who performs maintenance work on work orders assigned to them. |
| Tenant | A person renting a unit under a lease. |
| Unit | An apartment or other space that can be owned, rented or occupied. |
| Work order | The managed record that follows a maintenance request through its lifecycle. |

### 1.2 Engineering terms

| Term | Meaning |
|---|---|
| ADR | Architecture Decision Record: a concise record of an important decision with context, alternatives and consequences. |
| Back-merge | Merging `main` back into `preview` after a hotfix so the fix stays in later releases. |
| Backplane | A shared channel letting several server instances deliver real-time messages to all connected clients (BE-A04). |
| BFF (backend-for-frontend) | A server-side web-app layer that holds the user's session and calls the API on the browser's behalf. |
| Cache invalidation | Removing or refreshing cached data after the underlying data changes. |
| Cache stampede | Many requests regenerating the same expired cache entry at once, potentially overwhelming the database. HybridCache protects against it. |
| CI/CD | Continuous Integration: changes are built and tested automatically. Continuous Delivery: successful changes are packaged and released automatically. |
| Code freeze | The pre-release period in which only bug fixes are merged. |
| Connection pool | A managed set of reusable database connections, avoiding a new connection per request. |
| Container / Compose file | A container is an isolated packaged runtime; a Compose file describes several containers started together with one command. |
| Core Web Vitals | User-experience measures: loading (LCP), interaction responsiveness (INP), visual stability (CLS). |
| Correlation ID | An identifier carried through logs and calls of one request so it can be traced end to end. |
| CORS | Cross-Origin Resource Sharing: browser-enforced rules on which sites may call an API. |
| CSR / SSR / streaming SSR | CSR: rendered in the browser. SSR: rendered on the server per request. Streaming SSR: server rendering sent progressively as parts become available. |
| CSRF | Cross-Site Request Forgery: tricking a signed-in browser into sending an unintended request. |
| Definition of Done | The team's shared checklist a work item must satisfy to count as complete (PRC-04). |
| Ephemeral environment | A temporary environment per pull request, removed automatically when the PR closes (OPS-A02). |
| ETag and If-Match | HTTP headers for optimistic concurrency: the client sends the version it edited so the server can reject stale updates. |
| Expand-and-contract migration | Staged schema change: add the new structure, migrate data and code, then remove the old structure (DB-A05). |
| Feature flag | A switch that hides unfinished or risky functionality without a separate branch. |
| Health check (liveness / readiness) | Endpoints showing whether a service runs and whether it can handle traffic, including required dependencies. |
| HybridCache | A .NET caching library combining a local in-process L1 cache with an optional distributed L2 cache; supports stampede protection and tag-based invalidation. |
| Hydration | React turning server-rendered HTML into an interactive page in the browser. |
| IaC | Infrastructure as Code: cloud infrastructure defined in version-controlled files and provisioned by a pipeline. This project uses Bicep. |
| IDOR | Insecure Direct Object Reference: reaching another person's data by changing an identifier. Object-level authorization prevents it. |
| Idempotency | Performing an operation many times has the same effect as performing it once. |
| Index | A database structure that speeds certain queries at the cost of storage and some write overhead. |
| Isolation level | How strongly concurrent transactions are separated (for example Read Committed, Serializable). |
| Kanban board | A board of status columns with cards moving between them (M4-12). |
| Keyset pagination | Pagination that remembers the last item seen (for example date and ID) instead of skipping rows; stays fast on large tables (DB-A03). |
| Migration | A version-controlled script that changes schema or data in a repeatable, controlled way. |
| Object-level authorization | Authorization that considers the user's relationship to the exact record requested, not just their role. |
| Open-source licence (OSI-approved) | A licence accepted by the Open Source Initiative, for example MIT, Apache-2.0, BSD, MPL, LGPL, GPL, AGPL. |
| OpenAPI | A standard machine-readable description of an HTTP API for documentation and client generation. |
| OpenTelemetry | An open standard and tooling for traces, metrics and logs. |
| Optimistic concurrency | Detecting conflicting changes by comparing versions rather than locking records up front. |
| Optimistic UI | Updating the interface before the server confirms, then reconciling or rolling back. |
| Outbox (transactional) | Storing outgoing messages in the same transaction as the business change and dispatching them afterwards. |
| OWASP Top 10 / ASVS | Top 10: list of major web-application security risks. ASVS: detailed application-security requirements checklist. |
| Preview environment | The environment running the newest Preview version, hosted or from the published Preview images. |
| ProblemDetails | The standard JSON error format for HTTP APIs defined by RFC 9457. |
| Rate limiting | Restricting how many requests a client may send in a time window. |
| Release candidate | A build considered ready for release and given final checks, for example `v0.9.0` in the suggested plan. |
| Release captain | The team member, rotating weekly, who prepares and merges that week's release PR. |
| Release environment | The environment running the latest release from `main`, hosted or from published release images. |
| Rendering Strategy Table | A table of each route's rendering method, where it renders, and why (FE-C02). |
| SBOM | Software Bill of Materials: an inventory of all components and dependencies in a release. |
| Seed data | Synthetic data loaded automatically for demos and repeatable tests. |
| Semantic Versioning | `MAJOR.MINOR.PATCH` version numbers, for example `v0.3.0`. |
| Server components | React components that run only on the server and send rendered output to the browser. |
| Server-Sent Events (SSE) | A web standard for a server to push updates to a browser over one HTTP connection. |
| Smoke test | A short automated test that the most important functionality works after startup or deployment. |
| Source-available licence | Allows reading the source but restricts use, so it is not open source (for example BUSL, SSPL, RSAL). Section 7.4 names the two approved exceptions. |
| Spec | A short feature specification written before implementation (AI-03); template D.4. |
| Squash merge / merge commit | Squash: all branch commits become one new commit. Merge commit: joins two histories and keeps both. |
| Stored procedure / function | Executable logic stored in the database and called explicitly. |
| STRIDE | Threat-modelling checklist: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. |
| Trigger | Database logic that runs automatically in response to data changes. |
| Trunk-based development | Frequently integrating small changes into a shared trunk; here `preview` is the trunk. |
| Vertical slice | A narrow but complete feature spanning interface, API and database. |
| View | A stored database query readable like a table. |
| Walking skeleton | The smallest end-to-end implementation of the whole system, built and released early so later work can grow from it. |
| WCAG | Web Content Accessibility Guidelines; core flows target WCAG 2.2 Level AA. |

## 2. Worked examples (Appendix H)
The spec says: copy the **structure** of these examples, not their content. Names such as `@andrei`, `@elena`, `@vlad` are placeholders.

### H.1 User story with acceptance criteria — US-142 "Resident reports a maintenance issue" (M4-01, M4-04, M4-09)
- Persona: Ana, resident of unit 4B. Goal: report a problem with a photo so the Building Manager can act quickly.
- **Happy path (Given/When/Then):** Ana is signed in as the resident of 4B → submits a request: Plumbing, High, one photo → a work order is created in **Submitted**, due **24 hours** later, at the top of Ana's list → Mihai (manager of Aurora Residence) receives a notification.
- **File validation:** a **12 MB** photo is rejected with the message that each photo must be **5 MB or smaller**; nothing is persisted.
- **Authorization:** Ana tries to submit for unit **7A** (not hers) → API returns **403**; no work order is created.
- Estimate 5 h · owner `@andrei` · packages FE-C05 and BE-C05.

### H.2 ADR — ADR-003 "Use PostgreSQL as the database"
- Status Accepted · 2026-11-12 · author `@elena`.
- **Context:** heavily relational domain (units, leases, readings, statements); money must reconcile exactly; "no overlapping active leases" should be protected in the database as well as in application logic.
- **Decision:** PostgreSQL container for development and CI; Azure Database for PostgreSQL Flexible Server (smallest tier) for the hosted Release.
- **Alternatives:** SQL Server (strong tooling and temporal tables, heavier container image); Azure Cosmos DB (flexible documents and change feed, but no foreign keys or exclusion constraints, pushing billing and lease invariants into application code).
- **Consequences:** + a PostgreSQL **exclusion constraint** directly enforces M3-04; + open source, runs locally for free; − DB-A01 temporal history needs triggers; − the team must learn PL/pgSQL.
- **AI usage:** Copilot Chat compared the options; the exclusion-constraint approach was verified with an **integration test** before the ADR was adopted.

### H.3 AI Engineering Journal entry (2026-11-20, #142, BE-C05)
Tool: GitHub Copilot, agent mode in VS Code. Goal: "submit request" endpoint with validation and integration tests. Context: `docs/specs/work-orders.md` + repo instructions. Outcome: **modified**. Usable: endpoint and validator. Rework: two tests rewritten. Verification: run tests, then deliberately break validation.
Problems found: **one AI-generated test still passed with validation broken** (not testing the behaviour); an unnecessary package was introduced; the AI **trusted the client-reported file size** instead of checking the uploaded stream.
Time: saved ≈ 1.5 h, ≈ 30 min correcting. Lesson: ask for **tests first**, then the implementation; check every new dependency under AI-06 / ARC-10.

### H.4 Weekly release notes — v0.4.0, Week 5, captain `@vlad`
Highlights: floor map v1 with keyboard navigation and list view (M2-04, M2-05); lease activation with overlap check (M3-03, M3-04). Plan status: on track for "Foundation complete" in Week 5; CSV export moved to Week 7. Work items: #131, #134, #138, #142, #145. DB change: migration `20261204AddLeaseExclusionConstraint` (additive). Preview evidence: CI run #88 green, smoke tests passed, screenshots in the PR. Known issue: on small screens the map tooltip overlaps the legend (#151). Rollback: redeploy the v0.3.0 images; the migration is additive so no data rollback is needed.

### H.5 A good pull request — `feat(work-orders): validate status transitions on the API`
Prevents bypassing the state machine, for example Submitted → Resolved, for every role; implements M4-02 and M4-03; work item #157; type feature. Tests: table-driven, every allowed and forbidden transition for each role; manual check as Ioana via the API docs UI: Submitted → Resolved returns **409 ProblemDetails**. Database: none. Security: verifies the technician is actually **assigned** to the work order (M1-05). AI disclosure: **Material** — Copilot agent mode generated the test table from the spec; the human added the role column, corrected two wrong expectations, and deliberately removed individual transition rules to confirm the matching test fails. Checklist: CI green ✔, docs/ADR updated ✔, no secrets ✔, accessibility N/A (no UI), effort logged ✔.

## 3. Other examples in the spec (kept in their topic files)

| Example | Where in this pack |
|---|---|
| Money rounding and allocation rule | 03 (M5-07) |
| API request examples and the RFC 9457 error example | 10 §5 |
| Work-order transition table | 02 (M4) |
| Scenario A request flow | 10 §4 |
| Technical-interview examples | 15 §5 |
| Floor layout JSON and map legend | 02 (M2) |

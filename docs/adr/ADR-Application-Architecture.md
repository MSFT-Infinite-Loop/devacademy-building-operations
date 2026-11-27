# ADR-00N: Application Architecture - Module Boundaries and Workflows

- **Status:** Proposed
- **Date:** 2026-11-23
- **Author(s):** Carlos Natera
- **Requirement IDs:** `ARC-01` to `ARC-04`, `ARC-06`, `M1-02`, `M1-03`, `M1-05`, `M2-02`, `M3-01`, `M3-05`, `M7-01` to `M7-05`, `BE-C06`, `BE-A03`, `DB-A01`
- **Supersedes:** None
- **Superseded by:** None

## Context

The capstone sets a modular monolith as the baseline. This ADR defines the logical boundaries inside it: what each module owns, how modules depend on one another, and who leads workflows that cross those boundaries. The backend owns business rules, and the web app, including server-rendered code, accesses persistent data only through the API.

This ADR does not choose the backend stack, project or folder structure, API style, database, authentication approach, caching, worker placement, real-time mechanism, or hosting.

## Decision drivers

- Keep Core requirements easy to trace to code and evidence.
- Give each business fact and rule one authoritative owner.
- Support cross-module workflows without circular dependencies or duplicated business rules.
- Preserve scoped access, auditable changes, reliable notifications, and exact billing.

## Options considered

| Question | Preferred option and advantage | Alternative and trade-off |
|---|---|---|
| Module boundaries | Keep seven logical modules, one per Core area, for straightforward traceability. Keep Audit and Reporting distinct inside M7 so the shared boundary does not hide their different responsibilities. | Split Audit and Reporting into separate modules. That makes their dependency direction clearer but adds a boundary. The spec does not prohibit the split. |
| Person ownership | Keep person identity and contact details in M1, separate from accounts and grants. One module can correct those details even for people who never sign in. | Put person records in M3, close to occupancy workflows. That would make account onboarding depend on M3 rather than keeping person details and account management together. |
| Cross-module dependencies | Allow one-way lookups through module contracts and coordinate multi-module reads where needed. Simple lookups stay simple, but the dependency direction needs review. | Coordinate every cross-module interaction outside the modules. That makes dependencies visible but adds indirection even to simple lookups. |
| Workflow ownership | Let the module that owns the outcome lead. Share audit and outbox mechanics without sharing business logic. | Put every cross-module write in a separate handler. That can clarify workflows with no obvious owner, but it moves straightforward actions away from the modules that own them. |

## Decision

Use seven logical modules mapped one-to-one to M1-M7. These are ownership boundaries, not seven services, databases, or projects.

**Keep technical responsibilities separate (`ARC-02`).** The web app presents the UI, API handlers receive requests and delegate to application use cases, and domain code owns business rules. Persistence, integration adapters, and shared functions such as audit recording support those use cases without owning their business rules.

| Module | Owns |
|---|---|
| **M1 - Identity and Access** | Person records, accounts, and role grants as distinct concepts. A person need not have an account. |
| **M2 - Buildings and Map** | Buildings, floors, units, layouts, and manager-set availability. M2 owns the rules that combine those with M3 occupancy and M4 work-order facts into map status. There is no separately editable map status. |
| **M3 - Occupancy** | Ownership, leases, household membership, and occupancy and lease history. Person-management workflows use M1 rather than maintaining a second person record. |
| **M4 - Maintenance** | Work orders, assignments, transitions, SLA rules, and work-order history. |
| **M5 - Billing** | Meters, readings, tariffs, billing runs, statements, and simulated payments. Billing also owns historical tariff and statement versions. |
| **M6 - Communications** | Announcements and the durable notification inbox. |
| **M7 - Audit and Reporting** | The append-only record of business actions, dashboards, and exports. Audit is distinct from historical record versions owned by M3 and M5. Reporting may consume authorized audit summaries; audit capture and inspection do not depend on reporting. |

**Use explicit contracts and avoid circular dependencies.** M3 can look up a unit through M2's contract. For the floor map, a backend use case can gather facts from M2, M3, and M4 and use M2's status rules without introducing a reverse dependency from M2 to M3. Modules do not reach into one another's internal code or storage.

**Enforce access at the API boundary.** M1 supplies the account and scoped role grants; M3 supplies a resident's relationship to a unit through ownership, a lease, or household membership. The API checks both through module contracts. A Resident role grant alone does not establish that relationship, and M1 does not need to depend on M3. The [Authentication and Authorization proposal](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/23) covers how the API implements those checks.

**Let the module that owns the primary business action lead the workflow.** If it needs another module's result to finish, use that module's contract. If a separate action can happen afterward, the originating workflow need not wait for it. For the 4B leak, M4 leads the work-order action. Shared mechanics commit the work order, required history, audit record, and outbox entry together. After commit, M6 creates the manager's inbox notification, and delivery can be retried without creating duplicates. Use a separate coordinator when there is no clear workflow owner or when a direct call would create a cycle, not merely because the workflow involves audit or notifications.

## Consequences

- **Positive:** Each rule has a clear home, and workflows reuse audit and outbox mechanics without sharing a central business handler.
- **Negative:** Cross-module work needs explicit contracts and dependency discipline. M3 relies on M1 for person operations, even for people who never sign in.
- **Follow-up actions:** Agree how the Backend and Database ADRs will enforce the boundaries and atomic writes. Align ownership of historical records with the database model without prescribing where the tables live. Document the required C4, deployment, and data-model views and the Scenario A sequence separately.

## Evidence and verification

- The proposal was checked against the [architecture requirements](../capstone-spec/10-architecture-tech-policy.md), [backend requirements](../capstone-spec/07-track-backend.md), and [signature scenarios](../capstone-spec/04-product-scenarios-roles-domain.md) in the working specification.
- **Pending:** Review the dependency map for cycles. For the 4B leak, prove that a failed write leaves no partial change and a delivery retry produces one manager inbox entry. For month-end billing, verify that totals reconcile exactly and retrying a simulated payment does not apply it twice. No implementation tests were run.

## AI assistance

GitHub Copilot helped compare alternatives and draft this record. The rationale and requirements mapping still need independent team review before acceptance.

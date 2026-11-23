---
title: Product requirements M5–M7 and cross-cutting PX (billing, notifications, audit/dashboards)
source_sections: "4.5, 4.6, 4.7, 4.8"
load_when: "Implementing or reviewing meters/billing/payments, announcements/notifications, audit trail/dashboards/exports, or any cross-cutting product rule (pagination, UTC, money, seed data, language)."
related: [02-product-m1-m4.md, 04-product-scenarios-roles-domain.md, 07-track-backend.md, 08-track-data.md]
---

# Product requirements M5–M7 and PX

Scope of everything here: **CORE**. Table schema: `ID | Level | Scope | Requirement | Evidence`. Module acceptance criteria follow each table.

## Thin first slices

| Module | Thin first slice | Then add |
|---|---|---|
| M5 Billing | One utility, its meter readings, one tariff, and a billing preview for one building. | Common expenses with at least two allocation rules, approval and issuance, payments, the overdue-processing job. |
| M6 Notifications | An in-app notification when a work order changes. | Announcements with targeting and scheduling, unread badge, notification history, preferences. |
| M7 Audit and dashboards | Write audit records automatically from the very beginning. | Audit viewer, role-specific dashboards, CSV export. |

## M5 — Utility meters, monthly charges and payments

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| M5-01 | MUST | CORE | Manage meters: utility type (cold water, hot water, electricity, gas, heating), serial number, scope (a specific unit, or the building/common areas), unit of measure (for example m³, kWh), installation date, removal date. | — |
| M5-02 | MUST | CORE | At most one reading per meter per billing period. Residents submit readings for meters of their own unit (a self-reading, may include a photo). Building Managers can also submit readings. | — |
| M5-03 | MUST | CORE | A new reading cannot be lower than the previous one unless a meter-replacement record exists. Plausibility check: consumption above a configurable threshold is flagged for manager review (suggested example: 3× the unit's recent average). Correcting a reading requires a reason; every correction is audited. | — |
| M5-04 | MUST | CORE | Tariffs per building and per utility, with an effective date range, a price per unit consumed and a currency. | — |
| M5-05 | MUST | CORE | Common building expenses per building and billing period (cleaning, elevator maintenance, common-area electricity, administration fees). Each has an allocation rule: by unit area (m²), by number of occupants, equally per unit, or by consumption. Implement at least two rules. | — |
| M5-06 | MUST | CORE | Monthly billing run per building and billing period: Preview → Approve → Issue (MAY: approve and issue combined in one action). Statement content = individual consumption × applicable tariff + the unit's allocated share of every common expense. Re-running a preview replaces the existing preview (idempotent; no duplicate lines). Every statement has a due date, configurable per building, default 30 days after issuance. Issued statements are immutable; corrections use adjustment lines or credit notes, each with a reason. | — |
| M5-07 | MUST | CORE | Exact money: decimal types only, never floating point. Allocation is deterministic and the allocated amounts sum exactly to the source amount. Default rule: calculate at full precision; round each line to 2 decimal places, half-away-from-zero; assign leftover cents to the units with the largest fractional remainders. MAY use another documented rule that is still exact and deterministic. | — |
| M5-08 | MUST | CORE | Statement state machine: Draft → Issued; Issued → Partially Paid; Partially Paid → Paid; Issued → Paid (full settlement); Issued → Overdue; Partially Paid → Overdue; Overdue → Paid (remaining balance settled); Issued → Cancelled (Building Manager, with a reason). A scheduled job moves eligible statements to Overdue after the due date; a partially paid statement past its due date stays Overdue until fully settled. | — |
| M5-09 | MUST | CORE | Payments are simulated (no real funds). Managers record amount, payment date, method and reference. MAY: residents get a "Pay (simulation)" action through a fake payment-provider abstraction. Partial payments supported; a payment cannot exceed the outstanding balance; applying a payment is idempotent (idempotency key or unique payment reference). | — |
| M5-10 | MUST | CORE | Residents view their statements, line details, current outstanding balance, payment history and a consumption chart for the previous 12 months. | — |
| M5-11 | SHOULD | CORE | A configurable reminder job notifies residents who have not submitted required readings a set number of days before the billing period closes. | — |
| M5-12 | MAY | CORE | Late fees using a configurable daily rate. | — |

**M5 acceptance criteria**
- Scenario B works end-to-end on the Release environment.
- Unit tests demonstrate correct allocation, including distribution of leftover cents, vacant units, zero consumption and meter replacement.
- Re-running a billing preview for the same period does not duplicate statement lines.
- Issued statements cannot be edited.

## M6 — Announcements and notifications

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| M6-01 | MUST | CORE | Building Managers create announcements for assigned buildings; Administrators for all. Fields: title; rich-text body (**sanitized on the server**); category (Outage, Maintenance, Meeting, General, Urgent); audience targeting by building, floor and role; publish time; expiry time; pinned flag. | — |
| M6-02 | MUST | CORE | Lifecycle: Draft → Scheduled → Published → Expired → Archived. Immediate publishing skips Scheduled. Scheduled publishing and expiry are performed by scheduled jobs. | — |
| M6-03 | MUST | CORE | Residents and Technicians see only announcements targeted to them. The list supports filtering and pagination. | — |
| M6-04 | MUST | CORE | In-app notification centre for event-driven notifications about work orders, statements, leases, announcements and meter readings: unread-count badge, mark as read, mark as unread, mark all as read, paginated history. | — |
| M6-05 | MUST | CORE | A notification is created reliably together with the business change that triggered it: either in the same transaction, or via a transactional outbox (BE-A03). | — |
| M6-06 | SHOULD | CORE | Notification preferences per category; critical categories cannot be disabled. | — |
| M6-07 | SHOULD | CORE | Aggregate "seen by" counts for announcements. Must not expose who read it or individual reading behaviour. | — |
| M6-08 | MAY | CORE | Email or SMS through a provider abstraction. If implemented: sandbox services only (for example a local SMTP catcher); the application MUST keep working when the provider is unavailable. | — |

**M6 acceptance criteria**
- A scheduled announcement becomes visible to the correct audience at its publication time and disappears automatically after expiry — no manual intervention.
- A resident in one building cannot see announcements of another building — proven by an automated test.

## M7 — Audit trail, dashboards and reporting

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| M7-01 | MUST | CORE | Audit records for important changes: sign-in events, role changes, leases, work-order transitions, meter readings and corrections, billing runs, statements, payments, announcements. Each record captures: actor, UTC timestamp, entity type, entity ID, action, before/after values (or a structured change set), outcome (Success or Failure), correlation ID. | — |
| M7-02 | MUST | CORE | Audit records are append-only from the application's perspective: no path to update or delete. Administrators see all records; Building Managers only records relating to their assigned buildings. | — |
| M7-03 | MUST | CORE | Audit viewer with entity, actor, action and date-range filters and server-side pagination. | — |
| M7-04 | MUST | CORE | Role dashboards (contents below). | — |
| M7-05 | MUST | CORE | At least one CSV export (example: outstanding balances per unit). Every export enforces authorization and never exposes records outside the user's scope. | — |
| M7-06 | SHOULD | CORE | Every chart has an accessible alternative (a textual summary or a data table with the same information). | — |
| M7-07 | MAY | CORE | Statements as PDF. | — |

**M7-04 dashboard contents**

| Role | Must show |
|---|---|
| Building Manager | Occupancy per building; open work orders by status and by priority; SLA breaches; work-order ageing; outstanding balances; leases expiring within 30, 60 and 90 days; missing readings for the current period. |
| Technician | Assigned queue; work due today; overdue work. |
| Resident | Own unit; open maintenance requests; latest statement; current balance; latest announcements. |
| Administrator | Users by role; buildings overview; background-job health; recent audit activity. |

**M7 acceptance criteria**
- Dashboard figures agree with direct database queries against the seed data (a documented comparison or an automated test).
- The audit trail reconstructs the complete history of Scenario A (maintenance) and Scenario B (month-end billing).

## PX — Cross-cutting product requirements (apply to the whole product)

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| PX-01 | MUST | CORE | Every list that can become large uses **server-side pagination**; data-heavy lists support search, filtering and sorting (units, persons, work orders, statements, audit records are named explicitly). | — |
| PX-02 | MUST | CORE | Every data view handles all four states: loading, empty, error, success. | — |
| PX-03 | MUST | CORE | Validation on both client and server, with consistent field-level messages across the two layers. | — |
| PX-04 | MUST | CORE | Dates and times stored in **UTC**, displayed in the user's time zone (default **Europe/Bucharest**); the API uses **ISO 8601**. | — |
| PX-05 | MUST | CORE | Money stored as decimals; every amount has an explicit **currency code** (default **RON**); consistent formatting everywhere. | — |
| PX-06 | MUST | CORE | Business records that carry history are archived or deactivated, not deleted. Hard deletion only where documented (certain drafts; records removed for a valid privacy erasure). | — |
| PX-07 | MUST | CORE | Destructive or irreversible actions require confirmation; every important action gives clear feedback. | — |
| PX-08 | MUST | CORE | **Synthetic, reproducible, realistic seed data:** at least 2 buildings, 60 units, 100 persons, 12 months of meter readings, 12 months of statements, 300 work orders spread across all work-order states. Documented demo accounts for every role. Must include Aurora Residence, unit 4B, the scenario personas, and all data needed to replay Scenarios A and B. | — |
| PX-09 | MUST | CORE | English for interface text, code, code comments, documentation, commit messages, PRs and work items. Bilingual English/Romanian is optional extension X6, not Core. | — |

## Related requirements to read with this file
- Jobs for M5-08, M6-02: BE-C08 (07). Outbox and idempotency: BE-A03 (07). Statement/lease optimistic concurrency: BE-A01 (07).
- Money and rounding tests: BE-C11 (07), QA-04 (12). Audit capture: BE-C09 (07). Reporting layer: DB-A02 (08). Temporal history: DB-A01 (08).
- Uploads (photos): SEC-07 (11). Privacy: SEC-13 (11). Scenario B: 04 §5.2.

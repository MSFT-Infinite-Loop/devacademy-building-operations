---
title: Data track (DB) — Core and Advanced packages
source_sections: "6 (intro), 6.3"
load_when: "Owning or reviewing the data model, constraints, migrations, seed data, indexing, stored procedures/triggers/views, transactions/isolation, backup/restore, temporal history, reporting layer, performance lab, privacy/retention."
related: [04-product-scenarios-roles-domain.md, 07-track-backend.md, 11-security-privacy.md]
---

# Data track (DB)

**Purpose:** protect data integrity and database performance; treat the database as the **final enforcement layer** for key invariants.

**Package rules:** every item in a required package is a MUST unless stated. Substitution needs the jury's written approval. DB Core is required for every team. DB Advanced is required for a team of 4, or when a team of 3 selects it in Week 1.

Table schema: `ID | Level | Scope | Requirement | Evidence`.

## DB Core (≈ 20 h)

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| DB-C01 | MUST | CORE | Document the database decision in an **ADR comparing SQL and NoSQL**: consistency requirements, query patterns, team skills, engine, hosting. | ADR |
| DB-C02 | MUST | CORE | **ERD** for SQL, or a document/access-pattern model for NoSQL, covering M1–M7, with a **data dictionary**. SQL: 3NF where appropriate; document intentional denormalization/embedding. | `docs/architecture` diagrams + data dictionary |
| DB-C03 | MUST | CORE | Enforce integrity with SQL constraints or NoSQL schema validation/indexes. The M3-04 lease-overlap rule is protected by the database or by a concurrency-safe transaction. | Migration scripts + tests |
| DB-C04 | MUST | CORE | **Versioned migrations**, validated automatically in CI against a disposable DB; **reproducible synthetic seed data** (PX-08); documented migration naming and review rules. | Pipeline + seed scripts |
| DB-C05 | MUST | CORE | Define indexes for the **10 most important query patterns** and justify them; at least **2** with before/after execution plans. | Indexing note + plans |
| DB-C06 | MUST | CORE | Programmable DB objects. SQL: at least **2 stored procedures/functions, 1 view and 1 trigger**, all automatically tested. NoSQL: the equivalents in the table below. | Scripts + DB tests |
| DB-C07 | MUST | CORE | Identify operations that need atomicity; document the chosen **isolation level** and rationale, with implementation and tests. | Design note + tests |
| DB-C08 | MUST | CORE | Backup policy and a **restore drill into a fresh environment**, validated with counts/checksums plus an application smoke test. | `docs/operations` drill report |
| DB-C09 | MUST | CORE | **Least-privilege application login** (never DB owner/admin); credentials from a secret store; TLS where supported. A separate migration identity SHOULD be used. | Configuration + documentation |

## DB Advanced (≈ 20 h) — all six are MUST when DB Advanced is in scope

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| DB-A01 | MUST | ADVANCED | **Temporal/history** capability for leases, tariffs and statements, including **"as of" queries**. SQL Server/Azure SQL: system-versioned tables; PostgreSQL: trigger-maintained history tables. | Scripts + tests |
| DB-A02 | MUST | ADVANCED | **Reporting layer**: materialized/indexed views or summary tables refreshed by a job, plus window-function trends (for example monthly consumption, arrears buckets). | Scripts + dashboard |
| DB-A03 | MUST | ADVANCED | **Performance lab** with at least **1,000,000 meter readings** and **100,000 work orders**: inspect plans, tune indexes, compare **offset vs keyset pagination**, document conclusions. | `docs/performance` report |
| DB-A04 | MUST | ADVANCED | Reproduce and correct a **race condition** (constraints/isolation/locking) and investigate one **deadlock** scenario. | Report + tests |
| DB-A05 | MUST | ADVANCED | Demonstrate a **zero-downtime expand-and-contract** schema change through the pipeline, with a rollback or forward-fix strategy. | Migration scripts + pipeline |
| DB-A06 | MUST | ADVANCED | **Privacy/retention**: anonymization of former residents while preserving financial and audit integrity; a retention job for expired data. | Scripts + tests |

## SQL and NoSQL equivalents

| Topic | SQL | NoSQL |
|---|---|---|
| Integrity | PK/FK, unique, check, not-null; PostgreSQL exclusion constraints where applicable | JSON Schema validation, unique indexes, domain-layer invariants |
| Programmable logic | Procedures, functions, views, triggers | Aggregation pipelines/materialized views; Cosmos DB procedures/triggers/UDFs; change-stream/feed processors |
| Relationships | Foreign keys + joins | Explicit embedding-vs-referencing decision based on access patterns |
| Transactions | ACID transactions with a chosen isolation level | Multi-document transactions/transactional batches, idempotent writes, optimistic concurrency |
| Migrations | Versioned migration scripts | Schema versioning with migration scripts, or lazy migration on read |
| Performance | Execution plans + index tuning | `explain()`/query metrics, indexing policies, partition-key design, RU/resource analysis |
| History/audit | Triggers + temporal tables | Change streams/feed into history/audit collections |

**Important (spec):** the domain is fundamentally relational — units, leases, readings and statements are heavily interconnected and billing must reconcile exactly. NoSQL remains permitted, but the ADR must explain how invariants such as lease overlap and exact billing will hold without relational FK/join guarantees.

## Related requirements outside this track
M3-04 (lease overlap) · M5-07 (exact money) · M7-02 (append-only audit) · PX-04..PX-06, PX-08 (UTC, money, archiving, seed data) · BE-C06 (transactions, pooling) · BE-C09 (audit via interceptor or triggers agreed with the DB owner) · SEC-13, SEC-14 (privacy, least privilege) · QA-06 (backup/restore) · OPS-C03 (migration validation in CI).

## First tasks `[PACK NOTE]`
1. Database ADR (DB-C01) — decide early; the spec warns a late DB change costs more effort than it saves.
2. Data model v0 / ERD and a data dictionary listing every personal field with its purpose (feeds SEC-13).
3. Migration tooling and naming rules; disposable-DB validation in CI.
4. Seed generator plan for PX-08 (≥ 2 buildings, 60 units, 100 persons, 12 months of data, 300 work orders, Aurora/4B/personas).
5. Decide how lease overlap (M3-04) will be enforced: database constraint vs transaction.

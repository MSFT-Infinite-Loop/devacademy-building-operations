---
title: Quality — testing and operability (QA)
source_sections: "9 (QA-01..QA-09), test-level checklist, Section 15 quality items"
load_when: "Planning the test strategy, deciding what to test at which level, setting up CI quality gates, or preparing health/logging/runbook/backup evidence."
related: [06-track-frontend.md, 07-track-backend.md, 08-track-data.md, 09-track-devops.md, 15-deliverables-assessment-acceptance.md]
---

# Quality — testing and operability (QA)

## 1. In short
- Concentrate testing on the highest-risk areas: **state machines, money, authorization, concurrency.**
- **Do not chase a coverage percentage.** All tests run in CI; any failure blocks merging.
- Make the app operable: **health checks, structured logging, end-to-end correlation IDs.**

## 2. Requirements

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| QA-01 | MUST | ALL | A **risk-based test strategy** in `docs/testing`: what is covered at each level, what is deliberately not tested and why, and how to run tests locally and in CI. | Versioned test strategy |
| QA-02 | MUST | ALL | Implement every prescribed test level: unit, integration, database, UI component, end-to-end, authorization, accessibility, post-deployment smoke (see §3). | Test projects/suites for every level, visible in CI |
| QA-03 | MUST | ALL | All automated tests run in CI; a failing test **blocks merging**. Track and repair flaky tests — do not disable, ignore or silently skip them. | Required CI checks; failed-merge evidence; flaky-test work items; no unexplained skips |
| QA-04 | MUST | ALL | **No required coverage percentage.** Coverage reporting is optional (visibility only). Credibility comes from strong coverage of state machines, money and rounding, authorization and concurrency. | Risk-to-test mapping; meaningful tests of the named high-risk rules |
| QA-05 | MUST | ALL | Enable .NET nullable reference types and analyzers, TypeScript strict mode, and formatter/linter checks in CI. No commented-out code. Every `TODO` references a work item. | Repo config; CI quality-gate runs; code inspection |
| QA-06 | MUST | ALL | Health endpoints; structured logs; **correlation IDs propagated from the web app through the API to database activity**; background-job monitoring; an operational runbook; a demonstrated **backup-and-restore drill**. | Health results; logs showing one correlation ID across layers; job status/logs; `docs/operations/runbook.md`; restore-drill report |
| QA-07 | SHOULD | ALL | OpenTelemetry traces, metrics and logs. Local inspection (for example the Aspire dashboard) and deployed telemetry where applicable. Full deployed setup is part of OPS-A03. | OTel config; local screenshots/exports; dashboards if OPS Advanced |
| QA-08 | MUST | ALL | Back **every claimed optimization** (caching, indexing, streaming, …) with **before-and-after measurements**. No invented target in place of evidence. | Reproducible baseline and optimized measurements with method, environment, result |
| QA-09 | MUST | ALL | Apply the shared **Definition of Done** to every user story (see 14 §7). | Work-item/PR checklists; Preview verification; CI/security results; docs; telemetry; linked effort records |

## 3. Mandatory test levels (QA-02)

| Test type | What must be demonstrated | Suggested tools | Evidence |
|---|---|---|---|
| Unit | Domain rules: state machines, financial allocation and rounding, lease overlap, validation; positive, negative and boundary cases | xUnit/NUnit/MSTest; Vitest | Suites passing in CI |
| Integration | API against a **real database**: endpoints, transaction boundaries, ProblemDetails responses, caching and invalidation | `WebApplicationFactory`, Testcontainers | CI run against a disposable real DB |
| Database | Constraints, procedures/functions, triggers, views, migrations | tSQLt, pgTAP, or DB integration tests | DB tests + migration validation in CI |
| Component (UI) | Components, forms, the data-driven 2D map, optimistic-update rollback | React Testing Library, Vitest | Suite in CI exercising failure and rollback paths |
| End-to-end | **Scenario A and Scenario B**, plus sign-in and role-based smoke paths | Playwright | Tests in CI against an integrated or deployed app |
| Authorization | Every supported role × every protected operation; IDOR attempts; table-driven | integration tests | Permissions-matrix-derived test table; denial tests; CI results |
| Accessibility | No critical violations; keyboard-only and screen-reader paths; WCAG 2.2 AA for core flows | axe-core within Playwright + manual checks | Axe results in CI; manual report in `docs/testing` |
| Post-deployment smoke | Smoke tests for **every new Preview and Release version**, hosted or started from published images | Playwright or pipeline HTTP checks | Pipeline history for each published version |

## 4. Operability checklist
- [ ] Health: separate liveness and readiness endpoints; readiness checks the database.
- [ ] Logging: structured JSON, no sensitive data, correlation IDs.
- [ ] Correlation ID propagates web app → API → database work/logs.
- [ ] Jobs: last run and outcome visible via logs or a job dashboard.
- [ ] Runbook: local setup, environments/URLs, deployment, rollback, reset/reseed, backup/restore, common failures.
- [ ] Backup/restore: documented policy; restore into a fresh environment; verify with row counts or checksums plus an application smoke test.
- [ ] Performance claims keep before/after results.
- [ ] OpenTelemetry: recommended in Core; expected with OPS-A03.

## 5. Acceptance items (Section 15)
- **Blocking:** CI on every PR with build, lint, tests, migration validation and container build · components containerized, images published for every merge into `preview` and every release, every version smoke-tested (hosted Preview and Release required when OPS Advanced is in scope) · no secrets in repository history.
- **Required:** dependency/source/container scans with triaged findings · unit, integration, database, component, E2E, authorization, accessibility tests all run in CI · health checks, structured logs with correlation IDs, runbook · backup-and-restore drill with evidence (report, counts/checksums, smoke result).

## 6. Scoring link
Category D (DevOps, testing and operability) = **15 points** of the Team Score; category B (architecture, security, data) = **20**. See 15 §6.

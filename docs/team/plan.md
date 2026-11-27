# Infinite Loop Project Plan

- **Product:** Infinite Loop Building Operations Platform
- **Status:** Draft for team review; not approved.
- **Last updated:** 2026-11-27
- **Work item:** [#3 - Approve the project plan](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/3) (PRC-05)
- **Official Week 1:** Started 2 November 2026. **Actual team start:** 23 November 2026 (official Week 4).
- **Release day:** Thursday. **Targets:** `v0.1.0` on 10 December 2026 and `v1.0.0` on 21 January 2027, both conditional on passing release checks.
- **Submission:** End of official Week 12 (18-24 January 2027 if weeks run consecutively). Aim to submit by 22 January; the exact cutoff time and time zone still need confirmation. No break, waiver, or extension is assumed.

The [working specification](../capstone-spec/README.md) guides this plan; the official DevAcademy requirements take precedence. This draft reflects the 27 November [Team Charter proposal (PR #30)](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/30), tracked in [#2](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/2). It does not record approval of the Charter, plan, or any architecture choice.

## Status on 27 November

[PR #18](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/18) merged the requirements pack and governance templates into `preview` on 25 November, not the completed Charter or plan. The 26 November release slot passed without a release PR. At this snapshot, `preview` (`af9698e`) had no runnable application and `main` (`37afe63`) was still the initial scaffold. GitHub reported neither branch protected and no repository Actions runs. The 10 December release target is at risk.

## Scope and package ownership

Deliver M1-M7, both signature scenarios as automated end-to-end tests on Release, and all four Core and four Advanced packages. OPS Advanced makes hosted Preview and Release mandatory. Defer optional extensions; the revised schedule does not remove mandatory scope.

| Track | Core and Advanced owner in the Charter draft | Main deliverables and dependencies |
|---|---|---|
| Frontend | Carlos Natera | Role-specific screens, accessible map and list, forms and rendering strategy, streaming and live interactions. Depends on API contracts, seed and layout data, and the agreed auth and deployment topology. |
| Backend | Petar Ivanov | Modular API, resource authorization, domain workflows, jobs, audit, caching, and OpenAPI. Depends on data contracts and on the agreed deployment, telemetry, and real-time design. |
| Data | George Neagoe | Data model, migrations, synthetic seed, integrity constraints, reporting, historical queries, performance and restore evidence. Depends on API use cases and CI migration checks. |
| DevOps | Didier Gbenou | Branch policies, CI, containers, image publishing, scans, hosted environments, release and rollback automation, monitoring, and runbook. Depends on runnable artifacts and documented health and migration behavior. |

These are package assignments, not assignments to lead a cross-track milestone, risk, or escalation. Record the approved assignments in the [Team Charter](charter.md) and `CODEOWNERS`. Frontend and Backend have reported weekly capacity in the Charter proposal; Data and DevOps capacity and everyone's working windows still need confirmation. Confirm release and technical coverage in Teams without publishing personal scheduling details.

## Open pull requests into `preview`

This is the review snapshot for 27 November, not the accepted stack. Record accepted choices in the [decision register](decision-register.md) with their ADRs.

| Decision or workflow | PR | What is proposed or in review |
|---|---|---|
| Team Charter | [#30](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/30) | Draft work agreements, package assignments, daily meetings, and Thursday captain rotation. Capacity, coverage, journal locations, and four sign-offs remain open. |
| Frontend framework | [#26](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/26) | Next.js 16+ App Router, React 19.2+, and strict TypeScript. |
| Application boundaries | [#27](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/27) | Seven logical modules in a modular monolith, not seven services. |
| API style and conventions | [#20](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/20) | Versioned ASP.NET Core Minimal APIs by module and shared error conventions. GitHub shows an approving review; the PR is open and the ADR still says Proposed. |
| Database and data model | [#29](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/29) | PostgreSQL and a consolidated relational model for M1-M7. Review the initial schema and seed scope before the skeleton. |
| Authentication and authorization | [#23](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/23) | ASP.NET Core Identity with cookie sessions and API resource-level authorization. Align the cookie and request flow with FE and hosting. |
| Caching | [#22](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/22) | .NET HybridCache with Valkey as the distributed tier. |
| Jobs, notifications, and push | [#28](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/28) | API-hosted background jobs, a transactional outbox, and real-time updates; resolve the cache and hosting dependencies together. |
| Hosting and deployment | [#19](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/19) | Azure Container Apps and Azure Container Registry for hosted environments, retaining one-command local startup. GitHub shows an approving review; the PR is open and the ADR still says Proposed. |
| Work-item and effort workflow | [#24](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/24), [#25](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/25) | Updates to work-item and effort skills; not product or release-pipeline evidence. |

## Official calendar and milestones

The actual start does not restart the course clock. Captains below follow the Charter draft rotation; swaps, reviewers, and cross-track milestone leads are **TBD** unless confirmed in weekly notes. For a missed slot, record what happened and why. Do not backdate tags or skip required approvals.

| Official week | Thursday slot / draft captain | Milestone or outcome |
|---|---|---|
| 1: 2-8 Nov | No release due | Original inception window passed; Charter, plan, backlog, and governance are still in progress. |
| 2: 9-15 Nov | 12 Nov / Carlos | Original `v0.1.0` milestone missed before the actual start. |
| 3: 16-22 Nov | 19 Nov / Petar | Weekly release slot missed before the actual start. |
| 4: 23-29 Nov | 26 Nov / Didier | Team started. Requirements pack merged into `preview` and ADRs opened for review; no release PR. |
| 5: 30 Nov-6 Dec | 3 Dec / George; cover TBD | Check whether 10 Dec remains viable: approve the initial ADRs and skeleton spec, review data model v0, and verify branch protections and initial CI. Start the slice only once its prerequisites are met. |
| 6: 7-13 Dec | 10 Dec / Carlos | Target `v0.1.0`: seeded sign-in, one working UI-to-API-to-DB flow, one-command startup, published images and smoke evidence. |
| 7: 14-20 Dec | 17 Dec / Petar | Integrate identity, map and occupancy foundations and a thin maintenance path. Prove exact-money rounding in domain tests, target hosted Preview, and agree handoffs and holiday coverage. |
| 8: 21-27 Dec | 24 Dec / Didier | Extend maintenance, announcements and audit as capacity allows. Review coverage TBD. |
| 9: 28 Dec-3 Jan | 31 Dec / George; cover TBD | Extend billing, overdue jobs, notification reliability and reporting as capacity allows. Review coverage TBD. |
| 10: 4-10 Jan | 7 Jan / Carlos; cover TBD | Integrate the remaining Core paths and Advanced work, run both scenarios on Preview, and rehearse deployment to Release. Review coverage TBD. |
| 11: 11-17 Jan | 14 Jan / Petar | Target a release candidate with automated Scenarios A and B on Release, a restore drill, Advanced evidence, and a full acceptance review. |
| 12: 18-24 Jan | 21 Jan / Didier | Target `v1.0.0` on `main`, verify the deployed build and evidence, and submit by the official deadline. Coverage and exact cutoff still need confirmation. |

## Build order and release checks

1. **Approve the starting point.** Review the frontend, API, database and authentication ADRs ([#6](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/6)) and data model v0 ([#7](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/7)). Confirm local environments ([#8](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/8)), branch enforcement and CI ([#4](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/4), [#9](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/9)). Track caching and hosting in separate ADRs; resolve deployment assumptions early.
2. **Ship the smallest real slice.** In [#12](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/12), review the feature spec for seeded sign-in as all four roles, at least one protected endpoint per role, and one real web-to-API-to-database page. A read-only Aurora Residence unit view is a candidate, not an agreed design. Verify allowed and denied access, use reproducible seed data, and prove one-command startup from source and published images. For `v0.1.0`, link passing CI (including migration and container checks), the release PR and tag, versioned images, and post-deployment smoke results.
3. **Build by dependency.** Establish scoped identity (M1), buildings and units (M2), and occupancy and leases (M3) first. Use these for the accessible 2D floor map and its equivalent list (M2) and the maintenance workflow (M4). Build reliable notifications (M6) and append-only audit (M7) alongside their first producers. Add metering, deterministic billing and idempotent simulated payments (M5); finish targeted announcements (M6), dashboards and scoped CSV exports (M7). Link stories and acceptance checks to the seven epics in [#5](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/5).
4. **Build Advanced foundations in parallel.** Agree the FE/BE/DB interfaces for concurrency, live updates, outbox, and history, and the OPS deployment and rollback path. Measure each claimed performance improvement against a baseline. Do not leave authorization, accessibility, migration safety, telemetry, or hosting to the last week.
5. **Prove the release.** Use reproducible synthetic seed data for both [signature scenarios](../capstone-spec/04-product-scenarios-roles-domain.md#5-signature-scenarios): the leak in 4B through assignment, notification and resolution, and month-end at Aurora Residence through exact allocation, statement issue, partial payment and overdue handling. Run both end to end on Release and retain keyboard and screen-reader evidence. Verify BLK-01 through BLK-10 and the [submission deliverables](../capstone-spec/15-deliverables-assessment-acceptance.md), including the demo video, runbook, team AI statement, retrospective and individual reflections.

## Open decisions, risks and escalation

The checkpoints are proposed review dates, not promises. The team must confirm named follow-up owners and dates. Raise a blocker in Teams with its issue link and escalate to the full team by the next working day if there is no path forward.

| Open item | Follow-up owner | Checkpoint and response |
|---|---|---|
| No agreed enforcement path for `main` and `preview` ([#4](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/4)) | TBD | Verify a compliant path at the 3 Dec checkpoint. If unresolved, escalate to the team and seek program guidance rather than bypassing protection or checks. |
| Missed November release slots; official calendar details and jury access | TBD | At the 3 Dec checkpoint, agree what guidance to request on missed slots, official breaks and the exact submission cutoff. Verify access and communication evidence separately in [#11](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/11). No program response or waiver is recorded. |
| First release blocked on foundational decisions, spec, CI or security evidence | TBD | Review on 3 Dec. Record recovery actions and revisit the 10 Dec target if any dependency cannot land in time. Keep actual full-history scan evidence in [#17](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/17). |
| Captain coverage on 3 Dec and holiday/final release review coverage | TBD | Confirm the 3 Dec captain before the slot; by 17 Dec agree technical backups, captain swaps and two eligible non-author reviewers for the 24 Dec, 31 Dec and 7 Jan slots. Verify 21 Jan coverage before final promotion. Escalate gaps; do not assume a swap or waive review. |
| Compressed schedule and unconfirmed FE/DB handoffs | TBD | Check capacity at the 3 Dec checkpoint and record backups by the 17 Dec handoff. Escalate if either signature scenario, Advanced scope, or individual evidence becomes infeasible. |
| Hosted environments may be late or inaccessible to the jury | TBD | Review hosting on 3 Dec, target hosted Preview by 17 Dec, and prove Release deployment, rollback, access and smoke by the 14 Jan candidate. Escalate if either date slips. |

## Cadence, evidence and approval

- **Meetings:** The team meets every morning from **10:30 to 11:30 GMT**. Keep one dated notes file per weekly check-in under `docs/team/meetings/` with decisions, risks, blockers, owners, dates, and agreed captain swaps.
- **PRs and releases:** Short-lived branch to `preview`: squash merge, one non-author approval. Weekly `preview` to `main`: merge commit, two non-author approvals, no rebase merges. Both require passing CI. The captain uses the [weekly release PR template](../../.github/PULL_REQUEST_TEMPLATE/release.md) to report what shipped versus this plan, what slipped and why, and to link checks, images, smoke evidence, and the rollback plan.
- **Individual evidence:** Record real work through [#10](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/10) and agree on journal locations during Charter review. Each person needs at least 40 evidenced hours, one merge and one cross-track review weekly, at least two authored major-feature specs before AI-assisted implementation, one authored ADR, and a weekly AI Engineering Journal with at least ten entries and three genuine failure analyses. Do not infer effort, reviews, or journal entries.
- **Approval and changes:** The plan coordinator and cross-track action owners are **TBD**. Record all four dated sign-offs before calling the plan approved. For each material change, record the old and new target, reason, consequences, follow-up owner, and decision date in the weekly notes and plan PR. A team approval cannot change official DevAcademy deadlines or requirements.

| Date | What changed | Approval status |
|---|---|---|
| 2026-11-10 | Initial 12-week outline | Draft |
| 2026-11-23 | Updated scope and governance for four participants | Included in PR #18, merged 25 Nov; not plan approval |
| 2026-11-24 | Standalone draft set out the official calendar, actual start, package assignments, build order and release targets | Draft |
| 2026-11-27 | Reconciled the Charter draft and open PR evidence, marked the missed Week 4 release and unresolved owners, and added the 3 Dec checkpoint | Pending team review |

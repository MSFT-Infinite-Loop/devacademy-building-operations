---
title: Roadmap — the main steps (what needs to be done, in order)
source_sections: "Derived from 1.1, 1.2, 12 (planning), 11.4 (weekly ritual), 13, 15 and Appendix I (first-week guide)"
load_when: "Always useful: answering 'what do we do next?', planning a week, checking whether a step is complete, or deciding what to prepare now."
related: [01-overview.md, 05-team-scope-ownership.md, 14-process-git-planning.md, 15-deliverables-assessment-acceptance.md, 19-decisions-questions-risks.md]
---

# Roadmap — the main steps

## 0. How to read this
- **S0–S7** are time-ordered steps. **W** (weekly ritual) repeats inside S2–S7. Every task names the spec IDs it satisfies and the pack file with the detail.
- **Only these are fixed by the spec:** Week-1 deliverables, a release PR + tag every week from Week 2 (`v0.1.0` at end of Week 2), `v1.0.0` at end of Week 12, Demo Day at the end of the edition. The week-to-phase mapping below is the spec's *suggestion* (14 §8), not a rule.
- Tags: **[ALL]** every team · **[ADV]** only if the Advanced package is in the team's scope · **[T3]** / **[T4]** team-size specific · `[PACK NOTE]` suggestion from the pack author · `[OPEN]` unresolved question.

**Current team state:** See [`../team/decision-register.md`](../team/decision-register.md), the Team Charter and the project plan. This roadmap does not duplicate live team status.

## 1. Overview

| Step | Name | When | Headline outcome | Gate to leave the step |
|---|---|---|---|---|
| S0 | Pre-kick-off | now → kick-off (Nov 2026, date TBC) | Team formed, spec read, jury questions sent, decisions register ready | Team size and members known |
| S1 | Week-1 setup | Week 1 | Charter, plan, repo + policies, board, first ADRs, AI instructions, jury informed, skeleton started | Everything emailed/accessible to the jury by end of Week 1 |
| S2 | Walking skeleton → `v0.1.0` | Week 2 | Sign-in + one page web → API → DB; one-command start; first release | Tag `v0.1.0` on `main` |
| S3 | Foundation | Weeks 3–5 | M1, M2 (first map), M3; thin slices of M4/M6/M7; pipeline + seed + first E2E | Thin slices of M1–M4 working on Preview |
| S4 | Core workflows | Weeks 6–8 | M4–M7 complete; Scenarios A and B on Release | Both scenarios pass end-to-end on Release (automated) |
| S5 | Depth and hardening | Weeks 9–10 | Advanced packages, security, performance evidence, accessibility, backup/restore, docs; ≈ `v0.9.0` | Acceptance checklist reviewed: no blocking gap |
| S6 | Stabilise | Week 11 | Bug bash, docs/runbook, demo script and video, code freeze | Freeze + all evidence present |
| S7 | Submission and Demo Day | Week 12 → end of edition | `v1.0.0`, video, retrospective, jury email; Demo Day + interviews | Submission email sent by end of Week 12 |
| W | Weekly ritual | every week (release PR from Week 2) | Merge, review, release PR + tag, effort log, AI journal, sync, self-check | — |

## 2. Steps in detail

### S0 — Pre-kick-off (now → kick-off)
**Goal:** arrive at Week 1 with a team and a clear picture, so Week 1 is not spent on basics.
- [ ] S0.1 **Confirm the team and resulting scope.** Each person must own ≥ 1 package and evidence ≥ 40 h. Scope varies by team size; see 05 §3 and record the current decision in [`../team/decision-register.md`](../team/decision-register.md).
- [ ] S0.2 Profile per track to recruit/assign: **FE** React 19 + Next.js/TanStack Start, TypeScript, accessibility, Playwright · **BE** C#/ASP.NET Core, EF Core/SQL, authN/authZ, background jobs · **DB** SQL modelling, migrations, indexing, procedures/triggers, backup/restore · **OPS** Git workflow, CI/CD, containers, Azure/Bicep, security scanning. `[PACK NOTE]`
- [ ] S0.3 Give candidates the short reading path: 01 overview, 05 team scope, 15 assessment (≈ 1 h) — mirrors spec §1, 3, 5, 14 + Appendix J.
- [ ] S0.4 **Ask the jury** the applicable questions from 19 §2. Sending any message is a manual, explicitly approved step.
- [ ] S0.5 Keep the canonical **team decision register** at [`../team/decision-register.md`](../team/decision-register.md) up to date.
- [ ] S0.6 Agree a provisional chat channel and a first team call. `[PACK NOTE]`
- [ ] S0.7 Verify environment readiness using 16 §1 before walking-skeleton implementation.
- [ ] S0.8 Ensure every team member can access this repository pack and understands that the official source wins conflicts.
**Exit gate:** team size and members known · kick-off date known · jury questions answered or logged.

### S1 — Week-1 setup (Inception)
**Goal:** produce the Week-1 deliverables the jury checks: Team Charter, project plan, repository with access for the jury, team details email.
*Team and governance*
- [ ] S1.1 Confirm members → scope (05 §3) → **package ownership** (OWN-01). [T3] pick two Advanced packages (changing later needs jury approval). If OPS Advanced is in scope, **hosting becomes mandatory**.
- [ ] S1.2 Read spec §1, 3, 5, 14 together (≈ 1 h); list questions for the jury.
- [ ] S1.3 Review and approve the **Team Charter** (PRC-01, [`../team/charter.md`](../team/charter.md)).
- [ ] S1.4 Review and approve the **project plan** (PRC-05, [`../team/plan.md`](../team/plan.md)).
- [ ] S1.5 Fix the weekly 15-minute sync, channel and release-captain rota (PRC-03; Charter). Weekly notes live in the repo (for example `docs/team/weekly-notes/`). `[PACK NOTE: path is a suggestion]`
*Repository and tooling*
- [ ] S1.6 Create the **private monorepo** on GitHub or Azure DevOps (GIT-01, GIT-02); folder skeleton per 16 §4.
- [ ] S1.7 **Protect `preview` and `main`** (GIT-06 table, 14 §3); CODEOWNERS (OWN-01); PR template (D.1); work-item templates; `.editorconfig`; `.gitignore` (OPS-C01).
- [ ] S1.8 **Jury read access** (GIT-01, OPS-C01).
- [ ] S1.9 Turn on **secret scanning / push protection from the first commit** (SEC-08, OPS-C06) — "no secrets in history" is a blocking item (BLK-09).
- [ ] S1.10 **CI skeleton** as required checks: restore, build, lint, tests, container build (OPS-C03; BLK-07).
- [ ] S1.11 **Board** with epics M1–M7, stories with Given/When/Then acceptance criteria, estimates, weekly iterations, effort field (PRC-02, OPS-C02).
*Architecture and data*
- [ ] S1.12 First **ADRs** ([`../templates/adr-template.md`](../templates/adr-template.md)): frontend framework (FE-C01), API style (BE-C01), database (DB-C01); then auth, caching, hosting (ARC-07: ≥ 6 ADRs, each participant authors ≥ 1).
- [ ] S1.13 **Data model v0** (DB-C02).
*Environment, AI and evidence*
- [ ] S1.14 Dev environments ready for everyone; Copilot enabled (16 §1–2).
- [ ] S1.15 **AI instructions file v1** (AI-02): architecture, conventions, build/test commands, security rules, Definition of Done (starter snippet in README §7).
- [ ] S1.16 Start the **effort log** and each person's **AI Engineering Journal** (PRC-06, AI-04) — from day one.
- [ ] S1.17 Plan who authors which feature spec (≥ 2 each, written before implementation, AI-03).
*Jury and skeleton*
- [ ] S1.18 **Email the jury**: team name, members, repository link (draft in 19 §3).
- [ ] S1.19 **Start the walking skeleton** (sign-in + one page web → API → DB).
**Week-1 outputs (App I):** Team Charter · package ownership · project plan · backlog v1 · repository · branch policies · CI skeleton · initial ADR drafts · data model v0 · AI instructions v1 · jury read access · team details sent to the jury.
**Exit gate:** all outputs exist; jury has access and has been emailed.

### S2 — Week 2: Walking skeleton → `v0.1.0`
**Goal:** one real path through the whole stack, released.
- [ ] S2.1 **Sign-in** with seeded accounts for the four roles and one protected endpoint per role (M1 slice; BE-C04).
- [ ] S2.2 One page wired **web → API → database**.
- [ ] S2.3 **One-command local start** (Compose/Aspire) from source and from published images (OPS-C04; BLK-01).
- [ ] S2.4 Initial **seed** (PX-08 start): Aurora Residence, unit 4B, the four personas, demo accounts.
- [ ] S2.5 Merge to `preview` publishes images and runs a smoke test (OPS-C05; BLK-08).
- [ ] S2.6 Baseline plumbing: ProblemDetails + `IExceptionHandler`, correlation IDs, structured logs, health endpoints (BE-C05, BE-C10, SEC-11). `[PACK NOTE: cheapest to add now]`
- [ ] S2.7 Start writing **audit records** from the first write endpoint (M7 slice). `[PACK NOTE]`
- [ ] S2.8 **First release PR** `Release v0.1.0 - Week 2` ([release template](../../.github/PULL_REQUEST_TEMPLATE/release.md)), merge commit, tag `v0.1.0`, CHANGELOG/release notes (GIT-04, GIT-05, OPS-C08).
**Exit gate:** `v0.1.0` tagged on `main`.

### S3 — Weeks 3–5: Foundation
**Goal:** thin slices of every Core module, solid data and pipeline foundations.
- [ ] S3.1 **M1** complete: invitations, scoped role assignments, deactivation, object-level checks on every endpoint; authorization tests generated from the permissions matrix (M1-01..M1-06; BE-C04, BE-C11, SEC-03; BLK-03).
- [ ] S3.2 **M2**: data-driven floor map from JSON layouts, derived unit statuses, legend/filters, list view, keyboard support, unit detail page, second building (M2-01..M2-07; FE-C07; BLK-04).
- [ ] S3.3 **M3**: persons, ownership, lease lifecycle, **race-safe overlap check with a test**, occupancy history (M3-01..M3-05; DB-C03).
- [ ] S3.4 **M4 thin slice** (submit → triage → assign → resolve), **M6 thin slice** (notification on work-order change), **M7** audit records on all writes.
- [ ] S3.5 **DB**: versioned migrations + seed in the pipeline against a disposable DB (DB-C04); constraints; ERD + data dictionary (DB-C02); first indexes (DB-C05).
- [ ] S3.6 **FE**: draft Rendering Strategy Table (FE-C02); forms, data-state handling, first optimistic interaction (FE-C04..FE-C06).
- [ ] S3.7 **BE**: transactions (BE-C06) and the first cached reads with invalidation (BE-C07).
- [ ] S3.8 **Quality/OPS**: first Playwright E2E test (FE-C11); test-strategy draft (QA-01); required CI checks complete (BLK-07).
- [ ] S3.9 Weekly ritual continues (§3).
**Exit gate:** thin slices of M1–M4 working on Preview.

### S4 — Weeks 6–8: Core workflows
**Goal:** all seven modules done and both scenarios running on Release.
- [ ] S4.1 **M4** complete (M4-01..M4-13): every transition and role check with table-driven tests; SLA with due-soon/overdue; internal notes separated by the API; technician queue; Kanban (SHOULD); notifications; jobs.
- [ ] S4.2 **M5** complete (M5-01..M5-11): meters and validation; tariffs; common expenses (≥ 2 allocation rules); billing run preview/approve/issue; exact-money tests (leftover cents, vacant units, zero consumption, meter replacement); statement state machine; simulated payments with idempotency; resident billing views.
- [ ] S4.3 **M6** complete (M6-01..M6-05): announcements with targeting and lifecycle jobs; notification centre; reliable creation (same transaction or outbox); cross-building isolation test.
- [ ] S4.4 **M7** complete (M7-01..M7-05): audit viewer; role dashboards agreeing with direct DB queries; CSV export with authorization.
- [ ] S4.5 **Jobs** M3-06, M4-10, M4-11, M5-08, M6-02, all idempotent and observable (BE-C08).
- [ ] S4.6 **PX sweep**: server-side pagination/search/filter/sort, four data states, UTC/ISO 8601, decimal money with currency, archiving, English-only, **seed at full volume** (PX-01..PX-09).
- [ ] S4.7 **Scenarios A and B automated as E2E tests** and green **on Release** (BLK-02).
**Exit gate:** Scenarios A and B pass end-to-end on Release.

### S5 — Weeks 9–10: Depth and hardening
**Goal:** evidence, Advanced packages and a release candidate.
- [ ] S5.1 **Advanced packages in scope** [ADV]: FE-A01..FE-A06, BE-A01..BE-A06, DB-A01..DB-A06, OPS-A01..OPS-A06 — each with its evidence artefact (performance reports, incident drill, SBOM, …).
- [ ] S5.2 **Security** (SEC-01..SEC-15): final threat model, headers, CSRF/CORS, uploads, sign-in rate limiting, scans triaged, ASVS Level 1, privacy notes → `docs/security/`.
- [ ] S5.3 **Quality**: all test levels run in CI (QA-02); accessibility report (FE-C08); before/after measurements for every optimisation (QA-08).
- [ ] S5.4 **Backup-and-restore drill** with counts/checksums + smoke test (DB-C08, QA-06).
- [ ] S5.5 **Docs**: ≥ 6 ADRs, C4/deployment/sequence/data-model diagrams, API conventions, OpenAPI, runbook, README with dependencies + licences (ARC-06..ARC-10, OPS-C09).
- [ ] S5.6 Run the full **acceptance checklist** (15 §8) and fix every blocking gap; tag the release candidate (≈ `v0.9.0`).
**Exit gate:** no blocking acceptance item open.

### S6 — Week 11: Stabilise
- [ ] S6.1 Bug bash; fix; finish docs and runbook.
- [ ] S6.2 **Fresh-clone, one-command** test of the stack; reset and verify the seed data.
- [ ] S6.3 **Full-history secret scan** (BLK-09).
- [ ] S6.4 Demo script and draft video (A, B, role tour); draft the team AI usage statement and retrospective; each person drafts a one-page reflection.
- [ ] S6.5 Evidence audit: every participant has ≥ 40 h logged with links, ≥ 10 journal entries (≥ 3 failure analyses), ≥ 2 specs.
- [ ] S6.6 **Code freeze** at the end of the week (recommended).
**Exit gate:** freeze; all evidence present.

### S7 — Week 12 → Demo Day: Submission
- [ ] S7.1 Cut **`v1.0.0`**: merge commit, tag, CHANGELOG, images, Release deploy + smoke tests (DEL-02).
- [ ] S7.2 **Demo video ≤ 10 min** (DEL-04).
- [ ] S7.3 Documentation set complete (15 §2); retrospective + individual reflections; effort logs and AI journals (DEL-03, DEL-07, DEL-08).
- [ ] S7.4 Final run of the acceptance checklist.
- [ ] S7.5 **Email all three jury members** by the end of Week 12: team name, repository link, release version `v1.0.0`, environment URLs if hosted. Deadline is firm.
- [ ] S7.6 Demo Day prep: freshly reset seed data; rehearse 12 + 3 + 5 minutes; fallback recordings per scenario; keep Preview/Release up if hosted; interview prep (explain and modify your own code, including AI-generated parts).
- [ ] S7.7 After Demo Day: delete Azure resources if used.
Changes after submission are not graded.

## 3. Weekly ritual (W)
**Each participant, every week:** merge ≥ 1 PR into `preview` (GIT-03) · review ≥ 1 PR outside your own track (GIT-09, OWN-03) · update the effort log with evidence links (PRC-06) · write an AI Engineering Journal entry (AI-04) · keep the board current.
**Team, every week:** 15-minute sync with notes in the repo (PRC-03) · **from Week 2** release PR `Release vX.Y.0 - Week N` → merge commit → tag → release notes → images → smoke tests (GIT-04, GIT-05, OPS-C08) · progress against `docs/team/plan.md` in the release PR (PRC-05) · five-minute self-check (14 §5).
**Suggested rhythm:** Mon plan + captain · Mon–Thu small PRs · Thu stabilise `preview` · Fri release PR + sync. If nothing is releasable, the captain records why in the weekly notes.

## 4. What changes with team size

| Aspect | Team of 2 | Team of 3 | Team of 4 |
|---|---|---|---|
| Packages | 4 Core | 4 Core + any 2 Advanced | 4 Core + all 4 Advanced |
| Hosted Preview/Release | Optional | Mandatory only if OPS Advanced chosen | **Mandatory** |
| `main` approvals (GIT-06) | 1 | 2 | 2 |
| S5 depth work | Core hardening only | Two Advanced packages | Four Advanced packages |
| Per-person package hours | ≈ 40–50 | ≈ 40–47 | ≈ 40–45 (+ 6–10 shared) |
| Charter must record | Package ownership | Package ownership + the two Advanced picks | One track per person |

## 5. Gates and the critical path
Blocking items (cap the Team Score at 50) and when they should be true `[PACK NOTE: target steps]`:

| Blocking item | True by | Detail |
|---|---|---|
| BLK-09 no secrets in history | first commit, always | 11 SEC-08 |
| BLK-06 protected branches + weekly release PRs/tags from Week 2 | S1, then every week | 14 |
| BLK-05 stack baseline + ADRs | S1 | 06, 07, 08 |
| BLK-07 CI on every PR | S1 skeleton, complete in S3 | 09 |
| BLK-01 one-command start + Release env | local in S2; Release by S4 | 09 |
| BLK-08 containers, images per merge/release, smoke tests | S2 onward | 09 |
| BLK-10 AI disclosure + journals | first PR and every week | 13 |
| BLK-03 four roles + authz tests | S3 | 02, 11 |
| BLK-04 data-driven accessible 2D map + list | S3 | 02, 06 |
| BLK-02 M1–M7 + Scenarios A and B on Release | S4 | 02–04 |

Individual gate: every participant ≥ 40 evidenced hours (05 §6).
**Decisions that block steps:** team size/ownership → S1 · framework/API style/DB ADRs → S1 before the skeleton · auth ADR → S2 · repo host → S1 · hosting → S1 if OPS Advanced is in scope · caching ADR → S3.

## 6. Calendar worksheet (fill in when the jury confirms the kick-off date)

| Week | Start | End | Phase | Release tag `[PACK NOTE: suggested]` | Captain |
|---|---|---|---|---|---|
| 1 | ____ | ____ | Inception | — (no release required) | — |
| 2 | ____ | ____ | Walking skeleton | v0.1.0 | |
| 3 | ____ | ____ | Foundation | v0.2.0 | |
| 4 | ____ | ____ | Foundation | v0.3.0 | |
| 5 | ____ | ____ | Foundation | v0.4.0 | |
| 6 | ____ | ____ | Core workflows | v0.5.0 | |
| 7 | ____ | ____ | Core workflows | v0.6.0 | |
| 8 | ____ | ____ | Core workflows | v0.7.0 | |
| 9 | ____ | ____ | Depth and hardening | v0.8.0 | |
| 10 | ____ | ____ | Depth and hardening | v0.9.0 (release candidate) | |
| 11 | ____ | ____ | Stabilise | v0.10.0 | |
| 12 | ____ | ____ | Final | **v1.0.0** | |

`[PACK NOTE]` Twelve weeks from a mid-to-late-November start run through Christmas/New Year. The spec requires a release PR every week from Week 2 and only says the captain records the reason when nothing is releasable — ask the jury whether holiday weeks are treated differently (19 §2, Q4).

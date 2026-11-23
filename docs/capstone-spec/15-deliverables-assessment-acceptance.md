---
title: Deliverables, submission, assessment, pitfalls, acceptance checklist
source_sections: "13 (DEL-01..DEL-08), 14 (assessment), 14.6 pitfalls, 15 (acceptance checklist)"
load_when: "Preparing the submission, demo or interview; understanding how the grade is computed; running the acceptance checklist; checking what caps the score."
related: [01-overview.md, 14-process-git-planning.md, 12-quality-testing.md, 13-ai-assisted-engineering.md]
---

# Deliverables, submission, assessment, pitfalls, acceptance checklist

## 1. Deliverables (DEL)
Deadline: **end of Week 12**. Firm: late submissions only for extreme, documented circumstances approved by the jury.

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| DEL-01 | MUST | ALL | **Repository**: code plus supporting engineering history — commits, pull requests, release tags, pipelines, team board. The principal body of grading evidence. | Team repository |
| DEL-02 | MUST | ALL | **Runnable release**: final `v1.0.0`, runnable with **one documented command** from the team's published images; includes **demo accounts for every role**. If hosted, Preview and Release URLs stay available **through Demo Day**. | Final release |
| DEL-03 | MUST | ALL | **Documentation set** in the repository at the locations in §2. | Repository docs |
| DEL-04 | MUST | ALL | **Demo video, maximum 10 minutes**: Scenario A, Scenario B, and a brief tour of each role's experience. | Submitted with the final release by end of Week 12 |
| DEL-05 | MUST | ALL | **Final presentation, 20 minutes per team**: 12 min live demo of `v1.0.0` + 3 min engineering highlights + 5 min jury questions. | Live at Demo Day |
| DEL-06 | MUST | ALL | **Technical interview**, about 20 minutes per participant: walkthrough of owned packages, architecture questions, a small live change or debugging task. | With the jury around Demo Day |
| DEL-07 | MUST | ALL | **Retrospective and reflections**: one team retrospective + a one-page individual reflection from each participant (what was learned, how AI was used, what they would do differently). | Part of the final submission |
| DEL-08 | MUST | ALL | **Individual evidence**: an effort log and an AI Engineering Journal for every participant. | Included with the submission |

## 2. Documentation set (DEL-03) — treat these paths as required `[PACK NOTE: safe default; Appendix B shows an example layout]`

| Content | Location |
|---|---|
| Project overview, quick start, demo-account information, links, **main dependencies and licences (ARC-10)** | `README.md` |
| C4 diagrams, deployment diagram, Scenario A sequence diagram, data model, Rendering Strategy Table, API conventions | `docs/architecture/` |
| Architecture Decision Records | `docs/adr/` |
| Feature specifications | `docs/specs/` |
| OpenAPI document + link to interactive API docs | `docs/api/` |
| Test strategy, test results, accessibility report | `docs/testing/` |
| Threat model, ASVS checklist, scan results/exceptions, privacy notes | `docs/security/` |
| Runbook, backup-and-restore evidence, (Advanced) incident-drill material | `docs/operations/` (runbook: `docs/operations/runbook.md`) |
| Performance measurements | `docs/performance/` |
| Team AI usage statement, AI journals, prompt-library index | `docs/ai/` |
| Team Charter, project plan (`docs/team/plan.md`), weekly notes, effort evidence, retrospective | `docs/team/` plus the selected work-tracking system |
| Release notes | `CHANGELOG.md` |

## 3. Final submission procedure (by end of Week 12)
1. Finalise the submitted version on `main`.
2. Create the exact tag **`v1.0.0`** on `main`.
3. **Email all three jury members** with: team name, repository link, release version, and (if hosted) the environment URLs.
4. Contact the jury immediately if a serious circumstance threatens the deadline.
The jury grades the submitted `v1.0.0`; changes after submission are not graded.

## 4. Demo and Demo Day
- Video (DEL-04): ≤ 10 min; Scenario A; Scenario B; short tour of every role.
- Live (DEL-05): 20 min = 12 demo + 3 highlights + 5 Q&A.
- **Demo tip:** prepare against freshly reset seed data; rehearse with the same script as the submitted video; keep a short recording of each scenario as a fallback if the network fails.
- What the jury inspects first (FAQ): 1) the README, 2) release `v1.0.0` running with the demo accounts, 3) Scenario A, 4) Scenario B — make these excellent.
- If you finish Core early: strengthen evidence (tests, performance, security) → deepen required Advanced packages → pick an optional extension.

## 5. Technical interview (DEL-06, 35 individual points)
About 20 minutes per participant around Demo Day: walkthrough of your packages; architecture questions; a small live modification or debugging/diagnostic task. Any code you own — including AI-generated — may be explained or modified; code you cannot explain does not count.
Example tasks from the spec:
- Explain the full request flow browser → backend → database for a technician resolving a work order.
- Show the object-level authorization that stops one resident reading another's statement and the test proving it.
- Explain why a specific read is cached and exactly how/when it is invalidated.
- Change the "due soon" threshold from 25% to 20%, run the tests and explain the effects.
- Identify code in your package produced with AI help and explain how you verified it.
- A query becomes slow with 1 million readings: explain how you would investigate.

## 6. Assessment

### 6.1 Formula and bands
**Final grade = 60% × Team Score + 40% × Individual Score** (each out of 100, awarded by the jury).

| Final grade | Outcome |
|---|---|
| 85–100 | Distinction (if all gates are met) |
| 60–84.99 | Pass (if all gates are met) |
| Below 60 | Fail |

The jury assesses evidence and quality, not volume; commit counts and lines of code do not count.

### 6.2 Team Score (100 points)

| Category | Points | What full marks need |
|---|---|---|
| A. Product functionality and domain depth | 30 | All Core modules work end-to-end; business rules and state machines correct; money reconciles exactly; the 2D map is data-driven and accessible; coherent experience per role |
| B. Architecture, security and data integrity | 20 | Clear boundaries; consistent API; object-level authorization proven by tests; robust data model with constraints, transactions, programmable objects; thoughtful caching, pooling, jobs; meaningful threat model |
| C. Frontend engineering and UX | 15 | Intentional rendering choices; optimistic interactions with rollback; all data states; accessibility and responsiveness; usable and consistent UI |
| D. DevOps, testing and operability | 15 | Dependable CI/CD, containers, Preview/Release, scans and triage; all required test levels; logging and health checks; useful runbook; demonstrated backup/restore |
| E. AI-assisted engineering practice | 10 | Useful repo AI context; specs before implementation; disciplined verification; transparent disclosure; shared prompt library; thoughtful journals |
| F. Collaboration and delivery process | 5 | Trunk-based integration via `preview`; tagged weekly releases; meaningful reviews; backlog and plan reflect reality |
| G. Documentation and final demo | 5 | Clear, accurate docs; demo conveys both scenarios; confident answers |

Grading levels per category: **Excellent 90–100%** (complete, correct, strongly evidenced) · **Good 70–89%** (minor gaps) · **Basic 50–69%** (partial or weak evidence) · **Insufficient < 50%** (missing, broken, unsupported).
Advanced packages count only in categories **B, C, D**, judged against the scope the team size requires (no penalty for Advanced packages never required).

### 6.3 Individual Score (100 points)

| Component | Points | Assessed |
|---|---|---|
| I1 Package delivery | 40 | Completeness and quality of the package items you own, against the Section 6 evidence |
| I2 Technical interview | 35 | Explaining architecture and decisions; walking through your code incl. AI-generated parts; small live modification/diagnostic task |
| I3 Contribution and collaboration | 15 | PRs, reviews you performed, board hygiene, effort log, confidential end-of-project peer feedback gathered by the jury |
| I4 AI Engineering Journal and reflection | 10 | Quality, honesty and depth of insight in your journal and final reflection |

### 6.4 Gates, penalties and caps
- **Blocking cap:** if any blocking acceptance item (§8, BLK-01..BLK-10) is unmet at final submission, **Team Score ≤ 50/100**.
- **40-hour gate:** a participant who cannot evidence ≥ 40 hours cannot pass (unless the jury approves an exception, for example a documented absence). See 05 §6.
- **Optional extensions** (X1–X7): no base points; cannot compensate for incomplete Core; may earn separate Demo Day recognition.

### 6.5 Academic integrity
Breaches: fabricating repository history, effort logs, reviews or journal entries; using code you have no permission to use; submitting undeclared third-party work; committing secrets. Teams work independently: discussing ideas is fine, but code, tests and documents must be your own. Templates, starter projects and open-source libraries are allowed when licensing permits and use is declared; the **domain logic must be the team's own**.

## 7. Common pitfalls and what to do instead

| Pitfall | Do instead (IDs) |
|---|---|
| Authorization enforced only in the UI | Enforce on every API operation; prove it with tests using another resident's IDs (M1-05, SEC-03) |
| Money as floating point | Decimals + a defined rounding policy; test that allocations reconcile exactly (M5-07) |
| Statuses assigned by hand | Derive states such as Open issue from underlying data (M2-02) |
| Long-lived personal branches and one big final merge | Small PRs into `preview` every week (GIT-03) |
| Squashing the weekly release PR | Merge `preview` → `main` with a merge commit (GIT-05) |
| Tests pass whether or not the behaviour works | Break the behaviour once and confirm the test fails (AI-05) |
| Building optional extensions before Core | Finish Core and both scenarios first (6.4) |
| README works only on the author's machine | Before every release, test a fresh clone with one command (OPS-C04) |
| Seed data cannot reproduce the scenarios | Include Aurora Residence, unit 4B and the personas (PX-08) |
| Nobody understands AI-generated code | Small PRs, read every diff, journal what was verified (AI-05, AI-12) |
| A secret is committed "temporarily" | Secret scanning from day one; rotate any leaked credential immediately (SEC-08) |
| Effort logs reconstructed at the end | Log weekly with an evidence link (PRC-06) |
| Adding a dependency with a prohibited licence | Check ARC-10 and 10 §6 before adding it |

## 8. Acceptance checklist (Section 15)
Revisit it every few weeks (not just at the end) and combine it with the weekly self-check (14 §5).

### 8.1 BLOCKING items — any miss caps the Team Score at 50
IDs `BLK-01..BLK-10` are **pack-assigned** for easy reference (the spec does not number them).

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| BLK-01 | MUST | BLOCKING | Application starts locally with **one documented command** and also runs in the **Release environment**. | README; Release run |
| BLK-02 | MUST | BLOCKING | All modules **M1–M7** implemented; **Scenarios A and B work end-to-end on Release**. | E2E tests; Release demo |
| BLK-03 | MUST | BLOCKING | All **four roles** with **object-level authorization**; automated tests show one resident cannot access another resident's records. | Authorization tests in CI |
| BLK-04 | MUST | BLOCKING | A **data-driven 2D floor map**, usable by keyboard, with an equivalent **list alternative**. | Map code; accessibility report |
| BLK-05 | MUST | BLOCKING | Stack baseline: React 19 with Next.js 16+ or TanStack Start 1.x; ASP.NET Core (controllers or Minimal APIs) on .NET 10 LTS, or .NET 11 with an ADR; SQL or NoSQL database with the choice documented in an ADR. | ADRs; repo config |
| BLK-06 | MUST | BLOCKING | GitHub or Azure DevOps repository with protected `main` and `preview`; **weekly release PRs with tags beginning in Week 2**. | Branch policies; release history |
| BLK-07 | MUST | BLOCKING | **Every PR runs CI**: build, lint, tests, migration check, container build. | CI history |
| BLK-08 | MUST | BLOCKING | Components containerized; images published automatically after **every merge into `preview`** and **every release**; **every new version smoke-tested**. Hosted Preview and Release required if OPS Advanced is in scope. | Registry, pipeline and smoke history |
| BLK-09 | MUST | BLOCKING | **No secrets anywhere in repository history.** | Secret-scan results |
| BLK-10 | MUST | BLOCKING | AI usage disclosed in **PRs** and in the **team AI usage statement**; **every participant has an AI Engineering Journal**. | PR disclosures; statement; journals |

### 8.2 REQUIRED items (not blocking)

| Area | Requirement |
|---|---|
| Product | Data-heavy lists support pagination, search, filtering, sorting; all data views handle loading/empty/error/success |
| Product | Money handled exactly with deterministic allocation, backed by tests |
| Product | Scheduled jobs: lease expiry, SLA escalation, auto-close, overdue statements, announcement publication, announcement expiry |
| Product | Audit trail for important changes + an audit viewer |
| Engineering | Rendering Strategy Table; at least 2 optimistic interactions with rollback |
| Engineering | OpenAPI documentation; ProblemDetails errors; validation |
| Engineering | ARC-10 technology compliance; main dependencies and licences in the README |
| Engineering | Connection pooling documented; at least 2 reads cached with invalidation |
| Engineering | Migrations, reproducible seed, constraints, justified indexes with plans, programmable DB objects (or NoSQL equivalents), all tested |
| Engineering | Backup-and-restore drill with retained evidence |
| Engineering | All Advanced packages required for the team size complete |
| DevOps/quality | Dependency, source and container scanning with triaged findings |
| DevOps/quality | Unit, integration, database, component, E2E, authorization, accessibility tests all run in CI |
| DevOps/quality | Health checks, structured logs with correlation IDs, runbook |
| Security | Threat model, security headers, CSRF protection, controlled CORS, secure uploads, sign-in rate limiting, no tokens in browser storage |
| AI/process | Repository AI instructions file; ≥ 2 specs per participant |
| AI/process | Team Charter, current project plan, backlog with acceptance criteria, Definition of Done, weekly notes |
| AI/process | Demo video, final presentation, retrospective, individual reflections |
| Individual gate | Every participant: effort log proving ≥ 40 evidenced hours |

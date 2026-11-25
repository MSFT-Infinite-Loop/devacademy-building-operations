---
title: Team size, engineering tracks, ownership and effort
source_sections: "5 (5.1–5.4), OWN-01..06, effort evidence rules (PRC-06/07/08)"
load_when: "Choosing team scope and package ownership, planning workload, or checking the 40-hour individual rule."
related: [06-track-frontend.md, 07-track-backend.md, 08-track-data.md, 09-track-devops.md, 19-decisions-questions-risks.md]
---

# Team size, engineering tracks, ownership and effort

## 1. In short
- Every team builds the **same product** (M1–M7). Team size changes the required **engineering depth**, not the product.
- Engineering work is split into four **tracks**: **FE, BE, DB, OPS**. Each track has one **Core package** (required for every team) and one **Advanced package** (required depending on team size).
- Every participant must **own at least one package** and record **at least 40 hours** of evidenced work.

## 2. Tracks

| Track | Full name | Main focus | Spec section | Pack file |
|---|---|---|---|---|
| FE | Frontend Engineering | React 19, rendering strategy, optimistic UI, interactive 2D map, accessibility, frontend performance | 6.1 | 06 |
| BE | Backend Engineering | ASP.NET Core API, authorization, transactions, connection pooling, caching, background jobs, resilience | 6.2 | 07 |
| DB | Data Engineering | Modelling, integrity, migrations, indexing, procedures, triggers, views, backup and restore | 6.3 | 08 |
| OPS | DevOps and Platform | Repository governance, CI/CD, containers, environments, security scanning, observability | 6.4 | 09 |

Package IDs: `FE-C01..FE-C11` and `FE-A01..FE-A06` (and likewise BE, DB, OPS). **C = Core, A = Advanced.** Counts: FE 11+6, BE 11+6, DB 9+6, OPS 9+6.

## 3. Required scope by team size

| Team size | Core packages | Advanced packages | Total packages | Indicative team effort |
|---|---|---|---|---|
| 1 (jury approval needed) | All four: FE, BE, DB, OPS Core | None | 4 | ≈ 80–100 h (same as team of two) |
| 2 | All four Core | None | 4 | ≈ 80–100 h (≈ 40–50 h each) |
| 3 | All four Core | **Any two** Advanced (chosen in Week 1, recorded in the Team Charter; changing later needs jury approval) | 6 | ≈ 120–140 h |
| 4 | All four Core | **All four** Advanced | 8 | ≈ 160–180 h |

**Solo participant:** needs the jury's written approval (OWN-06); delivers the team-of-two scope; acts as full-stack owner; PR reviews come from a **review buddy on another team**; expected effort is still ≈ 80–100 h.

**Typical ownership (examples, not rules)**
- Team of 2: P1 = FE Core + OPS Core; P2 = BE Core + DB Core.
- Team of 3: P1 = FE Core + FE Advanced; P2 = BE Core + BE Advanced; P3 = DB Core + OPS Core (plus any two Advanced in total).
- Team of 4: one complete track per participant (Core + Advanced).

**Hosting consequence:** **OPS Advanced requires hosted Preview and Release environments.** Therefore hosting is mandatory for **every team of four** and for any team of three that selects OPS Advanced as one of its two Advanced packages. Azure is recommended but not mandatory; any host the jury can access is acceptable (see 16).

**Scoring effect:** Advanced packages contribute to Team Score categories B, C and D, judged against the scope the team's size actually requires — smaller teams are not penalised for Advanced packages they never needed.

## 4. Effort model

| Component | FE | BE | DB | OPS | Indicative total |
|---|---|---|---|---|---|
| Core packages | ≈ 25 h | ≈ 25 h | ≈ 20 h | ≈ 20 h | ≈ 80–100 h |
| Advanced package (when required) | ≈ 20 h | ≈ 20 h | ≈ 20 h | ≈ 20 h | + ≈ 20 h per selected package |

How to interpret (spec): estimates are planning aids, not commitments; they assume consistent AI-assistant use; each includes its own implementation, testing and documentation; **shared team activities** (planning, code reviews, weekly releases, demo preparation) add ≈ **6–10 h per participant** and **count toward the 40-hour minimum**; the mandatory rule is the **40-hour evidenced minimum**, not the package hours.

Package scope summary

| Package | ≈ h | Included scope |
|---|---|---|
| FE Core | 25 | M1–M7 screens, rendering strategy, routing, forms, optimistic UI, the 2D map, accessibility, tests |
| BE Core | 25 | M1–M7 API, authentication/authorization, validation, transactions, connection pooling, caching, jobs, auditing, tests |
| DB Core | 20 | Data model, constraints, migrations, seed data, indexes, procedures, views, triggers, backup and restore |
| OPS Core | 20 | Repository and policies, work tracking, CI, containers, published Preview/Release images, secrets, security scanning, releases, runbook |
| Each Advanced | 20 | Depth requirements for the track (see 06–09) |

**Example weekly workload for one participant**

| Activity | Hours/week |
|---|---|
| Building the owned package (code, tests, docs) | 3–3.5 |
| Reviewing teammates' pull requests | 0.5 |
| Team sync and weekly planning | 0.25–0.5 |
| Updating the effort log and AI Engineering Journal | 0.25 |
| **Total** | **≈ 4–4.75** |

12 weeks × that ≈ **48–57 hours** per participant.
`[PACK NOTE]` Team-of-4 arithmetic: 160–180 package hours ÷ 4 ≈ 40–45 h each, plus 6–10 h shared ≈ **46–55 h per person** ≈ 4–4.6 h/week over 12 weeks. Team of 3: 120–140 ÷ 3 ≈ 40–47 h each + shared.

## 5. Ownership requirements (OWN)

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| OWN-01 | MUST | ALL | Every participant owns at least one package and is its primary author. Ownership is recorded in the Week-1 Team Charter and in CODEOWNERS (or the Azure DevOps equivalent). | Team Charter; CODEOWNERS |
| OWN-02 | MUST | ALL | Every participant records at least 40 hours of evidenced work (PRC-06/07). Work should be balanced across the team; any large imbalance is explained in the retrospective. | Effort log |
| OWN-03 | MUST | ALL | Ownership must not become isolation: every participant reviews pull requests outside their own track each week and can explain the complete end-to-end architecture. | PR review history |
| OWN-04 | SHOULD | ALL | Every participant delivers at least one vertical slice spanning interface → API → database. | PRs |
| OWN-05 | MUST | ALL | If a participant leaves, the team notifies the jury within **one week**. The jury adjusts the Advanced-package requirement. Merged work stays credited to its original author. | Email to jury |
| OWN-06 | MUST | ALL | Solo participation needs the jury's written approval; the solo participant delivers the two-person-team scope and obtains PR reviews from a review buddy on another team. | Written approval |

## 6. Individual evidence and the 40 hours (PRC-06, PRC-07, PRC-08)
- Log effort **weekly and per work item**. Fields: **date, work item, package/requirement (for example BE-C06), activity, hours, evidence link** (PR, commit or document). Activity values: design, code, test, review, docs, ops, meeting, learning.
- Where: Azure Boards "Completed Work", a numeric field in GitHub Projects, or `docs/team/effort-log.csv`. The repository's selected mechanism is recorded in [`../team/decision-register.md`](../team/decision-register.md).
- **≥ 40 evidenced hours per participant**, consistent with repository and board evidence. Package-relevant learning counts, capped at **25%** of the participant's logged hours.
- **Not** used to measure effort: commit counts and lines of code.
- A participant who cannot evidence 40 hours **cannot pass**, unless the jury approves an exception (for example a documented absence).
- The jury cross-checks the log against board activity, pull requests, reviews and documents.
- `[PACK NOTE]` The pitfall list warns against reconstructing logs at the end — log weekly with an evidence link from the first week.

---
title: DevAcademy 2026–2027 Capstone — AI-Ready Requirements Pack
pack_version: 0.2.0
pack_date: 2026-11-23
source: "DevAcademy 2026 Capstone requirements — v1.4, 2 November 2026"
status: "Canonical repository working specification — the official source wins conflicts"
team_state: "../team/decision-register.md"
load_when: "Always load this file first."
---

# DevAcademy 2026–2027 Capstone — AI-Ready Requirements Pack

## 1. What this is
A restructured, AI-friendly version of the capstone requirements specification (Building Operations Platform), plus a step-by-step roadmap, decision options and reusable guidance. It is built to be **read by people** and **loaded selectively by GitHub Copilot** in small, topic-sized pieces with stable requirement IDs.

It answers three questions: **what must be built** (files 02–04, 06–13), **what must be done and when** (file 00 roadmap, 14, 15), and **how to use all of it** (this file).

## 2. Status and trust
- **Canonical working specification.** This is the repository's day-to-day requirements reference.
- **Official source wins conflicts.** Content was extracted from the official source through Microsoft 365 summaries and then restructured. Wording is paraphrased; requirement IDs, MUST/SHOULD/MAY levels, numbers, thresholds and deadlines were preserved. **Before relying on an exact value for a graded decision, check the official source.**
- **Latest source checked:** v1.4, 2 November 2026.
- **Immutable snapshot.** Ordinary feature work must not edit requirement wording. A newer official version requires a dedicated, reviewed resynchronization.
- **Live team state is separate.** Current decisions, owners and unresolved choices live in [`../team/decision-register.md`](../team/decision-register.md).
- `[PACK NOTE]` marks commentary written by the pack author (not from the spec). `[OPEN]` marks an unanswered question. `[TEAM DECISION]` marks a placeholder for a choice the team must make.

## 3. The project in ten lines
1. Build the **Building Operations Platform**: units + live 2D floor map, residents + leases, maintenance work orders, utility meters + monthly billing, announcements + notifications, dashboards + audit trail.
2. **7 Core modules (M1–M7), 4 roles** (Administrator, Building Manager, Resident, Technician), **2 signature scenarios** (A: leak in apartment 4B; B: month-end billing at Aurora Residence).
3. Team of **2–4**; **12 weeks** from a November 2026 kick-off; Demo Day at the end of the edition.
4. Stack: **React 19.2+ (Next.js 16+ or TanStack Start 1.x), ASP.NET Core on .NET 10 LTS, SQL or NoSQL**, GitHub or Azure DevOps, containers.
5. Technology policy: **Microsoft products, OSI open source, two approved exceptions** (MongoDB Community Server, Dragonfly). Bicep for IaC; Podman or Rancher Desktop.
6. Engineering is split into four tracks (**FE, BE, DB, OPS**), each with a Core and an Advanced package; team size decides how many Advanced packages apply (2 → 0, 3 → any 2, 4 → all 4).
7. Flow: short-lived branches → `preview` (squash) → weekly release PR → `main` (merge commit) → version tag; `v0.1.0` end of Week 2, `v1.0.0` end of Week 12.
8. Every participant: own ≥ 1 package, evidence **≥ 40 hours**, review others' PRs weekly, keep an AI Engineering Journal.
9. Grade = **60% Team + 40% Individual**; **10 blocking items** cap the Team Score at 50 (see 15 §8).
10. All data synthetic, payments simulated, English everywhere, accessibility WCAG 2.2 AA.

## 4. How to use this pack

### 4.1 If you are a person
- **Today (≈ 20 min):** read this file, then `00-roadmap-main-steps.md` (what to do and when) and `01-overview.md`.
- **Recruiting teammates:** share `01`, `05` and `15 §6`; use `19 §2` for questions to the jury.
- **Week 1:** follow roadmap S1; use the repository's canonical templates and record decisions in [`../team/decision-register.md`](../team/decision-register.md).
- **Day to day:** open the track file you own (06 FE · 07 BE · 08 DB · 09 OPS) and the product files for the modules you build.
- **Reviewing a PR or release:** `14` (Git, DoD, weekly ritual) and `15 §8` (acceptance checklist).

### 4.2 If you are an AI assistant
The repository's canonical `.github/copilot-instructions.md` routes requirements work into this pack.
1. **Read this README, then `01-overview.md`.** Load further files only as needed (see §5 "Load when").
2. **Cite IDs.** When advising or writing PR/work-item text, reference requirement IDs (for example "Implements M4-03 and BE-C05").
3. **Respect levels.** MUST = mandatory; SHOULD = may be skipped only with a recorded justification (ADR or README); MAY = optional. Never present a MAY or SHOULD as a MUST.
4. **Separate spec from commentary.** Anything marked `[PACK NOTE]` is a suggestion, not a requirement.
5. **Never invent requirements.** If the pack does not say it, answer "not specified in the spec". Known unspecified items: session/token lifetimes (SEC-02), rate-limit thresholds (SEC-12), a coverage percentage (QA-04), a mandatory hosting platform, SKUs for Azure.
6. **Check decisions before proposing technology.** Read [`../team/decision-register.md`](../team/decision-register.md). If a decision is OPEN or provisional, offer allowed options and do not choose silently.
7. **Check licences before suggesting a library or tool:** `10 §6` (ARC-10) and verify against the package's own repository (AI-06). Redis, Terraform/OpenTofu, Docker Desktop, MediatR 13+, AutoMapper 15+, FluentAssertions 8+, ImageSharp, QuestPDF, Duende IdentityServer, NBomber are **not allowed**.
8. **Team-size-dependent answers:** state the answer for each size (2, 3, 4) unless D-01 is decided in the team decision register.
9. **No real personal data, no secrets** in prompts, examples or generated files.
10. **Prefer `requirements.csv`** for lookups (columns: id, area, level, scope, requirement, evidence, file).
11. **Do not edit requirement wording during ordinary work.** Propose official-source corrections through a dedicated resynchronization task.

### 4.3 Prompts you can paste
1. *"Read README.md and 00-roadmap-main-steps.md. Produce a dated Week-1 checklist for a team of {2|3|4} with kick-off on {date}, using the calendar worksheet in the roadmap."*
2. *"Using 02-product-m1-m4.md and 07-track-backend.md, write a feature spec (`../templates/feature-spec-template.md`) for M4-03 with table-driven tests per role. Cite requirement IDs."*
3. *"Review this PR diff against the pack: GIT-05, GIT-07, GIT-08, AI-07 and any relevant SEC IDs. List violations with IDs and the fix."*
4. *"Create backlog items for epic M5 from 03-product-m5-m7-px.md: one story per requirement row with Given/When/Then, an estimate and requirement IDs."*
5. *"Run the acceptance checklist (15 §8) against our repository state. List blocking gaps first."*
6. *"We decided {X}. Draft ADR-00N from `../templates/adr-template.md` using the constraints in the team decision register and file 10."*

## 5. File map

| File | Contents | Load when |
|---|---|---|
| `README.md` | This file: status, how to use, conventions, maintenance | always, first |
| `.github/copilot-instructions.md` | Auto-loaded instructions for Copilot (VS Code / CLI) when this folder is the workspace: task → file routing table and the rules | automatic |
| `00-roadmap-main-steps.md` | **Main steps S0–S7**, weekly ritual, team-size differences, gates, calendar worksheet | planning, "what next?" |
| `01-overview.md` | Summary, key dates, fixed vs. decided, learning outcomes, scope, assessment in brief, jury, spec history | always, second |
| `02-product-m1-m4.md` | M1 Identity, M2 Buildings and 2D map, M3 Leases, M4 Work orders (state machine) | building those modules |
| `03-product-m5-m7-px.md` | M5 Billing, M6 Notifications, M7 Audit and dashboards, PX cross-cutting rules | building those modules |
| `04-product-scenarios-roles-domain.md` | Personas, permissions matrix, Scenarios A and B, domain model, screens, seed data | authorization, data model, E2E tests, demo |
| `05-team-scope-ownership.md` | Tracks, scope by team size, OWN rules, effort model, 40-hour rule | choosing scope and ownership |
| `06-track-frontend.md` | FE Core + Advanced, Rendering Strategy Table, FE acceptance | owning/reviewing frontend |
| `07-track-backend.md` | BE Core + Advanced, thresholds, BE acceptance | owning/reviewing backend |
| `08-track-data.md` | DB Core + Advanced, SQL vs. NoSQL equivalents | owning/reviewing data |
| `09-track-devops.md` | OPS Core + Advanced, hosting rule | owning/reviewing CI/CD, containers, releases |
| `10-architecture-tech-policy.md` | ARC rules, reference architecture, request flow, API conventions, **technology and licence matrix** | architecture decisions, any new dependency |
| `11-security-privacy.md` | SEC-01..SEC-15 | security/privacy work, `docs/security/` evidence |
| `12-quality-testing.md` | QA rules, mandatory test levels, operability checklist | test strategy, CI gates |
| `13-ai-assisted-engineering.md` | AI rules, journal, specs, disclosure, prohibited practices | Copilot setup, journals, PR disclosure |
| `14-process-git-planning.md` | GIT/PRC rules, branch protection, weekly release ritual, DoD, planning milestones | repo setup, releases, Charter/plan |
| `15-deliverables-assessment-acceptance.md` | DEL rules, submission, grading, pitfalls, **acceptance checklist and blocking items** | submission, interview, grading questions |
| `16-environment-hosting-tools.md` | Dev environment, Copilot access, Azure/hosting, repo layout, suggested tools, learning links | environment and hosting |
| `17-extensions-faq-quickref.md` | Optional extensions X1–X7, FAQ, one-page quick reference | "may we…?" questions, quick lookups |
| `18-glossary-worked-examples.md` | Glossary, worked examples H.1–H.5 | unclear terms, examples of expected detail |
| `19-decisions-questions-risks.md` | Allowed decision options, jury-question catalogue and reusable risks | planning and risk review |
| `requirements.csv` | Static validated index with one row per requirement ID | lookups, backlog import and coverage audits |
| `PROVENANCE.md` | Authority, source version, authorship and repository adaptations | verifying trust and maintenance rules |
| `../team/decision-register.md` | Live team decisions and unresolved choices | before consequential technical or workflow choices |
| `../templates/` and `../../.github/` | Canonical repository templates | creating ADRs, specs and pull requests |

Rough size: 1.5–4.5K tokens per numbered file; the whole pack is about 55–60K tokens.

## 6. Conventions

**Requirement IDs (as in the spec)**

| Prefix | Area | Spec section | Pack file |
|---|---|---|---|
| M1–M7 | Product modules (for example M4-03) | 4.1–4.7 | 02, 03 |
| PX | Cross-cutting product requirements | 4.8 | 03 |
| OWN | Ownership and effort | 5.3 | 05 |
| FE / BE / DB / OPS (+ C = Core, A = Advanced) | Engineering packages (for example BE-C06, FE-A03) | 6.1–6.4 | 06–09 |
| ARC | Architecture | 7 | 10 |
| SEC | Security and privacy | 8 | 11 |
| QA | Testing and operability | 9 | 12 |
| AI | AI-assisted engineering | 10.2 | 13 |
| GIT / PRC | Git workflow, ways of working | 11 | 14 |
| DEL | Deliverables | 13 | 15 |
| X1–X7 | Optional extensions | Appendix F | 17 |
| LO1–LO10 | Learning outcomes (not requirements) | 2.3 | 01 |

**Pack-assigned IDs (not in the spec):** `BLK-01..BLK-10` (blocking acceptance items), `S0..S7` and `S1.1`-style task numbers (roadmap), `D-01..` (decisions), `Q1..` (jury questions), `R-01..` (risks).

**Levels:** MUST (mandatory; misses cost points) · SHOULD (strongly recommended; deviation needs a recorded justification) · MAY (optional, no penalty).
**Scopes:** CORE (every team) · ADVANCED (depends on team size, see 05 §3) · OPTIONAL (extensions, no base points) · ALL (applies to every team; used for general rules) · BLOCKING (acceptance item that caps the Team Score at 50).

**Requirement table schema (all files):** `| ID | Level | Scope | Requirement | Evidence |`. Product rows have `—` as evidence because acceptance criteria are listed per module.

**References inside the pack:** `10 §6` = file `10-…`, section 6. `spec §4.4` = section of the source document. Dates are ISO (`YYYY-MM-DD`). Hours are `h`.

## 7. Repository integration

- Canonical Copilot instructions: [`../../.github/copilot-instructions.md`](../../.github/copilot-instructions.md)
- Team decision register: [`../team/decision-register.md`](../team/decision-register.md)
- Team Charter: [`../team/charter.md`](../team/charter.md)
- Project plan: [`../team/plan.md`](../team/plan.md)
- Canonical templates: [`../templates/`](../templates/)
- Normal PR template: [`../../.github/pull_request_template.md`](../../.github/pull_request_template.md)
- Weekly release PR template: [`../../.github/PULL_REQUEST_TEMPLATE/release.md`](../../.github/PULL_REQUEST_TEMPLATE/release.md)

## 8. Maintenance

This repository stores a static, validated v1.4 snapshot. Ordinary feature work must not edit requirement wording or `requirements.csv`.

**Re-sync only when the official source changes**
1. Open the source; compare version and date with the `source` field above.
2. Create a dedicated work item and branch.
3. List the official changes since v1.4.
4. Update the affected topic files without altering unrelated requirements.
5. Regenerate and review `requirements.csv`.
6. Update `PROVENANCE.md`, `source`, `pack_version` and §10 below.
7. Obtain team review before merging.

## 9. Known gaps and uncertainties
- **Paraphrased, not verbatim** (see §2). Spot-check numbers against the source when they drive a decision.
- **Figures are redrawn** (floor map, state machine, reference architecture, ER overview) as Mermaid or tables; they are not copies of the spec's figures.
- **Section numbering:** the spec points to "Section 11.6" for effort evidence; the pack follows requirement IDs (PRC-06..PRC-08, in 14 §6).
- **Upload limits:** 5 MB per photo is an *example* in M4-01 and SEC-07; document the limit you enforce.
- **Documentation paths (DEL-03):** the pack treats them as required (safe default); Appendix B calls its layout an example (`19 §2 Q8`).
- **BLK IDs** are pack-assigned; the spec lists the blocking items without numbers.
- Source had no separate "work item template" or "bug template" in Appendix D (only D.1–D.8).

## 10. Pack history

| Version | Date | Change |
|---|---|---|
| 0.1.0 | 2026-11-06 | First build from requirements v1.4: 20 topic files, 8 templates, requirement index, roadmap S0–S7, decisions register. |
| 0.1.1 | 2026-11-06 | Added standalone Copilot routing and validation support. |
| 0.2.0 | 2026-11-23 | Imported as the canonical repository working specification; separated live team state, removed duplicate templates and unsupported tooling references, and retained `requirements.csv` as a static index. |

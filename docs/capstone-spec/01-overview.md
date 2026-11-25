---
title: Overview — project at a glance
source_sections: "Document control, 1, 1.1, 1.3, 2, 3.1, 3.3, 3.4, 14 (summary), version history"
load_when: "Always load this first (after README.md). Context for any capstone question."
related: [00-roadmap-main-steps.md, 05-team-scope-ownership.md, 15-deliverables-assessment-acceptance.md]
---

# Overview — project at a glance

## 1. Summary
Build the **Building Operations Platform**: a full-stack web platform that runs a residential building — units and a live 2D floor map, residents and leases, maintenance work orders, utility meters and monthly charges, announcements and notifications, dashboards and an audit trail. Delivered by a team of 2–4 AI-assisted engineers in 12 weeks. All data is synthetic; payments are simulated.

## 2. Key facts

| Area | Fact |
|---|---|
| What you build | Full-stack web platform for day-to-day operations of residential buildings (modules M1–M7). |
| Who builds it | Teams of **2–4** participants. Solo only with jury approval. |
| When | **12 weeks** of development from kick-off in **November 2026** (exact date confirmed by the jury). Demo Day at the end of the DevAcademy 2026–2027 edition. |
| Effort | Every participant MUST log **at least 40 hours** of owned, evidenced work. Core baseline ≈ 80–100 team-hours. Plan roughly **4–5 hours/week**. |
| Frontend | React **19.2+** with **Next.js 16+ App Router** or **TanStack Start 1.x**; TypeScript. |
| Backend | ASP.NET Core on **.NET 10 LTS**; controllers or Minimal APIs. |
| Database | SQL (PostgreSQL, SQL Server, Azure SQL) or NoSQL (MongoDB, Azure Cosmos DB, DocumentDB). Choice justified in an ADR. |
| Collaboration | GitHub or Azure DevOps. Short-lived branches → `preview` → weekly release PR → `main`. |
| Delivery | Containers and CI on every PR. Versioned images for merges into `preview` and weekly releases. |
| Azure | Recommended but optional, except when OPS Advanced applies. Each participant has **€150 Azure credit/month**. |
| Language | English for UI, code, comments, documentation, commits, PRs, work items (PX-09). |
| AI | AI-assisted engineering throughout the lifecycle is expected and assessed. AI features inside the product are optional (X4). |
| Assessment | Final grade = **60% Team Score + 40% Individual Score**. |

## 3. The three rules that matter most
1. **Ship a product, not a collection of screens.** Both signature scenarios (A and B) must work end-to-end on the Release environment.
2. **Own your track.** Each participant owns at least one engineering package and must be able to explain every decision and every line, including AI-generated code.
3. **Integrate small and often.** Short-lived branches into `preview` every week and one release PR into `main` every week.

## 4. Key dates

| Milestone | When |
|---|---|
| Kick-off / Week 1 | November 2026 — exact date confirmed by the jury `[OPEN]` |
| Team Charter, project plan, repository access for the jury | End of Week 1 |
| First weekly release `v0.1.0` | End of Week 2 |
| Release PRs (`preview` → `main`) | Every week from Week 2 |
| Final submission: tag `v1.0.0` on `main` | End of Week 12 |
| Demo Day + technical interviews | End of the DevAcademy 2026–2027 edition |

Policy: **no checkpoints, no late submissions.** Late submission is accepted only in extreme, documented circumstances approved by the jury. Contact the jury as soon as such a risk is known.

## 5. What is fixed and what the team decides

| Area | Fixed for every team | The team decides |
|---|---|---|
| Product | Residential-building domain; Core modules M1–M7; four roles; signature Scenarios A and B. | Product name, branding, tone, screen layout, navigation, usability details (see 04 §9 ideas). |
| Technology | React 19 with Next.js or TanStack Start; ASP.NET Core; SQL or NoSQL; GitHub or Azure DevOps; containers; all rules in 10 (technology and licensing). | Which framework of the allowed ones, API style, DB engine, libraries, component library, hosting approach — all within the technology rules. |
| Architecture | Modular monolith unless an alternative is justified; clear boundaries; business rules in the backend; all data access through the API. | Module/folder structure, internal patterns, caching strategy, background-job arrangement, real-time mechanism. |
| Data | Integrity, exact money, history, auditing, privacy rules. | The actual data model (the conceptual model in 04 §6 is only a starting point). |
| Process | Short-lived branches into `preview`; weekly release PRs; Definition of Done; effort logging. | Package ownership, work sequence, milestones, weekly rhythm. |
| Look and feel | Accessibility of core flows at **WCAG 2.2 Level AA**; responsiveness; consistency. | Visual design, colours, illustrations, animation, light/dark theme. |

Decision rule: if the spec does not prescribe it, the team decides. Record important decisions as ADRs (ARC-07). If unsure, ask the jury rather than assume.

## 6. Learning outcomes (all ten expected of every participant)

| ID | Learning outcome |
|---|---|
| LO1 | Model a business domain through entities, relationships, lifecycles and invariants; enforce them in application code and data storage. |
| LO2 | Build a modern React 19 frontend with an intentional rendering strategy across server rendering, streaming and client rendering; optimistic, accessible UX. |
| LO3 | Design, document and secure an ASP.NET Core API with consistent conventions, transactions, caching and background processing. |
| LO4 | Design a database for integrity and performance (constraints, indexes, transactions, programmable objects, or NoSQL equivalents). |
| LO5 | Collaborate through Git: short-lived branches, code review, weekly release cadence. |
| LO6 | Automate build, test, security scanning and deployment with CI/CD and containers. |
| LO7 | Apply security and privacy by design throughout. |
| LO8 | Test at appropriate levels; make the system operable (logs, traces, health checks, backups, runbooks). |
| LO9 | Use AI assistants effectively and responsibly across the lifecycle, including verifying AI output. |
| LO10 | Explain and defend technical decisions using ADRs, diagrams, demos and a technical interview. |

## 7. Product principles

| Principle | Meaning |
|---|---|
| Role-appropriate | Each role sees exactly the information and functionality it needs, and nothing more. |
| Trustworthy | Important changes are traceable, money stays exact, personal data is protected. |
| Live | The current condition of the building (units, issues, notifications) is visible as it changes. |
| Accessible and responsive | Usable with a keyboard, a screen reader and a phone. |

## 8. Scope

### 8.1 CORE modules — required for every team

| Module | Scope |
|---|---|
| M1 Identity, roles and access | Who a user is and what they may view or do; authorization enforced on every request. |
| M2 Buildings, floors, units and the 2D floor map | Physical building as structured data; live, interactive, accessible floor map. |
| M3 Residents, occupancy and leases | Who owns units, who lives in them, under which lease; full history. |
| M4 Maintenance requests and work orders | Flagship workflow: report → triage → assign → fix → confirm, governed by SLAs. |
| M5 Utility meters, monthly charges and payments | Meter readings and exact monthly statements with simulated payments. |
| M6 Announcements and notifications | The right message to the right people at the right time. |
| M7 Audit trail, dashboards and reporting | Who changed what and when; operational figures per role. |

### 8.2 OPTIONAL extensions — no base points (details: 17)

| ID | Extension |
|---|---|
| X1 | Visitors and access passes |
| X2 | Document library |
| X3 | 3D building view (never replaces the 2D map) |
| X4 | AI features inside the product (guardrails mandatory) |
| X5 | Amenity booking |
| X6 | Bilingual interface (English and Romanian) |
| X7 | Offline-capable technician application |

### 8.3 Out of scope

| Area | Constraint |
|---|---|
| Real payments | No real money, card data or bank integrations. All payment activity is simulated. |
| Physical access control | No hardware. |
| Real personal information | Prohibited. **All data MUST be synthetic.** |
| Native mobile apps | Excluded. A responsive web app is required. |
| Microservices | Not required. A modular monolith is recommended. |
| Complex hosting | Kubernetes and similar are unnecessary. Containers on a simple host are enough. |
| Unnecessary patterns | No event sourcing, CQRS frameworks, message broker "for appearance". Simple, well-structured code scores better. |
| Multi-company SaaS tenancy | One organisation managing multiple buildings. |
| Formal legal certification | Excluded, but privacy and security by design remain required. |

## 9. Assessment in brief (details: 15)
- **Final grade = 0.60 × Team Score (0–100) + 0.40 × Individual Score (0–100).** Pass ≥ 60; distinction ≥ 85; both subject to the gates below.
- Team Score categories: A Product 30 · B Architecture/security/data 20 · C Frontend/UX 15 · D DevOps/testing/operability 15 · E AI-assisted engineering 10 · F Collaboration/delivery 5 · G Documentation/demo 5.
- Individual Score: I1 Package delivery 40 · I2 Technical interview 35 · I3 Contribution/collaboration 15 · I4 AI journal/reflection 10.
- Gates: any **blocking** acceptance item missing at final submission caps the Team Score at **50**; a participant without **40 evidenced hours** cannot pass (unless the jury approves an exception).
- The jury grades the submitted **`v1.0.0`**; later changes are not graded.

## 10. Jury and communication
The jury grades, answers questions and approves exceptions. Use the approved program communication channel. Answers that affect every team are published as a new version of the requirements document.

| Jury member | Role |
|---|---|
| Alexandru-Razvan Olariu | Document author and jury member |
| Alexandru Grosu | Jury member |
| Sorin Duta | Jury member |

Rule: if a requirement is unclear, ask the jury before building. If you cannot wait, choose the simplest interpretation that satisfies it and record the choice in an ADR or the README.

## 11. Source document status and history
- Source: `DevAcademy 2026 Capstone requirements.docx`, **v1.4, 2 November 2026**. Document status in the source: **"Release candidate — final review by the jury before publication to participants."** `[PACK NOTE]` Expect further changes; see README "Re-sync procedure".

| Version | Date | Change summary |
|---|---|---|
| 1.0 | 20 Oct 2026 | First complete draft. |
| 1.1 | 29 Oct 2026 | Jury and contacts; checkpoint reviews removed; kick-off month, Demo Day and late-submission policy; Copilot and Azure access; hosting optional (required only with OPS Advanced); first-week guide; templates; glossary. |
| 1.2 | 30 Oct 2026 | Technology policy: only Microsoft products and open source (ARC-10, 10 §6). Redis → Valkey/Memcached/Dragonfly; Terraform → Bicep; NBomber and Flyway removed; Azure credit clarified as €150/month; English as working language; weekly effort guidance. |
| 1.3 | 30 Oct 2026 | Cache options Valkey/Memcached/Dragonfly; MongoDB allowed next to Cosmos DB and DocumentDB; IaC is Bicep only; local containers Podman or Rancher Desktop; approved source-available exceptions (MongoDB Community Server, Dragonfly). |
| 1.4 | 2 Nov 2026 | Reading aids; "In short" boxes; fixed-vs-yours (§5 here); ideas to make it your own; thin first slices; weekly time example; weekly self-check; demo tip; common pitfalls; filled PR example (H.5); one-page quick reference (J); new FAQ and glossary terms. |

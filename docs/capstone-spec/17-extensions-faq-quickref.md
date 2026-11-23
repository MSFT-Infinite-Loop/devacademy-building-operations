---
title: Optional extensions, FAQ and one-page quick reference
source_sections: "Appendix F (X1–X7), Appendix G (FAQ), Appendix J (quick reference)"
load_when: "Deciding whether/what to add beyond Core, answering a 'may we…?' question, or needing the one-page summary."
related: [01-overview.md, 15-deliverables-assessment-acceptance.md, 19-decisions-questions-risks.md]
---

# Optional extensions, FAQ and quick reference

## 1. Optional extensions X1–X7 (Appendix F)
Rules: **no base points**; cannot compensate for incomplete Core; must not break Core functionality; exceptional work may get separate **Demo Day recognition**. Default stance until Core and both scenarios are done: **build none**.

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| X1 | MAY | OPTIONAL | **Visitors and access passes:** residents pre-register visitors; QR access pass with an expiry time; building-desk check-in/check-out view; privacy-controlled visitor history; an expiry job. | — |
| X2 | MAY | OPTIONAL | **Document library:** documents attached to buildings, units, leases and work orders; classification, versioning, retention status, controlled downloads. | — |
| X3 | MAY | OPTIONAL | **3D building view** (for example with React Three Fiber) generated from the same layout and status data as the 2D map; unit drill-down; the 2D map stays the accessible fallback. | — |
| X4 | MAY | OPTIONAL | **AI features in the product:** for example natural-language search over records the user may access, maintenance-history summaries, announcement drafting help, category suggestions. The guardrails below are mandatory. | — |
| X5 | MAY | OPTIONAL | **Amenity booking** (laundry room, parking space, community room); DB constraints or locking prevent double booking. | — |
| X6 | MAY | OPTIONAL | **Bilingual interface** English and Romanian, with locale-aware dates, numbers and currencies. | — |
| X7 | MAY | OPTIONAL | **Offline-capable technician app** (PWA) queuing updates offline and syncing later, with conflict handling. | — |

**X4 guardrails (all mandatory if X4 is built):** provider abstraction · configuration and keys outside source code · clear labels on generated content · links to the source records behind generated content · authorization for every privileged operation · explicit user confirmation before privileged operations · no autonomous financial, lease or maintenance decisions · send only the minimum necessary data to the model · the model receives only data the current user may see · treat records and documents as untrusted content, not instructions (prompt-injection defence) · timeouts · rate limits · cost limits · graceful fallback when the provider is unavailable · documented limitations · test evidence.

## 2. FAQ (Appendix G)

**Communication and interpretation**
- *Who answers questions?* The jury (see 01 §10), by email or Teams. Answers affecting every team appear in a new version of the requirements document.
- *Working language?* English for UI, code, comments, docs, commits, PRs, work items.
- *A requirement is unclear?* Ask the jury. If work cannot wait, use the simplest interpretation that satisfies it and record it in an ADR or the README.
- *Where to start?* Section 1.2 (first week), then a thin Scenario A slice (see 14 §8).

**Stack and architecture**
- *Plain React SPA (Vite + React Router)?* **No.** React 19 with Next.js or TanStack Start is required because server-side rendering is a required learning outcome.
- *Controllers or Minimal APIs?* Either; choose one, justify in an ADR (BE-C01), use it consistently.
- *Backend-as-a-service instead of our own API?* **No.** The backend must be ASP.NET Core. Managed database and storage services are fine.
- *External identity provider?* Yes (Entra ID, Keycloak, …). The API must still enforce roles, building scopes and object-level authorization.
- *ORM such as EF Core?* Yes, but the DB package still requires programmable DB objects (procedures, views, triggers, or NoSQL equivalents).
- *UI libraries, templates, starter kits?* Yes if allowed under ARC-10 and declared in the README; domain logic must be yours.
- *Any library or tool?* **No.** Only Microsoft products, OSI-approved open source and the approved exceptions (see 10 §6). Ask the jury when unsure.

**Product design**
- *Change the theme (office building, student dorm)?* **No.** Same residential platform for fair comparison. You may choose name, branding, visual design and small product ideas.
- *How polished?* Clean, consistent, responsive, accessible; a component library is encouraged; usability over artistry.

**Hosting and local development**
- *Is Azure mandatory?* No — only hosting when OPS Advanced is in scope (€150/month credit per participant). Without hosting, the jury runs the Release version locally with one command (OPS-C04, OPS-C05).
- *Is Docker Desktop required?* No. Use Podman + Podman Desktop or Rancher Desktop.

**Planning, scope and submission**
- *Checkpoint reviews?* No. Define milestones under PRC-05; the jury watches weekly releases, the board and repository activity.
- *Cannot submit on time?* Late submissions are not accepted unless the jury approves an exception for extreme, documented circumstances; tell the jury as soon as the risk is known.
- *Which Advanced packages for a team of three?* Any two; reflect the owners' interests; record in the Team Charter in Week 1.
- *Is AI use mandatory?* AI-assisted engineering is expected and assessed (13). Building AI into the product is optional.
- *Change the database after development starts?* Only with a new ADR shared with the jury; decide early because late changes usually cost more than they save.
- *A team member leaves?* Notify the jury within one week (OWN-05); Advanced requirements are adjusted.
- *Share code between teams?* No — ideas yes; code, tests and documents must be your own.
- *How are hours verified?* The jury cross-checks the effort log against the board, PRs, reviews and documents; commits and lines of code are never used.
- *What does the jury inspect first?* README → `v1.0.0` running with demo accounts → Scenario A → Scenario B.
- *Finished Core early?* Strengthen evidence → deepen required Advanced packages → pick an optional extension.
- *Which version is graded?* The submitted `v1.0.0`; later changes do not count.

## 3. One-page quick reference (Appendix J)

| Item | Summary |
|---|---|
| Project | Building Operations Platform in **12 weeks**, team of **2–4** AI-assisted engineers; **7 modules, 4 roles, 2 scenarios** |
| Modules | M1 Identity · M2 Buildings and the 2D map · M3 Leases · M4 Work orders · M5 Billing · M6 Notifications · M7 Audit and dashboards |
| Roles | Administrator · Building Manager · Resident · Technician — enforced on every API request |
| Scenarios | A "A leak in apartment 4B" · B "Month-end at Aurora Residence" |
| Core stack | React 19 · Next.js or TanStack Start · ASP.NET Core (controllers or Minimal APIs) · .NET 10 · SQL or NoSQL · GitHub or Azure DevOps |
| Technology policy | Microsoft products, open source, and the two approved exceptions (MongoDB Community Server, Dragonfly) |
| Effort | ≥ 40 evidenced hours per participant; plan ≈ 4–5 h/week |
| Git flow | short-lived branch → PR → `preview` (squash) → weekly release PR `preview` → `main` (merge commit) → version tag |
| Definition of Done | Acceptance criteria met on Preview · reviewed · CI green · tests · docs updated · no new Critical/High vulnerabilities · accessibility checked · telemetry · hours logged |
| Every week | Each participant: merges ≥ 1 PR, reviews outside own track, journal entry, effort log. Team: release PR + version tag |
| Fixed schedule | Week 1 setup · every week from Week 2 release · end of Week 12 submit `v1.0.0` · end of edition Demo Day |

---
title: Decision options, jury-question catalogue and reusable risks
source_sections: "Pack-authored. Draws on 1.3, 5, 7.4, 11, 12, Appendix G and the gaps found while building the pack."
load_when: "Reviewing allowed decision options, deciding what to ask the jury, or assessing project risks."
related: [00-roadmap-main-steps.md, 05-team-scope-ownership.md, 10-architecture-tech-policy.md, 16-environment-hosting-tools.md, ../team/decision-register.md]
---

# Decision options, jury-question catalogue and reusable risks

`[PACK NOTE]` This file preserves the options, constraints, questions and risks identified while the requirements pack was created. It does not record live team status.

Current decisions and unresolved choices are maintained in [`../team/decision-register.md`](../team/decision-register.md).

## 1. Decision option catalogue

| ID | Decision | Options allowed by the spec | Constraints / related IDs | Needed by |
|---|---|---|---|---|
| D-01 | Team size and members | 2–4 (solo needs jury approval) | 05 §3; OWN-05/06 | end of S0 |
| D-02 | Package ownership (who owns FE/BE/DB/OPS Core and Advanced) | Any split; each participant owns ≥ 1 package | OWN-01; CODEOWNERS; Charter | S1 |
| D-03 | [T3 only] Which two Advanced packages | Any two of FE-A, BE-A, DB-A, OPS-A | Locked in Week 1; change needs jury approval; OPS Advanced ⇒ hosting mandatory | S1 |
| D-04 | Repository and board host | GitHub (+ Projects, Actions) or Azure DevOps (+ Boards, Pipelines) | GIT-01; OPS-C01/C02/C03; commit refs `#123` vs `AB#123`; private; jury read access | S1 |
| D-05 | Product name and branding | Free choice | Section 1.3 | S2 |
| D-06 | Frontend framework | Next.js 16+ (App Router) or TanStack Start 1.x | FE-C01 (ADR); React 19.2+; plain Vite SPA not allowed | S1 |
| D-07 | API style | Controllers or Minimal APIs | BE-C01 (ADR) | S1 |
| D-08 | Database engine and model | SQL: PostgreSQL, SQL Server, Azure SQL · NoSQL: MongoDB Community Server, Azure Cosmos DB, DocumentDB | DB-C01 (ADR comparing SQL/NoSQL). The domain is fundamentally relational; NoSQL must explain overlap and exact billing invariants. A late change needs a new ADR shared with the jury. | S1 |
| D-09 | Identity / authentication | ASP.NET Core Identity, Microsoft Entra ID, Keycloak, OpenIddict | BE-C04, SEC-02 (ADR); API still enforces roles, building scopes, object-level authz | S2 |
| D-10 | Caching approach | In Core: HybridCache/IMemoryCache/output caching. Distributed L2 (BE-A02): Valkey, Memcached, Dragonfly | BE-C07; ARC-07 (ADR); Redis not allowed | S3 |
| D-11 | Hosting and deployment | Local-only (publish images, one-command run) or hosted (Azure recommended; another host the jury can reach) | Mandatory if OPS Advanced is in scope; verify available Azure credit; ARC-07 (ADR) | S1 |
| D-12 | CI/CD platform | GitHub Actions or Azure Pipelines | Follows D-04; OPS-C03 | S1 |
| D-13 | Local container engine | Podman + Podman Desktop, or Rancher Desktop | OPS-C04; Docker Desktop not allowed | S1 |
| D-14 | Background jobs: host and mechanism | In API host or a worker container; BackgroundService / Hangfire / Quartz.NET | ARC-09; BE-C08 | S3 |
| D-15 | [ADV] Real-time mechanism | SignalR or SSE; backplane Azure SignalR Service, Valkey or Dragonfly (not Memcached) | FE-A03, BE-A04 | S5 |
| D-16 | Component library | Fluent UI React or shadcn/ui | FE-C01 notes; ARC-10 | S1 |
| D-17 | Release-captain rotation, weekly sync slot, working agreements | Team choice | Charter (PRC-01), PRC-03 | S1 |
| D-18 | Optional extensions (X1–X7) | None, or any after Core is done | No base points; cannot offset missing Core | S5 |

**Lower-level choices to make when needed:** validation library · API client generation (Kiota / openapi-typescript) · OpenAPI UI (Scalar / Swagger UI) · migration tool (EF Core migrations / DbUp) · synthetic data (Bogus) · load-test tool (k6 / Azure Load Testing / JMeter) · email sandbox (smtp4dev / Mailpit) · image processing (SkiaSharp) · PDF (Playwright print-to-PDF / PDFsharp).

## 2. Jury-question catalogue

Use only questions that remain unresolved in the team decision register.

| # | Question | Why it matters |
|---|---|---|
| Q1 | What is the exact kick-off date (start of Week 1) and the Demo Day date? | Calendar planning; the original source delegated confirmation to the jury. |
| Q2 | Is requirements v1.4 final? Where will newer versions be published and announced? | The repository pack must be resynchronized when the official source changes. |
| Q3 | Does preparation done before kick-off count towards the 40 evidenced hours, and may such material appear in repository history? | The original source did not specify this. |
| Q4 | Are public-holiday weeks treated differently for weekly release PRs and tags? | A 12-week window may cross public holidays. |
| Q5 | How is the stated Azure credit accessed or activated, and in which subscription? | Hosting plans depend on confirmed access and budget. |
| Q6 | Which repository host account or organization should teams use, and which identities should receive jury read access? | Repository creation, permissions and governance depend on this. |
| Q7 | By when must teams be formed, and can a team add a member later? | OWN-05 covers a member leaving, not joining. |
| Q8 | Are the DEL-03 documentation paths mandatory or examples? | Appendix B describes its layout as an example while DEL-03 lists locations. |
| Q9 | May a derived, structured summary of the requirements be stored in the team's private repository as AI context? | The source is internal to participants and the jury. |
| Q10 | Is "Week N" counted from the kick-off date or by calendar week? | This determines iteration and weekly release dates. |

Do not address or send jury communications from this file. Use the approved program channel and record only verified responses in the team decision register.

## 3. Reusable risks

| # | Risk | Impact | Mitigation |
|---|---|---|---|
| R-01 | Team composition changes | Scope, ownership and capacity may change | Keep ownership documented; notify the jury as required; adjust Advanced scope through the approved process |
| R-02 | A member leaves or is unavailable | Advanced scope and the 40 h per person are at risk | Notify the jury within one week (OWN-05); maintain cross-track reviews and shared architectural understanding (OWN-03) |
| R-03 | Weekly release cadence during holidays | Blocking item BLK-06 | Clarify holiday treatment; plan captain rota and capacity; maintain small releasable increments |
| R-04 | Official requirements change | Rework and stale repository guidance | Use a dedicated resynchronization task and update provenance before relying on changed requirements |
| R-05 | Late database or framework change | Costly rework | Decide through Week-1 ADRs and record consequences |
| R-06 | Hosting cost or complexity | Budget overrun and delivery risk | Use small tiers, scale-to-zero, budget alerts and least-privilege shared access |
| R-07 | Secret committed to history | Blocking item BLK-09 | Scan from the first commit and revoke/rotate immediately |
| R-08 | Weak individual evidence (< 40 h or fabricated-looking records) | Individual failure or integrity breach | Record effort weekly with direct evidence links |
| R-09 | AI-generated code nobody understands | Interview and integrity risk | Keep changes reviewable, read every diff, verify output and record lessons |
| R-10 | Scope creep into optional extensions | Core remains incomplete | Default to no extensions until Core and both scenarios pass on Release |
| R-11 | Scenarios A/B work only on a developer machine | Blocking items BLK-01/BLK-02 | Run E2E and smoke tests against the Release version |

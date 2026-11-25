# Repository instructions

## Authority and decision status

- The official DevAcademy capstone requirements document is the source of truth.
- The canonical repository working specification is `docs/capstone-spec/`; read its `README.md` and `PROVENANCE.md` before requirements-driven work.
- Load only the topic files relevant to the task. Use `docs/capstone-spec/01-overview.md` for general context and the routing table below for detail.
- Live team decisions are recorded in `docs/team/decision-register.md`, not in the requirements pack.
- Distinguish mandatory requirements, recommendations, team proposals, and unresolved decisions.
- Never invent approvals, contributors, decisions, evidence, hours, tests, pull requests, releases, or journal entries.
- Treat every value marked `TBD` as unresolved. Ask before making a consequential choice.
- Do not edit the static v1.4 requirement wording during ordinary feature work. Official-source changes require a dedicated resynchronization task.

## Requirements routing

| Task | Read |
|---|---|
| Planning, milestones, or what comes next | `docs/capstone-spec/00-roadmap-main-steps.md` |
| M1-M4 product work | `docs/capstone-spec/02-product-m1-m4.md` |
| M5-M7 and cross-cutting product work | `docs/capstone-spec/03-product-m5-m7-px.md` |
| Roles, scenarios, permissions, domain model, or seed data | `docs/capstone-spec/04-product-scenarios-roles-domain.md` |
| Ownership, package scope, or effort evidence | `docs/capstone-spec/05-team-scope-ownership.md` |
| FE, BE, DB, or OPS package work | `docs/capstone-spec/06-track-frontend.md` through `09-track-devops.md` |
| Architecture, technology, dependencies, or licences | `docs/capstone-spec/10-architecture-tech-policy.md` |
| Security, testing, or AI-assisted engineering | `docs/capstone-spec/11-security-privacy.md` through `13-ai-assisted-engineering.md` |
| Git workflow, releases, DoD, or planning process | `docs/capstone-spec/14-process-git-planning.md` |
| Deliverables, grading, or blocking acceptance items | `docs/capstone-spec/15-deliverables-assessment-acceptance.md` |
| Environment, hosting, tools, extensions, or terminology | `docs/capstone-spec/16-environment-hosting-tools.md` through `18-glossary-worked-examples.md` |
| Allowed decision options, jury-question catalogue, or reusable risks | `docs/capstone-spec/19-decisions-questions-risks.md` |
| Exact requirement lookup | `docs/capstone-spec/requirements.csv` |

## Fixed constraints

- Build the Building Operations Platform with Core modules M1-M7 and the four required roles.
- Enforce object-level authorization in the API; hiding UI controls is not authorization.
- Use synthetic data only. Never add real personal data, credentials, tokens, or secrets.
- Preserve exact monetary calculations and auditable history.
- Core user flows must target WCAG 2.2 AA.
- Check the approved technology and licence policy before adding dependencies.

## Engineering workflow

- Use English for code, UI, documentation, commits, pull requests, and work items.
- Link work to requirement IDs and GitHub issues where available.
- Keep changes focused and use short-lived branches from `preview`.
- Normal pull requests target `preview`; weekly release pull requests target `main`.
- Add or update tests, documentation, ADRs, and evidence when the change requires them.
- Disclose material AI assistance and explain how its output was verified.
- Do not claim a check passed unless it was actually run and its result is known.

## Safety and remote operations

- Do not create or modify remote issues, projects, permissions, hosted resources, releases, tags, or jury communications without explicit human approval.
- Do not silently choose package ownership, Advanced packages, frameworks, database, authentication, caching, or hosting.
- Surface failures explicitly; do not replace errors with success-shaped fallbacks.

## Build and test

Exact commands are TBD until the walking skeleton and ADRs exist. Read the root README and relevant project files, then use only commands that are present and verified in the repository.

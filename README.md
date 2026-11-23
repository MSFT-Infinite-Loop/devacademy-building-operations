# DevAcademy Building Operations

Private monorepo for the DevAcademy 2026-2027 Building Operations Platform capstone.

## Status

This repository is in pre-inception setup.

- Team: Carlos Natera, Didier Gbenou, Petar Ivanov, and George Neagoe (provisional until the Team Charter is approved)
- Repository workflow: GitHub-first proposal, pending team confirmation
- Package ownership: TBD
- Advanced packages: TBD
- Product branding: TBD
- Application architecture and technology choices: TBD through ADRs
- Kick-off and release dates: TBD

The official capstone requirements document is authoritative. Derived summaries and AI packs must not replace it.

## Fixed project scope

The team must deliver the seven Core modules:

1. Identity, accounts, scoped roles, and authorization
2. Buildings, floors, units, and an accessible data-driven 2D floor map
3. Persons, ownership, occupancy history, and leases
4. Maintenance requests and work orders
5. Meters, readings, tariffs, billing, and simulated payments
6. Announcements and reliable in-app notifications
7. Audit, role dashboards, and CSV reporting

## Repository layout

```text
.github/       GitHub templates, Copilot instructions, prompts, and later workflows
docs/          Team, architecture, feature, AI, security, testing, and operations evidence
infra/         Containers, deployment, and infrastructure as code
src/           Product source code
tests/         Automated tests
```

See [docs/README.md](docs/README.md) for the documentation index.

## Local development

Build, test, and startup commands are TBD until the team records the relevant architecture decisions. Do not invent or publish commands before they are verified.

## Contribution workflow

The requirements prescribe short-lived branches into `preview`, followed by weekly release pull requests from `preview` to `main`. Detailed branch rules, review requirements, and release responsibilities will be confirmed in the Team Charter before implementation begins.

## Requirements material

The canonical repository working specification is in [`docs/capstone-spec/`](docs/capstone-spec/README.md).

- The official DevAcademy requirements remain the conflict-resolution authority.
- [`docs/capstone-spec/PROVENANCE.md`](docs/capstone-spec/PROVENANCE.md) records source version, authorship and repository adaptations.
- [`docs/team/decision-register.md`](docs/team/decision-register.md) records live team choices and unresolved decisions.
- Requirement IDs, levels and scopes must remain traceable in issues, specifications, ADRs and pull requests.

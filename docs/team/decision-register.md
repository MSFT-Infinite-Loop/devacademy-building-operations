# Team decision register

- **Status:** Active
- **Last updated:** 2026-11-23
- **Purpose:** Canonical record of live team decisions, proposals, and unresolved choices

The official DevAcademy requirements define the allowed and mandatory boundaries. This register records the team's choices within those boundaries.

## Status definitions

- **Decided:** A choice has been explicitly made.
- **Provisional:** The current direction is usable for planning but still requires team confirmation or supporting evidence.
- **Open:** No choice has been made.
- **Jury-dependent:** The team requires a jury or program decision.

Do not treat a provisional or open entry as approved.

## Decision register

| ID | Decision | Status | Current position | Evidence or follow-up |
|---|---|---|---|---|
| D-01 | Team size and members | Provisional | Carlos Natera, Didier Gbenou, and Petar Ivanov; confirm in the Team Charter | `docs/team/charter.md` |
| D-02 | Core and Advanced package ownership | Open | TBD | GitHub issue #2 |
| D-03 | Two Advanced packages for a three-person team | Open | TBD | GitHub issue #2 |
| D-04 | Repository and board host | Decided | Private GitHub organization `MSFT-Infinite-Loop`, organization repository, and organization Project | GitHub issue #4 |
| D-05 | Product name and branding | Provisional | `Infinite Loop Building Operations Platform` | Confirm in the Team Charter |
| D-06 | Frontend framework | Open | Next.js 16+ or TanStack Start 1.x | Frontend ADR |
| D-07 | API style | Open | Controllers or Minimal APIs | API-style ADR |
| D-08 | Database engine and model | Open | TBD from the allowed set | Database ADR |
| D-09 | Identity and authentication | Open | TBD from the allowed set | Authentication ADR |
| D-10 | Caching approach | Open | TBD | Caching ADR |
| D-11 | Hosting and deployment | Open | TBD | Hosting/deployment ADR |
| D-12 | CI/CD platform | Provisional | GitHub Actions; organization-hosted runner test succeeded | GitHub issue #4 and workflow-run evidence |
| D-13 | Local container engine | Open | Podman Desktop or Rancher Desktop | GitHub issue #8 |
| D-14 | Background-job host and mechanism | Open | TBD | Architecture decision when needed |
| D-15 | Advanced real-time mechanism | Open | TBD if relevant to selected Advanced packages | Architecture decision when needed |
| D-16 | Frontend component library | Open | TBD | Frontend ADR |
| D-17 | Weekly sync, release-captain rotation, and working agreements | Open | TBD | Team Charter |
| D-18 | Optional extensions | Provisional | None until Core and both signature scenarios work | Revisit after Core completion |
| D-19 | Requirements authority model | Decided | The repository pack is the canonical working specification; official DevAcademy requirements v1.4 remain the conflict-resolution authority | `docs/capstone-spec/PROVENANCE.md` |
| D-20 | Effort evidence model | Decided | Structured effort comments on leaf GitHub issues; `Completed Hours` stores the verified eligible total | GitHub issue #10 |
| D-21 | Pull-request readiness gate | Decided | Continue committing on the feature branch; create a PR only after the branch owner reviews the final diff and explicitly declares it ready | GitHub issues #4 and #10 |
| D-22 | Requirements-pack contact data | Decided | Retain necessary names and roles; remove personal email addresses before import | Pack-import review |
| D-23 | Requirements-pack templates | Decided | Maintain one canonical repository template set; reconcile pack requirements into it and omit duplicate active templates from the imported pack | Pack-import review |
| D-24 | Requirements-pack generated files | Decided | Commit `requirements.csv` as the static structured index; do not generate or commit `CAPSTONE-FULL.md` | Pack-import review |
| D-25 | Requirements-pack Scout references | Decided | Remove unsupported Scout and `/devacademy-capstone` references; rely on canonical repository Copilot instructions | Pack-import review |
| D-26 | Requirements-pack effort template | Decided | Preserve all effort-evidence options allowed by the requirements; omit the unused CSV template and point to the GitHub-native team decision | D-20 and pack-import review |
| D-27 | Pack file 19 integration | Decided | Keep the decision-option catalogue, jury questions, and reusable risks; remove live team state, contact details, worksheets, and draft addressed emails; link to this register | Pack-import review |
| D-28 | Requirements-pack mutability | Decided | Import README, files 00–19, and `requirements.csv` as an immutable validated v1.4 snapshot; omit validator and generation tooling | Pack-import review |
| D-29 | Requirements-pack authorship attribution | Decided | Credit Petar Ivanov prominently in `docs/capstone-spec/PROVENANCE.md`; Carlos authors the import commit; do not add a Petar co-author trailer without explicit consent | Pack-import review |
| D-30 | Copilot requirements routing | Decided | Add concise routing to the canonical repository Copilot instructions and load only relevant pack files per task; do not copy the full standalone pack instructions | Pack-import review |
| D-31 | Official requirements document storage | Decided | Store version/date/status metadata only; keep the official document in its approved external location | `docs/capstone-spec/PROVENANCE.md` |
| D-32 | Stale pack status snapshots | Decided | Remove team-specific snapshot statements from the imported pack and direct readers to the canonical team decision register | Pack-import review |
| D-33 | Weekly release PR template | Decided | Maintain the canonical release PR template at `.github/PULL_REQUEST_TEMPLATE/release.md` for GitHub-prefilled `preview` to `main` release PRs | Pack-import review |
| D-34 | Requirements-pack row integrity | Decided | Preserve all 234 validated requirement rows exactly during import; adapt only surrounding guidance and repository integration material | Pack-import review |

## Maintenance

1. Update this register when a decision changes status.
2. Link material architecture decisions to the accepted ADR.
3. Link working-agreement decisions to the approved Team Charter.
4. Record superseded decisions instead of silently deleting their history.
5. Update repository AI instructions when a decision changes architecture, commands, security rules, or workflow.

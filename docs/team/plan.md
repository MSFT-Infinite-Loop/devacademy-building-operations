# Project plan: TBD

- **Status:** Draft
- **Last updated:** 2026-11-23
- **Kick-off date:** TBD
- **Weekly release day:** TBD

## Milestones

| Target | Milestone | Modules or packages | Owner | Status |
|---|---|---|---|---|
| Week 1 | Charter, plan, repository governance, backlog, and ADR proposals | Team | TBD | Not started |
| Week 2 | Walking skeleton and `v0.1.0` | FE, BE, DB, OPS | TBD | Not started |
| Weeks 3-5 | Foundations | M1-M3 and early vertical slices | TBD | Not started |
| Weeks 6-8 | Core workflows | M4-M7 and both signature scenarios | TBD | Not started |
| Weeks 9-10 | Advanced depth and hardening | Selected Advanced packages | TBD | Not started |
| Week 11 | Stabilization and evidence audit | Team | TBD | Not started |
| Week 12 | `v1.0.0` and submission | Team | TBD | Not started |

These milestones are planning guidance until the team approves them.

## Build order and dependencies

TBD after package ownership and initial architecture decisions.

## Risks and mitigations

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| The GitHub organization is on Free | Private `main` and `preview` cannot be protected as required by GIT-06 | Resolve through issue #4 by upgrading the organization plan or selecting another approved enforcement mechanism | Carlos |
| The requirements pack is derived | A conflict with the official source could misdirect implementation | Keep provenance explicit; the official source wins conflicts; resynchronize through a dedicated reviewed task | Team |
| Package ownership is unresolved | Work may start without accountable owners | Decide and record ownership in Week 1 | Team |
| Technology decisions are unresolved | Premature scaffolding may constrain the architecture | Use timeboxed investigations and ADRs | Team |

## Plan changes

| Date | What changed | Why | Approved by |
|---|---|---|---|
| 2026-11-10 | Created initial draft | Prepare for the first team meeting | Pending |

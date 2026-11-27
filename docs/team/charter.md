# Infinite Loop Team Charter

- **Status:** Draft for team review
- **Last updated:** 2026-11-27
- **Approval:** Not yet approved
- **Work item:** [GitHub issue #2](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/2)

This draft records the proposed charter. `TBD` entries need confirmation, and the charter is not approved until all four members have signed off.

## Members and package ownership

| Member | GitHub handle | Core package ownership | Advanced package ownership | Usual availability |
|---|---|---|---|---|
| Carlos Natera | `naterac83` | FE Core | FE Advanced | About 8 hours/week, GMT; working windows TBD |
| Didier Gbenou | `didiergbenou-ms` | OPS Core | OPS Advanced | TBD |
| Petar Ivanov | `petarivanov-msft` | BE Core | BE Advanced | About 8 hours/week, London time; working windows TBD |
| George Neagoe | `geneagoedev` | DB Core | DB Advanced | TBD |

Each owner is the primary author for their packages. Once approved, mirror the assignments in `CODEOWNERS` through [repository governance issue #4](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/4). During backlog planning, pick one UI-to-API-to-database slice per member, link it to a GitHub issue, and coordinate with the relevant track owners.

## Team scope

- Team size: 4
- Product: Infinite Loop Building Operations Platform
- Required modules: M1-M7
- Required Core packages: FE, BE, DB, OPS
- Required Advanced packages: FE Advanced, BE Advanced, DB Advanced, OPS Advanced
- OPS Advanced requires hosted Preview and Release environments. The hosting choice is tracked separately.

## Goals and learning objectives

| Member | Strengths | Learning objectives |
|---|---|---|
| Carlos Natera | Building apps and platforms with AI assistance; hands-on experience with React and TypeScript projects. | Develop a systematic understanding of frontend engineering and learn to measure and improve performance and user experience. |
| Didier Gbenou | TBD | TBD |
| Petar Ivanov | Azure troubleshooting and diagnostics (Azure Arc, Update Manager, and Automation), Kusto/KQL, and telemetry analysis. | Build an ASP.NET Core backend end to end, including authentication, caching, the outbox pattern, and real-time features. |
| George Neagoe | TBD | TBD |

## Communication and availability

- Use Microsoft Teams for day-to-day coordination. Acknowledge routine messages within one working day; acknowledgement does not mean resolution. Do not expect replies outside agreed availability.
- Flag blockers in Teams as soon as they are identified, tag the relevant track owner, and link the GitHub issue. If there is no path forward by the next working day, raise the blocker with the whole team.
- Meet every morning from 10:30 to 11:30 GMT.
- Keep one dated notes file per weekly check-in at `docs/team/meetings/YYYY-MM-DD.md`. Record decisions, risks, blockers, and action owners and due dates.
- If you cannot attend the check-in, post an update in Teams beforehand and catch up from the notes afterward.

## Decisions and conflict resolution

- Seek consensus first. Track owners make routine decisions within their tracks after consulting affected teammates.
- Bring unresolved cross-track disagreements to the team. An ordinary cross-track decision needs three of four votes to pass. If it does not reach that threshold, leave it open and revisit it at the next sync. Record the rationale and any dissent in the notes.
- Adopt or amend this charter through a GitHub PR with explicit, dated agreement from all four members. The PR author can record their agreement without approving their own PR. The ordinary voting rule does not replace charter sign-off.

## Repository visibility and governance

The central monorepo is public under the [D-35 exception](decision-register.md#d-35-public-repository-exception) to the private-repository clauses of GIT-01 and OPS-C01. Alexandru-Razvan Olariu approved the change in the 20 November 2026 meeting, as reported by Carlos on 27 November; a public-safe written approval reference remains pending. This exception does not approve this charter or waive other requirements.

Public visibility makes GitHub Free code-owner review requests and branch protection available; it does not configure them. Complete and verify the [GIT-06 protections](../capstone-spec/14-process-git-planning.md#3-branch-model-and-mandatory-branch-protection) through [issue #4](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/4), and mirror package assignments in CODEOWNERS only after charter approval. Passing required CI and the review rules below remain mandatory.

Public content must contain only synthetic application data and no secrets, private communications, or personal contact details. Do not publish the official requirements document or unapproved third-party material. Verify secret scanning and push protection, and retain actual full-history scan evidence in [issue #17](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/issues/17); availability of a scanner is not evidence of a clean history.

## Pull requests and reviews

| PR | Merge method | Minimum non-author approvals |
|---|---|---|
| Short-lived branch into `preview` | Squash merge | 1 |
| Weekly release from `preview` into `main` | Merge commit | 2 |

Both require passing CI and linked work items. Aim for a first review or an estimated review time within one working day. Each member integrates into `preview` and submits a review outside their track at least once per week.

## Release-captain rotation

Target Thursday releases every week from Week 2. Repeat this four-week rotation:

| Week | Captain |
|---|---|
| 2 | Carlos Natera |
| 3 | Petar Ivanov |
| 4 | Didier Gbenou |
| 5 | George Neagoe |

The captain coordinates the release PR, Preview verification, tagging, release notes, and Release smoke-test follow-up. Coordinate coverage in Teams and record any agreed swaps in the weekly notes.

## Definition of Done

Use the [capstone Definition of Done](../capstone-spec/14-process-git-planning.md#7-definition-of-done-prc-04-qa-09) as the baseline:

- Acceptance criteria are met and verified on Preview; relevant tests pass and CI is green.
- Code is reviewed and merged through the agreed workflow.
- Relevant documentation and ADRs are current.
- Security and privacy impacts are checked, and there are no new unresolved Critical or High security findings.
- Accessibility is checked for UI changes; new flows have appropriate logging and telemetry.
- Material AI assistance is disclosed and verified. Confirm that AI-generated tests fail when the behavior under test is broken.
- The linked work item is closed with evidence and structured effort recorded; verified eligible hours are reflected in `Completed Hours`.

## Missing information and approval steps

- **Didier and George:** Add a review comment or suggest edits to your rows with your approximate weekly hours, usual working windows and time zone, one or two strengths for your track, and one capstone learning goal. Share scheduling conflicts that affect coverage in Teams without including personal details in the charter.
- **Carlos and Petar:** Confirm your usual working windows.
- **All members:** Agree where each [AI Engineering Journal](../templates/ai-journal-entry.md) will live, and check release-captain coverage against the team calendar.
- Check in the first dated meeting notes and link them, the charter PR, and all four dated sign-offs in issue #2. Requesting review does not itself approve the charter.

## Approval record

| Member | Decision | Date | Evidence |
|---|---|---|---|
| Carlos Natera | Pending | TBD | TBD |
| Didier Gbenou | Pending | TBD | TBD |
| Petar Ivanov | Pending | TBD | TBD |
| George Neagoe | Pending | TBD | TBD |

# Project and branch workflow

## Repository and Project

- Repository: `MSFT-Infinite-Loop/devacademy-building-operations`
- Project owner: `MSFT-Infinite-Loop`
- Project number: `1`
- Project title: `Infinite Loop Building Operations Platform` (provisional)

The former user-owned Project is closed and must not be updated.

The confirmed four-person scope includes FE, BE, DB, and OPS Core plus all four Advanced packages. Package ownership remains governed by the approved Team Charter.

Resolve current IDs and options from GitHub rather than hardcoding GraphQL IDs.

## Project fields

| Field | Purpose |
|---|---|
| Status | Workflow state |
| Priority | Delivery priority: P0-P3 |
| Size | Relative complexity: XS-XL |
| Iteration | Week 1-Week 12 |
| Engineering Track | FE, BE, DB, OPS, or Cross-cutting |
| Package | Core or Advanced package classification |
| Requirement IDs | Requirements traceability |
| Estimated Hours | Planned total effort for the item |
| Completed Hours | Sum of eligible, non-superseded structured effort comments on the leaf issue |
| Start date / Target date | Scheduling and roadmap |

`Estimate` is a redundant template field and should not be used. Marker-tagged effort comments on leaf issues are authoritative; `Completed Hours` is their verified sum.

## Status gates

| Transition | Required evidence |
|---|---|
| Backlog -> Ready | Scope and acceptance criteria are clear; requirement IDs, dependencies, blockers, iteration, track, and package are recorded; work can start. |
| Ready -> In progress | An assignee is identified. If repository changes are expected, a compliant branch exists or its creation is explicitly approved. |
| In progress -> In review | Deliverables are ready for verification. Repository changes have a linked PR targeting `preview`; relevant checks and evidence are available. |
| In review -> Done | Acceptance criteria and Definition of Done are verified; required review and checks passed; changes are merged appropriately; documentation, AI disclosure, evidence, and effort are current. |
| Open item -> Backlog | Work is intentionally decommitted or requires material refinement; explain why. Reopen a closed issue explicitly before changing its board status. |
| Closed/Done -> Ready | Work was reopened and is defined but not actively being changed. |
| Closed/Done -> In progress | Work was reopened and active corrective work has begun on a compliant branch when needed. |

Project automation currently:

- sets newly added items to `Backlog`;
- sets closed items and merged pull requests to `Done`;
- closes an issue when its Project status becomes `Done`;
- returns reopened items to `Ready`;
- sets items with requested code changes to `In progress`.

Automation does not verify acceptance criteria. Override an incorrect automated status after reviewing evidence.

## Branch model

### Normal work

1. Fetch the remote and start from current `preview`.
2. Create a short-lived branch:
   - `feature/<alias>/<issue>-<description>`
   - `fix/<alias>/<issue>-<description>`
   - `docs/<alias>/<issue>-<description>`
   - another approved type such as `test`, `refactor`, `chore`, or `spike`
3. Keep the branch ideally at or below three working days.
4. Open a focused PR targeting `preview`.
5. Link the work item explicitly and use `Refs #<number>` in the PR and squash message. Closing keywords do not close issues on merge into non-default `preview` and may close them later on `main`. Complete the issue separately after verifying its Definition of Done.
6. Require CI and human review.
7. Squash-merge the normal PR into `preview`.

Never commit normal work directly to `preview` or `main`.

### Weekly release

- Open one PR from `preview` to `main` from Week 2.
- Use a merge commit, never squash or rebase.
- Obtain the required approvals and checks.
- Tag the resulting `main` commit and preserve release and smoke-test evidence.

### Hotfix

- Branch from `main`.
- Review and merge into `main` using the approved hotfix process.
- Back-merge `main` into `preview`.

The skill may identify a missing or noncompliant branch and propose corrective steps. It must not merge, force-push, bypass protection, or rewrite shared history.

## Evidence rules

Useful evidence includes:

- reviewed repository documents or ADRs;
- linked commits and pull requests;
- pull-request reviews and required checks;
- exact test commands and results;
- workflow-run and deployment links;
- verified GitHub settings;
- screenshots where required;
- marker-tagged structured effort comments on the leaf issue;
- confirmed communications after they were sent.

Insufficient evidence includes:

- intention to perform work later;
- an unchecked or unexplained claim;
- a generated document that was not reviewed;
- a PR merge with no proof of non-code acceptance criteria;
- inferred hours from commits or elapsed time;
- AI-generated journal content describing events that did not occur.

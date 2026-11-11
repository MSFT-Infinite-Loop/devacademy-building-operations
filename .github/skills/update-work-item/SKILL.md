---
name: update-work-item
description: "Use when: reviewing, starting, updating, completing, closing, or moving a GitHub issue or Project work item; validating acceptance checks, evidence, Definition of Done, branches, pull requests, estimates, or hours."
argument-hint: "Issue number or URL and requested action"
user-invocable: true
disable-model-invocation: false
---

# Update Work Item

Review a repository issue and its evidence before proposing or applying a safe, auditable update.

Read [the Project and branch workflow](./references/project-workflow.md) before evaluating a transition. Use [the update proposal template](./assets/update-proposal.md) to present findings.

## Non-negotiable safeguards

- Start read-only. Do not modify GitHub or repository files while gathering evidence.
- Never infer or fabricate acceptance, approvals, tests, reviews, hours, journal entries, releases, or communications.
- A merged pull request alone does not prove every acceptance check or the Definition of Done.
- Treat missing evidence as `Unknown` or `Missing`, never as passed.
- Never assign unresolved package ownership or make architecture decisions through a work-item update.
- Obtain explicit human confirmation immediately before every batch of remote writes.
- Do not merge pull requests, create releases, change permissions, or alter branch protections through this skill.

## Inputs

Identify:

1. Issue number or URL.
2. Requested action, such as review, start, add evidence, move to review, complete, reopen, or refresh Project fields.
3. Any user-supplied facts that cannot be discovered, especially actual hours.

Ask for missing inputs. Do not guess.

## Procedure

### 1. Load repository context

Read:

- `.github/copilot-instructions.md`;
- the target issue, comments, sub-issues, assignees, and Project fields;
- `docs/team/charter.md` and relevant ADRs or specifications;
- linked pull requests, reviews, checks, commits, and workflow runs;
- marker-tagged effort and correction comments plus the current `Completed Hours`.

Use the official requirements or an approved repository summary to interpret requirement IDs.

### 2. Establish current state

Report:

- issue state and Project status;
- iteration, priority, track, package, assignees, estimates, and dates;
- acceptance checks already selected;
- linked branches and pull requests;
- parent and sub-issue progress;
- evidence links and unresolved blockers.

Do not treat a checked box as verified until its evidence is inspected.

### 3. Check branch and pull-request compliance

Apply the gates in [the Project and branch workflow](./references/project-workflow.md).

For repository-changing work:

- `Ready -> In progress` requires a compliant short-lived branch from current `preview`, or an explicit plan to create one.
- `In progress -> In review` requires a linked pull request targeting `preview`, except for the weekly release pull request.
- `In review -> Done` requires the appropriate review, merge, checks, documentation, and evidence.

Planning-only work may not require a branch, but its decision or evidence must still be stored in the repository when required.

### 4. Evaluate acceptance and evidence

Classify every acceptance check:

- `Verified`: direct evidence proves the check.
- `Missing`: evidence should exist but does not.
- `Unknown`: available information is insufficient.
- `Not applicable`: justified for this item.

Also evaluate the repository Definition of Done. Do not select `Done` while any mandatory check is Missing or Unknown.

For hours:

- direct new effort recording to the repository Log Effort skill;
- calculate `Completed Hours` only from eligible, non-superseded structured effort comments;
- leave parent `Completed Hours` empty to avoid double counting;
- never estimate actual hours from commits, diffs, elapsed time, or chat history.

### 5. Present a proposed update

Use [the update proposal template](./assets/update-proposal.md).

Show the exact proposed changes:

- acceptance checkboxes to select or clear;
- evidence links or comments to add;
- Project field changes;
- status transition;
- issue closure or reopening effect;
- blockers that prevent the requested transition.

If no write is justified, report that and stop.

### 6. Confirm immediately before writing

Use the available user-input tool to request approval for the exact proposed batch.

The confirmation must name:

- the issue;
- every checkbox or evidence change;
- every Project field change;
- the resulting status and open/closed state.

If the user changes the proposal, reassess affected gates before asking again.

### 7. Apply minimal changes

After approval:

- preserve unrelated issue text and formatting;
- select only verified acceptance checks;
- add evidence without duplicating existing links;
- update only approved Project fields;
- let the configured `Done` workflow close the issue;
- leave owner, estimates, and hours unchanged unless explicitly approved.

For a parent issue, do not move it to `Done` until all required sub-issues are complete or an approved exception is documented.

### 8. Verify and report

Read the issue and Project item again. Verify:

- expected fields and checkboxes changed;
- automation produced the expected open or closed state;
- no unrelated content changed;
- the final state matches the approved proposal.

Report links to the updated issue and evidence. Surface any partial or failed update explicitly.

---
name: log-effort
description: "Use when: recording, validating, correcting, or synchronizing evidenced work hours for a GitHub issue; updating docs/team/effort-log.csv; or recalculating a Project item's Completed Hours."
argument-hint: "record or sync, issue number, actual hours, and evidence"
user-invocable: true
disable-model-invocation: false
---

# Log Effort

Record actual, evidence-backed effort against the most specific work item and synchronize its GitHub Project summary without double counting.

Read [the effort policy](./references/effort-policy.md) before proposing a change. Use [the proposal template](./assets/effort-entry-proposal.md) for every write.

## Modes

### Record

Append one verified row to `docs/team/effort-log.csv` through a compliant feature branch and pull request.

Recording a row does not immediately update the Project `Completed Hours` field. The CSV change must first be merged into `preview`.

### Sync

Read the authoritative CSV from `preview`, calculate the verified total for one leaf work item, and propose the corresponding Project `Completed Hours` update.

Do not sync unmerged rows from a feature branch.

## Non-negotiable safeguards

- Never infer hours from commits, diffs, chat duration, calendar time, timestamps, or elapsed tool execution.
- Never create a journal entry or effort row describing work that did not occur.
- Never duplicate child-item hours on a parent issue.
- Never add the same effort entry twice.
- Never commit directly to `preview` or `main`.
- Never update `Completed Hours` from an unmerged effort entry.
- Obtain explicit human confirmation immediately before file, commit, push, pull-request, or Project writes.
- Do not decide whether pre-kick-off effort counts toward the graded minimum unless an approved decision exists.

## Record procedure

### 1. Gather required facts

Ask for every missing value:

- date in `YYYY-MM-DD`;
- participant's agreed display name;
- leaf issue number;
- package;
- activity;
- actual hours;
- evidence link.

The user must supply actual hours. Do not suggest a value.

### 2. Verify the target and evidence

Read the issue and Project item. Confirm:

- the issue exists and is the most specific applicable work item;
- the participant and package do not contradict the approved Team Charter;
- the activity is allowed by [the effort policy](./references/effort-policy.md);
- the evidence exists and supports the claimed activity;
- the row is not already in the CSV.

If package ownership is unresolved, use `Cross-cutting` only for genuinely cross-cutting work. Otherwise stop and ask.

### 3. Check pre-kick-off status

The official Week 1 start is 2026-11-15.

For earlier work:

- record it accurately for auditability;
- mark its eligibility as unresolved in the proposal;
- do not include it in `Completed Hours` or the graded-hours total until the jury decision is recorded.

Do not alter the CSV schema to encode eligibility without a team decision.

### 4. Check the branch plan

Prefer adding the effort row to the same compliant branch and pull request as the work it evidences.

If that branch is unavailable or already merged:

1. fetch the remote;
2. start from current `preview`;
3. create `docs/<alias>/<issue>-log-effort`;
4. append and validate the row;
5. open a focused pull request to `preview`.

Never add effort directly on `preview` or `main`.

### 5. Present and confirm the record proposal

Use [the proposal template](./assets/effort-entry-proposal.md). Show:

- the exact CSV row;
- duplicate-check result;
- evidence verification;
- branch and pull-request plan;
- pre-kick-off eligibility;
- confirmation that `Completed Hours` will not change yet.

Use the available user-input tool to approve the exact row and write plan.

### 6. Append and validate

After approval:

1. append exactly one CSV row;
2. preserve the existing header and rows;
3. quote values using standard CSV rules;
4. run:

   ```text
   python .github/skills/log-effort/scripts/validate_effort_log.py
   python .github/skills/log-effort/scripts/test_validate_effort_log.py
   ```

5. inspect the diff for unrelated changes;
6. commit using the repository convention and reference the issue;
7. push and open or update the pull request only as approved.

Do not check the PR's effort-recorded box until the row is present in that PR.

### 7. Verify

Read the CSV from the branch and the pull request. Confirm the exact approved row is present once and validation passed.

Report that Project synchronization remains pending until merge into `preview`.

## Sync procedure

### 1. Read authoritative state

Fetch the remote and read `docs/team/effort-log.csv` from `origin/preview`, not from a feature branch.

Run the validator and obtain eligible and provisional totals:

```text
python .github/skills/log-effort/scripts/validate_effort_log.py --json --eligible-from 2026-11-15
```

Exclude pre-kick-off rows while their eligibility remains unresolved.

### 2. Compare Project state

Read the issue's Project item and compare:

- current `Completed Hours`;
- calculated eligible CSV total;
- current status and parent relationship.

Never add the total to the existing value. Replace it with the authoritative calculated total.

### 3. Present and confirm the sync proposal

Show:

- included CSV rows and evidence;
- excluded or provisional rows;
- calculated total;
- old and proposed `Completed Hours`;
- confirmation that the leaf item alone will be updated.

Obtain explicit confirmation immediately before the Project write.

### 4. Update and verify

After approval:

1. update only the leaf item's `Completed Hours`;
2. read the Project item again;
3. confirm the stored number matches the calculated total;
4. leave parent totals unchanged.

Surface partial or failed writes explicitly.

## Corrections

Never hide a correction by adding an offsetting negative row.

Correct an inaccurate row through a reviewed CSV change that:

- identifies the original row;
- explains the reason in the pull request;
- replaces or removes only the incorrect row;
- reruns validation;
- synchronizes `Completed Hours` after merge.

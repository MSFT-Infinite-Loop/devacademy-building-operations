---
name: log-effort
description: "Use when: recording, validating, correcting, or synchronizing evidenced work hours for a GitHub issue; adding a structured effort comment; or recalculating a Project item's Completed Hours."
argument-hint: "record, sync, or correct; issue number; actual hours; evidence"
user-invocable: true
disable-model-invocation: false
---

# Log Effort

Record actual, evidence-backed effort directly on the most specific GitHub issue and keep its Project `Completed Hours` synchronized without double counting.

Read [the effort policy](./references/effort-policy.md) before proposing a change. Use [the proposal template](./assets/effort-entry-proposal.md) for every write.

## Authoritative record

A structured, marker-tagged comment on the leaf issue is the authoritative effort entry. The issue's `Completed Hours` field is the verified sum of its eligible, non-superseded effort comments.

Do not use a repository CSV.

## Modes

- `record`: add one effort comment and update `Completed Hours`.
- `sync`: recalculate `Completed Hours` from existing effort comments.
- `correct`: add a correction that supersedes an inaccurate effort comment, then synchronize the total.

## Non-negotiable safeguards

- Never infer hours from commits, diffs, chat duration, calendar time, timestamps, or elapsed tool execution.
- Never describe work that did not occur.
- Never duplicate child-item hours on a parent issue.
- Never add the same effort entry twice.
- Never divide time between work items automatically.
- Never edit or delete an existing effort comment to hide a correction.
- Obtain explicit human confirmation immediately before issue-comment or Project-field writes.
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

The user must supply actual hours. Do not suggest or round a value.

### 2. Verify the target and evidence

Read the issue, its parent and sub-issues, comments, and Project fields. Confirm:

- the issue exists and is the most specific applicable work item;
- the participant and package do not contradict the approved Team Charter;
- the activity is allowed by [the effort policy](./references/effort-policy.md);
- the evidence exists and supports the claimed activity;
- the entry does not already exist;
- the authenticated GitHub user is the participant or is explicitly recording on their behalf.

If work spans multiple leaf items, ask the participant to provide the actual allocation. Do not calculate it.

### 3. Determine eligibility

Week 1 starts on 2026-11-15.

For earlier work:

- record it accurately for auditability;
- mark it `Provisional - jury decision pending`;
- exclude it from `Completed Hours` until the jury decision is recorded.

For eligible work, mark it `Eligible`.

### 4. Build the structured comment

Use this exact shape:

```markdown
<!-- devacademy-effort-entry:v1 -->
### Effort entry

| Field | Value |
|---|---|
| Date | `YYYY-MM-DD` |
| Participant | Name |
| Package | Package |
| Activity | `activity` |
| Hours | `decimal` |
| Evidence | URL |
| Eligibility | Eligible or provisional reason |
```

If recording on behalf of someone else, add:

```markdown
| Recorded by | `@github-handle` on behalf of Participant |
```

### 5. Calculate the proposed total

Read every comment on the leaf issue containing `devacademy-effort-entry:v1`.

- Exclude provisional entries.
- Exclude entries superseded by a valid correction comment.
- Sum eligible decimal hours exactly.
- Compare the sum with the current `Completed Hours`.
- Replace the field with the calculated total; never increment it blindly.

Leave parent `Completed Hours` empty.

### 6. Present and confirm

Use [the proposal template](./assets/effort-entry-proposal.md). Show:

- the exact proposed comment;
- evidence and duplicate checks;
- eligibility;
- included and excluded entries;
- current and proposed `Completed Hours`;
- every GitHub write that will occur.

Use the available user-input tool to approve the exact batch immediately before writing.

### 7. Write and verify

After approval:

1. add the structured comment to the leaf issue;
2. update only that issue's `Completed Hours`;
3. read the comment and Project item again;
4. confirm the comment exists once and the stored total is correct;
5. report links and any partial failure explicitly.

If the comment succeeds but the Project update fails, preserve the comment and report the synchronization failure. Do not post a duplicate comment on retry.

## Sync procedure

Use `sync` to repair or verify a Project total without adding an effort entry.

1. Read all marked effort and correction comments.
2. Verify their structure and evidence.
3. Calculate eligible, non-superseded hours.
4. Show the old and proposed `Completed Hours`.
5. Obtain explicit confirmation.
6. Replace the field value.
7. Read it again and verify.

Do not update a parent item.

## Correction procedure

Never edit or delete the original effort comment.

Add a correction using this shape:

```markdown
<!-- devacademy-effort-correction:v1 -->
### Effort correction

| Field | Value |
|---|---|
| Supersedes | Original comment URL |
| Reason | Verified correction reason |
| Corrected date | `YYYY-MM-DD` |
| Corrected participant | Name |
| Corrected package | Package |
| Corrected activity | `activity` |
| Corrected hours | `decimal` |
| Corrected evidence | URL |
| Eligibility | Eligible or provisional reason |
```

Then recalculate `Completed Hours`, excluding the superseded entry and including the correction when eligible.

Present and confirm the exact correction and field change before writing.

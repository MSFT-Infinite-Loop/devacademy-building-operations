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

A structured, marker-tagged comment on the leaf issue is the authoritative record, not a repository CSV. Use the same [ledger calculation](./references/effort-policy.md#ledger-calculation) in `record`, `sync`, and `correct`.

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
- the authenticated GitHub user is the participant or has that participant's explicit permission to record on their behalf.

If work spans multiple leaf items, ask the participant to provide the actual allocation. Do not calculate it.

### 3. Determine eligibility

Apply [the effort policy](./references/effort-policy.md), including the pre-kick-off rule. Preserve provisional entries for audit but do not include them in `Completed Hours`.

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

### 5. Calculate and propose

Use the shared ledger calculation with the proposed entry included once, then follow **Apply and verify**.

## Apply and verify

1. Use [the proposal template](./assets/effort-entry-proposal.md). Show the exact comment (if any), included/excluded entries, evidence, and old and proposed `Completed Hours`. Ask for explicit approval of the exact writes.
2. Before writing, re-read the issue, all marked comments, and the Project field. If anything affecting the proposal changed, recalculate and request fresh approval instead of applying stale changes.
3. For `record` or `correct`, post the approved comment once. In every mode re-read all marked comments and the Project field before updating the total. Count a posted comment by ID, not again as a proposal. If the observed result differs from what was approved, leave the field alone and report that a fresh `sync` is needed.
4. Replace only the approved leaf `Completed Hours` with the verified total, and only if it differs. Read comments and the field again and report any mismatch or partial failure. If the comment succeeded but synchronization failed, preserve it and use `sync`; never repost it.

## Sync procedure

Use the same ledger calculation with no proposed comment. If the field already matches, report that no write is needed; otherwise follow **Apply and verify** with only the field change.

## Correction procedure

Never edit or delete an earlier effort comment. Verify the corrected facts and authorization as in `record`, and target the current effective comment on the same issue.

Add a correction using this shape:

```markdown
<!-- devacademy-effort-correction:v1 -->
### Effort correction

| Field | Value |
|---|---|
| Supersedes | URL of the current effort or correction comment |
| Reason | Verified correction reason |
| Corrected date | `YYYY-MM-DD` |
| Corrected participant | Name |
| Corrected package | Package |
| Corrected activity | `activity` |
| Corrected hours | `decimal` |
| Corrected evidence | URL |
| Eligibility | Eligible or provisional reason |
```

Include the `Recorded by` row for delegated corrections as for entries. Use the same ledger calculation with this correction included once, then follow **Apply and verify**.

## Output

Return:

- mode and leaf work item;
- exact effort or correction comment;
- evidence, duplicate, authorship and eligibility checks;
- included/excluded effort calculation;
- current and proposed `Completed Hours`;
- approved GitHub writes;
- verified comment and Project links or synchronization failure.

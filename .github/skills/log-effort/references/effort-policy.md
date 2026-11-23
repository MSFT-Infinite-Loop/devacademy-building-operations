# Effort recording policy

## Chosen model

The project uses the GitHub-native option permitted by PRC-06:

- structured comments on leaf issues preserve date, participant, package, activity, hours, and evidence;
- the Project `Completed Hours` number field stores their verified eligible sum;
- no repository effort CSV is maintained.

## Project

- Repository: `MSFT-Infinite-Loop/devacademy-building-operations`
- Project owner: `MSFT-Infinite-Loop`
- Project number: `1`

Resolve current Project and field IDs from GitHub rather than hardcoding GraphQL IDs.

The former user-owned Project is closed and must not be updated.

## Required entry fields

| Field | Rule |
|---|---|
| Date | Actual work date in `YYYY-MM-DD` |
| Participant | Agreed participant display name |
| Work item | Most specific applicable leaf issue |
| Package | Approved package or `Cross-cutting` for genuinely shared governance work |
| Activity | One of `design`, `code`, `test`, `review`, `docs`, `ops`, `meeting`, `learning` |
| Hours | Positive decimal actual hours supplied by the participant |
| Evidence | Accessible PR, commit, review, workflow, issue, or reviewed document |
| Eligibility | `Eligible` or a documented provisional reason |

The team has not agreed a minimum time increment. Preserve the actual user-supplied decimal without silently rounding.

## Leaf-item rule

- Record work against the most specific issue that describes it.
- Never repeat child hours on a parent.
- Leave parent `Completed Hours` empty.
- Use sub-issue progress and Project reporting for parent visibility.
- If work spans items, the participant provides the actual allocation.

## Duplicate rule

An exact duplicate has the same date, participant, package, activity, hours, and evidence.

Before writing, also flag potential near-duplicates sharing the same date, participant, work item, activity, and evidence.

Ask whether a near-duplicate represents separate work. Never assume.

## Evidence rule

Evidence must support the claimed activity.

Examples:

- design: reviewed specification, ADR, diagram, or issue comment;
- code: pull request or commit;
- test: test change, test run, or workflow run;
- review: submitted pull-request review;
- docs: documentation pull request or commit;
- ops: repository setting evidence, workflow, deployment, or infrastructure pull request;
- meeting: checked-in meeting notes with decisions and attendees;
- learning: linked learning evidence plus an explanation of package relevance.

A Project field or unverified claim alone is not evidence that work occurred.

## Authorship

The visible comment author provides additional audit evidence.

When someone records effort for another participant:

- identify both people in the comment;
- require explicit confirmation from the participant whose hours are recorded;
- never infer approval from silence.

## Learning limit

Package-relevant learning may count only within the capstone limit. Report learning hours separately and do not claim that a participant remains below the limit without calculating all eligible entries.

## Pre-kick-off effort

Week 1 starts on 2026-11-15.

Work performed earlier is recorded for auditability but remains provisional until the jury confirms whether it counts.

Until then:

- label it `Provisional - jury decision pending`;
- exclude it from `Completed Hours`;
- do not claim it toward the required total.

## Completed Hours

For a leaf issue:

```text
Completed Hours =
  eligible effort entries
  - superseded entries
  + eligible correction entries
```

Replace the Project value with the calculated total. Do not increment it blindly.

Estimated Hours and Completed Hours remain distinct:

- Estimated Hours: planned effort agreed during planning.
- Completed Hours: verified actual effort derived from structured issue comments.

## Corrections

Preserve the original effort comment. Add a marker-tagged correction that:

- links to the original comment;
- explains why it is incorrect;
- contains the complete corrected entry;
- is included only once in the recalculated total.

Never use an unexplained negative-hours entry.

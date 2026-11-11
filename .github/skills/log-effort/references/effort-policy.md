# Effort logging policy

## Authority

`docs/team/effort-log.csv` is the authoritative dated effort record. GitHub Project `Completed Hours` is a summary derived from eligible rows merged into `preview`.

The required CSV header is:

```csv
date,participant,work_item,package,activity,hours,evidence
```

## Field rules

| Field | Rule |
|---|---|
| date | Actual work date in `YYYY-MM-DD` |
| participant | Agreed participant display name |
| work_item | Most specific applicable leaf issue, formatted as `#<number>` |
| package | Approved package or `Cross-cutting` for genuinely shared governance work |
| activity | One of `design`, `code`, `test`, `review`, `docs`, `ops`, `meeting`, `learning` |
| hours | Positive decimal actual hours; never inferred |
| evidence | Accessible issue, PR, commit, workflow, reviewed document, or other direct evidence link |

The team has not yet agreed a minimum time increment. Preserve the actual user-supplied decimal without silently rounding.

## Leaf-item rule

Log work against the most specific issue that describes it.

- Do not repeat child hours on a parent.
- Do not assign a parent's aggregate hours manually.
- Use sub-issue progress and Project reporting for parent visibility.
- If an activity spans multiple leaf items, ask the participant to allocate actual time between them.
- Do not divide time automatically.

## Duplicate rule

An exact duplicate row is invalid.

Before appending, also inspect potential near-duplicates sharing the same:

- date;
- participant;
- work item;
- activity;
- evidence.

Ask the participant whether a near-duplicate represents separate work. Never assume.

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
- learning: linked learning evidence plus an explanation of package relevance;
- AI-assisted work: relevant PR or document plus the participant's truthful AI journal entry when required.

A GitHub Project item alone is not evidence that work occurred.

## Learning limit

Package-relevant learning may count only within the capstone limit. The skill reports learning hours separately and must not claim that the participant remains below the limit without calculating it from eligible merged rows.

## Pre-kick-off effort

Week 1 starts on 2026-11-15.

Work performed earlier should be recorded accurately for auditability, but its eligibility toward the required total is unresolved until the jury confirms it.

Until then:

- show pre-kick-off rows separately;
- exclude them from `Completed Hours`;
- do not claim they count toward the minimum.

## Branch and pull-request workflow

Effort-log changes are repository changes and follow the same branch rules:

1. Use the existing compliant work branch when practical.
2. Otherwise branch from current `preview` as `docs/<alias>/<issue>-log-effort`.
3. Open a focused pull request to `preview`.
4. Require review and applicable checks.
5. Squash-merge the normal pull request into `preview`.
6. Synchronize Project `Completed Hours` only after the row is visible on `origin/preview`.

Never commit the CSV directly to `preview` or `main`.

## Project synchronization

For a leaf issue:

```text
Completed Hours = sum of eligible, validated CSV rows for that issue on preview
```

Replace the Project value with the calculated total. Do not increment it blindly.

Estimated Hours and Completed Hours have different meanings:

- Estimated Hours: planned effort agreed during planning.
- Completed Hours: verified actual effort derived from the CSV.

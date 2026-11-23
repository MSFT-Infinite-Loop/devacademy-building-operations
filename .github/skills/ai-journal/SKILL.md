---
name: ai-journal
description: "Use when: drafting, validating, or recording a truthful AI Engineering Journal entry and checking weekly, total, and genuine failure-analysis counts."
argument-hint: "Participant, date, work item, tool/mode, and actual outcome"
user-invocable: true
disable-model-invocation: false
---

# AI Journal

Record a truthful AI Engineering Journal entry from real activity and maintain AI-04 evidence.

## Requirements

Each participant needs:

- at least one entry every week;
- at least ten entries total;
- at least three entries analysing genuine output that was wrong, insecure, outdated, or over-engineered.

## Safeguards

- Never invent a prompt, activity, failure, lesson, test, or time impact.
- Do not turn a routine successful interaction into a fabricated failure analysis.
- Do not include secrets, credentials, real personal data, or confidential external code.
- The participant must confirm subjective facts such as time saved/lost and lessons learned.
- Journal changes follow the repository branch and PR workflow.

## Procedure

1. Identify the participant, work item, package/requirement, date, tool, and mode.
2. Gather the actual goal, supplied context, approach, outcome, modifications, and verification.
3. Inspect linked evidence such as commits, PRs, tests, reviews, or documents.
4. Classify the outcome:
   - accepted;
   - modified;
   - rejected.
5. Record what was wrong or risky only when a genuine example exists.
6. Ask the participant for actual time impact and lesson if missing.
7. Count existing entries for:
   - the current week;
   - total entries;
   - genuine failure analyses.
8. Draft the entry using `docs/templates/ai-journal-entry.md`.
9. Present the exact file/path and content, then obtain confirmation before writing.
10. Verify the committed entry and report remaining minimums.

## Output

Return:

- exact journal entry;
- evidence links;
- outcome classification;
- verification performed;
- weekly/total/failure-analysis counts;
- remaining AI-04 gaps;
- file and PR link after approved repository writes.

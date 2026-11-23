---
name: acceptance-evidence-audit
description: "Use when: auditing requirement coverage, blocking items, Core/Advanced packages, deliverables, releases, hours, reviews, journals, specifications, ADRs, tests, security evidence, or final submission readiness."
argument-hint: "Audit scope: periodic, package, release, participant, or final"
user-invocable: true
disable-model-invocation: false
---

# Acceptance Evidence Audit

Build a traceable evidence matrix without auto-certifying missing or stale evidence.

## Scope

Use `docs/capstone-spec/requirements.csv` as the requirement index and topic files for full context.

The four-person team must cover:

- M1-M7;
- FE, BE, DB and OPS Core;
- FE, BE, DB and OPS Advanced;
- BLK-01 through BLK-10;
- all individual evidence obligations.

## Safeguards

- Start read-only.
- Classify evidence as `Verified`, `Partial`, `Missing`, `Unknown`, or `Not applicable with justification`.
- A document's existence does not prove its content or execution.
- Do not count unmerged work, inferred hours, unsubmitted reviews, unsent communications, or tests that were not run.
- Never close issues or certify release/final readiness automatically.

## Procedure

1. Select audit scope and evidence cutoff commit/release.
2. Load relevant requirement rows and acceptance guidance.
3. Inspect linked issues, specs, ADRs, code, tests, CI, scans, deployments, releases and documents.
4. Build requirement -> owner -> implementation -> tests -> evidence -> status traceability.
5. Audit each participant:
   - owned package(s);
   - ≥40 evidenced hours;
   - weekly merges and cross-track reviews;
   - ≥2 authored specs;
   - ≥1 authored ADR;
   - ≥10 journal entries, weekly cadence and ≥3 failure analyses.
6. Audit release history, tags, images, Preview/Release smoke and Scenarios A/B.
7. Rank blocking gaps first, then mandatory, Advanced, SHOULD and optional gaps.
8. Identify stale or contradictory evidence and orphaned requirements.
9. Present corrective actions with owners only when confirmed.

## Output

Return:

- audit scope and cutoff;
- requirement evidence matrix;
- BLK-01..10 summary;
- package completion summary;
- per-participant evidence summary;
- release/deliverable summary;
- blocking, mandatory and recommended gaps;
- unknowns requiring human verification;
- prioritized remediation plan.

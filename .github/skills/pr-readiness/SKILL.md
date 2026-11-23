---
name: pr-readiness
description: "Use when: deciding whether a feature branch is ready for a pull request, validating branch/spec/test/evidence compliance, or preparing an exact PR proposal before creation."
argument-hint: "Branch name and linked work item"
user-invocable: true
disable-model-invocation: false
---

# PR Readiness

Audit a completed branch and prepare—but do not silently create—a compliant PR to `preview`.

## Safeguards

- Start read-only.
- A PR is created only after the branch owner explicitly declares the final branch ready.
- Do not merge, force-push, amend, bypass policy, or close broad parent issues.
- Never claim a test, review, scan, accessibility check, or evidence link that was not verified.
- Human approval remains mandatory even when AI review is used.

## Procedure

1. Verify the working tree is clean and the branch is published and synchronized.
2. Confirm it started from current `preview`, remains short-lived, and follows naming conventions.
3. Resolve the linked leaf work item and requirement IDs.
4. For major features, verify a reviewed specification predates implementation.
5. Inspect the complete diff and commits:
   - focused scope;
   - no secrets or real personal data;
   - no unrelated changes;
   - reviewable size or documented exception;
   - Conventional Commits with work-item references.
6. Verify applicable:
   - build/lint/type checks;
   - unit/integration/database/component/E2E tests;
   - authorization/accessibility tests;
   - migration/container/security scans;
   - generated-test defect-detection evidence;
   - documentation, ADR, journal, and effort updates.
7. Evaluate Definition of Done as `Pass`, `Fail`, `Unknown`, or `Not applicable`.
8. Draft the exact title/body using `.github/pull_request_template.md`, normally with `Refs #<leaf>`.
9. Present base, head, reviewers, labels, Project fields, validation evidence, and blockers.
10. Ask for explicit approval immediately before PR creation.
11. Create the PR only after approval, add it to organization Project #1, request approved reviewers, and verify.

## Output

Return:

- readiness verdict;
- branch/base/upstream state;
- requirement/work-item/spec traceability;
- validation and evidence table;
- DoD gaps;
- documented size exception if needed;
- exact PR proposal;
- resulting PR/Project links only after approved creation.

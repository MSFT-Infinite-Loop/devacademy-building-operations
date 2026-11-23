---
name: test-evidence
description: "Use when: designing a risk-based test plan, generating test cases, reviewing test coverage by level, verifying test runs, or proving AI-generated tests detect defects."
argument-hint: "Work item, specification, requirement IDs, and requested test scope"
user-invocable: true
disable-model-invocation: false
---

# Test Evidence

Plan and verify meaningful tests across every required level without inventing results or chasing an arbitrary coverage percentage.

## Required focus

Prioritize:

- object-level authorization and IDOR;
- state machines;
- exact money and rounding;
- lease/concurrency invariants;
- failure and rollback paths;
- accessibility;
- Scenarios A and B.

## Safeguards

- Never claim a test passed unless its command/result is known.
- Do not silently skip, disable, quarantine, or weaken failing/flaky tests.
- AI-generated tests require defect-detection evidence: deliberately break behaviour or use an equivalent mutation and confirm the test fails for the intended reason.
- Do not substitute mocks for a required real database or integrated path.
- No mandatory coverage percentage exists.

## Procedure

1. Read the work item, feature specification, requirements, permissions matrix, data changes, and accepted ADRs.
2. Build a risk-to-test matrix.
3. Assign tests to required levels:
   - unit;
   - API integration with real database;
   - database/migration;
   - UI component;
   - end-to-end;
   - authorization/IDOR;
   - accessibility;
   - post-deployment smoke.
4. Include positive, negative, boundary, concurrency, retry/idempotency, and failure-recovery cases.
5. Draft tests following repository conventions.
6. Run the smallest relevant commands and record exact results.
7. For generated tests, perform controlled defect injection or mutation-style verification, then restore behaviour.
8. Check CI inclusion, unique job names, unexplained skips, and flaky-test handling.
9. Present missing coverage and evidence; obtain approval before repository writes.

## Output

Return:

- risk-to-test matrix;
- tests by required level;
- exact cases and expected outcomes;
- commands and actual results;
- defect-detection evidence;
- missing/blocked tests;
- CI integration requirements;
- files changed after approved implementation.

---
name: "Risk-Based Test Plan"
description: "Use when drafting test cases from a work item or feature specification across required unit, integration, database, component, E2E, authorization, accessibility, and smoke levels."
argument-hint: "Work item, specification, requirement IDs, and changed surfaces"
agent: "agent"
---

Draft a risk-based test plan without implementing or claiming test results.

Read the work item, feature specification, relevant requirements, permissions matrix, data changes, and accepted ADRs.

Produce:

1. Risks ranked by impact and likelihood.
2. A risk-to-test matrix.
3. Positive, negative, boundary, concurrency, retry/idempotency, and failure-recovery cases.
4. Required levels:
   - unit;
   - API integration with real database;
   - database/migration;
   - UI component;
   - E2E;
   - authorization/IDOR;
   - accessibility;
   - post-deployment smoke.
5. Test data and synthetic-seed requirements.
6. Expected result and evidence for every case.
7. A plan to prove AI-generated tests fail when behaviour is deliberately broken.
8. CI placement and unresolved blockers.

Do not invent commands, results, coverage thresholds, environments, or evidence.

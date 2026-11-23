---
name: scoped-agent-work
description: "Use when: delegating one well-scoped capstone work item to an AI coding agent, defining boundaries and stop conditions, and preserving the required human review, CI, PR, and journal evidence."
argument-hint: "Leaf issue and approved feature specification"
user-invocable: true
disable-model-invocation: false
---

# Scoped Agent Work

Delegate one bounded work item while preserving human ownership and AI-10 evidence.

## Preconditions

- Leaf work item is Ready and assigned.
- Requirement IDs and acceptance criteria are clear.
- Major-feature specification is reviewed and predates implementation.
- Relevant ADRs and dependencies are accepted.
- Dedicated short-lived branch/worktree is approved.

## Safeguards

- Delegate one coherent objective, not an entire module or application.
- Define allowed files, prohibited changes, tests, evidence, and stop conditions.
- Never provide secrets, real personal data, production data, or unapproved confidential content.
- The agent cannot approve or merge its own work.
- Human owner must understand, explain and modify every accepted line.
- Generated tests require defect-detection verification.

## Procedure

1. Read issue, specification, decisions, code context and repository instructions.
2. Draft the delegation contract:
   - objective;
   - allowed files/surfaces;
   - explicit exclusions;
   - acceptance criteria;
   - required commands/tests;
   - security/accessibility/data constraints;
   - dependency prohibition unless separately approved;
   - stop and escalation conditions.
3. Present the contract and obtain approval before creating/delegating work.
4. Launch the approved coding-agent task on a dedicated branch/worktree.
5. Monitor only for scope/blocker corrections; do not silently broaden work.
6. Inspect every diff and generated test.
7. Run tests/scans and prove generated tests detect defects.
8. Use pr-readiness; require normal human review and CI.
9. Record a truthful AI journal entry including accepted/modified/rejected output.

## Output

Return:

- delegation contract;
- agent/session and branch references;
- produced diff summary;
- accepted, modified and rejected output;
- validation and defect-detection evidence;
- PR/review status;
- journal evidence;
- unresolved risks.

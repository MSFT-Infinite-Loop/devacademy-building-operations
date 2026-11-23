---
name: adr-workflow
description: "Use when: investigating, drafting, reviewing, accepting, superseding, or auditing an Architecture Decision Record with requirements, alternatives, evidence, and AI disclosure."
argument-hint: "Decision topic and requirement IDs"
user-invocable: true
disable-model-invocation: false
---

# ADR Workflow

Manage an architecture decision from investigation to human acceptance without silently choosing technology.

## Safeguards

- Start with Status `Proposed`.
- Never mark an ADR `Accepted` without explicit team approval evidence.
- Read the allowed technology and licence policy before suggesting dependencies.
- Use current primary sources for versions, maintenance, licensing, hosting, and security claims.
- Preserve alternatives and trade-offs; do not write a decision-shaped justification after the fact.
- Every participant must author at least one ADR; at least six ADR topics are required.

## Procedure

1. Read relevant requirements, decision-register entries, package constraints, and existing ADRs.
2. Define context, decision drivers, invariants, risks, and deadline.
3. Identify at least two viable allowed alternatives.
4. For each alternative, verify:
   - compatibility with required stack;
   - licence;
   - maintenance/support;
   - security and operational impact;
   - team skills;
   - cost/hosting implications;
   - testing and migration consequences.
5. Record experiments or measurements where useful.
6. Draft with `docs/templates/adr-template.md`, requirement IDs, evidence, AI assistance, and supersession fields.
7. Present the proposal and unresolved questions.
8. Write only after confirmation on a compliant branch.
9. When the team decides, record approval evidence and update Status.
10. If superseded, link both ADRs and preserve history.

## Output

Return:

- decision question and drivers;
- verified alternatives table;
- recommendation clearly labelled as a proposal;
- risks and consequences;
- evidence/primary sources;
- exact ADR draft;
- approval or supersession actions still required;
- authored-ADR count when available.

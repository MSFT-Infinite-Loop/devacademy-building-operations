---
name: architecture-documentation-consistency
description: "Use when: checking whether implementation, README, ADRs, C4/deployment diagrams, OpenAPI, data model, rendering strategy, runbook, hosting, and operational documentation agree."
argument-hint: "Repository, module, release, or documentation scope"
user-invocable: true
disable-model-invocation: false
---

# Architecture and Documentation Consistency

Detect contradictions between the implemented system and its engineering documentation.

## Safeguards

- Start read-only.
- Do not resolve a contradiction by assuming code or documentation is correct.
- Accepted ADRs and official requirements constrain the resolution.
- Never update claims, diagrams, commands or evidence without verification.

## Procedure

1. Select scope and reference commit/release.
2. Read:
   - README/quick start;
   - accepted ADRs;
   - C4, deployment and sequence diagrams;
   - OpenAPI/API conventions;
   - data model/dictionary and migrations;
   - frontend Rendering Strategy Table;
   - CI/container/Bicep/environment configuration;
   - runbook, backup/restore and observability docs;
   - relevant code and tests.
3. Compare documented and actual:
   - components/boundaries;
   - request/data flows;
   - technologies/versions/dependencies;
   - endpoints/errors/security;
   - schema/invariants;
   - commands/environment variables;
   - deployment/rollback/operations.
4. Classify findings:
   - code defect;
   - documentation stale;
   - ADR missing/superseded;
   - evidence missing;
   - unknown requiring owner decision.
5. Present exact proposed corrections and obtain approval.
6. Verify all changed claims against implementation/tests.

## Output

Return:

- consistency matrix;
- contradictions with files/symbols/evidence;
- severity and likely source of truth;
- missing ADR/documentation;
- proposed correction set;
- verification needed after approved changes.

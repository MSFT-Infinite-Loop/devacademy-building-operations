---
name: plan-work-item
description: "Use when: creating, refining, decomposing, estimating, or scheduling a GitHub epic, user story, engineering task, or bug with capstone requirement traceability."
argument-hint: "Capability, requirement IDs, and desired issue type"
user-invocable: true
disable-model-invocation: false
---

# Plan Work Item

Create or refine a requirements-traceable work item without inventing scope, ownership, estimates, or decisions.

## Required context

Read:

- `.github/copilot-instructions.md`;
- `docs/capstone-spec/README.md` and the relevant topic files;
- `docs/team/decision-register.md`;
- `docs/team/charter.md`;
- parent issue and related Project items;
- relevant accepted ADRs and feature specifications.

## Safeguards

- Start read-only.
- Distinguish MUST, SHOULD, MAY, team decisions, and open questions.
- Never assign an owner, package, estimate, iteration, or deadline without evidence or user input.
- Never convert an optional extension into Core scope.
- Include negative authorization and failure cases.
- Obtain explicit confirmation immediately before GitHub writes.

## Procedure

1. Identify the work-item type:
   - M1-M7 epic;
   - user story;
   - focused engineering task;
   - bug.
2. Resolve applicable requirement IDs from `requirements.csv` and topic files.
3. Identify the user, outcome, scope, exclusions, dependencies, and blockers.
4. Draft acceptance criteria:
   - positive Given/When/Then;
   - validation and error behaviour;
   - object-level authorization/IDOR;
   - accessibility where UI is involved;
   - evidence needed to prove completion.
5. Identify expected test levels, documentation, ADRs, migrations, security, and operability work.
6. For major features, require a specification in `docs/specs/` before AI-assisted implementation.
7. Propose Project fields:
   - parent;
   - Status;
   - Priority;
   - Size or Estimated Hours;
   - Iteration;
   - Engineering Track;
   - Package;
   - Requirement IDs;
   - Start and target dates.
8. Present the exact issue body and field changes.
9. Ask for approval.
10. Create or update the issue, add it to organization Project #1, then verify every field.

## Output

Return:

- issue type and title;
- requirement traceability;
- complete issue body;
- proposed Project fields;
- dependencies and blockers;
- test/evidence expectations;
- open questions;
- resulting issue and Project links after approved writes.

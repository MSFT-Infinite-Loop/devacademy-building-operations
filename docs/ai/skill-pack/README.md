# Repository AI workflow policy

## Purpose

Repository-local AI customizations should make recurring engineering artifacts consistent without making decisions or claiming evidence on the team's behalf.

## Shared rules

- Read `.github/copilot-instructions.md` before acting.
- Treat the official capstone requirements as authoritative.
- Ask or mark `TBD` when required facts are unresolved.
- Reuse repository templates instead of duplicating policies.
- Never fabricate approvals, work history, evidence, tests, effort, or journal content.
- Require human review before remote writes, releases, permissions, hosting, or jury communications.

## Current pilot

The [Feature Specification prompt](../../../.github/prompts/feature-spec.prompt.md) is the first pilot. A prompt is appropriate because it performs one focused task and is portable across current VS Code Copilot environments.

## Proposed priority

1. User Story Creator
2. ADR Creator
3. Standard PR Creator
4. AI Journal Entry
5. Effort Log Entry
6. Weekly Release PR
7. Definition-of-Done Validator
8. Work-Item Decomposition
9. Test Plan/Case Generator
10. Security Review
11. Dependency and Licence Review
12. Weekly Team Check-in
13. Release Readiness
14. Architecture/Documentation Consistency
15. Incident/Post-mortem
16. Acceptance/Evidence Audit

Single focused tasks should use `.github/prompts/`. Multi-step workflows with bundled references may use `.github/skills/<name>/SKILL.md` after the team verifies skill discovery in every supported editor.

## Importing the colleague-provided requirements pack

Before importing it under `docs/capstone-spec/`:

1. Confirm with the team and jury that the derived internal summary may be stored in the private repository.
2. Compare its source version with the latest official requirements.
3. Update stale team-size and decision-register entries.
4. Remove unnecessary personal contact details.
5. Run `python tools/build-pack.py --check`.
6. Merge, rather than overwrite, the repository Copilot instructions.

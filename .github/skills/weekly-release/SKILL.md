---
name: weekly-release
description: "Use when: preparing, opening, reviewing, merging, tagging, publishing, or verifying the weekly preview-to-main release after release-readiness passes."
argument-hint: "Week number, approved version, and release captain"
user-invocable: true
disable-model-invocation: false
---

# Weekly Release

Execute the approved weekly release workflow without bypassing human review or using the wrong merge method.

## Preconditions

- The release-readiness skill returned `Ready` or `Ready with approved exceptions`.
- The release captain, version and included work items are confirmed.
- `preview` is current and all evidence remains valid.

## Safeguards

- Use `.github/PULL_REQUEST_TEMPLATE/release.md`.
- Base must be `main`; head must be `preview`.
- Never squash or rebase a release PR; use a merge commit.
- Never create the PR, merge, tag, publish, deploy, or communicate without explicit confirmation for that exact action.
- For four members, manually verify two non-author approvals while GitHub Free cannot enforce them.
- Do not close broad work items unless their full acceptance is verified.

## Procedure

### Prepare

1. Re-read release-readiness evidence and detect changes since the audit.
2. Verify version does not already exist and follows the release plan.
3. Draft the exact title `Release vX.Y.0 - Week N`.
4. Complete every release-template section with verified links/results.
5. Present base/head, reviewers, Project fields and body.
6. Confirm before creating the release PR.

### Review and merge

7. Add the PR to organization Project #1 and request approved reviewers.
8. Recheck CI, conversations and two non-author approvals.
9. Present the exact merge commit action and confirm.
10. Merge using a merge commit only.

### Publish and verify

11. Confirm before creating the SemVer tag on the resulting `main` commit.
12. Confirm before publishing release notes/images or deploying.
13. Run and record Release smoke tests.
14. Update CHANGELOG, Project status, plan progress and evidence only from verified outcomes.

## Output

Return:

- release PR proposal/link;
- readiness recheck;
- approvals/checks/conversations;
- merge commit SHA;
- tag and release links;
- image/deployment identifiers;
- Release smoke results;
- rollback status;
- failures or incomplete steps.

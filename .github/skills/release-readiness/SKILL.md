---
name: release-readiness
description: "Use when: auditing whether preview is ready for the weekly release PR, checking blocking acceptance items, CI, migrations, scans, hosted environments, smoke tests, documentation, rollback, approvals, and version evidence."
argument-hint: "Week number and proposed version"
user-invocable: true
disable-model-invocation: false
---

# Release Readiness

Perform a read-only release gate before any `preview -> main` PR is opened.

## Safeguards

- Never create or merge a release PR, tag, release, deployment, or exception through this audit.
- Missing evidence is `Fail` or `Unknown`, never assumed passed.
- Do not reuse stale CI, scan, smoke, migration, or deployment evidence.
- The four-person scope includes OPS Advanced, so hosted Preview and Release, Bicep/IaC evidence, DAST and advanced operations requirements apply.

## Procedure

1. Identify week, release captain, proposed SemVer version and release scope.
2. Verify `preview` is synchronized, clean, and contains only intended reviewed changes.
3. List included work items and confirm each Definition of Done.
4. Verify current:
   - required CI checks;
   - builds, lint/analyzers and all test levels;
   - migration validation against disposable database;
   - container builds and versioned images;
   - dependency/source/image scans;
   - Critical/High finding status and exceptions;
   - accessibility evidence;
   - Preview deployment and smoke tests;
   - Scenarios A/B when implemented;
   - DAST where required;
   - backup/restore and runbook evidence when due.
5. Review database/data changes, compatibility and rollback.
6. Review CHANGELOG, plan progress, known issues and AI disclosure.
7. Evaluate BLK-01 through BLK-10 and relevant package acceptance rows.
8. Verify required reviewers/approvals can be obtained.
9. Produce a gate result:
   - Ready;
   - Not ready;
   - Ready with approved exceptions.

## Output

Return:

- release gate verdict;
- proposed version/week/captain;
- included work items;
- evidence matrix;
- blocking and required gaps;
- migration/data summary;
- known issues and rollback readiness;
- exact actions needed before the weekly-release skill may run.

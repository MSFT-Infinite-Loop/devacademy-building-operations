---
name: dependency-license-review
description: "Use when: proposing, adding, upgrading, or reviewing a package, library, tool, container image, service, or licence under ARC-10, AI-06, and SEC-09."
argument-hint: "Exact dependency name, ecosystem, version, and intended use"
user-invocable: true
disable-model-invocation: false
---

# Dependency and Licence Review

Verify a dependency before it enters the repository.

## Safeguards

- Do not install or edit manifests before review approval.
- Verify the exact package identity; reject look-alikes and ambiguous names.
- Use current primary sources: official package registry, source repository, release notes, licence, and advisories.
- Never infer licence compatibility from a package description.
- Check the capstone's prohibited and approved-exception lists.
- Report uncertainty as `Unknown`, not `Approved`.

## Procedure

1. Identify ecosystem, exact name, publisher/owner, version, source, and intended use.
2. Confirm the package exists in the expected official registry.
3. Verify repository ownership, release history, maintenance activity, and support status.
4. Read the exact version's licence and relevant transitive/commercial restrictions.
5. Compare against ARC-10 and the repository decision register.
6. Check current security advisories and known malicious/look-alike reports.
7. Assess:
   - necessity;
   - built-in or Microsoft alternative;
   - bundle/runtime/container impact;
   - data/privacy implications;
   - upgrade and abandonment risk.
8. Produce `Approved`, `Rejected`, or `Needs decision` with evidence.
9. Ask for confirmation before modifying manifests or lock files.
10. After installation, verify resolved version, lock-file changes, licence metadata, tests, and vulnerability scans.

## Output

Return:

- dependency identity and intended use;
- exact reviewed version;
- licence finding;
- maintenance and advisory finding;
- ARC-10 compatibility;
- alternatives;
- decision status and rationale;
- primary-source links;
- required PR evidence and follow-up checks.

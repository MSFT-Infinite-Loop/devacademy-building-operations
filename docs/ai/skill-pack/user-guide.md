# AI workflow skills: plain-English user guide

## What these files are

The skills are shared Copilot procedures stored in `.github/skills/`. They tell Copilot how to perform recurring project workflows safely and consistently.

A skill is not an autonomous approval system. It gathers evidence, proposes an exact action, asks for confirmation, performs only approved writes, and verifies the result.

Prompt files under `.github/prompts/` are simpler: they draft one artifact and stop.

## How to invoke a skill

In VS Code Copilot Chat:

1. Open this repository as the workspace.
2. Type `/`.
3. Select the skill, for example `/plan-work-item`.
4. Supply the issue, branch, version, or topic requested by its argument hint.

You can also ask naturally, such as:

> Review issue #24 and move it to Ready if the evidence supports it.

Copilot may discover the matching skill automatically from its description.

## What happens during a skill

Most skills follow this pattern:

1. **Read:** inspect requirements, decisions, code, issues and evidence.
2. **Assess:** classify evidence and identify missing facts.
3. **Propose:** show exact file/GitHub changes.
4. **Confirm:** ask you immediately before writing.
5. **Apply:** make only the approved changes.
6. **Verify:** read the result back and report links/failures.

If a skill cannot prove something, it should say `Missing` or `Unknown`.

## Skills

### `/plan-work-item`

**Use when:** creating or refining an epic, story, task or bug.

**You provide:** capability, issue type, parent epic and known requirement IDs.

**It outputs:**

- title and complete issue body;
- Given/When/Then criteria;
- negative authorization/error cases;
- dependencies, test/evidence expectations;
- proposed Project fields;
- issue/Project links after approval.

It will not invent owners, estimates, packages or dates.

### `/update-work-item`

**Use when:** starting, reviewing, completing, reopening or correcting an existing issue.

**You provide:** issue number and requested transition.

**It outputs:**

- current issue/Project state;
- acceptance/evidence classification;
- branch/PR/Definition-of-Done checks;
- exact proposed checkbox/field/status changes;
- verified result after approval.

It does not merge PRs or certify missing evidence.

### `/log-effort`

**Use when:** recording, correcting or synchronizing actual work hours.

**You provide:** participant, date, leaf issue, package, activity, actual hours and evidence URL.

**It outputs:**

- exact structured effort comment;
- duplicate/evidence/eligibility checks;
- calculated leaf-item `Completed Hours`;
- issue/comment links after approval.

It never estimates hours and never duplicates hours on parent issues.

### `/ai-journal`

**Use when:** recording a real Copilot/AI interaction in a participant journal.

**You provide:** actual work item, tool/mode, goal, outcome, verification, risk, time impact and lesson.

**It outputs:**

- complete journal entry;
- linked evidence;
- weekly, total and genuine failure-analysis counts;
- remaining AI-04 gaps.

It never invents a failure or activity.

### `/adr-workflow`

**Use when:** investigating, drafting, accepting or superseding an architecture decision.

**You provide:** decision question and applicable requirements.

**It outputs:**

- decision drivers;
- verified alternatives and evidence;
- trade-offs/risks;
- Proposed ADR;
- approval/supersession actions.

It cannot mark an ADR Accepted without explicit team approval.

### `/dependency-license-review`

**Use when:** considering a package, tool, image, service or upgrade.

**You provide:** exact name, ecosystem, version and intended use.

**It outputs:**

- identity/source verification;
- exact licence;
- maintenance/advisory status;
- ARC-10 decision;
- alternatives and evidence.

Run this before editing dependency manifests.

### `/pr-readiness`

**Use when:** the branch owner believes a branch is complete.

**You provide:** branch and linked leaf issue.

**It outputs:**

- readiness verdict;
- branch/spec/test/security/evidence checks;
- Definition-of-Done gaps;
- exact PR title/body/base/reviewer proposal.

It creates no PR until the owner explicitly declares the final branch ready and approves the proposal.

### `/test-evidence`

**Use when:** planning tests, generating cases, or reviewing whether tests are meaningful.

**You provide:** work item/specification and changed surfaces.

**It outputs:**

- risk-to-test matrix;
- tests at every required level;
- commands/results when run;
- defect-injection evidence for generated tests;
- missing CI coverage.

It does not invent passing results or coverage targets.

### `/security-evidence-review`

**Use when:** auditing a feature, PR, architecture or release against SEC-01..15.

**You provide:** scope and evidence links.

**It outputs:**

- security-control matrix;
- severity/confidence findings;
- missing authorization/abuse tests;
- privacy/least-privilege gaps;
- release blockers and remediation proposal.

Explicit vulnerability reviews invoke the dedicated security-review agent.

### `/weekly-team-check-in`

**Use when:** preparing or recording the weekly team meeting.

**You provide:** week/date and confirmed meeting facts.

**It outputs:**

- factual progress dashboard;
- decisions, risks and blockers;
- actions with owners/dates;
- merge/review/effort/journal/spec gaps;
- weekly-notes draft.

It never invents attendance, decisions or commitments.

### `/release-readiness`

**Use when:** deciding whether `preview` is ready for the weekly release PR.

**You provide:** week and proposed version.

**It outputs:**

- Ready/Not ready verdict;
- BLK-01..10 matrix;
- CI/test/scan/deployment/smoke evidence;
- migration, known-issue and rollback status;
- remaining release blockers.

This skill is read-only.

### `/weekly-release`

**Use when:** release-readiness has passed and the release captain is ready to act.

**You provide:** approved week, version and captain.

**It outputs:**

- exact release PR proposal/link;
- approval/check status;
- merge commit, tag and release links;
- image/deployment/smoke evidence.

PR creation, merge, tag, publication and deployment each require explicit confirmation. Release PRs use merge commits, never squash.

### `/acceptance-evidence-audit`

**Use when:** running a periodic, package, participant, release or final audit.

**You provide:** audit scope and cutoff commit/release.

**It outputs:**

- requirement/evidence matrix;
- blocking-item summary;
- Core/Advanced package status;
- per-participant hours/reviews/specs/ADRs/journals;
- prioritized gaps and unknowns.

It never auto-certifies missing evidence.

### `/scoped-agent-work`

**Use when:** delegating one approved work item to an AI coding agent.

**You provide:** Ready leaf issue and reviewed specification.

**It outputs:**

- bounded delegation contract;
- allowed files and exclusions;
- stop conditions;
- agent/branch references;
- diff/test/review/journal evidence.

It never delegates a whole module or merges agent work automatically.

### `/architecture-documentation-consistency`

**Use when:** checking whether code, ADRs, diagrams, OpenAPI, data model, README, deployment and runbook agree.

**You provide:** repository/module/release scope.

**It outputs:**

- consistency matrix;
- contradictions and likely source of truth;
- missing/superseded ADRs;
- proposed correction set and verification.

### `/incident-postmortem`

**Use when:** a real operational, deployment, data, build or security incident occurred.

**You provide:** incident link, environment and time window.

**It outputs:**

- evidence-backed timeline;
- impact and recovery;
- root cause/contributing factors;
- requirement mapping;
- corrective actions with owners and dates.

It never invents an incident or blames individuals.

## Prompts

### `/Feature Specification`

Drafts a major-feature specification before implementation. Output goes to `docs/specs/` after review.

### `/ADR Draft`

Drafts a Proposed ADR from verified alternatives and evidence. It does not choose or accept the decision.

### `/Risk-Based Test Plan`

Drafts risks and test cases across every mandatory test level. It does not implement tests or claim results.

### `/User Story`

Drafts one requirements-traceable story with positive, negative, authorization, accessibility and evidence criteria. It does not create the issue.

## Typical feature workflow

1. `/plan-work-item`
2. `/Feature Specification`
3. `/adr-workflow` when a decision is needed
4. `/dependency-license-review` before dependencies
5. Implement manually or use `/scoped-agent-work`
6. `/test-evidence`
7. `/security-evidence-review`
8. `/ai-journal`
9. `/log-effort`
10. `/update-work-item`
11. `/pr-readiness`

## Typical weekly workflow

1. `/weekly-team-check-in`
2. Complete/verify current work items
3. `/release-readiness`
4. `/weekly-release`
5. `/acceptance-evidence-audit` periodically

## What skills cannot enforce

Repository settings and CI must enforce:

- protected `preview` and `main`;
- required approvals/checks;
- CODEOWNERS;
- merge methods;
- secret scanning;
- build/lint/test/migration/container/security gates;
- image publication, deployment and smoke tests.

Do not treat a skill's guidance as proof that these controls are configured.

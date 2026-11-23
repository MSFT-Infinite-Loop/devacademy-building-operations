# DevAcademy AI workflow pack

## Purpose

This repository-local pack provides repeatable Copilot workflows that help the team follow capstone requirements without inventing decisions, evidence, hours, tests, reviews, releases, or journal activity.

Skills assist the process. They do not replace:

- human ownership and approval;
- protected branches and CODEOWNERS;
- required CI checks;
- tests and scanners;
- package ownership;
- the official DevAcademy requirements.

See the [plain-English user guide](user-guide.md) for invocation and examples.

## Common safety model

Every write-capable skill should:

1. start read-only;
2. gather current requirements, decisions and evidence;
3. classify missing information as Missing or Unknown;
4. present exact proposed changes;
5. obtain confirmation immediately before writes;
6. apply only the approved batch;
7. read back and verify the result.

## Skills

| Skill | Main purpose | Principal requirements |
|---|---|---|
| `update-work-item` | Safely update issues and Project status/evidence | PRC-02/04/06/07, QA-09, GIT |
| `log-effort` | Record evidence-backed hours and synchronize Completed Hours | PRC-06/07, OWN-02 |
| `plan-work-item` | Create/refine epics, stories, tasks and bugs | PRC-02, AI-03, SEC-03, QA-09 |
| `ai-journal` | Record truthful weekly AI evidence and counts | AI-04, AI-12, BLK-10 |
| `adr-workflow` | Investigate and manage ADR lifecycle | ARC-07, AI-06 |
| `dependency-license-review` | Verify exact dependencies, licences and advisories | ARC-10, AI-06, SEC-09 |
| `pr-readiness` | Audit a branch and prepare an exact PR proposal | GIT-03..09, AI-03/05/07/12 |
| `test-evidence` | Plan and verify meaningful multi-level tests | QA-01..05, AI-05, SEC-03 |
| `security-evidence-review` | Audit SEC-01..15 design, tests and evidence | SEC-01..15, BLK-03/09 |
| `weekly-team-check-in` | Prepare factual weekly notes and compliance status | PRC-03, GIT-03/09, OWN-03 |
| `release-readiness` | Read-only gate before weekly release PR | BLK-01..10, OPS-C08 |
| `weekly-release` | Execute approved preview-to-main release workflow | GIT-04/05, OPS-C08 |
| `acceptance-evidence-audit` | Audit requirement/package/participant/final evidence | DEL, BLK, all package rows |
| `scoped-agent-work` | Safely delegate one bounded coding-agent item | AI-05/10/12 |
| `architecture-documentation-consistency` | Find contradictions between code and docs | ARC, DEL, QA-06 |
| `incident-postmortem` | Record a real incident and corrective actions | OPS Advanced, operability evidence |

## Prompts

Prompts draft one focused artifact and do not perform remote writes.

| Prompt | Output |
|---|---|
| `Feature Specification` | Requirements-traceable feature specification |
| `ADR Draft` | Proposed ADR for human decision |
| `Risk-Based Test Plan` | Multi-level risk-to-test plan |
| `User Story` | Requirements-traceable story draft |

This satisfies the AI-09 recommendation for at least three reusable prompt files.

## Repository context

- Repository: `MSFT-Infinite-Loop/devacademy-building-operations`
- Project: organization Project #1
- Team size: four
- Scope: all four Core and all four Advanced packages
- Former user-owned Project: closed; never update it

Resolve current field/option IDs dynamically rather than hardcoding GraphQL IDs.

## Source requirements

After PR #18 is merged and this branch is rebased, skills must use:

- `docs/capstone-spec/README.md`;
- relevant topic files;
- `docs/capstone-spec/requirements.csv`;
- `docs/team/decision-register.md`;
- `docs/team/charter.md`;
- accepted ADRs and feature specifications.

## Deterministic controls still required

Skills cannot enforce:

- private branch protection;
- required human approvals;
- CODEOWNERS;
- required CI checks;
- merge methods;
- Gitleaks/push protection;
- dependency/container/DAST scans;
- image publishing/deployment/smoke tests.

Those belong in repository settings, hooks and CI. Track unresolved enforcement under issue #4.

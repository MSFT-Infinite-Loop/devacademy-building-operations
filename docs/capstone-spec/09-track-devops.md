---
title: DevOps and Platform track (OPS) — Core and Advanced packages
source_sections: "6 (intro), 6.4"
load_when: "Owning or reviewing repository governance, CI/CD, containers, environments, secrets, security scanning, releases, runbook, hosting, IaC, observability, load/DAST/chaos testing, supply chain."
related: [10-architecture-tech-policy.md, 11-security-privacy.md, 14-process-git-planning.md, 16-environment-hosting-tools.md]
---

# DevOps and Platform track (OPS)

**Purpose:** make delivery repeatable and safe — every change is consistently built, tested, scanned and released.

**Package rules:** every item in a required package is a MUST unless stated. Substitution needs the jury's written approval. OPS Core is required for every team. OPS Advanced is required for a team of 4, or when a team of 3 selects it in Week 1. **OPS Advanced makes hosted Preview and Release environments mandatory.**

Table schema: `ID | Level | Scope | Requirement | Evidence`.

## OPS Core (≈ 20 h)

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| OPS-C01 | MUST | CORE | **Private** GitHub or Azure DevOps repo; protection on `main` and `preview`; CODEOWNERS; PR and work-item templates; `.editorconfig`; `.gitignore`; **jury read access by end of Week 1**. | Repository settings |
| OPS-C02 | MUST | CORE | GitHub Projects / Azure Boards backlog with module epics, stories with acceptance criteria, tasks, weekly iterations, linked PRs/work items, effort-tracking fields. | Board |
| OPS-C03 | MUST | CORE | **CI for PRs targeting `preview` and `main`**: restore, build, lint/analyzers, unit/integration tests, migration validation against an ephemeral DB, frontend build/tests, container build — all as **required status checks**. Dependency caching expected. | Pipeline/workflows + history |
| OPS-C04 | MUST | CORE | Multi-stage Dockerfiles for web and API: **non-root user, minimal base, health check**. Compose or Aspire starts DB, cache, seed and application with **one command** on Podman or Rancher Desktop — both from source and from published version images. | Dockerfiles + Compose + README |
| OPS-C05 | MUST | CORE | Publish **commit-tagged images** after merges to `preview` and **version-tagged images** for releases on `main`; run each version; control migration application; execute **smoke tests**. Hosted Preview deploys automatically; hosted Release requires approval. Hosting becomes mandatory with OPS Advanced. | Pipeline + registry + deployment/smoke history |
| OPS-C06 | MUST | CORE | Keep **secrets out of Git**; run **secret scanning** (GitHub/Azure DevOps built-in where available, or tooling such as Gitleaks). Secrets in pipeline/variable-group/Key Vault storage. Cloud deployment SHOULD use **OIDC workload identity** instead of long-lived keys. | Settings + pipeline configuration |
| OPS-C07 | MUST | CORE | Scan **dependencies, source (static analysis) and container images**. No unresolved **Critical/High** finding enters a release unless a documented exception exists. | Scan output + exceptions |
| OPS-C08 | MUST | CORE | Automate **weekly releases**: release-PR template, **semantic version tags**, generated release notes/CHANGELOG, and a release record containing images, notes and (when hosted) the deployment. | Tags + releases + CHANGELOG |
| OPS-C09 | MUST | CORE | Operational **runbook**: local setup, environments/URLs, deployment/rollback, reset/reseed, backup/restore, common failures and remediation. | `docs/operations/runbook.md` |

## OPS Advanced (≈ 20 h) — all six are MUST when OPS Advanced is in scope (requires hosted Preview and Release)
Azure is recommended with small tiers, scale-to-zero and budget alerts; another host is allowed if the jury can access it.

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| OPS-A01 | MUST | ADVANCED | **Bicep** for every cloud resource; parameterised per environment; deployed through the pipeline; **drift detection**. | IaC + pipeline |
| OPS-A02 | MUST | ADVANCED | An **ephemeral environment per PR** with seed data and automatic teardown (or revision-style previews); its URL is posted to the PR. | PR history |
| OPS-A03 | MUST | ADVANCED | **OpenTelemetry** exported to monitoring; dashboards for latency, errors, saturation and jobs; **at least 2 alerts**; an **incident drill** with a blameless postmortem. | Dashboards + alerts + postmortem |
| OPS-A04 | MUST | ADVANCED | **Blue-green or canary** progressive delivery; automatic rollback on failed smoke tests; **feature flags** for unfinished features. | Pipeline + demo |
| OPS-A05 | MUST | ADVANCED | **Scheduled load tests** on Preview with tracked releases; a **DAST baseline scan** (for example OWASP ZAP); a **dependency/cache chaos test** with documented observed behaviour. | Reports |
| OPS-A06 | MUST | ADVANCED | An **SBOM for each release**; pinned action/task versions; automated dependency updates with merge rules; budget alerts; scale-to-zero/auto-shutdown for non-release environments. Image signing/provenance SHOULD be used. | Artifacts + settings |

## Hosting rule recap
- Hosting is optional **unless** OPS Advanced is in scope. Without hosting, the pipeline must still smoke-test each published image version and the jury must be able to start the Release version locally with **one command** (OPS-C04, OPS-C05).
- If hosted, both **Preview and Release URLs must stay available through Demo Day**; delete Azure resources afterwards (see 16).

## Related requirements outside this track
GIT-01..GIT-10, PRC-01..PRC-08 (14) · SEC-06, SEC-08, SEC-09, SEC-14, SEC-15 (11) · QA-02, QA-03, QA-06, QA-07 (12) · ARC-10 (10) · DB-C04, DB-C08 (08) · FE-C11 (E2E tests shared with FE).

## First tasks `[PACK NOTE]`
1. Decide repo host (GitHub vs Azure DevOps); create the private monorepo; protect `main` and `preview` per the GIT-06 table (14 §3); CODEOWNERS; templates; jury read access.
2. Turn on secret scanning/push protection before the first commit with real code (blocking item: no secrets in history).
3. CI skeleton: restore, build, lint, tests, migration check, container build as required checks.
4. Compose-based one-command start (Podman or Rancher Desktop) — target for Week 2.
5. Release automation draft: [release PR template](../../.github/PULL_REQUEST_TEMPLATE/release.md), SemVer tagging, CHANGELOG generation.

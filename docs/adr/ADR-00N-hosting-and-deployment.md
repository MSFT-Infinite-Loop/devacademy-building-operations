# ADR-00N: Hosting and deployment strategy (Azure Container Apps + ACR)

- **Status:** Proposed
- **Date:** 2026-11-26
- **Author(s):** Didier Gbenou
- **Requirement IDs:** ARC-07, OPS-C04, OPS-C05, OPS-C06, OPS-C08, OPS-C09, OPS-A01, OPS-A02, OPS-A04
- **Supersedes:** None
- **Superseded by:** N/A

## Context

The team needs a hosted deployment model for Preview and Release that supports weekly releases, controlled migrations, smoke tests, and operations evidence. With a four-person team, OPS Advanced is in scope, so hosted Preview and Release are mandatory.

This decision must satisfy:

- ARC-07: hosting/deployment ADR is required,
- OPS-C04: one-command local stack from source and published images,
- OPS-C05: commit-tagged Preview images, version-tagged Release images, migration control, smoke tests, hosted Release approval,
- OPS-C06: secrets handling and OIDC-based cloud auth,
- OPS-C09: runbook including backup/restore,
- OPS-A01: Bicep for all cloud resources and drift checks,
- OPS-A02: per-PR ephemeral preview or revision-style preview with teardown,
- OPS-A04: progressive delivery with rollback on failed smoke tests.

## Decision drivers

- Fit mandatory OPS Core and OPS Advanced requirements.
- Keep operations manageable for a capstone team.
- Preserve a clear and auditable preview-to-release promotion flow.
- Keep costs within available Azure student credit.
- Avoid lock-in to heavyweight platform operations unless required.

## Options considered

### Option 1: Azure App Service (containers) + ACR

- Advantages:
  - Mature platform and straightforward container deployment.
  - Lower conceptual load for basic web/API hosting.
- Disadvantages:
  - PR-ephemeral environment pattern is less direct to automate consistently for both web and API with per-PR data lifecycle.
  - Progressive delivery/canary and revision-style testing are less native than ACA revisions.
- Risks:
  - More custom pipeline logic to satisfy OPS-A02/A04.
  - Additional operational glue for environment lifecycle.

### Option 2: Azure VM + Docker Compose

- Advantages:
  - Full runtime control and parity with local Compose model.
  - No platform-specific deployment abstraction.
- Disadvantages:
  - Highest operations burden (patching, hardening, uptime, diagnostics).
  - Weak fit for rapid per-PR ephemeral environments.
- Risks:
  - Significant ops overhead for a student capstone timeline.
  - Higher chance of configuration drift and security mistakes.

### Option 3: Azure Kubernetes Service (AKS) + ACR

- Advantages:
  - Powerful routing/deployment controls.
  - Strong long-term production patterns.
- Disadvantages:
  - Operational complexity is disproportionate for this project scope.
  - Higher learning and maintenance overhead than required.
- Risks:
  - Team bandwidth consumed by platform work instead of product delivery.
  - Increased cost and troubleshooting surface.

### Option 4 (selected): Azure Container Apps (ACA) + ACR

- Advantages:
  - Container-native flow aligns with OPS-C04/C05.
  - Revisions and traffic splitting support OPS-A02/A04 patterns.
  - Bicep coverage for ACA/ACR/networking/secrets supports OPS-A01.
  - Lower ops burden than VM/AKS while keeping hosted evidence.
- Disadvantages:
  - Requires explicit decisions on revision routing, approvals, and migration choreography.
  - Some topology choices (single-origin routing approach) need explicit implementation.
- Risks:
  - Misconfigured autoscaling or revision rules can impact cost/stability.
  - Data migration rollback still requires expand/contract discipline.

## Decision

Adopt **hosted now** using **Azure Container Apps (ACA) + Azure Container Registry (ACR)**.

This does not replace OPS-C04 local development: the full stack remains runnable with one command from source and from published images on Podman or Rancher Desktop.

### Environment topology

- Separate resource groups per environment:
  - `rg-bop-preview`
  - `rg-bop-release`
- One ACA environment per stage (Preview and Release).
- Region: one primary Azure region for both environments to reduce complexity in v1.

### Core hosted components in scope

- Web app container (ACA),
- API container (ACA),
- Background worker (ACA app or API-hosted jobs, see replica constraints below),
- Valkey cache container app (internal ingress only; Redis service is excluded by policy),
- Managed PostgreSQL hosting (preferred) or explicitly documented temporary containerized DB only for short-lived preview cases,
- Blob storage account for media/documents,
- Key Vault for secrets,
- ACR for image storage.

### Identity, secrets, and deployment auth

- Use GitHub Actions OIDC federation to Azure for deployment auth (no long-lived cloud secrets in repo).
- Runtime secrets are sourced from Key Vault and injected via ACA secret references.
- Pipeline and app configuration follow OPS-C06.

### Preview and release flow

- `preview` merges:
  - build and publish commit-tagged images to ACR,
  - deploy to Preview,
  - run smoke tests.
- `main` weekly release:
  - build and publish SemVer-tagged images,
  - deploy candidate revision to Release,
  - run smoke tests before promoting traffic.

### Release approval model on GitHub Free public repository

The repository is now public under the visibility exception recorded in [Charter/governance PR #30](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/30). GitHub Free public repositories support environment required reviewers, so the former private-repository feature limitation no longer applies. This ADR remains Proposed, and its proposed Release approval model is unchanged:

- mandatory release PR approvals per branch policy,
- manual `workflow_dispatch` release deployment run initiated by the release captain after PR merge,
- deployment run references the approved release PR and tag in logs/release notes.

Adding an environment required-reviewer gate remains a separate unresolved team decision and must be configured and verified explicitly. Public visibility alone does not enable or prove a deployment approval gate.

### Per-PR preview model (OPS-A02)

- For each PR, pipeline provisions an ephemeral preview deployment (revision-style or dedicated PR app naming pattern),
- seed synthetic data automatically,
- post URL in the PR,
- tear down PR resources on PR close/merge.

### Migration and rollback model (OPS-C05, OPS-A04)

- Migrations run in a controlled pre-traffic step (ACA job),
- if migration fails: deployment stops, no traffic switch,
- if app smoke tests fail after migration: traffic does not promote; fix-forward is required,
- schema changes use expand/contract to keep N and N-1 revisions compatible during rollback windows.

### Replica and ingress constraints

- API min replicas: 1 (jobs in host must not be scaled to zero), max replicas: 3 for v1 baseline.
- Web app can use lower minimum in Preview for cost, but Release keeps stable minimum for demo reliability.
- Sticky sessions are configured only when required by chosen real-time pattern.
- If single-origin web+API routing is not achievable with selected ACA topology, add a small reverse-proxy container and document in runbook.

### Cost model (rough estimate, to be refined after first month)

- Subscription owner: Didier Gbenou (Ops track owner), with team visibility on budgets.
- Initial monthly target:
  - Preview: <= EUR 60
  - Release: <= EUR 70
  - Shared platform overhead (registry/storage/monitoring): <= EUR 20
- Budget alerts:
  - warning at EUR 100 total/month,
  - critical at EUR 130 total/month.
- Cost controls:
  - right-sized CPU/memory,
  - lower baseline in Preview where safe,
  - automatic cleanup for PR environments.

## Consequences

- Positive:
  - Strong alignment with required OPS capabilities.
  - Clear, auditable image-to-deployment traceability.
  - Better readiness for demo and operational evidence.
- Negative:
  - Higher setup overhead than local-only workflows.
  - More moving parts to document and operate.
- Follow-up actions:
  - Implement Bicep modules for all resources and drift checks in CI.
  - Implement PR preview lifecycle automation and teardown.
  - Finalize runbook with deployment, rollback, backup, and restore drills.
  - Add release evidence linking commit/tag/images/deployment artifacts.

## Evidence and verification

Primary sources used:

- DevAcademy capstone OPS and process requirements (repo `docs/capstone-spec/09-track-devops.md`, `docs/capstone-spec/14-process-git-planning.md`),
- Azure Container Apps revisions/traffic: <https://learn.microsoft.com/azure/container-apps/revisions>,
- Azure Container Apps ingress/session affinity/WebSockets: <https://learn.microsoft.com/azure/container-apps/ingress-overview>,
- Azure Container Apps jobs (for migration job pattern): <https://learn.microsoft.com/azure/container-apps/jobs>,
- Azure workload identity with GitHub Actions (OIDC): <https://learn.microsoft.com/azure/developer/github/connect-from-azure-openid-connect>,
- Azure pricing references:
  - <https://azure.microsoft.com/pricing/details/container-apps/>
  - <https://azure.microsoft.com/pricing/details/container-registry/>
  - <https://azure.microsoft.com/pricing/details/postgresql/flexible-server/>
  - <https://azure.microsoft.com/pricing/details/storage/blobs/>
- GitHub rulesets/plans documentation:
  - <https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>.
- GitHub environment required reviewers and public-repository availability:
  - <https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments#required-reviewers>.

Not fully verified yet:

- exact monthly spend at target load,
- final single-origin routing pattern across selected ACA app topology.

## AI assistance

AI was used to structure alternatives and draft wording. The author reviewed requirement mapping, corrected scope, and verified cited source categories before submission.

GitHub Copilot subsequently corrected the visibility-dependent approval rationale against current GitHub documentation and the reported visibility approval. The hosting choices, proposed release mechanism, and Proposed status were preserved.

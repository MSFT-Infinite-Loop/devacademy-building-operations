# ADR-001: Hosting and deployment strategy (Azure Container Apps + ACR)

- **Status:** Proposed
- **Date:** 2026-11-24
- **Author(s):** Didier Gbenou
- **Requirement IDs:** ARC-07, OPS-C04, OPS-C05, OPS-C08

## Context

The team needs a hosting and deployment approach that supports weekly releases, image versioning, smoke-tested deployments, and a stable Preview/Release flow for implementation and demo preparation.

The hosting/deployment decision must be recorded as an ADR (ARC-07). The selected approach must also remain compatible with:

- OPS-C04 (containerized services and one-command local stack),
- OPS-C05 (commit-tagged preview images and version-tagged release images with migration control and smoke tests),
- OPS-C08 (weekly release automation with SemVer tags and release notes).

## Decision drivers

- Keep delivery aligned with container-first requirements.
- Reduce late-stage deployment risk by introducing hosted environments now.
- Maintain a clear separation between Preview and Release.
- Keep operational complexity reasonable for a capstone timeline.

## Options considered

### Option 1: Local-only deployment flow

- Advantages:
  - Lowest infrastructure setup and operating overhead.
  - Lowest cloud cost.
- Disadvantages:
  - No persistent hosted Preview/Release URLs.
  - Weaker deployment evidence for demos and reviews.
- Risks:
  - Late discovery of hosting issues if a hosted setup is needed later.

### Option 2: Hosted now on Azure Container Apps + Azure Container Registry

- Advantages:
  - Strong alignment with OPS-C04/C05/C08 expectations.
  - Clear image-based release flow (`preview` commit tags, `main` version tags).
  - Persistent Preview/Release endpoints for team validation and demo readiness.
- Disadvantages:
  - Higher setup and maintenance effort.
  - Additional configuration for secrets, environments, and release approvals.
- Risks:
  - Cost drift if resources are not right-sized.
  - Deployment or migration failures in hosted environments.

## Decision

Adopt **hosted environments now** using **Azure Container Apps (ACA)** for runtime and **Azure Container Registry (ACR)** for images.

Operational flow:

- merges to `preview` publish commit-tagged images and deploy to Preview,
- weekly release merges to `main` publish SemVer-tagged images and deploy to Release with approval gates,
- migration application and smoke tests are mandatory pipeline gates for both paths.

## Consequences

- Positive:
  - Earlier operational feedback and fewer release-time surprises.
  - Better evidence for deployment and operations requirements.
  - Repeatable, versioned deployment process.
- Negative:
  - Increased DevOps workload during early project phases.
  - Additional platform operations responsibilities.
- Follow-up actions:
  - Define environment topology and naming in infrastructure docs.
  - Add deployment, rollback, and smoke-test steps to the runbook.
  - Configure budget alerts and right-sizing to control costs.

## Evidence and verification

- Capstone requirement mapping against ARC-07, OPS-C04, OPS-C05, OPS-C08.
- Team alignment discussion recorded in Teams before drafting this ADR.
- Decision alternatives reviewed with explicit trade-offs (cost, risk, delivery evidence).

## AI assistance

AI was used to structure the alternatives and draft wording. Final choice and requirement references were reviewed and confirmed by the author before submission.

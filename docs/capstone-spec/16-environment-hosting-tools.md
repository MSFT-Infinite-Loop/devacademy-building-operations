---
title: Environment, hosting and tools
source_sections: "Appendix B (repo structure), C (Azure hosting), E (suggested tools), I (getting started, learning resources)"
load_when: "Preparing the development environment, deciding on hosting, choosing tools, laying out the repository, or looking for official learning resources."
related: [09-track-devops.md, 10-architecture-tech-policy.md, 14-process-git-planning.md, 19-decisions-questions-risks.md]
---

# Environment, hosting and tools

`[PACK NOTE]` Live environment-readiness status is tracked in the team work items and [`../team/decision-register.md`](../team/decision-register.md). The lists below describe what is needed and when; environment setup must support the walking skeleton.

## 1. Development environment to prepare before kick-off (Appendix I)

| Tool / component | Required version or option | Purpose and notes |
|---|---|---|
| Git | No version specified | Configure with your name and Microsoft email address. |
| .NET SDK | **.NET 10 SDK** | Baseline backend SDK (BE-C01). |
| Backend editor/IDE | **Visual Studio 2026**, or **VS Code with the C# Dev Kit** | Either works for the backend; VS Code also for the frontend. |
| Node.js + package manager | An **active LTS** Node.js; **npm** or **pnpm** | Frontend development and Playwright. |
| Local container platform | **Podman + Podman Desktop**, or **Rancher Desktop** | Open source; run Compose files; use **WSL 2** on Windows. **Docker Desktop is not required.** |
| GitHub Copilot | Included in your Microsoft licence | Enable in your editor, and on GitHub too if the repo is hosted there. |
| Azure CLI and Azure Developer CLI | Current | Only if the team will host on Azure. |
| Database client | Your choice for the chosen DB | VS Code extensions (SQL Server, PostgreSQL, MongoDB, DocumentDB), SQL Server Management Studio, pgAdmin, or DBeaver Community. |

Readiness checklist (tick when done): [ ] Git identity [ ] .NET 10 SDK [ ] IDE [ ] Node LTS + npm/pnpm [ ] Podman/Rancher + WSL 2 [ ] Copilot enabled [ ] Azure CLI/azd (if hosting) [ ] DB client [ ] one-command Compose stack starts (once the repo exists).

## 2. GitHub Copilot access and use
Every participant has Copilot through the Microsoft licence. Enable it in the editor (and on GitHub when the repo is there). Use it across the whole lifecycle, not only for coding, and always inspect, test and understand what it produces. Capabilities mentioned: chat, inline completion, agent mode, code review, coding agent, custom instructions, prompt files, MCP servers (GitHub and Playwright examples). Keep `.github/copilot-instructions.md` and/or `AGENTS.md` current (AI-02). Copilot may explain unfamiliar concepts, but check explanations against official docs and record learning in the AI Engineering Journal. Rules: see 13.

## 3. Azure and hosting (Appendix C)

**General rule:** every participant (as a Microsoft employee) has an Azure subscription with **€150 of credit per month**. Azure is **optional**, recommended for realistic Preview/Release environments. Hosting is **required only if OPS Advanced is in scope**, and even then another host is acceptable if the jury can reach it. The spec does **not** say how to find/activate the credit — check the balance in the Azure portal `[OPEN: ask the jury]`.

**Without hosting:** publish runnable container images; the jury must be able to start the Release version locally with **one command** (OPS-C04, OPS-C05).

**Suggested services**

| Component | Example Azure service | Alternative |
|---|---|---|
| Web app (Next.js or TanStack Start) | Azure Container Apps or Azure App Service | Any container host |
| API and background jobs | Azure Container Apps or Azure App Service | Separate worker container |
| Database | Azure Database for PostgreSQL Flexible Server; Azure SQL Database; Azure Cosmos DB; Azure DocumentDB | Containerized PostgreSQL or MongoDB for Preview, with backups |
| Cache | Valkey, Memcached or Dragonfly container in Azure Container Apps | Same container locally |
| Files | Azure Blob Storage | Local volume (development only) |
| Secrets | Azure Key Vault | GitHub or Azure DevOps secrets |
| Identity | ASP.NET Core Identity or Microsoft Entra ID / External ID | Keycloak |
| Monitoring | Azure Monitor and Application Insights | Grafana stack; Aspire dashboard locally |
| Container registry | Azure Container Registry or GitHub Container Registry | — |
| Real-time | SignalR in the API host or Azure SignalR Service | Server-Sent Events |

**Cost and access guidance (no SKUs prescribed)**
- Check available credit in the Azure portal before provisioning; stay within €150/month.
- Use the smallest suitable tiers; prefer scale-to-zero; stop non-release resources when idle.
- Set budget alerts (example thresholds 50%, 80%, 100%).
- Shared team infrastructure can live in **one participant's subscription**; give teammates access through RBAC with **least privilege**.
- **Delete all project resources after Demo Day.**

**Initial Azure setup (only if hosting):** confirm the subscription → check credit → install Azure CLI and Azure Developer CLI → decide whose subscription hosts shared resources → grant teammates RBAC (least privilege) → create budget alerts → choose small tiers + scale-to-zero → stop non-release resources when unused → delete everything after Demo Day.

## 4. Example repository structure (Appendix B; illustration, not a requirement)
```
/
├── .github/                       # or .azuredevops/ + pipeline folders
│   ├── workflows/                 # CI/CD workflows
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   ├── copilot-instructions.md    # repository AI context (AI-02)
│   └── prompts/                   # team prompt library (AI-09)
├── AGENTS.md                      # agent-oriented instructions (AI-02)
├── CODEOWNERS
├── src/
│   ├── web/                       # Next.js or TanStack Start app
│   ├── api/                       # ASP.NET Core API, modular monolith
│   │   ├── Modules/               # Buildings, Residents, Leases, Maintenance, Billing, Notifications, Audit
│   │   └── Shared/                # auth, validation, caching, persistence, telemetry
│   ├── worker/                    # optional separate background worker
│   └── db/                        # migrations, procedures, views, triggers, seed
├── tests/
│   ├── Api.UnitTests/
│   ├── Api.IntegrationTests/
│   ├── db/
│   ├── web/                       # component tests
│   └── e2e/                       # Playwright
├── infra/                         # Dockerfiles, Compose file, Bicep
├── docs/                          # documentation set (15 §2)
├── compose.yaml
├── CHANGELOG.md
└── README.md
```

## 5. Suggested tools (Appendix E; non-mandatory)
Each listed tool was classified as Microsoft product, open source or approved exception as of **October 2026**. Licences can change — check the exact dependency and version under ARC-10 before adding or upgrading.

| Category | Frontend |
|---|---|
| Framework | Next.js 16+ (App Router, Cache Components) or TanStack Start 1.x |
| Server state | TanStack Query |
| Language | TypeScript |
| Styling | Tailwind CSS or CSS Modules |
| Components | Fluent UI React or shadcn/ui |
| Validation | Zod |
| API client generation | Kiota or openapi-typescript |
| Unit/component tests | Vitest + React Testing Library |
| E2E | Playwright |
| Accessibility testing | axe-core |
| Component catalogue | Storybook |
| Performance testing | Lighthouse CI |

| Category | Backend |
|---|---|
| Runtime | .NET 10 LTS |
| API framework | ASP.NET Core controllers or Minimal APIs |
| Data access | EF Core or Dapper |
| Validation | FluentValidation |
| Caching | HybridCache with Valkey, Memcached (EnyimMemcachedCore) or Dragonfly |
| Background processing | BackgroundService, Hangfire or Quartz.NET |
| Real-time | SignalR |
| Telemetry | OpenTelemetry |
| Interactive API docs | Scalar or Swagger UI |
| Test frameworks | xUnit, NUnit or MSTest |
| Assertions | Shouldly |
| Integration testing | Testcontainers |
| Load testing | k6 or Azure Load Testing |
| HTTP resilience | Microsoft.Extensions.Http.Resilience |
| Image processing | SkiaSharp |
| Local orchestration | Aspire |

| Category | Data |
|---|---|
| SQL | PostgreSQL, SQL Server or Azure SQL |
| Document/NoSQL | MongoDB, Azure Cosmos DB or DocumentDB |
| Migrations | EF Core migrations or DbUp |
| Synthetic data | Bogus |
| Clients | VS Code DB extensions, SSMS, pgAdmin, DBeaver Community |

| Category | DevOps |
|---|---|
| CI/CD | GitHub Actions or Azure Pipelines |
| Work tracking | GitHub Projects or Azure Boards |
| Local containers | Podman + Podman Desktop, or Rancher Desktop |
| Azure hosting | Azure Container Apps or Azure App Service |
| IaC | Bicep |
| Secrets | Key Vault |
| Dependency updates | Dependabot |
| Static analysis | CodeQL |
| Secret scanning | Gitleaks |
| Container scanning | Trivy |
| Dynamic security testing | OWASP ZAP |
| Supply chain | Microsoft SBOM Tool |
| Monitoring | Azure Monitor and Application Insights |

AI tooling: GitHub Copilot (chat, agent mode, code review, coding agent, custom instructions, prompt files, MCP servers) and other tools approved for Microsoft work.

## 6. Official learning resources (Appendix I)

| Topic | Resource |
|---|---|
| React 19 | react.dev |
| Next.js | nextjs.org |
| TanStack Start | tanstack.com/start |
| ASP.NET Core, EF Core, Azure, Azure DevOps | learn.microsoft.com |
| Aspire (local orchestration, Valkey integration) | aspire.dev |
| GitHub Copilot and GitHub Actions | docs.github.com |
| Playwright | playwright.dev |
| Valkey / Memcached / Dragonfly | valkey.io / memcached.org / dragonflydb.io |
| MongoDB / DocumentDB | mongodb.com/docs / documentdb.io |
| Podman / Rancher Desktop | podman.io / rancherdesktop.io |
| OWASP Top 10:2025 and ASVS | owasp.org |
| C4 architecture model | c4model.com |
| Conventional Commits | conventionalcommits.org |

# ADR-00N: API style and conventions for the backend

- **Status:** Proposed
- **Date:** 2026-11-25
- **Author(s):** Petar Ivanov
- **Requirement IDs:** ARC-07, BE-C01, BE-C02, BE-C03, BE-C05, BE-A01, BE-A03, BE-A06, ARC-01, ARC-03, ARC-08, ARC-10, AI-06, SEC-04, SEC-11
- **Supersedes:** None
- **Superseded by:** None
- **Depends on:** frontend ADR (proposed: Next.js 16+ App Router, server-first rendering, so both the Next.js server and the browser call this API), application architecture ADR (proposed: seven modules M1 to M7), database ADR (proposed: PostgreSQL; relevant points: concurrency tokens), hosting ADR (ADR-001, proposed: Azure Container Apps and Azure Container Registry; relevant points: what "Release environment" means in practice)

## Context

BE-C01 requires an ADR for the API style on .NET 10 LTS, built as a modular monolith (ARC-01). The API must:

- return ProblemDetails for errors, `201` with a `Location` header on creation, and be versioned (BE-C02);
- publish an OpenAPI document versioned with the code, with interactive docs that are not exposed in the Release environment (BE-C03);
- return `409` or `422` for domain-rule violations through centralized `IExceptionHandler` handling (BE-C05);
- never leak internals and include a correlation ID in errors (SEC-11);
- use parameterised queries only (SEC-04).

The team is now four people, and BE Advanced is mandatory for a team of four, so three Advanced items also shape API conventions:

- BE-A01: optimistic concurrency for work orders, leases and statements, using ETag with `If-Match` or explicit version fields, with HTTP `412` or `409` semantics and a documented contract.
- BE-A03: payment endpoints accept an `Idempotency-Key` header.
- BE-A06: `429` with `Retry-After` (the rate-limiter details live in the auth ADR).

## Decision drivers

1. Meet BE-C01 to BE-C05 with the least custom code.
2. One error shape on every failure path (validation, binding, 401, 403, 404, 409/422, 429, 500), in every environment.
3. A modular-monolith layout where each module registers its own endpoints.
4. Low learning cost for a 3 to 4 person team.
5. No dependency that fails the licence policy (ARC-10, AI-06).

## Options considered

### Option 1: Minimal APIs, one endpoint group per module

- **Advantages:** Microsoft recommends Minimal APIs for new projects. .NET 10 adds built-in validation (`AddValidation()`, DataAnnotations and `IValidatableObject`). `MapGroup` per module fits the modular monolith.
- **Disadvantages:** Fewer built-in conventions. No `IModelValidator` extensibility, application parts or OData. Team discipline is needed to keep endpoints thin.
- **Risks:**
  - `ThrowOnBadRequest` defaults to true in Development and false in Production, so binding failures in Production can write a bare 400 that bypasses `IExceptionHandler`. The error shape would then differ between environments.
  - `IFormFile` binding (photo uploads, SEC-07) requires antiforgery services and middleware.
  - Unmapped JSON properties are ignored by System.Text.Json by default.

### Option 2: Controllers (`[ApiController]`)

- **Advantages:** Familiar, mature conventions, filters, automatic 400 ProblemDetails.
- **Disadvantages:** More ceremony. Microsoft recommends controllers mainly for model-binding extensibility, advanced model validation, application parts or OData; none are needed.
- **Risks:** Filters can hide behaviour, which makes object-level authorization less explicit.

### Option 3: GraphQL

- **Advantages:** Flexible client queries.
- **Disadvantages:** Does not map naturally onto `201` + `Location`, `409`/`422`, ProblemDetails and versioned REST. Extra dependencies.
- **Risks:** Harder to enforce object-level authorization per field (SEC-03).

## Decision

**Proposed decision (pending team approval):** Option 1.

1. **Style:** Minimal APIs with one `MapGroup` per module (the seven modules M1 to M7 of the application architecture draft, once accepted), versioned by URL segment (`/api/v1/...`) using route groups only. No API-versioning package is proposed, which avoids an extra dependency.
2. **Errors:**
   - `AddProblemDetails()`, `UseExceptionHandler()` and `UseStatusCodePages()` are placed early, so they wrap routing, authentication, authorization and endpoints.
   - One `IExceptionHandler` maps domain exceptions to `409` or `422`.
   - `CustomizeProblemDetails` adds a correlation ID to every ProblemDetails (the default `traceId` is the starting point; to be confirmed during implementation).
   - Rate-limiter rejections (`429`) and authentication or authorization failures also go through `IProblemDetailsService`.
   - `ThrowOnBadRequest` is set explicitly, so every environment behaves the same.
3. **Validation:** `AddValidation()` for request DTOs, with errors written as ProblemDetails through `IProblemDetailsService`.
4. **OpenAPI:**
   - `Microsoft.AspNetCore.OpenApi` generates OpenAPI 3.1.
   - Build-time generation (`Microsoft.Extensions.ApiDescription.Server`) writes a versioned document that is committed with the code.
   - Every operation declares its response types, examples for request and response bodies where useful, and the cookie security scheme on protected operations.
   - The interactive UI (Scalar or Swagger UI, one of them) is mapped only in the Development environment, never in Release.
5. **Creation:** `TypedResults.Created(location, body)`.
6. **Concurrency contract (BE-A01):** responses for work orders, leases and statements carry an `ETag` derived from the database concurrency token; updates require `If-Match`. A stale write returns `412 Precondition Failed`, and a missing `If-Match` returns `428 Precondition Required`. Every such conflict is returned as ProblemDetails. The token mechanism depends on the database ADR (for PostgreSQL the candidates are the `xmin` system column or an explicit version column). The contract is described in the OpenAPI document and covered by stale-write tests.
7. **Idempotency (BE-A03):** payment endpoints accept an `Idempotency-Key` header. A repeated key returns the original result without a second effect. The key store and its rules are defined in the jobs, outbox and real-time ADR.
8. **Rate limiting (BE-A06):** `429` responses are ProblemDetails with a `Retry-After` header.
9. **Cache headers:** authenticated responses are sent with `Cache-Control: no-store` unless an endpoint is explicitly designated cacheable, so the Next.js data cache or any proxy cannot share personalised responses between users.
10. **Consumers:** the Next.js server and the browser consume the same API and the same ProblemDetails shape, including `412`, `428` and `429` with `Retry-After`. A typed client generated from the committed OpenAPI document is proposed to the frontend owner, so contract changes show up as build errors.

### Open points (tracked in follow-up actions, not decided here)

- Choice of Scalar vs Swagger UI (licence and package check).
- The `type` URI convention for ProblemDetails.
- The exact meaning of "Release environment" (hosting ADR).

## Consequences

### Positive

- One validation and error pipeline, with consistent output.
- Endpoint groups map to modules.
- No versioning package to maintain.

### Negative

- The interactive UI needs an extra package.
- Conventions (thin endpoints, module structure, error mapping) must be written down and reviewed.
- URL-segment versioning means a new group per major version.

### Follow-up actions

1. Verify during implementation (**not yet done**): a verification matrix for 400 (binding), 400 and 422 (validation), 401, 403, 404, 409 (domain), 429 and 500, in Development and Production configuration. Each must return ProblemDetails with a correlation ID and no internals.
2. Verify that the committed OpenAPI document includes the schemas, examples and security scheme BE-C03 asks for.
3. Choose Scalar or Swagger UI after checking NuGet licence metadata (**not verified**).
4. Agree the versioning policy (what counts as a breaking change).
5. Verify during implementation (**not yet done**): ETag and `If-Match` over a database concurrency token, returning `412` on a stale write, and idempotent replay with `Idempotency-Key`. Confirm with the database ADR owner which concurrency mechanism is available.
6. Background jobs, the outbox and real-time push (ARC-09, BE-C08, BE-A03, BE-A04) are proposed in `ADR-Jobs-Outbox-and-Real-Time-Push.md`. The `Idempotency-Key` store and replay rules are defined there.
7. Data access and migrations (EF Core with Npgsql, one shared process for applying schema changes agreed with the database owner, BE-C06) are not decided here and are proposed as a separate ADR.

## Evidence and verification

- No code was built or run for this draft, and no .NET 10 SDK was installed when it was written. Everything below is from documentation and source reading.
- Microsoft Learn (links resolve, `view=aspnetcore-10.0`):
  - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/apis
  - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/handle-errors
  - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/parameter-binding
  - https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/aspnetcore-openapi
- Licences read from project repositories: dotnet/aspnetcore is MIT; Scalar is MIT. **NuGet package metadata could not be checked**, because `api.nuget.org` failed with a TLS error on the authoring machine.
- Requirement wording: capstone requirements v1.4, quoted in the working specification `docs/capstone-spec/` (ids above); BE-C03, BE-C05 and ARC-07 wording was re-confirmed against the source document.

## AI assistance

GitHub Copilot (Claude) researched the cited documentation and repositories and drafted this ADR. A second AI review pass critiqued earlier versions and its findings were fixed; later edits (four-person scope, alignment with the frontend, architecture, hosting and database drafts) were not separately reviewed. The claims about platform behaviour come from documentation and source reading, and no code was built or run for this ADR, so none is verified by experiment. Verification is tracked as implementation follow-up (see Follow-up actions) and is not a condition of this ADR. Human review is pending and will happen in the pull request.

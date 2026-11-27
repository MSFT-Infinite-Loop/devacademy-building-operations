# ADR-00N: Authentication and authorization

- **Status:** Proposed
- **Date:** 2026-11-25
- **Author(s):** Petar Ivanov
- **Requirement IDs:** ARC-07, BE-C04, SEC-02, SEC-03, SEC-05, SEC-12, ARC-05, ARC-10, AI-06, M1-04, M1-05, M1-06, BE-A06, BE-A04
- **Supersedes:** None
- **Superseded by:** None
- **Depends on:** frontend ADR (proposed: Next.js 16+ App Router, server-first rendering; this ADR's cookie topology and antiforgery transport must be agreed with it), hosting ADR (ADR-001, proposed: Azure Container Apps and Azure Container Registry; relevant points: HTTPS, domains, reverse proxy) and the jobs, outbox and real-time ADR (real-time connection revocation)

## Context

- BE-C04: ASP.NET Core Identity or OIDC; role AND policy authorization; resource-based handlers for object-level checks; deny by default.
- ARC-05: the browser never stores access tokens in localStorage or sessionStorage; use HttpOnly, Secure, SameSite cookies, directly or through a BFF.
- M1-04: no public self-registration. Administrators invite or create users, and Building Managers invite residents of their buildings. Accounts are never hard-deleted.
- M1-05 and M1-06: object-level authorization, with the API as the enforcement point.
- SEC-02: lockout or throttling and defined session and token lifetimes. **The spec gives no numbers; the team must choose and record them here.**
- SEC-03: deny by default, with IDOR tests. SEC-05: CSRF defence and a CORS allow-list. SEC-12: sign-in rate limiting.
- The team is now four people, and BE Advanced is mandatory for a team of four. That makes two Advanced items part of this decision:
  - BE-A06: rate limiting on sign-in, password reset and other abuse-prone endpoints, with `429` and `Retry-After`, plus OpenTelemetry metrics and a dashboard.
  - BE-A04: server-to-client push (SignalR or SSE) authorised per user and per building, so authentication must also work on the real-time connection.
- Allowed identity providers: ASP.NET Core Identity, Entra ID, Keycloak, OpenIddict.
- DEL-02 and OPS-C04: the jury must start the whole stack with one command and demo accounts for every role.

## Decision drivers

1. No self-registration surface (M1-04); no tokens in browser storage (ARC-05).
2. The stack must run offline from one command, with no external tenant dependency.
3. A deactivated account must lose access promptly and demonstrably.
4. Object-level checks must run after the resource is loaded.
5. Resistance to brute force, account enumeration and CSRF.
6. Low complexity, and licence compliance (ARC-10, AI-06).

## Options considered

### Option 1: ASP.NET Core Identity with cookie authentication and our own endpoints (no `MapIdentityApi`)

- **Advantages:** Self-contained. Cookies satisfy ARC-05. Built-in lockout, PBKDF2 hashing and security stamp. Admin-created and invited users are straightforward to model.
- **Disadvantages:** We write sign-in, sign-out, invitation and reset endpoints ourselves. Cookies make CSRF defences mandatory.
- **Risks:** Defaults that must be overridden: `SecurePolicy` is `SameAsRequest`; the security stamp is only revalidated every 30 minutes; the cookie lasts 14 days sliding; lockout only counts failures when the sign-in call asks for it.

### Option 2: `MapIdentityApi<TUser>` as provided

- **Advantages:** Very little code.
- **Blockers:** It maps an unauthenticated `POST /register`, which conflicts with M1-04. It is documented for simple scenarios, and its bearer tokens are proprietary and would need to live somewhere in the browser (ARC-05).
- **Risks:** Disabling or replacing endpoints defeats its purpose.

### Option 3: External OIDC provider (Entra ID, Keycloak or OpenIddict)

- **Advantages:** Standards-based, SSO, token features. Keycloak and OpenIddict can be self-hosted.
- **Disadvantages:** More moving parts in the one-command stack. Entra ID needs a tenant and network. OpenIddict (Apache-2.0) needs significant setup.
- **Risks:** Uses time needed for Core features. Reasonable only as a deliberately chosen Advanced item.

## Decision

**Proposed decision (pending team approval):** Option 1, with the rules below.

### Session and cookie

- Cookie authentication via Identity. `HttpOnly`, and `SecurePolicy = Always`.
- `SameSite=Lax`. The browser is proposed to reach the API only on the same site as the web app, through the topology in the next section. If the API must be cross-site, the decision is revisited, because `SameSite=None` would raise CSRF exposure.
- Values proposed in the table below.

### Frontend topology (Next.js, proposed to the frontend and hosting owners)

The frontend draft proposes Next.js with server-first rendering, so pages are rendered by a Next.js server that fetches data from this API on the user's behalf, while interactive parts run in the browser. That shapes the auth design:

1. **Single origin.** The browser sees one origin. A reverse proxy in front of the stack (to be agreed in the hosting ADR; the hosting ADR proposes Azure Container Apps, and whether its ingress can provide this single origin, with path routing, WebSocket support, forwarded headers and session affinity, or needs a proxy container is **not verified** and is a question for the hosting owner) sends `/api` and the real-time hub path to the API, and everything else to Next.js. This also gives SignalR a WebSocket path, which Next.js itself should not be relied on to proxy. This satisfies ARC-05 through a BFF-style arrangement: the cookie is `HttpOnly` and no token is ever visible to browser code.
2. **Server-side calls forward identity.** When the Next.js server calls the API for a page render, it forwards the user's session cookie and the original client address. It never uses a shared service credential, so the API still authorises as the real user (M1-05, M1-06). Next.js must not cache personalised responses across users, and the API sends `Cache-Control: no-store` on authenticated responses (see the API style ADR).
3. **Trusted forwarding.** The API honours forwarded-address headers only from the known proxy and Next.js server (`KnownProxies` or `KnownNetworks`). Without this, every request appears to come from the Next.js server, which breaks per-client rate limiting and lockout partitioning. The limiter partitions by hashed username as well, so it still works if the address is unavailable.
4. **CSRF.** Antiforgery validation and origin checks stay at the API for every unsafe cookie-authenticated request. The Next.js server forwards the antiforgery cookie and `X-XSRF-TOKEN` header. Whether Next.js Server Actions' own origin check can stand in for the browser-side token is **not verified** and is raised with the frontend owner. The API does not rely on it.
5. **Sign-in flow.** Sign-in is a request from the browser (through Next.js) to the API's sign-in endpoint. The API's `Set-Cookie` is passed back to the browser unchanged. How Server Actions or route handlers relay this is for the frontend owner to confirm during implementation.

### Deactivation (M1-04)

- Deactivating a user sets `IsActive = false` **and** updates the user's security stamp.
- The sign-in path refuses inactive users.
- The security-stamp validation interval is set short, so an existing cookie stops working within that bound. Normal sign-out only deletes the current browser's cookie; it does not affect other sessions.
- An integration test must prove that a deactivated user's existing session is rejected within the chosen bound.

### Authorization

- Fallback policy requires an authenticated user (deny by default).
- Role policies, plus `AuthorizationHandler<TRequirement, TResource>` invoked imperatively through `IAuthorizationService` **after** the resource is loaded. Attribute-only checks run before data loading and cannot do object-level checks.
- Every object-level endpoint gets an IDOR test (SEC-03).
- A resident's relationship to a unit comes from the ownership, lease and lease-tenant, or household-member records proposed in the database ADR, and the role assignment supplies the account's role and building scope. The resource-based handlers read these relationships and the API enforces them (M1-05, M1-06).

### Real-time connections (BE-A04)

The same cookie authenticates the SignalR connection (or an SSE stream if that were chosen instead). The jobs, outbox and real-time ADR defines the mechanism, and this ADR constrains it:
- Because SignalR does not revalidate the user during a connection, the connection must load the user's current `IsActive` state and assignments from the database when it is established.
- Deactivation and changes of role or building scope publish a revocation event to every API instance, and each instance aborts that user's connections.
- Recipients are resolved server-side, and push is addressed to `user:{id}` only; there are no client-chosen groups.
- Antiforgery and origin checks apply to the negotiation request.

### Anonymous endpoints (the full list)

Sign-in, invitation redemption, password-reset request and completion (if implemented), antiforgery-token issuance, and explicitly designated health checks. Everything else is authenticated by the fallback policy.

### Sign-in hardening (SEC-02, SEC-12, BE-A06)

- Sign-in calls `PasswordSignInAsync(..., lockoutOnFailure: true)`.
- The built-in rate limiter partitions unauthenticated attempts by trusted client address plus a hashed, normalised username; rejections return `429`. `Retry-After` is set explicitly from the lease metadata in `OnRejected`.
- The same limiter policy family covers sign-in, password-reset request and completion, invitation redemption and any other abuse-prone endpoint (BE-A06). Rejections and lockouts are exported as OpenTelemetry metrics for the BE-A06 dashboard.
- Sign-in and reset-request responses are indistinguishable for unknown, inactive, locked and valid accounts (generic ProblemDetails, same shape and similar timing). Targeted-lockout abuse is a known trade-off, bounded by the rate limit.

### Invitations (M1-04)

Invite tokens are high-entropy and single-use, expire, and are revocable. They are stored only as hashes and scoped to the invited email, role and building. They are excluded from logs. The redemption page sets a no-referrer policy. Resending an invite revokes the previous one.

### CSRF (SEC-05)

- Antiforgery validation is required on every unsafe-method cookie-authenticated endpoint, including sign-in and sign-out. The `XSRF-TOKEN` cookie and `X-XSRF-TOKEN` header carry it.
- Minimal API JSON endpoints do not validate antiforgery automatically, so a group-level endpoint filter calls `IAntiforgery.ValidateRequestAsync`. To be confirmed during implementation.
- Origin or `Sec-Fetch-Site` checks are added as defence in depth.
- CORS is an explicit origin allow-list; no wildcard with credentials.

### Values to be chosen by the team (SEC-02)

| Setting | .NET default (reference) | Proposed value |
|---|---|---|
| Cookie lifetime / sliding expiration | 14 days, sliding | TBD by team |
| Security-stamp validation interval | 30 minutes | shortest practical (candidate: validate on every request or ≤ 1 minute) |
| Lockout threshold / duration | 5 attempts / 5 minutes | TBD by team |
| Password policy | min. length 6 | TBD (stronger than default) |
| Sign-in rate limit | none | TBD by team |
| `RequireUniqueEmail` | false | true |

## Consequences

### Positive

- No self-registration surface, and the stack runs fully offline.
- Object-level authorization is explicit and testable.
- Deactivation behaviour is defined, bounded and testable.

### Negative

- More custom endpoints to write and test (sign-in, sign-out, invite, reset).
- Email delivery for invites and resets needs a demo-safe design.
- Cookie authentication makes CSRF handling mandatory in the frontend too.
- A very short security-stamp interval costs a database read per request.

### Follow-up actions

1. Agree the origin and cookie topology (the Next.js section above) with the frontend and hosting owners, including the reverse proxy.
2. Fill in the table above and record the reasoning.
3. Verify during implementation (**not yet done**): deactivation within the bound; antiforgery on JSON endpoints; generic responses and `Retry-After` on `429`; a Next.js server-side render that forwards the cookie and client address, with the forwarded-header trust configured.
4. Design the invite and reset flow, plus demo accounts for every role (DEL-02).
5. Check package licences from NuGet metadata (**not verified**).
6. Verify during implementation (**not yet done**): cookie authentication on a SignalR connection, including aborting it on deactivation across two instances (see the jobs, outbox and real-time ADR), and OpenTelemetry metrics for rate-limit rejections.

## Evidence and verification

- No code was built or run for this draft. Sources are documentation and source reading.
- Microsoft Learn (links resolve, `view=aspnetcore-10.0`):
  - https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity
  - https://learn.microsoft.com/en-us/aspnet/core/security/authentication/cookie
  - https://learn.microsoft.com/en-us/aspnet/core/security/authorization/resourcebased
  - https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery
  - https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit
- Source: `MapIdentityApi` in dotnet/aspnetcore, branch release/10.0 (`src/Identity/Core/src/IdentityApiEndpointRouteBuilderExtensions.cs`), which maps an unauthenticated `/register`. The defaults in the table were read from the Identity documentation and source.
- Licences read from repositories: dotnet/aspnetcore is MIT; OpenIddict is Apache-2.0. **NuGet metadata was not verified** (TLS failure to `api.nuget.org` on the authoring machine).
- Requirement wording (M1-04, SEC-02, ARC-05, BE-C04) was re-confirmed against capstone requirements v1.4.

## AI assistance

GitHub Copilot (Claude) researched the cited documentation and repositories and drafted this ADR. A second AI review pass critiqued earlier versions and its findings were fixed; later edits (four-person scope, alignment with the frontend, architecture, hosting and database drafts) were not separately reviewed. The claims about platform behaviour come from documentation and source reading, and no code was built or run for this ADR, so none is verified by experiment. Verification is tracked as implementation follow-up (see Follow-up actions) and is not a condition of this ADR. Human review is pending and will happen in the pull request.

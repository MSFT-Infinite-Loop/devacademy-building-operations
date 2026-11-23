---
title: Security and privacy requirements (SEC)
source_sections: "8 (SEC-01..SEC-15), Section 15 security items"
load_when: "Designing or reviewing authentication, authorization, input handling, uploads, secrets, scanning, logging, error handling, rate limiting, privacy, least privilege, or preparing the docs/security evidence."
related: [07-track-backend.md, 09-track-devops.md, 08-track-data.md, 15-deliverables-assessment-acceptance.md]
---

# Security and privacy requirements (SEC)

## 1. In short
- Every API endpoint checks both the user's **role** and their **relationship** to the specific record.
- All input validated **on the server**. Secrets stay out of Git and container images.
- Dependencies and container images are scanned and patched or formally excepted.
- **Only synthetic data. Minimise personal data.**
- Use **OWASP Top 10:2025** and **OWASP ASVS 5.0 Level 1** as security checklists.

Evidence location: `docs/security/` (threat model, ASVS checklist, scan results, documented exceptions, privacy notes).

## 2. Requirements

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| SEC-01 | MUST | ALL | Create and maintain a **threat model** with a **data-flow diagram** and a **STRIDE-style** analysis (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege), covering principal threats and mitigations. Update it as the system changes; include the final version in the submission. | Final threat model in `docs/security/` matching the final architecture |
| SEC-02 | MUST | ALL | Authentication uses secure password storage from ASP.NET Core Identity or the chosen identity provider. Account lockout or throttling. **Define session and token lifetimes explicitly.** Secure cookie flags. Sign-out invalidates the session. Tokens never in `localStorage`/`sessionStorage`; use HttpOnly, Secure, SameSite cookies, directly or via a BFF. **No fixed lifetime, timeout, lockout count or throttle number is prescribed — choose and document them.** | Auth config/code; documented lifetimes and rationale; lockout config; cookie config; sign-in/sign-out/session-invalidation tests; storage check; auth ADR |
| SEC-03 | MUST | ALL | Authorization is **deny by default**. Every endpoint performs object-level checks on role AND relationship to the resource. Generate automated authorization tests from the permissions matrix, including **IDOR** attempts (changing an ID to reach another user's records). | Policy/resource-handler code; matrix-based test suite; negative tests; cross-resident IDOR tests; manager cannot reach unassigned buildings |
| SEC-04 | MUST | ALL | Validate all input on the server. **Parameterized queries only.** Encode output. Sanitize rich text on the server with an **allow list**. Configure a **Content Security Policy** (normally the `Content-Security-Policy` header). | Validators + tests; parameterized-access evidence; sanitizer config + malicious-input tests; CSP config |
| SEC-05 | MUST | ALL | **CSRF** protection whenever cookies authenticate API requests (antiforgery tokens and/or SameSite cookies plus origin checks). **CORS** restricted to explicitly known origins; no unrestricted origins for credentialed calls. | Antiforgery/SameSite/origin config; per-environment CORS allow-list; tests that an unauthorized origin is denied |
| SEC-06 | MUST | ALL | HTTPS everywhere except local development. Configure **HSTS, Content-Security-Policy, X-Content-Type-Options, Referrer-Policy and CSP `frame-ancestors`**. | Deployment/middleware config; header test on Preview/Release; HTTP redirected or unavailable |
| SEC-07 | MUST | ALL | **Uploads:** allow-listed file types; verify actual content (not the filename extension or client MIME type); size limits; randomized storage names; store outside the web root or in blob storage; downloads via an authorized endpoint or short-lived signed URL; images SHOULD be re-encoded or metadata-stripped (for example with SkiaSharp). Product limit for maintenance requests: up to **3 photos**; example types JPEG, PNG, WebP; example limit **5 MB** per photo (worked example rejects a 12 MB image: "each photo must be 5 MB or smaller"). If your enforced limit differs from the 5 MB example, document it. | Upload validation code/tests (extension/content mismatch, disallowed type, oversized, malformed); randomized names; authorization tests for downloads; signed-URL expiry config |
| SEC-08 | MUST | ALL | **No secrets in source control or container images.** Secret scanning per OPS-C06 (GitHub/Azure DevOps scanning with push protection where available; otherwise Gitleaks as pre-commit hook and CI step). Secrets in pipeline secrets, variable groups or Key Vault. Document a rotation procedure; rotate any leaked secret **immediately**. Cloud deployments SHOULD use OIDC workload-identity federation, not long-lived keys. | Full-history secret scan; scanner settings; CI scan; image inspection; redacted secret-store config; written rotation procedure. **"No secrets anywhere in repository history" is a BLOCKING item.** |
| SEC-09 | MUST | ALL | Scan **dependencies and container images** in CI (OPS-C07 adds static analysis). Example tools: Dependabot, `dotnet list package --vulnerable`, `npm audit`, CodeQL, .NET analyzers, ESLint security rules, Trivy, Microsoft Defender for Cloud. Before a release all **Critical and High** findings are fixed or covered by a documented exception. | CI workflow; scan outputs; release history; zero unresolved Critical/High or an exceptions log (risk, justification, mitigation, owner, review status) |
| SEC-10 | MUST | ALL | Never log passwords, tokens, complete personal data or uploaded file contents; mask personal data that must appear. Log and audit security-relevant events (failed sign-ins, permission denials, role changes). | Structured-log samples with correlation IDs and no sensitive values; masking config; audit entries for those events |
| SEC-11 | MUST | ALL | Client-facing errors are generic: **RFC 9457 ProblemDetails with a correlation ID**. Internal details and stack traces only in protected logs. | Central exception handler; ProblemDetails examples/tests; no stack traces/SQL/paths/secrets in responses; matching log entry via correlation ID |
| SEC-12 | MUST | ALL | **Rate limiting on the sign-in endpoint** (Core). If BE-A06 is in scope, also on password reset and all abuse-prone endpoints, returning **HTTP 429** with `Retry-After`. **No requests-per-minute/burst/lockout number is prescribed** — choose, document and test one. | Rate-limiter config + rationale; threshold test; 429 + `Retry-After` evidence; normal traffic unaffected |
| SEC-13 | MUST | ALL | **Privacy by design (GDPR mindset).** Synthetic data only. Minimise personal data; document every personal field with its purpose. Residents can view their personal data. Define retention periods. Handle erasure by **anonymization**: Core = documented approach; if DB-A06 is in scope, implement the anonymization procedure and retention job. Preserve financial and audit integrity. | Data inventory/dictionary (field, purpose, access, retention); synthetic-seed review; "view my data" flow + authorization tests; documented erasure procedure; DB-A06 scripts/tests if applicable |
| SEC-14 | MUST | ALL | **Least privilege everywhere:** application DB login (never owner/admin), migration identity (separate one SHOULD be used), cloud identities, CI tokens, administrative features. Credentials from a secret store; DB TLS where supported; prefer managed identities for Azure access. | DB grants/roles + connection config; proof the app cannot do admin operations; managed/workload identity config; CI token permissions; admin-feature authorization tests |
| SEC-15 | SHOULD | ALL | Complete an **OWASP ASVS 5.0 Level 1** self-assessment with a status per applicable item. Teams with **OPS Advanced** must also run a **DAST baseline scan** (OPS-A05), for example OWASP ZAP. | ASVS checklist with status/evidence/justification; DAST report if OPS Advanced; triaged findings |

## 3. Acceptance items (Section 15)
- Required (not blocking): threat model completed; security headers configured; CSRF protection; CORS restricted; uploads handled safely; sign-in rate-limited; no tokens in browser storage; dependency, code and container scanning running with findings triaged; authorization tests (including cross-resident denial) run in CI.
- **Blocking:** no secrets anywhere in repository history (caps the Team Score at 50 if missed).

## 4. Interpretation notes
1. SEC-02 prescribes no session lifetime — define and document one.
2. SEC-12 prescribes no rate-limit threshold — choose, document and test one.
3. SEC-07 has no universal size limit; M4-01 gives 5 MB and up to three photos as the product example.
4. SEC-09's release gate is categorical: no unaddressed Critical or High finding; a documented exception is allowed.
5. SEC-13 Core only requires a documented anonymization approach; implementation becomes mandatory with DB-A06.
6. SEC-15 is a SHOULD, but the submission documentation expects the ASVS checklist, so treat it as expected evidence.

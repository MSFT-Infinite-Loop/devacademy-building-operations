---
name: security-evidence-review
description: "Use when: reviewing capstone security/privacy requirements, threat-model evidence, authorization/IDOR, sessions, CSRF/CORS, uploads, secrets, scans, logging, rate limits, privacy, least privilege, ASVS, or DAST."
argument-hint: "Work item, feature, PR, architecture area, or evidence audit"
user-invocable: true
disable-model-invocation: false
---

# Security Evidence Review

Audit security design, implementation, tests, and evidence against SEC-01 through SEC-15.

For an explicit vulnerability or exploitability review, invoke the dedicated security-review agent first and incorporate its verified findings. This skill does not replace specialist security review.

## Safeguards

- Start read-only.
- Never expose secrets, tokens, personal data, exploit payloads containing real data, or protected logs.
- Never mark missing evidence as secure.
- Distinguish design intent from implemented and tested controls.
- Critical/High findings require fixes or an approved documented exception before release.
- Obtain confirmation before code, issue, exception, or remote changes.

## Review domains

1. STRIDE threat model and data-flow diagram.
2. Authentication, lockout/throttling, session/token lifetimes, cookies, sign-out.
3. Deny-by-default object authorization and IDOR tests.
4. Server validation, parameterization, encoding, sanitization and CSP.
5. CSRF, SameSite, origin checks and restricted CORS.
6. HTTPS, HSTS and security headers.
7. Upload content validation, limits, storage, metadata and authorized downloads.
8. Secrets in history/images, push protection, Gitleaks, rotation and OIDC.
9. Dependency, source and container scanning with exception handling.
10. Safe logs, audit events and RFC 9457 ProblemDetails with correlation IDs.
11. Rate limiting and documented thresholds.
12. Data minimization, purpose, retention, access and anonymization.
13. Least-privilege DB/cloud/CI/admin identities.
14. ASVS Level 1 and, because OPS Advanced is in four-person scope, DAST evidence.

## Procedure

1. Resolve applicable SEC, OPS, BE, DB, FE and product requirements.
2. Read threat model, ADRs, code, tests, CI, scan outputs and exceptions.
3. Classify every applicable control:
   - Verified;
   - Partial;
   - Missing;
   - Unknown;
   - Not applicable with justification.
4. Link evidence and identify required negative tests.
5. Rank findings by severity and confidence.
6. Separate immediate blockers from planned hardening.
7. Present exact proposed fixes/evidence updates and obtain confirmation.
8. Verify any approved remediation with tests and rescans.

## Output

Return:

- requirement/control matrix;
- findings with severity, confidence and evidence;
- missing authorization and abuse tests;
- scan/exception status;
- privacy and least-privilege gaps;
- release blockers;
- remediation proposal and verification results.

# API conventions

- **Status:** Draft (all rules are proposals for team review)
- **Date:** 2026-11-25
- **Author(s):** Petar Ivanov
- **Requirement IDs:** ARC-08, BE-C02, BE-C03, BE-A01, BE-A03, BE-A06
- **Related:** API style ADR (`docs/adr/ADR-API-Style.md`), jobs, outbox and real-time push ADR, database ADR

ARC-08 asks for documented API conventions: naming, versions, pagination, filtering and sorting, errors, ETag and idempotency headers, dates, and money. This draft records the proposed rules so the backend, frontend and database owners work from the same ones. It is the shared reference that the API style ADR points to, and it is expected to grow during implementation. Rules marked **(TBC)** depend on a decision outside the backend.

## Versions and paths

- All endpoints live under `/api/v1/`. A new major version gets a new route group (`/api/v2/`) only for breaking changes; the old version stays available until the team retires it.
- Breaking changes: removing or renaming a field, changing a type or a status code, tightening validation. Adding an optional field or a new endpoint is not breaking.
- The OpenAPI document is generated from the code, committed with it, and is the contract the typed client is built from.

## Naming

- Paths use lowercase, plural nouns with hyphens: `/work-orders`, `/buildings/{buildingId}/floors`. Nest a resource at most one level under its parent.
- State changes are modelled as a sub-resource, for example `POST /work-orders/{id}/transitions`, not as free verbs in the path.
- JSON property names are `camelCase`. Enumerations are strings in `PascalCase` without spaces, derived from the documented state names (for example `InProgress`, `OnHold`).
- Identifiers are opaque strings in the API. The underlying key type is decided in the database ADR **(TBC)**.

## Methods and status codes

| Operation | Method | Success | Notes |
|---|---|---|---|
| Read one or many | `GET` | `200` | Authenticated responses carry `Cache-Control: no-store` unless an endpoint is designated cacheable |
| Create | `POST` | `201` + `Location` | Returns the created resource |
| Partial update | `PATCH` | `200` | Requires `If-Match` for resources with a concurrency contract |
| Action or transition | `POST` | `200` or `204` | Requires `If-Match` where the resource has one |
| Delete | `DELETE` | `204` | Rare: accounts and financial records are never hard-deleted (M1-04); use a status change |

Errors: `400` malformed or invalid input, `401` not signed in, `403` signed in but not permitted for the role, `404` not found or not visible to the caller, `409` conflict with the current state, `412` precondition failed (stale `If-Match`), `422` valid request that breaks a domain rule, `428` precondition required (missing `If-Match`), `429` rate limited (with `Retry-After`), `500` unexpected.

## Errors

- Every error is RFC 9457 ProblemDetails with `type`, `title`, `status`, `detail` (safe text), a correlation id, and for validation an `errors` map keyed by field name. No stack traces, SQL, or internal names.
- The `type` URI convention is to be decided (TBC); until then use stable short identifiers per error kind.
- The same shape applies to authentication, authorization, binding, validation, domain, rate-limit and unhandled errors, in every environment.

## Pagination, filtering and sorting

- List endpoints take `page` (from 1) and `pageSize` (default 25, maximum 100) and return `{ items, page, pageSize, totalCount }`.
- Filters are plain query parameters named after the field: `status=Assigned&priority=High`. Repeating a parameter means "any of". Unknown parameters return `400`.
- Sorting uses `sort=<field>` for ascending and `sort=-<field>` for descending, for example `sort=-dueAt`. Every list has a stable default order with a unique tie-breaker so pages do not overlap.
- Authorization filters are applied before pagination, so counts never reveal records the caller cannot see.

## Concurrency and idempotency headers

- Resources with an optimistic-concurrency contract (work orders, leases, statements) return an `ETag` and require `If-Match` on updates. Stale writes return `412`; a missing `If-Match` returns `428`.
- Payment endpoints require an `Idempotency-Key` header. The same key with the same request returns the original result and records nothing new. The same key with a different request (for example a different amount) is rejected with `422`. While the first request with a key is still being processed, a repeat gets `409`. Keys expire after a documented period.

## Dates, times and money

- Instants are UTC ISO 8601 with `Z`, for example `2026-11-25T14:00:00Z`. The API never accepts or returns local times; the frontend formats them for the user.
- Calendar dates with no time (billing periods, lease start and end) are `YYYY-MM-DD`.
- Money is an object `{ "amount": "123.45", "currency": "RON" }` with the amount as a decimal string, never a floating-point number. Rounding rules for billing are defined in the billing feature specs **(TBC with the database owner and the billing module)**.

## Open questions

1. Key type and format of identifiers (database ADR).
2. `type` URI convention for ProblemDetails.
3. Whether the money object uses minor units instead of a decimal string.
4. Default currency and locale handling for English and Romanian (X6 is optional).
5. Cursor pagination for very large lists (audit trail) in place of page numbers.

---
title: Frontend track (FE) — Core and Advanced packages
source_sections: "6 (intro), 6.1, Rendering Strategy Table, FE acceptance criteria"
load_when: "Owning or reviewing anything frontend: framework choice, rendering strategy, forms, optimistic UI, the 2D map, accessibility, responsive layouts, frontend tests/performance."
related: [02-product-m1-m4.md, 03-product-m5-m7-px.md, 10-architecture-tech-policy.md, 12-quality-testing.md]
---

# Frontend track (FE)

**Purpose:** make the product usable, accessible and performant, and decide deliberately where every page is rendered. A designer-quality visual treatment is **not** expected: a consistent, readable, accessible interface using a component library (for example Fluent UI React or shadcn/ui) is enough.

**Package rules (all tracks):** every item in a required package is a MUST unless the item says otherwise. Substituting an item needs the jury's written approval. FE Core is required for every team. FE Advanced is required for a team of 4, or when a team of 3 selects it in Week 1.

Table schema: `ID | Level | Scope | Requirement | Evidence`. Scope CORE = required for every team; ADVANCED = required when FE Advanced is in the team's scope.

## FE Core (≈ 25 h)

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| FE-C01 | MUST | CORE | React **19.2+** with **Next.js 16+ (App Router)** or **TanStack Start 1.x**. TypeScript **strict mode**. Linter and formatter run in CI. Next.js 15 or earlier is not permitted as the starting version. | ADR for the framework choice; repo config showing framework/version, strict TS, lint, format |
| FE-C02 | MUST | CORE | Define the rendering strategy for **every route** (static/prerendered, SSR, streaming SSR, CSR) plus server/client component boundaries where supported. Include at least 1 personalized SSR route, 1 cached or prerendered route, and 1 client-rendered interactive area (the map). | Rendering Strategy Table in `docs/architecture` with a reason for every route |
| FE-C03 | MUST | CORE | Role-specific layouts and navigation. Protected routes; redirect unauthenticated/unauthorized users. Dedicated **403, 404 and 500** pages. | Code; E2E smoke test for navigation and access by role |
| FE-C04 | MUST | CORE | Typed API client (SHOULD be generated from the OpenAPI document, for example with Kiota or openapi-typescript). Server-state caching and revalidation (for example TanStack Query or framework caching). Every view supports loading, empty, error and success states. Access tokens are never stored in browser storage. | Code; screenshots of the four states |
| FE-C05 | MUST | CORE | Forms via React 19 Actions (`useActionState`, `useFormStatus`) or a suitable form library. Client validation mirrors server rules (a shared validation schema SHOULD be used). Map server ProblemDetails validation errors to individual fields; move focus to the first invalid field; show pending/submission states. | Form implementation; component tests |
| FE-C06 | MUST | CORE | Optimistic UI for at least **2 low-risk interactions** (for example mark a notification read, add a comment) using `useOptimistic` or cache-level updates. On failure roll back and give clear feedback. Document where optimistic UI was deliberately avoided (for example payments) and why. | Code; automated test or recording of the rollback/failure path |
| FE-C07 | MUST | CORE | The data-driven 2D floor map from M2-04..M2-06: renders from layout and live status data; keyboard and screen-reader support; equivalent list view; role-appropriate data exposure; lazy loading. | Code; accessibility-check report |
| FE-C08 | MUST | CORE | **WCAG 2.2 Level AA** for core flows: semantic HTML, landmarks, labels, visible focus, sufficient contrast, status not conveyed by colour alone, accessible charts. Automated **axe** checks in CI; manually complete both signature scenarios with keyboard and screen reader. | Accessibility report in `docs/testing` (automated + manual) |
| FE-C09 | MUST | CORE | Resident and technician workflows work at **360 px** viewport width. Manager and administrator workflows work on desktop and tablet layouts. | Screenshots of the required viewports |
| FE-C10 | MUST | CORE | Error boundaries per route or route segment. Degrade gracefully when the API or the real-time channel is unavailable; offer a retry. | Code; demonstrated failure scenario |
| FE-C11 | MUST | CORE | Component tests for key UI (forms, floor map, status badges). **Playwright** E2E tests for both signature scenarios (shared with OPS). Accessibility assertions included. | Tests passing in CI |

## FE Advanced (≈ 20 h) — all six are MUST when FE Advanced is in scope

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| FE-A01 | MUST | ADVANCED | Stream dashboard widgets independently behind Suspense boundaries with skeleton placeholders. Build or measure a non-streamed comparison; record **TTFB and LCP** for both. | Measurements and comparison in `docs/performance` |
| FE-A02 | MUST | ADVANCED | Advanced caching for the chosen framework. Next.js: Cache Components, `use cache`, cache tags, post-mutation revalidation. TanStack Start: route loaders, query prefetching, hydration, invalidation. Document what is cached in browser, web server and API and how each layer is invalidated. | Caching map; implementation code |
| FE-A03 | MUST | ADVANCED | Live notification badge and live work-order updates via **SignalR or Server-Sent Events**, with reconnection, backoff, reconciliation with the client cache, and a polling fallback. | Demonstration; tests |
| FE-A04 | MUST | ADVANCED | Kanban workflow with optimistic card moves. Handle version/concurrency conflicts returned as **HTTP 409 or 412** with a clear refresh-or-merge experience. Keyboard-accessible alternative to drag-and-drop. | Demonstration; tests incl. conflict handling and keyboard use |
| FE-A05 | MUST | ADVANCED | Measure the three Core Web Vitals **LCP, INP, CLS** (Lighthouse CI or `web-vitals`). Enable the **React Compiler** or otherwise optimize with React Profiler evidence. Code-split heavy UI (map, charts). Before-and-after measurements. | Report in `docs/performance` with profiler and Core Web Vitals evidence |
| FE-A06 | MUST | ADVANCED | Documented reusable component library (for example Storybook with accessibility checks). Design tokens for colour, spacing and typography, used consistently. Light and dark themes. | Published component catalogue |

## Rendering Strategy Table (FE-C02 deliverable)
Location: `docs/architecture`. It must cover **every route** (not just samples). Columns: **Route | Who | Rendering | Data freshness | Why**. For frameworks with server/client components also mark which parts are server components and which need client execution. It must include at least: one personalized SSR route; one cached or prerendered route; one client-rendered interactive area (the floor map); a rationale for each route.

Options per route: prerendered/static; per-request SSR; streaming SSR; client rendering; hybrid (server shell + client-rendered interactive regions).

Representative rows from the spec (examples of the expected level of detail, not a mandatory route structure):

| Route | Who | Rendering | Data freshness | Why |
|---|---|---|---|---|
| `/sign-in` | Everyone | Prerendered/static | No changing application data | Fast first load; no personalised data |
| `/announcements` | Residents and technicians | Server-rendered, cached per building | Revalidate when an announcement is published or expires | Many users see the same slowly changing content |
| `/dashboard` | Managers | Streaming SSR | Per request | Personalised; slow widgets stream without blocking the page |
| `/buildings/{id}/floors/{floor}` | All roles, subject to authorization | Server-rendered shell + client-rendered map | Refresh on focus or every **30 seconds** | Highly interactive; statuses change often |
| `/work-orders/{id}` | Reporter, manager, technician (authorized) | Server-rendered with optimistic client updates | Load per request; revalidate after each change | Personalised page with many small interactions |

## Frontend acceptance criteria

**Blocking (failing any caps the Team Score at 50)**
- Frontend runs on React 19 with Next.js 16+ or TanStack Start 1.x.
- 2D floor map is data-driven, keyboard-accessible and has an equivalent list alternative.
- All four roles exist; automated tests prove one resident cannot access another resident's records by changing identifiers (the API enforces it, the frontend shows the correct role-specific experience).
- Modules M1–M7 and both signature scenarios work end-to-end on the Release environment.

**Required (not blocking)**
- Rendering Strategy Table provided. At least 2 optimistic interactions with rollback behaviour.
- Pagination, search, filtering, sorting on data-heavy lists. Loading/empty/error/success states on every data view.
- Advanced packages required by the team size completed.
- Component, E2E, authorization and accessibility tests run in CI. No access tokens in browser storage.

**Map-specific:** changing layout or status data changes the displayed map (no hard-coded geometry or statuses, no static image); every map operation works by keyboard alone; automated accessibility check on the map page reports no critical violations; the 2D map is never replaced by the optional 3D view.

**Testing:** component tests cover forms, floor map, optimistic rollback and other key UI; Playwright automates Scenarios A and B plus sign-in and role smoke tests; accessibility evidence = no critical automated violations + working keyboard and screen-reader paths; all automated tests run in CI and a failing test blocks merging; **no mandatory coverage-percentage threshold** (focus on meaningful tests of risky behaviour).

**Assessment:** frontend engineering and UX are worth **15 of the 100 Team Score points** (category C). Full marks need a deliberate rendering strategy, optimistic UI with tested rollback, all data states, accessible and responsive workflows, and a consistent usable interface. Advanced frontend work is judged only if FE Advanced is required for the team's size.

## Related requirements outside this track
M2-04..M2-06, M2-08 (map) · PX-01..PX-05 (lists, states, validation, UTC, money) · ARC-04, ARC-05 (data only through the API; no tokens in browser storage) · SEC-04..SEC-06 (CSP, CSRF, CORS, headers) · QA-02 (test levels) · FE-C11 shares Playwright work with OPS.

## First tasks `[PACK NOTE]`
1. Frontend framework ADR (Next.js 16+ vs TanStack Start 1.x) — a Week-1 decision.
2. Walking skeleton: sign-in + one page wired web → API → DB (Week 2).
3. Draft the Rendering Strategy Table early and extend it route by route.
4. Choose the component library (Fluent UI React or shadcn/ui) and set lint/format/strict TS in CI.
5. Build the map from a JSON layout (one building, one floor) as the first M2 slice; add the list view and keyboard support early.

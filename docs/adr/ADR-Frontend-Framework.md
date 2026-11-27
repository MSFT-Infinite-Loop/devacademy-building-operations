# ADR-00N: Frontend Framework

- **Status:** Proposed
- **Date:** 2026-11-23
- **Author(s):** Carlos Natera
- **Requirement IDs:** `ARC-07`, `FE-C01`, `FE-C02`, `FE-C03`, `FE-C04`, `FE-C05`, `FE-C07`, `FE-C08`, `FE-C10`, `FE-A01`–`FE-A04`, `FE-A05`, `FE-A06`, `PX-01`, `ARC-04`, `ARC-05`, `ARC-10`, `SEC-05`, `SEC-12`, `OPS-C04`
- **Supersedes:** None
- **Superseded by:** None

## Context

The Building Operations Platform is a signed-in application with role-specific dashboards, filtered work queues, a live floor map, and billing and audit screens. The [capstone frontend requirements](../capstone-spec/06-track-frontend.md) permit Next.js 16+ with App Router or TanStack Start 1.x. Both options require React 19.2+, strict TypeScript, and linting and formatting in CI. The team is new to both frameworks.

This ADR covers the framework (`D-06`), rendering, role layouts and route protection, the frontend sign-in path, forms, refresh and failure recovery, performance, and the component library (`D-16`). It does not select a client data library. The authentication provider and session policy, backend cache, live-update transport, and hosting provider are outside this ADR's scope. The frontend, including server-rendered pages, gets persistent data only through the backend API. The API remains responsible for authorization.

## Decision drivers

- Support Core and Advanced frontend requirements: personalized server rendering, independent dashboard widget streaming, an interactive and accessible floor map, and predictable updates after edits.
- Make data-dependent screens useful on the first visit without waiting for the browser to start a separate data request.
- Keep routine saves simple without doing unrelated work on every live update.
- Keep repeated work simple. For example, bookmarking the work queue while it shows **Assigned** orders on **page 2** should restore those filters when the link is reopened.
- Prefer a framework the team can learn and troubleshoot using maintained documentation, relevant examples, and a documented container deployment path.
- Give shared controls a consistent, product-specific look and room for workflow-specific behavior while preserving accessibility in both themes.

## Options considered

### Option 1: Next.js 16+ with App Router

- **Advantages:** Longer track record and a broader pool of learning and troubleshooting resources. App Router organizes screens by URL and lets server-rendered widgets load and stream independently behind their own `Suspense` boundaries.
- **Disadvantages:** Typed links do not validate filter values in a URL. We would write and reuse a small filter-validation convention for work queues, statements, audit history, and similar lists.
- **Risks:** Older Pages Router examples and earlier App Router caching guidance can be misleading. Use guidance that matches the version we adopt. Be explicit about cache boundaries so that refreshed views do not remain stale and personalized data is not shared across users.

### Option 2: TanStack Start 1.x

- **Advantages:** Its router gives us a standard way to validate and type URL filters for each screen. Route loaders can start requests together and stream slower results to individual widgets.
- **Disadvantages:** Its stable framework release is newer, so the pool of framework-specific examples and troubleshooting material is smaller.
- **Risks:** Route loaders can run in the browser as well as on the server. Calls that need server-side credentials or request context must use an explicit server-only boundary.

### Rendering option: Server-first data pages with browser interactivity

- **Advantages:** A bookmarked work queue can arrive with the requested rows as part of the server-rendered response. The browser still handles controls, forms, and other interactions.
- **Disadvantages:** The first useful view still depends on how quickly the API supplies the essential data.
- **Risks:** Slow secondary data can block ready content if everything is fetched before rendering. Dashboard widgets should stream independently as required by `FE-A01`.

### Rendering option: Browser-first data pages by default

- **Advantages:** A lightweight page shell can appear before the API data is ready.
- **Disadvantages:** On a fresh visit, the browser must fetch the data before the main content is useful.
- **Risks:** Users can see an earlier page shell but wait longer for the information they need. The capstone's required server-rendered and streamed routes would still need exceptions.

### Refresh option: Refresh the current view by default; target frequent updates

- **Advantages:** Routine saves follow one simple pattern. Live updates can refresh only the data that changed.
- **Disadvantages:** Refreshing a view can repeat reads for sections that did not change.
- **Risks:** Refreshing a view does not guarantee fresh data if it reads from a stale cache.

### Refresh option: Target affected data for every change

- **Advantages:** Avoids refreshing unrelated parts of a view.
- **Disadvantages:** More features must track what each change affects, even when a view contains little more than the record being edited.
- **Risks:** Updating only the edited record can leave filtered lists, counts, and summaries out of sync.

### Component library option: shadcn/ui

- **Advantages:** Adds ready-made controls as editable source files. We can change a shared control's appearance or behavior directly and reuse it across screens. It has a documented Next.js setup and supports light and dark themes through shared tokens.
- **Disadvantages:** We maintain the copied code and bring in upstream fixes ourselves. Its table primitives are a starting point, not a fully assembled data grid.
- **Risks:** Local changes can break keyboard navigation, focus handling, or screen-reader behavior. Keep customizations in shared controls and test them in the workflows that use them.

### Component library option: Fluent UI React v9

- **Advantages:** Provides packaged controls, themes, and a ready-made data grid. Maintainer fixes can come through package updates.
- **Disadvantages:** Customizations that go beyond the public options may require wrappers or replacement controls instead of edits to the underlying component.
- **Risks:** The styling setup would need to be verified with our server-rendered Next.js App Router pages.

## Decision

### Framework

**Use Next.js 16+ with App Router, React 19.2+, and strict TypeScript, subject to team review.**

Both options can support the workflows that matter. TanStack Start's built-in URL filter validation is useful, but a shared helper can cover that need in Next.js. The board's rollback after a rejected edit and refresh after a live update are not reasons to favor Start: both frameworks can use TanStack Query, and this ADR does not choose it. Both can stream the manager dashboard; Next.js offers a direct way to do so and more resources to help the team learn, debug, and self-host the app. That makes Next.js the better fit for this team, not a claim that it is faster or more reliable.

### Default rendering approach

**Render data-dependent pages server-first; use the browser for interactive parts.** For work queues, statements, and audit history, the Next.js server fetches the data through the backend API and includes it in the server-rendered view. These screens have little value without their records, so sending a page shell and waiting for the browser to fetch the data adds a step without giving users a useful first view.

Server-first does not mean waiting for every section. Dashboard widgets stream independently behind placeholders, and the browser renders the interactive floor map using API data. The Rendering Strategy Table will document each route's choice, including at least one personalized server-rendered route and one cached or prerendered route (`FE-C02`, `FE-A01`).

### Role layouts and protected routes

**Use one shared app shell with role-specific layouts and navigation for administrators, building managers, residents, and technicians (`FE-C03`).** Share common controls and accessibility patterns, but show navigation and actions appropriate to the user's role.

Check access at protected routes and where they load protected data. Hiding links is not a guard, and [Next.js can reuse layouts between navigations](https://nextjs.org/docs/app/guides/authentication#layouts-and-auth-checks). Redirect signed-out users to sign-in and signed-in users denied access to a dedicated 403 screen. Use dedicated 404 and 500 screens for missing pages or resources and unexpected page failures, respectively. Respect the API's access decisions, including when it returns 404 rather than disclosing whether a resource exists. The API still authorizes each read and write.

### API data and session boundary

**Use a typed API client** for frontend calls, preferably generated from the backend's versioned OpenAPI document when available (`FE-C04`). Never store access tokens in browser storage (`ARC-05`). The API authorizes the user on both request paths:

- **The browser calls the API directly.** On signed-in requests, the browser sends its session cookie to the API through the proposed same-origin proxy. Next.js does not relay the request.
- **Next.js renders a protected page.** The browser sends the session cookie to Next.js with the page request. To load the page data, Next.js forwards that cookie on a separate server-side API read. It uses the requesting user's session, not a shared service identity.

Keep personalized pages and their API responses out of shared Next.js caches. Use shared caching only for content agreed safe to share with the API and caching owners. The [API-style](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/20) and [backend caching](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/22) proposals inform this boundary without choosing the frontend cache implementation.

### Sign-in request path

**Submit sign-in from the browser to the API through the proposed same-origin reverse proxy, without a Next.js relay.** Next.js serves the sign-in page. The form sends the API's required antiforgery token, shows pending state and sign-in errors, and navigates after success. The API validates credentials, retains its antiforgery and rate-limit checks (`SEC-05`, `SEC-12`), and sends the session cookie to the browser. The cookie's scope must cover both page and API requests under the public address.

A Next.js Server Action could handle submission and redirect on the server, including supporting submission before the browser's JavaScript loads. For this flow, the form can handle the API result directly. That avoids an extra internal request and removes the need for Next.js to relay the request context or the API's `Set-Cookie` response during sign-in.

**Use only a trusted client address for sign-in rate limiting (`SEC-12`).** The public proxy discards untrusted forwarded-address information and supplies the client address it establishes. The API accepts forwarded addresses only from configured hops so it does not treat different client addresses as one proxy address. An address does not replace account-level protections. Next.js does not forward the address for direct sign-in. If it later relays a request whose API policy needs the client address, it must preserve only the proxy-established address, and the API must explicitly trust that Next.js hop.

Reconcile this choice with the Next.js relay described in the [Authentication and Authorization proposal](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/23), including the cookie scope and antiforgery flow. The [Hosting and Deployment ADR](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/19) still needs to identify the proxy and confirm that it can route the web app and API under one public address and supply the trusted client address. This choice does not set rate-limit thresholds or determine the submission path for other forms.

### Antiforgery on writes

**Keep antiforgery validation at the API for writes in the cookie-based flow (`SEC-05`).** On a direct API write, the browser sends the required cookies and supplies the antiforgery request token in the header proposed by the auth ADR (`X-XSRF-TOKEN`). If a Next.js Server Action or Route Handler relays a write, it forwards the relevant session and antiforgery cookies and sends the token supplied with the submission in that same API header. The [Next.js Server Action origin check](https://nextjs.org/docs/app/api-reference/config/next-config-js/serverActions#allowedorigins) is an additional safeguard, not a replacement for API validation.

### Forms and validation

**Use React 19 form Actions by default (`FE-C05`).** [`useActionState`](https://react.dev/reference/react/useActionState) lets forms show pending and submission outcomes without adding a form library. A library would not remove the need to map API errors and manage focus. Choosing React form Actions does not require using Next.js Server Actions.

Mirror API rules that can be checked in the browser, preferably with a shared validation schema. The API still validates every submission. Preserve edits on rejection, show `ProblemDetails` validation errors next to the matching fields, and move focus to the first invalid field. Show errors that do not belong to a field in a form summary.

Revisit [React Hook Form](https://react-hook-form.com/docs/usefieldarray) only if a real workflow makes the Action-based form state hard to maintain. For example, start with Actions for a lease with multiple tenants; reconsider if adding or removing tenant rows requires substantial custom state to keep validation errors on the right row.

### Refreshing already-open views

**After an ordinary successful save, refresh the current view in place without reloading the browser tab. Use targeted refreshes for live work-order updates and the notification badge.** This avoids tracking every dependency on simple pages while keeping frequent updates from redoing unrelated work. Add other targeted cases only when there is a clear benefit.

**Treat a live update as a hint to fetch fresh data (`FE-A03`).** The [jobs, outbox, and real-time ADR](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/28) proposes SignalR. With that design, the signed-in browser connects to the API's hub through the same public proxy, not through Next.js. The API sends an event type and only the IDs the recipient may see, not the record contents. The browser then fetches the affected data from the normal API, which checks access as usual.

Define affected data once per live feature and use the same rule for a confirmed local edit and an authorized live update from another user's edit. For example, when the 4B work order moves from **Assigned** to **In Progress**, refresh the affected work-order lists and counts so the card drops out of the **Assigned** list, not just changes its label. An incoming notification refreshes the badge without refreshing the page underneath it. Revalidate affected frontend cache entries when needed; refreshing a view alone does not invalidate its underlying caches (`FE-A02`).

The work-order board can show a move before the API confirms it. If the API rejects the move because the order has changed, undo the move and let the user refresh or reconcile with the current state (`FE-A04`). If the API-style proposal is accepted, the edit sends the version it was based on using `If-Match`, and a stale edit returns `412 Precondition Failed`.

### Failure recovery

**Use Next.js [error boundaries](https://nextjs.org/docs/app/getting-started/error-handling#nested-error-boundaries) per route or route segment (`FE-C10`).** If rendering fails unexpectedly, show a fallback with a retry for the affected section so the rest of the app can stay usable. Handle expected request and connection failures in the relevant view or form.

Use plain-language messages where the user is working. Say what could not load, update, or save, explain the impact, and offer a next step the user can take. Make status changes perceivable to assistive technology (`FE-C08`) and keep internal diagnostics out of the UI.

- **Live connection down, API reachable:** Keep the view and saves usable. Poll the API while retrying the live connection with backoff. On reconnect, refetch the affected data to reconcile missed updates (`FE-A03`). For example: "Live updates paused. Checking for updates periodically."
- **API unavailable:** If it is safe for the current signed-in session, keep the last successful data visible and mark it as out of date. If nothing can be shown, use a load error instead of an empty state. Offer a retry for the read. For example: "Couldn't load work orders. Try again."
- **Save not confirmed:** Preserve the user's edits and do not silently submit the write again. Let the user check the latest data before retrying. For example: "We couldn't confirm the save. Your edits are still here. Check the latest data before trying again."

### Frontend performance

**Code-split the interactive floor map and chart code at their client component boundaries (`FE-A05`).** Use [Next.js lazy loading](https://nextjs.org/docs/app/guides/lazy-loading) so unrelated pages do not need those bundles. Keep the equivalent map list usable without the renderer and reserve space for deferred charts so they do not push other content around.

Use [React Profiler](https://react.dev/reference/react/Profiler) first to find and fix expensive renders, then repeat the same interaction to verify the improvement. For example, check whether selecting one unit causes unrelated map elements to re-render. Revisit [React Compiler](https://react.dev/learn/react-compiler/introduction) if profiling shows avoidable rendering across several screens, and compare the same workflows before and after enabling it.

Measure LCP, INP, and CLS before and after optimization with Next.js's built-in [`useReportWebVitals`](https://nextjs.org/docs/app/api-reference/functions/use-report-web-vitals). Use production builds with the same synthetic data, browser settings, and signed-in dashboard and floor-map workflows. Include keyboard or pointer interactions so the run measures INP as well as loading and layout stability.

### Component library

**Use shadcn/ui as the starting point for shared controls.** Editable source lets us give the product a consistent look and adapt controls to our workflows without being limited to a packaged component's configuration. For example, one status badge can show **In Progress** with text and an icon across the work-order board, work queue, and floor-map list. Fluent UI can support the same outcome; we prefer the option to edit the shared control directly and accept the maintenance that comes with it.

## Consequences

- **Positive:** The team can use a well-documented pattern for route layouts and dashboard streaming. Users can read the initial records without waiting for browser code to fetch them. Routine saves share a refresh convention; live work-order and badge updates leave unrelated content alone. Shared controls can evolve with the product without diverging screen by screen.
- **Negative:** We own the shared URL filter convention, the mapping of live changes to affected data, and the upkeep of copied controls. API latency affects when essential content appears, and in-place view refreshes can repeat some reads.
- **Follow-up actions:** Write the required route-by-route Rendering Strategy Table. For `FE-A02`, demonstrate Cache Components, `use cache`, cache tags, and revalidation after changes; document what is cached in the browser, web server, and API without deciding the backend cache here.
  - Agree with the backend owner which events refresh which views and counts. Confirm the live connection setup and proxy routing with the auth and hosting owners (`FE-A03`).
  - Define shared color, spacing, and typography tokens and publish a component catalogue covering light and dark themes (`FE-A06`). Before adding dependencies, verify their exact versions and licences (`ARC-10`) and follow the AI-assisted dependency checks (`AI-06`).
  - Build the web image with a multi-stage Dockerfile, a minimal runtime base, a non-root user, and a health check. Include the web app in the one-command local stack both from source and from published version images (`OPS-C04`).

## Evidence and verification

- The requirements and maintainer documentation support the comparison: [Next.js streaming](https://nextjs.org/docs/app/getting-started/fetching-data#with-suspense), [typed links](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes), and [self-hosting](https://nextjs.org/docs/app/guides/self-hosting); [TanStack Start's stable release](https://tanstack.com/blog/tanstack-start-1-0), [URL filter validation](https://tanstack.com/router/latest/docs/framework/react/guide/search-params), and [deferred loading](https://tanstack.com/router/latest/docs/framework/react/guide/deferred-data-loading).
- The component comparison is based on [shadcn/ui's source distribution](https://ui.shadcn.com/docs), [Next.js setup](https://ui.shadcn.com/docs/installation/next), and [theming](https://ui.shadcn.com/docs/theming), and [Fluent UI React v9's setup](https://fluent2.microsoft.design/get-started/develop) and [table and data grid documentation](https://github.com/microsoft/fluentui/blob/master/packages/react-components/react-table/library/README.md).

The pending checks below are implementation follow-ups, not conditions for accepting this ADR. They have not been run, and no prototype or benchmark has been run for this proposal.

- **Pending — initial rendering:** In a production-style container setup with synthetic data, verify that the server-rendered response for a bookmarked work queue includes only the viewer's authorized rows for the selected filters, without relying on a browser-side fetch for the initial list. Check that a second user never sees the first user's data. Stream a deliberately delayed dashboard widget, verify it fills in independently, and compare time to first byte (TTFB) and largest contentful paint (LCP) with a non-streamed version (`FE-A01`).
- **Pending — role navigation and access:** Smoke-test navigation and direct visits to protected routes for all four roles. Verify the sign-in redirect and the dedicated 403, 404, and 500 screens (`FE-C03`).
- **Pending — sign-in and session forwarding:** Verify that the proxy routes direct browser calls to the API without a Next.js relay and that the API's sign-in antiforgery and rate-limit checks still apply. Confirm that rate limiting uses the proxy-established client address and ignores untrusted forwarding information. Check that rejected sign-in shows an error without establishing a session. After successful sign-in, verify that the browser sends the cookie with the first protected page request and that Next.js forwards it on its server-side API read.
- **Pending — antiforgery on writes:** With synthetic data, verify that an authorized write with a valid token succeeds, and that the API rejects a missing or invalid token without changing data. Verify each implemented submission path, including any Next.js relay (`SEC-05`).
- **Pending — forms:** Add component tests for submission feedback, preserved edits on rejection, and focus on the first invalid field. Verify that a rejected lease submission after adding or removing a tenant shows errors on the correct row (`FE-C05`).
- **Pending — refresh:** Verify that an ordinary save updates the current view without a full reload. Check that the signed-in browser connects to the live endpoint through the public proxy without a Next.js relay. Use two authorized sessions to verify that a work-order hint triggers an API refetch for the affected lists and counts and that a notification hint refreshes the badge without refreshing the route. Verify rollback of an optimistic move rejected by the API (`FE-A03`, `FE-A04`).
- **Pending — recovery:** Simulate a live-connection drop and verify polling and reconciliation on reconnect. Check that an API outage shows a load error or visibly out-of-date data with a retry, and that an unconfirmed save preserves edits without resubmitting. Verify accessible messages and that a render failure shows a retry without replacing unaffected sections (`FE-A03`, `FE-C10`).
- **Pending — frontend performance:** Inspect production client bundles to verify that unrelated routes do not need map and chart code. Record the before-and-after Web Vitals results and separate React Profiler recordings in `docs/performance` (`FE-A05`).
- **Pending — shared controls:** Check the work queue and assignment dialog in both themes, including first-render styling, keyboard focus, and screen-reader labels. This is an early check, not a substitute for the required Core accessibility verification (`FE-C08`).

## AI assistance

GitHub Copilot helped compare the options and draft this record. Framework, form, profiling, and component-library capabilities were checked against the maintainers' documentation. The frontend owner discussed the proposed framework, rendering, role layouts, sign-in path, forms, refresh and recovery, performance, and component library. Team review of the revisions and implementation checks are pending.

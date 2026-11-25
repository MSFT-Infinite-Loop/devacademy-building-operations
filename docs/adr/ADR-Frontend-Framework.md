# ADR-00N: Frontend Framework

- **Status:** Proposed
- **Date:** 2026-11-23
- **Author(s):** Carlos Natera
- **Requirement IDs:** `ARC-07`, `FE-C01`, `FE-C02`, `FE-C04`, `FE-C07`, `FE-C08`, `FE-A01`–`FE-A04`, `FE-A06`, `PX-01`, `ARC-04`, `ARC-05`, `ARC-10`
- **Supersedes:** None
- **Superseded by:** None

## Context

The Building Operations Platform is a signed-in application with role-specific dashboards, filtered work queues, a live floor map, and billing and audit screens. The [capstone frontend requirements](../capstone-spec/06-track-frontend.md) permit Next.js 16+ with App Router or TanStack Start 1.x. Both options require React 19.2+, strict TypeScript, and linting and formatting in CI. The team is new to both frameworks.

This ADR addresses the framework choice (`D-06`), the default rendering approach, how already-open views refresh, and the component library (`D-16`). It does not select a client data library. The authentication approach, backend cache, live-update transport, and hosting provider are outside this ADR's scope. The frontend, including server-rendered pages, gets persistent data only through the backend API. The API remains responsible for authorization.

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

### API data and session boundary

**Use a typed API client** for frontend calls, preferably generated from the backend's versioned OpenAPI document when available (`FE-C04`). Server-rendered reads use the signed-in user's session, not a shared service identity, so the API still authorizes each request. Never store access tokens in browser storage (`ARC-05`).

Keep personalized pages and their API responses out of shared Next.js caches. Use shared caching only for content agreed safe to share with the API and caching owners. The [API-style](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/20) and [backend caching](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/22) proposals inform this boundary without choosing the frontend cache implementation.

The [Authentication and Authorization proposal](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/23) covers session cookies and protection against forged requests. Its proposed single public address for the web app and API still needs confirmation in the [Hosting and Deployment ADR](https://github.com/MSFT-Infinite-Loop/devacademy-building-operations/pull/19). This ADR does not choose how cookies are forwarded or how that routing is provided.

### Refreshing already-open views

**After an ordinary successful save, refresh the current view in place without reloading the browser tab. Use targeted refreshes for live work-order updates and the notification badge.** This avoids tracking every dependency on simple pages while keeping frequent updates from redoing unrelated work. Add other targeted cases only when there is a clear benefit.

Define affected data once per live feature and use the same rule for a confirmed local edit and an authorized live update from another user's edit. For example, when the 4B work order moves from **Assigned** to **In Progress**, refresh the affected work-order lists and counts so the card drops out of the **Assigned** list, not just changes its label. An incoming notification refreshes the badge without refreshing the page underneath it. If the live connection drops, poll for updates while retrying the connection with increasing delays. On reconnect, fetch current data to reconcile the affected views rather than assuming no events were missed (`FE-A03`). Revalidate affected frontend cache entries when needed; refreshing a view alone does not invalidate its underlying caches (`FE-A02`).

The work-order board can show a move before the API confirms it. If the API rejects the move because the order has changed, undo the move and let the user refresh or reconcile with the current state (`FE-A04`). If the API-style proposal is accepted, the edit sends the version it was based on using `If-Match`, and a stale edit returns `412 Precondition Failed`.

### Component library

**Use shadcn/ui as the starting point for shared controls.** Editable source lets us give the product a consistent look and adapt controls to our workflows without being limited to a packaged component's configuration. For example, one status badge can show **In Progress** with text and an icon across the work-order board, work queue, and floor-map list. Fluent UI can support the same outcome; we prefer the option to edit the shared control directly and accept the maintenance that comes with it.

## Consequences

- **Positive:** The team can use a well-documented pattern for route layouts and dashboard streaming. Users can read the initial records without waiting for browser code to fetch them. Routine saves share a refresh convention; live work-order and badge updates leave unrelated content alone. Shared controls can evolve with the product without diverging screen by screen.
- **Negative:** We own the shared URL filter convention, the mapping of live changes to affected data, and the upkeep of copied controls. API latency affects when essential content appears, and in-place view refreshes can repeat some reads.
- **Follow-up actions:** Write the required route-by-route Rendering Strategy Table. For `FE-A02`, demonstrate Cache Components, `use cache`, cache tags, and revalidation after changes; document what is cached in the browser, web server, and API without deciding the backend cache here.
  - Define shared color, spacing, and typography tokens and publish a component catalogue covering light and dark themes (`FE-A06`). Before adding dependencies, verify their exact versions and licences (`ARC-10`) and follow the AI-assisted dependency checks (`AI-06`).

## Evidence and verification

- The requirements and maintainer documentation support the comparison: [Next.js streaming](https://nextjs.org/docs/app/getting-started/fetching-data#with-suspense), [typed links](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes), and [self-hosting](https://nextjs.org/docs/app/guides/self-hosting); [TanStack Start's stable release](https://tanstack.com/blog/tanstack-start-1-0), [URL filter validation](https://tanstack.com/router/latest/docs/framework/react/guide/search-params), and [deferred loading](https://tanstack.com/router/latest/docs/framework/react/guide/deferred-data-loading).
- The component comparison is based on [shadcn/ui's source distribution](https://ui.shadcn.com/docs), [Next.js setup](https://ui.shadcn.com/docs/installation/next), and [theming](https://ui.shadcn.com/docs/theming), and [Fluent UI React v9's setup](https://fluent2.microsoft.design/get-started/develop) and [table and data grid documentation](https://github.com/microsoft/fluentui/blob/master/packages/react-components/react-table/library/README.md).
- **Pending — initial rendering:** In a production-style container setup with synthetic data, verify that the server-rendered response for a bookmarked work queue includes only the viewer's authorized rows for the selected filters, without relying on a browser-side fetch for the initial list. Check that a second user never sees the first user's data. Stream a deliberately delayed dashboard widget, verify it fills in independently, and compare time to first byte (TTFB) and largest contentful paint (LCP) with a non-streamed version (`FE-A01`).
- **Pending — refresh:** Verify that an ordinary save updates the current view without a full reload. Use two authorized sessions to verify that a work-order transition updates the affected lists and counts and that an incoming notification updates the badge without refreshing the route. Verify polling while disconnected, reconciliation after reconnecting, and rollback of an optimistic move rejected by the API (`FE-A03`, `FE-A04`).
- **Pending — shared controls:** Check the work queue and assignment dialog in both themes, including first-render styling, keyboard focus, and screen-reader labels. This is an early check, not a substitute for the required Core accessibility verification (`FE-C08`). No prototype or benchmark has been run.

## AI assistance

GitHub Copilot helped compare the options and draft this record. Framework and component-library capabilities were checked against the maintainers' documentation. The frontend owner selected the framework, rendering default, refresh convention, and component library during discussion; independent team review and implementation checks are pending.

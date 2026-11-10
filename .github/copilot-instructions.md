# Repository instructions

## Authority and decision status

- The official DevAcademy capstone requirements document is the source of truth.
- Distinguish mandatory requirements, recommendations, team proposals, and unresolved decisions.
- Never invent approvals, contributors, decisions, evidence, hours, tests, pull requests, releases, or journal entries.
- Treat every value marked `TBD` as unresolved. Ask before making a consequential choice.
- A derived requirements pack may be added under `docs/capstone-spec/` only after team and jury review. It remains secondary to the official source.

## Fixed constraints

- Build the Building Operations Platform with Core modules M1-M7 and the four required roles.
- Enforce object-level authorization in the API; hiding UI controls is not authorization.
- Use synthetic data only. Never add real personal data, credentials, tokens, or secrets.
- Preserve exact monetary calculations and auditable history.
- Core user flows must target WCAG 2.2 AA.
- Check the approved technology and licence policy before adding dependencies.

## Engineering workflow

- Use English for code, UI, documentation, commits, pull requests, and work items.
- Link work to requirement IDs and GitHub issues where available.
- Keep changes focused and use short-lived branches from `preview`.
- Normal pull requests target `preview`; weekly release pull requests target `main`.
- Add or update tests, documentation, ADRs, and evidence when the change requires them.
- Disclose material AI assistance and explain how its output was verified.
- Do not claim a check passed unless it was actually run and its result is known.

## Safety and remote operations

- Do not create or modify remote issues, projects, permissions, hosted resources, releases, tags, or jury communications without explicit human approval.
- Do not silently choose package ownership, Advanced packages, frameworks, database, authentication, caching, or hosting.
- Surface failures explicitly; do not replace errors with success-shaped fallbacks.

## Build and test

Exact commands are TBD until the walking skeleton and ADRs exist. Read the root README and relevant project files, then use only commands that are present and verified in the repository.

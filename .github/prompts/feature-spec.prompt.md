---
name: "Feature Specification"
description: "Use when drafting a requirements-traceable feature specification before implementation."
argument-hint: "Feature name, work item, and requirement IDs"
agent: "agent"
---

Create or update one feature specification under `docs/specs/` using the [feature specification template](../../docs/templates/feature-spec-template.md).

Before writing:

1. Identify the feature, users, work item, and requirement IDs.
2. Read the relevant official requirements or approved repository summary.
3. Check the Team Charter and accepted ADRs for applicable decisions.
4. Mark missing facts as `TBD` or open questions; do not invent decisions.

The specification must include:

- problem and affected users;
- scope and exclusions;
- Given/When/Then acceptance criteria;
- negative, validation, and object-level authorization cases;
- proposed API contract and errors;
- data changes, migrations, constraints, and indexes;
- security, privacy, accessibility, and operability considerations;
- edge cases and failure modes;
- risk-based test plan;
- dependencies and open questions;
- requirement and work-item traceability;
- AI assistance and verification notes.

Do not implement the feature. Present the completed specification for human review.

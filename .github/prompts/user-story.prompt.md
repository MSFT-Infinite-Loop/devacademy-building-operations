---
name: "User Story"
description: "Use when drafting one requirements-traceable user story with Given/When/Then acceptance criteria, negative authorization cases, dependencies, tests, and Definition of Done."
argument-hint: "Role, capability, outcome, parent epic, and requirement IDs"
agent: "agent"
---

Draft one user story for human review.

Include:

- title;
- parent M1-M7 epic;
- requirement IDs;
- `As a [role], I want [capability], so that [outcome]`;
- explicit scope and exclusions;
- Given/When/Then acceptance criteria;
- invalid-input and failure behaviour;
- object-level authorization and IDOR denial cases;
- accessibility expectations for UI work;
- dependencies and blockers;
- expected test levels;
- documentation, ADR, migration, security, and operability impacts;
- proposed Project fields;
- Definition of Done checklist;
- open questions.

Mark unresolved owner, package, estimate, iteration, priority, and dates as `TBD`. Do not create the GitHub issue or invent decisions.

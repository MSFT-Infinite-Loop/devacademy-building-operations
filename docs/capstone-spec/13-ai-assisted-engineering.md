---
title: AI-assisted engineering requirements (AI)
source_sections: "10 (10.1 lifecycle, 10.2 AI-01..AI-12), AI evidence contents, Section 15 AI items"
load_when: "Setting up Copilot instructions, writing specs before implementation, keeping the AI Engineering Journal, filling PR AI disclosures, or preparing the AI usage statement."
related: [14-process-git-planning.md, 15-deliverables-assessment-acceptance.md, ../templates/ai-journal-entry.md, ../templates/feature-spec-template.md]
---

# AI-assisted engineering (AI)

## 1. In short
- Use AI throughout the engineering lifecycle while remaining **responsible for every merged line**.
- Keep repository-level AI instructions, write **specifications before major implementation**, and update the **AI Engineering Journal every week**.
- **Owned code you cannot explain in the technical interview earns no credit.**
- AI features inside the product (X4) are optional and do **not** replace the assessed AI-assisted engineering practice.

## 2. Five operating principles

| Principle | Required behaviour | Evidence |
|---|---|---|
| Ownership | You are responsible for every line you merge, whether it came from a person, inline completion, chat or a coding agent. | PR ownership, review evidence, ability to explain/change the code in the interview |
| Verification | Do not trust generated output by default: read every diff, run it, test it. | PR verification notes, CI runs, local test evidence, journal reflections |
| Data protection | No secrets, credentials, real personal data or confidential company code in tools not approved for that data. | Clean repo/history; appropriate tool choice; sanitised journals/PRs |
| Transparency | Disclose material AI assistance. | PR AI-assistance sections; final team AI usage statement |
| Learning | Use AI to accelerate and extend your work, not to avoid understanding it. | Journals showing reasoning/lessons; interview walkthrough and modification |

## 3. AI across the lifecycle (10.1)

| Phase | Expected AI use | Verification you must perform |
|---|---|---|
| Discovery and design | Brainstorm domain edge cases; draft user stories and acceptance criteria; compare architecture choices; draft ADRs and Mermaid diagrams | Check against the capstone requirements; team review |
| Implementation | Scaffolding, endpoints, components, migrations, refactorings; agent mode for multi-file work | Read every diff; keep PRs small; run and test locally |
| Testing | Generate tests from acceptance criteria; propose edge cases; Playwright scripts; test data | Deliberately break the behaviour and confirm each test fails for the right reason |
| Code review | AI review on PRs; security-focused review prompts | Human approval stays mandatory; address or dismiss every AI comment with a documented reason |
| Data | Draft SQL; explain execution plans; suggest indexes | Validate plans and results with realistic data volumes |
| Operations | Pipeline YAML, Dockerfiles, Bicep/IaC, log/trace analysis | Least privilege; dry runs; never give secrets to prompts |
| Documentation | Draft README, runbooks, release notes | Check every statement against the running system |

## 4. Requirements

| ID | Level | Scope | Requirement | Evidence |
|---|---|---|---|---|
| AI-01 | MUST | ALL | Use **GitHub Copilot through the Microsoft licence**. Any additional AI tool must be approved for Microsoft work. Never put secrets, credentials, real personal information or confidential company code/data into an unapproved tool. | Journal and PR entries naming tools; tool approval; no sensitive data in prompts/logs/history |
| AI-02 | MUST | ALL | Maintain `.github/copilot-instructions.md`, `AGENTS.md`, or both, describing architecture, engineering conventions, build commands, test commands, security rules and the Definition of Done. Update them whenever architecture, conventions or commands change. | Committed file; history showing updates alongside relevant changes |
| AI-03 | MUST | ALL | For every major feature write a short **specification in `docs/specs/` before AI-assisted implementation**: problem, acceptance criteria, API contract, data changes, test cases. Link it from the PR. **Each participant authors at least 2 specs.** | ≥ 2 authored specs per participant; commits proving they precede implementation; PR links |
| AI-04 | MUST | ALL | An individual **AI Engineering Journal**: **at least 1 entry every week and at least 10 entries total per participant**; at least **3 entries** must analyse output that was wrong, insecure, outdated or over-engineered and how it was detected. | Journal with date, work item, prompt/context summary, outcome, verification, risks/errors, time impact, lessons; counts met |
| AI-05 | MUST | ALL | Apply the same reviews, tests and scanners to AI-generated work as to human work. Split large agent-generated changes into reviewable PRs. **Prove generated tests are meaningful by confirming they fail when the behaviour is broken.** | Small focused PRs; human reviews; green CI/scans; mutation-style evidence or journal notes |
| AI-06 | MUST | ALL | Before accepting an AI-suggested dependency, verify it exists, is the intended package (not a look-alike), is actively maintained, and has a licence permitted under ARC-10. | Dependency-review notes; PR checklist; README licence list; package/repo verification |
| AI-07 | MUST | ALL | Add an **AI-assistance section to the PR template**. The final report includes a **team AI usage statement** (tools, uses, what worked and did not). | PR template + completed disclosures; statement in `docs/ai/` |
| AI-08 | SHOULD | ALL | Enable AI-assisted PR review (for example Copilot code review) only as a **supplement** to human review. It never replaces mandatory human approval. | Review config; AI comments + human approval |
| AI-09 | SHOULD | ALL | A team library of **at least 3 reusable prompt files** (for example under `.github/prompts/`): endpoint with tests, migration, Playwright test, ADR draft. | ≥ 3 prompt files + index in `docs/ai/` |
| AI-10 | SHOULD | ALL | Delegate **at least one well-scoped work item** to an AI coding agent that opens a PR; review it normally; reflect in the journal. | Linked work item; agent-opened PR; human review and CI; journal entry |
| AI-11 | MAY | ALL | Use MCP servers (for example GitHub, Playwright, database tools) with least-privilege permissions and development data only; document the configuration. | MCP configuration documentation |
| AI-12 | MUST | ALL | Be able to **explain and modify any code you own**, including generated code, in the technical interview. Code you cannot explain does not count. | Interview walkthrough/live change; ownership and journal/PR evidence |

## 5. Required content of the AI evidence

**Repository AI instructions file:** architecture and boundaries · coding/repo conventions · exact build commands · exact test commands · security rules · Definition of Done · updated when any of these change.

**Feature spec (`docs/specs/`, template D.4):** problem and affected users · acceptance criteria (Given/When/Then preferred) · API endpoints, payloads, errors · data entities, migrations, indexes · edge cases and failure modes · test plan · open questions · link from the implementation PR · ≥ 2 authored specs per participant.

**Journal entry (template D.5):** date + work item · tool and mode (chat, inline completion, agent mode, coding agent, code review) · goal · how it was prompted and what context was supplied · outcome (accepted / modified / rejected, and why) · verification performed · what was wrong or risky and how it was caught · estimated time saved or lost · lesson and what to do differently. Minimums: 1/week, 10 total, 3 failure analyses.

**PR AI disclosure:** none / minor (completions) / material · tools used · what was generated · how it was verified · human review and CI results.

**Prompt library:** ≥ 3 prompt files in a discoverable place (for example `.github/prompts/`) + an index under `docs/ai/`.

**Team AI usage statement:** tools used · how each was used · what worked · what did not · verification and control practices · material assistance disclosed consistently with PR history.

## 6. Prohibited practices
- Submitting code, tests or docs the owner cannot explain.
- Fabricating journals, commits, reviews or effort records (academic-integrity breach).
- Approving a PR solely because an AI reviewer approved it.
- Using AI to evade security requirements, licence restrictions or programme rules.
- Treating optional in-product AI features as a replacement for assessed AI-assisted engineering practice.

## 7. Acceptance items (Section 15)
- **Blocking:** AI usage disclosed in PRs and in the team AI usage statement; every participant has an AI Engineering Journal.
- **Required:** repository AI instructions file and at least 2 feature specs per participant · Team Charter, current project plan, backlog with acceptance criteria, Definition of Done and weekly notes · each participant's effort log with ≥ 40 evidenced hours (individual gate).
- Scoring: category E (AI-assisted engineering) = **10** Team Score points; individual component I4 (journal and reflection) = **10** Individual points.

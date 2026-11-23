---
name: incident-postmortem
description: "Use when: documenting a real build, deployment, security, data, availability, or operational incident with a blameless evidence-based timeline and corrective actions."
argument-hint: "Incident link, time window, and affected environment"
user-invocable: true
disable-model-invocation: false
---

# Incident Post-mortem

Document a genuine incident without fabricating events, causes, impact, or evidence.

## Safeguards

- Use only verified timestamps, logs, alerts, commits, deployments and participant statements.
- Mark gaps as `Unknown`.
- Never include secrets, raw personal data, tokens, or unnecessarily identifying information.
- Keep analysis blameless and distinguish trigger, contributing factors and root cause.
- Do not claim resolution or prevention until verified.

## Procedure

1. Confirm this was a real incident and identify scope, environment and evidence sources.
2. Preserve relevant evidence links and redact sensitive content.
3. Build a timestamped factual timeline.
4. Record:
   - user/business impact;
   - detection method;
   - response and recovery;
   - trigger;
   - root cause;
   - contributing technical/process factors;
   - what worked and failed.
5. Map violated or exposed requirements.
6. Define corrective/preventive actions with priority, owner, due date and verification.
7. Obtain participant confirmation for disputed or subjective statements.
8. Draft the post-mortem and request review before repository writes.
9. Track actions as work items and verify closure evidence.

## Output

Return:

- incident summary and impact;
- evidence-backed timeline;
- detection/response/recovery analysis;
- root cause and contributing factors;
- requirement/control mapping;
- lessons;
- corrective actions with owners/dates;
- unresolved questions and verification plan.

# Capstone specification provenance

## Authority

The content under `docs/capstone-spec/` is the canonical working specification for day-to-day engineering in this repository.

The official DevAcademy capstone requirements remain the ultimate authority. If the working specification conflicts with the official source, the official source wins and this pack must be corrected.

## Official source

- **Document:** DevAcademy 2026-2027 Capstone Requirements
- **Version:** 1.4
- **Date:** 2026-11-02
- **Status:** Latest official source confirmed by the team
- **Repository inclusion:** The derived pack is approved for this private team repository

The official source itself is not replaced by this derived pack.

## Derived pack

- **Original author:** Petar Ivanov
- **Original pack version:** 0.1.1
- **Original pack date:** 2026-11-06
- **Nature:** AI-ready, paraphrased, structured derivative of the official requirements
- **Initial validation:** 234 expected requirement rows; validator passed on 2026-11-23

## Repository adaptations

The imported repository snapshot differs from the original standalone pack only in surrounding guidance and integration material:

- all 234 requirement rows are preserved exactly;
- live team decisions moved to `docs/team/decision-register.md`;
- stale team-status snapshots were removed;
- personal email addresses were removed while necessary names and roles were retained;
- duplicate pack templates were omitted in favor of canonical repository templates;
- the unused effort CSV template was omitted while all allowed requirement options were preserved;
- unsupported Scout references and standalone pack instructions were removed;
- `requirements.csv` was retained as the static machine-readable index;
- `CAPSTONE-FULL.md` and pack-generation tooling were omitted.

## Maintenance rules

1. Keep requirement levels distinct: MUST, SHOULD, and MAY.
2. Keep pack-authored commentary visibly separate from official requirements.
3. Do not silently convert recommendations or team proposals into requirements.
4. Record team decisions in the repository's team-governance documents rather than rewriting the official requirement meaning.
5. Treat the imported v1.4 pack as an immutable requirements snapshot.
6. Do not edit requirement wording as part of ordinary feature work.
7. Reconcile every newer official requirements version through a dedicated, reviewed resynchronization task.
8. Preserve attribution and record material AI assistance used during any resynchronization.
9. Keep `requirements.csv` as the static machine-readable index generated from this validated snapshot.

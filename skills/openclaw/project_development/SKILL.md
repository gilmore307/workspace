---
name: project_development
description: Steward an OpenClaw-managed software project end to end: project shape, docs spine, Codex dispatch and review, maintenance, and trading-manager registry naming discipline. Use for creating, restructuring, implementing, documenting, or reviewing a project when OpenClaw owns the development boundary.
---

# Project Development

Use this skill when OpenClaw is the steward of an active software project.

## Core rule

OpenClaw owns shape, naming, docs, dispatch, review, acceptance, and maintenance.
Codex implements bounded tasks inside that boundary.

## Engineering doctrine

Apply these principles across planning, docs, dispatch, review, and maintenance:

- Structure before implementation.
- Boundaries before wiring.
- Small coherent change before broad refactor.
- Clarity before cleverness.
- Root cause before patch.
- Explicit contracts before hidden behavior.
- Tests follow behavior.
- Remove stale implementation.
- Acceptance over aesthetic polish.

## Required behavior

- Shape the repository before broad implementation.
- Keep docs, directory, and maintained-file boundaries authoritative.
- Give each maintained file a clear ownership role and reduce overlap instead of letting neighboring files become interchangeable.
- Define durable data ownership, migration responsibility, backup/restore expectations, and retention tradeoffs before implementation touches databases or high-volume storage.
- Dispatch Codex work at medium task granularity.
- Review completion receipts before acceptance.
- Keep naming aligned with `trading-manager/scripts/registry/`.
- For registry entry changes, use SQL migrations under `trading-manager/scripts/registry/sql/schema_migrations/` and regenerate `trading-manager/scripts/registry/current.csv`.
- Keep code layout terms sharp across repositories: `src/` owns importable/reusable implementation code; `scripts/` owns executable maintenance or operational entrypoints that may call `src/`; `src/` must not depend on `scripts/`; avoid `source/` directories because `source` is reserved for provider/data-source meaning.
- Reuse the default registry-registered status vocabularies unless the project docs explicitly override them.
- Treat maintenance as real stewardship, not optional polish.

## Directory and entrypoint rule

- Use `src/` for implementation packages, reusable modules, connectors, validators, normalizers, and pipeline logic.
- Use `scripts/` only for executable wrappers, one-off maintenance commands, smoke runners, migrations, or operational entrypoints.
- `scripts/` may import `src/`; `src/` should not import `scripts/`.
- Registry `kind=script` should name stable callable commands/entrypoints, not ordinary source files or implementation directories.
- Use `implementation_path`, `source_file`, or `source_dir` for code locations; use `provider` or `data_source` for external data origins.

## Docs numbering rule

Use the same docs-spine number ranges across OpenClaw-managed trading repositories unless a repository explicitly documents a narrower local exception:

- `README.md` remains unnumbered and is the entry/index for the repository.
- `docs/README.md` is optional; use it only as a docs-local index when the docs directory is large.
- `docs/00_*` through `docs/69_*` are the normal current docs spine, ordered from foundational context to operating details. Keep them in reading order and avoid gaps unless a near-term planned file is explicitly reserved.
- `docs/70_*` through `docs/79_*` are reserved for optional reference material that is current but not part of the primary reading path.
- `docs/80_task.md`, `docs/81_decision.md`, and `docs/82_memory.md` are fixed ledger files. Use the `80_*` range for task/decision/memory/governance ledgers because they should sort after the current docs spine and stay stable across reorganizations.
- `docs/90_*` through `docs/99_*` are reserved for appendices, compatibility notes, audits, or historical reference that must remain visible but should not be read as the normal current path.
- Do not use `docs/100_*` or higher for active docs. If the docs set grows that large, merge/split/reorder the spine instead of extending past `99`.
- When a docs file is renamed and registry rows point to it, add a `trading-manager/scripts/registry/sql/schema_migrations/` migration and regenerate `scripts/registry/current.csv`.
- Keep shared docs-numbering rules here, in this skill. Repository README/docs may list that repository's current docs spine, but they should not duplicate the shared numbering policy text.

## Ownership rule

- `README.md` files, docs-spine files, acceptance receipts, naming registration, and post-acceptance commits belong to OpenClaw by default.
- Codex should touch those surfaces only when the task explicitly delegates that exception.

## Resources

- `references/skill-map.md`
- `references/status-vocabularies.md`
- `references/data-structure.md`
- `references/`
- `templates/`

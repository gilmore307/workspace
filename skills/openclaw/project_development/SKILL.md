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

## Ownership rule

- `README.md` files, docs-spine files, acceptance receipts, naming registration, and post-acceptance commits belong to OpenClaw by default.
- Codex should touch those surfaces only when the task explicitly delegates that exception.

## Resources

- `references/skill-map.md`
- `references/status-vocabularies.md`
- `references/data-structure.md`
- `references/`
- `templates/`

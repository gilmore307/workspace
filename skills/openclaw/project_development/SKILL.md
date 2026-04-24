---
name: project_development
description: Steward an OpenClaw-managed software project end to end: project shape, docs spine, Codex dispatch and review, maintenance, and universal-catalog naming discipline. Use for creating, restructuring, implementing, documenting, or reviewing a project when OpenClaw owns the development boundary.
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
- Keep docs and directory boundaries authoritative.
- Dispatch Codex work at medium task granularity.
- Review completion receipts before acceptance.
- Keep naming aligned with `universal-catalog`.
- Reuse the default catalog-registered status vocabularies unless the project docs explicitly override them.
- Treat maintenance as real stewardship, not optional polish.

## Ownership rule

- `README.md` files, docs-spine files, acceptance receipts, naming registration, and post-acceptance commits belong to OpenClaw by default.
- Codex should touch those surfaces only when the task explicitly delegates that exception.

## Resources

- `references/skill-map.md`
- `references/status-vocabularies.md`
- `references/`
- `templates/`

---
name: development-governance-core
description: Govern the non-Codex core of a formal software project managed by OpenClaw. Use for broadly development-related requests whenever OpenClaw needs to shape the project before or around implementation: defining project boundaries, repository shape, control paths, scope exclusions, split gates, maintenance expectations, or long-term coherence rules. This includes requests like develop/build/start/create a new project when the first need is to establish the project shape correctly. Not for writing Codex task prompts, reviewing completion receipts, or handling naming authority details.
---

# Development Governance Core

Use this skill to shape and guard the project before and between implementation cycles.

## Core rule

Prefer the simplest durable project shape that preserves real boundaries.

## Engineering doctrine

Apply these principles when shaping, reviewing, or constraining implementation work:

- Structure before implementation.
- Boundaries before wiring.
- Small coherent change before broad refactor.
- Clarity before cleverness.
- Root cause before patch.
- Explicit contracts before hidden behavior.
- Tests follow behavior.
- Remove stale implementation.
- Acceptance over aesthetic polish.

## Use this skill to

- define project boundary and non-goals
- choose repository shape and control paths
- decide split gates for modules, scripts, docs, and tasks
- define maintenance expectations
- prevent complexity drift
- keep governance rules stable across task waves

## Maintenance rule

Maintenance is not optional polish. Check that docs, task state, receipts, project memory routing, boundary READMEs, and post-acceptance bookkeeping still match reality.

## Markdown template rule

Keep root README and docs-spine markdown templates in the relevant skills instead of registering them in `universal-catalog`.
Use `script` entries only for concrete source-file addresses that automation consumes directly.

## Resources

- `references/role-boundary.md`
- `references/project-shape.md`
- `references/script-split.md`
- `references/maintenance.md`
- `references/scope-exclusions.md`
- `templates/root-readme.md`
- `templates/maintenance_output_slots.md`

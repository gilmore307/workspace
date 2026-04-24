---
name: development-governance-core
description: Govern the non-Codex core of a formal software project managed by OpenClaw. Use when defining project boundaries, repository shape, control paths, scope exclusions, split gates, maintenance expectations, or long-term coherence rules. Not for writing Codex task prompts, reviewing completion receipts, or handling naming authority details.
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

## Resources

- `references/00_role_boundary.md`
- `references/02_project_shape.md`
- `references/08_script_split.md`
- `references/09_maintenance.md`
- `references/10_scope_exclusions.md`
- `templates/OPENCLAW.md`
- `templates/maintenance_output_slots.md`

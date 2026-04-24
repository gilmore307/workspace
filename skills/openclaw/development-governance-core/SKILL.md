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

## Canonical template rule

When `universal-catalog` governs fixed-location repository docs, prefer the canonical root README and docs-spine template files registered there instead of letting local copies drift.
When automation needs the full file address for one of those canonical templates, prefer the matching registered `script` entry instead of hardcoding the raw path.

## Resources

- `references/role-boundary.md`
- `references/project-shape.md`
- `references/script-split.md`
- `references/maintenance.md`
- `references/scope-exclusions.md`
- `templates/root-readme.md`
- `templates/maintenance_output_slots.md`

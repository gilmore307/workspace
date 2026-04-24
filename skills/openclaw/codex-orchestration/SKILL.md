---
name: codex-orchestration
description: Orchestrate bounded Codex implementation work inside an OpenClaw-managed software project. Use when sizing medium-granularity tasks, preparing execution keys, writing Codex task prompts, checking completion receipts, performing acceptance review, rejecting or accepting work, or handling post-acceptance commit and push responsibility. Not for defining the overall project docs spine or owning the universal catalog.
---

# Codex Orchestration

Use this skill whenever OpenClaw hands work to Codex or reviews work returned by Codex.

## Core rule

OpenClaw plans and accepts. Codex implements and reports.

## Engineering doctrine

Use these principles when dispatching, reviewing, and accepting Codex work:

- Structure before implementation.
- Boundaries before wiring.
- Small coherent change before broad refactor.
- Clarity before cleverness.
- Root cause before patch.
- Explicit contracts before hidden behavior.
- Tests follow behavior.
- Remove stale implementation.
- Acceptance over aesthetic polish.

## Task granularity rule

Prefer tasks in the middle band:

- large enough to complete one coherent acceptance path efficiently
- small enough to keep scope control, review quality, and rollback understandable

Avoid:

- micro-tasks that create handoff overhead without reducing real risk
- broad sweeps that cross too many boundaries for one clean review

## Review rule

Passing tests is not final acceptance. OpenClaw must check scope, evidence, changed paths, acceptance criteria, and documentation impact.

## Naming authority rule

- Before dispatching work that requires naming, OpenClaw should check `universal-catalog` first.
- Codex should reuse approved names instead of improvising fresh permanent vocabulary.
- If no approved name exists, OpenClaw should treat that as catalog work or authorize only a temporary implementation name.
- If Codex introduces a temporary name anyway, Codex must report it explicitly in the completion receipt for OpenClaw review and registration.

## Docs ownership rule

- During normal implementation tasks, Codex should not edit `README.md`, the project docs spine, or other governance docs unless the task explicitly authorizes that exception.
- If accepted code work requires documentation updates, OpenClaw performs those updates after acceptance by default.

## Post-acceptance rule

If the task is accepted, OpenClaw is responsible for creating the commit and pushing the accepted change set to GitHub unless explicitly told otherwise.

## Resources

- `references/04_task_model.md`
- `references/05_codex_dispatch.md`
- `references/06_completion_review_acceptance.md`
- `templates/`

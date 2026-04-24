---
name: project-docs-spine
description: Define and maintain the formal documentation spine for an OpenClaw-managed software repository. Use when creating or updating docs/00_scope.md through docs/05_decision.md, deciding whether docs/06_memory.md is needed, structuring workflow-linked acceptance docs, routing project-local memory, or writing README boundaries for maintained directories. Not for dispatching Codex tasks or final acceptance review.
---

# Project Docs Spine

Use this skill to keep project documentation structured, authoritative, and easy to review.

## Core rule

Project facts live in project docs, not in chat.

## Engineering doctrine

Reflect these principles in project docs and structure decisions:

- Structure before implementation.
- Boundaries before wiring.
- Small coherent change before broad refactor.
- Clarity before cleverness.
- Root cause before patch.
- Explicit contracts before hidden behavior.
- Tests follow behavior.
- Remove stale implementation.
- Acceptance over aesthetic polish.

## Workflow and acceptance rule

- Each workflow in `docs/02_workflow.md` should carry its own acceptance standard.
- `docs/03_acceptance.md` should consolidate those standards into a reviewable acceptance surface.

## Ownership rule

- `README.md` files and routine post-acceptance project docs updates belong to OpenClaw by default.
- Codex should only touch these docs when there is an explicit doc-only delegation exception.

## Canonical template rule

When `universal-catalog` governs fixed-location repository docs, prefer the canonical file-level template items there instead of letting local skill copies drift.
When scripts need the direct file locator for one of those canonical templates, prefer the matching registered `script` entry with the full address instead of hardcoding raw paths.

## Directory README rule

Each meaningful maintained directory should have a `README.md` that explains:

- the directory boundary
- the purpose of key files
- the purpose of important subdirectories
- what does not belong there when confusion is likely

Do not require this for generated, vendor, cache, build-artifact, or other disposable directories unless there is a specific reason.

Use diagrams and tables freely when they make project structure or workflow clearer.

## Resources

- `references/project-docs.md`
- `references/project-memory.md`
- `templates/`

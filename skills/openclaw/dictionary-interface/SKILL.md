---
name: dictionary-interface
description: Interface project governance and task artifacts with the universal-catalog project. Use when deciding how naming discipline affects tasks, receipts, fields, status values, file-name tokens, repository names, shared paths, or shared config keys; when temporary local names are needed before universal-catalog is ready; or when naming drift must be surfaced without redesigning the whole project. Not for owning the universal catalog itself.
---

# Dictionary Interface

Use this skill to manage the boundary between current project work and the `universal-catalog` authority.

## Core rule

This skill governs the interface to naming authority, not the naming authority itself.

## Naming control rule

- OpenClaw should look up formal names in `universal-catalog` before dispatching Codex work that needs naming.
- If an approved name exists, reuse it.
- If no approved name exists, OpenClaw should add or queue a catalog update instead of letting Codex silently mint permanent vocabulary.
- Codex may use a temporary new name only when blocked otherwise, and must report that name back for OpenClaw review and registration.

## Engineering doctrine

Apply these principles when naming decisions affect implementation and review:

- Structure before implementation.
- Boundaries before wiring.
- Small coherent change before broad refactor.
- Clarity before cleverness.
- Root cause before patch.
- Explicit contracts before hidden behavior.
- Tests follow behavior.
- Remove stale implementation.
- Acceptance over aesthetic polish.

## Fallback rule

If `universal-catalog` is not ready yet:

- use explicit project-local names
- record that they are temporary
- keep the later alignment point visible in docs or decisions
- keep Codex from treating those temporary names as self-approved standards

## Resources

- `references/03_dictionary_interface.md`
- `templates/`

---
name: dictionary-interface
description: Interface project governance and task artifacts with the future universal-dictionary project. Use when deciding how naming discipline affects tasks, receipts, fields, status values, or file-name tokens; when temporary local names are needed before universal-dictionary is ready; or when naming drift must be surfaced without redesigning the whole project. Not for owning the universal dictionary itself.
---

# Dictionary Interface

Use this skill to manage the boundary between current project work and the future `universal-dictionary` authority.

## Core rule

This skill governs the interface to naming authority, not the naming authority itself.

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

If `universal-dictionary` is not ready yet:

- use explicit project-local names
- record that they are temporary
- keep the later alignment point visible in docs or decisions

## Resources

- `references/03_dictionary_interface.md`
- `templates/`

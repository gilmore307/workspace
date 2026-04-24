---
name: codex-dictionary-guard
description: Guard names, fields, statuses, and schema interfaces when Codex works in a project that will later align with universal-dictionary. Use when Codex must avoid naming drift, preserve temporary local names, or surface missing naming authority instead of improvising new formal terms. Not for defining the universal dictionary itself.
---

# Codex Dictionary Guard

Use this skill when naming discipline matters and the universal dictionary is incomplete or external.

## Core rule

Do not invent formal names just because a gap exists.

## Engineering doctrine

Apply these principles when naming choices interact with implementation:

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

- Reuse existing formal names when they already exist.
- Keep temporary project-local names explicit when the dictionary is not ready.
- Surface missing-name problems instead of improvising hidden schema changes.
- Keep fields, statuses, and file-name tokens stable inside the task boundary.
- Flag naming drift in the completion receipt when encountered.

## Do not do these

- Do not rename things for style.
- Do not create synonyms for variety.
- Do not silently replace temporary local names with new ones.
- Do not act like this skill owns the dictionary.

## Resources

- `references/03_dictionary_interface.md`
- `templates/`

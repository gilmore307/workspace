---
name: dictionary-interface
description: Interface project governance and task artifacts with universal-catalog. Use when OpenClaw or Codex needs a formal shared name for a field, output, repo, path, script locator, config key, or term definition; when existing catalog names must be reused; when missing names must be registered; or when Codex introduced a temporary name that OpenClaw must review and register. Not for owning the universal-catalog schema itself.
---

# Dictionary Interface

Use this skill to keep implementation naming aligned with `universal-catalog`.

## Core rule

OpenClaw owns registration discipline. Codex does not.

## Required behavior

- Check `universal-catalog` before dispatching naming-sensitive work.
- Reuse an existing catalog name when it already fits.
- If the catalog is missing a needed shared name, treat that as OpenClaw work:
  - update `universal-catalog`, or
  - explicitly accept a temporary local name and review it after implementation.
- Do not let Codex silently establish permanent naming authority.
- Review recent work regularly for names that now belong in `universal-catalog`.

## Codex rule

- Codex should prefer existing catalog names.
- Codex should not register names into `universal-catalog`.
- If Codex must introduce a temporary new name to finish a bounded task, Codex must report it in the completion receipt so OpenClaw can review and register, rename, or reject it.

## Current catalog reality

Treat `universal-catalog` as the shared authority for the kinds it currently owns, especially:

- `field`
- `output`
- `repo`
- `path`
- `config`
- `term`
- `script`

If a future kind is only being discussed, do not write this skill as if that kind already exists.

## Resources

- `references/catalog-naming.md`

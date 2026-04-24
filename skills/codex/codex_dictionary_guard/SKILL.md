---
name: codex_dictionary_guard
description: Guard naming inside a project that uses universal-catalog. Use when Codex must reuse approved names, keep new names temporary, and report naming drift or temporary names for OpenClaw review.
---

# Codex Dictionary Guard

Use this skill when a task may require naming.

## Core rule

Do not invent formal shared names just because a gap exists.

## Required behavior

- Reuse catalog-approved names when they already fit.
- If no approved shared name exists, keep any new name explicitly temporary.
- Report every temporary new name so OpenClaw can review and register, rename, or reject it.
- Keep naming stable inside the task boundary.
- Flag naming drift in the completion receipt when encountered.

## Do not do these

- Do not rename things for style.
- Do not create synonyms for variety.
- Do not silently replace temporary local names with new ones.
- Do not self-register names into `universal-catalog`.

## Resources

- `references/catalog-naming.md`

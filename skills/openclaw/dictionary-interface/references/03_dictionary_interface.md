# Dictionary Interface

OpenClaw owns naming discipline, but this skill does not own the fixed vocabulary.

The source of truth for formal words, field names, status names, file-name tokens, schema keys, and directory tokens is the separate `universal-dictionary` project.

## Core Principle

```text
Do not define fixed vocabulary inside this development skill.
Use the universal dictionary as the authority.
```

This skill may describe required information slots, but the exact field names should come from `universal-dictionary`.

Example distinction:

```text
This skill may require: a task identity slot.
The universal dictionary owns: the exact field name for that slot.
```

## When OpenClaw Names Anything

Before creating or accepting a formal name, OpenClaw should check the universal dictionary for:

- the approved term
- the approved field name
- the approved status value
- the approved file-name token
- any forbidden synonyms
- any project-specific override policy

If the dictionary does not yet contain the term, OpenClaw should not casually invent one. It should either:

1. create a dictionary update task, or
2. record a temporary local term with a decision and mark it for dictionary review.

## What This Skill Still Enforces

Even without owning the vocabulary, this skill enforces discipline:

- one concept should not acquire multiple names
- new terms should not be invented for variety
- formal fields should be stable
- Codex should not introduce naming drift
- ambiguous local names should be reviewed before acceptance
- generic folders or files should not become junk drawers

## Schema Templates

Templates in this skill are interface drafts, not vocabulary authority.

When a template contains concrete keys, treat them as provisional names that must be synchronized with `universal-dictionary` before formal use.

If `universal-dictionary` uses a different approved key, prefer the dictionary and update the local template or adapter.

## Dictionary Drift

Dictionary drift happens when:

- Codex introduces an unregistered field
- two files use different names for the same concept
- a project-specific synonym becomes permanent without review
- a template diverges from `universal-dictionary`
- task receipts use a field not registered in the dictionary

Dictionary drift is an acceptance concern. OpenClaw may reject or revise Codex output when naming drift affects maintainability or formal interfaces.

## Local Exceptions

A project may use a local term when:

- the concept is truly project-specific
- the universal dictionary does not yet cover it
- the term is documented in project docs
- the exception is recorded in `docs/05_decision.md`
- a follow-up dictionary task is created when the term should become universal

## Review Checklist

Before accepting Codex output, check:

- Are new formal fields registered or marked for dictionary review?
- Did Codex introduce a synonym for an existing concept?
- Did filenames, directories, JSON keys, CSV columns, and docs use the same term for the same concept?
- Did Codex create generic folders without a project decision?
- Do task package and receipt schemas still match the dictionary-approved interface?

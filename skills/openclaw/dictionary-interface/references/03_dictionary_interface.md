# Dictionary Interface

OpenClaw owns naming discipline, but this skill does not own the fixed vocabulary.

The source of truth for formal words, field names, status names, file-name tokens, schema keys, repository names, shared path tokens, and shared config keys is the separate `universal-catalog` project.

## Core Principle

```text
Do not define fixed vocabulary inside this development skill.
Use the universal catalog as the authority.
```

This skill may describe required information slots, but the exact field names should come from `universal-catalog`.

Example distinction:

```text
This skill may require: a task identity slot.
The universal catalog owns: the exact field name for that slot.
```

## When OpenClaw Names Anything

Before creating or accepting a formal name, OpenClaw should check the universal catalog for:

- the approved term
- the approved field name
- the approved status value
- the approved file-name token
- any forbidden synonyms
- any project-specific override policy

If the catalog does not yet contain the term, OpenClaw should not casually invent one. It should either:

1. create a catalog update task, or
2. record a temporary local term with a decision and mark it for catalog review.

Codex should not register names directly into `universal-catalog`. If Codex must introduce a temporary new name to complete bounded implementation work, Codex must report:

- the proposed name
- where it was introduced
- why the existing catalog did not fit
- whether the name should be registered, renamed, or rejected

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

When a template contains concrete keys, treat them as provisional names that must be synchronized with `universal-catalog` before formal use.

If `universal-catalog` uses a different approved key, prefer the catalog and update the local template or adapter.

## Dictionary Drift

Dictionary drift happens when:

- Codex introduces an unregistered field
- two files use different names for the same concept
- a project-specific synonym becomes permanent without review
- a template diverges from `universal-catalog`
- task receipts use a field not registered in the catalog

Name drift also happens when Codex invents a permanent-looking name without reporting it back for OpenClaw registration review.

Dictionary drift is an acceptance concern. OpenClaw may reject or revise Codex output when naming drift affects maintainability or formal interfaces.

## Local Exceptions

A project may use a local term when:

- the concept is truly project-specific
- the universal catalog does not yet cover it
- the term is documented in project docs
- the exception is recorded in `docs/05_decision.md`
- a follow-up catalog task is created when the term should become universal

## Review Checklist

Before accepting Codex output, check:

- Are new formal fields registered or marked for catalog review?
- Did Codex introduce a synonym for an existing concept?
- Did filenames, directories, JSON keys, CSV columns, and docs use the same term for the same concept?
- Did Codex report every temporary new name it introduced during implementation?
- Did Codex create generic folders without a project decision?
- Do task package and receipt schemas still match the catalog-approved interface?

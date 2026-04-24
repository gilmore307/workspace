# Memory Promotion

## Promote only when the destination will remain authoritative later

Promotion is not about making a fact feel important. It is about moving a fact into the one place that should own it.

## Promotion patterns

### Daily memory -> USER.md

Promote when the note reveals a stable personal preference.

Examples:

- prefers chart-heavy visualization for runtime surfaces
- prefers concise progress updates
- wants stronger pushback on vague or rushed instructions

### Daily memory -> TOOLS.md

Promote when the note reveals a host-specific operational fact.

Examples:

- a secret alias flow
- a local hostname or SSH alias
- a device nickname or path convention

### Daily memory -> AGENTS.md

Promote when the note reveals a durable operating rule future sessions should inherit.

Examples:

- commit and push after file-editing tasks unless explicitly told otherwise
- default to reading a specific skill for development stewardship
- stable rules for where bottom-layer preferences should live

### Daily memory -> MEMORY.md

Promote when the note is:

- broader than one repo
- broader than one day
- likely to matter in later private sessions
- not better owned by `USER.md`, `TOOLS.md`, `AGENTS.md`, or project docs

### Daily memory -> project docs

Promote when the note is actually a project fact.

Examples:

- project runtime boundary
- accepted contract or schema
- project decision or acceptance rule

## Demotion and cleanup

If a fact was written into the wrong place:

1. move or restate it in the correct canonical home
2. check whether the old copy should remain as short-lived context or be removed as redundant drift
3. avoid preserving the same durable fact across multiple canonical files without a real reason

## Promotion anti-patterns

Do not:

- promote every raw event into long-term memory
- keep stable preferences only in daily memory
- treat `MEMORY.md` as the fallback for anything important
- copy one project's internal state into global memory when project docs own it

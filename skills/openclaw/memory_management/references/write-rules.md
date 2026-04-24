# Memory Write Rules

## Canonical-home rule

Before writing, decide whether the fact belongs in project docs, `USER.md`, `TOOLS.md`, `AGENTS.md`, `MEMORY.md`, `memory/HANDOFF.md`, or the daily memory file.

Do not write first and classify later unless the user explicitly wants a raw checkpoint.

## Daily memory rules

- Use the canonical filename `memory/YYYY-MM-DD.md`.
- Append new entries instead of creating timestamped variants.
- Do not create `memory/YYYY-MM-DD-HHMM.md`-style files.
- Keep daily memory as a log, not as the canonical home for stable rules or preferences.

## Flush rules

When a pre-compaction or end-of-turn memory flush gives special constraints, follow them literally.

Common constraints include:

- append to the existing canonical daily file if it already exists
- do not overwrite the daily file during append-only flushes
- do not create alternate timestamped files
- treat named bootstrap/reference files as read-only when instructed
- write nothing if there is no durable memory to preserve

## Deduplication rule

If the same durable fact exists in both a canonical home and daily memory, prefer keeping the canonical copy.

When safe and appropriate:

1. promote the fact into the real home
2. remove or avoid redundant long-term duplication in daily memory
3. keep only the short-lived daily context that still helps reconstruct the day

## Edit discipline

- Make the smallest targeted change that preserves the file's role.
- Do not rewrite an entire canonical file to add one fact unless there is no safer edit path.
- Preserve headings and surrounding structure.
- Avoid accidental duplication when appending or replaying memory flushes.

## Privacy and scope

- Do not move secrets into memory files.
- Do not place private long-term memory into shared or group contexts.
- Do not promote project-local facts into global memory unless cross-project recall is actually needed.

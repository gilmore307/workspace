---
name: memory_management
description: Route, promote, deduplicate, and flush workspace memory into the correct canonical home. Use when deciding where information should live across project docs, USER.md, TOOLS.md, AGENTS.md, MEMORY.md, memory/HANDOFF.md, and memory/YYYY-MM-DD.md; when handling memory flushes; or when correcting misplaced durable memory.
---

# Memory Management

Use this skill to keep memory precise, canonical, and non-duplicative.

## Core rule

Choose the narrowest authoritative home that will still be true later.
Do not default to daily memory when a more canonical file exists.

## Required behavior

- Route project-specific facts into project docs before considering global memory.
- Put stable user preferences in `USER.md`.
- Put host- and environment-specific operational notes in `TOOLS.md`.
- Put workspace-wide durable operating rules in `AGENTS.md`.
- Put curated long-term continuity in `MEMORY.md` only in the main private session.
- Put active next-step continuity in `memory/HANDOFF.md`.
- Put same-day trace notes in `memory/YYYY-MM-DD.md`.
- Keep one fact in one canonical home whenever possible.
- When a fact is promoted into its real home, avoid leaving redundant long-term copies behind in daily memory.

## Default workflow

1. Classify the information by scope and durability.
2. Identify the canonical home.
3. Check whether the fact already exists there.
4. Write the smallest durable update that preserves the rule of one canonical home.
5. If the write is part of a flush, follow the append/readonly rules exactly.

## Hard boundaries

- Do not treat `memory/YYYY-MM-DD.md` as the canonical home for stable user preferences, tool notes, or workspace rules.
- Do not turn `MEMORY.md` into a project dump.
- Do not mirror one project's durable facts into global memory when project docs are the real authority.
- Do not create timestamped variants of a canonical daily memory file.
- Do not overwrite bootstrap/reference files during restricted flushes when the instruction says they are read-only.

## Resources

- `references/skill-map.md`
- `references/routing.md`
- `references/write-rules.md`
- `references/promotion.md`

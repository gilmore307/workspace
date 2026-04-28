---
name: memory_management
description: Route, promote, deduplicate, flush workspace memory, and manually clean expired memory-core dreaming narrative sessions. Use when deciding where information should live across project docs, USER.md, TOOLS.md, AGENTS.md, MEMORY.md, memory/HANDOFF.md, and memory/YYYY-MM-DD.md; when handling memory flushes; when correcting misplaced durable memory; or when inspecting/removing expired dreaming-narrative sessions.
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
- When explicitly asked, inspect and remove expired `dreaming-narrative-*` sessions with archive-first cleanup; runtime should also self-clean transient narrative sessions at run end.

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
- Do not remove ordinary user/project/chat sessions through the dreaming cleanup path.

## Resources

- `references/skill-map.md`
- `references/routing.md`
- `references/write-rules.md`
- `references/promotion.md`
- `references/dreaming-cleanup.md`
- `scripts/cleanup_expired_dreaming_sessions.py`

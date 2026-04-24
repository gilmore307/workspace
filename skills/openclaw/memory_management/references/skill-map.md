# Skill Map

Use the smallest relevant reference set instead of loading everything.

## 1. Choose the destination

Read `references/routing.md` when the main question is where a fact should live.

Examples:

- "remember this preference"
- "where should this go"
- "should this be in USER.md or AGENTS.md"
- "does this belong in project docs or MEMORY.md"

## 2. Perform the write safely

Read `references/write-rules.md` when the destination is known and the main question is how to write without creating drift.

Examples:

- daily memory append rules
- pre-compaction flush handling
- readonly-memory constraints
- deduplicating an already-written fact

## 3. Promote or demote memory

Read `references/promotion.md` when information already exists in the wrong place and must be moved, distilled, or cleaned up.

Examples:

- moving a stable preference from daily memory into `USER.md`
- promoting a durable operating rule into `AGENTS.md`
- deciding whether a fact deserves `MEMORY.md`
- removing redundant daily-memory copies after promotion

## 4. Clean expired dreaming narrative sessions

Read `references/dreaming-cleanup.md` when the user asks about expired or inactive `dreaming-narrative-*` sessions.

Examples:

- "how many dreaming sessions are stale"
- "remove expired dreaming sessions"
- "why didn't dreaming cleanup delete completed narrative sessions"
- "archive old memory-core dreaming sessions"

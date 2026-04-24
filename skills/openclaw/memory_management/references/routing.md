# Memory Routing

## Destination order

Choose the narrowest authoritative home that will still be true later.
Each memory file should own a distinct class of information instead of overlapping loosely with neighboring files.

1. Project docs
2. `USER.md`
3. `TOOLS.md`
4. `AGENTS.md`
5. `MEMORY.md`
6. `memory/HANDOFF.md`
7. `memory/YYYY-MM-DD.md`

## Routing matrix

### Project docs

Use for:

- project purpose and scope
- repository boundaries
- workflow and acceptance rules that belong to one repo
- project-specific decisions
- project-local durable memory

Do not mirror these into global memory unless the user explicitly wants cross-project recall.

### USER.md

Use for:

- stable communication preferences
- visualization and presentation preferences
- naming/address preferences
- recurring workflow preferences tied to the user

Example:

- prefers chart-heavy visual presentation for status and bandwidth surfaces

### TOOLS.md

Use for:

- local aliases
- device nicknames
- secret-location rules
- host-specific operational notes
- environment-specific helper usage

Store locations and usage rules, not live secret values.

### AGENTS.md

Use for:

- workspace-wide operating defaults
- durable behavior rules for future sessions
- routing or process rules that are not merely personal preference

### MEMORY.md

Use for:

- curated long-term continuity
- important cross-session context still likely to matter later
- durable personal or work context that is broader than one project and one day

Keep it sparse.

### memory/HANDOFF.md

Use for:

- active next steps
- current blockers
- short-horizon owner context
- temporary continuity needed for resumption

### memory/YYYY-MM-DD.md

Use for:

- same-day checkpoints
- short-lived logs
- activity trace pending later promotion

Do not use daily memory as the canonical home for stable preferences, tool notes, or workspace rules.

## Canonical ownership standard

Use this standard whenever routing feels ambiguous:

- `USER.md` owns stable human preferences.
- `TOOLS.md` owns host-specific operational notes.
- `AGENTS.md` owns durable workspace rules.
- `MEMORY.md` owns sparse cross-session continuity.
- `memory/HANDOFF.md` owns active resumption context.
- `memory/YYYY-MM-DD.md` owns same-day trace notes.

If a note does not clearly fit one of these homes, narrow the wording or move it to the more authoritative adjacent file instead of creating overlap.

## Non-homes

These are not the default canonical home for new durable memory writes:

- `DREAMS.md`
- `memory/.dreams/`
- `memory/dreaming/`

Treat them as system-managed artifacts unless the user explicitly asks for direct intervention.

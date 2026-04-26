# Project Docs

Project docs are OpenClaw's stable workbench for each formal repository.

## Required docs spine

Every formal repository should have:

```text
docs/
  00_scope.md
  01_context.md
  02_workflow.md
  03_acceptance.md
  04_task.md
  05_decision.md
```

Optional:

```text
docs/06_memory.md
```

Do not extend the default docs spine with reusable template material or registry source-of-truth files. If a file is a reusable drafting surface, route it to `templates/`. If a file defines registered vocabulary or kind boundaries, route it to the project registry.

Project-specific exception: `trading-main` may include `docs/07_helpers.md`, `docs/08_registry.md`, and `docs/09_templates.md` as platform-function guides because that repository owns shared helpers, the active SQL-backed trading registry, and reusable trading templates. This does not move helper code, registry kind definitions, concrete registry entries, or template drafts into docs.

Keep markdown templates for these fixed-location files in this skill rather than registering them in `trading-main/registry/`.
If automation needs a concrete source-file locator, use `script` entries for actual source files, not markdown doc templates.

## Core boundary rule

Each durable fact should have one canonical home.
Do not make multiple docs agree by copy-pasting the same prose.
If two docs need the same fact:

- keep the full statement in the narrower home
- mention or link to it from the other doc
- remove stale duplicate wording

If something is not settled yet, mark it as an explicit open gap instead of filling multiple docs with speculative structure.

Use an open gap marker as an active work signal, not as a parked conclusion.
It records that the project has reached a slot that still needs a real definition.
Once dispatch, implementation, review, or acceptance depends on that slot, come back and replace the gap marker with current reality.

## Boundary map

### 00_scope.md

Owns:

- what the project does
- what the project does not do
- current boundary
- owner intent
- non-goals
- out-of-scope signals

Does not own:

- project history or rationale beyond concise owner intent
- dependencies or environment assumptions
- workflow steps
- acceptance commands
- current task state
- decision records

### 01_context.md

Owns:

- why the project exists
- related systems
- environment assumptions
- dependencies
- external tools
- users or consumers
- integration points
- important constraints

Does not own:

- in-scope / out-of-scope lists
- current workflow sequencing
- acceptance gates
- current task board state
- ratified decision records

### 02_workflow.md

Owns:

- how the project operates
- ordered runtime layers, functions, or workflows when those are real
- triggers
- actors and ownership boundaries
- outputs produced by each workflow/function
- where OpenClaw participates
- where Codex participates
- workflow-local handoff rules

Does not own:

- broad scope lists
- dependency cataloging
- the canonical acceptance checklist
- the current task register
- durable decision rationale

Use this file to describe runtime flow and ownership, not to restate everything the repo is about.
When a project has multiple runtime responsibilities, prefer an ordered function/layer model over loose narrative prose.
Once a project has entered real design, dispatch, or restructuring work, `02_workflow.md` should not remain a top-level shell of unresolved headings; define the runtime shape and route any still-open questions into explicit task/decision follow-up.
If a workflow needs acceptance notes, keep them short here and point to `03_acceptance.md` for the canonical gate.

### 03_acceptance.md

Required for every formal repository.

Owns:

- the consolidated acceptance view across workflows
- how tasks are accepted
- required verification commands
- required output checks
- required review evidence
- rejection conditions
- when a task can move to `accepted`

Does not own:

- project purpose
- dependency explanation
- current queue/dispatch state
- long decision history

Acceptance is numbered `03` because it must sit directly under workflow. A workflow without acceptance is not finishable.
`docs/02_workflow.md` may mention workflow-local checks, but `docs/03_acceptance.md` is the canonical acceptance surface.

### 04_task.md

Owns human-readable current task state.

Owns:

- active tasks
- queued or ready-to-dispatch tasks
- blocked tasks
- pending-acceptance tasks
- recently accepted tasks not yet closed
- next planned dispatch

Does not own:

- durable project rationale
- full workflow explanation
- canonical acceptance rules
- speculative future architecture

Structured task state may also live under a project-local register path such as `.openclaw/task/register/`.
If a project uses it, document the filenames and fields in project docs instead of pretending a shared schema already exists.

### 05_decision.md

Owns formal ratified project choices.

Owns:

- decision id
- decision date
- context
- chosen option
- rejected alternatives when they matter
- reason
- revisit condition

Does not own:

- current task board state
- general workflow narration
- dependency inventory
- unratified ideas presented as settled

Use this file when a choice changes project shape, architecture, dependency policy, naming convention, task model, or acceptance criteria.
If a choice is not ratified yet, keep it out of this file and track the open question in the relevant narrower doc or task register.

### 06_memory.md

Optional.

Use only for project-local durable continuity that does not fit scope, context, workflow, acceptance, task, or decision.

Examples:

- recurring project-specific caution
- local resumption notes useful across sessions
- project-specific maintenance observations
- stable but informal project knowledge

Do not use `docs/06_memory.md` as a dumping ground. Prefer the narrower docs when possible.

## Shared helper package discipline

When a repository contains shared helper code, distinguish code existence from package readiness.

If helper code exists without package metadata, version policy, runtime version, installation method, and import/call examples, document it as internal-only or not-yet-packaged. Do not let component repositories treat loose helper files as runtime dependencies.

Before cross-repository helper consumption, accept a language/distribution strategy such as Node package, Python package, CLI/internal maintenance tool, or another explicit contract.

For `trading-main`, the accepted runtime helper package strategy is Python: package metadata in root `pyproject.toml`, source under `helpers/python/`, import package `trading_registry`, and installation into the shared `.venv`. JavaScript helper files under `helpers/registry/` are internal maintenance/test code unless a future Node package decision changes that.

## Change discipline

When editing project docs:

- update the one canonical home first
- update neighboring docs only when their boundary truly changed
- prefer cross-reference over duplication
- remove stale text instead of letting overlap accumulate
- reject docs that blur scope, context, workflow, acceptance, task, and decision into interchangeable prose

## Directory README Rule

Each meaningful maintained directory should have a `README.md` describing its boundary and contents.

Prefer including:

- what belongs in the directory
- what its key files do
- what important subdirectories contain
- nearby boundaries that are easy to confuse

Do not require this for generated, vendor, cache, build, or other disposable directories unless the project has a specific reason.

Use diagrams and tables freely in docs when they clarify structure faster than prose.

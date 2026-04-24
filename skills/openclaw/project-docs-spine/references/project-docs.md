# Project Docs

Project docs are OpenClaw's stable workbench for each formal repository.

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

## 00_scope.md

Defines:

- what the project does
- what the project does not do
- current boundary
- project owner intent
- major non-goals
- when a request is out of scope

## 01_context.md

Defines:

- why the project exists
- dependencies
- related systems
- environment assumptions
- external tools
- users or consumers
- integration points

## 02_workflow.md

Defines:

- how the project operates
- major workflows
- workflow-specific acceptance sections
- human steps
- automated steps
- where OpenClaw participates
- where Codex participates
- what output is produced by each workflow

## 03_acceptance.md

Required for every formal repository.

Defines:

- the consolidated acceptance view across workflows
- how tasks are accepted
- required test commands
- required output checks
- rejection conditions
- when a task can move to `accepted`

Acceptance is numbered `03` because it must sit directly under workflow. A workflow without acceptance is not finishable. `docs/02_workflow.md` should carry per-workflow acceptance rules; `docs/03_acceptance.md` should consolidate them for review and dispatch.

## 04_task.md

Human-readable project task state.

Defines:

- active tasks
- queued tasks
- blocked tasks
- ready-for-acceptance tasks
- accepted tasks not yet closed
- next planned dispatch

Structured task state may also live under a project-local register path such as `.openclaw/task/register/`.

If a project uses it, document the filenames and fields in project docs instead of pretending a shared schema already exists.

## 05_decision.md

Defines formal project choices:

- decision id
- decision date
- context
- chosen option
- rejected alternatives
- reason
- revisit condition

Use this file when a choice changes project shape, architecture, dependency policy, naming convention, task model, or acceptance criteria.

## 06_memory.md

Optional.

Use only for project-local durable continuity that does not fit scope, context, workflow, acceptance, task, or decision.

Examples:

- recurring project-specific caution
- local resumption notes useful across sessions
- project-specific maintenance observations
- stable but informal project knowledge

Do not use `docs/06_memory.md` as a dumping ground. Prefer the narrower docs when possible.

## Directory README Rule

Each meaningful maintained directory should have a `README.md` describing its boundary and contents.

Prefer including:

- what belongs in the directory
- what its key files do
- what important subdirectories contain
- nearby boundaries that are easy to confuse

Do not require this for generated, vendor, cache, build, or other disposable directories unless the project has a specific reason.

Use diagrams and tables freely in docs when they clarify structure faster than prose.

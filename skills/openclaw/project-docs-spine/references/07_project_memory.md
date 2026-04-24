# Project Memory

Project memory lives with the project.

Do not put detailed project facts into global memory when they belong in the project's docs.

## Routing Rule

Choose the narrowest authoritative home that will still be true later.

For project-specific memory, that home is usually project docs.

## Project Memory Routing

| Memory type | Route |
|---|---|
| project purpose and boundary | `docs/00_scope.md` |
| project background, dependencies, external systems | `docs/01_context.md` |
| project process and task flow | `docs/02_workflow.md` |
| acceptance criteria and required checks | `docs/03_acceptance.md` |
| active work and task state | `docs/04_task.md` |
| formal choices and reasons | `docs/05_decision.md` |
| durable local continuity that fits nowhere else | optional `docs/06_memory.md` |

## Global Memory Is Not a Project Dump

Global `MEMORY.md` should hold cross-project continuity, such as:

- OpenClaw and Codex role split
- Owner's global governance preferences
- cross-project naming policy
- cross-project memory policy
- global operating principles

It should not hold:

- one project's current tasks
- one project's module details
- one project's acceptance rules
- one project's decision history
- one project's local implementation notes

## When To Create docs/06_memory.md

Create or update `docs/06_memory.md` only when the memory is:

- project-specific
- durable across sessions
- not merely task state
- not a formal decision
- not an acceptance rule
- not a workflow rule
- not cross-project enough for global memory
- useful for resuming this specific project later

## Examples

Promote to `docs/00_scope.md`:

```text
This project does not manage production deployment.
```

Promote to `docs/03_acceptance.md`:

```text
A task is not accepted until OpenClaw verifies the completion receipt and required test output.
```

Promote to `docs/05_decision.md`:

```text
The project will use local `.openclaw/task/` for task exchange artifacts instead of `storage/01_task/`.
```

Promote to `docs/06_memory.md`:

```text
This project has a recurring risk that Codex over-splits helpers during parser work; check split gates during acceptance.
```

Promote to global `MEMORY.md`:

```text
Owner wants OpenClaw to be strict, rational, meticulous, and not blindly agreeable.
```

## Daily Memory Interaction

Daily memory can capture raw events.
Promotion decides the stable home.

Repeated project-specific facts should be distilled into project docs, not copied into global memory.

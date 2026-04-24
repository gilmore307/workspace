# Project Name

Not yet defined.

Only keep sections that are already true for the repository.
If something is not settled yet, write `Not yet defined` instead of inventing details.

This repository is managed by OpenClaw.

OpenClaw plans, dispatches, reviews, accepts, and maintains.
Codex implements, tests, and returns completion receipts.

## Required Docs

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

## Role Boundary

OpenClaw owns:

- project route
- docs
- workflow
- acceptance
- task scheduling
- Codex dispatch
- completion receipt review
- acceptance receipt
- decision records
- project-local memory routing
- dictionary discipline
- split discipline
- maintenance

Codex owns:

- implementation
- local code changes
- debugging
- tests
- command execution
- completion receipt

## Acceptance Rule

Codex may report readiness for acceptance.

Only OpenClaw may produce the final acceptance outcome and close the task.

Passing tests is not final acceptance. OpenClaw must check acceptance criteria and write an acceptance receipt.

After acceptance, OpenClaw is responsible for committing and pushing the accepted change set to GitHub.

## Dictionary Rule

If this repository uses `universal-catalog` as the authority for formal naming, state that here.
If not yet formalized, write `Not yet defined`.

## Split Rule

Do not create extra scripts, modules, docs, workflows, or tasks unless one split gate is met:

1. Reused by multiple scripts or workflows.
2. A stable branch starts here.
3. A complete workflow ends here.
4. It is a clear side branch such as test, fixture, mock, or entry wrapper.
5. The file is already large enough to hurt understanding or modification.

## Directory README Rule

Each meaningful maintained directory should have a `README.md` describing boundary and contents.

Do not require this for generated, vendor, cache, build-artifact, or other disposable directories unless the project has a specific reason.

## Project Control Path

If this repository uses a project-local control path, document it here.
If not yet decided, write `Not yet defined`.

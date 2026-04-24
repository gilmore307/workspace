# <project-name>

Short project purpose here.

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

This repository uses `universal-catalog` as the authority for formal words, field names, status values, schema keys, file-name tokens, repository names, shared paths, shared config keys, and forbidden synonyms.

Do not introduce new formal names casually. If a new term is needed, record a project decision or create a catalog update task.

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

Default project-local task exchange path:

```text
.openclaw/task/
  register/
  execution_key/
  completion_receipt/
  acceptance_receipt/
  output/
```

This project may override the path if documented.

No retention policy is defined by default.

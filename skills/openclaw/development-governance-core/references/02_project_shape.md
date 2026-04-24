# Project Shape

Project shape should remain as simple as the project allows.

OpenClaw chooses project shape before dispatching implementation work.

## Shape Questions

Before creating or restructuring a project, answer:

- Is this a formal repository or a temporary experiment?
- What is the project boundary?
- Is there one codebase or multiple repositories?
- Is there a real control layer, or just application code?
- Where do task control artifacts live?
- Where do project docs live?
- Where do tests live?
- What should Codex be allowed to edit?

## Default Small Project

For a small project:

```text
repo/
  OPENCLAW.md
  AGENTS.md
  docs/
  src/
  tests/
```

Optional project-local control directory:

```text
repo/
  .openclaw/task/
```

Do not add manager, services, SQL, or complex task runtime unless the project needs them.

## Medium Project

A medium project may have clearer peer roots:

```text
repo/
  OPENCLAW.md
  AGENTS.md
  docs/
  src/
  tests/
  .openclaw/task/
```

If a real control layer exists, it may add:

```text
repo/
  manager/
```

A manager layer is justified only when the project has real orchestration, dispatch, service registration, watcher behavior, retry/resume logic, or task routing.

## Large Project

Large projects may split repositories only when boundaries are real:

- separate ownership
- separate deployment
- separate data boundary
- separate operational cadence
- separate access control
- materially different cadence

Do not split repositories because a project feels large. Split when the boundary is durable.

## OpenClaw Control Directory

Suggested default for project-local control artifacts:

```text
.openclaw/task/
  register/
  execution_key/
  completion_receipt/
  acceptance_receipt/
  output/
```

This skill defines the task exchange structure but not retention policy for these files.

## Shape Discipline

Avoid creating generic folders:

```text
misc/
common/
utils/
helpers/
new/
old/
final/
v2/
```

Use names from the `universal-dictionary` when possible.

## Codex Scope

Project shape should help OpenClaw create bounded Codex tasks.

A good project shape makes it easy to specify:

- allowed edit paths
- blocked paths
- acceptance references
- test commands or test expectations
- output references
- receipt references

Exact field names for these slots should come from `universal-dictionary`.

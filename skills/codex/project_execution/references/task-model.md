# Task Model

OpenClaw turns workflow into bounded tasks.

A task is not a vague wish. A task is a bounded work unit with a goal, scope, acceptance reference, edit boundary, test expectation, output requirement, and lifecycle state.

This reference defines task governance.

Exact task field names and status labels are not standardized here.

## Task Status Flow

Conceptual flow:

```text
designing
  -> ready to dispatch
  -> dispatched
  -> executing
  -> blocked or ready for acceptance
  -> accepted or rejected
  -> closed or cancelled
```

Projects may use simpler or different status labels as long as the task state is clear.

## State Ownership

OpenClaw owns:

- task creation
- readiness for dispatch
- dispatch state
- acceptance outcome
- rejection outcome
- closure
- cancellation

Codex may report:

- execution started
- execution blocked
- implementation ready for OpenClaw review

Only OpenClaw may write the final acceptance outcome or close the task.

## Common Task Information

Each formal task should include these information slots:

- task identity
- task name or short label
- task lifecycle state
- workflow reference
- acceptance reference
- Owner or responsible party
- executor
- priority
- creation time
- update time
- output reference when required
- receipt reference
- issue list when applicable

Optional slots:

- decision reference
- allowed paths
- blocked paths
- test commands
- expected output
- next task reference
- closure time

Exact field names are not standardized here.

## Task Quality Rules

A good task has:

- one clear goal
- a bounded medium-granularity scope
- a workflow reference
- an acceptance reference
- clear allowed paths
- clear blocked paths
- required test commands or a documented reason tests are not needed
- expected output when applicable
- constraints

A poor task says:

```text
Make the project better.
Clean this up.
Fix whatever seems wrong.
You decide.
```

These are not Codex-ready tasks.

## Task Granularity Rule

Prefer tasks in the middle band:

- large enough to complete one coherent acceptance path efficiently
- small enough to keep scope control, review quality, and rollback understandable

Avoid two failure modes:

- micro-tasks that create handoff overhead without reducing material risk
- broad sweeps that cross too many boundaries for one clean review

## Task Decomposition

Do not split tasks too early.

A new task is justified when:

- it has a separate acceptance point
- it is a separate workflow step
- it can be safely dispatched independently
- it changes a different project boundary
- it has a different executor
- it is blocked by different information

Do not create a new task just because it can be phrased separately.

## Task Register

A project may maintain structured task state in its project-local control path if it actually uses it.

If it does not, `docs/04_task.md` may be enough.

`docs/04_task.md` remains the human-readable task summary.

## Transition Rules

Designing -> ready to dispatch:

- task goal is clear
- acceptance reference exists
- scope is bounded

Ready to dispatch -> dispatched:

- execution key is written
- Codex task is sent

Dispatched or executing -> ready for acceptance:

- Codex returns completion receipt
- Codex reports readiness

Ready for acceptance -> accepted:

- OpenClaw checks acceptance
- acceptance receipt is written

Ready for acceptance -> rejected:

- OpenClaw finds an acceptance gap
- issues are written
- follow-up task is created or task is returned

Accepted -> closed:

- docs and task state are updated
- no required follow-up remains

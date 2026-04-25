# Completion Review and Acceptance

Codex returns a completion receipt.
OpenClaw writes an acceptance receipt.

These are different objects.

This reference defines review responsibilities and the minimum information OpenClaw should expect.

Exact receipt container shapes are not standardized here.
Canonical completion-receipt and acceptance-receipt slot names may be standardized and reused across projects.
Default status vocabularies should reuse the registry-registered values for `task_lifecycle_state`, `review_readiness`, `acceptance_outcome`, and `test_status` unless the project docs explicitly override them.

## Completion Receipt

A completion receipt is Codex's structured report.

It should communicate:

- what changed
- which files changed
- which commands ran
- test status
- test output
- issues
- output reference when applicable
- whether Codex believes the task is ready for OpenClaw review

Suggested path:

```text
.openclaw/task/completion_receipt/{task_identity}_completion_receipt.json
```

## Completion Receipt Slots

When a project uses a formal completion receipt, current canonical slot names for these concepts are:

- `TASK_IDENTITY` (`task_identity`)
- `WORKFLOW_IDENTITY` (`workflow_identity`)
- `TASK_LIFECYCLE_STATE` (`task_lifecycle_state`) when the project records one
- `CHANGE_SUMMARY` (`change_summary`)
- `CHANGED_FILES` (`changed_files`)
- `COMMAND_LIST` (`command_list`)
- `TEST_STATUS` (`test_status`)
- `TEST_OUTPUT` (`test_output`)
- `ISSUE_LIST` (`issue_list`)
- `TEMPORARY_NEW_NAMES` (`temporary_new_names`) when applicable
- `OUTPUT_REFERENCE` (`output_reference`) when applicable
- `REVIEW_READINESS` (`review_readiness`)

Default completion vocabularies:

- `task_lifecycle_state`: `designing`, `ready_to_dispatch`, `dispatched`, `executing`, `blocked`, `ready_for_acceptance`, `accepted`, `rejected`, `closed`, `cancelled`
- `review_readiness`: `ready`, `not_ready`, `blocked`
- `test_status`: `passed`, `failed`, `not_run`, `partially_run`, `not_required`

Codex may report readiness or not-readiness.
Codex must not report final acceptance or rejection.

## OpenClaw Review Checklist

When Codex returns a completion receipt, OpenClaw checks:

1. Task identity matches the dispatched task.
2. Workflow identity matches the task.
3. Changed files are inside allowed paths.
4. No file in blocked paths was changed.
5. Command list includes required commands or explains why not.
6. Test status is consistent with test output.
7. Required output exists or is not required.
8. Issues are honest and specific.
9. Naming follows `trading-main/registry/`.
10. Any temporary new names are reported explicitly for OpenClaw review.
11. Any new file has a valid split reason.
12. Acceptance criteria are satisfied.
13. Docs or decisions are updated if the implementation changed project reality.

## Acceptance Receipt

An acceptance receipt is OpenClaw's review decision.

Suggested path:

```text
.openclaw/task/acceptance_receipt/{task_identity}_acceptance_receipt.json
```

When a project uses an acceptance receipt, current canonical slot names for these concepts are:

- `TASK_IDENTITY` (`task_identity`)
- `WORKFLOW_IDENTITY` (`workflow_identity`)
- `ACCEPTANCE_OUTCOME` (`acceptance_outcome`)
- `ACCEPTANCE_REFERENCE` (`acceptance_reference`)
- `REVIEWED_FILES` (`reviewed_files`)
- `REVIEWED_COMMANDS` (`reviewed_commands`)
- `TEST_STATUS` (`test_status`)
- `TEST_OUTPUT` (`test_output`)
- `ISSUE_LIST` (`issue_list`)
- `DECISION_REFERENCES` (`decision_references`) when relevant
- `NEXT_TASK_REFERENCE` (`next_task_reference`) when needed
- `ACCEPTANCE_SUMMARY` (`acceptance_summary`)

Default acceptance vocabularies:

- `acceptance_outcome`: `accepted`, `rejected`, `returned`, `blocked`
- `test_status`: `passed`, `failed`, `not_run`, `partially_run`, `not_required`

## Post-Acceptance Stewardship

When a task is accepted, OpenClaw is responsible for:

- confirming the accepted change set is the one being recorded
- creating the commit for the accepted work
- pushing that commit to GitHub

Do not leave accepted work uncommitted unless the Owner explicitly wants a different handling path.

## Acceptance Authority

Only OpenClaw writes the final acceptance outcome.

Codex may say the task is ready for review.
OpenClaw decides whether the task is accepted, rejected, returned, or blocked.

## Do Not Confuse Test With Acceptance

Passing tests means the task may be ready for review.
It does not automatically mean accepted.

Acceptance checks include:

- tests
- output
- allowed scope
- registry alignment
- docs drift
- decision impact
- split discipline
- Owner intent

# Completion Review and Acceptance

Codex returns a completion receipt.
OpenClaw writes an acceptance receipt.

These are different objects.

This reference defines review responsibilities and required information slots. Exact schema keys and status values belong to `universal-dictionary`.

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

A completion receipt should include:

- task identity
- workflow identity
- task lifecycle state or readiness state
- change summary
- changed file list
- command list
- test status
- test output
- issue list
- output reference when applicable
- acceptance readiness signal

The exact field names should come from `universal-dictionary`.

Codex may report readiness or not-readiness. Codex must not report final acceptance or rejection.

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
9. Naming follows `universal-dictionary`.
10. Any new file has a valid split reason.
11. Acceptance criteria are satisfied.
12. Docs or decisions are updated if the implementation changed project reality.

## Acceptance Receipt

An acceptance receipt is OpenClaw's review decision.

Suggested path:

```text
.openclaw/task/acceptance_receipt/{task_identity}_acceptance_receipt.json
```

An acceptance receipt should communicate:

- task identity
- workflow identity
- acceptance outcome
- acceptance reference
- reviewed files
- reviewed commands
- test status
- test output
- issue list
- decision references
- next task reference when needed
- acceptance summary

The exact field names and status values should come from `universal-dictionary`.

## Post-Acceptance Stewardship

When a task is accepted, OpenClaw is responsible for:

- confirming the accepted change set is the one being recorded
- creating the commit for the accepted work
- pushing that commit to GitHub

Do not leave accepted work uncommitted unless the Owner explicitly wants a different handling path.

## Acceptance Authority

Only OpenClaw writes the final acceptance outcome.

Codex may say the task is ready for review. OpenClaw decides whether the task is accepted, rejected, returned, or blocked.

## Do Not Confuse Test With Acceptance

Passing tests means the task may be ready for review.
It does not automatically mean accepted.

Acceptance checks include:

- tests
- output
- allowed scope
- dictionary alignment
- docs drift
- decision impact
- split discipline
- Owner intent

# Completion Review and Acceptance

Codex returns a completion receipt.
OpenClaw writes an acceptance receipt.

These are different objects.

This reference defines review responsibilities and the minimum information OpenClaw should expect.

Exact receipt schemas and status labels are not standardized here.

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

When a project uses a formal completion receipt, it should include enough information to show:

- task identity
- workflow identity
- task lifecycle state or readiness state
- change summary
- changed file list
- command list
- test status
- test output
- issue list
- temporary new names introduced, if any
- output reference when applicable
- acceptance readiness signal

Exact field names are not standardized here.

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
9. Naming follows `universal-catalog`.
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

When a project uses an acceptance receipt, it should communicate:

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

Exact field names and status labels are not standardized here.

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
- catalog alignment
- docs drift
- decision impact
- split discipline
- Owner intent

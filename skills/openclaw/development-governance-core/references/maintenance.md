# Maintenance Workflow

OpenClaw's long-term value is maintenance discipline.

Codex completes implementation tasks.
OpenClaw prevents the project from becoming incoherent.

## Maintenance Loop

Run maintenance when:

- starting work on a project after a pause
- before dispatching a new wave of tasks
- after Codex returns output
- after accepting or rejecting tasks
- when docs and code may have drifted
- when the Owner asks for project status

## Maintenance Checklist

Check:

1. Required docs exist.
2. `docs/03_acceptance.md` exists.
3. `docs/04_task.md` reflects current active tasks.
4. Every queued or ready task has an acceptance reference.
5. Every dispatched task has an execution key.
6. Every Codex-ready task has a completion receipt.
7. Every accepted or rejected task has an acceptance receipt.
8. Rejected tasks have issue details and follow-up tasks when needed.
9. Accepted changes that alter project reality are reflected in docs.
10. Formal choices are captured in `docs/05_decision.md`.
11. Project-specific memory has been routed into project docs.
12. Formal names follow `universal-catalog`.
13. Extra files or modules have valid split gates.
14. Codex did not modify blocked paths.
15. No global memory is carrying project details that belong in project docs.
16. Meaningful maintained directories have `README.md` boundary docs where needed.
17. Accepted work was committed and pushed after acceptance unless explicitly deferred.

## Maintenance Output

Maintenance output should include these information slots:

- project path
- maintenance status
- check time
- document status
- task status summary
- pending dispatch list
- pending acceptance list
- blocked task list
- dictionary issue list
- split issue list
- memory route issue list
- follow-up task list
- maintenance summary

The exact field names should come from `universal-catalog`.

Suggested path:

```text
.openclaw/task/output/{date}_maintenance_output.json
```

This skill does not define retention for maintenance outputs.

## Status Summary

A compact status summary should group tasks by lifecycle state.

The status values should come from `universal-catalog` or from the project-local task model while the catalog is being prepared.

## Docs Drift Check

Docs drift exists when:

- code behavior changed but workflow docs did not
- test requirements changed but acceptance docs did not
- project scope changed but scope docs did not
- a dependency changed but context docs did not
- task output created a new standard but decision docs did not

OpenClaw should create a docs update task or update docs directly when the correction is small and clearly within authority.

## Maintenance Anti-Patterns

Avoid:

- treating maintenance as optional polish
- accepting tasks without receipts
- leaving rejected tasks without follow-up
- letting docs grow stale because code passed tests
- making global memory carry project-specific details
- introducing retention rules casually

Storage retention is intentionally out of scope here.

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
5. If the project uses execution keys or task packages, dispatched tasks still have them.
6. If the project uses completion receipts or completion reports, returned tasks still have them.
7. If the project uses acceptance receipts, accepted or rejected tasks still have them.
8. Rejected tasks have issue details and follow-up tasks when needed.
9. Accepted changes that alter project reality are reflected in docs.
10. Formal choices are captured in `docs/05_decision.md`.
11. Project-specific memory has been routed into project docs.
12. Formal names reuse existing `trading-main/registry/` entries where they already exist.
13. Extra files or modules have valid split gates.
14. Codex did not modify blocked paths.
15. No global memory is carrying project details that belong in project docs.
16. Meaningful maintained directories have `README.md` boundary docs where needed.
17. Accepted work was committed and pushed after acceptance unless explicitly deferred.

## Maintenance Output

When a project uses a formal maintenance output, current canonical slot names for these concepts are:

- `REPOSITORY_PATH` (`repository_path`)
- `MAINTENANCE_STATUS` (`maintenance_status`)
- `CHECK_TIME` (`check_time`)
- `DOCS_STATUS` (`docs_status`)
- `TASK_STATUS_SUMMARY` (`task_status_summary`)
- `PENDING_DISPATCH_LIST` (`pending_dispatch_list`)
- `PENDING_ACCEPTANCE_LIST` (`pending_acceptance_list`)
- `BLOCKED_TASK_LIST` (`blocked_task_list`)
- `DICTIONARY_ISSUE_LIST` (`dictionary_issue_list`)
- `SPLIT_ISSUE_LIST` (`split_issue_list`)
- `MEMORY_ROUTE_ISSUE_LIST` (`memory_route_issue_list`)
- `FOLLOW_UP_TASK_LIST` (`follow_up_task_list`)
- `MAINTENANCE_SUMMARY` (`maintenance_summary`)

Exact nesting is not standardized here. Reuse the default registry-registered vocabularies for `task_lifecycle_state`, `maintenance_status`, and `docs_status` unless the project docs define an override.

Suggested path:

```text
.openclaw/task/output/{date}_maintenance_output.json
```

This skill does not define retention for maintenance outputs.

## Default Maintenance Vocabularies

Use these defaults unless the project docs define an explicit override:

- `maintenance_status`: `healthy`, `needs_attention`, `blocked`
- `docs_status`: `aligned`, `drifted`, `blocked`
- `task_lifecycle_state`: `designing`, `ready_to_dispatch`, `dispatched`, `executing`, `blocked`, `ready_for_acceptance`, `accepted`, `rejected`, `closed`, `cancelled`

## Status Summary

A compact status summary should group tasks by lifecycle state.

Status labels should come from the project's documented task model, defaulting to the registry-registered `task_lifecycle_state` values when the project has not defined an override.

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

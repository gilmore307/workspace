---
name: server-error-repair
description: "Autonomously diagnose, patch, execute necessary repair actions, verify, and classify server_error_agent_request failures while never mutating broker/account/order/position state."
---

# Server Error Repair

Use when handling a `server_error_agent_request` that needs an autonomous bug fix.

Your mission is to restore the system to the accepted current contract. Do not stop at diagnosis when a repair is possible. Act, verify, and leave a clear machine-readable receipt.

## Authority

You may perform actions needed to fix the bug and prove the fix:

- inspect referenced logs, receipts, read models, source, tests, docs, and config templates
- edit source, tests, scripts, dashboard read-model producers, and repository-owned config templates
- run tests, compile/build/lint checks, probes, local dry-runs, and bounded reproduction commands
- call provider/source APIs, regenerate missing data, rerun stages, write runtime/model outputs, restart services, apply storage maintenance, or adjust system config when that is the necessary repair path
- delete, archive, or rewrite generated/runtime artifacts only when directly required for repair and the receipt names exactly what changed
- mark a failure as `superseded` only when current contracts or task timelines prove the failed route is obsolete
- recommend retry only after the bug is fixed, superseded, no longer applicable, or credibly transient

This authority is intentionally broad enough to repair real bugs. Do not avoid a necessary repair just because it touches runtime, storage, service state, or regenerated artifacts. The constraint is not "read-only"; the constraint is current-contract discipline, narrow scope, and verifiable evidence.

## Project Boundary Rules

- Prefer the current accepted route over historical names, old SQL rows, compatibility wrappers, or stale dashboard/read-model behavior.
- If a source boundary changed, repair the producer and the consumed artifacts together so the old field does not immediately reappear.
- For Trading Economics macro data, the only accepted source is the canonical storage snapshot under `storage/01_source_data/monthly_backfill/trading_economics_calendar_web/`. Do not call or preserve Trading Economics website URLs as source references while the subscription is expired.
- Treat SQL rows, dashboard caches, control-plane artifacts, runtime receipts, and lifecycle outputs as derived or operational state unless the current contract explicitly says they are canonical.
- When a repair edits durable source artifacts, scan for secrets/sensitive values before committing or reporting.

## Non-Negotiable Boundary

Never do these:

- broker/order/fill/account/position mutation
- secret printing, copying, migration into repo files, or broad environment dumps

If repair requires broker/account/order/position mutation, stop and return `blocked_boundary` with a precise `blocked_actions` list.

For every powerful action, keep scope narrow and leave evidence:

- state why the action was necessary
- record affected paths, commands, services, providers, or tables without exposing secrets
- verify the system state after the action
- prefer current contracts over historical route names
- do not hide residual risk or unresolved failures
- commit/push repository edits only after the relevant verification gate passes, unless the owner explicitly asked for an uncommitted patch
- if a runtime/service change is needed, include the service name, command class, and post-action status/log evidence in the receipt

## Workflow

1. Read the request and referenced evidence. Identify the current accepted route before trusting old stage names.
2. Classify the fault: code, config, data-gap, external-provider, environment, obsolete-route, duplicate, transient, or insufficient-evidence.
3. Choose the smallest action that actually repairs the failure, including provider/source, runtime, service, storage, or system actions when needed.
4. Patch code/config and add or update focused tests when the repair touches maintained implementation.
5. Run verification that proves the repair. Expand when the touched boundary requires it.
6. If the route is obsolete, return `superseded` with the current route evidence and do not pretend the old stage was repaired.
7. Leave unresolved items explicit. Do not close an error because it is inconvenient.

## Final Output

Return strict JSON only:

```json
{
  "review_type": "server_error_repair",
  "error_ref": "string",
  "diagnosis_status": "repaired_verified|repaired_awaiting_retry|superseded|blocked_boundary|no_action_needed|not_supported|insufficient_evidence",
  "root_cause": "string",
  "repair_attempted": true,
  "repair": {
    "repair_status": "repaired|superseded|blocked|no_action_needed|not_supported",
    "repair_kind": "code|config|read_model|dashboard|obsolete_route|data_gap|provider|runtime|service|storage|system|environment|none",
    "reason": "string",
    "files_changed": ["string"]
  },
  "files_changed": ["string"],
  "verification": ["string"],
  "retry_recommendation": "retry|wait_for_scheduler|manual_review|do_not_retry|blocked_boundary",
  "actions_taken": ["string"],
  "blocked_actions": ["string"],
  "blockers": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

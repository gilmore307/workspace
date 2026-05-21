---
name: server-error-repair
description: "Autonomously diagnose, patch, verify, and classify bounded server_error_agent_request failures under strict trading-system safety gates."
---

# Server Error Repair

Use when handling a `server_error_agent_request` that may need an autonomous bug fix.

## Authority

You may repair internal repository bugs when the evidence is bounded and the fix is reversible:

- inspect referenced logs, receipts, read models, source, tests, docs, and config templates
- edit source, tests, scripts, dashboard read-model producers, and repository-owned config templates
- run non-destructive tests, compile/build/lint checks, read-only probes, and local dry-runs
- mark a failure as `superseded` only when current contracts or task timelines prove the failed route is obsolete
- recommend retry only after the bug is fixed, superseded, no longer applicable, or credibly transient

## Hard Gates

Do not perform these without an explicit separate gate or approval:

- provider/API calls for market, economic, SEC, news, calendar, or options data
- broker/order/fill/account/position mutation
- destructive storage mutation, artifact deletion, archive pruning, or lifecycle apply
- model-output database writes, runtime stage writes, or historical model reruns that change durable evidence
- live service restarts, package installation, OS/system config changes, or firewall/network changes
- secret printing, copying, migration into repo files, or broad environment dumps

If a fix requires a gated action, stop at diagnosis plus a precise `gated_actions` list.

## Workflow

1. Read the request and referenced evidence. Identify the current accepted route before trusting old stage names.
2. Classify the fault: code, config, data-gap, external-provider, environment, obsolete-route, duplicate, transient, or insufficient-evidence.
3. If it is a safe internal bug, patch the smallest repo-owned surface and add or update focused tests.
4. Run the smallest verification gate that proves the repair. Expand only when the touched boundary requires it.
5. If the original failing command writes durable model/runtime output, do not rerun it unless the request explicitly authorizes that write; return `repaired_awaiting_retry`.
6. If the route is obsolete, return `superseded` with the current route evidence and do not pretend the old stage was repaired.
7. Leave unresolved items explicit. Do not close an error because it is inconvenient.

## Final Output

Return strict JSON only:

```json
{
  "review_type": "server_error_repair",
  "error_ref": "string",
  "diagnosis_status": "repaired_verified|repaired_awaiting_retry|superseded|blocked_gate|no_action_needed|not_supported|insufficient_evidence",
  "root_cause": "string",
  "repair_attempted": true,
  "repair": {
    "repair_status": "repaired|superseded|blocked|no_action_needed|not_supported",
    "repair_kind": "code|config|read_model|dashboard|obsolete_route|data_gap|environment|none",
    "reason": "string",
    "files_changed": ["string"]
  },
  "files_changed": ["string"],
  "verification": ["string"],
  "retry_recommendation": "retry|wait_for_scheduler|manual_review|do_not_retry|needs_gate",
  "gated_actions": ["string"],
  "blockers": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

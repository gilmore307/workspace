---
name: server-error-diagnosis
description: Diagnose and safely repair server-wide trading-system failures from bounded evidence. Use when an agent receives a server_error_agent_request, agent_error_diagnosis task, failed stage handoff, or cross-component error bundle.
---

# Server Error Diagnosis

Use this skill for bounded diagnosis and safe internal repair. It is not a license to mutate external systems or hide unresolved failures.

## Allowed Work

- Inspect referenced logs, receipts, status artifacts, source files, docs, and tests.
- Classify the root cause as code, config, data, environment, provider, dependency, or operator-boundary related.
- Prepare reversible code, test, config-template, or documentation patches inside repository boundaries.
- Run non-destructive verification commands.
- Recommend retry only after the cause is fixed or credibly transient.

## Forbidden Work

- Do not call market-data providers without a separate provider-dispatch gate.
- Do not submit broker orders, construct live order submission, mutate accounts, or touch funds/positions.
- Do not print, copy, or exfiltrate secrets.
- Do not delete data, rewrite durable storage, restart services, or change system packages without an explicit higher-level approval path.
- Do not mark failures accepted, corrected, or skipped without durable diagnosis evidence and the appropriate review ref.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "server_error_diagnosis",
  "error_ref": "string",
  "diagnosis_status": "fixed|retry_recommended|blocked|insufficient_evidence|no_action",
  "root_cause": "string",
  "repair_attempted": true,
  "files_changed": ["string"],
  "verification": ["string"],
  "retry_recommendation": "retry|do_not_retry|manual_review",
  "blockers": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```


---
name: storage-lifecycle-review
description: Review storage-owned backup, cleanup, archive, restore, and deletion decisions before lifecycle mutation. Use when an agent is asked to approve or reject agent_storage_lifecycle_decision evidence.
---

# Storage Lifecycle Review

Use this skill when a storage lifecycle mutation needs judgment beyond deterministic retention rules. Storage owns the action; the agent only reviews evidence and produces a decision artifact.

## Non-Negotiable Boundaries

- Do not delete, archive, restore, or move files directly from the review.
- Do not approve mutation without policy evidence, protected-set checks, and restore/backup evidence when the action requires it.
- If an explicit accepted instruction says delete, do not replace deletion with a trash-folder workaround.
- Keep SQL-resident durable facts in SQL; do not preserve migrated legacy JSONL/catalog files under a new storage folder just to avoid deletion.
- Manager does not emit cleanup requests for completed folds; storage monitors fold completion state and acts through storage-owned lifecycle policy.

## Required Inputs

- lifecycle action: backup, cleanup, archive, restore, delete, or retention_update
- target scope and concrete paths/table refs
- retention policy and protected-set status
- backup or logical dump ref when required
- restore/readback verification plan
- deletion eligibility evidence, including fold completion status when fold cleanup is involved
- risk summary and rollback/restore route if available

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "storage_lifecycle_review",
  "decision": "approve|defer|reject|insufficient_evidence",
  "action": "backup|cleanup|archive|restore|delete|retention_update",
  "target_scope": "string",
  "backup_status": "present|not_required|missing|insufficient_evidence",
  "protected_set_status": "clear|blocked|insufficient_evidence",
  "restore_route_status": "available|not_required|missing|insufficient_evidence",
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```


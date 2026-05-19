---
name: failure-register-review
description: Review failed manager/component requests before they are accepted, skipped, corrected, retried, or left unresolved. Use when an agent is asked to decide failure_register disposition or validate agent_review_ref evidence.
---

# Failure Register Review

Use this skill to classify failed work without erasing the failure history. The agent decides whether evidence supports retry, correction, accepted skip, or unresolved status.

## Fixed Criteria

- Preserve the original failure row and append disposition evidence; do not rewrite history.
- Retry only when the cause is fixed, plausibly transient, or the retry risk is understood.
- Corrected requires evidence of the corrective change and verification.
- Accepted skip requires a concrete reason showing the skipped work is no longer required, impossible by accepted policy, or superseded by better evidence.
- Do not use accepted skip to hide flaky automation, missing provider evidence, failed tests, or unclear root cause.
- If the failure involves provider, broker, storage mutation, or secrets, require the corresponding higher-level gate before recommending action.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "failure_register_review",
  "failure_ref": "string",
  "decision": "retry|corrected|accepted_skip|unresolved|insufficient_evidence",
  "root_cause_status": "identified|probable|unknown",
  "evidence_status": "sufficient|insufficient",
  "retry_allowed": true,
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```


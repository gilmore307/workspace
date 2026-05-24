---
name: target-context-review
description: Review target-to-Layer-2 context mappings before target-specific model work uses them. Use when an agent is asked to approve, reject, or defer target context state, sector/industry/proxy mapping, or optionability routing evidence.
---

# Target Context Review

Use this skill before target-specific model layers consume Layer 2 context. The agent checks whether the target context is specific, point-in-time, and safe to use.

## Fixed Criteria

- The target must have a reviewed Layer 2 sector/industry/market-context mapping.
- Proxy rows must be target-specific and must not silently mutate Layer 1 or Layer 2 universes.
- Optionability must route option-dependent work explicitly; non-optionable targets must not receive option-chain or option-expression requirements.
- Evidence must include point-in-time availability and source refs, not only current metadata.
- Ambiguous sector, ticker, corporate-action, delisting, or proxy evidence should defer rather than approve.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "target_context_review",
  "target_id": "string",
  "decision": "approve|defer|reject|insufficient_evidence",
  "layer2_context_status": "accepted|rejected|deferred|insufficient_evidence",
  "proxy_status": "accepted|rejected|not_applicable|insufficient_evidence",
  "optionability_status": "accepted|rejected|not_applicable|insufficient_evidence",
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```


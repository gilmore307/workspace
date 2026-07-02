---
name: "event-strategy-promotion-review"
description: "Deprecated event-model review route; use narrower skills."
---

# Event Strategy Promotion Review

This is a deprecated compatibility route for older prompts that ask for event-strategy promotion or residual event-risk promotion review.

Do not use this skill as the current event-model review path. Under the current event impact distribution architecture, route to the narrower skill that owns the task.

## Current Routing

Use these skills instead:

- `event-interpretation`: raw PIT artifacts to standardized event facts.
- `event-taxonomy-standard-review`: reusable event type/family/lifecycle standards.
- `regime-interval-review`: persistent event-regime interval governance.
- `event-family-modelability-review`: M06 modelability, projection mode, and probability-function class.
- `event-context-projection-review`: context-only projection review.
- `event-state-projection-review`: M03 event_state_projection compliance review.
- `event-leakage-overlap-review`: PIT leakage, selected-path contamination, and feature/label overlap audit.
- `target-context-review`: PIT target/context/optionability routing only.

## Compatibility Behavior

If a legacy task invokes this skill:

1. Identify the actual current review type.
2. State the redirected skill name.
3. Return `defer` unless the caller provides the required inputs for the narrower skill.
4. Do not approve event evidence under the old Layer 4 promotion semantics.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "event_strategy_promotion_review_legacy_router",
  "subject_ref": "string",
  "decision": "defer|reject|insufficient_evidence",
  "redirect_to_skill": "event-interpretation|event-taxonomy-standard-review|regime-interval-review|event-family-modelability-review|event-context-projection-review|event-state-projection-review|event-leakage-overlap-review|target-context-review",
  "legacy_route_status": "deprecated",
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short explanation of why the old route is no longer authoritative"
}
```

## Non-Negotiable Boundaries

- Do not approve event evidence for model use through this legacy route.
- Do not output signed impact, probability-function class, modelability status, M03 parameters, alpha direction, trade decision, position sizing, option selection, or execution guidance.
- Do not preserve old `promote_to_layer_4` language as current architecture.

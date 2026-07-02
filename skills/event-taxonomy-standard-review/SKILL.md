---
name: "event-taxonomy-standard-review"
description: "Review reusable event taxonomy and family standards."
---

# Event Taxonomy Standard Review

Use this Codex skill when an agent must decide whether a proposed event type, event family, lifecycle class, or event-standard rule is reusable enough to register for the trading event model stack.

This is taxonomy governance. It does not model market impact, choose probability-function parameters, approve M03 training, or produce trade advice.

## Review Scope

Review proposals for:

- new `normalized_event_type`
- new `event_family_ref`
- lifecycle-class rules
- required event-interpretation fields
- source precedence and dedup rules
- inclusion and exclusion criteria
- unknown-event standard proposals
- canonical event vs narrative residual distinctions

## Required Inputs

- proposed event type/family key
- definition and scope
- inclusion criteria
- exclusion criteria
- lifecycle class and clock rules
- affected scope/entity routing hints
- canonical source precedence
- dedup/canonical relation rules
- score-anchor guidance for semantic valence, materiality, uncertainty, novelty, source quality, and evidence confidence
- examples, near-misses, and non-examples
- PIT evidence refs and source-quality notes
- downstream consumers and blocked uses

## Review Workflow

1. Validate point-in-time suitability.
   - The standard must be usable without future market reaction or post-hoc explanation.

2. Test reuse value.
   - Approve only if the event type/family is distinct, recurring or high-impact, and not better represented by an existing standard.

3. Check taxonomy boundaries.
   - Avoid over-specific one-off labels.
   - Avoid broad labels that merge different lifecycle/clock/source patterns.
   - Preserve scheduled vs surprise vs multi-stage vs regime distinctions.

4. Check canonical/dedup policy.
   - Specify when news is duplicate coverage of a canonical event.
   - Specify when narrative residuals can be preserved separately.

5. Check score-anchor safety.
   - Semantic valence is factual event valence, not predicted price direction.
   - No score anchor may imply alpha, expected return, impact function parameters, or trade action.

6. Decide whether the standard can be registered, deferred, rejected, or routed to a narrower review.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "event_taxonomy_standard_review",
  "standard_ref": "string",
  "decision": "approve|defer|reject|insufficient_evidence",
  "standard_kind": "event_type|event_family|lifecycle_class|source_precedence|dedup_rule|score_anchor|unknown_event_standard",
  "pit_status": "passed|failed|insufficient_evidence",
  "reuse_status": "reusable|too_specific|too_broad|duplicate|insufficient_evidence",
  "boundary_status": "clear|ambiguous|overlapping|insufficient_evidence",
  "canonical_policy_status": "passed|failed|not_applicable|insufficient_evidence",
  "allowed_event_interpretation_use": ["string"],
  "blocked_model_use": [
    "impact_direction",
    "signed_impact_distribution",
    "m03_parameter_training_approval",
    "alpha_direction",
    "trade_decision",
    "position_sizing",
    "broker_or_order_action"
  ],
  "required_fields": ["string"],
  "required_followups": ["string"],
  "blocking_issues": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

## Decision Rules

- `approve`: reusable, PIT-safe, clearly bounded, and not duplicate.
- `defer`: plausible but missing examples, boundary, source precedence, or clock rules.
- `reject`: duplicate, too broad, too narrow, non-PIT-safe, or predictive/trade-like.
- `insufficient_evidence`: required proposal evidence is absent.

## Non-Negotiable Boundaries

- Do not approve market-impact, return, volatility, or option-expression semantics as taxonomy fields.
- Do not turn taxonomy review into event-family modelability review.
- Do not infer trade direction or utility.
- Do not register standards from hindsight-only narratives.

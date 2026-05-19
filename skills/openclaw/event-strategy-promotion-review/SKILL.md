---
name: event-strategy-promotion-review
description: Review event-family and strategy-failure evidence before it can be promoted into Layer 4 or related model decision layers. Use when an agent judges event interpretation, event-family scouting, strategy-failure packets, or residual event-risk promotion.
---

# Event Strategy Promotion Review

Use this skill before event or strategy-failure evidence can affect model scoring, intervention, or Layer 4 promotion. The agent checks whether the evidence is causal enough, point-in-time enough, and non-overlapping enough to become model input.

## Non-Negotiable Boundaries

- Raw event text, news anomalies, or unreviewed labels cannot enter scoring.
- Event interpretation artifacts must be standardized and point-in-time.
- Evidence must prove non-overlap with upstream features or residual value after upstream conditioning.
- Matched controls, base rates, and leakage checks are required before promotion.
- Do not output buy/sell advice, position sizing, order construction, or broker/account actions.
- Do not promote a family because it is interesting; promote only when the incremental evidence survives controls.

## Required Inputs

- event family or strategy-failure id and scope
- interpreted event refs and point-in-time availability clocks
- matched-control evidence and base-rate comparison
- upstream overlap status: `not_in_upstream_features`, `residual_after_upstream_conditioning`, or `review_required_overlap_unknown`
- leakage review and label horizon evidence
- proposed model-layer consumption route and blocked outputs
- failure modes and known confounders

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "event_strategy_promotion_review",
  "subject_ref": "string",
  "decision": "approve|defer|reject|insufficient_evidence",
  "pit_status": "passed|failed|insufficient_evidence",
  "control_status": "passed|failed|insufficient_evidence",
  "overlap_status": "not_in_upstream_features|residual_after_upstream_conditioning|review_required_overlap_unknown|failed|insufficient_evidence",
  "leakage_status": "passed|failed|insufficient_evidence",
  "allowed_model_use": ["string"],
  "blocked_model_use": ["string"],
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```


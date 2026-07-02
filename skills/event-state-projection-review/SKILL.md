---
name: "event-state-projection-review"
description: "Review M03 event_state_projection compliance."
---

# Event State Projection Review

Use this Codex skill when an agent must review whether an M03 `event_state_projection` artifact is structurally valid, point-in-time safe, and compliant with M06-approved modelability/projection-mode governance.

This is an artifact compliance review. It does not choose event-family probability-function classes, train parameters, tune projections, judge profitability, or approve trade direction.

## Core Boundary

M03 owns learned event-state projections. This skill checks whether the artifact obeys the accepted contract:

- event row identity is correct
- source event refs and clocks are point-in-time
- projection mode matches M06 approval
- model/fold/parameter refs are frozen and auditable
- output summaries are standardized for M04/M05
- no freeform agent opinion enters production scoring

## Required Inputs

- `event_state_projection_ref`
- event row refs and row unit: event, event update, regime interval, episode node, or context flag
- source `event_interpretation` refs and clocks
- M06 `event_family_modelability_review` ref
- projection mode and probability-function class
- M03 training artifact refs, fold IDs, and frozen parameter refs
- output horizon summaries and schema refs
- leakage/overlap review ref if available
- downstream consumers: M04/M05/dashboard/replay review

## Review Workflow

1. Validate source lineage.
   - Every projection row must trace to accepted event-pool units.
   - M03 rows must not be selected-trade substitutes.

2. Validate point-in-time and fold safety.
   - Inference fields visible before decision time.
   - Training/fold refs frozen before validation/test use.
   - Outcome labels remain training/evaluation labels, not inference inputs.

3. Validate governance match.
   - Projection mode must match M06-approved status.
   - Probability-function class must match allowed class.
   - Context-only projections must not contain signed impact distributions.

4. Validate output contract.
   - M04/M05 receive standardized summaries only.
   - Family-specific internals stay behind the M03 contract.
   - Confidence, support, calibration, and downgrade flags are present when required.

5. Decide pass/defer/reject.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "event_state_projection_review",
  "event_state_projection_ref": "string",
  "decision": "pass|defer|reject|insufficient_evidence",
  "projection_mode": "impact_function_projection|conditional_effect_projection|context_only_projection|do_not_model|unknown",
  "governance_match_status": "passed|failed|insufficient_evidence",
  "pit_status": "passed|failed|insufficient_evidence",
  "fold_freeze_status": "passed|failed|not_applicable|insufficient_evidence",
  "row_identity_status": "passed|failed|insufficient_evidence",
  "schema_status": "passed|failed|insufficient_evidence",
  "calibration_evidence_status": "passed|failed|not_required|insufficient_evidence",
  "allowed_downstream_use": ["m04_risk_adjustment", "m05_expression_adjustment", "dashboard_display", "replay_evaluation"],
  "blocked_model_use": ["freeform_agent_opinion", "unapproved_signed_impact", "trade_decision", "position_sizing", "broker_or_order_action"],
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

## Decision Rules

- `pass`: artifact lineage, PIT, governance, schema, and fold/calibration requirements are adequate for proposed use.
- `defer`: plausible artifact but missing review refs, calibration evidence, or provenance.
- `reject`: governance mismatch, leakage, row-unit failure, schema failure, or unapproved signed impact.
- `insufficient_evidence`: required inputs are absent.

## Non-Negotiable Boundaries

- Do not tune or suggest parameter values.
- Do not judge whether the projection is profitable.
- Do not choose probability-function class; use `event-family-modelability-review` for that.
- Do not allow context-only projections to carry signed impact.
- Do not output alpha, trade direction, option selection, position sizing, or execution guidance.

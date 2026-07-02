---
name: "event-context-projection-review"
description: "Review event families that should remain context-only risk inputs."
---

# Event Context Projection Review

Use this Codex skill when an agent must decide whether an event family or event observation should be handled as `context_only_projection` instead of `impact_function_projection` or `conditional_effect_projection`.

This skill is for Codex CLI review tasks. It produces a governance judgment for M06/M03 event projection routing. It does not train M03, does not estimate an event impact function, and does not approve trade direction.

## Core Boundary

`context_only_projection` means the event is relevant context, but current evidence does not support a reliable signed impact distribution.

The review may allow downstream caution, uncertainty widening, or expression-risk constraints. It must not output bullish/bearish direction, impact magnitude, alpha, trade intent, position sizing, option structure, or broker/account actions.

## Use When

Use this skill for event families or event observations with one or more of these conditions:

- no stable reusable event impact morphology
- too few comparable samples
- high overlap with macro regime, sector regime, target fundamentals, liquidity stress, or concurrent events
- repeated updates whose process cannot be reduced to one point event
- ambiguous target/entity scope
- weak source quality or low confidence standardization
- direct effect mapping fails or has not passed fold-frozen calibration
- M06 modelability assessment proposes `context_only_projection`

Do not use this skill to review event families that already have accepted `impact_function_projection` evidence or a calibrated `conditional_effect_projection` unless the task is explicitly a downgrade or safety review.

## Required Inputs

If required evidence is missing, return `insufficient_evidence` rather than guessing.

- `subject_ref`: event family, event observation, candidate regime, or event packet id
- standardized event fields: normalized type, family, affected scope, affected entities, available time, event time or interval, source clocks, source quality, uncertainty, direction-bias fields if present
- M06 modelability evidence or proposed status
- known confounders and overlapping events/regimes
- sample/support evidence if available
- PIT/leakage evidence
- proposed downstream consumers: M03, M04, M05, dashboard, replay review, or training/evaluation
- proposed blocked outputs, if any

## Review Workflow

1. Verify point-in-time integrity.
   - Source clocks must be visible at or before `available_time`.
   - Later market reaction, later event revisions, and downstream trade results cannot be used as inference facts.

2. Decide whether impact-function modeling is unsupported.
   - Reject function modeling when the event family has no stable phase/clock/morphology, insufficient samples, unstable effects across folds, or unresolved overlap with other drivers.

3. Decide whether conditional effect projection is unsupported.
   - Reject signed effect mapping when calibrated direct mapping has not beaten context-only in fold-frozen tests, parameter support is sparse, confounding dominates, or tail/sign calibration is unreliable.

4. Classify context relevance.
   - `material`: downstream models should widen uncertainty or apply caution.
   - `moderate`: downstream models may display context and mild caution.
   - `weak`: track as context, but do not materially alter decisions.
   - `noise`: reject as unusable context.

5. Assign risk-context channels only.
   Allowed channels:
   - `uncertainty_widening`
   - `liquidity_caution`
   - `gap_risk_caution`
   - `reversal_risk_caution`
   - `regime_overlap`
   - `target_event_overlap`
   - `scope_escalation_caution`
   - `source_quality_caution`
   - `timing_uncertainty_caution`
   - `do_not_use`

6. Set downstream usage.
   - M03 may emit `risk_context_summary` only.
   - M04 may use it for risk adjustment or uncertainty widening only.
   - M05 may use it for expression caution only.
   - No layer may infer signed impact, utility delta, alpha direction, or trade instruction from this output.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "event_context_projection_review",
  "subject_ref": "string",
  "decision": "approve_context_only|defer|reject|insufficient_evidence",
  "projection_mode": "context_only_projection",
  "context_relevance": "material|moderate|weak|noise|unknown",
  "pit_status": "passed|failed|insufficient_evidence",
  "function_modelability_status": "unsupported|not_identifiable|insufficient_evidence|not_reviewed",
  "conditional_effect_status": "unsupported|not_calibrated|insufficient_evidence|not_reviewed",
  "confounding_status": "low|moderate|high|dominant|unknown",
  "primary_confounders": ["string"],
  "risk_context_channels": ["uncertainty_widening"],
  "allowed_model_use": ["risk_context_summary"],
  "blocked_model_use": [
    "signed_impact_distribution",
    "impact_function_projection",
    "conditional_effect_projection",
    "alpha_direction",
    "trade_decision",
    "position_sizing",
    "option_structure_selection",
    "broker_or_order_action"
  ],
  "m03_instruction": "emit_context_only_projection|do_not_emit|defer",
  "m04_instruction": "risk_adjustment_only|no_use|defer",
  "m05_instruction": "expression_caution_only|no_use|defer",
  "confidence": 0.0,
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

## Decision Rules

- Use `approve_context_only` only when PIT evidence is adequate and the event is relevant enough for context, but signed impact modeling is unsupported or unvalidated.
- Use `defer` when the event may deserve context-only treatment but required modelability, confounding, or source evidence is incomplete.
- Use `reject` when the event is noise, duplicate coverage, failed PIT integrity, or not relevant even as context.
- Use `insufficient_evidence` when required inputs are absent.

## Non-Negotiable Safety Rules

- Never infer or output bullish/bearish direction.
- Never output impact magnitude, utility delta, probability of profit, or trade recommendation.
- Never use future market reaction, selected trade outcome, replay failure label, or post-hoc event revision as inference input.
- Do not upgrade an event from context-only to signed effect projection. That requires M06 modelability evidence plus M03 fold-frozen calibration.
- When in doubt between signed effect and context-only, choose context-only or defer.

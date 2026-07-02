---
name: "event-family-modelability-review"
description: "Review event-family probability-function type and projection mode."
---

# Event Family Modelability Review

Use this Codex skill when an agent must judge whether an event family can be modeled by an event impact distribution function, what probability-function class is appropriate, or whether the family should be downgraded to conditional effect, context-only projection, or do-not-model.

This skill is for M06 governance review. It does not train M03, does not estimate concrete event parameters, and does not approve trade direction.

## Core Boundary

M06 owns event-family modelability and probability-function governance. M03 owns learned parameters and live/replay event-state projections.

The reviewer decides:

- whether the event family is function-modelable
- which probability-function or morphology class is allowed
- whether direct conditional mapping is allowed instead
- whether only context-only projection is allowed
- what evidence is required before M03 may train or emit signed impact summaries

The reviewer must not output concrete bullish/bearish direction, magnitude, half-life, amplitude, utility delta, trade recommendation, position sizing, option structure, or broker/account action.

## Same-Family Evidence Rule

M06 must not classify a probability-function type or event-family modelability from a single observed event.

A single event may support only:

- taxonomy normalization
- provisional family assignment
- context-only caution
- evidence-gap reporting
- a request to collect more same-family observations

To approve `impact_function_projection` or `conditional_effect_projection`, M06 must have multiple comparable events from the same canonical event family. The same-family packet must include enough point-in-time observations to evaluate repeatability across folds, targets/scopes when applicable, and horizons. If only one event or one event episode is available, return `insufficient_evidence` or `defer` even when the event looks intuitive.

Same-family support must be judged on:

- comparable-event count and coverage by fold/horizon
- event-family homogeneity and subtype separation
- repeated lifecycle/phase behavior
- matched-control or baseline evidence
- overlap/confounder separability
- out-of-fold calibration evidence when available

Do not mix unrelated event families to manufacture sample support. If the family is too broad, require a narrower family or subtype before approving a function class.

## Projection Modes

Allowed projection modes:

- `impact_function_projection`: event family has a stable enough morphology to model signed impact intensity over relative time.
- `conditional_effect_projection`: causal isolation is weak, but standardized event parameters have validated point-in-time association with later outcome distributions.
- `context_only_projection`: event is relevant context, but neither impact function nor signed conditional effect is reliable.
- `do_not_model`: event family is duplicate, noise, non-material, or fails point-in-time/source standards.

## Probability Function Classes

Choose a governed class, not an unconstrained distribution menu.

Allowed classes:

- `continuous_symmetric`: Gaussian or similarly symmetric continuous family.
- `continuous_skewed`: skew-normal, skew-t, or comparable signed continuous family.
- `heavy_tail`: Student-t, generalized error, tail-calibrated empirical, or comparable heavy-tail family.
- `zero_inflated_or_hurdle`: mass near no-impact plus signed continuous severity.
- `count_driven_compound`: count process such as Poisson/negative-binomial for event/update arrivals plus signed severity distribution. Do not use count distributions directly for signed impact intensity.
- `mixture`: documented multimodality, subtype ambiguity, or regime interaction. Requires stronger evidence.
- `regime_state_machine`: active/shadow/decay/resolution state with transition/hazard logic.
- `episode_graph`: multi-stage developing event where separate updates form an event episode graph.
- `empirical_quantile`: nonparametric calibrated quantile output when parametric assumptions are weak but sample support is adequate.
- `none`: no signed impact function is allowed.

## Required Inputs

If required evidence is missing, return `insufficient_evidence` or `defer` rather than guessing.

- `event_family_ref` and canonical family name
- lifecycle class and event clocks: awareness, scheduled, published, available, resolution, interval if applicable
- standardized event parameters and score anchors
- affected scope/entities and target-context routing evidence
- same-family observation packet with multiple comparable events, not just one observed event
- sample count and comparable-event support by fold/horizon
- base rates and matched-control evidence
- overlap/confounder evidence against M01 background, M02 target context, M05 option/liquidity context, concurrent events, and regimes
- leakage and point-in-time audit
- candidate probability-function classes and rationale if proposed
- calibration evidence if any: sign, quantile coverage, tail coverage, CRPS/log score/PIT diagnostics
- proposed M03/M04/M05 consumption route and blocked uses

## Review Workflow

1. Validate point-in-time integrity.
   - All interpretation inputs must be visible at or before `available_time`.
   - Later event revisions, later market reaction, selected trade outcome, and replay failure labels cannot be inference facts.

2. Validate same-family evidence support.
   - Count comparable events from the same canonical family.
   - Check whether the proposed family is too broad or mixes unrelated subtypes.
   - Reject single-event probability-function classification.
   - If support is weak, allow only context-only or defer.

3. Classify lifecycle and row unit.
   - Scheduled release, surprise event, recurring macro release, multi-stage event, persistent regime, abnormal activity, or other.
   - Decide whether the row unit is event, event update, regime interval, episode node, or context flag.

4. Decide modelability.
   - `function_modelable` only when the family has reusable phase/clock/morphology and adequate same-family support.
   - `conditional_effect_only` only when impact mechanism is not cleanly isolatable but PIT event parameters have validated predictive association across same-family observations.
   - `context_only` when signed impact is unreliable but context is material.
   - `not_modelable` when evidence is noise, duplicate, or too confounded even for context use.

5. Select probability-function class.
   - Use the simplest class that fits the event family morphology and calibration evidence.
   - Do not choose mixture or count-driven compound without specific same-family evidence.
   - Negative binomial or Poisson may model arrival/update counts only, not signed impact intensity directly.

6. Set M03 ownership.
   - M03 must train concrete parameters using fold-frozen point-in-time data.
   - M03 must emit standardized summaries, not family-specific internals, to M04/M05.

7. Set validation requirements.
   - Require fold-frozen calibration before production use.
   - Require ablation versus context-only for conditional effect projection.
   - Require uncertainty widening and downgrade rules for weak support.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "event_family_modelability_review",
  "event_family_ref": "string",
  "decision": "approve|defer|reject|insufficient_evidence",
  "modelability_status": "function_modelable|conditional_effect_only|context_only|not_modelable|insufficient_evidence",
  "projection_mode": "impact_function_projection|conditional_effect_projection|context_only_projection|do_not_model",
  "probability_function_class": "continuous_symmetric|continuous_skewed|heavy_tail|zero_inflated_or_hurdle|count_driven_compound|mixture|regime_state_machine|episode_graph|empirical_quantile|none",
  "row_unit": "event|event_update|regime_interval|episode_node|context_flag|unknown",
  "pit_status": "passed|failed|insufficient_evidence",
  "same_family_support_status": "adequate|weak|failed|insufficient_evidence",
  "same_family_event_count": 0,
  "sample_support_status": "adequate|weak|failed|insufficient_evidence",
  "confounding_status": "low|moderate|high|dominant|unknown",
  "calibration_status": "passed|failed|not_available|insufficient_evidence",
  "allowed_m03_output": ["event_state_projection"],
  "blocked_model_use": [
    "single_event_family_function_classification",
    "m06_concrete_parameter_prediction",
    "alpha_direction",
    "trade_decision",
    "position_sizing",
    "option_structure_selection",
    "broker_or_order_action"
  ],
  "required_m03_training_evidence": ["string"],
  "required_followups": ["string"],
  "blocking_issues": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

## Decision Rules

- `approve` with `impact_function_projection` only when the family has stable morphology, adequate same-family PIT sample support, and a justified probability-function class.
- `approve` with `conditional_effect_projection` only when direct mapping beats context-only in fold-frozen calibration/ablation across same-family observations and remains PIT-safe.
- Use `context_only_projection` when event context is material but signed impact modeling is unvalidated, unstable, single-event, or too confounded.
- Use `do_not_model` when the family is duplicate, noise, irrelevant, or fails PIT integrity.
- When uncertain between signed impact and context-only, choose context-only or defer.

## Non-Negotiable Safety Rules

- M06 must not output concrete direction, amplitude, half-life, probability of profit, or utility delta.
- M06 must not approve an event-family probability-function class from a single observed event.
- Distribution class choice is model structure and must be frozen per fold/version before validation.
- Never select a probability function because it fits full-history outcomes after the fact.
- Never train from selected trade outcomes or filter early event layers by downstream selected trades.
- M04/M05 consume standardized summaries only; they must not depend on family-specific internals.

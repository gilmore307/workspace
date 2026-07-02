---
name: "event-interpretation"
description: "Standardize PIT event facts without predicting market impact."
---

# Event Interpretation

Use this skill when raw event artifacts must become standardized point-in-time event artifacts before event-model training, replay review, or runtime event-state projection.

The agent is a conservative event-standardization worker. It does not predict market impact, choose probability functions, approve modelability, or produce trade advice.

## Core Boundary

Event interpretation creates event facts and interpretation metadata:

- what happened or is scheduled
- when it became knowable
- who or what it affects
- how reliable the evidence is
- what lifecycle class and event family it belongs to
- whether it is canonical, duplicate, follow-up, narrative residual, or unknown

It must not output learned market impact, expected return, signed impact distribution, half-life, event-impact function parameters, utility delta, alpha, trade direction, option expression, position sizing, or broker/account action.

## Required Inputs

- raw artifact path/ref, source, source type, and source hash
- provider/source timestamp fields
- capture/retrieval time and proposed `available_time`
- raw text or structured fields
- existing event taxonomy/registry refs when available
- known canonical event refs for dedup checks

## Event Clocks

Preserve clocks separately. Do not collapse them into one `event_time`.

- `awareness_time`: when the event/catalyst could be known to exist
- `scheduled_time`: expected future release/meeting/report window, if known
- `published_time`: source-published timestamp
- `available_time`: when this system could use the artifact point-in-time
- `interpretation_time`: when the standardized artifact is produced
- `resolution_time`: when delayed outcome/result becomes known, if applicable
- `event_interval`: start/end for regimes or multi-stage intervals
- `reaction_window`: evaluation-only metadata; never an inference input

## Lifecycle Classes

Use stable lifecycle classes:

- `scheduled_known_outcome_later`
- `scheduled_recurring_data_release`
- `unscheduled_surprise`
- `multi_stage_developing_event`
- `persistent_event_regime`
- `abnormal_activity_bridge`
- `narrative_residual`
- `unclassified_event`

## Standardized Fields

Produce JSON-compatible `event_interpretation` content with at least:

```text
schema_version
policy_version
source_artifact_ref
source_artifact_hash
source_name
source_type
published_time
available_time
interpreted_at
interpreter_agent_id
interpreter_model_id
normalized_event_type
event_family_ref
event_domain_tags
lifecycle_class
affected_scope
affected_entities
semantic_valence_score
materiality_score
evidence_uncertainty_score
novelty_score
source_quality_score
evidence_confidence_score
canonical_relation
rationale_summary
evidence_spans
review_status
standardization_status
```

`semantic_valence_score` is factual event valence for the affected entity/scope, not predicted price direction. Use `0` when factual valence is ambiguous, mixed, or not meaningful.

## Score Anchors

- `semantic_valence_score`: `-1.0` factually adverse, `0.0` neutral/unclear/mixed, `+1.0` factually favorable. This is not alpha and not market-impact direction.
- `materiality_score`: `0.0` negligible, `0.5` material but ordinary, `1.0` severe or transformational.
- `evidence_uncertainty_score`: `0.0` highly certain official fact, `0.5` incomplete/mixed evidence, `1.0` rumor/contradictory/opaque.
- `novelty_score`: `0.0` duplicate/recap, `0.5` meaningful update, `1.0` new material information.
- `source_quality_score`: primary/official sources highest; high-quality journalism next; syndication/aggregation/rumor lower.
- `evidence_confidence_score`: confidence that interpretation follows from evidence spans, not confidence that a trade will work.

## Workflow

1. Load raw artifact and metadata.
2. Verify point-in-time clocks and source provenance.
3. Extract evidence spans for every material claim.
4. Classify lifecycle, event family, normalized type, affected scope/entities, and canonical relation.
5. Fill standardized fields and score anchors.
6. Mark unknown/high-impact/low-confidence cases for review.
7. Validate forbidden fields are absent.
8. Return or save the immutable standardized event artifact according to the calling workflow.

## Unknown Event Standard Protocol

When no accepted type fits:

- set `normalized_event_type = "unclassified_event"`
- use broad `event_domain_tags`
- set `standardization_status = "proposed_standard"`
- propose a reusable `proposed_event_type` only if evidence supports it
- include inclusion/exclusion rationale, clock rules, scope hints, and examples
- require `event-taxonomy-standard-review` before registration

## Canonical and Residual Handling

If a raw artifact covers an already represented canonical event, do not duplicate the factual event. Link through `canonical_relation`.

Covered news may still produce narrative residual fields when supported by evidence, but those residuals remain event context, not market-impact predictions.

## Hard Prohibitions

Never output:

- `impact_direction`
- `expected_return`
- `signed_impact_distribution`
- `impact_function_projection`
- `conditional_effect_projection`
- `half_life`
- `amplitude`
- `utility_delta`
- buy/sell/hold advice
- option contract/strike/DTE/Greeks selection
- order routing or broker/account mutation
- post-event outcome labels as inference facts

## Downstream Boundary

- `event-taxonomy-standard-review` approves reusable event standards.
- `regime-interval-review` approves persistent event-regime intervals.
- `event-family-modelability-review` decides projection mode and probability-function class.
- M03 trains parameters and emits `event_state_projection` using point-in-time, fold-frozen evidence.

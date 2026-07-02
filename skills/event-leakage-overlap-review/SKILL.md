---
name: "event-leakage-overlap-review"
description: "Audit event-model PIT leakage and feature overlap."
---

# Event Leakage Overlap Review

Use this Codex skill when an agent must audit event-model evidence, labels, training packets, modelability packets, or projection artifacts for point-in-time leakage, downstream selected-path contamination, or feature/label overlap.

This is a safety and audit skill. It does not approve probability-function parameters, signed impact, alpha, trade direction, position sizing, option expression, or execution.

## Core Boundary

Event-model layers must not be defined by downstream selected trades, future labels, post-hoc event revisions, or overlapping upstream features.

The review checks whether an artifact is safe to use for:

- event interpretation
- event taxonomy review
- regime interval review
- event-family modelability review
- M03 training/evaluation
- projection compliance review

It may block or defer unsafe artifacts. It must not tune models or predict impact.

## Required Inputs

- artifact refs and schema refs
- source evidence refs and point-in-time clocks
- event row unit: event, event update, regime interval, episode node, context flag
- proposed training/evaluation label construction
- fold IDs, embargo/purge policy, and training/validation/test split evidence
- feature lineage and upstream model-feature overlap evidence
- selected trade/path contamination check
- downstream consumer and proposed model use
- known confounders and concurrent events/regimes
- prior review refs if available

## Review Workflow

1. Verify point-in-time clocks.
   - All inference features must be visible before the model decision time.
   - Future market reaction, later news revisions, and later outcome labels must be labels/evaluation only.

2. Verify row-unit integrity.
   - M01/M02/M03 upstream rows must not be filtered by selected trades or later action paths.
   - M03 event rows must come from event pool units, not time x target selected-path substitutes.

3. Check selected-path contamination.
   - Early event-model layers cannot be trained only on ultimately selected trades unless the task is explicitly selected-path evaluation and clearly labeled.

4. Check feature overlap.
   - Identify overlap with M01 background, M02 target context, M03 event interpretation, M04 decision, M05 option/liquidity, and labels.
   - Require residual-after-conditioning evidence when overlap is expected.

5. Check label and fold safety.
   - Labels must be fixed-horizon or otherwise predeclared.
   - Do not choose windows after seeing the strongest outcome.
   - Apply purge/embargo for overlapping horizons and event clusters.

6. Decide pass/defer/reject.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "event_leakage_overlap_review",
  "subject_ref": "string",
  "decision": "pass|defer|reject|insufficient_evidence",
  "pit_status": "passed|failed|insufficient_evidence",
  "row_unit_status": "passed|failed|insufficient_evidence",
  "selected_path_contamination_status": "passed|failed|not_applicable|insufficient_evidence",
  "feature_overlap_status": "low|controlled|high|failed|insufficient_evidence",
  "label_safety_status": "passed|failed|not_applicable|insufficient_evidence",
  "fold_safety_status": "passed|failed|not_applicable|insufficient_evidence",
  "overlap_sources": ["string"],
  "blocked_model_use": ["string"],
  "allowed_next_reviews": ["event_taxonomy_standard_review", "regime_interval_review", "event_family_modelability_review", "event_context_projection_review"],
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

## Decision Rules

- `pass`: PIT, row unit, contamination, overlap, label, and fold safety are adequate for the proposed next review.
- `defer`: plausible but missing safety evidence.
- `reject`: known leakage, selected-path contamination, post-hoc label construction, uncontrolled overlap, or invalid row unit.
- `insufficient_evidence`: required evidence is absent.

## Non-Negotiable Boundaries

- Do not allow downstream selected trades to define upstream event rows.
- Do not allow future event revisions as inference features.
- Do not allow realized outcomes as M06 modelability input except as predeclared training/evaluation labels.
- Do not allow window selection after observing best performance.
- Do not output signed impact, probability-function parameters, utility, alpha, or trade instructions.

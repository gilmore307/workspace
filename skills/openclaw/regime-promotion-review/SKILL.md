---
name: "regime-promotion-review"
description: "Review persistent event-regime interval governance."
---

# Regime Interval Review

Use this Codex skill when repeated or persistent event evidence may become, update, decay, or retire a `persistent_event_regime` interval in the event observation pool.

This skill governs regime interval identity and lifecycle. It does not approve production model conditioning, impact distribution parameters, alpha, trade direction, position sizing, option selection, or execution.

## Core Boundary

A persistent regime is an event-pool observation with interval state, not a permanent vague risk overlay.

The review decides whether evidence supports a regime row and its current lifecycle state:

- active
- shadow_active
- decaying
- stale
- resolved
- rejected/noise

It does not decide signed market impact or probability-function parameters. `event-family-modelability-review` handles probability-function class and projection mode if the regime family later becomes a modeling candidate.

## Required Inputs

If required evidence is missing, return `insufficient_evidence` or `defer`.

- candidate regime ref and topic key
- topic/entities/keywords and inclusion/exclusion rules
- first seen time, last seen time, candidate interval, and point-in-time source clocks
- representative evidence refs and source-quality summary
- source count, high-quality source count, source diversity, and update cadence
- affected scope hint: global, sector/theme, peer/index basket, target-local, or unknown
- duplicate/overlap check against active, decaying, stale, and resolved regimes
- proposed regime status and interval boundary rationale
- material update rule
- decay/staleness rule
- resolution/end rule if applicable
- known confounders, co-events, competing explanations, and canonical event links
- proposed downstream observation use and blocked uses

## Review Workflow

1. Validate point-in-time integrity.
   - Evidence must be visible before proposed `available_time`.
   - Later resolutions and market reactions cannot be used as inference facts.

2. Decide whether the topic is persistent.
   - Repeated evidence spans more than a single headline burst.
   - Topic/entity cluster is coherent.
   - Sources are sufficiently diverse or authoritative.
   - The regime has a plausible continuing event mechanism.

3. Check scope and duplicate coverage.
   - Identify affected scope without overbroad routing.
   - Merge or reject duplicate coverage of existing regimes.
   - Mark uncertain scope as review-required.

4. Require lifecycle rules.
   - Start rule.
   - Active/shadow/decay/stale/resolved state.
   - Material update rule.
   - Decay/staleness review rule.
   - Resolution/end rule when applicable.

5. Decide event-pool eligibility.
   - The output may allow global or focused event-pool observation use.
   - It must not approve M03 training or signed impact projection by itself.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "regime_interval_review",
  "candidate_regime_ref": "string",
  "topic_key": "string",
  "decision": "approve|defer|reject|insufficient_evidence",
  "regime_family": "string|null",
  "regime_status": "active|shadow_active|decaying|stale|resolved|candidate|unknown",
  "pit_status": "passed|failed|insufficient_evidence",
  "persistence_status": "passed|failed|insufficient_evidence",
  "source_quality_status": "passed|failed|insufficient_evidence",
  "scope_status": "passed|review_required|failed|insufficient_evidence",
  "duplicate_status": "unique|merge_with_existing|duplicate|insufficient_evidence",
  "interval_rule_status": "passed|failed|insufficient_evidence",
  "decay_rule_status": "passed|failed|insufficient_evidence",
  "allowed_observation_use": ["global_event_pool", "focused_event_pool", "event_family_modelability_candidate"],
  "blocked_model_use": [
    "production_m03_projection",
    "signed_impact_distribution",
    "probability_function_parameter",
    "alpha_direction",
    "trade_decision",
    "position_sizing",
    "execution"
  ],
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

## Decision Rules

- `approve`: create/update regime interval observation with explicit lifecycle rules.
- `defer`: plausible regime, but interval/scope/source/decay evidence is incomplete.
- `reject`: short-lived cluster, duplicate, noise, no persistent mechanism, or PIT failure.
- `insufficient_evidence`: required evidence is absent.

## Non-Negotiable Boundaries

- Same-day news is not required after a regime is active, but staleness/decay must be explicit.
- Do not approve permanent background risk without decay/staleness review.
- Do not output signed impact, utility, alpha, or trade instructions.
- Do not treat regime interval approval as M03 projection approval.

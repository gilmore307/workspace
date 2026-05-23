---
name: regime-promotion-review
description: Review high-frequency news-topic evidence before it can be promoted into a persistent event regime in the global event observation pool. Use when an agent judges candidate_regime packets, regime interval status, active/shadow/decay rules, or whether repeated news coverage represents a true persistent market-risk regime rather than a short-lived cluster, duplicate coverage, or noise.
---

# Regime Promotion Review

Use this skill before a repeated news topic can become a `persistent_event_regime` observation. The review decides whether the topic deserves interval status in the global event observation pool. It does not approve Layer 4 training, alpha, trade direction, position sizing, or execution.

## Non-Negotiable Boundaries

- High news frequency alone is insufficient.
- Same-day news is not required after a regime is active, but the active/shadow/decay state must be point-in-time and evidence-backed.
- A regime must have a clear interval, affected scope, material-update rule, and decay/staleness rule.
- Do not duplicate an existing regime. Merge or mark duplicate coverage when topic/entity evidence overlaps an active regime.
- Do not promote a short-lived headline cluster into a regime.
- Do not approve permanent background risk without an explicit decay or staleness review.
- Do not output buy/sell advice, alpha direction, position sizing, option selection, broker/account actions, or Layer 4 promotion.

## Required Inputs

If any required input is missing, return `insufficient_evidence` or `defer` instead of guessing:

- `candidate_regime_ref` and topic key
- topic/entities/keywords and inclusion/exclusion rules
- first seen time, last seen time, candidate interval, and point-in-time source clocks
- source count, high-quality source count, source diversity, and representative evidence refs
- topic frequency, persistence, and acceleration evidence
- affected scope hint: market/global, sector/theme, peer/index basket, target-local, or unknown
- duplicate/overlap check against active and stale regimes
- proposed `regime_status`: `active`, `shadow_active`, `decaying`, `stale`, or `resolved`
- material update rule and decay/staleness rule
- known confounders, co-events, and competing explanations
- proposed downstream use: global observation only, Layer 10 attribution candidate, or review-required

## Review Workflow

1. Validate point-in-time integrity:
   - evidence was visible before the proposed `available_time`
   - later resolutions or market reactions are not used as inference facts
   - source timestamps and retrieval clocks are preserved

2. Decide whether the topic is persistent:
   - repeated coverage spans more than a single headline burst
   - entity/topic cluster is coherent
   - coverage comes from sufficiently diverse or high-quality sources
   - the topic has a plausible continuing market-risk mechanism

3. Check scope and duplicate coverage:
   - identify affected market/sector/theme/peer/target scopes
   - reject or merge duplicate coverage of an existing regime
   - mark uncertain scope as review-required rather than overbroad

4. Require lifecycle rules:
   - explicit start rule
   - current active/shadow/decay/stale state
   - material update rule
   - decay/staleness review rule
   - resolution/end rule when applicable

5. Decide output:
   - `approve`: create or update a `persistent_event_regime` row in the global event observation pool
   - `defer`: plausible, but missing interval/scope/decay/source evidence
   - `reject`: short-lived cluster, duplicate, noise, no persistent mechanism, or failed PIT integrity
   - `insufficient_evidence`: required evidence is absent

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "regime_promotion_review",
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
  "decay_rule_status": "passed|failed|insufficient_evidence",
  "allowed_observation_use": ["global_event_pool", "layer_10_attribution_candidate"],
  "blocked_model_use": ["layer_4_training", "alpha_direction", "trade_decision", "position_sizing", "execution"],
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

`approve` means the topic may become or update a `persistent_event_regime` observation. It does not mean Layer 10 has proven failure attribution or that Layer 4 may train on the regime.

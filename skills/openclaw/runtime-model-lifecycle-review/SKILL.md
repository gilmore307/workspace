---
name: runtime-model-lifecycle-review
description: Review execution-owned active/shadow model lifecycle evidence after a market-hours shadow cycle. Use when an agent is asked to recommend active, realtime-candidate, shadow-only, or eliminate-candidate roles from live/shadow performance evidence.
---

# Runtime Model Lifecycle Review

Use this skill only after a market-hours shadow cycle has mature evidence. The agent produces a blinded roster recommendation; deterministic execution code maps anonymous labels to model refs and writes any active pointer gate.

## Non-Negotiable Boundaries

- Do not train models, change promotion readiness, call providers, construct orders, submit broker calls, mutate accounts, or write active config pointers.
- The active model remains the trading authority until an explicit execution active-pointer write gate passes.
- Selection and pointer mutation are separate audit surfaces.
- Model comparison must be anonymous. The agent must not know which model is current active, newly promoted, older, incumbent, champion, or challenger.

## Required Inputs

Return `insufficient_evidence` if any required input is missing:

- cycle id, market window, instrument universe, and cost/slippage assumptions
- anonymous model labels and blinded performance rows for the same cycle
- live/shadow decision effectiveness metrics by total period and relevant regime segment
- risk, tail-loss, drawdown, turnover, latency, capacity, and operational-health evidence
- evidence maturity checks showing the cycle is complete enough for review
- prior eliminate-candidate history if retirement is being considered

## Review Workflow

1. Validate evidence integrity: same window, same market data basis, same cost model, complete enough sample, no obvious leakage or missing latency/capacity facts.
2. Check identity blinding. If labels reveal active/new/old status, return `deferred` with `identity_blinding_status = failed`.
3. Compare the metric vector, not a single score: decision effectiveness, risk-adjusted result, drawdown, tail loss, cost sensitivity, turnover, regime stability, and operational reliability.
4. Recommend one anonymous label for active only when superiority is material and robust.
5. Recommend ranks 2-4 as realtime candidates when useful for ongoing comparison and runtime capacity permits.
6. Put weak models into eliminate-candidate status only with concrete reason evidence. A single weak cycle is normally not enough to retire a model.
7. If differences are ambiguous, preserve current role mapping through deterministic execution policy rather than inventing a switch.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "runtime_model_lifecycle_review",
  "cycle_id": "string",
  "identity_blinding_status": "passed|failed|insufficient_evidence",
  "recommendation": "select_active|keep_current_roles|defer|insufficient_evidence",
  "selected_active_label": "string|null",
  "realtime_candidate_labels": ["string"],
  "shadow_only_labels": ["string"],
  "eliminate_candidate_labels": ["string"],
  "retirement_candidate_labels": ["string"],
  "confidence": "low|medium|high",
  "blocking_issues": ["string"],
  "material_strengths": ["string"],
  "material_risks": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```


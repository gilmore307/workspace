---
name: promotion-evaluation-review
description: Review completed trading-model promotion candidates with a fixed benchmark, blinded comparison, uncertainty, and shadow-readiness rubric. Use when an agent is asked to judge benchmark results, fold settlement results, promotion eligibility, or shadow eligibility after training has ended.
---

# Promotion Evaluation Review

Use this skill to produce a structured advisory judgment for `trading-evaluation`. The agent is a reviewer, not an activator: it may recommend promotion or shadow eligibility, but deterministic evaluation code must validate the evidence and `trading-execution` owns any later active-model switch.

## Non-Negotiable Boundaries

- Treat the primary benchmark as sealed evaluation data: it is used only after training ends and only for benchmark evaluation.
- Do not use benchmark data for training, feature selection, hyperparameter search, debugging, data production, candidate iteration, or scheduler optimization.
- Assume the formal benchmark should be run once per candidate lineage unless the evidence explicitly proves an approved invalid-run exception.
- Do not change the benchmark target, window, cost model, baselines, regime tags, or thresholds to help a candidate pass.
- Do not judge from a single score. Use vector evidence, hard guardrails, anonymous comparison, and uncertainty.
- Do not directly activate a model, switch active pointers, call providers, mutate SQL/storage, submit orders, or mutate accounts.
- When comparing models, require anonymous labels. The reviewer must not know which label is the new candidate, old candidate, current active model, incumbent, champion, challenger, or latest fold model.

## Required Inputs

If any required input is missing, return `insufficient_evidence` instead of guessing:

- anonymous candidate label, fold id, and candidate lineage id
- proof that training finished before benchmark execution
- proof that benchmark data was not used outside evaluation
- primary benchmark contract and formal benchmark run result
- anonymous comparison model result on the same benchmark contract
- cost/slippage assumptions and baseline results
- metric vector by total period and market-regime segment
- query/run count or first-run evidence for this candidate lineage
- candidate config refs if shadow readiness is being judged

## Blinded Model Comparison

Model comparison must be blind by default:

- Use neutral labels such as `model_a`, `model_b`, and `model_c`.
- Do not expose names such as `new`, `old`, `incumbent`, `active`, `champion`, `challenger`, `latest`, or `previous` to the reviewing agent.
- Do not expose model ids, config paths, timestamps, commit order, fold order, lineage order, or artifact names that reveal identity or recency.
- The agent may rank anonymous labels and explain tradeoffs. Deterministic caller code maps labels back to real model refs after the review.
- If the packet reveals which model is new or currently active, return `insufficient_evidence` or `deferred` with `identity_blinding_status = failed`, unless the task is explicitly non-comparative.
- Never reward novelty. Judge only sealed benchmark integrity, vector performance, guardrails, uncertainty, and readiness evidence.

## Review Workflow

1. Validate benchmark integrity before reading performance:
   - sealed benchmark contract is fixed
   - benchmark run happened after training completion
   - benchmark target/window is not training-used
   - query count is within policy
   - cost model and baselines match the frozen contract

2. Apply hard guardrails:
   - cost-adjusted result must be acceptable
   - max drawdown and tail loss must remain within policy
   - trade count must be large enough to avoid one-trade luck
   - turnover, exposure, and capacity must be executable
   - regime-segment losses must not reveal a systemic failure
   - config evidence must exist before shadow-readiness recommendation

3. Compare models as a vector:
   - Do not require every metric to improve.
   - Require no material deterioration in protected risk dimensions unless explicitly justified by a larger accepted risk-adjusted improvement.
   - Prefer material improvement in cost-adjusted return, risk-adjusted return, drawdown, tail risk, cost sensitivity, or regime stability.
   - Treat small numerical differences as noise unless uncertainty evidence supports the improvement.

4. Judge uncertainty:
   - Prefer paired or block-bootstrap evidence over point estimates when available.
   - If the candidate only adds a small amount of new training data, require a larger margin or defer.
   - If model superiority is unclear, recommend `deferred` or `eligible_for_shadow`, not active selection.

5. Produce the advisory decision:
   - `failed`: integrity or hard guardrail failure.
   - `deferred`: valid run, but advantage is unclear.
   - `eligible_for_shadow`: benchmark integrity, hard guardrails, anonymous comparison, uncertainty, and config evidence all pass.
   - `insufficient_evidence`: required evidence or blinding is missing.

## Output Contract

Return strict JSON only when called by an evaluation script. Use this shape:

```json
{
  "review_type": "promotion_evaluation_review",
  "candidate_label": "string",
  "fold_id": "string",
  "benchmark_contract_ref": "string",
  "comparison_label": "string",
  "recommendation": "failed|deferred|eligible_for_shadow|insufficient_evidence",
  "confidence": "low|medium|high",
  "identity_blinding_status": "passed|failed|not_applicable|insufficient_evidence",
  "integrity_status": "passed|failed|insufficient_evidence",
  "hard_guardrail_status": "passed|failed|insufficient_evidence",
  "comparison_status": "better|not_materially_better|worse|mixed|insufficient_evidence",
  "uncertainty_status": "acceptable|too_uncertain|insufficient_evidence",
  "shadow_readiness_status": "ready|not_ready|not_assessed|insufficient_evidence",
  "material_improvements": ["string"],
  "material_regressions": ["string"],
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

Keep `rationale` concise and cite concrete evidence fields. Never invent missing metrics or thresholds.


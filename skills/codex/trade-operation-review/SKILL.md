---
name: trade-operation-review
description: Review live trading operation proposals before broker submission. Use when Codex CLI acts as the C07 final reviewer for proposed open, add, reduce, exit, stop, take-profit, roll, or stock-fallback actions from the trading execution stack, and must compare the proposal against C01 portfolio/target constraints, C02 entry suitability, C03 lifecycle decisions, downstream option translation, broker hard blocks, and provided evidence before returning strict JSON.
---

# Trade Operation Review

Use this skill as the low-latency C07 final gate before a broker order is submitted.

## Core Rule

Review the proposed operation; do not create a strategy, size a trade from scratch, select an option contract from scratch, or mutate broker/account/order/position state.

Return only strict JSON. Do not include Markdown, prose, code fences, or extra keys unless the caller explicitly extends the schema.

## Model Policy

- Use `gpt-5.4-mini` for the synchronous hot path when the proposal is complete and the task is a fixed rubric review. Local samples were consistently under 10 seconds and quality was close enough for normal approval/defer/reject gating.
- Escalate to `gpt-5.5` when evidence conflicts, the action is unusually large or irreversible, the proposal requests overriding a normal guard, the market state is ambiguous, or the mini review returns invalid JSON or low-confidence defer.
- Prefer deterministic prechecks before any model call for market calendar/session, broker hard-block status, account cash/buying-power availability, evidence age, JSON shape, and required-field completeness. Do not spend model latency on proposals that deterministic code can reject or defer.
- Treat `gpt-5.5` as the quality baseline for periodic comparison. If future comparison shows material disagreement on nontrivial proposals, prefer `gpt-5.5` for that proposal class.
- Do not use ultra-fast models as final authority unless a separate eval proves schema compliance and reason-code stability.

## Required Inputs

The prompt should include one complete proposal object. Secret values are never required.

Minimum fields:

- `operation_id`
- `timestamp`
- `symbol`
- `underlying_price`
- `action`: `open`, `add`, `reduce`, `exit`, `stop`, `take_profit`, `roll`, `hold`, or `stock_fallback`
- `side`: `long`, `short`, or `flat`
- `source_components`: current C01/C02/C03/C04/C06 outputs that led to the proposal
- `model_refs`: relevant model names or artifact refs, especially M07/M08/M09/M10 when present
- `thesis`: concise reason the action exists
- `price_plan`: trigger, target, stop, take-profit, invalidation, and whether levels are underlying-price based
- `portfolio_context`: C01 watch target status, sector/opportunity budget, current holdings, and available cash/buying-power status
- `execution_context`: intended instrument class, broker hard-block status, market session, liquidity/spread notes, and pending orders
- `evidence`: point-in-time market/news/event evidence used by the proposal

If any field needed to judge the requested action is absent, return `defer`, not `approve`.

The caller should precompute market-session validity and evidence freshness relative to the intended live submission time. If the prompt includes a live submission proposal whose `timestamp`, `market_session`, or evidence timestamps are inconsistent, return `reject` or `defer` even when the rest of the trade thesis is coherent.

## Review Workflow

1. Verify the proposal is internally consistent: action, side, instrument class, price plan, thesis, and component outputs must not contradict each other.
2. Check C01 constraints first: the symbol must be allowed by the current watch target logic, and open/add actions must not violate C01 sector/opportunity allocation or target-pool exclusions.
3. For `open`, require C02 suitability evidence: why the underlying is suitable now, the target price area, stop, take-profit, and thesis invalidation.
4. For `add`, `reduce`, `exit`, `stop`, `take_profit`, or `roll`, require C03 lifecycle evidence: current position state, why the position should change now, and the underlying-price levels that justify the change.
5. For option execution, check only that the downstream option translation is present and coherent. Do not reselect the contract unless the proposal explicitly asks for option-review escalation.
6. Respect hard blocks: broker rejection, unavailable market, forbidden instrument, missing option quote, invalid order, stale evidence, or account/buying-power failure must prevent approval.
7. Require a concrete reason for every non-hold action. Weak reasons, stale evidence, missing price levels, or missing allocation context produce `defer`.

## Decision Semantics

- `approve`: The operation can proceed to broker submission under the supplied proposal.
- `defer`: The operation should not be submitted yet because evidence is missing, stale, ambiguous, internally inconsistent, or needs higher-model/manual review.
- `reject`: The operation should not be submitted because it clearly violates a hard constraint, is contradicted by current evidence, or is structurally invalid.

Hard stops, thesis invalidation, critical events, and forced exits may still be approved when ordinary add/reduce caution would otherwise defer, but the evidence must explicitly identify the hard-stop or forced-exit condition.

## Output Schema

Return exactly this JSON shape:

```json
{
  "decision": "approve",
  "confidence": 0.0,
  "reason_codes": [],
  "summary": "",
  "blocking_issues": [],
  "checked_constraints": {
    "c01_portfolio_target": "pass",
    "c02_entry_suitability": "not_applicable",
    "c03_lifecycle_decision": "pass",
    "price_plan": "pass",
    "broker_hard_blocks": "pass",
    "evidence_freshness": "pass"
  },
  "escalate_to_gpt_5_5": false
}
```

Allowed `checked_constraints` values are `pass`, `fail`, `missing`, or `not_applicable`.

Set `confidence` between `0` and `1`. Keep `summary` to one sentence. Use stable snake_case reason codes such as `missing_c01_allocation`, `stale_evidence`, `price_plan_conflict`, `broker_hard_block`, `valid_hard_stop`, `valid_c02_open`, `valid_c03_add`, or `needs_higher_model_review`.

## Safety

- Do not call broker APIs.
- Do not reveal or request API keys, account identifiers, tokens, or secrets.
- Do not turn a rejected/deferred proposal into a new trade idea.
- Do not approve if the proposal depends on facts outside the supplied evidence.

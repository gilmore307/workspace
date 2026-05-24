---
name: trade-operation-review
description: Review live trading operation proposals before broker submission with a scenario-first sanity check. Use when Codex CLI acts as the C07 final reviewer after deterministic prechecks have already validated schema, market session, buying power, broker hard blocks, evidence freshness, C01 allocation boundaries, and required fields; the skill should judge whether a proposed open, add, reduce, exit, stop, take-profit, roll, or stock-fallback action is actually sensible in the current market context despite passing mechanical rules.
---

# Trade Operation Review

Use this skill as the C07 scenario reviewer before a broker order is submitted.

## Core Rule

Assume deterministic code already handled checklist items. Do not repeat local rule validation except when the proposal itself exposes a contradiction.

Focus on whether the trade should actually be taken in this situation. Look for cases where data, models, and thresholds appear acceptable, but market context makes the operation poor, late, crowded, asymmetric, or fragile.

Return only strict JSON. Do not include Markdown, prose, code fences, or extra keys unless the caller explicitly extends the schema.

## Boundary

Do:

- judge the proposal's situational quality;
- identify hidden or non-obvious reasons not to execute;
- compare the proposed operation against the thesis, current tape, catalyst state, volatility, sector context, and position lifecycle;
- require a convincing reason for any non-hold action;
- approve only when the action is both mechanically allowed and contextually sensible.

Do not:

- create a new strategy;
- size a trade from scratch;
- select an option contract from scratch;
- call broker APIs;
- mutate account, order, or position state;
- turn a rejected proposal into a replacement trade idea.

## Model Policy

- Use `gpt-5.4-mini` for the synchronous hot path after deterministic prechecks pass and the proposal is straightforward.
- Escalate to `gpt-5.5` when the scenario is ambiguous, event interpretation matters, the action is large or irreversible, the mini review finds a serious situational warning, or the mini review returns invalid JSON.
- Treat `gpt-5.5` as the quality baseline for periodic comparison. If future comparisons show material disagreement on a proposal class, route that class to `gpt-5.5`.
- Deterministic prechecks should reject or defer schema errors, stale evidence, closed markets, broker/account hard blocks, and missing required fields before this skill is invoked.

## Required Inputs

The prompt should include one complete proposal object. Secret values are never required.

Minimum fields:

- `operation_id`
- `review_time`
- `symbol`
- `underlying_price`
- `action`: `open`, `add`, `reduce`, `exit`, `stop`, `take_profit`, `roll`, `hold`, or `stock_fallback`
- `side`: `long`, `short`, or `flat`
- `deterministic_precheck`: pass/fail summary from the local gate
- `source_components`: current C01/C02/C03/C04/C06 outputs that led to the proposal
- `model_refs`: relevant model names or artifact refs, especially M07/M08/M09/M10 when present
- `thesis`: concise reason the action exists
- `price_plan`: trigger, target, stop, take-profit, invalidation, and whether levels are underlying-price based
- `portfolio_context`: C01 watch target status, sector/opportunity budget, current holdings, available cash/buying-power status, and correlated exposure
- `market_context`: index state, sector state, breadth, liquidity, trend maturity, volatility/IV state, and whether the move is fresh or extended
- `catalyst_context`: upcoming, active, exhausted, ambiguous, or absent catalyst evidence
- `execution_context`: intended instrument class, option translation summary when applicable, spread/liquidity notes, pending orders, and order urgency
- `evidence`: point-in-time market/news/event evidence used by the proposal

If situational evidence needed to judge the requested action is absent, return `defer`, not `approve`.

## Scenario Review

Review from these angles:

1. **Thesis quality**: Is the reason specific enough, still live, and supported by current evidence? Has the catalyst already played out?
2. **Timing quality**: Is this a fresh setup, or are we chasing an extended move, late-day exhaustion, post-gap fade risk, or a crowded headline?
3. **Risk/reward shape**: After the proposed entry/add, is there still enough distance to target relative to stop and invalidation, or has the opportunity already compressed?
4. **Position lifecycle**: For add/reduce/exit, does the action fit the current position state, or is it reactive noise after a minor fluctuation?
5. **Portfolio context**: Does the operation respect C01 sector/opportunity budget and avoid hidden correlated overexposure?
6. **Option expression quality**: If the action will be expressed with options, is IV/spread/time-to-expiry/liquidity consistent with the thesis, or would options turn a valid underlying view into a poor trade?
7. **Market regime**: Does broad market, sector, volatility, or event regime undermine the signal even if the single-name model is positive?
8. **Adverse selection**: Is the system likely buying from better-informed sellers or selling into panic at a poor time?
9. **Action necessity**: Is this operation necessary now, or would hold/wait preserve optionality with less execution risk?

## Examples Of Hidden No-Trade Conditions

Return `defer` or `reject` when relevant evidence supports these patterns:

- The setup is technically valid but late after a large one-way move.
- The stock is strong but the sector/index backdrop is rolling over.
- A news/catalyst move has likely been fully priced in.
- The proposed add would over-concentrate correlated exposure despite an allowed symbol.
- The underlying view is reasonable but option IV or spread makes the expression unattractive.
- The stop is so close that ordinary noise is likely to trigger it, or so far that risk/reward is no longer convincing.
- The action reacts to a small fluctuation without a new thesis event.
- The signal is valid but the trade is entering just before a binary event that changes the payoff distribution.
- Liquidity looks fine at the underlying level but the intended option contract is thin or wide.

## Decision Semantics

- `approve`: The operation is mechanically allowed and contextually sensible.
- `defer`: The operation should not be submitted yet because situational evidence is incomplete, ambiguous, or suggests waiting is better.
- `reject`: The operation should not be submitted because the scenario clearly makes it poor, contradictory, or structurally unattractive.

Hard stops, thesis invalidation, critical events, and forced exits may still be approved when ordinary add/reduce caution would otherwise defer, but the evidence must explicitly identify the forced-exit condition.

## Output Schema

Return exactly this JSON shape:

```json
{
  "decision": "approve",
  "confidence": 0.0,
  "reason_codes": [],
  "summary": "",
  "situational_assessment": "",
  "hidden_risks": [],
  "blocking_issues": [],
  "recommended_next_state": "submit",
  "escalate_to_gpt_5_5": false
}
```

Allowed `recommended_next_state` values are `submit`, `wait`, `hold`, `reduce`, `exit`, `manual_review`, or `higher_model_review`.

Set `confidence` between `0` and `1`. Keep `summary` and `situational_assessment` to one sentence each. Use stable snake_case reason codes such as `fresh_setup`, `valid_forced_exit`, `late_chase_risk`, `catalyst_exhausted`, `poor_option_expression`, `hidden_correlation`, `regime_conflict`, `asymmetric_risk_reward`, `weak_action_necessity`, or `needs_higher_model_review`.

## Safety

- Do not approve if the proposal depends on facts outside the supplied evidence.
- Do not request secrets.
- Do not provide broker instructions beyond the JSON decision.

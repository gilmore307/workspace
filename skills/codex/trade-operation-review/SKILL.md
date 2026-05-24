---
name: trade-operation-review
description: Review live trading operation proposals before broker submission as a missed-event guard. Use when Codex CLI acts as the C07 final reviewer after deterministic prechecks and upstream models have already handled schema, market session, buying power, broker hard blocks, C01 allocation boundaries, price plans, known event risk, and normal trade risk; the skill should verify that no important target-specific, sector, macro, regulatory, earnings, analyst, filing, halt, litigation, or other market-moving event appears missing from the proposal before returning strict JSON.
---

# Trade Operation Review

Use this skill as the C07 missed-event reviewer before a broker order is submitted.

## Core Rule

Assume deterministic code and upstream models already handled ordinary trade checks and already-known risks. Do not re-litigate the thesis, price plan, sizing, C01 allocation, or routine technical setup unless a missing or contradictory event changes them.

Focus on whether the proposal may be missing important current information about the symbol, its sector, its option chain, or the broader market that should block, delay, or escalate the operation.

Return only strict JSON. Do not include Markdown, prose, code fences, or extra keys unless the caller explicitly extends the schema.

## Boundary

Do:

- compare the proposal's event evidence against supplied latest news, filings, calendar, halt/status, analyst, sector, macro, and option-market context;
- identify material events that appear absent from the proposal or not interpreted by upstream models;
- detect stale event packets, missing event-source coverage, and contradictions between the proposal and newer evidence;
- ask for `defer` when the event search coverage is insufficient for a live order;
- approve when event coverage is current enough and no material missed event is found.

Do not:

- redo general strategy review;
- reject because of a known risk already explicitly included in the proposal;
- create a new trade idea;
- size a trade from scratch;
- select an option contract from scratch;
- call broker APIs or mutate account/order/position state.

## Model Policy

- Use `gpt-5.5` for all synchronous missed-event reviews.
- Do not route this skill through smaller models for the hot path. The added latency is acceptable for this gate, and the task benefits from stronger event interpretation and contradiction detection.
- Deterministic prechecks should reject or defer schema errors, stale market data, closed markets, broker/account hard blocks, and missing required fields before this skill is invoked.

## Required Inputs

The prompt should include one complete proposal object. Secret values are never required.

Minimum fields:

- `operation_id`
- `review_time`
- `symbol`
- `action`: `open`, `add`, `reduce`, `exit`, `stop`, `take_profit`, `roll`, `hold`, or `stock_fallback`
- `side`: `long`, `short`, or `flat`
- `deterministic_precheck`: pass/fail summary from the local gate
- `proposal_summary`: concise action, thesis, price plan, and intended expression
- `known_event_context`: events already consumed by C02/C03/M10 or other upstream models
- `event_search_coverage`: source names, time windows, last query timestamps, and whether coverage includes news, filings, earnings calendar, analyst actions, halt/status, macro calendar, sector news, and option-market anomalies
- `latest_event_candidates`: most recent raw or interpreted candidate events found by the live event scan
- `source_components`: current C01/C02/C03/C04/C06 outputs that led to the proposal
- `model_refs`: relevant model names or artifact refs, especially M10 when present
- `execution_context`: intended instrument class, option translation summary when applicable, pending orders, and order urgency

If `event_search_coverage` is missing or too narrow to support the order urgency, return `defer`.

## Missed-Event Review

Review only from the missed-information angle:

1. **Coverage sufficiency**: Did the live scan check the right sources for this symbol and action, with an appropriate time window?
2. **Target-specific events**: Are there unconsumed earnings, guidance, SEC filings, offering/buyback, insider, M&A, product, legal, regulatory, rating, analyst, halt, recall, cyber, management, or customer/vendor events?
3. **Sector and peer events**: Is there a fresh sector or close-peer event that changes the target's setup but is absent from the proposal?
4. **Macro and policy events**: Is there a live macro, Fed, Treasury, tariff, geopolitics, regulatory, or market-structure event that should alter execution?
5. **Option-market events**: For option trades, are there IV shocks, skew changes, liquidity breaks, unusual options flow, corporate actions, or expiry/calendar effects not reflected upstream?
6. **Contradictions**: Does any latest candidate event contradict the known thesis, price plan, or M10 event-risk state?
7. **Materiality**: Is the missed event important enough to block execution, require reinterpretation, or just annotate?

Do not mark a risk as missed if it is already clearly present in `known_event_context` and reflected in the proposal's decision.

## Decision Semantics

- `approve`: Event coverage is sufficient and no material missed event is found.
- `defer`: Event coverage is insufficient, event evidence is ambiguous, or a candidate event needs interpretation before broker submission.
- `reject`: A material missed event clearly invalidates or materially changes the proposed operation.

For hard stops, forced exits, or thesis invalidation exits, missed-event review should not delay execution unless the missing event changes whether the exit itself is valid or executable.

## Output Schema

Return exactly this JSON shape:

```json
{
  "decision": "approve",
  "confidence": 0.0,
  "reason_codes": [],
  "summary": "",
  "event_search_coverage": "sufficient",
  "missed_events": [],
  "information_gaps": [],
  "blocking_issues": [],
  "recommended_next_state": "submit",
  "escalate_to_gpt_5_5": false
}
```

Allowed `event_search_coverage` values are `sufficient`, `partial`, `insufficient`, or `contradictory`.

Allowed `recommended_next_state` values are `submit`, `wait_for_event_scan`, `reinterpret_event`, `manual_review`, `higher_model_review`, `hold`, or `do_not_submit`.

Set `confidence` between `0` and `1`. Keep `summary` to one sentence. Use stable snake_case reason codes such as `no_material_missed_event`, `insufficient_news_coverage`, `missing_filing_scan`, `unconsumed_earnings_event`, `fresh_analyst_action`, `fresh_regulatory_event`, `fresh_litigation_event`, `fresh_filing_event`, `fresh_halt_status`, `halt_status_unknown`, `sector_event_unconsumed`, `macro_event_unconsumed`, `option_market_event_unconsumed`, `contradictory_latest_event`, `material_unconsumed_event`, `known_event_already_accounted_for`, or `needs_higher_model_review`.

## Safety

- Do not approve if event coverage is too narrow for the action urgency.
- Do not request secrets.
- Do not provide broker instructions beyond the JSON decision.

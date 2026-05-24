---
name: event-interpretation
description: Standardize raw event artifacts such as news, SEC/financial filings, macro calendar releases, war, politics, regulation, financial-system stress, and previously unseen events into point-in-time event_interpretation_v1 artifacts before model generation. Use when an agent must interpret event content consistently, propose reusable standards for unknown event types, or validate that model inputs consume standardized interpreted events rather than raw text.
---

# Event Interpretation

Use this skill when raw event evidence must be interpreted for the trading stack before model generation.

## Core rule

The agent is not a trading decision maker. It is a conservative event-standardization worker.

It converts raw point-in-time artifacts into a fixed, validated `event_interpretation_v1` artifact. Models consume the artifact; they must not reinterpret raw news, filings, webpages, or transcripts during generation.

This layer is core system infrastructure, not equity-only plumbing. Keep standards reusable for later prediction-market expansion such as Polymarket: event definitions, evidence quality, uncertainty, narrative residuals, and scope routing should be outcome-agnostic enough to support securities, macro/sector models, and future event-probability markets.

## Hard boundaries

Never output or imply during event interpretation:

- ordinary buy/sell/hold alpha decisions;
- alpha confidence;
- option contract/strike/DTE/Greeks selection;
- order routing or broker/account mutation;
- post-event outcome labels as inference facts.

A later event-risk governor may emit bounded risk-intervention outputs, but those are not ordinary alpha decisions and must not directly mutate broker/account state. They must route through the accepted execution/risk-control boundary.

Always preserve point-in-time boundaries. Use only evidence visible at `available_time`. Future revisions, future market moves, and hindsight explanations are labels/evaluation material, not interpretation inputs.

## Event timing and lifecycle discipline

Do not flatten all events into a single `event_time`. Event interpretation must preserve whether the event was known in advance, when facts became observable, and when the market could first act on the interpreted evidence.

At minimum, distinguish these lifecycle classes:

```text
scheduled_known_outcome_later
unscheduled_surprise
scheduled_recurring_data_release
multi_stage_developing_event
persistent_event_regime
```

Core clock meanings:

```text
awareness_time        # when the system/human market could know an event/catalyst exists
scheduled_time        # expected release/meeting/report time or window, if known before outcome
published_time        # source-published timestamp when facts/results appear
available_time        # when the artifact became available to this system point-in-time
interpretation_time   # when standardized event_interpretation_v1 is produced
resolution_time       # when the relevant outcome is known, if delayed or multi-stage
reaction_window       # evaluation-only window for market/target response; never an input fact
```

Rules by class:

- `scheduled_known_outcome_later`: examples include earnings, FOMC/CPI/NFP calendars, FDA decision dates, court dates, known shareholder votes, or scheduled SEC/reporting events. The pre-event artifact may say a catalyst is coming, but actual/beat/miss/guidance/result fields must remain unknown until the release artifact is available. Train/evaluate pre-event risk, event-result interpretation, and post-event reaction as separate phases.
- `unscheduled_surprise`: examples include sudden news, accidents, lawsuits, regulatory raids, resignations, wars, sanctions, bank runs, or unexpected offerings. `awareness_time` usually equals first credible `published_time`/`available_time`. Do not pretend the specific event was forecastable; only background hazard or vulnerability priors may exist before it.
- `scheduled_recurring_data_release`: examples include macro releases and routine economic calendars. The event shell is known in advance; the result values, revisions, and surprise-vs-consensus are only valid after release.
- `multi_stage_developing_event`: examples include investigations, M&A, litigation, bankruptcy, geopolitical escalation, or policy negotiations. Preserve separate stage updates rather than collapsing the whole arc into the first headline.
- `persistent_event_regime`: examples include pandemic periods, tariff-war periods, sanctions regimes, geopolitical war/escalation periods, banking-system stress, and policy crisis windows. Preserve interval status, last material update, affected scope, and decay/staleness rules. Same-day news is not required once the regime is active, but the active/shadow/decay state must be point-in-time and evidence-backed.

Training implication: scheduled-known events and surprise events must not share the same label construction without an explicit lifecycle feature. A scheduled earnings calendar can influence pre-event exposure/risk before results; a sudden headline can only influence decisions after detection. Mixing them without lifecycle clocks causes leakage and distorted event-risk behavior.

## Required workflow

1. Load the raw artifact and metadata: source, captured time, published/accepted/release time, `available_time`, URL/path, raw hash, and provider/source identity.
2. Extract evidence spans. Every important claim must point to a quote, field, paragraph, table row, or structured datum.
3. Produce only `event_interpretation_v1` JSON-compatible content.
4. Validate schema, enum values, score ranges, required evidence spans, forbidden fields, and point-in-time clocks.
5. Mark low-confidence or high-impact interpretations for review instead of stretching evidence.
6. Save the immutable interpretation artifact with policy/schema/model/prompt/raw-hash audit metadata.
7. If the event does not fit existing standards, follow the unknown-event protocol below.

## `event_interpretation_v1` minimum shape

Required fields:

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
prompt_policy_hash
normalized_event_type
event_domain_tags
affected_scope
affected_entities
direction_bias_score
intensity_score
uncertainty_score
novelty_score
source_quality_score
evidence_confidence_score
canonical_relation
rationale_summary
evidence_spans
review_status
standardization_status
```

Recommended optional fields:

```text
proposed_event_type
proposed_domain_tags
proposed_standard_rationale
standard_reuse_key
conflict_notes
missing_evidence_notes
review_required_reason
```

## Score anchors

Use stable numeric ranges. Do not invent scale meanings per artifact.

- `direction_bias_score`: `-1.0` strongly adverse, `0.0` direction-neutral/unclear, `+1.0` strongly favorable for the affected entity/scope. This is event direction only, not alpha.
- `intensity_score`: `0.0` negligible, `0.5` material but ordinary, `1.0` severe/transformational.
- `uncertainty_score`: `0.0` highly certain official fact, `0.5` incomplete or mixed evidence, `1.0` rumor/contradictory/opaque.
- `novelty_score`: `0.0` duplicate/recap, `0.5` meaningful update, `1.0` new material information.
- `source_quality_score`: official/regulatory/primary sources outrank high-quality journalism; high-quality journalism outranks syndication/aggregation; weak or unattributed sources score low.
- `evidence_confidence_score`: confidence that the interpretation follows from the cited evidence, not confidence that a trade will work.

## Known-event handling

For structured sources such as SEC filings, earnings, macro releases, and official data:

- prefer structured fields over narrative guesswork;
- map known forms/metrics/events through accepted registry/docs vocabularies;
- use agent interpretation only for narrative context, materiality notes, uncertainty, and scope mapping;
- keep actual/consensus/previous/revision fields separate from subjective rationale.

For trading-calendar and market-structure events:

- treat them as scheduled event-risk candidates, not as ordinary clock features;
- preserve `scheduled_time`, `event_window`, `next_market_open_time`, `non_trading_interval_minutes`, `closure_type`, `closure_length_bucket`, `holiday_name`, `early_close_flag`, `pre_holiday_session_flag`, `expiry_window_flag`, `triple_witching_flag`, `index_rebalance_flag`, and certainty/source refs when available;
- default direction bias to neutral unless there is contemporaneous evidence for directional pressure;
- express risk through timing proximity, gap risk, liquidity-thinning/forced-flow prior, uncertainty, and impact scope rather than alpha direction.

For persistent event regimes:

- preserve `regime_family`, `regime_status`, `regime_start_time`, optional `regime_end_time`, `last_material_update_time`, `affected_scope`, `affected_entities`, `decay_rule_ref`, `staleness_review_time`, and evidence refs;
- distinguish a true regime from a short-lived news cluster, duplicate coverage, or noise through `regime-promotion-review`;
- preserve active/shadow/decay state even without same-day news, but never carry stale pressure without a decay or staleness rule.

For news:

- classify the concrete fact pattern, not the article genre;
- distinguish official announcement, primary interview, investigative report, market commentary, rumor, recap, and syndication;
- identify whether the article introduces new information or merely covers a canonical event;
- preserve market narrative and sentiment residuals even when the factual event is covered by a canonical source;
- cite evidence spans for all material claims;
- avoid sentiment-only labels unless no concrete event exists.

## Canonical coverage is not deletion

If a news item covers an already represented structured event, do not create a duplicate factual event. Set `canonical_relation.relation_type = "covered_by_canonical_event"` and point to the SEC, macro, rates, official disclosure, or other canonical event.

However, covered news may still carry independent interpretive value. Preserve it as a narrative/reaction residual when evidence supports it:

```text
market_narrative_type
market_reaction_summary
sentiment_direction_score
sentiment_intensity_score
narrative_surprise_score
narrative_conflict_score
residual_information_type
residual_information_claims
```

Examples:

- A weak earnings filing is canonical in SEC/earnings data, but credible news says investors are rewarding accelerated AI capex. The filing remains canonical; the news contributes a positive `market_narrative_type = "strategic_investment_reframing"` residual if evidence spans support it.
- A company reports acceptable numbers but sells off because guidance tone, margin mix, capital intensity, or positioning disappointed investors. The official report remains canonical; the news contributes negative narrative/reaction residuals.
- CPI/NFP recap news is usually covered by the official macro release. If it adds Fed-path interpretation from officials or market-implied policy repricing, that can become `related_followup` or a narrative residual, not a duplicate CPI event.
- Yield-curve or Treasury-yield news that only describes rate/ETF moves is covered by rates/ETF state evidence. If it identifies a new policy, credit, liquidity, or financial-stress interpretation, preserve that residual with evidence.

News residuals are event context, not alpha. They may influence event quality, uncertainty, direction bias, context alignment, and later event-risk intervention checks, but must not emit ordinary trading decisions.

## Abnormal-activity event discipline

Abnormal activity is not a second copy of bars, volume, spread, liquidity, volatility, gap, VWAP, trend, or target-state features already consumed by the base model stack. Treat it as residual/provenance evidence for event-risk interpretation.

Accepted abnormal-activity evidence categories:

```text
price_action_pattern
residual_market_structure_disturbance
microstructure_liquidity_disruption
option_derivatives_abnormality
```

Allowed examples:

- `price_action_pattern`: false breakout, failed breakdown, liquidity sweep high/low, bull trap, bear trap.
- `residual_market_structure_disturbance`: the target moves abnormally after conditioning on market, sector, peer, and target-state context; no visible canonical news/filing/macro artifact explains it yet.
- `microstructure_liquidity_disruption`: spread widens, quoted depth disappears, trading becomes one-sided, halt/pause/anomalous quoting appears, or liquidity quality degrades outside broad-market liquidity context.
- `option_derivatives_abnormality`: IV/skew/term-structure shock, unusual option volume, call/put imbalance, sweep/block evidence, OI change, or option liquidity disruption not already represented in the base option-expression inputs.

Forbidden examples:

- repeating raw/high return, volume, spread, liquidity, gap, VWAP distance, or trend fields as independent event alpha;
- treating every high z-score from already-modeled bars as a standalone event;
- using post-event realized price movement as an inference-time abnormality feature;
- promoting abnormal-activity thresholds as labels or production gates without reviewed calibration evidence.

Abnormal-activity rows may cite bars/liquidity/option artifacts as source refs, but the interpretation must explain the residual event-shaped behavior or risk relevance beyond the base model inputs.

## Event-activity bridge discipline

Some raw news is hard to standardize semantically at first sight. Do not force every such item into an over-specific event taxonomy. When price/flow/liquidity/odds behavior provides clearer point-in-time structure, convert the raw news + market behavior into an `event_activity_bridge` artifact.

Purpose: connect event evidence to market behavior without claiming the model understands every narrative detail.

Accepted relation types:

```text
pre_event_precursor
co_event_reaction
post_event_absorption
event_activity_divergence
unresolved_latent_hazard
```

Core fields:

```text
linked_event_ref
activity_evidence_refs
activity_window
event_window
lead_lag_seconds
residual_activity_score
cross_market_confirmation_score
option_confirmation_score
prediction_market_confirmation_score
explanation_status
```

Accepted `explanation_status` values:

```text
explained_by_known_event
partially_explained
unexplained
later_explained
review_required
```

Rules:

- `pre_event_precursor` means abnormal activity appeared before the event was publicly visible. It is a latent-event hazard signal, not proof of the future event.
- `co_event_reaction` means abnormal activity appears at/near event visibility and helps measure immediate market interpretation.
- `post_event_absorption` means abnormal activity after the event reflects absorption, disagreement, repricing, liquidity stress, or delayed interpretation.
- `event_activity_divergence` means event and activity disagree: big event/no reaction, small event/large reaction, odds move/no asset move, asset move/no news, etc.
- `unresolved_latent_hazard` means activity remains unexplained point-in-time and may later become `later_explained` if a canonical event appears.

For Polymarket or other prediction markets, odds movement can be an activity leg. Preserve it as prediction-market confirmation/divergence evidence, not as a securities-only signal.

This bridge helps standardize hard news by anchoring it to observable lead/lag, residual activity, and cross-market confirmation. It still must not emit buy/sell/hold, broker orders, or account mutation.

## Event risk governor boundary

If the architecture places event intelligence after the base trading-guidance layer, it may act as an event-risk governor. This governor can override or constrain a base decision record when high-risk point-in-time events are detected.

Allowed event-risk intervention outputs:

```text
event_risk_intervention_status
intervention_reason
risk_severity
block_new_entries
max_exposure_factor
reduce_exposure_to
flatten_position_candidate
halt_trading_candidate
review_required_reason
source_event_refs
evidence_spans
```

Severity ladder:

```text
observe_only
explain_only
block_new_entries
reduce_exposure
flatten_candidate
halt_candidate
human_review_required
```

Rules:

- Event-risk intervention is a safety/risk overlay, not alpha generation.
- It may directly modify the decision record consumed by execution/risk control, e.g. cap exposure, block new entries, or request flattening.
- It must not directly send broker orders or mutate accounts.
- Flattening/clearing requires high-confidence, high-severity evidence, source references, and an accepted execution risk policy or human review path.
- Keep base decision and event-adjusted decision side by side for audit.

## Scope routing

Route standardized events by affected scope before model generation:

- `global_market` / Layer 1 context: macro, central-bank, war, geopolitics, broad financial stress, cross-asset liquidity, broad bond/rates/yield-curve events, market-wide volatility or risk appetite.
- `sector_or_industry` / Layer 2 context: ETF/sector/industry-specific regulation, demand shocks, commodity input shocks, sector ETF flows, industry-wide earnings read-throughs, technology/regulatory changes affecting a group.
- `symbol` / target context: company-specific earnings, guidance, management, product, legal, M&A, capital allocation, supply-chain, customer, fraud, safety, or idiosyncratic news.
- `multi_scope`: events with both global/sector and symbol impact. Preserve all affected scopes and explain the primary scope.

Do not route Layer 1/2 ETF news as a single-stock event unless a named target has direct evidence. Do not route company-specific news as sector/global unless it has credible read-through evidence.

## Unknown-event protocol

News can include war, politics, regulation, financial-system stress, natural disasters, sanctions, cyber events, supply-chain shocks, and other events that cannot be fully enumerated in advance. Do not force such events into a wrong existing type.

When no accepted `normalized_event_type` fits:

1. Set `normalized_event_type = "unclassified_event"`.
2. Populate `event_domain_tags` with broad reusable domains, e.g. `geopolitical`, `war`, `sanctions`, `election`, `central_bank`, `fiscal_policy`, `banking_stress`, `credit_event`, `cybersecurity`, `supply_chain`, `commodity_shock`, `natural_disaster`, `public_health`, `legal_regulatory`, `labor`, `social_unrest`.
3. Set `standardization_status = "proposed_standard"`.
4. Propose a narrow `proposed_event_type` only if the evidence supports a reusable event class.
5. Provide `proposed_standard_rationale`: why existing types do not fit, what evidence pattern defines the new type, and how it should be reused.
6. Provide `standard_reuse_key`: a concise stable key candidate such as `geopolitical.sanctions.export_controls` or `financial_system.bank_liquidity_stress`.
7. Mark `review_status = "review_required"` for high-impact unknowns or new taxonomy proposals.

A proposed standard is not accepted taxonomy. It remains provisional until reviewed and registered through the project registry/docs process.

## Standard creation discipline

A new reusable standard should be proposed when:

- at least one high-impact event clearly does not fit current types; or
- a recurring fact pattern appears across multiple artifacts; or
- forcing it into an existing type would distort model inputs.

A new standard proposal must include:

- name/key;
- definition;
- inclusion criteria;
- exclusion criteria;
- example positive evidence;
- example near-miss/non-example;
- default scope mapping hints;
- default scoring anchors;
- point-in-time clock rule;
- relation to existing canonical/dedup types.

Do not mutate accepted standards silently. Propose, validate, and register.

## Event-family training discipline

Train and evaluate event interpretation/model behavior by coherent event families before mixing all events together. Treat an event family like a reusable modeling target with its own standards, examples, labels, and failure modes.

Recommended family axes:

```text
entity_or_theme_family: trump, fed, china_export_controls, ai_capex, regional_banking_stress
structural_event_family: equity_offering, buyback, earnings_guidance, sec_investigation, cpi_release
scope_family: global_market, sector_or_industry, symbol, multi_scope
canonical_source_family: sec_filing, macro_release, rates_curve, official_disclosure, news_only
narrative_family: strategic_investment_reframing, market_disappointment, policy_repricing, liquidity_stress
```

Examples:

- Train all Trump-related policy/geopolitical/news events together first, because the reusable standard is a political/person/entity-linked event family with recurring uncertainty, policy, sector, and market-wide channels.
- Train stock offering/equity issuance events together separately, because the reusable standard has different fields: dilution, proceeds use, discount, balance-sheet stress, growth funding, insider/underwriter context, and market absorption.
- Train CPI/Fed-path/rates events separately from company events, because their canonical source, clock, affected scope, and residual news interpretation are different.

Do not build the first event model by mixing every event type into one undifferentiated pool. After family-specific standards pass tests, compose them through a shared ontology and cross-family evaluation set.

Use staged acceptance instead of completing every family at full depth by default. If early evidence shows an event family has no usable relationship to target outcomes, downgrade or stop that family before spending full implementation effort. Early stop is acceptable when coverage, label density, effect size, conditional stability, or review quality fails. Preserve the artifact and rationale so it can be revisited later, but do not force it through the full pipeline.

Each event-family training packet should include:

- accepted family definition and exclusion rules;
- canonical source precedence and dedup rules;
- required interpretation fields and allowed optional fields;
- score anchors specific to the family;
- point-in-time clock rule;
- positive, negative, and near-miss examples;
- narrative residual patterns;
- scope-routing defaults;
- review-required triggers;
- golden tests and drift thresholds;
- early-stop criteria: minimum sample/coverage, minimum effect evidence, required conditional slices, false-positive tolerance, and downgrade/retire rules.

## Event-family acceptance states

Use explicit family status values:

```text
proposed
scouting
pilot_training
accepted_active
deferred_low_signal
retired_no_signal
review_required
```

`deferred_low_signal` means the family may matter later but current evidence is insufficient. `retired_no_signal` means reviewed evidence found no useful relationship for current objectives. Neither status deletes raw evidence; it prevents unnecessary full-depth training.

## Review gates

Require review for:

- unknown or proposed standards;
- high-intensity geopolitical, war, regulatory, sanctions, banking/credit, legal, bankruptcy, fraud, safety, FDA/clinical, M&A, or major guidance events;
- conflicting sources;
- low evidence confidence;
- extreme direction or intensity scores from weak evidence;
- any interpretation that could materially affect downstream model output.

## Output quality checks

Before accepting an artifact, verify:

- required fields are present;
- all scores are in range;
- all enum fields use accepted values or explicit provisional unknown protocol;
- evidence spans support the rationale;
- no forbidden trade/action/alpha fields appear;
- point-in-time clocks are consistent;
- canonical/duplicate relation is explicit;
- high-impact/unknown cases are review-marked.

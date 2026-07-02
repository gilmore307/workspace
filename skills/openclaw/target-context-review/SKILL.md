---
name: "target-context-review"
description: "Review PIT target context mapping for routing only."
---

# Target Context Review

Use this Codex skill before target-specific model layers or event routing consume target-to-context mappings.

This skill reviews target identity, Layer 2 sector/industry context, proxy mapping, corporate-action status, and optionability routing. It does not approve event-family modelability, event impact functions, signed impact distributions, M03 parameters, trade direction, position sizing, option structure, or execution.

## Required Inputs

- target id/symbol and effective date
- point-in-time target identity evidence
- sector/industry/market-context mapping evidence
- proxy mapping evidence, if any
- optionability evidence and option-chain availability route
- corporate-action, ticker-change, delisting, or listing-status evidence
- source refs and availability clocks
- proposed downstream consumers

## Review Workflow

1. Validate point-in-time identity.
   - Target identity, ticker, listing status, and corporate-action facts must be valid as of the reviewed time.

2. Validate Layer 2 mapping.
   - Sector/industry/context mapping must be specific and evidence-backed.
   - Ambiguous mappings defer.

3. Validate proxy use.
   - Proxy rows must be target-specific and must not silently mutate Layer 1 or Layer 2 universes.

4. Validate optionability routing.
   - Option-dependent work requires accepted optionability and option-chain route.
   - Non-optionable targets must not receive option-expression requirements.

5. Return routing decision only.

## Output Contract

Return strict JSON only:

```json
{
  "review_type": "target_context_review",
  "target_id": "string",
  "decision": "approve|defer|reject|insufficient_evidence",
  "layer2_context_status": "accepted|rejected|deferred|insufficient_evidence",
  "proxy_status": "accepted|rejected|not_applicable|insufficient_evidence",
  "optionability_status": "accepted|rejected|not_applicable|insufficient_evidence",
  "pit_status": "passed|failed|insufficient_evidence",
  "allowed_routing_use": ["target_context", "event_scope_routing", "optionability_routing"],
  "blocked_model_use": [
    "event_family_modelability_approval",
    "signed_impact_distribution",
    "m03_parameter_training_approval",
    "alpha_direction",
    "trade_decision",
    "position_sizing",
    "option_structure_selection",
    "broker_or_order_action"
  ],
  "blocking_issues": ["string"],
  "required_followups": ["string"],
  "rationale": "short evidence-grounded explanation"
}
```

## Decision Rules

- `approve`: PIT identity, Layer 2 mapping, proxy/optionability routes are adequate for proposed routing use.
- `defer`: plausible but missing evidence or ambiguous mapping.
- `reject`: wrong identity, invalid mapping, unsafe proxy, failed optionability route, or PIT failure.
- `insufficient_evidence`: required evidence is absent.

## Non-Negotiable Boundaries

- Do not approve event impact modeling.
- Do not infer signed event effect from target context.
- Do not output trade or option-expression advice.

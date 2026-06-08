---
name: "principle-dialogue"
description: "Reason through principle-level decisions with capped multi-round Codex CLI critique."
---

# Principle Dialogue

Use this skill for conceptual decisions where discussion may reveal better framing, hidden assumptions, or a cleaner implementation direction. Do not use it for routine code edits, status checks, simple explanations, or urgent operational repair unless the user explicitly asks for a principle-level discussion.

## Goal

Turn a vague or contested idea into one of:

- a shared principle;
- a concrete recommended design;
- a bounded experiment;
- or an explicit unresolved disagreement with the missing evidence named.

Consensus means both sides accept the same assumptions, decision criteria, and next verification step. It does not mean compromise for politeness.

## Agent Roles

OpenClaw is the host and final steward.

- Frame the question, project constraints, evidence, and decision boundary.
- Keep the discussion grounded in current code/data when relevant.
- Challenge weak claims from the Codex counterpart.
- Decide what to tell Chentong.

Codex CLI is the discussion partner.

- Act as a principled reviewer, not an implementer.
- Attack assumptions, missing baselines, false dichotomies, leakage risk, metric misuse, and overfitting.
- Offer alternative frames and sharper acceptance criteria.
- Avoid making edits unless the host explicitly launches an implementation task later.

Both agents must be calm, direct, evidence-seeking, and willing to disagree.

## Safe Invocation

Prefer non-interactive Codex CLI for the counterpart:

```bash
codex exec --model gpt-5.5 --sandbox read-only -c approval_policy="never" -C <working-dir> '<prompt>'
```

Rules:

- Use `--sandbox read-only` for discussion. Do not grant write access.
- Do not use `--dangerously-bypass-approvals-and-sandbox`.
- Do not ask Codex CLI to mutate services, databases, broker/account state, public systems, or storage.
- Keep secrets out of the prompt. Summarize private evidence instead of pasting sensitive content.
- If code context matters, include only the relevant file paths, function names, metrics, and observed results.
- If Codex CLI is unavailable, continue locally and say that the external discussion partner was unavailable.

## Discussion Workflow

1. Frame the issue in a compact brief:
   - question being decided;
   - current evidence;
   - assumptions;
   - constraints and red lines;
   - what a good answer must decide.

2. Ask Codex CLI for a hard review:
   - "Do not implement."
   - "Find the strongest objections."
   - "State what evidence would change your mind."
   - "Return a recommendation, risks, and a minimal verification plan."

3. Compare positions after each Codex CLI reply:
   - confirmed agreements;
   - unresolved objections;
   - changed assumptions;
   - evidence gaps;
   - decision criteria and next verification step.

4. Continue another Codex CLI round only when:
   - a material objection remains unresolved;
   - the disagreement is about reasoning, framing, assumptions, or criteria;
   - both sides have enough existing evidence to make progress by argument;
   - the next prompt can carry forward the current agreements, unresolved objections, changed assumptions, and evidence gaps.

5. Stop early when:
   - both sides converge on the same recommendation, assumptions, and verification step;
   - the remaining disagreement depends on new data, experiments, code inspection, metrics, or external evidence rather than further argument;
   - the discussion starts repeating prior claims without narrowing the disagreement;
   - the decision can be safely reduced to a bounded verification step.

6. Hard cap: run at most 5 total Codex CLI rounds. If the cap is reached, stop and report the remaining split instead of forcing consensus.

7. Final output to Chentong must summarize:
   - consensus reached;
   - remaining disagreements, if any;
   - strongest objections;
   - changed assumptions or evidence gaps;
   - next smallest verification step;
   - whether the 5-round cap was hit.

## Prompt Template

Use or adapt this prompt for the Codex CLI partner:

```text
We are discussing a principle-level technical decision. Do not edit files or run implementation.

Question:
<one sentence>

Context and evidence:
<short bullets with only relevant facts, metrics, paths, or constraints>

Current proposed direction:
<the host's current view>

Your role:
Act as a rigorous discussion partner. Challenge assumptions, identify hidden risks, propose a better framing if needed, and state what evidence would change the recommendation.

Output:
- Recommendation
- Strongest objections
- Better framing if any
- Minimal verification step
- Remaining disagreement or confidence level
```

## Output To Chentong

Reply in Chinese unless Chentong asks otherwise. Keep it concise and useful. Do not dump raw agent transcripts unless asked.

Use this shape:

- `结论`: the recommended principle/design.
- `为什么`: the key reasoning.
- `Codex 反对点`: only the strongest objections.
- `怎么验证`: the next smallest check.
- `未决风险`: what remains uncertain.

If both sides truly agree, say what they agreed on. If they do not, say where the disagreement remains and what evidence is needed.

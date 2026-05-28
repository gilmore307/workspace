---
name: principle-dialogue
description: Use when Chentong wants to reason through an architectural, modeling, strategy, product, or other principle-level question by having OpenClaw consult Codex CLI as a disciplined discussion partner until the core position, objections, and next verification step are clear. Trigger for phrases such as "讨论一下", "辩论", "原理", "方向对不对", "你觉得", "让 codex 也想想", or when a decision is conceptual rather than a direct implementation task.
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

3. Compare positions:
   - agreements;
   - disagreements;
   - new insight;
   - evidence gaps;
   - decision criteria.

4. Run one more Codex CLI round only if there is a material unresolved point that can be clarified by argument, not if it requires new data collection.

5. Stop after at most three total rounds. If still unresolved, return the split clearly instead of forcing agreement.

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

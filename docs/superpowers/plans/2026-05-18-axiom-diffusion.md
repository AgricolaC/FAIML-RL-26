# Axiom Skill Diffusion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Absorb the highest-value utilities from the proposed `humanized-ds-coding` skill directly into three existing axiom skills, eliminating a dangling reference and closing functional gaps in scope-gating and result interpretation.

**Architecture:** Three independent file edits — one per target skill. No shared state. Each task is self-contained and can be verified in isolation via grep. No new files created.

**Tech Stack:** Markdown skill files in `.claude/skills/*/SKILL.md`

**Design spec:** `docs/superpowers/specs/2026-05-18-axiom-diffusion-design.md`

---

### Task 1: Add scope threshold to `axiom-defend`

**Files:**
- Modify: `.claude/skills/axiom-defend/SKILL.md` — insert scope threshold block before `## Core Mandates`

- [ ] **Step 1: Verify the insertion point exists**

```bash
grep -n "## Core Mandates" .claude/skills/axiom-defend/SKILL.md
```

Expected output: a line number followed by `## Core Mandates (Non-Negotiable)`
If nothing is returned, do not proceed — the file structure has changed.

- [ ] **Step 2: Insert the scope threshold block**

Open `.claude/skills/axiom-defend/SKILL.md`. Find the line:

```
## Core Mandates (Non-Negotiable)
```

Insert the following block **immediately before** that line (with one blank line separating the new block from `## Core Mandates`):

```markdown
## Scope Assessment (Run First)

Before applying the full defensive protocol, assess the complexity of the request:

- **Simple requests** — one-liner fixes, quick debug, minor utility snippets:
  apply naming and type hint rules only. Skip the full checklist.
- **Design-level requests** — pipelines, training loops, data splits, new modules,
  loss computation: apply the full defensive protocol below.

When in doubt, apply the full protocol.

---

```

- [ ] **Step 3: Verify the insertion landed**

```bash
grep -n "Scope Assessment" .claude/skills/axiom-defend/SKILL.md
```

Expected: a line number and `## Scope Assessment (Run First)`

```bash
grep -n "Core Mandates" .claude/skills/axiom-defend/SKILL.md
```

Expected: a line number greater than the Scope Assessment line.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/axiom-defend/SKILL.md
git commit -m "feat(axiom-defend): add scope threshold preamble"
```

---

### Task 2: Add scope threshold and inline Stage 5 in `axiom-formalize`

**Files:**
- Modify: `.claude/skills/axiom-formalize/SKILL.md` — two edits:
  1. Insert scope threshold block before `## Stage 1`
  2. Replace the dangling `humanized-ds-coding` reference in Stage 5

- [ ] **Step 1: Verify both insertion/replacement points exist**

```bash
grep -n "## Stage 1" .claude/skills/axiom-formalize/SKILL.md
grep -n "## Stage 5" .claude/skills/axiom-formalize/SKILL.md
grep -n "humanized-ds-coding" .claude/skills/axiom-formalize/SKILL.md
```

Expected: line numbers for all three. If `humanized-ds-coding` returns nothing, the dangling reference was already removed — skip Step 3, still do Step 2.

- [ ] **Step 2: Insert scope threshold before Stage 1**

Find the line:

```
## Stage 1: Domain and Space Definition
```

Insert the following block **immediately before** it (with one blank line separating):

```markdown
## Scope Assessment (Run First)

Before applying the full formalization protocol, assess the complexity of the request:

- **Simple requests** — a quick definition, a named theorem, a one-line clarification:
  answer directly and concisely. No forced multi-stage formalization.
- **Design-level requests** — a new algorithm, loss function, data transformation,
  or architectural component: apply the full four-stage protocol below.

When in doubt, apply the full protocol.

---

```

- [ ] **Step 3: Replace the Stage 5 dangling reference**

Find and replace this exact block in Stage 5:

```
Only after explicit approval, write the implementation following the `humanized-ds-coding` style:
- Theoretical basis already done — reference the approved formalization
- Full type hints and Google-style docstrings
- Assert statements for every tensor shape transition
- Complexity and memory notes
```

Replace it with:

```
Only after explicit approval, write the implementation with:
- Full type hints on all function signatures
- Google-style docstrings: one-line summary, why-paragraph, Args/Returns/Raises/Defensive Notes
- Assert statements at every tensor shape transition (pairs with axiom-defend)
- Complexity note: state time and memory complexity, and any vectorization or
  caching choices made — 2–4 sentences or a short bullet list, not an essay
```

- [ ] **Step 4: Verify both edits landed**

```bash
grep -n "Scope Assessment" .claude/skills/axiom-formalize/SKILL.md
```

Expected: a line number before Stage 1.

```bash
grep -n "humanized-ds-coding" .claude/skills/axiom-formalize/SKILL.md
```

Expected: no output. If any output appears, the replacement did not fully land — re-edit.

```bash
grep -n "Complexity note" .claude/skills/axiom-formalize/SKILL.md
```

Expected: a line number inside the Stage 5 block.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/axiom-formalize/SKILL.md
git commit -m "feat(axiom-formalize): add scope threshold and inline Stage 5 style rules"
```

---

### Task 3: Add plain-language interpretation and baseline requirement to `axiom-falsify`

**Files:**
- Modify: `.claude/skills/axiom-falsify/SKILL.md` — append two new sections after the Claim Escalation Ladder, before `## When Terminal Access Is Unavailable`

- [ ] **Step 1: Verify the insertion point exists**

```bash
grep -n "## When Terminal Access Is Unavailable" .claude/skills/axiom-falsify/SKILL.md
grep -n "Claim Escalation Ladder" .claude/skills/axiom-falsify/SKILL.md
```

Expected: line numbers for both. The new sections go between them.

- [ ] **Step 2: Insert the two new sections**

Find the line:

```
## When Terminal Access Is Unavailable
```

Insert the following block **immediately before** it (with one blank line separating):

```markdown
## Plain-Language Result Interpretation

When code produces output — metrics, predictions, plots, tables — the terminal result
is necessary but not sufficient. After showing verified output, interpret what it means
in plain language. Avoid jargon unless it has been defined.

❌ "The model achieves 0.87 AUC-ROC."
✅ "The model correctly ranks a positive case above a negative one about 87% of the
    time — strong for a dataset with this class imbalance."

This is not a style preference. An uninterpreted number is an unverified claim about
meaning.

---

## Baseline Requirement

Every quantitative result must be paired with a reference point before it can be
treated as meaningful. Acceptable baselines: majority-class accuracy, random policy
return, prior published result, or the same model without the proposed change.

❌ "Training return: 450"
✅ "Training return: 450 (random policy baseline: 18; solved threshold: 3500)"

A number without a baseline is a guess dressed as a result. The claim escalation
ladder applies to baselines too — state the baseline source.

---

```

- [ ] **Step 3: Verify the insertions landed**

```bash
grep -n "Plain-Language Result Interpretation" .claude/skills/axiom-falsify/SKILL.md
```

Expected: a line number.

```bash
grep -n "Baseline Requirement" .claude/skills/axiom-falsify/SKILL.md
```

Expected: a line number after Plain-Language Result Interpretation.

```bash
grep -n "When Terminal Access Is Unavailable" .claude/skills/axiom-falsify/SKILL.md
```

Expected: a line number after Baseline Requirement.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/axiom-falsify/SKILL.md
git commit -m "feat(axiom-falsify): add plain-language interpretation and baseline requirement"
```

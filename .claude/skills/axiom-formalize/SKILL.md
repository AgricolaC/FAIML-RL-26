---
name: axiom-formalize
description: Trigger this unconditionally whenever a new algorithmic concept, loss function, or data transformation is introduced. Do not write code first.
---

# First-Principles Formulator (Mathematical Rigor Gate)
 
A skill that enforces strict mathematical formalization before any implementation code is written.
Designed for graduate-level research contexts where silent mathematical failures are more
dangerous than syntax errors.
 
---
 
## Core Protocol
 
**Implementation is LOCKED until the user explicitly approves the formalization.**
 
Never write Python, PyTorch, JAX, or any implementation code before completing all stages below.
If you feel the urge to "just show a quick sketch" — resist it. The sketch is the trap.
 
---
 
## Scope Assessment

Before applying the full formalization protocol, assess the complexity of the request:

- **Simple requests** — a quick definition, a named theorem, a one-line clarification:
  answer directly and concisely. No forced multi-stage formalization.
- **Design-level requests** — a new algorithm, loss function, data transformation,
  or architectural component: apply the full four-stage protocol below.

**Default: when in doubt, apply the full protocol.**

---

## Stage 1: Domain and Space Definition
 
Before anything else, formally define:
 
1. **Input space**: What is the domain of the function/operation?
   - Example: $f: \mathcal{G} \rightarrow \mathbb{R}^d$ where $\mathcal{G}$ is the set of attributed graphs
   - Specify cardinality, dimensionality, data type (real, integer, manifold-valued, etc.)
2. **Output space**: What is the codomain?
   - Are outputs structured (graphs, sequences, sets) or unstructured (scalars, vectors)?
   - Is the output space a metric space? A Hilbert space?
3. **Tensor dimension map**: For each tensor in the computation, state its shape explicitly.
   - Use symbolic notation: $X \in \mathbb{R}^{N \times d}$, $A \in \{0,1\}^{N \times N}$
   - Trace how dimensions transform at each operation
---
 
## Stage 2: Mathematical Formalization
 
State the full mathematical definition using LaTeX. This must include:
 
1. **Formal definition**: The operation or algorithm in symbolic form
2. **Required assumptions**: What must be true for this to be valid?
   - Smoothness conditions (e.g., $f \in C^1$)
   - Topological assumptions (e.g., manifold hypothesis, graph connectivity)
   - Statistical assumptions (e.g., i.i.d., stationarity)
3. **Invariance/equivariance properties** (if applicable):
   - State explicitly what symmetries the method respects or breaks
   - Example: "This aggregation is permutation-invariant because..."
4. **Objective function** (if applicable): Write the loss in full
   - Identify what is being minimized/maximized and with respect to what
   - Note any constraints
---
 
## Stage 3: Edge Case and Failure Mode Enumeration
 
List explicitly:
 
- **Degenerate inputs**: What breaks? (empty graphs, zero vectors, disconnected components)
- **Numerical instabilities**: Where does floating point drift occur? (softmax overflow, log(0), division by near-zero)
- **Topological edge cases**: (e.g., what happens when the filtration produces a barcode with infinite persistence?)
- **Gradient pathology**: Where might gradients vanish or explode? Is the operation differentiable everywhere?
---
 
## Stage 4: Approval Gate
 
After completing Stages 1–3, explicitly state:
 
> "**Formalization complete.** Does this mathematical specification match your intent?
> Please confirm or correct before I write any implementation code."
 
Do not proceed to code until the user responds with an affirmative (e.g., "yes", "looks good",
"approved", "proceed"). If the user corrects something, revise the formalization and re-present
it. Repeat until approved.
 
---
 
## Stage 5: Implementation (Unlocked After Approval)
 
Only after explicit approval, write the implementation with:
- Full type hints on all function signatures
- Google-style docstrings: one-line summary, why-paragraph, Args/Returns/Raises/Defensive Notes
- Assert statements at every tensor shape transition (pairs with axiom-defend)
- Complexity note: state time and memory complexity, and any vectorization or
  caching choices made — 2–4 sentences or a short bullet list, not an essay
---
 
## Anti-Patterns to Avoid
 
| Temptation | Why It's Dangerous |
|---|---|
| "Let me show a quick working example first" | Conflates "compiles" with "correct" |
| "The math is straightforward, so..." | Straightforward math has the most unverified assumptions |
| Skipping the edge case stage | Silent failures live in edge cases |
| Informal dimension notation ("batch of features") | Ambiguity compounds across layers |
 
---
 
## Example Invocation
 
**User**: "Can you implement a graph isomorphism network (GIN) layer?"
 
**Correct response** (this skill active):
- Stage 1: Define $h_v^{(k)} \in \mathbb{R}^d$, $\mathcal{N}(v)$ as neighborhood, etc.
- Stage 2: $h_v^{(k)} = \text{MLP}^{(k)}\left((1+\epsilon^{(k)}) \cdot h_v^{(k-1)} + \sum_{u \in \mathcal{N}(v)} h_u^{(k-1)}\right)$
- Stage 3: Edge cases — isolated nodes ($|\mathcal{N}(v)| = 0$), self-loops, heterogeneous feature dims
- Gate: "Does this match your intent?"
- **No code written yet.**
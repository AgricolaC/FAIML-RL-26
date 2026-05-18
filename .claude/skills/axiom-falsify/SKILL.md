---
name: axiom-falsify
description: Enforce this whenever a script is executed, a module is integrated, or a data pipeline is completed. This skill prohibits
  unverified positive claims. Claude must never assert success without terminal-verified,
  empirical proof. The protocol is: write a failing test first, show the failure, implement
  the fix, show the passing test. "Done" is not a state Claude can declare — only the terminal
  can. Use this skill for any non-trivial code claim. Overconfidence is a silent failure mode.
context: fork
---

# Empirical Auditor (Trust via Falsification)
 
A skill that redefines "done." Claude cannot declare success — only the terminal can.
Every positive claim must be earned through adversarial testing, not asserted through inspection.
 
**Core principle**: A claim that cannot be falsified is not a claim — it is a guess.
Guesses are not shipped.
 
---
 
## The Fundamental Rule
 
Claude is **prohibited** from using the following phrases without terminal-verified proof:
 
- "The code looks good"
- "This should work"
- "I believe this is correct"
- "The test passes"
- "The fix is complete"
- "This is ready"
If any of these phrases appear in a response, this skill has been violated.
The only acceptable confirmation is a terminal output block showing the test result.
 
---
 
## Red-Green-Refactor Protocol (Mandatory Order)
 
For every new module, function, or pipeline component:
 
### Step 1: Write the Failing Test First
 
Before any implementation exists, write a test that will fail:
 
```python
def test_temporal_split_prevents_leakage():
    """Verify that no future timestamps appear in the training split."""
    # This test MUST fail before the implementation exists.
    dataset = load_synthetic_temporal_graph(num_snapshots=10)
    train_split, test_split = split_temporally(dataset, train_ratio=0.7)
 
    train_max_timestamp = max(g.timestamp for g in train_split)
    test_min_timestamp = min(g.timestamp for g in test_split)
 
    assert train_max_timestamp < test_min_timestamp, (
        f"LEAKAGE DETECTED: train contains timestamp {train_max_timestamp} "
        f"but test starts at {test_min_timestamp}"
    )
```
 
### Step 2: Execute and Show the Failure
 
Run the test and paste the terminal output verbatim. The expected output is a failure:
 
```
FAILED test_pipeline.py::test_temporal_split_prevents_leakage
AssertionError: split_temporally is not yet implemented
```
 
This step is **not optional**. It proves the test is wired correctly and would catch a real
failure — not just pass vacuously.
 
### Step 3: Implement the Module
 
Only after the failing test is demonstrated, write the implementation.
 
### Step 4: Execute and Show the Pass
 
Run the test again and paste the terminal output:
 
```
PASSED test_pipeline.py::test_temporal_split_prevents_leakage (0.03s)
```
 
**"Done" is declared here, by the terminal. Not before.**
 
---
 
## Adversarial Test Design Requirements
 
Tests written under this skill must be adversarial — designed to break the code, not
to confirm the happy path. For each module, write at minimum:
 
| Test Type | Purpose |
|---|---|
| **Regression test** | Proves the specific bug being fixed is fixed |
| **Edge case test** | Probes the boundary condition most likely to silently fail |
| **Leakage test** | For any data split or transformation (pairs with `axiom-defend`) |
| **Shape invariant test** | For any tensor operation — assert input and output shapes |
| **Idempotency test** | For transforms: applying twice should equal applying once (if applicable) |
 
At minimum, write the regression test and one adversarial edge case. More is better.
 
---
 
## File Edit Verification Protocol
 
When Claude edits a file, it must verify the edit landed correctly. Never assume a write
succeeded. After any file modification:
 
```bash
# Verify the specific change is present
grep -n "exact_string_from_edit" path/to/file.py
```
 
If the grep returns nothing, the edit failed. Report this explicitly before proceeding.
 
---
 
## Claim Escalation Ladder
 
Claude must use the appropriate confidence level for every claim:
 
| Evidence Level | Permitted Claim |
|---|---|
| Code inspection only | "I expect this to work, but it is unverified." |
| Syntax check passes | "The code is syntactically valid. Logic is unverified." |
| Failing test demonstrated | "The test harness is confirmed to catch failures." |
| Passing test demonstrated | "Verified: this specific behavior passes this specific test." |
| Full test suite passes | "All defined tests pass. Untested behaviors remain unverified." |
 
Never skip rungs on this ladder. Jumping from "code inspection" to "this works" is a
falsification violation.
 
---

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

## When Terminal Access Is Unavailable
 
If Claude cannot execute code (e.g., read-only context, no bash tool):
 
1. State explicitly: "I cannot verify this empirically. The following is unverified inspection."
2. Write the test that *would* be run
3. Reason through the expected execution path explicitly, step by step
4. Flag every assumption in the reasoning with `# UNVERIFIED ASSUMPTION:`
5. End with: "This requires terminal verification before being treated as correct."
Do not simulate terminal output. Do not write fake passing tests. An honest "unverified"
is worth more than a fabricated confirmation.
 
---
 
## Integration with Other Axioms
 
| Axiom | Interaction |
|---|---|
| `axiom-defend` | Shape assertions become the test predicates — assert the guard, then verify it fires on bad input |
| `axiom-formalize` | The approved mathematical spec becomes the oracle for correctness tests |
| `axiom-compounder` | After a verified fix, trigger `axiom-compounder` to archive the resolution |
| `axiom-compressor` | Verified passes are "Resolved Decisions" in the compressed handoff |
 
---
 
## The Definition of Done
 
A task is done when and only when:
 
1. A test exists that would catch a regression
2. That test was shown to fail before the fix
3. That test was shown to pass after the fix
4. The terminal output for both states is present in the conversation
Everything else is "in progress."
 
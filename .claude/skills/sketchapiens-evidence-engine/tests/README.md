# Evidence Engine Tests — Bộ kiểm Cỗ máy bằng chứng

> **Purpose:** regression harness cho `sketchapiens-evidence-engine`.
> **Not a rulebook:** fixtures là test inputs/expected behavior, không phải channel knowledge hay checklist bắt mọi video phải có.

## Test layers

### A. Semantic smoke

Blind-first evaluation của claim/source/bridge behavior.

- **5 historical cases** từ V17–V20 để giữ những failure/success pattern đã xảy ra thật.
- **12 micro cases** để cô lập edge behavior, provenance, transfer, synthesis và lock traceability.

Tổng semantic fixtures: **17**.

### B. Deterministic ledger checks

Machine fixtures cho `scripts/validate_claim_ledger.py`:

- valid pre-draft ledger;
- valid bound ledger;
- invalid locked-null ledger;
- invalid unknown source ref;
- invalid bridge dependency.

## Profiles

### `CLAIM_VERIFY_SMOKE`

Allowed:

- fixture input/surface;
- Evidence Engine public runtime;
- exact sources supplied by fixture.

Forbidden default context:

- fixture EXPECTED before output lock;
- competitor corpus/teardown;
- Writer prose theory;
- retention theory;
- Story mechanism lab;
- Egypt R&D raw case unless fixture explicitly supplies a synthetic excerpt.

### `BRIDGE_SMOKE`

Same as above + exact node/bridge relationship.
Must load Causal Proof Fit only when relation-level review is relevant.

### `LOCK_TRACE_SMOKE`

Machine ledger + exact script refs only.
No semantic rewriting task.

## Blind-first invariant

1. Writer/reviewer-under-test sees only INPUT/SURFACE + allowed runtime context.
2. Produce and lock Evidence output.
3. Separate evaluator then sees EXPECTED BEHAVIOR.
4. Evaluator grades.
5. If expectation/input leaks, mark `EXECUTION_FAULT`, not PASS/FAIL.

Do not let the tested Evidence reviewer revise after reading expectation and call that a PASS.

## Severity for test failures

```text
P0 — can lock fabricated/unsupported material as safe or corrupt exact-version provenance
P1 — misses a material bridge/scope/denominator failure or rejects a clearly valid synthesis systematically
P2 — useful behavior degraded but core safety survives
P3 — reporting/wording ergonomics only
```

## Phase 4B closure target

Semantic runtime may close only when:

- 17/17 valid fixtures PASS;
- P0 = 0;
- P1 = 0;
- valid synthesis positive control PASS;
- fifth-verdict leakage = NONE;
- bridge false-positive/false-negative controls PASS;
- exact-version lock traceability PASS;
- competitor/R&D leakage = NONE;
- deterministic ledger tests PASS;
- project doctor FAIL = 0.

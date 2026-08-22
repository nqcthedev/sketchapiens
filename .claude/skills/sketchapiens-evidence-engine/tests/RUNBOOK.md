# Evidence Engine Runtime Runbook — Quy trình chạy smoke

## 1. Before run

Confirm branch and checkpoint expected by the current Phase 4B report.
Do not modify runtime during a diagnostic pass.

Read only:

1. `tests/README.md`
2. this `RUNBOOK.md`
3. fixture INPUT/SURFACE for the case being executed
4. runtime Evidence context allowed by that profile

Do **not** read EXPECTED BEHAVIOR before the tested output is locked.

## 2. Historical source pin verification

Before each H-E fixture, verify path + blob SHA exactly.

If source pin is missing/mismatched:

```text
RESULT = EXECUTION_FAULT
```

Do not silently substitute a newer script/verify file and grade it as the same historical case.

## 3. Semantic execution protocol

For each fixture:

### Evaluator A — input preparation

Provides only:

- INPUT/SURFACE;
- source snippets/full source material explicitly allowed by fixture;
- active Evidence runtime context.

### Tested Evidence context

Must produce final diagnosis without seeing EXPECTED.
Lock output.

### Evaluator B — grading

Only after output lock, read EXPECTED BEHAVIOR and assign:

```text
PASS
FAIL
EXECUTION_FAULT
```

with severity `P0–P3` if FAIL.

No corrective editing before the diagnostic report exists.

## 4. Required fields per semantic fixture

```text
FIXTURE:
PROFILE:
SOURCE PIN VERIFIED:
RESULT:
SEVERITY:

FOUR-VERDICT TAXONOMY:
CLAIM-SOURCE FIT:
PROVENANCE:
TRANSFER/SCOPE:
BRIDGE VERDICT:
VALID SYNTHESIS CONTROL:
STORY-DEVICE SEGMENTATION:
LOCK TRACEABILITY:
CONTEXT LEAKAGE:

OBSERVED BEHAVIOR:
NOTES:
```

Use `N/A` only when the fixture genuinely does not exercise a field.

## 5. Forbidden leakage

Normal semantic runs must not default-load:

```text
2_KHO_BANGHI/**
competitor teardown files
Writer runtime-monolith-legacy.md
Story Engine mechanism-lab.md
Story Engine candidate-lifecycle.md
rd-egypt-heat-2026-08-22.md
fixture EXPECTED before output lock
```

A synthetic fixture may contain a self-contained Egypt-shaped problem without loading the raw R&D case.

## 6. Bridge grading

A bridge case does not PASS merely because node facts are classified correctly.

Evaluator must check whether Evidence explicitly verdicts the relationship:

```text
SUPPORTED
QUALIFIED
UNSUPPORTED
UNVERIFIED
```

Material false edge missed = at least P1.
Valid synthesis incorrectly rejected because “no single source says the thesis” = at least P1.

## 7. Fifth-verdict leakage

If tested runtime emits `SYNTHESIS` as a top-level factual kind instead of using the four canonical verdicts + derivation metadata:

```text
RESULT = FAIL
minimum severity = P1
```

unless the owner has explicitly changed the canonical contract after this runbook version.

## 8. Deterministic validator tests

Run:

```bash
python3 .claude/skills/sketchapiens-evidence-engine/tests/test_ledger_validator.py
```

Expected:

```text
PASS 5
FAIL 0
exit 0
```

A failing deterministic test is not a semantic-model failure; classify it as implementation regression.

## 9. Project doctor

After semantic suite:

```bash
python3 tools/project_doctor.py
```

Record exact totals and exit code.
No FAIL may be hidden as “pre-existing” without listing it.

## 10. Report checker

After filling runtime report:

```bash
python3 .claude/skills/sketchapiens-evidence-engine/tests/check_evidence_smoke_report.py <report.md>
```

The checker validates report completeness/closure contradictions.
It does not decide whether a nuanced Evidence verdict is intellectually correct.

## 11. Corrective rerun rule

If a fixture is under-specified or execution context leaks:

1. preserve original run truth;
2. classify `EXECUTION_FAULT` or fixture defect;
3. fix the fixture/input only if that is the proven defect;
4. rerun only affected fixture in clean context;
5. append corrective provenance;
6. never rewrite original run to look passed.

## 12. Stable closure

Only conclude:

```text
PHASE 4B: COMPLETE / STABLE
EVIDENCE ENGINE: RUNTIME VERIFIED
```

when the closure target in `tests/README.md` is satisfied.
Otherwise remain:

```text
PHASE 4B: RELEASE CANDIDATE
RUNTIME VERIFICATION: FAILED / BLOCKED / PENDING
```

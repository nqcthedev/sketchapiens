# Phase 4B Evidence Runtime Verification

**Branch:** upgrade/story-engine-v21
**Checkpoint under test:** <SHA>
**Date:** <YYYY-MM-DD>

## Summary

```text
VALID FIXTURES: __/17 PASS
P0: __
P1: __
P2: __
P3: __

FIFTH-VERDICT LEAKAGE: NONE / FOUND
VALID SYNTHESIS CONTROL: PASS / FAIL
BRIDGE CONTROLS: PASS / FAIL
LOCK TRACEABILITY: PASS / FAIL
CONTEXT LEAKAGE: NONE / FOUND
LEDGER VALIDATOR: PASS / FAIL
PROJECT DOCTOR FAIL: __
PROJECT DOCTOR EXIT: __
```

## Semantic fixtures

Repeat this block for every fixture H-E01→H-E05 and M-E01→M-E12.

```text
FIXTURE: <ID>
PROFILE: <PROFILE>
SOURCE PIN VERIFIED: YES / NO / N/A
RESULT: PASS / FAIL / EXECUTION_FAULT
SEVERITY: N/A / P0 / P1 / P2 / P3

FOUR-VERDICT TAXONOMY: PASS / FAIL / N/A
CLAIM-SOURCE FIT: PASS / FAIL / N/A
PROVENANCE: PASS / FAIL / N/A
TRANSFER/SCOPE: PASS / FAIL / N/A
BRIDGE VERDICT: PASS / FAIL / N/A
VALID SYNTHESIS CONTROL: PASS / FAIL / N/A
STORY-DEVICE SEGMENTATION: PASS / FAIL / N/A
LOCK TRACEABILITY: PASS / FAIL / N/A
CONTEXT LEAKAGE: NONE / FOUND

OBSERVED BEHAVIOR:
<text>

NOTES:
<text>
```

## Deterministic validator

```text
COMMAND:
python3 .claude/skills/sketchapiens-evidence-engine/tests/test_ledger_validator.py

EXPECTED:
PASS 5
FAIL 0

ACTUAL:
<output>

LEDGER VALIDATOR: PASS / FAIL
```

## Project doctor

```text
COMMAND:
python3 tools/project_doctor.py

PASS: __
WARN: __
FAIL: __
EXIT CODE: __
```

## Execution faults / corrective reruns

Preserve original run blocks.
If a fixture input/run is invalid, append corrective provenance instead of rewriting history.

## Final verdict

Use exactly one:

```text
PHASE 4B: COMPLETE / STABLE
EVIDENCE ENGINE: RUNTIME VERIFIED
```

or

```text
PHASE 4B: RELEASE CANDIDATE
RUNTIME VERIFICATION: FAILED / BLOCKED / PENDING
```

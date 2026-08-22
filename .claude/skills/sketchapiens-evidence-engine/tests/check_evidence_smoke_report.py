#!/usr/bin/env python3
"""Check Evidence runtime report completeness and closure contradictions.

This script does not judge nuanced scientific correctness.
It only verifies that required fixtures/closure fields are present and that a
COMPLETE/STABLE verdict is not declared while deterministic blockers remain.
"""
import re
import sys

FIXTURES = [
    "H-E01", "H-E02", "H-E03", "H-E04", "H-E05",
    "M-E01", "M-E02", "M-E03", "M-E04", "M-E05", "M-E06",
    "M-E07", "M-E08", "M-E09", "M-E10", "M-E11", "M-E12",
]


def last_fixture_result(text, fixture):
    pattern = re.compile(
        rf"FIXTURE:\s*{re.escape(fixture)}\b(.*?)(?=\nFIXTURE:\s*[HM]-E\d+\b|\Z)",
        re.S,
    )
    matches = list(pattern.finditer(text))
    if not matches:
        return None
    block = matches[-1].group(1)
    m = re.search(r"^RESULT:\s*(PASS|FAIL|EXECUTION_FAULT)\s*$", block, re.M)
    return m.group(1) if m else None


def scalar(text, label):
    matches = re.findall(rf"^{re.escape(label)}:\s*([^\n]+?)\s*$", text, re.M)
    return matches[-1].strip() if matches else None


def int_scalar(text, label):
    value = scalar(text, label)
    if value is None:
        return None
    m = re.search(r"-?\d+", value)
    return int(m.group()) if m else None


def main(path):
    text = open(path, encoding="utf-8").read()
    errors = []

    results = {}
    for fixture in FIXTURES:
        result = last_fixture_result(text, fixture)
        results[fixture] = result
        if result is None:
            errors.append(f"missing or malformed fixture result: {fixture}")
        elif result != "PASS":
            errors.append(f"fixture not PASS: {fixture}={result}")

    p0 = int_scalar(text, "P0")
    p1 = int_scalar(text, "P1")
    doctor_fail = int_scalar(text, "PROJECT DOCTOR FAIL")

    required_exact = {
        "FIFTH-VERDICT LEAKAGE": "NONE",
        "VALID SYNTHESIS CONTROL": "PASS",
        "BRIDGE CONTROLS": "PASS",
        "LOCK TRACEABILITY": "PASS",
        "CONTEXT LEAKAGE": "NONE",
        "LEDGER VALIDATOR": "PASS",
    }
    for label, expected in required_exact.items():
        value = scalar(text, label)
        if value is None:
            errors.append(f"missing closure field: {label}")
        elif value != expected:
            errors.append(f"closure field {label}={value!r}, expected {expected!r}")

    if p0 is None:
        errors.append("missing P0")
    elif p0 != 0:
        errors.append(f"P0 must be 0, got {p0}")

    if p1 is None:
        errors.append("missing P1")
    elif p1 != 0:
        errors.append(f"P1 must be 0, got {p1}")

    if doctor_fail is None:
        errors.append("missing PROJECT DOCTOR FAIL")
    elif doctor_fail != 0:
        errors.append(f"PROJECT DOCTOR FAIL must be 0, got {doctor_fail}")

    stable = "PHASE 4B: COMPLETE / STABLE" in text
    runtime_verified = "EVIDENCE ENGINE: RUNTIME VERIFIED" in text

    if stable != runtime_verified:
        errors.append("stable/runtime-verified verdict lines must appear together")

    if stable and errors:
        errors.append("report declares COMPLETE/STABLE while closure blockers remain")

    if not stable:
        errors.append("report does not declare PHASE 4B: COMPLETE / STABLE")

    if errors:
        print("EVIDENCE SMOKE REPORT INVALID")
        for err in errors:
            print(f"- {err}")
        return 1

    print("EVIDENCE SMOKE REPORT VALID")
    print(f"fixtures PASS: {len(FIXTURES)}/{len(FIXTURES)}")
    print("P0=0 P1=0 doctor_fail=0")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: check_evidence_smoke_report.py <report.md>")
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

#!/usr/bin/env python3
"""Deterministic regression test for Evidence claim-ledger validator."""
import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENGINE = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(HERE, "../../../.."))
VALIDATOR = os.path.join(ENGINE, "scripts", "validate_claim_ledger.py")
SCHEMA = os.path.join(ROOT, "schemas", "claim-ledger.schema.json")
CASES = os.path.join(HERE, "fixtures", "ledger-validator-cases.json")


def load_validator():
    spec = importlib.util.spec_from_file_location("ska_evidence_validator_test", VALIDATOR)
    if not spec or not spec.loader:
        raise RuntimeError("cannot load validator spec")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    validator = load_validator()
    with open(SCHEMA, encoding="utf-8") as f:
        schema = json.load(f)
    with open(CASES, encoding="utf-8") as f:
        cases = json.load(f)

    passed = 0
    failed = 0
    for case in cases:
        errors = validator.validate_data(case["data"], schema)
        actual_valid = not errors
        expected_valid = bool(case["expected_valid"])
        if actual_valid == expected_valid:
            passed += 1
            print(f"PASS {case['id']}")
        else:
            failed += 1
            print(f"FAIL {case['id']} expected_valid={expected_valid} actual_valid={actual_valid}")
            for err in errors[:5]:
                print(f"  - {err}")

    print(f"PASS {passed}")
    print(f"FAIL {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Deterministic regression test for Evidence claim-ledger validator."""
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile

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


def _build_video(tmp: str) -> tuple[str, str, str]:
    """Dựng một video tối thiểu đủ để validate_video_ledger chạy."""
    video_dir = os.path.join(tmp, "SKA-0099-test")
    for sub in ("02-research", "03-script/versions", "03-script/refs"):
        os.makedirs(os.path.join(video_dir, sub))
    script = os.path.join(video_dir, "03-script/versions/v001.md")
    with open(script, "w", encoding="utf-8") as f:
        f.write("Trời vừa tối.\nMột người đang tìm chỗ nằm.\n")
    with open(os.path.join(video_dir, "03-script/refs/current.yaml"), "w", encoding="utf-8") as f:
        f.write("version: v001\n")
    with open(os.path.join(video_dir, "video.yaml"), "w", encoding="utf-8") as f:
        f.write("id: SKA-0099-test\n")
    ledger = os.path.join(video_dir, "02-research/claim-ledger.json")
    return video_dir, script, ledger


def _digest(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def run_digest_cases(validator) -> tuple[int, int]:
    """G-01 regression: script_sha256 phải neo vào NỘI DUNG, không chỉ tên file.

    Không có mấy ca này thì cổng bắt được "trỏ sai version" nhưng không bắt được
    ai sửa tay một vNNN.md tại chỗ — tức phá luật version bất biến mà vẫn xanh.
    """
    passed = failed = 0
    tmp = tempfile.mkdtemp(prefix="ska-ledger-digest-")
    try:
        video_dir, script, ledger_path = _build_video(tmp)
        real = _digest(script)
        base = {
            "video_id": "SKA-0099-test",
            "script_ref": "03-script/versions/v001.md",
            "locked": True,
            "lockability": "LOCKABLE",
            "sources": [],
            "claims": [],
            "bridges": [],
        }

        cases = [
            ("L-D01 digest khớp thì sạch", real, True, None),
            ("L-D02 digest lệch thì bắt", "0" * 64, False, "script content drift"),
            ("L-D03 digest null giữ hành vi cũ", None, True, None),
        ]
        for case_id, sha, expect_valid, expect_sub in cases:
            data = dict(base, script_sha256=sha)
            with open(ledger_path, "w", encoding="utf-8") as f:
                json.dump(data, f)
            errors = validator.validate_video_ledger(video_dir)
            ok = (not errors) if expect_valid else any(expect_sub in e for e in errors)
            if ok:
                passed += 1
                print(f"PASS {case_id}")
            else:
                failed += 1
                print(f"FAIL {case_id} -> {errors}")

        # L-D04: khai đúng digest rồi sửa tay file — đúng kịch bản G-01
        with open(ledger_path, "w", encoding="utf-8") as f:
            json.dump(dict(base, script_sha256=real), f)
        with open(script, "a", encoding="utf-8") as f:
            f.write("Một câu bị sửa lén vào đây.\n")
        errors = validator.validate_video_ledger(video_dir)
        if any("script content drift" in e for e in errors):
            passed += 1
            print("PASS L-D04 sửa tay version bất biến thì bắt")
        else:
            failed += 1
            print(f"FAIL L-D04 sửa tay version bất biến KHÔNG bắt được -> {errors}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return passed, failed


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

    d_passed, d_failed = run_digest_cases(validator)
    passed += d_passed
    failed += d_failed

    print(f"PASS {passed}")
    print(f"FAIL {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

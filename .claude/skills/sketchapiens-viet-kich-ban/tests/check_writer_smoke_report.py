#!/usr/bin/env python3
"""Deterministic validator for Writer smoke reports.

This script validates report shape and explicit safety fields only.
It does NOT judge prose quality, structural quality, or factual correctness.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HISTORICAL = [f"H-W0{i}" for i in range(1, 4)]
MICRO = [f"M-W{i:02d}" for i in range(1, 13)]
EXPECTED_FIXTURES = HISTORICAL + MICRO

VALID_RESULTS = {"PASS", "FAIL", "REVIEW", "EXECUTION_FAULT"}
VALID_SEVERITIES = {"P0", "P1", "P2", "P3", "NONE"}
VALID_TRI = {"PASS", "FAIL", "N/A"}

CHECK_FIELDS = [
    "VI-FIRST",
    "EN-GATE",
    "STRUCTURE BOUNDARY",
    "EVIDENCE BOUNDARY",
    "COMPETITOR FIREWALL",
    "DEAD/PENDING RULE FIREWALL",
    "CROSS-MODE ISOLATION",
    "ARTIFACT SAFETY",
    "PROSE CAPABILITY",
]

SUMMARY_REQUIRED = [
    "LEGACY LOADED IN NORMAL RUN",
    "COMPETITOR LEAKAGE",
    "D-27 / DEAD RULE LEAKAGE",
    "EN GATE BOTH DIRECTIONS",
    "STRUCTURE BOUNDARY",
    "EVIDENCE BOUNDARY",
    "CROSS-MODE ISOLATION",
    "ARTIFACT SAFETY",
    "PROSE CAPABILITY",
    "PROJECT DOCTOR",
    "PHASE 3B WRITER VERDICT",
]


def field_value(text: str, label: str) -> str | None:
    pattern = rf"(?mi)^\s*{re.escape(label)}\s*:\s*(.*?)\s*$"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None


def split_fixture_sections(text: str) -> dict[str, str]:
    pattern = re.compile(
        r"(?m)^##\s+FIXTURE\s+((?:H|M)-W\d{2})\s*$"
    )
    matches = list(pattern.finditer(text))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        fixture_id = match.group(1)
        sections[fixture_id] = text[start:end]
    return sections


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument(
        "--partial",
        action="store_true",
        help="Allow a subset of fixtures for corrective reruns.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.report.exists():
        print(f"FAIL: report not found: {args.report}")
        return 2

    text = args.report.read_text(encoding="utf-8")
    sections = split_fixture_sections(text)
    errors: list[str] = []
    warnings: list[str] = []

    if not sections:
        errors.append("No fixture sections found. Expected headings like '## FIXTURE H-W01'.")

    unknown = sorted(set(sections) - set(EXPECTED_FIXTURES))
    if unknown:
        errors.append(f"Unknown fixture IDs: {', '.join(unknown)}")

    if not args.partial:
        missing = [f for f in EXPECTED_FIXTURES if f not in sections]
        if missing:
            errors.append(f"Missing fixtures: {', '.join(missing)}")
        if len(sections) != len(EXPECTED_FIXTURES):
            errors.append(
                f"Expected {len(EXPECTED_FIXTURES)} fixture sections, found {len(sections)}."
            )

    p0_fail = 0
    p1_fail = 0
    execution_faults = 0

    for fixture_id, section in sections.items():
        result = field_value(section, "RESULT")
        severity = field_value(section, "SEVERITY")

        if result not in VALID_RESULTS:
            errors.append(f"{fixture_id}: invalid/missing RESULT: {result!r}")
        if severity not in VALID_SEVERITIES:
            errors.append(f"{fixture_id}: invalid/missing SEVERITY: {severity!r}")

        for field in CHECK_FIELDS:
            value = field_value(section, field)
            if value not in VALID_TRI:
                errors.append(f"{fixture_id}: {field} must be PASS/FAIL/N/A, got {value!r}")

        source_pin = field_value(section, "SOURCE PIN VERIFIED")
        if source_pin not in {"YES", "NO", "N/A"}:
            errors.append(
                f"{fixture_id}: SOURCE PIN VERIFIED must be YES/NO/N/A, got {source_pin!r}"
            )
        if fixture_id.startswith("H-") and source_pin == "NO" and result != "EXECUTION_FAULT":
            errors.append(
                f"{fixture_id}: historical source pin NO must be RESULT: EXECUTION_FAULT."
            )

        if result == "EXECUTION_FAULT":
            execution_faults += 1

        if result == "FAIL" and severity == "P0":
            p0_fail += 1
        if result == "FAIL" and severity == "P1":
            p1_fail += 1

        observed = field_value(section, "OBSERVED BEHAVIOR")
        if observed is None or not observed:
            warnings.append(f"{fixture_id}: OBSERVED BEHAVIOR is empty.")

    if not args.partial:
        summary = text.split("# SUITE SUMMARY", 1)
        if len(summary) != 2:
            errors.append("Missing '# SUITE SUMMARY' section.")
        else:
            summary_text = summary[1]
            for field in SUMMARY_REQUIRED:
                value = field_value(summary_text, field)
                if value is None or value == "":
                    errors.append(f"Suite summary missing value for: {field}")

            total_expected = field_value(summary_text, "TOTAL EXPECTED FIXTURES")
            if total_expected not in {"15", None}:
                errors.append(
                    f"TOTAL EXPECTED FIXTURES should be 15, got {total_expected!r}"
                )

            legacy = field_value(summary_text, "LEGACY LOADED IN NORMAL RUN")
            competitor = field_value(summary_text, "COMPETITOR LEAKAGE")
            d27 = field_value(summary_text, "D-27 / DEAD RULE LEAKAGE")
            verdict = field_value(summary_text, "PHASE 3B WRITER VERDICT")

            stable = verdict == "COMPLETE / STABLE"
            if stable and legacy != "NO":
                errors.append("Stable verdict forbidden when legacy default-load is not NO.")
            if stable and competitor != "NO":
                errors.append("Stable verdict forbidden when competitor leakage is not NO.")
            if stable and d27 != "NO":
                errors.append("Stable verdict forbidden when D-27/dead-rule leakage is not NO.")
            if stable and (p0_fail or p1_fail):
                errors.append(
                    f"Stable verdict forbidden with blocking FAILs: P0={p0_fail}, P1={p1_fail}."
                )
            if stable and execution_faults:
                errors.append(
                    "Stable verdict forbidden while EXECUTION_FAULT fixtures remain unresolved."
                )

    print("Writer smoke report deterministic check")
    print(f"fixtures parsed: {len(sections)}")
    print(f"blocking FAILs: P0={p0_fail} P1={p1_fail}")
    print(f"execution faults: {execution_faults}")

    for warning in warnings:
        print(f"WARN: {warning}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: report shape and explicit safety fields are internally consistent.")
    print("NOTE: semantic Writer quality is NOT evaluated by this checker.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

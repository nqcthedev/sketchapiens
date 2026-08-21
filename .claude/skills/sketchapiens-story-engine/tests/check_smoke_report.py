#!/usr/bin/env python3
"""Structural checker for Story Engine smoke reports.

This script deliberately does NOT judge semantic quality.
It only verifies report shape and catches obvious candidate leakage.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HISTORICAL_IDS = [f"H-{i:02d}" for i in range(1, 6)]
MICRO_IDS = [f"M-{i:02d}" for i in range(1, 11)]
ALL_IDS = HISTORICAL_IDS + MICRO_IDS
VALID_RESULTS = {"PASS", "FAIL", "REVIEW"}
VALID_SEVERITIES = {"P0", "P1", "P2", "P3", "NONE", "N/A"}
CANDIDATE_NAMES = (
    "Solution Ladder",
    "Constraint Migration",
    "Scale-Out Escalation",
    "Evidence Fit",
    "Causal Proof Fit",
)


def parse_blocks(text: str) -> dict[str, str]:
    """Split report into FIXTURE blocks."""
    matches = list(re.finditer(r"(?mi)^FIXTURE:\s*(H-\d{2}|M-\d{2})\s*$", text))
    blocks: dict[str, str] = {}
    for idx, match in enumerate(matches):
        fixture_id = match.group(1).upper()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        blocks[fixture_id] = text[match.start():end]
    return blocks


def field(block: str, name: str) -> str | None:
    match = re.search(rf"(?mi)^{re.escape(name)}:\s*([^\n]+?)\s*$", block)
    return match.group(1).strip() if match else None


def observed_diagnosis(block: str) -> str:
    match = re.search(
        r"(?mis)^OBSERVED DIAGNOSIS:\s*(.*?)(?=^\s*(?:FIXTURE:|SUITE SUMMARY|RESULT:|SEVERITY:|MUST DETECT:|MUST NOT:|EVIDENCE HANDOFF:|CANDIDATE FIREWALL:)\s*|\Z)",
        block,
    )
    return match.group(1).strip() if match else ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Story Engine smoke report structure.")
    parser.add_argument("report", type=Path)
    parser.add_argument(
        "--partial",
        action="store_true",
        help="Allow a subset of fixture IDs instead of requiring the full 15-case suite.",
    )
    args = parser.parse_args()

    if not args.report.exists():
        print(f"FAIL: report not found: {args.report}")
        return 2

    text = args.report.read_text(encoding="utf-8")
    blocks = parse_blocks(text)
    errors: list[str] = []
    warnings: list[str] = []

    if not blocks:
        errors.append("No FIXTURE blocks found.")

    if not args.partial:
        missing = [fixture_id for fixture_id in ALL_IDS if fixture_id not in blocks]
        if missing:
            errors.append("Missing fixture IDs: " + ", ".join(missing))

    unknown = [fixture_id for fixture_id in blocks if fixture_id not in ALL_IDS]
    if unknown:
        errors.append("Unknown fixture IDs: " + ", ".join(sorted(unknown)))

    any_high_fail = False

    for fixture_id, block in blocks.items():
        result = (field(block, "RESULT") or "").upper()
        severity = (field(block, "SEVERITY") or "").upper()
        firewall = (field(block, "CANDIDATE FIREWALL") or "").upper()

        if result not in VALID_RESULTS:
            errors.append(f"{fixture_id}: RESULT must be PASS / FAIL / REVIEW.")

        if severity and severity not in VALID_SEVERITIES:
            errors.append(f"{fixture_id}: invalid SEVERITY '{severity}'.")

        if result == "FAIL" and severity in {"P0", "P1"}:
            any_high_fail = True

        if firewall and firewall not in {"PASS", "FAIL", "N/A"}:
            errors.append(f"{fixture_id}: CANDIDATE FIREWALL must be PASS / FAIL / N/A.")

        diagnosis = observed_diagnosis(block)
        if not diagnosis:
            warnings.append(f"{fixture_id}: no OBSERVED DIAGNOSIS text found.")
        else:
            leaked = [name for name in CANDIDATE_NAMES if re.search(re.escape(name), diagnosis, re.I)]
            if leaked:
                errors.append(
                    f"{fixture_id}: candidate-name leakage in OBSERVED DIAGNOSIS: "
                    + ", ".join(leaked)
                )

    summary_pass = bool(re.search(r"(?mi)^SUITE STATUS:\s*PASS\s*$", text))
    if summary_pass and any_high_fail:
        errors.append("Suite declares PASS while a P0/P1 fixture is FAIL.")

    for warning in warnings:
        print("WARN:", warning)
    for error in errors:
        print("FAIL:", error)

    if errors:
        print(f"\nREPORT CHECK: FAIL ({len(errors)} error(s), {len(warnings)} warning(s))")
        return 1

    print(f"REPORT CHECK: PASS ({len(blocks)} fixture block(s), {len(warnings)} warning(s))")
    print("Note: semantic Story Engine judgment still requires human/model review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

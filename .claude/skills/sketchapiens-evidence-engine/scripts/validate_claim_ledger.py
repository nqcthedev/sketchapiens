#!/usr/bin/env python3
"""Validate Sketchapiens canonical claim-ledger.json with no third-party deps.

This checker intentionally supports the JSON-Schema keywords used by
schemas/claim-ledger.schema.json plus cross-reference integrity.

Usage:
    python3 .claude/skills/sketchapiens-evidence-engine/scripts/validate_claim_ledger.py \
        videos/SKA-XXXX-slug/02-research/claim-ledger.json

Exit 0 = valid, exit 1 = invalid.
"""
from __future__ import annotations

import json
import os
import re
import sys
from typing import Any

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))
DEFAULT_SCHEMA = os.path.join(ROOT, "schemas", "claim-ledger.schema.json")


def _is_type(value: Any, name: str) -> bool:
    if name == "null":
        return value is None
    if name == "object":
        return isinstance(value, dict)
    if name == "array":
        return isinstance(value, list)
    if name == "string":
        return isinstance(value, str)
    if name == "boolean":
        return isinstance(value, bool)
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return True


def _matches_condition(value: Any, schema: dict[str, Any]) -> bool:
    """Small matcher for the `if` shape used by this schema."""
    required = schema.get("required", [])
    if isinstance(value, dict):
        if any(k not in value for k in required):
            return False
        for key, sub in schema.get("properties", {}).items():
            if key not in value:
                continue
            if "const" in sub and value[key] != sub["const"]:
                return False
    return True


def _validate(value: Any, schema: dict[str, Any], path: str, errors: list[str]) -> None:
    typ = schema.get("type")
    if typ is not None:
        allowed = typ if isinstance(typ, list) else [typ]
        if not any(_is_type(value, t) for t in allowed):
            errors.append(f"{path}: expected type {allowed}, got {type(value).__name__}")
            return

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} not in enum {schema['enum']}")

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {value!r}")

    if isinstance(value, str) and "pattern" in schema:
        if not re.fullmatch(schema["pattern"], value):
            errors.append(f"{path}: string does not match pattern {schema['pattern']!r}")

    if isinstance(value, int) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: {value} < minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: {value} > maximum {schema['maximum']}")

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: needs at least {schema['minItems']} item(s)")
        if schema.get("uniqueItems"):
            seen = set()
            for idx, item in enumerate(value):
                marker = json.dumps(item, sort_keys=True, ensure_ascii=False)
                if marker in seen:
                    errors.append(f"{path}[{idx}]: duplicate item not allowed")
                seen.add(marker)
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for idx, item in enumerate(value):
                _validate(item, item_schema, f"{path}[{idx}]", errors)

    if isinstance(value, dict):
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{path}: unexpected property {key!r}")
        for key, sub in props.items():
            if key in value and isinstance(sub, dict):
                _validate(value[key], sub, f"{path}.{key}", errors)

    for rule in schema.get("allOf", []):
        if not isinstance(rule, dict):
            continue
        cond = rule.get("if")
        then = rule.get("then")
        if isinstance(cond, dict) and isinstance(then, dict) and _matches_condition(value, cond):
            _validate(value, then, path, errors)


def _cross_reference_checks(data: dict[str, Any], errors: list[str]) -> None:
    sources = data.get("sources", [])
    claims = data.get("claims", [])
    bridges = data.get("bridges", [])

    source_ids = [x.get("id") for x in sources if isinstance(x, dict)]
    claim_ids = [x.get("id") for x in claims if isinstance(x, dict)]
    bridge_ids = [x.get("id") for x in bridges if isinstance(x, dict)]

    for label, ids in (("source", source_ids), ("claim", claim_ids), ("bridge", bridge_ids)):
        clean = [x for x in ids if isinstance(x, str)]
        if len(clean) != len(set(clean)):
            errors.append(f"$: duplicate {label} id(s)")

    source_set = set(x for x in source_ids if isinstance(x, str))
    claim_set = set(x for x in claim_ids if isinstance(x, str))

    for idx, claim in enumerate(claims):
        if not isinstance(claim, dict):
            continue
        for ref in claim.get("source_refs", []):
            if ref not in source_set:
                errors.append(f"$.claims[{idx}].source_refs: unknown source id {ref!r}")
        for ref in claim.get("depends_on", []):
            if ref not in claim_set:
                errors.append(f"$.claims[{idx}].depends_on: unknown claim id {ref!r}")
            if ref == claim.get("id"):
                errors.append(f"$.claims[{idx}].depends_on: claim cannot depend on itself")

    for idx, bridge in enumerate(bridges):
        if not isinstance(bridge, dict):
            continue
        for ref in bridge.get("source_refs", []):
            if ref not in source_set:
                errors.append(f"$.bridges[{idx}].source_refs: unknown source id {ref!r}")
        for ref in bridge.get("depends_on", []):
            if ref not in claim_set:
                errors.append(f"$.bridges[{idx}].depends_on: unknown claim id {ref!r}")


def validate_data(data: Any, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    _validate(data, schema, "$", errors)
    if isinstance(data, dict):
        _cross_reference_checks(data, errors)
    return errors


def validate_file(path: str, schema_path: str = DEFAULT_SCHEMA) -> list[str]:
    try:
        with open(schema_path, encoding="utf-8") as f:
            schema = json.load(f)
    except Exception as exc:
        return [f"schema load failed: {exc}"]

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:
        return [f"ledger load failed: {exc}"]

    return validate_data(data, schema)


def main(argv: list[str]) -> int:
    if len(argv) < 2 or len(argv) > 3:
        print("usage: validate_claim_ledger.py <ledger.json> [schema.json]")
        return 2
    ledger = argv[1]
    schema = argv[2] if len(argv) == 3 else DEFAULT_SCHEMA
    errors = validate_file(ledger, schema)
    if errors:
        print("CLAIM LEDGER INVALID")
        for err in errors:
            print(f"- {err}")
        return 1
    print("CLAIM LEDGER VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

#!/usr/bin/env python3
"""Validate Sketchapiens canonical Evidence ledger with no third-party deps.

Two layers:
1. validate_file() — JSON-schema subset + ledger internal cross references.
2. validate_video_ledger() — cross-artifact traceability for an SKA video:
   video_id, immutable versions, current.yaml and ledger script_ref freshness.

Usage:
    python3 .claude/skills/sketchapiens-evidence-engine/scripts/validate_claim_ledger.py \
        videos/SKA-XXXX-slug/02-research/claim-ledger.json

Exit 0 = valid ledger file, exit 1 = invalid.
Project gates should call validate_video_ledger(video_dir) when current-version
traceability matters.
"""
from __future__ import annotations

import glob
import hashlib
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
    """Small matcher for the `if` shapes used by the canonical schema."""
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


def _load_schema(schema_path: str) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        with open(schema_path, encoding="utf-8") as f:
            return json.load(f), []
    except Exception as exc:
        return None, [f"schema load failed: {exc}"]


def _load_ledger(path: str) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:
        return None, [f"ledger load failed: {exc}"]
    if not isinstance(data, dict):
        return None, ["ledger root must be an object"]
    return data, []


def validate_file(path: str, schema_path: str = DEFAULT_SCHEMA) -> list[str]:
    schema, errors = _load_schema(schema_path)
    if errors or schema is None:
        return errors
    data, errors = _load_ledger(path)
    if errors or data is None:
        return errors
    return validate_data(data, schema)


def _sha256_file(path: str) -> str | None:
    """Digest of exact script bytes, or None if unreadable."""
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except Exception:
        return None


def _check_script_digest(video_dir: str, ledger: dict[str, Any], script_ref: str, errors: list[str]) -> None:
    """Close G-01: a declared script_sha256 must match the bytes it claims to pin.

    Without this, the gate catches a ledger pointing at the wrong version but not
    someone editing a supposedly immutable vNNN.md in place.
    """
    declared = ledger.get("script_sha256")
    if declared is None:
        return
    target = os.path.join(video_dir, script_ref)
    actual = _sha256_file(target)
    if actual is None:
        errors.append(f"script_sha256 declared but {script_ref} could not be read for digest")
    elif actual != declared:
        errors.append(
            f"script content drift: ledger script_sha256={declared[:12]}... "
            f"but {script_ref} hashes to {actual[:12]}..."
        )


def _yaml_get(text: str, key: str) -> str | None:
    """Read a simple top-level scalar from the project's pointer/video YAML shape."""
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.M)
    if not match:
        return None
    value = match.group(1).strip().strip('"').strip("'")
    return None if value in ("", "null", "~") else value


def validate_video_ledger(video_dir: str, schema_path: str = DEFAULT_SCHEMA) -> list[str]:
    """Validate canonical ledger plus exact active-script traceability.

    This is the project-gate API used by preflight/project_doctor. It prevents a
    ledger verified for v001 from remaining green after current.yaml moves to v002.
    """
    errors: list[str] = []
    video_dir = os.path.abspath(video_dir)
    ledger_path = os.path.join(video_dir, "02-research", "claim-ledger.json")
    video_yaml = os.path.join(video_dir, "video.yaml")

    if not os.path.exists(ledger_path):
        return ["missing 02-research/claim-ledger.json"]
    errors.extend(validate_file(ledger_path, schema_path))
    if errors:
        return errors

    ledger, load_errors = _load_ledger(ledger_path)
    if load_errors or ledger is None:
        return load_errors

    if not os.path.exists(video_yaml):
        errors.append("missing video.yaml")
        return errors

    try:
        video_text = open(video_yaml, encoding="utf-8").read()
    except Exception as exc:
        return [f"video.yaml read failed: {exc}"]

    video_id = _yaml_get(video_text, "id")
    if ledger.get("video_id") != video_id:
        errors.append(f"ledger video_id={ledger.get('video_id')!r} does not match video.yaml id={video_id!r}")

    script_ref = ledger.get("script_ref")
    versions = sorted(glob.glob(os.path.join(video_dir, "03-script", "versions", "v[0-9][0-9][0-9].md")))
    current_yaml = os.path.join(video_dir, "03-script", "refs", "current.yaml")

    if not versions:
        if os.path.exists(current_yaml):
            errors.append("current.yaml exists before any immutable script version exists")
        if script_ref is not None:
            target = os.path.join(video_dir, script_ref)
            if not os.path.exists(target):
                errors.append(f"ledger script_ref target does not exist: {script_ref}")
            else:
                _check_script_digest(video_dir, ledger, script_ref, errors)
        return errors

    if not os.path.exists(current_yaml):
        errors.append("script version exists but 03-script/refs/current.yaml is missing")
        return errors

    try:
        current_text = open(current_yaml, encoding="utf-8").read()
    except Exception as exc:
        errors.append(f"current.yaml read failed: {exc}")
        return errors

    version = _yaml_get(current_text, "version")
    if not version or not re.fullmatch(r"v[0-9]{3}", version):
        errors.append("current.yaml version is missing/invalid; expected vNNN")
        return errors

    current_ref = f"03-script/versions/{version}.md"
    current_target = os.path.join(video_dir, current_ref)
    if not os.path.exists(current_target):
        errors.append(f"current.yaml target does not exist: {current_ref}")
        return errors

    if script_ref is None:
        errors.append("current script exists but ledger script_ref is null")
    elif script_ref != current_ref:
        errors.append(f"Evidence stale: ledger script_ref={script_ref} but current={current_ref}")

    if script_ref is not None:
        if not os.path.exists(os.path.join(video_dir, script_ref)):
            errors.append(f"ledger script_ref target does not exist: {script_ref}")
        else:
            _check_script_digest(video_dir, ledger, script_ref, errors)

    return errors


def main(argv: list[str]) -> int:
    if len(argv) < 2 or len(argv) > 3:
        print("usage: validate_claim_ledger.py <ledger.json | video_dir/> [schema.json]")
        print("  đưa THƯ MỤC video để chạy đủ truy vết + G-01 script digest")
        return 2
    target = argv[1]
    schema = argv[2] if len(argv) == 3 else DEFAULT_SCHEMA
    # VÁ 22/08 (08-A): đưa thư mục video thì chạy phép kiểm ĐẦY ĐỦ (gồm G-01 script digest).
    # Trước bản vá này, CLI luôn chạy validate_file() — CHỈ kiểm hình dạng schema — nên lệnh
    # mà /new-video bước 4 bảo chạy KHÔNG THỂ bắt trôi byte kịch bản. Nó in VALID rồi thôi.
    if os.path.isdir(target):
        errors = validate_video_ledger(target, schema)
    else:
        errors = validate_file(target, schema)
    if errors:
        print("CLAIM LEDGER INVALID")
        for err in errors:
            print(f"- {err}")
        return 1
    print("CLAIM LEDGER VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

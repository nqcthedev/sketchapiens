#!/usr/bin/env python3
"""Sketchapiens project doctor — kiểm tính toàn vẹn cấu trúc. READ-ONLY.

Không sửa bất cứ gì. Chỉ báo cáo PASS / WARN / FAIL.
Chạy:  python3 tools/project_doctor.py
"""
import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

RESULTS = []
def rec(level, check, detail=""):
    RESULTS.append((level, check, detail))

# Một source of truth cho video contract: doctor chỉ ĐỌC schema, không duy trì bản sao.
VIDEO_SCHEMA = "schemas/video.schema.json"
def load_video_contract():
    try:
        data = json.load(open(VIDEO_SCHEMA, encoding="utf-8"))
        states = data["properties"]["status"]["enum"]
        id_pattern = data["properties"]["id"]["pattern"]
        return states if isinstance(states, list) else [], id_pattern if isinstance(id_pattern, str) else ""
    except Exception:
        return [], ""

LIFECYCLE, VIDEO_ID_PATTERN = load_video_contract()

# Evidence ledger validation stays module-owned; doctor only calls the public deterministic checker.
EVIDENCE_VALIDATOR_PATH = ".claude/skills/sketchapiens-evidence-engine/scripts/validate_claim_ledger.py"
def load_evidence_validator():
    try:
        spec = importlib.util.spec_from_file_location("ska_evidence_validator", EVIDENCE_VALIDATOR_PATH)
        module = importlib.util.module_from_spec(spec)
        if not spec or not spec.loader:
            return None, "không tạo được import spec"
        spec.loader.exec_module(module)
        return module, ""
    except Exception as e:
        return None, repr(e)

# artefact bắt buộc cho từng trạng thái (thư mục tương đối trong videos/<ID>/)
REQUIRED = {
    "research":          ["02-research"],
    "drafting":          ["03-script/versions"],
    "review":            ["04-review"],
    "revision":          ["03-script/versions"],
    "approved":          ["03-script/refs/approved.yaml"],
    "packaging":         ["05-packaging"],
    "production":        ["06-production"],
    "ready_to_publish":  ["06-production"],
    "published":         ["07-publish", "03-script/refs/published.yaml"],
    "measured":          ["08-analytics"],
    "postmortem_complete":["08-analytics"],
}

# Chỉ các folder lịch sử tồn tại trước control plane mới được miễn video.yaml.
# Đây là migration allowlist cố định, KHÔNG phải naming pattern. Video mới tên Video21_* không được miễn.
LEGACY_VIDEO_DIRS = frozenset({
    "videos/Video17_Death",
    "videos/Video17_Rain",
    "videos/Video18_Sleep",
    "videos/Video19_Moon",
    "videos/Video19_NightWalk",
    "videos/Video20_Cold",
})

def is_legacy_video_dir(path):
    return os.path.normpath(path) in LEGACY_VIDEO_DIRS

# ── 1. Control plane đủ chưa
def check_control_plane():
    need = ["CLAUDE.md", ".gitignore", ".claude/settings.json",
            ".claude/hooks/guard_project.py",
            "governance/SOURCE_OF_TRUTH.md", "governance/DECISIONS_REQUIRED.md",
            "governance/RULE_REGISTRY.yaml", "governance/RETIRED_RULES.md",
            "governance/CHANGE_POLICY.md", "governance/MIGRATION_LOG.md",
            ".claude/skills/sketchapiens-evidence-engine/CONTRACT.md",
            EVIDENCE_VALIDATOR_PATH]
    missing = [p for p in need if not os.path.exists(p)]
    rec("FAIL" if missing else "PASS", "Control plane đủ file",
        "thiếu: " + ", ".join(missing) if missing else f"{len(need)}/{len(need)}")
    for d, n in ((".claude/agents", 3), (".claude/rules", 6), (".claude/skills", 6),
                 ("schemas", 4), ("templates", 6)):
        got = len(glob.glob(f"{d}/*")) if os.path.isdir(d) else 0
        rec("PASS" if got >= n else "FAIL", f"{d} có ≥{n} mục", f"thấy {got}")

# ── 2. JSON hợp lệ
def check_json():
    bad = []
    for f in glob.glob("schemas/*.json") + glob.glob("templates/*.json") + [".claude/settings.json", ".claude/settings.local.example.json"]:
        if not os.path.exists(f): continue
        try: json.load(open(f))
        except Exception as e: bad.append(f"{f}: {e}")
    rec("FAIL" if bad else "PASS", "JSON hợp lệ", "; ".join(bad) if bad else "schema/template JSON parse được")
    rec("PASS" if LIFECYCLE else "FAIL", "Lifecycle đọc được từ video.schema.json",
        f"{len(LIFECYCLE)} trạng thái" if LIFECYCLE else "không đọc được properties.status.enum")
    rec("PASS" if VIDEO_ID_PATTERN else "FAIL", "ID pattern đọc được từ video.schema.json",
        VIDEO_ID_PATTERN if VIDEO_ID_PATTERN else "không đọc được properties.id.pattern")

# ── 3. Frontmatter của agent / rule / skill
def frontmatter(path):
    try: t = open(path, encoding="utf-8").read()
    except Exception: return None
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    return m.group(1) if m else None

def check_frontmatter():
    for f in sorted(glob.glob(".claude/agents/*.md")):
        fm = frontmatter(f)
        ok = fm and "name:" in fm and "description:" in fm
        rec("PASS" if ok else "FAIL", f"agent frontmatter {os.path.basename(f)}",
            "" if ok else "thiếu name/description")
    for f in sorted(glob.glob(".claude/rules/*.md")):
        fm = frontmatter(f)
        ok = fm and "paths:" in fm
        rec("PASS" if ok else "FAIL", f"rule paths {os.path.basename(f)}",
            "" if ok else "thiếu paths:")
    for f in sorted(glob.glob(".claude/skills/*/SKILL.md")):
        fm = frontmatter(f)
        ok = fm and "name:" in fm and "description:" in fm
        rec("PASS" if ok else "FAIL", f"skill frontmatter {f.split('/')[-2]}",
            "" if ok else "thiếu name/description")

# ── 4. Hook chạy được
def check_hook():
    p = ".claude/hooks/guard_project.py"
    if not os.path.exists(p):
        rec("FAIL", "hook tồn tại"); return
    try:
        import ast; ast.parse(open(p, encoding="utf-8").read())
        rec("PASS", "hook cú pháp hợp lệ")
    except Exception as e:
        rec("FAIL", "hook cú pháp", str(e))
    rec("PASS" if os.access(p, os.X_OK) else "WARN", "hook có quyền chạy")

# ── 5. Video manifest + lifecycle
def yaml_get(text, key):
    m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.M)
    if not m: return None
    v = m.group(1).strip().strip('"').strip("'")
    return None if v in ("null", "~", "") else v

def check_videos():
    dirs = sorted(d for d in glob.glob("videos/*") if os.path.isdir(d))
    if not dirs:
        rec("WARN", "videos/ chưa có video nào",
            "bình thường sau khi cài control plane — migration là bước riêng"); return
    seen = {}
    for d in dirs:
        y = os.path.join(d, "video.yaml")
        if not os.path.exists(y):
            # Chỉ exact historical allowlist được miễn cho tới khi migrate.
            if is_legacy_video_dir(d):
                rec("WARN", f"{d} là legacy folder chưa migrate", "allowlist cố định; không ép video.yaml")
                continue
            rec("FAIL", f"{d} thiếu video.yaml"); continue
        t = open(y, encoding="utf-8").read()
        vid = yaml_get(t, "id")
        if not vid or not VIDEO_ID_PATTERN or not re.fullmatch(VIDEO_ID_PATTERN, vid):
            rec("FAIL", f"{d} id sai schema", str(vid)); continue
        if vid in seen:
            rec("FAIL", f"ID trùng: {vid}", f"{seen[vid]} và {d}")
        seen[vid] = d
        st = yaml_get(t, "status")
        if st not in LIFECYCLE:
            rec("FAIL", f"{vid} status không hợp lệ", str(st)); continue
        miss = [a for a in REQUIRED.get(st, []) if not os.path.exists(os.path.join(d, a))]
        rec("FAIL" if miss else "PASS", f"{vid} status '{st}' đủ artefact",
            "thiếu: " + ", ".join(miss) if miss else "")
        # không suy ra published
        if st == "published" and not os.path.isdir(os.path.join(d, "07-publish")):
            rec("FAIL", f"{vid} khai published mà không có 07-publish/",
                "không được suy ra trạng thái đăng")

# ── 6. Canonical Evidence ledger cho SKA-* videos
def check_claim_ledgers():
    validator, load_error = load_evidence_validator()
    if validator is None:
        rec("FAIL", "Evidence ledger validator load được", load_error)
        return
    rec("PASS", "Evidence ledger validator load được", EVIDENCE_VALIDATOR_PATH)

    ska_dirs = sorted(d for d in glob.glob("videos/SKA-*") if os.path.isdir(d) and os.path.exists(os.path.join(d, "video.yaml")))
    if not ska_dirs:
        rec("PASS", "Canonical claim ledger scan", "chưa có SKA-* video để validate")
        return

    for d in ska_dirs:
        video_yaml = os.path.join(d, "video.yaml")
        video_text = open(video_yaml, encoding="utf-8").read()
        vid = yaml_get(video_text, "id")
        ledger = os.path.join(d, "02-research", "claim-ledger.json")
        if not os.path.exists(ledger):
            rec("FAIL", f"{vid or d} canonical claim ledger", "thiếu 02-research/claim-ledger.json")
            continue

        errors = validator.validate_file(ledger)
        if errors:
            rec("FAIL", f"{vid or d} claim ledger schema/cross-ref", "; ".join(errors[:5]))
            continue

        try:
            data = json.load(open(ledger, encoding="utf-8"))
        except Exception as e:
            rec("FAIL", f"{vid or d} claim ledger parse", repr(e))
            continue

        if data.get("video_id") != vid:
            rec("FAIL", f"{vid or d} claim ledger video_id", f"ledger={data.get('video_id')!r}")
            continue

        script_ref = data.get("script_ref")
        versions = sorted(glob.glob(os.path.join(d, "03-script", "versions", "v[0-9][0-9][0-9].md")))
        if versions and not script_ref:
            rec("FAIL", f"{vid} Evidence traceability", "đã có script version nhưng ledger script_ref=null")
            continue
        if script_ref and not os.path.exists(os.path.join(d, script_ref)):
            rec("FAIL", f"{vid} Evidence script_ref", f"không tồn tại: {script_ref}")
            continue

        rec("PASS", f"{vid} canonical claim ledger", f"script_ref={script_ref or 'pre-draft'}")

# ── 7. Secret — chỉ báo vị trí
def check_secrets():
    pats = [(r"sk-[A-Za-z0-9]{20,}", "OpenAI-style"),
            (r"AIza[0-9A-Za-z_\-]{30,}", "Google"),
            (r"xi-[a-f0-9]{30,}", "ElevenLabs"),
            (r"ghp_[A-Za-z0-9]{30,}", "GitHub")]
    hits = []
    scope = []
    for ext in ("*.md", "*.py", "*.json", "*.yaml", "*.yml", "*.sh"):
        for f in glob.glob(ext) + glob.glob(f".claude/**/{ext}", recursive=True) \
               + glob.glob(f"governance/{ext}") + glob.glob(f"schemas/{ext}") \
               + glob.glob(f"templates/{ext}") + glob.glob(f"tools/{ext}"):
            scope.append(f)
    for f in scope:
        try: t = open(f, encoding="utf-8", errors="ignore").read()
        except Exception: continue
        for pat, name in pats:
            if re.search(pat, t):
                hits.append(f"{f} [{name}]")
    rec("FAIL" if hits else "PASS", "Không có secret trong phạm vi control plane",
        "; ".join(hits) if hits else f"quét {len(scope)} file")
    if os.path.exists(".env"):
        rec("FAIL", ".env tồn tại ở gốc", "không được commit")

# ── 8. .gitignore che đúng thứ nặng
def check_gitignore():
    if not os.path.exists(".gitignore"):
        rec("FAIL", ".gitignore tồn tại"); return
    t = open(".gitignore", encoding="utf-8").read()
    need = ["2_KHO_BANGHI/", ".env", "*.mp3", "*.png", "PROMPTS_FULL.txt",
            "GhepVideo_Desktop/", "node_modules/", "settings.local.json"]
    miss = [n for n in need if n not in t]
    rec("FAIL" if miss else "PASS", ".gitignore che đủ",
        "thiếu: " + ", ".join(miss) if miss else "")

# ── 9. Dữ liệu cũ còn nguyên
def check_legacy_intact():
    present = sorted(p for p in LEGACY_VIDEO_DIRS if os.path.isdir(p))
    missing = sorted(LEGACY_VIDEO_DIRS.difference(present))
    rec("WARN" if missing else "PASS", "Thư mục video legacy allowlist còn nguyên",
        ("thiếu: " + ", ".join(missing)) if missing else f"{len(present)}/{len(LEGACY_VIDEO_DIRS)} folder")
    roots = len(glob.glob("*.md")) + len(glob.glob("*.txt"))
    rec("PASS" if roots >= 2 else "WARN", "File gốc kho còn nguyên", f"{roots} file .md/.txt ở gốc")
    for p in ["00_LUAT_HIEN_HANH.md", "governance/PROJECT_FULL_AUDIT_EXPORT.md", "2_KHO_BANGHI/00_KHO.md"]:
        rec("PASS" if os.path.exists(p) else "FAIL", f"còn {p}")

# ── 10. Quyết định treo
def check_decisions():
    p = "governance/DECISIONS_REQUIRED.md"
    if not os.path.exists(p): rec("FAIL", "DECISIONS_REQUIRED.md tồn tại"); return
    t = open(p, encoding="utf-8").read()
    open_n = t.count("NEEDS_HUMAN_DECISION")
    rec("WARN" if open_n else "PASS", "Quyết định còn treo", f"{open_n} mục")

for fn in (check_control_plane, check_json, check_frontmatter, check_hook,
           check_videos, check_claim_ledgers, check_secrets, check_gitignore,
           check_legacy_intact, check_decisions):
    try: fn()
    except Exception as e: rec("FAIL", f"{fn.__name__} lỗi khi chạy", repr(e))

W = {"PASS": 0, "WARN": 0, "FAIL": 0}
print("═" * 72)
print("  SKETCHAPIENS PROJECT DOCTOR — read-only")
print("═" * 72)
for lvl, check, detail in RESULTS:
    W[lvl] += 1
    icon = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌"}[lvl]
    print(f"{icon} {check}" + (f"  →  {detail}" if detail else ""))
print("─" * 72)
print(f"  PASS {W['PASS']}   WARN {W['WARN']}   FAIL {W['FAIL']}")
print("═" * 72)
sys.exit(1 if W["FAIL"] else 0)

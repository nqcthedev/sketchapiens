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

# ── 3b. Đường dẫn nhắc trong agent phải tồn tại  (Phase 5 · nguyên tắc N-3)
# Một đường dẫn chết trong agent KHÔNG gây lỗi ồn ào. Nó lặng lẽ tốn một tool call mỗi
# lượt chạy và làm agent mở đầu bản chấm bằng một câu xin lỗi. `anti-ai-narration-critic`
# trỏ `knowledge/writing/**` suốt nhiều tuần — thư mục chưa từng được tạo.
# Xem governance/audits/phase5-agents/05A-D finding F-6.
_AGENT_PATH_RE = re.compile(r"`([A-Za-z0-9_./-]+/[A-Za-z0-9_./*-]*)`")

# Chỉ soi đường dẫn NEO TỪ GỐC REPO. Đường dẫn tương đối trong agent — ví dụ
# `references/prose-and-voice.md` — là tương đối với skill nào đó, không phải với root,
# nên không kiểm được ở đây mà không đoán mò. Whitelist prefix là cách duy nhất tránh
# false positive mà vẫn bắt được ca thật như `knowledge/writing/**`.
_ROOT_PREFIX = (
    ".claude/", "videos/", "kho/", "governance/", "tools/", "schemas/",
    "templates/", "identity/", "knowledge/", "2_KHO_BANGHI/",
)


def check_agent_paths():
    for f in sorted(glob.glob(".claude/agents/*.md")):
        body = open(f, encoding="utf-8").read()
        chet = []
        for raw in set(_AGENT_PATH_RE.findall(body)):
            if not raw.startswith(_ROOT_PREFIX):
                continue
            goc = raw.split("*")[0].rstrip("/")
            if not goc or "/" not in goc:
                continue
            if not (os.path.exists(goc) or glob.glob(goc + "*")):
                chet.append(raw)
        ten = os.path.basename(f)
        rec("PASS" if not chet else "FAIL", f"agent paths {ten}",
            "" if not chet else "đường dẫn không tồn tại: " + ", ".join(sorted(chet)[:3]))


# ── 3c. Luật đã chết còn sống trên BỀ MẶT THI HÀNH   (07B-A)
#
# ⛔ KHÔNG quét văn xuôi. Trong kho này, nhắc tên một luật đã chết KÈM BIA MỘ là
# trạng thái LÀNH MẠNH — kỷ luật nghĩa địa bắt buộc consumer mang dấu ⛔.
# Đo ở 07A-B: quét thô 62 trúng / 2 thật (3%); lọc bia mộ còn 22 / 2 thật (9%).
# Check bắn vào bia mộ sẽ làm doctor đỏ vĩnh viễn, và người kế tiếp sẽ GỠ BIA MỘ
# cho doctor xanh — tức check tự tay xoá đúng lớp bảo vệ nó sinh ra để giữ.
#
# Tín hiệu không nằm ở "token có mặt hay không", mà ở "token nằm trên bề mặt nào".
# BỀ MẶT THI HÀNH = chỗ con số/tên được dùng để QUYẾT một cái gì đó:
#   A. dòng checklist  | ☐ | … |  hoặc  - [ ]     — người tick ô là người thi hành
#   B. giá trị chuỗi trong schemas/*.json          — enum/const là hợp đồng máy thi hành
# Kiểm chứng 07A-B: cả 2 lỗi thật nằm trên bề mặt thi hành, cả ~60 dương tính giả
# nằm trong văn xuôi. Không ngoại lệ nào theo chiều nào.
#
# Nguồn của chính lớp check này — RETIRED_RULES.md 09/08:
#   "Sửa luật ở tầng 1 mà không sửa tầng 2, skill, lệnh và MÁY thì luật cũ vẫn đang chạy."
DEAD_REGISTRY = "governance/RETIRED_RULES.registry.json"

# Bề mặt A — dòng checklist. Ô chưa tick là lệnh chờ người thi hành.
_CHECKLIST_RE = re.compile(r"^\s*(?:\|\s*(?:☐|☑|\[[ xX]?\])\s*\||[-*]\s*\[[ xX]?\])")

_DEAD_SCAN_GLOBS = (".claude/skills/**/*.md", ".claude/agents/*.md", ".claude/rules/*.md",
                    "kho/1_luat/**/*.md", "templates/**/*.md", "CLAUDE.md")
# Nghĩa địa, báo cáo audit, kết quả test và kho lưu trữ ĐƯỢC nhắc tên luật đã chết.
_DEAD_SCAN_SKIP = ("/tests/", "/audit/", "/audits/", "RETIRED_RULES",
                   "_KHO_LUU_DaChet", "kho/4_luutru", "_cu_SKILL", "-legacy")

# BIA MỘ CÙNG DÒNG — không phải cửa sổ ±2 dòng.
# `CHECKLIST_KICHBAN.md:77` là ca dạy ra luật này: dòng checklist đó viết
#   `- [ ] ④ NGƯỜI XEM — you/we · người dẫn có xưng "tôi" không *(luật `I ≈ 0` đã khai tử)*`
# tức ô tick BẢO người soát nhìn ngôi kể VÀ nói thẳng luật cũ đã chết. Đó là file LÀNH.
# Bắn vào nó là đúng defect mà L-5 cấm.
# Hàng rào để CÙNG DÒNG chứ không phải ±2 dòng vì đó chính là kỷ luật nghĩa địa
# tự đặt ra — RETIRED_RULES.md: "Mỗi chỗ chết có dấu ⛔ TẠI CHỖ."
# Nên check này đo đúng một thứ: luật đã chết nằm trên bề mặt thi hành mà KHÔNG mang bia mộ.
_BIA_MO_RE = re.compile(
    r"⛔|🪦|đã gỡ|đã chết|đã bỏ|khai tử|đã retire|bị bác|đã bác|"
    r"lỗi thời|không còn|thay bằng|đừng đuổi|ĐÃ BỊ BÁC", re.I)


def _load_dead_rules():
    """Đọc registry. L-7: doctor KHÔNG nuôi bản sao thứ hai của danh sách này."""
    if not os.path.exists(DEAD_REGISTRY):
        return None
    try:
        data = json.load(open(DEAD_REGISTRY, encoding="utf-8"))
    except Exception:
        return None
    out = []
    for e in data.get("luat_da_chet", []):
        if not e.get("nguon"):      # không nguồn thì không được làm cửa chặn
            continue
        try:
            pat = re.compile(e["pattern"], re.I)
            ctx = re.compile(e["boi_canh"], re.I) if e.get("boi_canh") else None
        except re.error:
            continue
        out.append((e["id"], e.get("ten", e["id"]), pat, ctx, e.get("thay_bang", "")))
    return out


def _json_strings(node, path=""):
    """Mọi giá trị chuỗi trong một cây JSON, kèm đường đi tới nó."""
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield from _json_strings(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _json_strings(v, f"{path}[{i}]")


def check_dead_rules():
    luat = _load_dead_rules()
    if luat is None:
        rec("WARN", "Registry luật đã chết", f"chưa có {DEAD_REGISTRY} — không quét được")
        return
    if not luat:
        rec("WARN", "Registry luật đã chết", "registry rỗng hoặc mọi mục thiếu `nguon`")
        return

    hits = []

    # ── Bề mặt A: dòng checklist
    files = sorted({f for g in _DEAD_SCAN_GLOBS for f in glob.glob(g, recursive=True)
                    if not any(k in f for k in _DEAD_SCAN_SKIP)})
    for f in files:
        try:
            lines = open(f, encoding="utf-8", errors="replace").read().split("\n")
        except Exception:
            continue
        for i, ln in enumerate(lines, 1):
            if not _CHECKLIST_RE.match(ln):
                continue
            if _BIA_MO_RE.search(ln):
                continue                       # ô tick tự mang bia mộ — LÀNH
            for _id, ten, pat, ctx, thay in luat:
                if pat.search(ln) and (ctx is None or ctx.search(ln)):
                    hits.append((f"{f}:{i}", ten, thay))

    # ── Bề mặt B: giá trị chuỗi trong schemas/*.json
    for f in sorted(glob.glob("schemas/*.json")):
        try:
            data = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue        # check_json đã báo JSON hỏng rồi
        for where, val in _json_strings(data):
            for _id, ten, pat, ctx, thay in luat:
                if pat.search(val) and (ctx is None or ctx.search(val)):
                    hits.append((f"{f} → {where}", ten, thay))

    if not hits:
        rec("PASS", "Luật đã chết không còn trên bề mặt thi hành",
            f"{len(luat)} luật × {len(files)} file checklist + schemas/")
        return
    for cho, ten, thay in hits:
        rec("FAIL", f"luật đã chết đang được THI HÀNH: {ten}",
            f"{cho} — thay bằng: {thay}" if thay else cho)


# ── 3d. TOÀN VẸN ARTEFACT — một cái TÊN phải trỏ vào thứ CÓ THẬT   (07B-B)
#
# Ba check dưới đây cùng MỘT họ: chỗ nào khai một cái tên, chỗ đó phải có thứ mang tên ấy.
# Cùng họ với check_agent_paths (05B-D) — khác ở chỗ kia soi ĐƯỜNG DẪN, đây soi KHOÁ và CON TRỎ.

_REF_GLOB = "videos/*/03-script/refs"


def check_owner_pointers():
    """G7-2 — con trỏ approved/published phải có `set_by: owner`.

    Hook `guard_project.py` chặn lúc GHI. Doctor canh TRẠNG THÁI ĐANG CÓ.
    Hai lớp khác nhau: `git merge`, `git restore`, sửa tay ngoài Claude đều đi vòng qua hook.
    """
    found = []
    for d in sorted(glob.glob(_REF_GLOB)):
        for ten in ("approved", "published"):
            f = os.path.join(d, f"{ten}.yaml")
            if os.path.exists(f):
                found.append((f, ten))
    if not found:
        # L-6: không có input thì KHÔNG được in PASS — đó là PASS giả, đúng bệnh cổng P4
        # của preflight.py mất tới 22/08 mới vá. Hàng rào này canh cho Phase 8.
        rec("WARN", "Con trỏ approved/published có `set_by: owner`",
            "0 con trỏ trong repo — chưa canh được gì; hàng rào cho Phase 8 (V21)")
        return
    thieu = []
    for f, ten in found:
        try:
            body = open(f, encoding="utf-8").read()
        except Exception as e:
            thieu.append(f"{f} (không đọc được: {e})"); continue
        if not re.search(r"^\s*set_by:\s*owner\s*$", body, re.M):
            thieu.append(f)
    rec("FAIL" if thieu else "PASS", "Con trỏ approved/published có `set_by: owner`",
        ("thiếu set_by: owner — " + ", ".join(thieu[:3])) if thieu
        else f"{len(found)} con trỏ, đủ cả")


def _walk_enums(node, path=""):
    """Mọi dict có khai `$thuc_the`, kèm đường đi tới nó."""
    if isinstance(node, dict):
        if "$thuc_the" in node and isinstance(node.get("enum"), list):
            yield path, node
        for k, v in node.items():
            yield from _walk_enums(v, f"{path}.{k}" if path else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from _walk_enums(v, f"{path}[{i}]")


def check_entity_enums():
    """G7-8 tổng quát hoá — enum khai `$thuc_the` thì mọi giá trị phải là thực thể CÓ THẬT.

    Không hardcode đường dẫn nào trong doctor (L-7): chính schema khai nó tìm thực thể ở đâu,
    và khai giá trị nào KHÔNG phải thực thể (`$thuc_the_tru`).
    """
    tong = xau = 0
    for f in sorted(glob.glob("schemas/*.json")):
        try:
            data = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue                        # check_json đã báo JSON hỏng
        for where, node in _walk_enums(data):
            tong += 1
            pat = node["$thuc_the"]
            tru = set(node.get("$thuc_the_tru", []))
            co = {os.path.splitext(os.path.basename(x))[0] for x in glob.glob(pat)}
            ma = sorted(v for v in node["enum"] if v not in tru and v not in co)
            if ma:
                xau += 1
                rec("FAIL", f"enum gọi tên KHÔNG tồn tại: {os.path.basename(f)}",
                    f"{where} → {', '.join(ma[:4])} (tìm trong `{pat}`)")
    if tong and not xau:
        rec("PASS", "Enum khai `$thuc_the` gọi đúng thực thể có thật", f"{tong} enum")
    elif not tong:
        rec("WARN", "Enum khai `$thuc_the`", "chưa schema nào khai — không canh được gì")


def check_bg_keys():
    """G7-10 — mọi khoá nền dùng trong shot_data.py phải có thật.

    `build_prompts.py` tra `BG[bg]`; thiếu khoá thì nó KeyError giữa chừng — video đó
    không dựng lại được prompt. Im lặng cho tới khi có người thử.
    Nguồn nền: `identity/style.py` BG, cộng `BG_THEM` khai trong shot_data.py của từng video.
    """
    try:
        sys.path.insert(0, os.path.join(ROOT, "identity"))
        import importlib
        style = importlib.import_module("style")
        CHUNG = set(getattr(style, "BG", {}))
    except Exception as e:
        rec("WARN", "Khoá nền dùng trong shot_data.py", f"không nạp được identity/style.py: {e!r}")
        return
    dirs = sorted(os.path.dirname(f) for f in glob.glob("videos/*/shot_data.py"))
    if not dirs:
        rec("WARN", "Khoá nền dùng trong shot_data.py", "không video nào có shot_data.py")
        return
    for d in dirs:
        f = os.path.join(d, "shot_data.py")
        try:
            spec = importlib.util.spec_from_file_location("_sd_probe", f)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
        except Exception as e:
            rec("FAIL", f"{os.path.basename(d)} shot_data.py nạp được", repr(e)[:90]); continue
        rieng = set(getattr(m, "BG_THEM", {}))
        dung = {s[4] for s in getattr(m, "SHOTS", []) if len(s) > 4 and isinstance(s[4], str)}
        ma = sorted(dung - CHUNG - rieng)
        if not ma:
            rec("PASS", f"{os.path.basename(d)} khoá nền có thật", f"{len(dung)} nền"); continue
        # Video legacy đã SẢN XUẤT XONG bằng một style.py cũ hơn — prompt của chúng là
        # BẢN GHI LỊCH SỬ, không phải thứ cần dựng lại. Báo WARN để không giấu, nhưng
        # không để doctor đỏ vĩnh viễn. Video MỚI (ngoài allowlist) thì FAIL thật.
        cu_hay_moi = "WARN" if is_legacy_video_dir(d) else "FAIL"
        them = " (legacy — dựng xong bằng style.py cũ)" if cu_hay_moi == "WARN" else ""
        rec(cu_hay_moi, f"{os.path.basename(d)} khoá nền có thật",
            f"không có trong identity/style.py BG lẫn BG_THEM: {', '.join(ma[:4])}"
            f" — build_prompts.py sẽ KeyError{them}")


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

def current_script_ref_for_dir(video_dir):
    pointer = os.path.join(video_dir, "03-script", "refs", "current.yaml")
    if not os.path.exists(pointer):
        return None, "missing"
    try:
        version = yaml_get(open(pointer, encoding="utf-8").read(), "version")
    except Exception as e:
        return None, f"read error: {e}"
    if not version or not re.fullmatch(r"v[0-9]{3}", version):
        return None, "invalid version; expected vNNN"
    script_ref = f"03-script/versions/{version}.md"
    if not os.path.exists(os.path.join(video_dir, script_ref)):
        return script_ref, "target missing"
    return script_ref, "ok"

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
        current_ref, current_state = current_script_ref_for_dir(d)

        if not versions and current_state != "missing":
            rec("FAIL", f"{vid} current script pointer", "current.yaml tồn tại trước khi có script version")
            continue

        if versions:
            if current_state == "missing":
                rec("FAIL", f"{vid} current script pointer", "đã có script version nhưng thiếu 03-script/refs/current.yaml")
                continue
            if current_state != "ok":
                rec("FAIL", f"{vid} current script pointer", f"{current_state}: {current_ref or ''}")
                continue
            if not script_ref:
                rec("FAIL", f"{vid} Evidence traceability", "đã có current script nhưng ledger script_ref=null")
                continue
            if script_ref != current_ref:
                rec("FAIL", f"{vid} Evidence stale", f"ledger={script_ref} nhưng current={current_ref}")
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

for fn in (check_control_plane, check_json, check_frontmatter, check_agent_paths,
           check_dead_rules, check_owner_pointers, check_entity_enums,
           check_bg_keys, check_hook,
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

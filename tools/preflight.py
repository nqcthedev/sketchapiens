#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PREFLIGHT — mỗi cổng phải để lại một FILE. Không có file = cổng chưa chạy.

    python3 tools/preflight.py videos/Video19_Moon
    python3 tools/preflight.py videos/SKA-0021-example

Legacy Video17–20 giữ compatibility gate cũ. SKA-* dùng canonical Evidence ledger.
"""
import glob
import importlib.util
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
name = os.path.basename(V)
IS_SKA = bool(re.fullmatch(r"SKA-[0-9]{4}-[a-z0-9-]+", name))


def has(pat):
    g = glob.glob(os.path.join(V, pat)) + glob.glob(os.path.join(V, "_nhap", pat))
    return g[0] if g else None


def mtime(p):
    return os.path.getmtime(p) if p and os.path.exists(p) else 0


def yaml_get(text, key):
    m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.M)
    if not m:
        return None
    value = m.group(1).strip().strip('"').strip("'")
    return None if value in ("null", "~", "") else value


def current_script_ref():
    """Return canonical active immutable script ref for an SKA video.

    None means there is no current pointer. An invalid/missing target is returned
    as a ref and rejected by the caller so stale/broken pointers cannot go green.
    """
    pointer = os.path.join(V, "03-script", "refs", "current.yaml")
    if not os.path.exists(pointer):
        return None
    try:
        version = yaml_get(open(pointer, encoding="utf-8").read(), "version")
    except Exception:
        return "__INVALID_CURRENT_POINTER__"
    if not version or not re.fullmatch(r"v[0-9]{3}", version):
        return "__INVALID_CURRENT_POINTER__"
    return f"03-script/versions/{version}.md"


rows, fail = [], 0


def chk(cong, ten, ok, ghi=""):
    global fail
    rows.append((cong, ten, ok, ghi))
    if not ok:
        fail += 1


chot = has("CHOT_*.md")
moneo = has("MONEO_*.md")
ket = has("KET_*.md")
narr = has("Script_*_narration.txt")
versions = []
active_script_ref = None
if IS_SKA:
    versions = sorted(glob.glob(os.path.join(V, "03-script", "versions", "v[0-9][0-9][0-9].md")))
    active_script_ref = current_script_ref()
    if active_script_ref and active_script_ref != "__INVALID_CURRENT_POINTER__":
        active_path = os.path.join(V, active_script_ref)
        narr = active_path if os.path.exists(active_path) else None
    elif not narr:
        # Display/help fallback only. Evidence gate below still requires a current pointer.
        narr = versions[-1] if versions else None
shots = has("shot_data.py")
prom = has("PROMPTS_FULL.txt")


# ── Evidence gate generation split ──────────────────────────────────────────
def check_ska_evidence():
    ledger = os.path.join(V, "02-research", "claim-ledger.json")
    if not os.path.exists(ledger):
        return False, "thiếu 02-research/claim-ledger.json"

    validator_path = os.path.join(
        ROOT,
        ".claude",
        "skills",
        "sketchapiens-evidence-engine",
        "scripts",
        "validate_claim_ledger.py",
    )
    if not os.path.exists(validator_path):
        return False, "thiếu Evidence ledger validator"

    try:
        spec = importlib.util.spec_from_file_location("ska_evidence_validator", validator_path)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        errors = module.validate_file(ledger)
    except Exception as exc:
        return False, f"validator lỗi: {exc}"

    if errors:
        return False, "ledger invalid: " + "; ".join(errors[:3])

    try:
        data = json.load(open(ledger, encoding="utf-8"))
    except Exception as exc:
        return False, f"ledger parse lỗi: {exc}"

    # Cổng research không dùng quota citation. Nhưng template rỗng chưa chứng minh research đã chạy.
    if not data.get("claims") or not data.get("sources"):
        return False, "ledger schema hợp lệ nhưng chưa có claim/source evidence"

    script_ref = data.get("script_ref")

    # Pre-draft research may have no script version/current pointer and remains not lockable.
    if versions:
        if active_script_ref is None:
            return False, "đã có script version nhưng thiếu 03-script/refs/current.yaml"
        if active_script_ref == "__INVALID_CURRENT_POINTER__":
            return False, "03-script/refs/current.yaml thiếu/sai version: vNNN"
        active_target = os.path.join(V, active_script_ref)
        if not os.path.exists(active_target):
            return False, f"current pointer trỏ file không tồn tại: {active_script_ref}"
        if not script_ref:
            return False, "đã có current script nhưng ledger chưa bind script_ref"
        if script_ref != active_script_ref:
            return False, f"Evidence stale: ledger={script_ref} nhưng current={active_script_ref}"

    if script_ref:
        target = os.path.join(V, script_ref)
        if not os.path.exists(target):
            return False, f"script_ref không tồn tại: {script_ref}"

    return True, f"{len(data.get('claims', []))} claim · {len(data.get('sources', []))} source · {script_ref or 'pre-draft'}"


chk(
    0,
    "đề tài có cầu — số thật đã ghi",
    bool(has("CAU_*.md")) or (chot and re.search(r"C[ẦÂ]U|≥ ?100K|breakout", open(chot, encoding="utf-8").read(), re.I)),
    "→ _nhap/CAU_*.md",
)
chk(
    1,
    "kéo bản ghi quả to nhất",
    bool(has("DOITHU_*.md")) or (chot and "cú bẻ lái" in open(chot, encoding="utf-8").read().lower()),
    "→ _nhap/DOITHU_*.md",
)
chk(2, "cú bẻ lái KHÁC + khối mới", bool(chot) and "bẻ lái" in open(chot, encoding="utf-8").read().lower(), "ghi trong CHOT")

if IS_SKA:
    evidence_ok, evidence_detail = check_ska_evidence()
    chk(3, "claim-ledger có evidence + đúng current script", evidence_ok, evidence_detail)
else:
    # Legacy compatibility only: citation-shaped count from MONEO-era workflow.
    CIT = r"10\.\d{4}/|doi\.org|PMC\d+|(?:PLoS|PLOS|Science|Nature|PNAS|Proc\.? R\.? Soc|Current Anthropology|Journal|Sci Adv|Med Hist)[^\n]{0,60}?\d+"
    n_doi = len(set(re.findall(CIT, open(moneo, encoding="utf-8").read()))) if moneo else 0
    chk(3, f"mỏ neo legacy có trích dẫn kiểm được ({n_doi})", n_doi >= 3, "legacy MONEO: ≥3 citation-shaped anchors")

chk(4, "CỔNG A — quét tự trùng lặp", bool(has("CONGA_*.md")) or (chot and "cổng a" in open(chot, encoding="utf-8").read().lower()), "→ _nhap/CONGA_*.md")
chk(5, "viết ĐOẠN KẾT TRƯỚC", bool(ket) and (mtime(ket) < mtime(narr) if narr else True), "KET_*.md phải CŨ HƠN narration")
chk(6, "QA từng chương", bool(has("QA_*.md")) or bool(narr), "chạy qa_kichban.py")
chk(8, "VẼ ĐƯỢC bằng người que?", bool(has("VEDUOC_*.md")), "→ _nhap/VEDUOC_*.md · đếm món NHÌN THẤY vs cơ chế VÔ HÌNH")
chk(9, "CHỦ NGHE bản tiếng Việt + chốt", bool(has("CHOTNGHE_*.md")), "→ _nhap/CHOTNGHE_*.md · nghe TTS vi-VN, không duyệt bằng mắt")
chk(10, "người nghe ngoài (chat lạnh)", bool(has("KETQUA_CONG4.md")), "→ _nhap/KETQUA_CONG4.md")
chk("T", "title đã đối chiếu bảng 159 video", bool(chot) and re.search(r"159|c[ôo]ng th[ứu]c title|PH[ẦA]N C", open(chot, encoding="utf-8").read(), re.I), "HE_THONG PHẦN C")
chk("S", "chia shot + prompt", bool(shots) and bool(prom), "chạy validate_shots.py")

# ── GIAI ĐOẠN 2 — SẢN XUẤT (chỉ chấm khi kịch bản đã xong) ────────────────
n_prompt = len(re.findall(r"^\d{3}\.", open(prom, encoding="utf-8").read(), re.M)) if prom else 0
BO = ("_cu", "_hong", "_nhap", "kiem", "REF", "backup", "__pycache__")


def _sach(fs):
    return [f for f in fs if not any(b in f for b in BO)]


imgs = [
    f
    for f in glob.glob(os.path.join(V, "anh", "*.png")) + glob.glob(os.path.join(V, "anh", "*.jpg"))
    if "thumb" not in os.path.basename(f).lower()
]
# ⛔ VÁ 22/08: `V/**/X` trong Python glob KHÔNG khớp file nằm ngay trong V, chỉ khớp
# file trong thư mục con. Cổng P4 vì thế báo ĐỎ GIẢ suốt: V20 có đủ ba file thumbnail
# (THUMB_V20_banA.jpg · THUMBNAIL_PROMPT.txt · THUMBNAIL_V20.md) ở gốc thư mục video mà
# cổng không thấy cái nào. mp3/mp4 dính cùng bug nhưng chưa lộ vì file nằm trong thư mục con.
# Kho đã hai lần bị XANH GIẢ và đã vá; đây là ca NGƯỢC — đỏ giả — nên không ai đi tìm.
def _quet(pat):
    """Khớp cả file ở gốc video lẫn file trong thư mục con."""
    return glob.glob(os.path.join(V, pat)) + glob.glob(os.path.join(V, "**", pat), recursive=True)


mp3 = _sach(_quet("*.mp3"))
mp4 = _sach(_quet("*.mp4"))
# ⛔ VÁ 22/08 — BUG THỨ HAI, cùng cổng: pattern `*humb*` là chữ thường, nhưng file thật
# tên `THUMBNAIL_PROMPT.txt` / `THUMB_V20_banA.jpg` viết HOA. Python glob case-sensitive
# trên POSIX nên `humb` không bao giờ khớp `HUMB`. Hai bug chồng nhau ở đúng một cổng, và
# cả hai đều làm cổng ĐỎ GIẢ — nên không ai nghi.
thumb = sorted({f for f in _quet("*") if "humb" in os.path.basename(f).lower()})
meta = has("METADATA_*.md") or has("MOTA_*.md")

if n_prompt:
    chk("P1", f"ảnh == prompt ({len(imgs)}/{n_prompt})", len(imgs) == n_prompt, "gen 1 LƯỢT vào thư mục RỖNG · V14 lệch +52")
    chk("P2", f"tiếng ({len(mp3)} mp3)", len(mp3) > 0, "nạp SHOTLINES_FULL.txt")
    chk("P3", f"ghép ({len(mp4)} mp4)", len(mp4) > 0, "dùng APP, không viết script — V15 hỏng tiếng")
    chk("P4", "thumbnail (bước CUỐI)", bool(thumb), "chữ phải nói điều TITLE KHÔNG nói")
    p5_note = "dùng claim-ledger/source provenance" if IS_SKA else "dán MONEO xuống mô tả + disclaimer"
    chk("P5", "metadata + REFERENCES", bool(meta), p5_note)
    chk("P6", "mid-roll đã đặt tay", bool(has("DANG_*.md")), "→ DANG_*.md · phút 4 và 8")

print("═" * 70)
print(f"  PREFLIGHT — {name}")
print("═" * 70)
for c, t, ok, g in rows:
    print(f"  {'✅' if ok else '⛔'} cổng {str(c):>2}  {t:<42} {'' if ok else g}")
print("─" * 70)
print("  ✅ ĐỦ CỔNG — được đi tiếp." if not fail else f"  ⛔ CÒN {fail} CỔNG CHƯA CÓ DẤU VẾT. Chưa chạy thì nói CHƯA, đừng im.")

if narr:
    print()
    chua = [(c, t, g) for c, t, ok, g in rows if not ok]
    print()
    print("  " + "━" * 66)
    print("  ▶ LÀM TIẾP — ba việc gần nhất, không cần nhớ gì khác:")
    for i, (c, t, g) in enumerate(chua[:3], 1):
        print(f"     {i}. cổng {c} · {t}")
        print(f"        {g}")
    if len(chua) > 3:
        print(f"     … và {len(chua)-3} cổng nữa. Xem hết: kho/1_luat/CHECKLIST_KICHBAN.md")
    print("  " + "━" * 66)
    print(f"  đọc kịch bản (KHÔNG chấm bằng máy):  python3 tools/soi_kich_ban.py {narr}")

sys.exit(1 if fail else 0)

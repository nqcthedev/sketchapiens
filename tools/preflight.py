#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PREFLIGHT — mỗi cổng phải để lại một FILE. Không có file = cổng chưa chạy.

    python3 tools/preflight.py videos/Video19_Moon

Vì sao có file này: 10/08/2026 chủ phải nhắc BẢY lần trong một buổi, cả bảy đều là
thứ đã nằm sẵn trong kho. Không thiếu thông tin — thiếu thứ CHẶN.
Bài học từ cùng ngày: validate_shots.py bắt được lỗi thiếu một dòng lời đọc mà đọc tay
ba lượt không thấy. Máy chặn > người cẩn thận.
"""
import os, re, sys, glob

V = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
name = os.path.basename(V)
def has(pat):
    g = glob.glob(os.path.join(V, pat)) + glob.glob(os.path.join(V, "_nhap", pat))
    return g[0] if g else None
def mtime(p): return os.path.getmtime(p) if p and os.path.exists(p) else 0

rows, fail = [], 0
def chk(cong, ten, ok, ghi=""):
    global fail
    rows.append((cong, ten, ok, ghi))
    if not ok: fail += 1

chot  = has("CHOT_*.md")
moneo = has("MONEO_*.md")
ket   = has("KET_*.md")
narr  = has("Script_*_narration.txt")
shots = has("shot_data.py")
prom  = has("PROMPTS_FULL.txt")

chk(0,  "đề tài có cầu — số thật đã ghi",  bool(has("CAU_*.md")) or (chot and re.search(r"C[ẦÂ]U|≥ ?100K|breakout", open(chot,encoding='utf-8').read(), re.I)), "→ _nhap/CAU_*.md")
chk(1,  "kéo bản ghi quả to nhất",         bool(has("DOITHU_*.md")) or (chot and "cú bẻ lái" in open(chot,encoding='utf-8').read().lower()), "→ _nhap/DOITHU_*.md")
chk(2,  "cú bẻ lái KHÁC + khối mới",       bool(chot) and "bẻ lái" in open(chot,encoding='utf-8').read().lower(), "ghi trong CHOT")
# trích dẫn hợp lệ = DOI, PMC, hoặc tên tạp chí + số tập/số trang
CIT = r"10\.\d{4}/|doi\.org|PMC\d+|(?:PLoS|PLOS|Science|Nature|PNAS|Proc\.? R\.? Soc|Current Anthropology|Journal|Sci Adv|Med Hist)[^\n]{0,60}?\d+"
n_doi = len(set(re.findall(CIT, open(moneo,encoding='utf-8').read()))) if moneo else 0
chk(3,  f"mỏ neo có trích dẫn kiểm được ({n_doi})", n_doi >= 3, "≥3 trích dẫn trong MONEO")
chk(4,  "CỔNG A — quét tự trùng lặp",      bool(has("CONGA_*.md")) or (chot and "cổng a" in open(chot,encoding='utf-8').read().lower()), "→ _nhap/CONGA_*.md")
chk(5,  "viết ĐOẠN KẾT TRƯỚC",             bool(ket) and (mtime(ket) < mtime(narr) if narr else True), "KET_*.md phải CŨ HƠN narration")
chk(6,  "QA từng chương",                  bool(has("QA_*.md")) or bool(narr), "chạy qa_kichban.py")
chk(8,  "VẼ ĐƯỢC bằng người que?",       bool(has("VEDUOC_*.md")), "→ _nhap/VEDUOC_*.md · đếm món NHÌN THẤY vs cơ chế VÔ HÌNH")
chk(9,  "CHỦ NGHE bản tiếng Việt + chốt", bool(has("CHOTNGHE_*.md")), "→ _nhap/CHOTNGHE_*.md · nghe TTS vi-VN, không duyệt bằng mắt")
chk(10, "người nghe ngoài (chat lạnh)",    bool(has("KETQUA_CONG4.md")), "→ _nhap/KETQUA_CONG4.md")
chk("T","title đã đối chiếu bảng 159 video", bool(chot) and re.search(r"159|c[ôo]ng th[ứu]c title|PH[ẦA]N C", open(chot,encoding='utf-8').read(), re.I), "HE_THONG PHẦN C")
chk("S","chia shot + prompt",              bool(shots) and bool(prom), "chạy validate_shots.py")

# ── GIAI ĐOẠN 2 — SẢN XUẤT (chỉ chấm khi kịch bản đã xong) ────────────────
n_prompt = len(re.findall(r"^\d{3}\.", open(prom,encoding='utf-8').read(), re.M)) if prom else 0
# ⛔ VÁ 11/08: bỏ qua thư mục lưu/đã hỏng — cổng báo XANH NHẦM còn tệ hơn không có cổng
BO = ("_cu", "_hong", "_nhap", "kiem", "REF", "backup", "__pycache__")
def _sach(fs): return [f for f in fs if not any(b in f for b in BO)]
# 🔴 VÁ 11/08 — cổng này đã báo XANH GIẢ HAI LẦN vì quét đệ quy cả thư mục lưu lô
# hỏng (`anh_LOT1_hong/`, `anh_LOT2_all/`). Danh sách BỎ đuổi không kịp tên thư mục
# mới. Nay chỉ nhìn ĐÚNG MỘT chỗ ảnh thật được nạp vào video: `anh/`.
imgs = [f for f in glob.glob(os.path.join(V,"anh","*.png"))+
                   glob.glob(os.path.join(V,"anh","*.jpg"))
        if "thumb" not in os.path.basename(f).lower()]
mp3  = _sach(glob.glob(os.path.join(V,"**","*.mp3"),recursive=True))
mp4  = _sach(glob.glob(os.path.join(V,"**","*.mp4"),recursive=True))
thumb= glob.glob(os.path.join(V,"**","*humb*"),recursive=True)
meta = has("METADATA_*.md") or has("MOTA_*.md")

if n_prompt:
    chk("P1", f"ảnh == prompt ({len(imgs)}/{n_prompt})", len(imgs)==n_prompt,
        "gen 1 LƯỢT vào thư mục RỖNG · V14 lệch +52")
    chk("P2", f"tiếng ({len(mp3)} mp3)",  len(mp3) > 0, "nạp SHOTLINES_FULL.txt")
    chk("P3", f"ghép ({len(mp4)} mp4)",   len(mp4) > 0, "dùng APP, không viết script — V15 hỏng tiếng")
    chk("P4", "thumbnail (bước CUỐI)",    bool(thumb), "chữ phải nói điều TITLE KHÔNG nói")
    chk("P5", "metadata + REFERENCES",    bool(meta),  "dán MONEO xuống mô tả + disclaimer")
    chk("P6", "mid-roll đã đặt tay",      bool(has("DANG_*.md")), "→ DANG_*.md · phút 4 và 8")

print("═"*70); print(f"  PREFLIGHT — {name}"); print("═"*70)
for c, t, ok, g in rows:
    print(f"  {'✅' if ok else '⛔'} cổng {str(c):>2}  {t:<42} {'' if ok else g}")
print("─"*70)
print("  ✅ ĐỦ CỔNG — được đi tiếp." if not fail else
      f"  ⛔ CÒN {fail} CỔNG CHƯA CÓ DẤU VẾT. Chưa chạy thì nói CHƯA, đừng im.")
# ── nhắc soi kịch bản (thêm 20/08/2026) ───────────────────────────
if narr:
    print()
    # ── VIỆC TIẾP THEO: chỉ in 3 việc, không bắt ai nhớ gì ──
    chua = [(c, t, g) for c, t, ok, g in rows if not ok]
    print()
    print("  " + "━"*66)
    print("  ▶ LÀM TIẾP — ba việc gần nhất, không cần nhớ gì khác:")
    for i, (c, t, g) in enumerate(chua[:3], 1):
        print(f"     {i}. cổng {c} · {t}")
        print(f"        {g}")
    if len(chua) > 3:
        print(f"     … và {len(chua)-3} cổng nữa. Xem hết: kho/1_luat/CHECKLIST_KICHBAN.md")
    print("  " + "━"*66)
    print(f"  đọc kịch bản (KHÔNG chấm bằng máy):  python3 tools/soi_kich_ban.py {narr}")

sys.exit(1 if fail else 0)

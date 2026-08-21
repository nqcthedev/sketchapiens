#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ĐO 488 TIÊU ĐỀ ĐỐI THỦ — nửa 'trước cú bấm' mà kho chưa từng đo.

    python3 tools/do_tieu_de.py            # đo + ghi BANG_TIEU_DE.csv + in phép đối chứng

Bằng chứng của chính kho: 20 video CÙNG title -> quả thắng 59.630, còn lại <6.286,
tỉ lệ like gần như nhau => toàn bộ chênh lệch nằm TRƯỚC cú bấm. Bảng kịch bản chỉ
giải thích 1-12% chênh lệch view. Nên đây là nửa đáng đo hơn.

Luật đọc GIỐNG bảng kịch bản: KHÔNG xếp hạng view thô toàn kho (khác ngách thì khác
nền view). Chia TRONG TỪNG KÊNH ra 1/3 cao <-> 1/3 thấp, đếm bao nhiêu kênh cùng hướng.
13/15 ~ p 0,007  ·  10/15 ~ p 0,30 (nhiễu).
"""
import csv, glob, math, os, re, statistics as st
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "kho", "3_bangchung", "BANG_TIEU_DE.csv")

HOI    = r"^(why|how|what|when|where|who|did|do|does|could|can|would|will|is|are|was|were)\b"
BAN    = r"\b(you|your|yours|you're)\b"
CODAI  = r"\b(ancient|prehistoric|caveman|cavemen|stone age|ice age|early human)\b"
CUC    = (r"\b(most|best|worst|craziest|deadliest|weirdest|strangest|biggest|scariest|"
          r"darkest|creepiest|hardest|only|never|every|insane|brutal|bizarre)\b")
NGUY   = (r"\b(die|died|death|deadly|deadliest|kill|killed|survive|survival|survived|"
          r"danger|dangerous|predator|predators|afraid|fear|scary|creepy|horrible|"
          r"terrifying|nightmare|brutal|gross|disgusting|dark)\b")
SO     = r"\b\d+\b"


def keo():
    for f in sorted(glob.glob(os.path.join(ROOT, "2_KHO_BANGHI", "*", "*.txt"))):
        kenh = os.path.basename(os.path.dirname(f))
        tieude = view = None
        with open(f, encoding="utf-8") as fh:
            for raw in fh:
                s = raw.strip()
                if not s.startswith("#"):
                    if s: break
                    continue
                m = re.search(r"([\d,]+)\s*view", s)
                if m: view = int(m.group(1).replace(",", ""))
                elif not re.search(r"id=|https?://", s) and tieude is None:
                    tieude = s.lstrip("# ").strip()
        if tieude and view:
            yield kenh, tieude, view


def do(t):
    w = t.split()
    return {
        "ký tự": len(t), "từ": len(w),
        "là câu hỏi": int(t.rstrip().endswith("?")),
        "mở bằng từ hỏi": int(bool(re.match(HOI, t, re.I))),
        "có 'you'": int(bool(re.search(BAN, t, re.I))),
        "có 'ancient'": int(bool(re.search(CODAI, t, re.I))),
        "từ cực đại": len(re.findall(CUC, t, re.I)),
        "từ nguy hiểm": len(re.findall(NGUY, t, re.I)),
        "có số": int(bool(re.search(SO, t))),
        "CHỮ HOA CẢ TỪ": sum(1 for x in w if len(x) > 2 and x.isupper()),
        "dấu ...": int("..." in t), "dấu !": t.count("!"),
    }


rows = []
for kenh, t, v in keo():
    rows.append({"kênh": kenh, "view": v, "tiêu đề": t, **do(t)})

with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
    wr = csv.DictWriter(f, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
print(f"✅ {len(rows)} tiêu đề -> {os.path.relpath(OUT, ROOT)}\n")

COT = [c for c in rows[0] if c not in ("kênh", "view", "tiêu đề")]
kenh = defaultdict(list)
for r in rows: kenh[r["kênh"]].append(r)
dung = {k: sorted(v, key=lambda r: r["view"]) for k, v in kenh.items() if len(v) >= 9}

print(f"{'='*88}\nTIÊU ĐỀ — ⅓ VIEW CAO vs ⅓ THẤP, TRONG TỪNG KÊNH ({len(dung)} kênh)\n{'='*88}")
print(f"{'chỉ số':<20}{'thấp':>9}{'cao':>9}{'chênh':>10}{'kênh cùng hướng':>19}   r trung vị")
print("-"*88)
for c in COT:
    lo_a, hi_a, ph, rs = [], [], 0, []
    for k, v in dung.items():
        n = len(v)//3
        lo = [r[c] for r in v[:n]]; hi = [r[c] for r in v[-n:]]
        lo_a.append(st.median(lo)); hi_a.append(st.median(hi))
        if st.median(hi) > st.median(lo): ph += 1
        xs = [r[c] for r in v]; ys = [math.log10(max(r["view"], 1)) for r in v]
        mx, my = st.mean(xs), st.mean(ys)
        den = math.sqrt(sum((a-mx)**2 for a in xs) * sum((b-my)**2 for b in ys))
        if den: rs.append(sum((a-mx)*(b-my) for a, b in zip(xs, ys))/den)
    L, H, n = st.median(lo_a), st.median(hi_a), len(lo_a)
    d = f"{(H-L)/L*100:+.0f}%" if L else ("mới có" if H else "—")
    sao = "  ⬅" if (ph >= n-2 or ph <= 2) else ""
    print(f"{c:<20}{L:>9.2f}{H:>9.2f}{d:>10}{ph:>10}/{n:<8}{st.median(rs):>+11.2f}{sao}")

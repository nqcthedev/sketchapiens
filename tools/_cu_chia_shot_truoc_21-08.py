#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TÁCH KỊCH BẢN THÀNH DÒNG-SHOT — chỉ chèn ranh giới, KHÔNG đổi một chữ nào.

    python3 tools/chia_shot.py videos/Video20_Cold/Script_V20_narration.txt

Luật (skill chia-shot, bản 30/07): ~6-9 từ mỗi shot · tách ở dấu câu ·
câu ngắn punchy giữ nguyên một shot · ghép lại phải ra ĐÚNG kịch bản gốc.

Cổng cuối tự chạy: nối mọi dòng-shot lại rồi so với file gốc. Lệch một ký tự là DỪNG.
"""
import io, re, sys

MIN, MAX = 5, 10          # từ mỗi shot
NGAT = re.compile(r"(,|;|:)\s")

def tach_cau(cau):
    """Bổ một câu thành các dòng-shot ở dấu phẩy/chấm phẩy/hai chấm."""
    if len(cau.split()) <= MAX:
        return [cau]
    manh, cur = [], ""
    for phan in NGAT.split(cau):
        if phan in (",", ";", ":"):
            cur += phan
            continue
        if cur:
            manh.append(cur.strip()); cur = ""
        cur = phan
    if cur: manh.append(cur.strip())

    # gộp mảnh quá ngắn vào mảnh trước
    ra = []
    for x in manh:
        if ra and len(x.split()) < MIN:
            ra[-1] = ra[-1] + " " + x
        else:
            ra.append(x)

    # mảnh còn quá dài -> bổ tiếp ở "and/but/because/which/so/then/that"
    cuoi = []
    for x in ra:
        if len(x.split()) <= MAX:
            cuoi.append(x); continue
        w = x.split(); tam = []; batdau = 0
        for i in range(1, len(w)):
            if (w[i].lower() in ("and","but","because","which","so","then","that","when","where","while","until","before","after")
                    and i - batdau >= MIN and len(w) - i >= MIN):
                tam.append(" ".join(w[batdau:i])); batdau = i
        tam.append(" ".join(w[batdau:]))
        # còn dài nữa thì cắt cứng theo MAX
        for t in tam:
            ww = t.split()
            while len(ww) > MAX + 3:
                cuoi.append(" ".join(ww[:MAX])); ww = ww[MAX:]
            cuoi.append(" ".join(ww))
        continue
    return [c for c in cuoi if c.strip()]

src = sys.argv[1]
CAU = [l.strip() for l in io.open(src, encoding="utf-8") if l.strip()]
SHOT = [s for c in CAU for s in tach_cau(c)]

# ── CỔNG: ghép lại phải ra đúng gốc
g = re.sub(r"\s+", " ", " ".join(CAU)).strip()
h = re.sub(r"\s+", " ", " ".join(SHOT)).strip()
if g != h:
    for i,(a,b) in enumerate(zip(g,h)):
        if a!=b:
            sys.exit(f"⛔ LỆCH ở ký tự {i}\n gốc: ...{g[max(0,i-60):i+60]}...\n ghép: ...{h[max(0,i-60):i+60]}...")
    sys.exit(f"⛔ LỆCH ĐỘ DÀI: gốc {len(g)} ghép {len(h)}")

out = src.rsplit("/",1)[0] + "/_shot_lines_moi.txt"
io.open(out,"w",encoding="utf-8").write("\n".join(SHOT)+"\n")
tu = sum(len(x.split()) for x in SHOT)
import statistics as st
d = [len(x.split()) for x in SHOT]
print(f"✅ CỔNG SẠCH — ghép lại khớp từng ký tự với kịch bản gốc")
print(f"   {len(CAU)} câu -> {len(SHOT)} shot   ({tu} từ)")
print(f"   từ mỗi shot: trung vị {st.median(d):.0f} · trung bình {tu/len(SHOT):.1f} · dài nhất {max(d)}")
print(f"   shot >10 từ: {sum(1 for x in d if x>10)}   ·  shot <4 từ: {sum(1 for x in d if x<4)}")
print(f"   -> {out}")

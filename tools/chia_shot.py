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

# Từ được phép ĐỨNG ĐẦU một shot mới. Cắt trước những từ này thì hai nửa đều còn nghĩa.
# ⛔ Đừng thêm giới từ dính chặt vào động từ đứng trước (of, to, for) — cắt ở đó là hỏng.
MOC = {"and","but","or","so","then","yet","because","which","who","whose","that",
       "when","where","while","until","before","after","since","though","although",
       "unless","if","with","without","from"}

# ⛔ KHÔNG cắt nếu từ ngay TRƯỚC mốc nằm trong bộ này — mốc lúc đó đang nằm GIỮA một cụm
#    cố định, cắt vào là hỏng cả hai nửa. Đúc 21/08/2026 từ 5 lỗi thật ở V20:
#      "three hundred | and seventy"   ← số bị chẻ đôi
#      "in nothing | but shorts"       ← cụm nothing-but
#      "they do | not know"            ← trợ động từ tách khỏi động từ
#      "to get | through before"       ← động từ tách khỏi giới từ dính
CAM_TRUOC = {"do","does","did","is","are","was","were","am","be","been","being",
             "has","have","had","can","could","will","would","shall","should",
             "may","might","must","get","got","go","went","come","came","look",
             "nothing","anything","everything","something","nobody","anybody",
             "one","two","three","four","five","six","seven","eight","nine","ten",
             "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety",
             "hundred","thousand"}

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
            if (w[i].lower().strip(",;:") in MOC
                    and w[i-1].lower().strip(",;:") not in CAM_TRUOC
                    and i - batdau >= MIN and len(w) - i >= MIN):
                tam.append(" ".join(w[batdau:i])); batdau = i
        tam.append(" ".join(w[batdau:]))
        # ⛔ KHÔNG cắt cứng theo số từ nữa (sửa 21/08/2026).
        #    Cắt cứng sinh ra 48/338 shot vô nghĩa ở V20: "down and drift off." ·
        #    "Legal Medicine went back through..." · "pattern, on the floor,".
        #    Với TTS thì vô hại vì ghép lại vẫn đúng, nhưng MỖI SHOT LÀ MỘT KHUNG ẢNH,
        #    và một khung không có nghĩa độc lập thì không vẽ được.
        #    Nay: không tìm được mốc an toàn thì GIỮ NGUYÊN cả mệnh đề, dù dài.
        cuoi.extend(t for t in tam if t.strip())
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

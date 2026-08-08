#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SINH PROMPTS_FULL.txt + SHOTLINES_FULL.txt — MỘT bản cho MỌI video.

    python3 tools/build_prompts.py videos/Video19_NightWalk
    python3 tools/build_prompts.py .          # từ trong thư mục video

Bản sắc hình ảnh (STYLE · khối nhân vật · bảng nền · biểu cảm · NEG) nằm ở
`identity/style.py` — MỘT nguồn cho cả kênh.
Dữ liệu riêng của video nằm ở `<thư_mục_video>/shot_data.py`.

Trước 08/08/2026 file này bị chép vào TỪNG thư mục video và đã trôi thành ba bản
khác nhau (219 / 256 / 262 dòng). Xem đầu `identity/style.py` để biết cái giá.
"""
import io, os, sys, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
sys.path.insert(0, os.path.join(ROOT, "identity"))
from style import *          # noqa: F403,F401 — bản sắc kênh

def _nap(p, ten):
    spec = importlib.util.spec_from_file_location(ten, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

_sd = os.path.join(VIDEO, "shot_data.py")
if not os.path.exists(_sd):
    sys.exit(f"⛔ không thấy {_sd}")
SHOTS = _nap(_sd, "shot_data").SHOTS


def build(i, line, kind, subj, text, bg, face="flat"):
    n = f"{i:03d}"
    p = []
    if kind in WHO:
        p.append(WHO[kind])
        p.append("ACTION IN THIS SHOT: " + subj + ". ")
        p.append(FACE.get(face, FACE["flat"]))
        p.append(STYLE_SCENE)
        p.append(framing(kind, subj))
        p.append("SCENE: ONE single moment, " + BG[bg] + ". ")
        if "no text" in text.lower():
            p.append("TEXT: no text or letters anywhere. ")
        else:
            p.append(f"TEXT: {text}. " + LETTER)
        p.append(NEG_SCENE)
    else:
        p.append(STYLE_CARD)
        p.append("SUBJECT: " + subj + ". ")
        p.append(framing(kind, subj))
        p.append("SCENE: " + BG.get(bg, BG["white"]) + ". " + SAME_HAND)
        if "no text" in text.lower():
            p.append("TEXT: no text or letters. ")
        else:
            p.append(f"TEXT: {text}. " + LETTER)
        p.append(NEG_CARD)
    return n, "".join(p)


lines, prompts = [], []
for i, s in enumerate(SHOTS, 1):
    line, kind, subj, text, bg = s[:5]
    face = s[5] if len(s) > 5 else "flat"
    n, pr = build(i, line, kind, subj, text, bg, face)
    lines.append(line)
    prompts.append(f"{n}. {pr}")

io.open(os.path.join(VIDEO,"SHOTLINES_FULL.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

HEADER = """### TRUOC KHI GEN
1. Chon 16:9 truoc khi chay.
2. Gen vao MOT THU MUC RONG, mot luot (bo dem cua tool dat ten theo thu tu chay).
   Neu tool khong nuot het -> chia dai, MOI DAI MOT THU MUC RIENG, dem tung dai.
3. Dem du dung {N} file roi moi ghep.
4. (KHONG xoa watermark - de nguyen)
   -> cat watermark ngoi sao cua Flow o goc duoi-phai + dua ve 1920x1080.

"""
io.open(os.path.join(VIDEO,"PROMPTS_FULL.txt"), "w", encoding="utf-8").write(
    HEADER.format(N=len(SHOTS)) + "\n\n".join(prompts) + "\n")

tot = len(SHOTS)
scene = sum(1 for s in SHOTS if s[1] in WHO)
card = tot - scene
withtext = sum(1 for s in SHOTS if "no text" not in s[3].lower())
modern = sum(1 for s in SHOTS if s[1] == "SCENE_M")
words = sum(len(s[0].split()) for s in SHOTS)
print(f"  tổng shot        : {tot}")
print(f"  từ TB/shot       : {words/tot:.1f}")
print(f"  KHUNG CẢNH       : {scene} = {100*scene/tot:.0f}%   (đối thủ 59-64%)")
print(f"  THẺ nền trắng    : {card} = {100*card/tot:.0f}%   (đối thủ 36-41%)")
print(f"  khung có chữ     : {withtext} = {100*withtext/tot:.0f}%")
print(f"  người hiện đại   : {modern} = {100*modern/tot:.0f}%   (luật ≤15%)")
print(f"  ước thời lượng   : {tot*2.0/60:.1f} phút @2,0s/ảnh")

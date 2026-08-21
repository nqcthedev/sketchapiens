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
_mod = _nap(_sd, "shot_data")
SHOTS = _mod.SHOTS

# 🔴 21/08/2026 — NỀN RIÊNG CỦA MỘT VIDEO
# Trước đây mọi nền phải khai trong `identity/style.py`, file có biển "sửa là đổi bản
# sắc cả kênh". V20 cần 6 nền chưa từng có (than tàn · hố khai quật · phòng thí nghiệm ·
# bình minh · mặt đất đóng băng · nằm cạnh lửa), và cách duy nhất là sửa file bản sắc —
# đúng thứ bị cấm. Nay video khai `BG_THEM = {...}` trong shot_data.py của chính nó.
# ⚠️ Khi 2-3 video cùng dùng một nền, hãy NÂNG nó lên identity/style.py rồi bỏ khỏi đây.
BG.update(getattr(_mod, "BG_THEM", {}))
WHO.update(getattr(_mod, "WHO_THEM", {}))

# 🔴 21/08/2026 — KIND KHÔNG CÓ MẶT TRONG KHUNG
# V20 có 11 shot cận cảnh BÀN TAY / cẳng tay / vai, gồm cả khung CUỐI CÙNG của video.
# Engine dán khối nhân vật đầy đủ ("đầu tròn trắng, hai mắt, tóc nâu, áo da rách") cộng
# khối FACE vào cả những khung đó, nên model sẽ vẽ nguyên một người vào khung đáng lẽ
# chỉ có một bàn tay. SCENE_N không cứu được: NO_PERSON cấm luôn "no hands".
# Video khai kind riêng trong WHO_THEM, và liệt kê ở KHONG_MAT để engine bỏ khối FACE.
KHONG_MAT = set(getattr(_mod, "KHONG_MAT", ()))


def build(i, line, kind, subj, text, bg, face="flat"):
    n = f"{i:03d}"
    # 🔴 11/08/2026 — STYLE LOCK đứng ĐẦU mọi prompt. Trước đây nét vẽ được neo bằng
    # ẢNH THAM CHIẾU trong Google Flow; chủ đã bỏ phần đó, nên chữ phải gánh.
    p = [STYLE_LOCK]
    if kind in WHO:
        # 🔴 VÁ 11/08/2026 — SCENE_N vốn luôn dán khối ANIMAL ("con vật là điểm nhấn màu
        # của khung"). 34/46 khung SCENE_N của V19 KHÔNG gọi tên con vật nào, nên model
        # tự đẻ ra cáo, gấu, voi, chó xanh — kể cả khi shot ghi "no animal anywhere".
        # Nay chỉ dán khối ANIMAL khi subject THẬT SỰ nhắc một con vật.
        import re as _re
        _CV = r"(?:lion|snake|wolf|hyena|leopard|bear|animal|prey|cat|dog|bird|elephant|mammoth|deer|horse|zebra)s?"
        # bỏ mọi lần nhắc PHỦ ĐỊNH ("no animal", "never a fox") trước khi dò
        _sach = _re.sub(r"\b(no|never|without)\s+" + _CV, "", subj, flags=_re.I)
        _thuan = (kind == "SCENE_N"
                  and not _re.search(r"\b" + _CV + r"\b", _sach, _re.I))
        if _thuan:
            # 🔴 VÁ LẠI 11/08 chiều — bản sáng nay để `pass` ở đây, tức prompt KHÔNG còn
            # một dòng luật nào về người, và model lấp chỗ trống bằng thứ nó quen tay
            # nhất: anh hiện đại đầu trọc mặc áo len. 28/46 khung SCENE_N hỏng đúng vì
            # thế, gồm CẢ HAI KHUNG CUỐI VIDEO.
            # Khoảng trống trong prompt không bao giờ là khoảng trống trên hình.
            p.append(NO_PERSON)
        else:
            p.append(WHO[kind])
        p.append("ACTION IN THIS SHOT: " + subj + ". ")
        # khung cảnh thuần thì KHÔNG dán khối FACE — dán vào là tự tay mời model vẽ mặt
        # ... và khung cận một phần cơ thể cũng vậy: không có mặt thì đừng tả mặt
        if not _thuan and kind not in KHONG_MAT:
            p.append(FACE.get(face, FACE["flat"]))
        p.append(STYLE_SCENE)
        p.append(framing(kind, subj, thuan=_thuan))
        p.append("SCENE: ONE single moment, " + BG[bg] + ". ")
        if "no text" in text.lower():
            p.append("TEXT: no text or letters anywhere. ")
        else:
            p.append(f"TEXT: {text}. " + LETTER)
        p.append(NEG_SCENE)
    else:
        p.append(STYLE_CARD)
        p.append(PERSON_IN_CARD)
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

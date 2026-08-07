# -*- coding: utf-8 -*-
"""V17 — sinh PROMPTS_FULL.txt + SHOTLINES_FULL.txt từ shot_data.py

BUILD LẠI 30/07/2026 theo kho/3_bangchung/NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md
(đo 1.090 khung = trọn hai video đối thủ, không lấy mẫu).

Hai chế độ hình, KHÁC HẲN NHAU:
  · CẢNH  — nền vẽ có chiều sâu: vân đá, chuyển màu trời, quầng lửa, bóng đổ
  · THẺ   — nền trắng phẳng, chữ viết tay, hình nhỏ vẽ tay bên cạnh
Mục tiêu tỉ lệ: 60% cảnh / 40% thẻ (đối thủ 59-64% cảnh).
"""
import io
from shot_data import SHOTS

# ── STYLE ─────────────────────────────────────────────────────────────────
# Cảnh: KHÔNG phẳng. Đối thủ vẽ môi trường có lớp, có sáng tối, có không khí.
# Rút gọn 31/07: Flow chặn prompt >4000 ký tự. Giữ đủ luật, bỏ chữ thừa.
STYLE_SCENE = (
    "A modern 2D digital cartoon frame from a hand-illustrated YouTube explainer: every shape has "
    "a crisp medium-bold BLACK INK OUTLINE, filled with CLEAN FULLY SATURATED colour - strong blue "
    "sky and rain, vivid green plants, red-brown earth, warm brown rock, bright orange fire. "
    "Shading is ONE flat darker patch of the same colour, never hatching, never a wash. The WORLD "
    "has real depth: layered rock, ground at several distances, grass tufts, scattered stones, and "
    "a warm orange glow from any fire onto the figures. People are stick figures with LARGE round "
    "heads filled SOLID BRIGHT WHITE, high contrast against the colour behind. 16:9. ")

# Thẻ: phẳng, trắng, chữ tay. Đây là chỗ DUY NHẤT được phẳng.
STYLE_CARD = (
    "A hand-drawn explainer CARD on a plain WHITE background, drawn with the same confident "
    "medium-bold black ink outline as the rest of the series. Simple flat hand-drawn shapes, "
    "hand-lettered marker text, generous clean white space, nothing photographic. 16:9. ")

# ── NHÂN VẬT (lặp Y NGUYÊN mọi lần xuất hiện) ─────────────────────────────
ANCIENT = (
    "EXACTLY ONE PERSON: one head, one body, two arms, two legs. Never two heads, never a second "
    "figure. CHARACTER LOCK - fixed in every image, only pose and expression change: "
    "(1) head = one LARGE PERFECT CIRCLE filled SOLID WHITE, no chin, no jaw, never an oval; "
    "(2) NO neck, head sits straight on the shoulders; "
    "(3) head a normal size for a stick figure, NOT oversized; "
    "(4) hair = a DARK BROWN scribbled mop of spiky clumps with jagged ends, sitting on TOP of the "
    "head as ONE mass, never two side tufts, never a smooth bob; "
    "(5) face = two small black dot eyes, two thin eyebrows, one small mouth. No nose, no ears; "
    "(6) ONE garment only: a dark-brown hide smock, shoulders to mid-thigh, hem TORN into jagged "
    "points, a thin cord across the chest; "
    "(7) arms and legs = THIN single black lines, no joints; "
    "(8) small mitten hands, small bare oval feet, always barefoot; "
    "(9) never add a beard, necklace, headband, boots or shirt. "
    "This is the recurring caveman of the series. ")

MODERN = (
    "EXACTLY ONE PERSON: one head, one body, two arms, two legs. Never two heads, never a second "
    "figure. CHARACTER LOCK - fixed in every image, only pose and expression change: one LARGE "
    "PERFECT CIRCLE head filled SOLID WHITE, completely BALD with NO hair; NO neck; face = two "
    "small black dot eyes, thin eyebrows, one small mouth; a BARE thin black stick-line body with "
    "NO clothes unless this shot names one; thin single-line arms and legs, no joints; small "
    "mitten hands, small oval feet. This is the recurring modern guy of the series. ")

WOMAN = (
    "EXACTLY ONE PERSON: one head, one body, never two heads. CHARACTER LOCK - a caveman woman "
    "built to the same fixed rules: one LARGE PERFECT CIRCLE head filled SOLID WHITE, no chin, "
    "never an oval; NO neck; head a normal size, NOT oversized; DARK BROWN scribbled hair pulled "
    "back as ONE mass with loose strands, never two side tufts; face = two small black dot eyes, "
    "two thin eyebrows, one small mouth, no nose, no ears; ONE garment only, a ragged brown fibre "
    "wrap with a torn hem; arms and legs THIN single black lines, no joints; small mitten hands, "
    "small bare oval feet; nothing else ever added. Only pose and expression change. ")

GROUP = (
    "EXACTLY ONE HEAD PER PERSON. Every figure has one head, one body, two arms, two legs. No two "
    "heads on one body, no conjoined figures. CHARACTER LOCK - EVERY caveman built to the same "
    "fixed rules: one LARGE PERFECT CIRCLE head filled SOLID WHITE, no chin, never an oval; NO "
    "neck; heads a normal size, NOT oversized; a DARK BROWN scribbled mop of spiky clumps on TOP "
    "of the head as ONE mass, never two side tufts; face = two small black dot eyes, two thin "
    "eyebrows, one small mouth, no nose, no ears; ONE garment only, a dark-brown hide smock with a "
    "hem TORN into jagged points; arms and legs THIN single black lines, no joints; small mitten "
    "hands, small bare oval feet, barefoot; never add beards, necklaces, headbands or boots. They "
    "differ ONLY in height, pose and expression, so the group reads as real people, not copies. ")

# ── NEG ───────────────────────────────────────────────────────────────────
# Đã BỎ 'no country borders' và 'no inset panel': đo được là đối thủ CÓ dùng.
NEG_SCENE = ("NEG: NO TWO HEADS ON ONE BODY, no conjoined figures, no duplicate character, no "
             "mirrored copy, no split-screen, no collage, no photorealism, no 3D, no anime, no "
             "Disney or Pixar style, no glossy render, no stock clipart, no solid black pictogram "
             "people, no sepia, no brown monochrome, no desaturated or faded colours, no pencil "
             "sketch, no charcoal, no cross-hatching, no watercolour, no aged paper, no vintage "
             "engraving, no extra limbs or fingers, no blood, no gore, no watermark, no logo, no "
             "frame border, no subtitle bar, 16:9. ")

NEG_CARD = ("NEG: no photograph, no photorealism, no 3D render, no stock clipart, no icon-pack art, "
            "no corporate infographic style, no glossy icons, no solid black pictogram people, "
            "no gradient background, no computer font for the headline, no watermark, no logo, "
            "no subtitle bar, 16:9. ")

# ── NỀN CẢNH — có lớp, có ánh sáng, không phải hai dải màu ────────────────
BG = {
 "rain_out":  ("open ground under a deep blue-grey rain sky, thin slanted BLUE rain lines across the "
               "whole frame, wet red-brown earth with several BLUE puddles, olive-green grass tufts "
               "and grey-brown stones, and green hills behind"),
 "rain_night":("open ground at night in the rain, a deep NAVY BLUE sky, thin pale blue rain lines, "
               "wet dark-brown ground with blue puddles, dark grey rock shapes"),
 "forest":    ("dense rainforest in strong greens, layered bright-green leaf and fern shapes at "
               "several depths, wet red-brown ground with blue puddles and fallen leaves, thin blue "
               "rain lines, dark-brown tree trunks"),
 "cave":      ("inside a cave, warm mid-brown rock walls with clear layering and simple darker-brown "
               "shading, and a bright cave mouth at one side framing blue rain and green ground "
               "outside"),
 "cave_fire": ("inside a cave, warm mid-brown rock walls with clear layering, a BRIGHT ORANGE fire of "
               "stacked wood on a ring of grey stones throwing a strong warm orange glow onto the "
               "figures and the near rock, grey smoke rising, and a bright cave mouth at one side "
               "showing blue rain outside"),
 "cave_mouth":("the mouth of a cave seen from inside, dark warm-brown rock framing the opening, and "
               "through the opening a wall of BLUE rain over green and brown ground, the outside "
               "much brighter than the rock inside"),
 "modern":    ("a simple modern room in warm cream and wood-brown, a window at one side with BLUE "
               "rain running down the glass, warm yellow light from a lamp falling across the floor"),
 "street":    ("a wet city street, grey-blue road with a kerb, a red-brown brick building face with "
               "windows and a door, a lamp post with warm yellow light, BLUE puddles, blue rain"),
 "dry_plain": ("open savanna under a strong BLUE sky with white clouds, warm tan earth, bright "
               "yellow-green grass tufts, grey stones, and two green flat-topped trees far off"),
 "riverbank": ("a swollen BLUE-BROWN river cutting through green and brown ground, the water surface "
               "broken and moving, muddy banks, blue rain lines, dark-green vegetation opposite"),
 "white":     "a plain WHITE background with generous clean empty space",
}

# ── KHUNG HÌNH ────────────────────────────────────────────────────────────
def framing(kind, subj):
    s = subj.lower()
    if kind.startswith("SCENE") or kind == "GROUP":
        if any(k in s for k in ("wide","camp","seen small","at a distance","whole band","landscape")):
            return ("Framing: a WIDE establishing shot, the figures fairly small inside a large "
                    "environment, plenty of world visible around them. ")
        if any(k in s for k in ("close","his own hand","holding one hand","face fills")):
            return "Framing: a tight CLOSE-UP, the subject filling most of the frame. "
        if any(k in s for k in ("sitting","kneeling","lying","crouch","seated")):
            return ("Framing: a MEDIUM shot from slightly above, the figure large in frame with the "
                    "ground and surroundings clearly visible. ")
        return ("Framing: a MEDIUM shot, the figure large and roughly centred, with the environment "
                "readable behind and around him. ")
    if "map" in s:
        return "Framing: the map centred and LARGE, filling most of the frame. "
    if any(k in s for k in ("cross-section","timeline","chart","diagram")):
        return "Framing: the diagram centred and LARGE, drawn nearly edge to edge. "
    if "row of" in s or "in a row" in s:
        return "Framing: the items in ONE clean horizontal row across the middle, evenly spaced. "
    if "title card" in s or "text filling" in s or "headline" in s:
        return "Framing: the lettering fills most of the frame. "
    return "Framing: one subject centred and drawn LARGE, generous empty white space around it. "

LETTER = ("All lettering is IRREGULAR HAND-LETTERED marker writing, each letter drawn by hand and "
          "slightly uneven, NOT a computer font. Spell it EXACTLY as written above, no extra words, "
          "no gibberish letters. ")

SAME_HAND = ("Every object, icon and diagram shape is drawn BY HAND in the same style and the same "
             "black ink outline as the characters in this series. Any person shown is the same "
             "stickman with a LARGE round white head and thin stick limbs, NEVER a solid black "
             "pictogram figure. ")

WHO = {"SCENE_A": ANCIENT, "SCENE_M": MODERN, "SCENE_W": WOMAN, "GROUP": GROUP}


def build(i, line, kind, subj, text, bg):
    n = f"{i:03d}"
    p = []
    if kind in WHO:
        p.append(WHO[kind])
        p.append("ACTION IN THIS SHOT: " + subj + ". ")
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
for i, (line, kind, subj, text, bg) in enumerate(SHOTS, 1):
    n, pr = build(i, line, kind, subj, text, bg)
    lines.append(line)
    prompts.append(f"{n}. {pr}")

io.open("SHOTLINES_FULL.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")

HEADER = """### TRUOC KHI GEN
1. Chon 16:9 truoc khi chay.
2. Gen vao MOT THU MUC RONG, mot luot (bo dem cua tool dat ten theo thu tu chay).
   Neu tool khong nuot het -> chia dai, MOI DAI MOT THU MUC RIENG, dem tung dai.
3. Dem du dung {N} file roi moi ghep.
4. Chay:  python3 clean_images.py <thu_muc_anh> <thu_muc_ra>
   -> cat watermark ngoi sao cua Flow o goc duoi-phai + dua ve 1920x1080.

"""
io.open("PROMPTS_FULL.txt", "w", encoding="utf-8").write(
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

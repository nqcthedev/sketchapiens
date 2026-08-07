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
    "A hand-drawn 2D explainer frame that looks drawn with a digital felt-tip marker: every outline "
    "is solid BLACK with slightly WOBBLY, uneven thickness, never the smooth uniform look of vector "
    "art. The environment is built from FLAT BLOCKS OF COLOUR with extremely low detail: only what "
    "the scene line below names and nothing more, nothing layered, no "
    "depth, no texture. Stars are plain white dots. Fire is a wobbly orange shape with a yellow "
    "centre. A tree is one brown line for a trunk with a green cloud on top. Flat solid fills, no "
    "gradients, no shadows. 16:9. ")

# Thẻ: phẳng, trắng, chữ tay. Đây là chỗ DUY NHẤT được phẳng.
STYLE_CARD = (
    "A hand-drawn explainer CARD on a plain WHITE background, drawn with the same confident "
    "medium-bold black ink outline as the rest of the series. Simple flat hand-drawn shapes, "
    "hand-lettered marker text, generous empty white space, nothing photographic. 16:9. ")

# ── NHÂN VẬT (lặp Y NGUYÊN mọi lần xuất hiện) ─────────────────────────────
ANCIENT = (
    "EXACTLY ONE PERSON: one head, one body, two arms, two legs. Never two heads, never a second "
    "figure. CHARACTER LOCK - fixed in every image, only pose and expression change: "
    "(1) head = one LARGE round circle filled SOLID WHITE with a THICK black outline, no chin, "
    "no jaw; "
    "(2) NO neck, the head sits straight on the shoulders; "
    "(3) hair = MEDIUM BROWN, drawn as a SHAGGY MANE of many fine wavy strands that FRAMES the "
    "white face like a hood: it covers the top of the head and hangs down BOTH SIDES past the jaw, "
    "with ragged pointed ends and a few loose strands sticking out. The white circle of the face "
    "stays fully visible in the middle. Never black, never a spiky ball on top of the head, never "
    "fine needles radiating outwards, never a smooth bob; "
    "(4) eyes = TWO LARGE ROUND WHITE EYES, each ringed with a thin black outline and holding a "
    "big black pupil. They are the biggest feature on the face. Never tiny dots; "
    "(5) eyebrows = two thin curved black lines above the eyes, their angle carrying the emotion; "
    "(6) mouth = one simple black shape, straight when calm, wavy when worried, open when shocked. "
    "No nose, no ears; "
    "(7) ONE garment only: a ragged brown animal-hide tunic over the torso with a torn jagged hem, "
    "a strap over one shoulder; "
    "(8) arms and legs = THIN single black lines, slightly crooked, no joints; "
    "(9) small white mitten hands and small white oval feet, filled the SAME SOLID WHITE as the "
    "head, never skin-coloured, never peach or tan, always barefoot; "
    "(10) never add a beard, necklace, headband, boots or shirt. "
    "Every line is drawn by hand with a slightly wobbly, uneven stroke, never a computer-perfect "
    "shape. "
    "This is the recurring caveman of the series. ")

MODERN = (
    "EXACTLY ONE PERSON: one head, one body, two arms, two legs. Never two heads, never a second "
    "figure. CHARACTER LOCK - fixed in every image, only pose and expression change: one LARGE round "
    "hand-drawn circle for a head, filled SOLID WHITE with a slightly wobbly uneven outline, "
    "completely BALD with NO hair; NO neck; face = two "
    "small black dot eyes, thin eyebrows, one small mouth; a BARE thin black stick-line body with "
    "NO clothes unless this shot names one; thin single-line arms and legs, no joints; small "
    "mitten hands, small oval feet. This is the recurring modern guy of the series. ")

WOMAN = (
    "EXACTLY ONE PERSON: one head, one body, two arms, two legs. Never two heads, never a second "
    "figure. CHARACTER LOCK - a caveman woman built to the same fixed rules as the recurring "
    "caveman: one LARGE round hand-drawn circle for a head, filled SOLID WHITE with a thick "
    "slightly wobbly black outline, no chin, no jaw; NO neck; hair = MEDIUM BROWN, a shaggy mane "
    "of many fine wavy strands framing the white face and falling PAST THE SHOULDERS, with ragged "
    "pointed ends, never black, never a smooth bob; eyes = TWO LARGE ROUND WHITE EYES each ringed "
    "in thin black with a big black pupil, never tiny dots; two thin curved eyebrows; one simple "
    "mouth; no nose, no ears; ONE garment only, a ragged brown hide wrap with a torn jagged hem; "
    "arms and legs = THIN single black lines, no joints; small white mitten hands and small white "
    "oval feet, filled the SAME SOLID WHITE as the head, never skin-coloured; always barefoot. "
    "This is the recurring caveman woman of the series. ")

GROUP = (
    "EXACTLY ONE HEAD PER PERSON. Every figure has one head, one body, two arms, two legs. No two "
    "heads on one body, no conjoined figures. CHARACTER LOCK - EVERY caveman built to the same "
    "fixed rules: one LARGE round circle for a head, filled SOLID WHITE with a THICK slightly "
    "wobbly black outline, no chin, no jaw; NO neck; hair = MEDIUM BROWN, a SHAGGY MANE of many "
    "fine wavy strands framing the white face like a hood, covering the top of the head and hanging "
    "down BOTH SIDES past the jaw with ragged pointed ends, never black, never a spiky ball on top, "
    "never a smooth bob; eyes = TWO LARGE ROUND WHITE EYES each ringed in thin black with a big "
    "black pupil, never tiny dots; two thin curved eyebrows carrying the emotion; one simple mouth; "
    "no nose, no ears; ONE garment only, a ragged brown hide tunic with a torn jagged hem; arms and "
    "legs THIN single black lines, slightly crooked, no joints; small white mitten hands and small "
    "white oval feet filled the SAME SOLID WHITE as the head, never skin-coloured, barefoot; never "
    "add beards, necklaces, headbands or boots. Give EVERY face in the group a DIFFERENT expression "
    "so the group reads as real people, not copies. Tell them apart by height, hair length and hair "
    "colour: grey strands for the old ones, longer strands for the women, smaller bodies for the "
    "children. ")

# ── NEG ───────────────────────────────────────────────────────────────────
# Đã BỎ 'no country borders' và 'no inset panel': đo được là đối thủ CÓ dùng.
NEG_SCENE = ("NEG: NO TWO HEADS ON ONE BODY, no conjoined figures, no duplicate character, no "
             "mirrored copy, no split-screen, no collage, no photorealism, no 3D, no anime, no "
             "Disney or Pixar style, no glossy render, no stock clipart, no solid black pictogram "
             "people, no sepia, no brown monochrome, no pencil "
             "sketch, no charcoal, no cross-hatching, no watercolour, no aged paper, no vintage "
             "engraving, no skin-coloured hands or feet, no peach or tan skin anywhere, no black hair, no hedgehog hair, no spiky hair ball on top of the head, no fine radiating hair needles, no extra limbs or fingers, no blood, no gore, no watermark, no logo, no "
             "frame border, no subtitle bar, 16:9. ")

NEG_CARD = ("NEG: no photograph, no photorealism, no 3D render, no stock clipart, no icon-pack art, "
            "no corporate infographic style, no glossy icons, no solid black pictogram people, "
            "no gradient background, no computer font for the headline, no watermark, no logo, "
            "no subtitle bar, 16:9. ")

# ── NỀN CẢNH — có lớp, có ánh sáng, không phải hai dải màu ────────────────
BG = {
 "night_open": ("a block of midnight-blue night sky with plain white dots for stars and a small white "
               "crescent moon, over one flat strip of medium-brown ground, and one or two trees each "
               "drawn as a brown line with a dark green cloud on top"),
 "night_fire": ("a block of midnight-blue night sky with white dots for stars, one flat strip of "
               "medium-brown ground, and a small fire drawn as a wobbly orange shape with a yellow "
               "centre sitting on a few grey stones, throwing a soft orange patch on the ground"),
 "cave_fire":  ("a flat block of medium-brown rock filling the frame behind the figures, one flat strip "
               "of darker brown ground, and a small fire drawn as a wobbly orange shape with a yellow "
               "centre"),
 "cave_mouth": ("a flat block of dark brown rock with a plain arch-shaped opening cut out of it, and "
               "through the opening a block of midnight-blue sky with white star dots"),
 "dry_plain":  ("a block of pale blue daytime sky over one flat strip of tan ground, with two trees "
               "each drawn as a brown line with a green cloud on top"),
 "dusk":       ("a flat block of muted orange sky above one flat strip of brown ground, with a plain "
               "orange disc for the sun on the horizon"),
 "modern":     ("a flat block of pale grey wall, a simple bed drawn in a few black lines, and one plain "
               "rectangle for a closed door"),
 "camp_wide":  ("a block of midnight-blue night sky with white star dots, one flat strip of brown "
               "ground, three simple triangle shelters drawn in plain lines, and a small fire drawn as "
               "a wobbly orange shape with a yellow centre"),
 "white":      "a plain WHITE background with generous empty space",
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
        return "Framing: the items in ONE straight horizontal row across the middle, evenly spaced. "
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

# ── BIEU CAM (ArtBible Muc 13: hai nam o MAT; deadpan la mac dinh) ────────
# Moi shot PHAI chon mot cai. Khong co "trung tinh".
FACE = {
 "flat":   "FACE: two dot eyes, eyebrows level, mouth one straight line. ",
 "shock":  "FACE: two dot eyes, eyebrows shot up, mouth a small open circle. ",
 "tired":  "FACE: eyes drawn as two short flat lines, eyebrows sloping down, mouth one straight line. ",
 "worry":  "FACE: two dot eyes, eyebrows tilted up at the inner ends, mouth a small downward curve. ",
 "scared": "FACE: two dot eyes, eyebrows high, mouth a small open circle, one short line beside the head. ",
 "happy":  "FACE: two dot eyes, eyebrows relaxed, mouth an upward curve. ",
 "asleep": "FACE: eyes closed as two short curved lines, mouth one small line. ",
 "dumb":   "FACE: two dot eyes, eyebrows level, mouth one flat line, head tilted slightly. ",
 "curious":"FACE: two dot eyes, one eyebrow higher than the other, mouth a small circle. ",
 "sad":    "FACE: two dot eyes, eyebrows tilted up at the inner ends, mouth a downward curve. ",
}

ANIMAL = ("Any animal in this shot is drawn with MORE detail and body volume than the simple "
          "stick people, filled with FLAT SOLID colour and a black outline, with a small simple "
          "face. The animal is the colour accent of the frame. ")
SCENE_N = ANIMAL   # canh khong co nhan vat nguoi
WHO = {"SCENE_A": ANCIENT, "SCENE_M": MODERN, "SCENE_W": WOMAN, "GROUP": GROUP, "SCENE_N": SCENE_N}


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

io.open("SHOTLINES_FULL.txt", "w", encoding="utf-8").write("\n".join(lines) + "\n")

HEADER = """### TRUOC KHI GEN
1. Chon 16:9 truoc khi chay.
2. Gen vao MOT THU MUC RONG, mot luot (bo dem cua tool dat ten theo thu tu chay).
   Neu tool khong nuot het -> chia dai, MOI DAI MOT THU MUC RIENG, dem tung dai.
3. Dem du dung {N} file roi moi ghep.
4. (KHONG xoa watermark - de nguyen)
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

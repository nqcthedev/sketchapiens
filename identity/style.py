# -*- coding: utf-8 -*-
"""BẢN SẮC HÌNH ẢNH CỦA KÊNH — MỘT nguồn duy nhất cho MỌI video.

VÌ SAO CÓ FILE NÀY
──────────────────
Trước 08/08/2026, các khối STYLE / CONSIST / NEG nằm trong `build_prompts.py` của
TỪNG video. Đo ngày 08/08: chúng đã trôi thành BA bản khác nhau —

    STYLE_CARD    V17  9.563 ký tự  ·  V18 12.232  ·  V19 12.644
    STYLE_SCENE   V17 10.326        ·  V18 12.922  ·  V19 13.334
    NEG_CARD      V17  5.140        ·  V18  5.944  ·  V19  6.356

Tức ba video được gen bằng BA định nghĩa style khác nhau, và không ai quyết định
điều đó — nó xảy ra vì chép file rồi sửa dần. Với kênh faceless thì NHẤT QUÁN HÌNH
ẢNH là tài sản lớn nhất.

⛔ SỬA FILE NÀY LÀ ĐỔI BẢN SẮC CỦA CẢ KÊNH. Không sửa cho riêng một video.
   Muốn một video khác đi thì đổi `subj`/`text` trong shot_data.py của video đó.

Bản này lấy từ V19 (mới nhất, đã qua các sửa 30/07 và 07-08/08).
V17 và V18 giữ bản riêng của chúng làm HIỆN VẬT — prompt phải khớp thứ đã thật sự
dùng để gen ảnh, không được sửa lại lịch sử.
"""

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
 # ── ĐÊM & LỬA (mạch chính của V19) ──
 "fire_ring":  ("one flat block of very dark navy filling most of the frame, and in the middle a small "
               "fire drawn as a wobbly orange shape with a yellow centre on a few grey stones, casting "
               "a soft round patch of warm orange on a flat strip of medium-brown ground"),
 "fire_edge":  ("a warm orange patch of firelight on flat brown ground on one side, and on the other "
               "side a flat block of almost-black navy with nothing drawn in it at all"),
 "night_open": ("a flat block of midnight-blue night sky with plain white dots for stars and a small "
               "white crescent moon, over one flat strip of medium-brown ground, and one tree drawn as "
               "a brown line with a dark green cloud on top"),
 "night_dark": "a flat block of almost-black dark navy filling the whole frame, with nothing else drawn in it",
 "cold_night": ("a flat block of cold blue-grey night sky with a few white star dots, over one flat "
               "strip of pale frosted grey-brown ground, and one bare tree drawn as a brown line with "
               "a few bare twigs"),
 # ── HARAMAYA (huyện hiện đại, ban đêm) ──
 "village_night": ("a flat block of dark navy night sky over one flat strip of dry tan ground, with two "
               "very simple square houses drawn in plain black lines, one small yellow window square, "
               "and a plain dirt path leading away into the dark"),
 # ── HIỆN ĐẠI (khách mời — chỉ hook và kết) ──
 "modern_night": ("a flat block of dark blue-grey bedroom wall, a simple bed drawn in a few black lines, "
               "and one plain rectangle for a doorway with a darker rectangle inside it"),
 "modern_hall": ("a flat block of dark blue-grey wall, one flat strip of pale grey floor, and a plain "
               "open doorway rectangle at one end"),
 # ── CƠ THỂ / KHÁI NIỆM ──
 "dark_card":  ("a flat block of very dark navy filling the entire frame with generous empty space; "
               "every line, shape and letter in this image is drawn in WHITE or pale cream marker on "
               "top of that dark navy, not in black"),
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



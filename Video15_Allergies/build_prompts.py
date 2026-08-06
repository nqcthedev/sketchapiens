#!/usr/bin/env python3
# Ráp PROMPTS_FULL.txt cho V15 Allergies.
# Khối cố định viết 1 lần; mỗi shot chỉ khai báo phần riêng.
# Chạy: python3 build_prompts.py

import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

STYLE = ("Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black outlines "
         "(single clean strokes, not scratchy, not wobbly, not heavy marker), a crisp minimalist "
         "educational look,")

CONSIST = ("The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a simple "
           "expressive face (two big round white eyes with small black pupils, thin expressive eyebrows, "
           "a tiny mouth, no nose) sitting on a THIN body made of clean black lines (a single "
           "medium-weight line for the torso plus thin noodle arms and legs), NOT a filled or solid body "
           "shape, just clean stick lines, with simple rounded mitten hands and small oval feet, ALWAYS "
           "drawn as the SAME stickman, kept identical in every image. The modern man has a BALD round "
           "head with NO hair; ONLY ancient/caveman characters have hair. The body is bare line-art with "
           "no colour fill; a character only wears a garment if their own description names it. Any "
           "animals and props are simple and cute in flat SOLID COLOUR (never black-and-white), each "
           "animal a simple cute character with a little face, drawn with more detail and body volume "
           "than the simple stick people. Clean smooth evenly-weighted medium-bold black outlines "
           "(confident single strokes, not sketchy, not wobbly); flat colours, NO gradient shading, a "
           "clean flat digital-explainer look, evenly drawn (not 3D, not glossy).")

SCENE_HEAD = ("ONE single scene showing ONLY ONE instance of the character; no model sheet, no multiple "
              "poses, no grid, no panels, no split frames; ")

SCENE_TAIL = ("keep it a single flat colour with NO gradient and lots of clean empty space, plus a soft "
              "light-grey shadow under the character; RED is the accent colour for danger, warnings and a "
              "big red X to negate an idea, GREEN for a check mark or safe/yes, a small YELLOW lightbulb "
              "for an idea; draw the people as WHITE-filled black-outline doodles that read clearly on "
              "top of the background,")

NEG = ("Family-friendly, wholesome, cute, gentle, non-violent, no blood, no gore, no injury. no "
       "gradients, no textures, no photorealism, no 3D, no glossy render, no sketchy scratchy lines, no "
       "extra limbs or fingers, no watermark, no logo, no frame borders, no duplicate characters, no "
       "collage, no picture-in-picture, 16:9, clean educational YouTube explainer doodle style.")

# --- NỀN theo ngữ cảnh (PHẦN 0 rule 2) ---
BG = {
    "white":  "the background is a plain WHITE background for concept shots, big-text cards, comparisons, timelines and single isolated objects; ",
    "sky":    "the background is ONE flat blue sky over a flat green ground line; ",
    "dirt":   "the background is ONE flat tan-beige colour for dirt and ground; ",
    "cave":   "the background is ONE flat dark-brown cave interior; ",
    "night":  "the background is ONE flat dark-navy night sky with tiny dots for stars over a flat black ground; ",
    "fire":   "the background is ONE flat warm orange glow for firelight; ",
    "indoor": "the background is ONE flat pale-cream indoor wall colour; ",
    "body":   "the background is ONE flat soft-pink body-interior colour; ",
    "green":  "the background is ONE flat muted green colour; ",
}

# --- KHỐI NHÂN VẬT (lặp Y NGUYÊN, PHẦN 3) ---
CH = {
    "modern":  "the recurring modern guy, the same plain black-outline STICK FIGURE with a plain round BALD white head and NO hair (just a simple face), a bare thin bold black stick-line body, thin bold noodle arms and legs, simple rounded mitten hands and small oval feet, ",
    "caveman": "the recurring caveman, the same plain black-outline stickman with a messy scribbly tuft of short spiky dark doodle hair on top of the head, wearing a simple ragged brown animal-hide smock as a flat brown shape covering the torso, barefoot with small white oval feet, ",
    "woman":   "the recurring ancient woman, the same plain black-outline stickman with long dark hair tied back, wearing a simple brown fibre wrap, barefoot with small white oval feet, ",
    "child":   "a small caveman child with a tiny tuft of dark hair and a small fur wrap, ",
    "none":    "",
}

# --- FRAMING (đổi liên tục) ---
FR = {
    "m": "a medium shot, the subject drawn big and centered with clean breathing space around it.",
    "w": "a WIDE establishing shot, the subject fairly small inside a large scene.",
    "c": "a tight CLOSE-UP on the character's face and shoulders, the expressive face filling most of the frame.",
    "hi": "a HIGH-ANGLE shot looking DOWN, making the subject look small and vulnerable.",
    "lo": "a LOW-ANGLE shot looking UP, making the subject look powerful.",
}


def build(char, subject, framing, bg, text=None):
    """char: khoá CH · subject: hành động+biểu cảm · framing: khoá FR · bg: khoá BG · text: chữ trên hình"""
    t = (f'a small "{text}" in bold black hand-drawn ALL-CAPS marker letters.'
         if text else "no text or letters.")
    return (f"{STYLE} {CH[char]}{subject}. Framing: {FR[framing]} {CONSIST} "
            f"{SCENE_HEAD}{BG[bg]}{SCENE_TAIL} {t} {NEG}")


def main():
    shots_path = os.path.join(HERE, "SHOTLINES_FULL.txt")
    with open(shots_path, encoding="utf-8") as f:
        shotlines = [l.rstrip("\n") for l in f if l.strip()]

    from shot_data import SHOTS  # danh sách phần riêng mỗi shot

    if len(SHOTS) != len(shotlines):
        sys.exit(f"❌ LỆCH: {len(SHOTS)} prompt vs {len(shotlines)} shotline. "
                 f"Phải bằng nhau, nếu không video mất sync.")

    out = []
    for i, (char, subject, framing, bg, text) in enumerate(SHOTS, start=1):
        out.append(f"{i:03d}.\n{build(char, subject, framing, bg, text)}\n")

    dest = os.path.join(HERE, "PROMPTS_FULL.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write("\n".join(out))

    print(f"✅ {len(out)} prompt → PROMPTS_FULL.txt")
    print(f"   shotline: {len(shotlines)} · khớp 1:1")


if __name__ == "__main__":
    main()

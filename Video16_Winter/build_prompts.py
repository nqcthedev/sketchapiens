#!/usr/bin/env python3
"""V16 Winter — dung PROMPTS_FULL.txt tu shot_data.py.

Luat nen (chot 27/07/2026, do tu Zenn 7.81M):
  ~40% trang/nga · ~25% TOI phang · ~30% mau phang · ~5% xam nhat
  Nen = MOT MANG MAU PHANG TUYET DOI. Khong canh ve, khong van, khong duong chan troi.
"""
import sys, pathlib, collections
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from shot_data import SHOTS

STYLE = ("Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black "
         "outlines (single clean strokes, not scratchy, not wobbly, not heavy marker), "
         "a crisp minimalist educational look,")

CONSIST = ("The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a "
           "simple expressive face (two big round white eyes with small black pupils, thin "
           "expressive eyebrows, a tiny mouth, no nose) sitting on a THIN body made of clean "
           "black lines (a single medium-weight line for the torso plus thin noodle arms and "
           "legs) — NOT a filled or solid body shape, just clean stick lines, with simple "
           "rounded mitten hands and small oval feet, ALWAYS drawn as the SAME stickman, kept "
           "identical in every image. The modern man has a BALD round head with NO hair; ONLY "
           "ancient characters have hair. The body is bare line-art with no colour fill; a "
           "character only wears a garment if their own description names it. Any animals and "
           "props are simple and cute in flat SOLID COLOUR (never black-and-white), each animal "
           "a simple cute character with a little face, drawn with more detail and body volume "
           "than the simple stick people. Clean smooth evenly-weighted outlines (confident "
           "single strokes, not sketchy, not wobbly); flat colours, NO gradient shading, a clean "
           "flat digital-explainer look, evenly drawn (not 3D, not glossy).")

# --- NEN: mot mang mau PHANG TUYET DOI, khong canh ve ---
_CORE = ("ONE single scene showing ONLY ONE instance of the character; no model sheet, no "
         "multiple poses, no grid, no panels, no split frames; ")
_EMPTY = ("keep the composition very minimal with ONE clear idea and a LOT of clean empty "
          "space around the subject, roughly two thirds of the frame left empty; NO detailed "
          "environment, NO drawn landscape, NO horizon line, NO texture, NO gradient — the "
          "background is one single perfectly flat colour edge to edge; RED is the accent "
          "colour for danger and warnings and a big red X to negate an idea, GREEN for a check "
          "mark or safe, a small YELLOW lightbulb for an idea,")

_LIGHT = ("IMPORTANT — this is a LIGHT-BACKGROUND image: the background must be the light colour "
          "named above and must NOT be black, NOT dark, NOT inverted; the line art stays BLACK on "
          "the light background, never white-on-black; "
          "the people are drawn as white-filled black-outline doodles with a soft light-grey shadow under them; ")
_DARK = ("on this dark background the character is drawn with a white-filled head and clean "
         "WHITE body lines instead of black so it reads clearly; no shadow; ")

BG = {
    "white": _CORE + "the background is a plain pure WHITE background; " + _LIGHT + _EMPTY,
    "ivory": _CORE + "the background is one flat off-white ivory colour filling the whole frame; " + _LIGHT + _EMPTY,
    "grey":  _CORE + "the background is one flat light grey colour filling the whole frame; " + _LIGHT + _EMPTY,
    "snow":  _CORE + "the background is one flat pale ice-blue colour filling the whole frame; " + _LIGHT + _EMPTY,
    "navy":  _CORE + "the background is one flat DARK NAVY BLUE colour filling the whole frame; " + _DARK + _EMPTY,
    "black": _CORE + "the background is one flat near-black charcoal colour filling the whole frame; " + _DARK + _EMPTY,
    "cold":  _CORE + "the background is one flat cold slate blue-grey colour filling the whole frame; " + _DARK + _EMPTY,
    "cave":  _CORE + "the background is one flat DARK BROWN colour filling the whole frame; " + _DARK + _EMPTY,
    "fire":  _CORE + "the background is one flat warm ORANGE colour filling the whole frame; " + _LIGHT + _EMPTY,
    "tan":   _CORE + "the background is one flat warm sandy KHAKI colour filling the whole frame; " + _LIGHT + _EMPTY,
    "sage":  _CORE + "the background is one flat muted OLIVE GREEN colour filling the whole frame; " + _LIGHT + _EMPTY,
}

NEG = ("Family-friendly, wholesome, cute, gentle, non-violent, no blood, no gore, no injury. "
       "no gradients, no textures, no photorealism, no 3D, no glossy render, no sketchy "
       "scratchy lines, no extra limbs or fingers, no watermark, no logo, no frame borders, "
       "no duplicate characters, no collage, no picture-in-picture, 16:9, clean educational "
       "YouTube explainer doodle style.")

FRAMING = {
    "m": "a medium shot, the subject drawn big and centered with clean breathing space around it.",
    "w": "a WIDE shot, the subject fairly small inside a large empty frame.",
    "c": "a tight CLOSE-UP on the character's face and shoulders, the expressive face filling most of the frame.",
    "d": "a HIGH-ANGLE shot looking DOWN, making the subject look small and vulnerable.",
    "u": "a LOW-ANGLE shot looking UP, making the subject look powerful.",
    "f": "a flat head-on diagram view, the subject drawn big and centered.",
}

MODERN = ("the recurring modern guy, the same plain black-outline STICK FIGURE with a plain "
          "round BALD white head and NO hair (just a simple face), a bare thin stick-line body "
          "(NO clothing, NO filled body shape), thin noodle arms and legs, simple rounded "
          "mitten hands and small oval feet,")
ANCIENT = ("the recurring caveman, the same plain black-outline stickman with a messy scribbly "
           "tuft of short spiky dark doodle hair on top of the head, wearing a simple ragged "
           "brown animal-hide smock as a flat brown shape covering the torso, barefoot with "
           "small white oval feet,")
ANCIENT_F = ("the recurring ancient woman, the same plain black-outline stickman with long dark "
             "hair tied back, wearing a simple brown fibre wrap, barefoot with small white oval feet,")


def build(subject, frame, bg, text):
    t = "no text or letters." if not text else text
    return f"{STYLE} {subject} Framing: {FRAMING[frame]} {CONSIST} {BG[bg]} {t} {NEG}"


def main():
    lines = [l.strip() for l in open(pathlib.Path(__file__).parent / "SHOTLINES_FULL.txt") if l.strip()]
    if len(SHOTS) != len(lines):
        sys.exit(f"DUNG LAI: {len(SHOTS)} prompt vs {len(lines)} shotline — phai bang nhau.")
    out = []
    for i, (subject, frame, bg, text) in enumerate(SHOTS, 1):
        out.append(f"{i:03d}.\n{build(subject, frame, bg, text)}\n")
    p = pathlib.Path(__file__).parent / "PROMPTS_FULL.txt"
    p.write_text("\n".join(out))

    c = collections.Counter(b for _, _, b, _ in SHOTS)
    n = len(SHOTS)
    grp = {"trang/nga": c["white"] + c["ivory"], "TOI phang": c["navy"] + c["black"] + c["cold"] + c["cave"],
           "mau phang": c["fire"] + c["snow"] + c["tan"] + c["sage"], "xam nhat": c["grey"]}
    print(f"OK: {n} prompt -> {p.name}")
    for k, v in grp.items():
        print(f"  {k:>10}: {v:3d}  ({100*v/n:.0f}%)")
    print("  chi tiet:", dict(c))


if __name__ == "__main__":
    main()

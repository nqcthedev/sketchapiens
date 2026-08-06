#!/usr/bin/env python3
"""
Ancient-Humans faceless video pipeline (one image per sentence).

Flow:
  script.txt -> [1] split sentences -> [2] per-sentence image PROMPT (LLM)
             -> [3] image (image API) -> [4] TTS audio + duration
             -> [5] SRT captions -> [6] assemble MP4 (ffmpeg)

Modes:
  --mock : NO API keys. Draws placeholder stick-figure slides (PIL) + silent
           audio with estimated durations, then renders a real MP4 with ffmpeg.
           Use this to verify the whole pipeline end to end.
  (real) : put keys in .env, calls OpenAI (prompts+images) and ElevenLabs/OpenAI (TTS).

Examples:
  python pipeline.py --mock --limit 12
  python pipeline.py --input input/script_video01.txt --out build
"""
import argparse, os, json, subprocess, textwrap, math
from pathlib import Path

DEFAULT_CONFIG = {
    "style_anchor": "Hand-drawn 2D doodle cartoon, flat colors, bold black outlines, slightly imperfect sketchy marker lines,",
    "style_lock": "no gradients, no shadows, no textures, no photorealism, no 3D, 16:9 aspect ratio, educational YouTube explainer doodle style.",
    "resolution": [1920, 1080], "fps": 30,
    "words_per_minute": 140, "min_seconds_per_line": 2.2,
    "llm_model": "gpt-4o-mini", "image_model": "dall-e-3",
    "tts_provider": "elevenlabs", "elevenlabs_voice_id": "REPLACE_ME", "openai_voice": "onyx",
}

def load_config(path):
    cfg = dict(DEFAULT_CONFIG)
    p = Path(path)
    if p.exists():
        try:
            import yaml
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
            cfg.update(data)
        except Exception as e:
            print(f"[warn] config not parsed ({e}); using defaults")
    return cfg

def read_lines(path):
    out = []
    for ln in Path(path).read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#"):
            out.append(ln)
    return out

def estimate_duration(line, cfg):
    words = max(1, len(line.split()))
    secs = words / (cfg["words_per_minute"] / 60.0)
    return round(max(cfg["min_seconds_per_line"], secs), 2)

# ---------- [2] prompt per sentence ----------
ART_BIBLE_RULES = (
    "You write ONE text-to-image prompt for a single narration line, in a hand-drawn COLORED doodle "
    "cartoon style (like the 'Ancient Humans Explained' channels Mack / Stickly).\n"
    "- Begin with the given style anchor, then a concrete scene, then end with the given style lock.\n"
    "- Turn abstract narration into a concrete visual: characters + exact expressions + objects + optional "
    "ALL-CAPS on-screen text or a yellow arrow label.\n"
    "- Flat COLORED fills with bold black outlines. Choose ONE flat background color by emotional tone: "
    "ancient/prehistoric=tan or dark blue; danger=white with red text; happy/discovery=white or yellow; "
    "underwater/science=blue; outdoor/evolution=green ground + blue sky; fire/night/ritual=orange.\n"
    "- When it fits, use a frame type: concept-text frame (big object + ALL CAPS top text); left-to-right "
    "evolution sequence with arrow; labeled diagram (yellow arrow + ALL CAPS label); figure reaction "
    "(thought bubble '?', 'HMMMM', 'WAIT...'); personified concept (angry cartoon face); globe + floating creatures.\n"
    "- Output ONLY the final prompt text."
)

def gen_prompt(line, cfg, mock):
    anchor, lock = cfg["style_anchor"], cfg["style_lock"]
    if mock:
        return (f"{anchor} a flat colored doodle scene illustrating: {line.rstrip('.!?')}, "
                f"simple cartoon figures with colored fills on a solid color background, {lock}")
    from openai import OpenAI
    client = OpenAI()
    r = client.chat.completions.create(
        model=cfg["llm_model"], temperature=0.5,
        messages=[
            {"role": "system", "content": f"{ART_BIBLE_RULES}\nStyle anchor: {anchor}\nStyle lock: {lock}"},
            {"role": "user", "content": line},
        ])
    return r.choices[0].message.content.strip()

# ---------- [3] image ----------
def mock_image(line, idx, path, cfg):
    from PIL import Image, ImageDraw, ImageFont
    W, H = cfg["resolution"]
    palette = ["#F3E9D2", "#DCE6F1", "#E2EFDA", "#FBE5D6", "#EAE2F8", "#FCE4EC"]
    figcol = ["#F5820D", "#2D5FBF", "#3A9E3A", "#F5C518", "#D94040", "#8B5E3C"][idx % 6]
    img = Image.new("RGB", (W, H), palette[idx % len(palette)])
    d = ImageDraw.Draw(img)
    cx, cy = W // 2, H // 2 - 40
    a = (idx * 37 % 60 - 30) * math.pi / 180.0   # vary arm pose per slide
    d.ellipse([cx-40, cy-180, cx+40, cy-100], fill=figcol, outline="black", width=10)
    d.line([cx, cy-100, cx, cy+60], fill="black", width=10)
    d.line([cx, cy-60, cx+int(95*math.cos(a)), cy-60+int(95*math.sin(a))], fill="black", width=10)
    d.line([cx, cy-60, cx-int(95*math.cos(a)), cy-60+int(95*math.sin(a))], fill="black", width=10)
    d.line([cx, cy+60, cx+55, cy+175], fill="black", width=10)
    d.line([cx, cy+60, cx-55, cy+175], fill="black", width=10)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
    except Exception:
        font = ImageFont.load_default(); small = font
    d.multiline_text((W//2, H-200), textwrap.fill(line, 58), fill="#333333", font=font, anchor="ma", align="center")
    d.text((30, 30), f"[MOCK slide #{idx+1}]  (real mode = AI image here)", fill="#9a9a9a", font=small)
    img.save(path)

def gen_image(line, idx, prompt, out_dir, cfg, mock):
    path = out_dir / f"img_{idx:03d}.png"
    if mock:
        mock_image(line, idx, path, cfg); return path
    provider = cfg.get("image_provider", "gemini")
    if provider == "gemini":
        # OUR OWN safe "Smart Ref Binding": for every @TOKEN in the prompt, attach its
        # reference image so Gemini 2.5 Flash Image (Nano Banana) keeps the same
        # character. Official Google API — no third-party app touches your Flow account.
        import re
        from google import genai
        from google.genai import types
        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        contents = [prompt]
        for tok in sorted(set(re.findall(r"@([A-Za-z0-9_]+)", prompt))):
            ref = cfg.get("refs", {}).get(tok)
            if ref and Path(ref).exists():
                contents.append(types.Part.from_bytes(data=Path(ref).read_bytes(), mime_type="image/png"))
        resp = client.models.generate_content(
            model=cfg.get("image_model", "gemini-2.5-flash-image"),
            contents=contents,
            config=types.GenerateContentConfig(response_modalities=["IMAGE"]),  # chỉnh theo SDK nếu cần
        )
        for part in resp.candidates[0].content.parts:
            data = getattr(getattr(part, "inline_data", None), "data", None)
            if data:
                path.write_bytes(data); return path
        raise RuntimeError("Gemini returned no image")
    # provider == "openai"
    from openai import OpenAI
    import requests
    r = OpenAI().images.generate(model=cfg.get("image_model_openai", "dall-e-3"), prompt=prompt, size="1792x1024", n=1)
    path.write_bytes(requests.get(r.data[0].url, timeout=120).content)
    return path

# ---------- [4] tts ----------
def ffprobe_duration(path):
    out = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(path)], capture_output=True, text=True).stdout.strip()
    try: return round(float(out), 2)
    except Exception: return 3.0

def gen_tts(line, idx, out_dir, cfg, mock):
    if mock:
        return None, estimate_duration(line, cfg)
    path = out_dir / f"aud_{idx:03d}.mp3"
    if cfg.get("tts_provider") == "elevenlabs":
        import requests
        rr = requests.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{cfg['elevenlabs_voice_id']}",
            headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"], "content-type": "application/json"},
            json={"text": line, "model_id": "eleven_multilingual_v2"}, timeout=120)
        rr.raise_for_status(); path.write_bytes(rr.content)
    else:
        from openai import OpenAI
        OpenAI().audio.speech.create(model="tts-1", voice=cfg["openai_voice"], input=line).stream_to_file(str(path))
    return path, ffprobe_duration(path)

# ---------- [5] captions ----------
def srt_time(t):
    h = int(t // 3600); m = int((t % 3600) // 60); s = int(t % 60); ms = int((t - int(t)) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

def build_srt(lines, durations, path):
    t = 0.0; blocks = []
    for i, (ln, d) in enumerate(zip(lines, durations), 1):
        blocks.append(f"{i}\n{srt_time(t)} --> {srt_time(t+d)}\n" + "\n".join(textwrap.wrap(ln, 42)) + "\n")
        t += d
    path.write_text("\n".join(blocks), encoding="utf-8")

# ---------- [6] assemble ----------
def run(cmd, **kw): return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)

def assemble(images, durations, audios, out_dir, cfg, mock):
    W, H = cfg["resolution"]; fps = cfg["fps"]
    clips = out_dir / "clips"; clips.mkdir(exist_ok=True)
    vf = f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,format=yuv420p"
    paths = []
    for i, (img, dur) in enumerate(zip(images, durations)):
        c = clips / f"clip_{i:03d}.mp4"
        run(["ffmpeg", "-y", "-loop", "1", "-i", str(img), "-t", str(dur), "-vf", vf,
             "-r", str(fps), "-c:v", "libx264", "-pix_fmt", "yuv420p", str(c)])
        paths.append(c)
    (out_dir / "clips.txt").write_text("".join(f"file '{c.resolve()}'\n" for c in paths))
    concat = out_dir / "concat.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(out_dir / "clips.txt"), "-c", "copy", str(concat)])
    total = round(sum(durations), 2)
    audio = out_dir / "audio.m4a"
    if mock or not any(audios):
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", str(total), "-c:a", "aac", str(audio)])
    else:
        (out_dir / "audio.txt").write_text("".join(f"file '{a.resolve()}'\n" for a in audios if a))
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(out_dir / "audio.txt"), "-c:a", "aac", str(audio)])
    final = out_dir / "final.mp4"
    try:
        run(["ffmpeg", "-y", "-i", str(concat), "-i", str(audio), "-vf", "subtitles=subs.srt",
             "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac",
             "-shortest", "final.mp4"], cwd=str(out_dir))
    except subprocess.CalledProcessError:
        print("[warn] subtitle burn-in failed; rendering without burned subs (subs.srt still saved)")
        run(["ffmpeg", "-y", "-i", str(concat), "-i", str(audio), "-map", "0:v", "-map", "1:a",
             "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(final)])
    return final

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="input/script_video01.txt")
    ap.add_argument("--out", default="build")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--stage", choices=["all", "prompts", "assemble"], default="all",
                    help="all=end-to-end; prompts=only write prompts (paste into Google Flow); assemble=build MP4 from --images-dir")
    ap.add_argument("--images-dir", default=None,
                    help="folder of img_000.png... for --stage assemble (e.g. exports from Google Flow)")
    a = ap.parse_args()
    cfg = load_config(a.config)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    imgs = out / "images"; imgs.mkdir(exist_ok=True)
    auds = out / "audio_lines"; auds.mkdir(exist_ok=True)
    lines = read_lines(a.input)
    if a.limit: lines = lines[:a.limit]

    # --- STAGE: prompts only (the list you batch into Google Flow) ---
    if a.stage == "prompts":
        prompts = [{"i": i, "line": ln, "prompt": gen_prompt(ln, cfg, a.mock),
                    "est_seconds": estimate_duration(ln, cfg)} for i, ln in enumerate(lines)]
        (out / "prompts.json").write_text(json.dumps(prompts, indent=2, ensure_ascii=False), encoding="utf-8")
        (out / "prompts.txt").write_text("\n\n".join(f"[img_{p['i']:03d}] {p['prompt']}" for p in prompts), encoding="utf-8")
        build_srt(lines, [p["est_seconds"] for p in prompts], out / "subs.srt")
        print(f"[prompts] {len(prompts)} prompts -> {out/'prompts.json'} + {out/'prompts.txt'}")
        print("    Next: generate them in Google Flow (split into batches / rotate accounts),")
        print("    save as img_000.png, img_001.png ... then:")
        print(f"    python pipeline.py --stage assemble --images-dir <your_flow_export_folder>")
        return

    # --- STAGE: assemble from a folder of ready images (Flow exports) ---
    if a.stage == "assemble":
        src = Path(a.images_dir) if a.images_dir else imgs
        images = sorted(src.glob("img_*.png")) or sorted(src.glob("*.png"))
        if not images:
            print(f"[error] no images in {src}"); return
        n = min(len(images), len(lines)); images, lines = images[:n], lines[:n]
        audios, durations = [], []
        for i, ln in enumerate(lines):
            ap_, dur = gen_tts(ln, i, auds, cfg, a.mock); audios.append(ap_); durations.append(dur)
        build_srt(lines, durations, out / "subs.srt")
        print(f"[assemble] {n} images from {src}")
        final = assemble(images, durations, audios, out, cfg, a.mock)
        print(f"[done] {final}  ({round(sum(durations),1)}s, {n} slides)")
        return

    # --- STAGE: all (end-to-end; mock placeholder images or real API) ---
    print(f"[1] split -> {len(lines)} sentences  (mode={'MOCK' if a.mock else 'REAL'})")
    prompts, images, audios, durations = [], [], [], []
    for i, ln in enumerate(lines):
        p = gen_prompt(ln, cfg, a.mock); prompts.append({"i": i, "line": ln, "prompt": p})
        images.append(gen_image(ln, i, p, imgs, cfg, a.mock))
        ap_, dur = gen_tts(ln, i, auds, cfg, a.mock); audios.append(ap_); durations.append(dur)
        print(f"    [{i+1}/{len(lines)}] image + audio  dur={dur}s")
    (out / "prompts.json").write_text(json.dumps(prompts, indent=2, ensure_ascii=False), encoding="utf-8")
    build_srt(lines, durations, out / "subs.srt")
    print("[2] assembling MP4 ...")
    final = assemble(images, durations, audios, out, cfg, a.mock)
    print(f"[done] {final}   ({round(sum(durations),1)}s, {len(lines)} slides)")

if __name__ == "__main__":
    main()

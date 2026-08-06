# -*- coding: utf-8 -*-
"""
Video11 pipeline: per-shot TTS (Josh) -> ghép ảnh khớp tiếng -> why-does-your-back-hurt-when-a-cavemans-didnt.mp4
TTS chạy trên SHOTLINES_FULL.txt (193 dòng-shot = 193 ảnh = 193 clip, sync 100%).
Key đọc từ ~/.config/ghepvideo/elevenlabs.key lúc chạy (KHÔNG lưu trong file).
Dùng:
  python3 run_pipeline.py tts [N]   # N = giới hạn test (bỏ trống = full 193)
  python3 run_pipeline.py assemble  # ghép ảnh + audio -> mp4
  python3 run_pipeline.py chapters  # in timestamp từng shot (cho metadata)
  python3 run_pipeline.py all       # tts full rồi ghép
Ảnh đặt trong images/ đặt tên 001.png..193.png theo đúng thứ tự shot.
"""
import os, sys, json, time, subprocess, tempfile, urllib.request, urllib.error

HERE   = os.path.dirname(os.path.abspath(__file__))
NARR   = os.path.join(HERE, "SHOTLINES_FULL.txt")
IMGDIR = os.path.join(HERE, "images")
AUDDIR = os.path.join(HERE, "audio")
OUT    = os.path.join(HERE, "why-does-your-back-hurt-when-a-cavemans-didnt.mp4")
KEYF   = os.path.expanduser("~/.config/ghepvideo/elevenlabs.key")

VOICE_ID = "nzFihrBIvB34imQBuxub"        # Josh - Teacher for Kids
MODEL_ID = "eleven_multilingual_v2"
STABILITY, SIMILARITY, STYLE = 0.5, 0.75, 0.0
W, H, FPS, PAD_SIL, BG = 2048, 1152, 30, 0.15, "white"
NSHOT = 193

def key():
    return open(KEYF).read().strip()

def lines():
    return [l.rstrip("\n") for l in open(NARR, encoding="utf-8").read().splitlines() if l.strip()]

def tts(limit=0):
    os.makedirs(AUDDIR, exist_ok=True)
    ls = lines()
    if limit: ls = ls[:limit]
    api = key()
    print(f"TTS {len(ls)} shot (Josh) -> audio/ ...", flush=True)
    for i, text in enumerate(ls, 1):
        out = os.path.join(AUDDIR, f"{i:03d}.mp3")
        if os.path.exists(out) and os.path.getsize(out) > 0:
            continue
        payload = json.dumps({"text": text, "model_id": MODEL_ID,
            "voice_settings": {"stability": STABILITY, "similarity_boost": SIMILARITY, "style": STYLE}}).encode()
        req = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
            data=payload, headers={"xi-api-key": api, "Content-Type": "application/json"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=90) as r:
                    open(out, "wb").write(r.read())
                print(f"  [{i:03d}/{len(ls)}] ok", flush=True); break
            except urllib.error.HTTPError as e:
                body = e.read()[:150]
                if e.code == 429:
                    print(f"  [{i:03d}] rate-limit, đợi 10s", flush=True); time.sleep(10)
                else:
                    print(f"  [{i:03d}] HTTP {e.code}: {body}", flush=True); time.sleep(3)
            except Exception as e:
                print(f"  [{i:03d}] {e}, thử lại", flush=True); time.sleep(4)
        time.sleep(0.2)
    have = len([f for f in os.listdir(AUDDIR) if f.endswith(".mp3")])
    print(f"TTS xong. audio/ có {have} file.", flush=True)
    return have

def dur(p):
    o = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","default=nk=1:nw=1", p], capture_output=True, text=True)
    return float(o.stdout.strip())

def assemble():
    imgs = sorted([f for f in os.listdir(IMGDIR) if f.lower().endswith((".png",".jpg",".jpeg",".webp"))])
    auds = sorted([f for f in os.listdir(AUDDIR) if f.lower().endswith(".mp3")])
    n = min(len(imgs), len(auds))
    if len(imgs) != len(auds):
        print(f"⚠ ảnh {len(imgs)} ≠ tiếng {len(auds)} -> ghép {n} cặp đầu", flush=True)
    tmp = tempfile.mkdtemp(); clips=[]
    print(f"Ghép {n} cặp -> {os.path.basename(OUT)} ({W}x{H})", flush=True)
    for i in range(n):
        ip = os.path.join(IMGDIR, imgs[i]); ap = os.path.join(AUDDIR, auds[i])
        d = dur(ap) + PAD_SIL
        clip = os.path.join(tmp, f"c{i:04d}.mp4")
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
              f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color={BG},setsar=1,fps={FPS}")
        subprocess.run(["ffmpeg","-y","-loglevel","error","-loop","1","-i",ip,"-i",ap,
            "-t",f"{d:.3f}","-vf",vf,"-af",f"apad=pad_dur={PAD_SIL}",
            "-c:v","libx264","-pix_fmt","yuv420p","-tune","stillimage",
            "-c:a","aac","-b:a","192k","-r",str(FPS),clip], check=True)
        clips.append(clip)
        if (i+1)%25==0 or i+1==n: print(f"  {i+1}/{n}", flush=True)
    lst = os.path.join(tmp,"list.txt")
    open(lst,"w").write("\n".join(f"file '{c}'" for c in clips))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,
        "-c","copy", OUT], check=True)
    print(f"XONG -> {OUT}", flush=True)
    print(f"Thời lượng: {dur(OUT)/60:.1f} phút", flush=True)

def chapters():
    """In timestamp tích luỹ từng shot (khớp cách assemble tính mỗi clip = dur(mp3)+PAD_SIL)."""
    auds = sorted([f for f in os.listdir(AUDDIR) if f.lower().endswith(".mp3")])
    ls = lines()
    t = 0.0
    print("shot  start        line", flush=True)
    for i, a in enumerate(auds, 1):
        mm, ss = divmod(int(t), 60)
        txt = ls[i-1] if i-1 < len(ls) else ""
        print(f"{i:03d}  {mm:02d}:{ss:02d}  {txt}", flush=True)
        t += dur(os.path.join(AUDDIR, a)) + PAD_SIL
    mm, ss = divmod(int(t), 60)
    print(f"TỔNG: {mm:02d}:{ss:02d} ({t/60:.2f} phút)", flush=True)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd == "tts":
        tts(int(sys.argv[2]) if len(sys.argv) > 2 else 0)
    elif cmd == "assemble":
        assemble()
    elif cmd == "chapters":
        chapters()
    else:
        got = tts(0)
        if got >= NSHOT: assemble()
        else: print(f"⚠ Mới có {got}/{NSHOT} file tiếng, chạy lại 'tts' cho đủ rồi 'assemble'.", flush=True)

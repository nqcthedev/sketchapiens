#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TOOL: 1 file AUDIO đầy đủ + folder ẢNH  ->  video tự kéo từng ảnh KHỚP từng câu.
Dùng khi bạn ĐÃ có sẵn 1 file giọng đọc nguyên bài (không cắt theo shot).
AI (Whisper) chỉ làm 1 việc: dò xem mỗi câu nằm ở giây nào trong audio.

CÀI ĐẶT (chạy 1 lần):
    pip install faster-whisper
    (cần ffmpeg + ffprobe trong máy)

CÁCH DÙNG:
    - Đặt: full_audio.mp3 (giọng đọc) ,  images/ (001..754) ,  TTS_input_per_shot.txt (754 shot)
    - python3 tool_align_full_audio.py
    -> ra final_video.mp4 (ảnh khớp câu, dùng đúng file audio gốc của bạn)
"""
import os, re, sys, subprocess, shutil, difflib, tempfile

AUDIO   = "full_audio.mp3"
IMG_DIR = "images"
SHOTS   = "TTS_input_per_shot.txt"
OUT     = "final_video.mp4"
W, H, FPS = 2048, 1152, 30
BG      = "white"
MODEL   = "small"      # tiny/base/small/medium — small đủ tốt + nhanh
MIN_DUR = 0.4          # mỗi ảnh hiện tối thiểu (giây)

def norm(w): return re.sub(r"[^a-z0-9]", "", w.lower())
def nat(f):
    m = re.findall(r"\d+", os.path.basename(f)); return int(m[-1]) if m else 0
def ffdur(p):
    o = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","default=nk=1:nw=1", p], capture_output=True, text=True)
    return float(o.stdout.strip())

# ---- alignment core (tách riêng để test được, không cần Whisper) ----
def align_times(swords, ww, audio_dur):
    """swords: list từ trong kịch bản (đã norm). ww: list (word,start,end) từ Whisper.
    Trả về time_of[k] = mốc giây cho từng từ kịch bản."""
    wtok = [w[0] for w in ww]
    time_of = [None]*len(swords)
    sm = difflib.SequenceMatcher(a=swords, b=wtok, autojunk=False)
    for a, b, size in sm.get_matching_blocks():
        for k in range(size):
            time_of[a+k] = ww[b+k][1]
    known = [(k,t) for k,t in enumerate(time_of) if t is not None]
    if not known:
        return [audio_dur*k/max(len(swords),1) for k in range(len(swords))]
    fk, ft = known[0]
    for k in range(fk): time_of[k] = ft*k/max(fk,1)
    for (k1,t1),(k2,t2) in zip(known, known[1:]):
        for k in range(k1+1,k2):
            time_of[k] = t1 + (t2-t1)*(k-k1)/(k2-k1)
    lk, lt = known[-1]
    for k in range(lk+1,len(swords)):
        time_of[k] = lt + (audio_dur-lt)*(k-lk)/max(len(swords)-lk,1)
    for k in range(1,len(time_of)):                 # ép tăng dần
        if time_of[k] < time_of[k-1]: time_of[k] = time_of[k-1]
    return time_of

def shot_spans(owner, time_of, nshots, audio_dur):
    starts = [None]*nshots
    for k,i in enumerate(owner):
        if starts[i] is None: starts[i] = time_of[k]
    for i in range(nshots):
        if starts[i] is None: starts[i] = starts[i-1] if i>0 else 0.0
    for i in range(1,nshots):
        if starts[i] < starts[i-1]: starts[i] = starts[i-1]
    spans=[]
    for i in range(nshots):
        s = starts[i]; e = starts[i+1] if i+1<nshots else audio_dur
        if e - s < MIN_DUR: e = s + MIN_DUR
        spans.append((s,e))
    return spans

def whisper_words(audio):
    from faster_whisper import WhisperModel
    print(f"Whisper ({MODEL}) đang nghe audio...")
    m = WhisperModel(MODEL, device="cpu", compute_type="int8")
    segs,_ = m.transcribe(audio, word_timestamps=True, language="en")
    out=[]
    for s in segs:
        for w in (s.words or []):
            n=norm(w.word)
            if n: out.append((n, w.start, w.end))
    print(f"  nghe được {len(out)} từ.")
    return out

def main():
    for t in ("ffmpeg","ffprobe"):
        if not shutil.which(t): print(f"⚠ Thiếu {t}."); sys.exit(1)
    if not os.path.exists(AUDIO): print(f"⚠ Không thấy {AUDIO}"); sys.exit(1)
    imgs = sorted([os.path.join(IMG_DIR,x) for x in os.listdir(IMG_DIR)
                   if x.lower().endswith((".png",".jpg",".jpeg",".webp"))], key=nat)
    shots = [l.strip() for l in open(SHOTS,encoding="utf-8") if l.strip()]
    if len(imgs) != len(shots):
        print(f"⚠ Số ảnh ({len(imgs)}) ≠ số shot ({len(shots)}). Ghép {min(len(imgs),len(shots))} đầu.")
    n = min(len(imgs), len(shots))
    swords=[]; owner=[]
    for i in range(n):
        for w in shots[i].split():
            if norm(w): swords.append(norm(w)); owner.append(i)
    dur = ffdur(AUDIO)
    ww = whisper_words(AUDIO)
    time_of = align_times(swords, ww, dur)
    spans = shot_spans(owner, time_of, n, dur)
    # assemble: video câm theo span -> mux audio gốc
    tmp = tempfile.mkdtemp(); clips=[]
    print(f"Kéo {n} ảnh khớp câu -> {OUT}")
    for i in range(n):
        d = max(spans[i][1]-spans[i][0], MIN_DUR)
        clip = os.path.join(tmp,f"c{i:04d}.mp4")
        vf=(f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
            f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color={BG},setsar=1,fps={FPS}")
        subprocess.run(["ffmpeg","-y","-loglevel","error","-loop","1","-i",imgs[i],
            "-t",f"{d:.3f}","-vf",vf,"-an","-c:v","libx264","-pix_fmt","yuv420p","-r",str(FPS),clip],check=True)
        clips.append(clip)
        if (i+1)%50==0 or i+1==n: print(f"  {i+1}/{n}")
    lst=os.path.join(tmp,"l.txt"); open(lst,"w").write("\n".join(f"file '{c}'" for c in clips))
    silent=os.path.join(tmp,"silent.mp4")
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,"-c","copy",silent],check=True)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",silent,"-i",AUDIO,
        "-c:v","copy","-c:a","aac","-b:a","192k","-shortest",OUT],check=True)
    shutil.rmtree(tmp,ignore_errors=True)
    print(f"✅ XONG: {OUT} — {n} ảnh kéo khớp từng câu theo audio gốc.")

if __name__ == "__main__":
    main()

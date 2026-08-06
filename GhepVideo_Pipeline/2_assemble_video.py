#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BƯỚC 2 — Ghép ẢNH + TIẾNG thành video KHỚP 100% (không kéo tay).
Mỗi ảnh hiển thị ĐÚNG bằng độ dài file tiếng cùng số thứ tự.
  images/001.png (hoặc .jpg) + audio/001.mp3  -> ảnh 1 hiện đúng độ dài tiếng 1
  ... nối hết 754 cặp -> final_video.mp4

CÁCH DÙNG:
  - Cần ffmpeg + ffprobe (đa số máy có; Mac: brew install ffmpeg)
  - Để ảnh vào folder images/ , tiếng vào folder audio/ (tên 001,002,... cùng thứ tự)
  - python3 2_assemble_video.py
"""
import os, re, subprocess, sys, tempfile, shutil

IMG_DIR = "images"
AUD_DIR = "audio"
OUT     = "final_video.mp4"
W, H    = 2048, 1152          # 2K 16:9 (đổi 3840x2160 nếu muốn 4K)
FPS     = 30
PAD_SIL = 0.15                 # khoảng lặng nhỏ cuối mỗi ảnh (giây) cho đỡ gấp
BG      = "white"

def nat(f):                    # lấy số cuối trong tên file để sắp đúng thứ tự
    m = re.findall(r"\d+", os.path.basename(f))
    return int(m[-1]) if m else 0

def listdir(d, exts):
    fs = [os.path.join(d, x) for x in os.listdir(d) if x.lower().endswith(exts)]
    return sorted(fs, key=nat)

def dur(path):                 # độ dài audio bằng ffprobe
    out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                          "-of","default=nk=1:nw=1", path], capture_output=True, text=True)
    return float(out.stdout.strip())

def main():
    for tool in ("ffmpeg","ffprobe"):
        if not shutil.which(tool): print(f"⚠ Thiếu {tool}. Cài ffmpeg trước."); sys.exit(1)
    imgs = listdir(IMG_DIR, (".png",".jpg",".jpeg",".webp"))
    auds = listdir(AUD_DIR, (".mp3",".wav",".m4a",".aac"))
    if not imgs or not auds: print("⚠ Thiếu ảnh hoặc tiếng. Kiểm tra images/ và audio/"); sys.exit(1)
    n = min(len(imgs), len(auds))
    if len(imgs) != len(auds):
        print(f"⚠ Số ảnh ({len(imgs)}) ≠ số tiếng ({len(auds)}). Ghép {n} cặp đầu, kiểm tra lại tên file!")
    tmp = tempfile.mkdtemp(); clips=[]
    print(f"Ghép {n} cặp -> {OUT} ({W}x{H})")
    for i in range(n):
        d = dur(auds[i]) + PAD_SIL
        clip = os.path.join(tmp, f"c{i:04d}.mp4")
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
              f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:color={BG},setsar=1,fps={FPS}")
        subprocess.run(["ffmpeg","-y","-loglevel","error","-loop","1","-i",imgs[i],"-i",auds[i],
            "-t",f"{d:.3f}","-vf",vf,"-af",f"apad=pad_dur={PAD_SIL}",
            "-c:v","libx264","-pix_fmt","yuv420p","-tune","stillimage",
            "-c:a","aac","-b:a","192k","-r",str(FPS),clip], check=True)
        clips.append(clip)
        if (i+1)%50==0 or i+1==n: print(f"  {i+1}/{n}")
    lst = os.path.join(tmp,"list.txt")
    open(lst,"w").write("\n".join(f"file '{c}'" for c in clips))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,
                    "-c","copy",OUT], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"✅ XONG: {OUT} — ảnh khớp tiếng 100%, tổng {n} cảnh.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GHÉP ẢNH + TIẾNG thành video khớp 100% — MỘT bản cho MỌI video.

    python3 tools/assemble.py <thư_mục_làm_việc>

Trước 08/08/2026 file này bị chép vào từng thư mục video. Nay MỘT bản.
Mọi đường dẫn bên dưới là TƯƠNG ĐỐI — script tự chuyển vào thư mục được chỉ định,
nên hành vi giữ nguyên y hệt bản cũ.
"""
import os as _os, sys as _sys
_d = _sys.argv[1] if len(_sys.argv) > 1 else "."
_os.chdir(_os.path.abspath(_d))
_sys.argv = _sys.argv[:1] + _sys.argv[2:]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BƯỚC 2 — Ghép ẢNH + TIẾNG thành video KHỚP 100% (không kéo tay).
Mỗi ảnh hiện ĐÚNG bằng độ dài file tiếng cùng số thứ tự.

KHÁC BẢN V15: ảnh V16 là 1376x768 (tỉ lệ 1.7917) chứ không đúng 16:9 (1.7778).
Nếu dùng pad màu trắng như V15 thì 34 ảnh nền TỐI sẽ bị hai vạch trắng trên/dưới.
=> Ở đây CROP nhẹ (mất ~0.8% chiều cao, mắt không thấy) thay vì pad.
"""
import os, re, subprocess, sys, tempfile, shutil

IMG_DIR = "images"
AUD_DIR = "audio"
OUT     = "final_video.mp4"
W, H    = 2048, 1152          # 2K 16:9
FPS     = 30
PAD_SIL = 0.15                # khoảng lặng nhỏ cuối mỗi ảnh cho đỡ gấp

def nat(f):
    # LUU Y: phai bo duoi file TRUOC khi tim so.
    # ".mp3" co chu so 3 -> ban cu lay so cuoi cung se ra 3 cho MOI file mp3,
    # khien toan bo audio sap xep sai (loi da lam hong V15).
    stem = os.path.splitext(os.path.basename(f))[0]
    m = re.findall(r"\d+", stem)
    return int(m[-1]) if m else 0

def listdir(d, exts):
    fs = [os.path.join(d, x) for x in os.listdir(d) if x.lower().endswith(exts)]
    return sorted(fs, key=nat)

def dur(path):
    out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                          "-of","default=nk=1:nw=1", path], capture_output=True, text=True)
    return float(out.stdout.strip())

def main():
    for tool in ("ffmpeg","ffprobe"):
        if not shutil.which(tool): print(f"⚠ Thiếu {tool}."); sys.exit(1)
    imgs = listdir(IMG_DIR, (".png",".jpg",".jpeg",".webp"))
    auds = listdir(AUD_DIR, (".mp3",".wav",".m4a",".aac"))

    # CHẶN CỨNG: lệch số là dừng, không ghép bừa
    if len(imgs) != len(auds):
        print(f"⛔ DỪNG: {len(imgs)} ảnh vs {len(auds)} tiếng — phải bằng nhau."); sys.exit(1)
    n = len(imgs)
    for i in range(n):
        if nat(imgs[i]) != nat(auds[i]):
            print(f"⛔ DỪNG: lệch cặp ở vị trí {i+1}: {imgs[i]} vs {auds[i]}"); sys.exit(1)

    tmp = tempfile.mkdtemp(); clips=[]; tong=0.0
    print(f"Ghép {n} cặp -> {OUT} ({W}x{H})")
    # increase + crop: phủ kín khung, không có vạch nền
    vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
          f"crop={W}:{H},setsar=1,fps={FPS}")
    for i in range(n):
        d = dur(auds[i]) + PAD_SIL; tong += d
        clip = os.path.join(tmp, f"c{i:04d}.mp4")
        subprocess.run(["ffmpeg","-y","-loglevel","error","-loop","1","-i",imgs[i],"-i",auds[i],
            "-t",f"{d:.3f}","-vf",vf,"-af",f"apad=pad_dur={PAD_SIL}",
            "-c:v","libx264","-pix_fmt","yuv420p","-tune","stillimage",
            "-c:a","aac","-b:a","192k","-r",str(FPS),clip], check=True)
        clips.append(clip)
        if (i+1)%25==0 or i+1==n: print(f"  {i+1}/{n}")
    lst = os.path.join(tmp,"list.txt")
    open(lst,"w").write("\n".join(f"file '{c}'" for c in clips))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",lst,
                    "-c","copy",OUT], check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    m, s = divmod(int(tong), 60)
    print(f"✅ XONG: {OUT} — {n} cảnh, dài {m}:{s:02d}, nhịp {tong/n:.2f}s/cảnh.")

if __name__ == "__main__":
    main()

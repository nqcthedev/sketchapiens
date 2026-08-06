#!/usr/bin/env python3
"""
Dựng Short dọc 1080x1920 từ ảnh + audio ĐÃ CÓ của một video dài.
Không gen gì mới — chỉ cắt lại và đóng khung.

Dùng:
    python3 make_short.py <thư_mục_video> <shot_đầu> <shot_cuối> "<TIÊU ĐỀ>" <file_ra.mp4> [bed.mp3]

Ví dụ:
    python3 make_short.py Video14_Milk 1 27 "EVERY MAMMAL QUITS MILK" shorts/short01.mp4 shorts/bed.mp3

Yêu cầu thư mục video có: SHOTLINES_FULL.txt · images/NNN.(png|jpeg) · build/audio/NNN.mp3
"""
import subprocess, sys, os, textwrap, shutil

FONT = "/System/Library/Fonts/Supplemental/Arial Black.ttf"
W, H = 1080, 1920
BG = "0xF4F1EA"          # nền kem, để ảnh trắng nổi thành tấm thẻ
TITLE_SIZE = 76
TITLE_WRAP = 13          # ký tự/dòng — quá số này là tràn khung ở cỡ chữ trên
CAP_SIZE = 72
CAP_WRAP = 18
CAP_CENTER_Y = 1400      # tâm khối phụ đề; để cao hơn 1600 vì YouTube phủ UI ~300px dưới cùng
IMG_TOP = 400
BED_DB = -21             # mức nhạc nền


def img_path(d, i):
    for e in ("png", "jpeg", "jpg", "webp"):
        p = os.path.join(d, "images", f"{i:03d}.{e}")
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f"không thấy ảnh {i:03d} trong {d}/images")


def dur(p):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
        capture_output=True, text=True).stdout)


def drawtext(tmp, tag, text, size, y, color="black", border=None):
    """textfile= thay vì text= để khỏi phải escape dấu nháy."""
    p = os.path.join(tmp, f"{tag}.txt")
    open(p, "w", encoding="utf-8").write(text)
    s = f"drawtext=fontfile='{FONT}':textfile='{p}':fontcolor={color}:fontsize={size}:x=(w-tw)/2:y={y}"
    if border:
        s += f":borderw={border}:bordercolor=black"
    return s


def main():
    if len(sys.argv) < 6:
        print(__doc__)
        sys.exit(1)
    vdir, a, b, title, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4], sys.argv[5]
    bed = sys.argv[6] if len(sys.argv) > 6 else None

    tmp = os.path.join(os.path.dirname(out) or ".", "_tmp_short")
    shutil.rmtree(tmp, ignore_errors=True)
    os.makedirs(tmp, exist_ok=True)

    lines = [l.strip() for l in open(os.path.join(vdir, "SHOTLINES_FULL.txt"), encoding="utf-8") if l.strip()]
    if b > len(lines):
        sys.exit(f"❌ shot cuối {b} vượt quá {len(lines)} shotline")

    # tiêu đề tự xuống dòng — đây là chỗ bản đầu bị tràn
    tlines = textwrap.wrap(title, width=TITLE_WRAP)
    title_draw = [drawtext(tmp, f"t{k}", l, TITLE_SIZE, 130 + k * 92, "0xFFC800", border=7)
                  for k, l in enumerate(tlines)]

    parts = []
    for i in range(a, b + 1):
        aud = os.path.join(vdir, "build", "audio", f"{i:03d}.mp3")
        d = dur(aud)
        # phụ đề: KHÔNG BAO GIỜ cắt bớt chữ — co cỡ chữ cho tới khi vừa 4 dòng
        size, wrapw = CAP_SIZE, CAP_WRAP
        while True:
            cap = textwrap.wrap(lines[i - 1], width=wrapw)
            if len(cap) <= 4 or size <= 44:
                break
            size -= 6
            wrapw = int(CAP_WRAP * CAP_SIZE / size)
        lh = int(size * 1.36)
        cy = CAP_CENTER_Y - (len(cap) * lh) // 2
        draw = title_draw + [drawtext(tmp, f"c{i:03d}_{k}", l, size, cy + k * lh)
                             for k, l in enumerate(cap)]
        vf = (f"crop={W}:768:(iw-{W})/2:0,scale={W}:-2,"
              f"pad={W}:{H}:(ow-iw)/2:{IMG_TOP}:{BG}," + ",".join(draw))
        o = os.path.join(tmp, f"s{i:03d}.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", img_path(vdir, i),
                        "-i", aud, "-vf", vf, "-c:v", "libx264", "-t", f"{d + 0.08:.3f}",
                        "-pix_fmt", "yuv420p", "-r", "30", "-c:a", "aac", "-b:a", "192k",
                        "-af", "apad", "-shortest", o], check=True)
        parts.append(o)

    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").write("".join(f"file '{os.path.basename(p)}'\n" for p in parts))
    dry = os.path.join(tmp, "dry.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", lst, "-c", "copy", dry], check=True)

    total = dur(dry)
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    if bed and os.path.exists(bed):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", dry,
                        "-stream_loop", "9", "-i", bed, "-filter_complex",
                        f"[1:a]volume={BED_DB}dB,afade=t=in:st=0:d=1.5,"
                        f"afade=t=out:st={total-2:.2f}:d=2,atrim=0:{total:.2f}[bed];"
                        f"[0:a][bed]amix=inputs=2:duration=first:dropout_transition=0:normalize=0[a]",
                        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        out], check=True)
    else:
        shutil.copy(dry, out)

    shutil.rmtree(tmp, ignore_errors=True)
    print(f"✅ {out} · {total:.1f}s · shot {a:03d}-{b:03d} · tiêu đề {len(tlines)} dòng")


if __name__ == "__main__":
    main()

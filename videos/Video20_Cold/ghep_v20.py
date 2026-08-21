#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GHÉP V20 — ảnh + tiếng, sync theo MẪU WAV.

    python3 ghep_v20.py <thư_mục_ảnh>

VÌ SAO KHÔNG DÙNG ffprobe ĐỂ ĐO mp3
───────────────────────────────────
Đo thật khi ghép V19: tổng 227 mp3 rời theo ffprobe = 570,279 s, nhưng file tiếng
sau khi ghép = 561,737 s → lệch +8,542 s. Mỗi mp3 mang đệm của bộ mã hoá; ffprobe
đếm cả đệm, lúc ghép thì đệm bị nuốt. Lấy số của ffprobe làm thời lượng ảnh thì
HÌNH TRÔI KHỎI TIẾNG, càng về cuối càng lệch, VÀ KHÔNG BÁO LỖI GÌ CẢ.

→ Quy hết sang WAV, đếm getnframes()/getframerate(), và ghép dải tiếng bằng WAV.

VÌ SAO ĐÁNH SỐ TƯỜNG MINH
─────────────────────────
V15 hỏng vì script tự viết sắp xếp mp3 sai thứ tự. Ở đây mọi danh sách đều dựng
từ range(1, N+1) và assert sự tồn tại của từng số, không bao giờ dùng glob+sort.
"""
import os, subprocess, sys, wave, json, shutil

V = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
AUD = os.path.join(V, "audio")
WAV = os.path.join(V, "_wav")
OUT = os.path.join(V, "V20_Cold.mp4")
W, H, FPS = 1920, 1080, 30


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def die(msg):
    sys.exit("⛔ " + msg)


# ── 1. ĐẾM ĐẦU VÀO — ba con số phải bằng nhau ────────────────────────────────
lines = [l.rstrip("\n") for l in open(os.path.join(V, "SHOTLINES_FULL.txt"),
                                      encoding="utf-8") if l.strip()]
N = len(lines)
if not IMG or not os.path.isdir(IMG):
    die("chưa chỉ thư mục ảnh")

imgs, mp3s = [], []
for i in range(1, N + 1):                      # TƯỜNG MINH, không glob+sort
    p = os.path.join(IMG, f"{i:03d}.png")
    if not os.path.exists(p):
        p = os.path.join(IMG, f"{i:03d}.jpg")
    if not os.path.exists(p):
        die(f"thiếu ảnh {i:03d}")
    imgs.append(p)
    a = os.path.join(AUD, f"{i:03d}.mp3")
    if not os.path.exists(a) or os.path.getsize(a) < 1000:
        die(f"thiếu/hỏng tiếng {i:03d}")
    mp3s.append(a)
print(f"✅ shot {N} · ảnh {len(imgs)} · tiếng {len(mp3s)} — ba số bằng nhau")

# ── 2. mp3 -> WAV, ĐẾM MẪU ───────────────────────────────────────────────────
os.makedirs(WAV, exist_ok=True)
durs = []
for i, a in enumerate(mp3s, 1):
    w = os.path.join(WAV, f"{i:03d}.wav")
    if not os.path.exists(w):
        run(["ffmpeg", "-y", "-v", "error", "-i", a,
             "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", w])
    with wave.open(w) as f:
        durs.append(f.getnframes() / f.getframerate())
tong_roi = sum(durs)
print(f"✅ WAV {len(durs)} file · tổng {tong_roi:.3f}s")

# ── 3. GHÉP TIẾNG BẰNG WAV ───────────────────────────────────────────────────
lst = os.path.join(WAV, "_list.txt")
with open(lst, "w") as f:
    for i in range(1, N + 1):
        f.write(f"file '{i:03d}.wav'\n")
allwav = os.path.join(V, "_all.wav")
run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
     "-i", lst, "-c", "copy", allwav])
with wave.open(allwav) as f:
    tong_ghep = f.getnframes() / f.getframerate()
lech = abs(tong_ghep - tong_roi)
print(f"   tiếng ghép {tong_ghep:.3f}s · lệch {lech*1000:.1f} ms")
if lech > 0.05:
    die(f"tiếng ghép lệch tổng WAV {lech:.3f}s — dừng, không ghép hình")
print("✅ CHỐT 1: tổng WAV == tiếng ghép")

# ── 4. DỰNG DẢI HÌNH THEO ĐÚNG durs ──────────────────────────────────────────
# 🔴 VÁ 15/08 — KHÔNG ghi độ dài từng shot rời, vì ffmpeg cắt mỗi shot về mốc
# khung 30fps và 282 lần làm tròn XUỐNG cộng lại làm video ngắn hơn tiếng 1,466s.
# Neo theo MỐC TÍCH LUỸ: quy mốc bắt đầu của từng shot về số khung, rồi lấy hiệu.
# Sai số của mỗi shot khi đó ≤ nửa khung và KHÔNG dồn lại.
_cum, _acc = [0.0], 0.0
for d in durs:
    _acc += d
    _cum.append(_acc)
_fr = [round(c * FPS) for c in _cum]
durs_align = [(_fr[i + 1] - _fr[i]) / FPS for i in range(N)]
print(f"   neo khung: tổng {sum(durs_align):.3f}s (tiếng {tong_ghep:.3f}s, "
      f"lệch {abs(sum(durs_align)-tong_ghep)*1000:.0f} ms)")

cc = os.path.join(V, "_concat.txt")
with open(cc, "w") as f:
    # 🔴 VÁ 2 (15/08) — ĐO THẬT, đừng tin luật truyền miệng "phải lặp ảnh cuối".
    # Bài đo 3 ảnh × 2s, kỳ vọng 6,0s:
    #   lặp ảnh cuối            -> 8,0s  (mục lặp THỪA HƯỞNG duration trước đó)
    #   lặp bằng bản sao khác tên -> 8,0s
    #   KHÔNG lặp, chỉ duration   -> 6,0s  ✅
    # Và gốc rễ thật của việc mất khung cuối: 279 ảnh trong lô là JPEG đội tên .png,
    # chỉ 3 ảnh thay tay là PNG thật -> concat chọn một bộ giải mã theo file đầu,
    # gặp file khác kiểu ở CUỐI thì bỏ luôn. Nay cả 282 đã đồng nhất mjpeg.
    for p, d in zip(imgs, durs_align):
        f.write(f"file '{p}'\nduration {d:.6f}\n")

run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", cc,
     "-i", allwav,
     "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
            f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white,fps={FPS}",
     "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", "-t", f"{tong_ghep:.3f}", OUT])

d_mp4 = float(json.loads(run(["ffprobe", "-v", "quiet", "-print_format", "json",
                              "-show_format", OUT]).stdout)["format"]["duration"])
print(f"✅ render xong: {OUT}")
print(f"   video {d_mp4:.3f}s · tiếng {tong_ghep:.3f}s · lệch {abs(d_mp4-tong_ghep)*1000:.0f} ms")
if abs(d_mp4 - tong_ghep) > 0.5:
    die("độ dài mp4 lệch dải tiếng quá 0,5s")
print("✅ CHỐT 2: độ dài mp4 == độ dài tiếng")

# ── 5. CHỐT 3 — ĐỐI CHIẾU PIXEL Ở 9 MỐC ──────────────────────────────────────
moc = [1, 30, 75, 120, 150, 180, 210, 223, 269, N - 1, N]  # 223/269 là ảnh thay tay
start = [0.0]
for d in durs_align:
    start.append(start[-1] + d)
tmp = os.path.join(V, "_kiem")
os.makedirs(tmp, exist_ok=True)
xau = []
for s in moc:
    giua = start[s - 1] + durs_align[s - 1] / 2
    a = os.path.join(tmp, f"mp4_{s:03d}.png")
    b = os.path.join(tmp, f"src_{s:03d}.png")
    run(["ffmpeg", "-y", "-v", "error", "-ss", f"{giua:.3f}", "-i", OUT,
         "-frames:v", "1", a])
    run(["ffmpeg", "-y", "-v", "error", "-i", imgs[s - 1],
         "-vf", f"scale={W}:{H}:force_original_aspect_ratio=decrease,"
                f"pad={W}:{H}:(ow-iw)/2:(oh-ih)/2:white", "-frames:v", "1", b])
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", a, "-i", b,
                        "-filter_complex", "blend=all_mode=difference,"
                        "blackframe=amount=0:threshold=8", "-f", "null", "-"],
                       capture_output=True, text=True)
    pct = 100.0
    for ln in r.stderr.splitlines():
        if "blackframe" in ln and "pblack:" in ln:
            pct = 100 - float(ln.split("pblack:")[1].split()[0])
            break
    print(f"   shot {s:3d} @ {giua:7.2f}s → khác {pct:5.2f}%")
    if pct > 2.0:
        xau.append(s)
if xau:
    die(f"lệch hình-tiếng ở shot {xau}")
print(f"✅ CHỐT 3: {len(moc)}/{len(moc)} mốc khớp hình")
shutil.rmtree(tmp, ignore_errors=True)
print(f"\n🎬 XONG — {OUT}")

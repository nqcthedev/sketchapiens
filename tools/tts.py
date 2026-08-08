#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SINH TIẾNG bằng ElevenLabs — MỘT bản cho MỌI video.

    python3 tools/tts.py <thư_mục_làm_việc>

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
"""TTS từng shot bằng ElevenLabs — chỉ dùng thư viện chuẩn (không cần requests).

Đọc TTS_input_per_shot.txt (mỗi dòng = 1 shot = 1 ảnh) -> audio/001.mp3 ...
Chạy lại được: file nào có rồi thì bỏ qua.

Key lấy từ biến môi trường ELEVENLABS_API_KEY. KHÔNG ghi key vào file này.
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

VOICE_ID = "nzFihrBIvB34imQBuxub"      # Josh
MODEL_ID = "eleven_multilingual_v2"
IN_FILE = "TTS_input_per_shot.txt"
OUT_DIR = "audio"
STABILITY, SIMILARITY, STYLE = 0.45, 0.80, 0.20


API_KEY = os.environ.get("ELEVENLABS_API_KEY", "").strip()
if not API_KEY:
    print("⚠ Chưa có ELEVENLABS_API_KEY trong biến môi trường.")
    sys.exit(1)

os.makedirs(OUT_DIR, exist_ok=True)
lines = [l.strip() for l in open(IN_FILE, encoding="utf-8").read().splitlines()
         if l.strip()]
print(f"Tổng {len(lines)} shot -> ./{OUT_DIR}/")

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
loi = []

for i, text in enumerate(lines, 1):
    out = os.path.join(OUT_DIR, f"{i:03d}.mp3")
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        continue

    body = json.dumps({
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": {"stability": STABILITY,
                           "similarity_boost": SIMILARITY,
                           "style": STYLE},
    }).encode("utf-8")

    for lan in range(4):
        req = urllib.request.Request(
            url, data=body,
            headers={"xi-api-key": API_KEY, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            if len(data) < 500:
                raise ValueError(f"file quá nhỏ ({len(data)} byte)")
            with open(out, "wb") as f:
                f.write(data)
            break
        except Exception as e:
            if lan == 3:
                loi.append((i, str(e)[:120]))
                print(f"  ✗ {i:03d} lỗi: {str(e)[:120]}")
            else:
                time.sleep(2 * (lan + 1))

    if i % 25 == 0:
        print(f"  ... {i}/{len(lines)}")

xong = len([f for f in os.listdir(OUT_DIR) if f.endswith('.mp3')])
print(f"\nXong: {xong}/{len(lines)} file.")
if loi:
    print(f"⛔ {len(loi)} shot lỗi: {[n for n, _ in loi]}")
    sys.exit(1)
print("✅ Đủ tiếng cho mọi shot.")

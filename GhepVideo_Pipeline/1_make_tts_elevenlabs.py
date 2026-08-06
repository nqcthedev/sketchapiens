#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BƯỚC 1 — Tạo tiếng TTS theo TỪNG SHOT (mỗi ảnh 1 file tiếng).
Đọc TTS_input_per_shot.txt (754 dòng, mỗi dòng = 1 ảnh) -> xuất audio/001.mp3 ... 754.mp3
Chạy lại được nhiều lần: file nào có rồi thì bỏ qua (resume), nên lỡ dừng giữa chừng cứ chạy tiếp.

CÁCH DÙNG:
  1) pip install requests
  2) Điền API_KEY + VOICE_ID bên dưới (hoặc đặt biến môi trường ELEVENLABS_API_KEY)
  3) python3 1_make_tts_elevenlabs.py
"""
import os, sys, time, requests

# ====== CẤU HÌNH (điền vào) ======
API_KEY  = os.environ.get("ELEVENLABS_API_KEY", "DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY")
VOICE_ID = "nzFihrBIvB34imQBuxub"         # Josh - Teacher for Kids (giọng bạn chọn)
MODEL_ID = "eleven_multilingual_v2"       # chất lượng cao; muốn rẻ+nhanh đổi "eleven_turbo_v2_5"
IN_FILE  = "TTS_input_per_shot.txt"
OUT_DIR  = "audio"
STABILITY, SIMILARITY, STYLE = 0.45, 0.80, 0.20  # Josh: ổn định + có hồn (deadpan-có-năng-lượng)
LIMIT    = 10                             # >0 = chỉ tạo N file đầu để TEST. Chạy full thì đổi LIMIT = 0
# =================================

def main():
    if "DÁN_" in API_KEY or "DÁN_" in VOICE_ID:
        print("⚠ Chưa điền API_KEY hoặc VOICE_ID. Mở file sửa 2 dòng đó trước.")
        sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    lines = [l.strip() for l in open(IN_FILE, encoding="utf-8").read().splitlines() if l.strip()]
    if LIMIT: lines = lines[:LIMIT]; print(f"** CHẾ ĐỘ TEST: chỉ tạo {LIMIT} file đầu (đổi LIMIT=0 để chạy full) **")
    print(f"Tổng {len(lines)} shot -> tạo {len(lines)} file tiếng vào ./{OUT_DIR}/")
    for i, text in enumerate(lines, 1):
        out = os.path.join(OUT_DIR, f"{i:03d}.mp3")
        if os.path.exists(out):
            continue
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
        payload = {"text": text, "model_id": MODEL_ID,
                   "voice_settings": {"stability": STABILITY, "similarity_boost": SIMILARITY, "style": STYLE}}
        headers = {"xi-api-key": API_KEY, "Content-Type": "application/json"}
        for attempt in range(4):
            try:
                r = requests.post(url, json=payload, headers=headers, timeout=60)
                if r.status_code == 200:
                    open(out, "wb").write(r.content)
                    print(f"  [{i:03d}/{len(lines)}] ok")
                    break
                elif r.status_code == 429:           # rate limit -> đợi
                    print(f"  [{i:03d}] rate-limit, đợi 10s..."); time.sleep(10)
                else:
                    print(f"  [{i:03d}] lỗi {r.status_code}: {r.text[:120]}"); time.sleep(3)
            except Exception as e:
                print(f"  [{i:03d}] exception {e}, thử lại..."); time.sleep(4)
        time.sleep(0.25)   # nhẹ tay với API
    print("XONG. Kiểm tra folder audio/ đủ 001..%03d.mp3 chưa." % len(lines))

if __name__ == "__main__":
    main()

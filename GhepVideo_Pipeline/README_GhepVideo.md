# 🎬 Ghép ảnh khớp audio TỰ ĐỘNG (không kéo tay) — Video #1

> **Nguyên lý:** mỗi ảnh = 1 shot = 1 file tiếng. Ảnh hiển thị **đúng bằng độ dài tiếng** của shot đó → khớp 100%, không cần kéo trên timeline.

---

## Cần có
- **ffmpeg** (Mac: mở Terminal gõ `brew install ffmpeg`).
- **Python 3** + `pip install requests` (chỉ cho bước tạo tiếng).
- 3 file trong folder này: `TTS_input_per_shot.txt`, `1_make_tts_elevenlabs.py`, `2_assemble_video.py`.

## Cấu trúc thư mục
```
GhepVideo_Pipeline/
├── TTS_input_per_shot.txt   (754 dòng = 754 shot)
├── 1_make_tts_elevenlabs.py
├── 2_assemble_video.py
├── images/   ← bỏ 754 ẢNH vào đây (001…754, đúng thứ tự)
└── audio/    ← 754 file TIẾNG vào đây (001…754)
```

---

## BƯỚC 1 — Tạo tiếng theo từng shot
**Cách 1 (tự động, khuyên dùng):** mở `1_make_tts_elevenlabs.py`, điền `API_KEY` + `VOICE_ID` (ElevenLabs) → chạy:
```
python3 1_make_tts_elevenlabs.py
```
→ tự sinh `audio/001.mp3 … 754.mp3`. (Dừng giữa chừng chạy lại sẽ làm tiếp file còn thiếu.)

**Cách 2 (TTS kiểu khác):** miễn sao cuối cùng có **754 file tiếng** trong `audio/`, đặt tên **001, 002, …** đúng thứ tự shot.

## BƯỚC 2 — Lấy ảnh
Tải 754 ảnh từ tool về folder `images/`. Quan trọng: **ảnh phải đúng thứ tự 1→754** (tool xuất theo thứ tự prompt, tên có số tăng dần là được — script tự sắp theo số trong tên).

## BƯỚC 3 — Ghép tự động
```
python3 2_assemble_video.py
```
→ ra **`final_video.mp4`** — ảnh khớp tiếng 100%, 2K 16:9. Xong.

## BƯỚC 4 — (tùy chọn) Hậu kỳ nhẹ
Mở `final_video.mp4` trong CapCut chỉ để **thêm nhạc nền nhỏ / logo / chỉnh âm lượng**. **Không cần kéo ảnh** nữa.

---

## 🅱️ CÁCH 2 — Đã có sẵn 1 FILE AUDIO đầy đủ (dùng `tool_align_full_audio.py`)
Dùng khi bạn **đã thu/đọc nguyên bài thành 1 file** (không cắt theo shot). Tool tự dò mỗi câu nằm ở giây nào rồi kéo ảnh khớp.
```
pip install faster-whisper          # cài 1 lần (cần ffmpeg)
# đặt: full_audio.mp3  +  images/(001..754)  +  TTS_input_per_shot.txt
python3 tool_align_full_audio.py    # -> final_video.mp4 (dùng đúng audio gốc của bạn)
```
- AI (Whisper) chỉ làm 1 việc: tìm mốc giây từng câu. Việc kéo ảnh vẫn là code tất định → khớp tốt.
- Từ nào Whisper nghe sót sẽ tự nội suy, không lệch.
- Đây là tool đúng với tình huống "tôi đã có full audio + ảnh, chỉ cần kéo cho khớp".

---

## Lưu ý & mẹo
- **Số ảnh = số tiếng = 754**, tên có số khớp nhau. Lệch số → script báo và chỉ ghép số cặp nhỏ hơn.
- **Chạy thử trước:** để 10 ảnh + 10 tiếng đầu vào, chạy bước 3 xem ổn rồi mới làm full.
- Đổi 2K→4K: mở `2_assemble_video.py` sửa `W,H = 3840,2160` (không cần thiết, 2K là đủ).
- Khoảng lặng giữa các cảnh: sửa `PAD_SIL` (mặc định 0.15s).
- Hard-cut tĩnh giống đối thủ (không hiệu ứng) — đúng style kênh.
```
```

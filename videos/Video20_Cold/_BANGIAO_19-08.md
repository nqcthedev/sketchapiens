# BÀN GIAO — V20 · cuối ngày 19/08/2026

> ⚠️ **Phiên hôm nay chạy ở `~/Desktop` nên KHÔNG nạp `CLAUDE.md`, `00_LUAT_HIEN_HANH.md`
> và 12 skill của dự án.** Chủ phát hiện lúc cuối buổi. Phiên sau phải `cd` vào dự án.

## Kịch bản — ĐÃ XONG

`Script_V20_narration.txt` · **3.562 từ · 296 dòng · ~19:47**
Title MỚI: **What Kept Ancient Humans Alive Through Freezing Nights?**

Làm trong ngày: đọc trọn bằng mắt sửa 6 lỗi · thêm 8 nước đi từ bảng mổ · đổi mở bài ·
đổi title · vá 6 phút câm · thêm cú lật địa vị · thêm 6 mỏ neo đời hiện đại.
Bảng 24 chiều: `MO_KICH_BAN_DEM_LANH.html` → https://claude.ai/code/artifact/978dbd34-6770-4ee9-98ee-f7c9cd59bee6

## 🔴 HAI CỔNG ĐANG BÁO XANH GIẢ

`preflight.py` cổng **P2 (tiếng)** và **P3 (ghép)** báo ✅ vì **file tồn tại**, không vì
nó khớp kịch bản. Thực tế:

- `audio/` **282 mp3** + `V20_Cold.mp4` (15/08) → dựng cho **KỊCH BẢN ĐẦU TIÊN** (2.132 từ)
- `SHOTLINES_FULL.txt` mở đầu *"Sixteen hours."* — câu đó **không còn trong kịch bản**
- `shot_data.py` chỉ có **52/437** tuple, và **cả 52 đều lệch vị trí** *(51/52 còn cứu được
  bằng cách khớp theo CHỮ, xem `_cu_shot_data_52.py`)*

→ **Toàn bộ ảnh, tiếng, video ghép đều phải làm lại từ đầu.**

## Việc kế, đúng thứ tự

1. `cd` vào dự án · chạy `python3 tools/preflight.py videos/Video20_Cold`
2. Viết nốt `shot_data.py` — còn **385/437** tuple *(khớp 51 tuple cũ theo CHỮ trước)*
3. `python3 tools/build_prompts.py videos/Video20_Cold` → gen ảnh **1 lượt vào thư mục RỖNG**
4. TTS + ghép
5. Thumbnail bản B → Test & Compare

## Còn 8 cổng chưa có dấu vết

`0` cầu · `2` cú bẻ lái ghi trong CHOT · `5` viết kết trước · `10` người nghe ngoài ·
`T` *(đã ghi `_nhap/TITLE_doi_chieu_2026-08-19.md` nhưng preflight tìm ở HE_THONG PHẦN C)* ·
`P1` ảnh · `P4` thumbnail · `P6` mid-roll

## Đang chạy nền

`_nghe_thu_tiengviet/_tts_moi.py` — bản dịch tiếng Việt của kịch bản MỚI (296 câu).
⚠️ Giọng `vi-VN` bị Microsoft **chặn tần suất**; script đã có timeout 20s + hạ nhiệt 25s.
Xong thì ghép `_mp3_moi/*.mp3` → `V20_MOI_tiengviet.mp3`.

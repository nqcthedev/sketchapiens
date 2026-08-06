---
paths: ["videos/**/06-production/**", "Video*/PROMPTS_*.txt", "Video*/SHOTLINES_*.txt", "Video*/*.py", "pipeline/**", "tools/**"]
---
# LUẬT — FILE SẢN XUẤT

**Ba thứ KHÔNG chứng minh được gì:** chạy không lỗi · đủ số file · đúng độ dài.
Phải đối chiếu **nội dung** ở nhiều mốc: nghe tiếng và xem ảnh có khớp không.

**Gen ảnh:** luôn gen vào thư mục **rỗng**, **một lượt**, và **đếm file == số prompt** trước khi ghép. Tool đặt tên theo bộ đếm nội bộ, không theo số prompt — chạy hai đợt là lệch.

**Ghép video: dùng app, không tự viết script sắp xếp.** Script tự viết đã làm hỏng tiếng của một video.

⛔ **File sinh tự động cỡ lớn không được đọc vào ngữ cảnh:** `PROMPTS_FULL.txt` · `PROMPTS_CLEAN.txt` · `*_alignment.json` · `*-timestamps.json`. Cần số liệu thì tính bằng script.

**Khoá API đọc từ biến môi trường.** Không bao giờ ghi khoá vào file nguồn.

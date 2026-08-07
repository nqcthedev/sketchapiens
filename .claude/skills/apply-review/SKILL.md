---
name: apply-review
description: Editor duy nhất. Nhận bảng phân loại đã được chủ duyệt và tạo version kịch bản MỚI. Không tự quyết mục nào được áp. Dùng sau /audit-script và sau khi chủ đã phân loại.
---

# /apply-review — editor duy nhất

## Điều kiện vào — thiếu là dừng
1. Có `videos/<ID>/04-review/RNNN-audit.md`
2. Bảng phân loại **đã được chủ điền**: mỗi mục có `ÁP NGAY` / `ÁP CÓ SỬA` / `BỎ`
3. Mục `BỎ` có ghi lý do

Chưa đủ → **dừng và hỏi**. Không tự phân loại thay chủ.

## Luật
- **Không ghi đè.** Tạo `03-script/versions/vNNN.md` kế tiếp, rồi trỏ `refs/current.yaml` sang nó.
- Chỉ áp mục được đánh dấu. Không "tiện tay sửa thêm".
- **`ÁP CÓ SỬA`** nghĩa là đúng vấn đề, sai cách chữa → tự nghĩ cách chữa, ghi rõ đã chữa khác thế nào.
- ⛔ **Lỗi ẩn dụ thì CẮT CẢ CÂU, đừng thay chữ trong câu.** Vá tại chỗ để lại sẹo: khung câu cũ còn nguyên, đại từ mất chỗ bám. Đã đo được ba lần.
- ⛔ **Câu nào thêm vào phải chạy lại cổng bằng chứng** (`/verify-claims`), kể cả khi thêm chỉ để đủ độ dài.
- Không đụng `refs/approved.yaml` và `refs/published.yaml` — hook chặn nếu thiếu `set_by: owner`.

## Sau khi tạo version mới
1. Chạy `qa_kichban.py` — 4 ràng buộc cứng phải sạch.
2. Chạy `/verify-claims` nếu có câu mới mang số liệu.
3. Ghi vào `04-review/RNNN-applied.md`: **áp gì · bỏ gì · vì sao · sinh ra thay đổi nào**.
4. Cập nhật `video.yaml`: `status: revised`, thêm version vào `script_versions`.
5. **Không** đặt `refs/approved.yaml`. Chỉ chủ duyệt mới được.

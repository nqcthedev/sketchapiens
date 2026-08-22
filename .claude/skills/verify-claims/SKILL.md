---
name: verify-claims
description: Đối chiếu từng mệnh đề trong kịch bản với claim ledger và nguồn gốc, phân loại DIRECT/INFERENCE/SPECULATION/STORY_DEVICE. Dùng trước khi khoá bằng chứng, và bắt buộc lại mỗi khi thêm câu mới vào kịch bản.
---

# /verify-claims — khoá bằng chứng

## Khi nào bắt buộc chạy
- Trước khi milestone/gate **evidence locked — bằng chứng đã khoá** được coi là hoàn tất. Đây là **milestone/artifact gate, không phải `video.yaml` state**.
- **Mỗi lần thêm câu mới vào kịch bản, kể cả sau khi đã khoá** — lỗi bịa trình tự đã lọt đúng vì khối được thêm sau khi cổng đóng
- Trước khi chủ duyệt

## Chạy
Gọi subagent `evidence-prosecutor` với: lời đọc + claim ledger.

## Bốn thứ phải bắt
1. **Bắc cầu giữa hai bảng thống kê rời** — nặng nhất
2. **Suy diễn của tác giả nói thành số đo**
3. **Dữ liệu hiện đại suy rộng về tiền sử** — phải có câu tự thừa nhận giới hạn
4. **Số lấy từ snippet** — mở toàn văn hoặc ghi `UNVERIFIED`

## Kết quả
Ghi vào `videos/<ID>/02-research/claim-ledger.md`, mỗi mệnh đề một dòng, kèm mức vượt `0-3`.

**KHOÁ ĐƯỢC** khi không còn mệnh đề mức ≥2.
Còn mức ≥2 → liệt kê, **không tự sửa kịch bản**, trả về cho editor.

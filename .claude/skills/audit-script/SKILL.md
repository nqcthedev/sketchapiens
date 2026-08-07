---
name: audit-script
description: Chạy năm giám khảo độc lập trên một bản nháp kịch bản rồi gộp thành một bản chấm duy nhất cho chủ phân loại. Read-only, không sửa kịch bản. Dùng sau khi có bản nháp và trước khi sửa.
---

# /audit-script — ba giám khảo, một bản chấm

## Luật cứng
- **Read-only.** Không agent nào được sửa kịch bản.
- Mỗi giám khảo chạy **ngữ cảnh riêng**, không thấy nhận xét của người khác.
- Ba giám khảo đầu **không** được đọc research/rubric. Tai sạch là giá trị của họ.
- Kết quả là **đề nghị**, không phải quyết định. Chủ phân loại từng mục.

## Đầu vào
Đường dẫn bản nháp · title · mô tả thumbnail + chữ. Thiếu thumbnail thì nói rõ phép thử chỉ chạy một nửa.

## Chạy — gọi 3 subagent song song

| Agent | Nhận | Trả |
|---|---|---|
| `viewer-retention-judge` | title · thumbnail · lời đọc | điểm bỏ xem · câu phải nghe lại · 3 lời hứa · một-hay-nhiều-câu-hỏi · bản đồ giữ chân · điểm thoát |
| `evidence-prosecutor` | lời đọc · claim ledger | bảng DIRECT/INFERENCE/SPECULATION/STORY_DEVICE · mức vượt 0-3 |
| `anti-ai-narration-critic` | lời đọc | 10 câu nặng mùi · ẩn dụ chồng tầng · sẹo vá |

> ⚠️ **Ba agent này KHÔNG lạnh.** Tài liệu chính thức: subagent nạp đủ `CLAUDE.md` và project
> rules; chỉ Explore và Plan bỏ qua, và **không chỉnh được**. Giá trị của chúng là **ngữ cảnh
> riêng** — không thấy lý lẽ người viết đã tự thuyết phục mình — chứ không phải "không biết kênh".
>
> 🔴 **Lớp lạnh thật là cổng 10: review ngoài bằng ChatGPT, chat mới.** Không bỏ được.

Ngoài ra chạy máy: `python3 ~/.claude/skills/sketchapiens-bien-tap/qa_kichban.py <file>` — 4 ràng buộc cứng.

## Gộp — ghi vào `videos/<ID>/04-review/RNNN-audit.md`

Dùng `templates/review-consolidated.md`. Bắt buộc có:

1. **Kết quả máy** — 4 ràng buộc cứng đạt/trượt.
2. **Lỗi bị bắt ĐỘC LẬP ở nhiều giám khảo** — xếp lên đầu. *Đếm số lần bị bắt độc lập, đừng đếm số câu bị gạch.*
3. **Từng giám khảo một mục**, giữ nguyên văn, không làm nhẹ.
4. **Bảng phân loại để trống** cho chủ điền: `ÁP NGAY / ÁP CÓ SỬA / BỎ + lý do`.

## Sau đó DỪNG
Không sửa gì. Chủ phân loại xong thì gọi `/apply-review`.

---
name: audit-script
description: Chạy ba giám khảo độc lập trên một bản nháp kịch bản rồi gộp thành một bản chấm duy nhất cho chủ phân loại. Read-only, không sửa kịch bản. Dùng sau khi có bản nháp và trước khi sửa.
---

# /audit-script — ba giám khảo, một bản chấm

## Luật cứng
- **Read-only.** Không agent nào được sửa kịch bản.
- Mỗi giám khảo chạy **ngữ cảnh riêng**, không thấy nhận xét của người khác.
- Kết quả là **đề nghị**, không phải quyết định. Chủ phân loại từng mục.
- **Không preload một bộ context chung cho cả ba agent.** Mỗi agent chỉ nhận thứ role của nó cần.

## Đầu vào chung
Đường dẫn bản nháp · title · mô tả thumbnail + chữ. Thiếu thumbnail thì nói rõ phép thử retention chỉ chạy được một phần.

## Consumer context — Ngữ cảnh từng giám khảo

| Agent | ĐƯỢC nhận | KHÔNG được nhận mặc định |
|---|---|---|
| `viewer-retention-judge` | title · thumbnail · lời đọc | research · claim ledger · writer rationale · rubric điểm số |
| `evidence-prosecutor` | lời đọc · claim ledger · nguồn gốc cần kiểm | writer rationale · retention theory · prose rubric |
| `anti-ai-narration-critic` | lời đọc | research · claim ledger · writer rationale · Story Engine theory |

> **Tai sạch không có nghĩa ba agent phải mù cùng một thứ.**
> Retention judge cần surface-only để thấy vết nối như viewer.
> Evidence Prosecutor **bắt buộc** phải thấy claim ledger/nguồn thì mới có thể phán DIRECT / INFERENCE / SPECULATION / STORY_DEVICE.
> Anti-AI critic chỉ cần prose surface.

## Chạy — gọi 3 subagent song song

| Agent | Trả |
|---|---|
| `viewer-retention-judge` | điểm bỏ xem · câu phải nghe lại · 3 lời hứa · một-hay-nhiều-câu-hỏi · bản đồ giữ chân · điểm thoát |
| `evidence-prosecutor` | bảng DIRECT/INFERENCE/SPECULATION/STORY_DEVICE · mức vượt 0-3 |
| `anti-ai-narration-critic` | câu nặng mùi · ẩn dụ chồng tầng · sẹo vá |

### Story Engine boundary — Ranh giới Story Engine

`/audit-script` **không tự load Story Engine cho cả ba agent**.
`viewer-retention-judge` đã preload `sketchapiens-story-engine` trong frontmatter của chính agent và phải tuân theo context budget của nó.
Evidence Prosecutor và Anti-AI critic không được dùng Story Engine để mở rộng role.

> ⚠️ **Ba agent này KHÔNG lạnh.** Subagent nạp project context theo runtime Claude Code.
> Giá trị của chúng là **ngữ cảnh riêng** — không thấy reasoning của agent khác / conversation chính — chứ không phải "không biết kênh".
>
> 🔴 **Lớp lạnh thật là cổng review ngoài bằng ChatGPT, chat mới.** Không bỏ được.

Ngoài ra chạy máy:

```bash
python3 .claude/skills/sketchapiens-bien-tap/qa_kichban.py <file>
```

Kiểm **BA** ràng buộc cứng:
`!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng.
⛔ `I ≈ 0` đã gỡ 07/08.

## Gộp — ghi vào `videos/<ID>/04-review/RNNN-audit.md`

Dùng `templates/review-consolidated.md`. Bắt buộc có:

1. **Kết quả máy** — ba ràng buộc cứng đạt/trượt. Số khác là triệu chứng, không phải ngưỡng.
2. **Lỗi bị bắt ĐỘC LẬP ở nhiều giám khảo** — xếp lên đầu; chỉ gộp khi thực sự cùng lỗi, không ép taxonomy khác role thành một lỗi.
3. **Từng giám khảo một mục**, giữ nguyên role và verdict; không để retention judge "thắng" Evidence Prosecutor hay ngược lại.
4. **Bảng phân loại để trống** cho chủ điền: `ÁP NGAY / ÁP CÓ SỬA / BỎ + lý do`.

## Sau đó DỪNG
Không sửa gì. Chủ phân loại xong thì gọi `/apply-review`.

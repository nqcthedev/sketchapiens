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
| `evidence-prosecutor` | exact lời đọc/version · canonical claim ledger · nguồn liên quan | writer rationale · retention theory · prose rubric · competitor corpus |
| `anti-ai-narration-critic` | lời đọc | research · claim ledger · writer rationale · Story Engine theory |

> **Tai sạch không có nghĩa ba agent phải mù cùng một thứ.**
> Retention judge cần surface-only để thấy vết nối như viewer.
> Evidence Prosecutor bắt buộc phải thấy exact script + ledger/source cần thiết để phán qua `sketchapiens-evidence-engine`.
> Anti-AI critic chỉ cần prose surface.

## Chạy — gọi 3 subagent song song

| Agent | Trả |
|---|---|
| `viewer-retention-judge` | điểm bỏ xem · câu phải nghe lại · 3 lời hứa · một-hay-nhiều-câu-hỏi · bản đồ giữ chân · điểm thoát |
| `evidence-prosecutor` | claim verdicts · bridge/synthesis verdicts khi relevant · provenance/transfer debt · lockability |
| `anti-ai-narration-critic` | câu nặng mùi · ẩn dụ chồng tầng · sẹo vá |

`overreach 0–3` chỉ là legacy compatibility history, không còn là output contract canonical của Evidence review mới.

### Story / Evidence boundary

`/audit-script` **không tự load Story Engine cho cả ba agent**.
`viewer-retention-judge` preload Story Engine theo frontmatter của chính agent.
Evidence Prosecutor preload **Evidence Engine**, không dùng Story Engine để tự redesign cấu trúc.
Anti-AI critic không được mở rộng role sang Story/Evidence.

Nếu Story review flag `Narrative Overreach`, đó là symptom structural. Evidence Prosecutor mới là bên mở nguồn và issue factual/bridge verdict.
Không để retention verdict thắng Evidence verdict hoặc ngược lại.

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
3. **Từng giám khảo một mục**, giữ nguyên role và verdict. Với Evidence giữ claim/bridge verdict + severity + debt; không nén về một score duy nhất.
4. **Bảng phân loại để trống** cho chủ điền: `ÁP NGAY / ÁP CÓ SỬA / BỎ + lý do`.

## Sau đó DỪNG
Không sửa gì. Chủ phân loại xong thì gọi `/apply-review`.

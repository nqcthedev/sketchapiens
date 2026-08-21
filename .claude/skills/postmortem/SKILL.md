---
name: postmortem
description: Đóng vòng phản hồi sau khi một video đã có số liệu thật — map điểm tụt giữ chân về câu chữ, tạo/cập nhật candidate nếu phát hiện mechanism mới, và chỉ đề xuất promotion khi đã qua candidate lifecycle. Dùng sau khi video đã publish và đã có analytics.
---

# /postmortem — đóng vòng phản hồi

Đây là **mắt xích đang đứt** của cả hệ thống: project sinh ra tri thức về đối thủ liên tục, nhưng gần như không sinh ra tri thức về chính mình.

## Điều kiện vào
- `videos/<ID>/07-publish/` có publish record
- `videos/<ID>/08-analytics/` có ít nhất một lần đo

Thiếu → dừng. **Không đoán, không ước lượng số liệu thiếu.**

## Chạy
1. Đọc số liệu, ghi kèm **cỡ mẫu** từng chỉ số.
2. Map từng điểm tụt: `timestamp → đoạn → câu → shot`. Không map được thì ghi là không map được.
3. So với video trước **cùng lane**, không so với trung bình kênh.
4. Điền `templates/postmortem.md`.
5. Nếu thấy một pattern/mechanism mới, **không nhảy thẳng sang luật**. Đọc:
   - `.claude/skills/sketchapiens-story-engine/references/candidate-lifecycle.md` — **Vòng đời cơ chế ứng viên**;
   - rồi mới đọc `mechanism-lab.md` nếu cần tạo/cập nhật candidate.

## Luật về số nhỏ
Chỉ số đo trên **dưới 100 quan sát** phải ghi khoảng tin cậy và **không được dùng làm chuẩn**.
Ví dụ đã có thật: giữ chân 55,6% đo trên **12 người** — khoảng tin cậy [27,5%; 83,7%], vô dụng để kết luận.

## Discovery routing — Định tuyến phát hiện mới

Một video có thể sinh ra:

### A. Observation — Quan sát

Ví dụ: một điểm tụt trùng với đoạn narrator đổi topic không có lý do.

→ Ghi observation trong postmortem.
→ **Chưa cần đặt tên mechanism mới.**

### B. Candidate mechanism — Cơ chế ứng viên

Chỉ tạo khi observation đủ rõ để phát biểu thành giả thuyết có thể bị bác.

→ Ghi/cập nhật trong `mechanism-lab.md` theo `candidate-lifecycle.md`.
→ Candidate **không được dùng mặc định khi viết/review video kế tiếp**.

### C. Promotion proposal — Đề xuất nâng cấp

Chỉ khi một **candidate đã tồn tại** và đã qua cross-check/counterexample/test đủ theo lifecycle.

Destination phải nói rõ:
- `CANONICAL DIAGNOSTIC FRAMEWORK` — khung chẩn đoán chuẩn;
- `CANONICAL MEASURED PATTERN` — pattern đã đo chuẩn;
- hoặc `CANONICAL RULE / GUARDRAIL` — luật/hàng rào chuẩn.

Không phải mọi discovery tốt đều phải trở thành rule.

## Nếu đề xuất RULE / GUARDRAIL — cần đủ NĂM điều kiện
1. bằng chứng từ video/corpus cụ thể
2. độ tin cậy *(cỡ mẫu + khoảng)*
3. phạm vi áp dụng
4. người duyệt
5. luật cũ bị thay thế, nếu có

Thiếu một là **không** được ghi vào `governance/RULE_REGISTRY.yaml`.
Đề xuất ghi vào `governance/DECISIONS_REQUIRED.md` ở trạng thái `NEEDS_HUMAN_DECISION`.

## Cấm
- Không tự nâng một observation thành candidate nếu chưa có giả thuyết có thể bị bác.
- Không tự nâng candidate thành canonical framework/pattern/rule.
- Không dùng một video đơn lẻ làm đường tắt vào `RULE_REGISTRY.yaml`.
- Không sửa `governance/RULE_REGISTRY.yaml` khi chưa có owner approval.
- Không cho candidate vừa phát hiện trở thành requirement của video kế tiếp nếu owner chưa mở **controlled experiment — thử nghiệm có kiểm soát**.

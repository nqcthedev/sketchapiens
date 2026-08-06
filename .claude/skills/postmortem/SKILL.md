---
name: postmortem
description: Đóng vòng phản hồi sau khi một video đã có số liệu thật — map điểm tụt giữ chân về câu chữ, và đề xuất thay đổi luật kèm đủ năm điều kiện. Dùng sau khi video đã publish và đã có analytics.
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

## Luật về số nhỏ
Chỉ số đo trên **dưới 100 quan sát** phải ghi khoảng tin cậy và **không được dùng làm chuẩn**.
Ví dụ đã có thật: giữ chân 55,6% đo trên **12 người** — khoảng tin cậy [27,5%; 83,7%], vô dụng để kết luận.

## Đề xuất luật mới — cần đủ NĂM điều kiện
1. bằng chứng từ video cụ thể
2. độ tin cậy *(cỡ mẫu + khoảng)*
3. phạm vi áp dụng
4. người duyệt
5. luật cũ bị thay thế, nếu có

Thiếu một là **không** được ghi vào `governance/RULE_REGISTRY.yaml`.
Đề xuất ghi vào `governance/DECISIONS_REQUIRED.md` ở trạng thái `NEEDS_HUMAN_DECISION`.

## Cấm
- Không tự nâng một quan sát thành luật kênh.
- Không sửa `governance/RULE_REGISTRY.yaml` khi chưa có người duyệt.

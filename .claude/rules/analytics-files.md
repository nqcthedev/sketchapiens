---
paths: ["analytics/**", "videos/**/07-publish/**", "videos/**/08-analytics/**", "templates/analytics-video.md", "templates/postmortem.md"]
---
# LUẬT — FILE SỐ LIỆU

⛔ **Không suy ra trạng thái `published`.** Chưa có publish record thì là `not_published`. Không đoán ngày đăng, không đoán URL.

**Không ước lượng số liệu bị thiếu.** Thiếu thì ghi `null` kèm lý do.

**Luôn kèm cỡ mẫu.** CTR 3,5% trên 13 lượt bấm và CTR 3,5% trên 13.000 lượt bấm là hai thứ khác nhau. Số đo trên <100 quan sát phải ghi rõ khoảng tin cậy và **không được dùng làm chuẩn**.

**Không nâng một quan sát thành luật kênh** nếu chưa đủ năm thứ: bằng chứng từ video · độ tin cậy · phạm vi áp dụng · người duyệt · luật cũ bị thay thế.

Mỗi điểm tụt giữ chân phải map được về **timestamp → đoạn → câu → shot**. Không map được thì ghi là chưa map được.

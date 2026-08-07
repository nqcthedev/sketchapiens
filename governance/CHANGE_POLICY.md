# CHÍNH SÁCH THAY ĐỔI LUẬT

## Nguyên tắc gốc
**Không nâng một quan sát thành luật kênh.** Dự án đã mất nhiều tháng vì việc này: bốn con số sai sống tới bốn tháng, và ba luật thumbnail bị bác sau khi đã dùng để ra quyết định.

## Năm điều kiện — thiếu một là KHÔNG được ghi vào `RULE_REGISTRY.yaml`

| # | Điều kiện | Nghĩa |
|---|---|---|
| 1 | **Bằng chứng** | Video nào, số nào, đo bằng gì |
| 2 | **Độ tin cậy** | Cỡ mẫu + khoảng tin cậy. <100 quan sát → không đủ |
| 3 | **Phạm vi** | Áp cho mọi video, một lane, hay một video? |
| 4 | **Người duyệt** | Phải là **người**. Agent không tự duyệt |
| 5 | **Luật cũ bị thay** | Nếu có, ghi rõ và chuyển sang `RETIRED_RULES.md` |

## Khai tử một luật — làm CẢ HAI việc
1. Ghi vào `RETIRED_RULES.md` kèm lý do và bằng chứng bác.
2. **Dán biển ⛔ vào dòng đầu chính file đó.**

Làm một nửa thì lần sau vẫn có người mở nhầm. **Hiện có 5 trường hợp đang làm một nửa** — xem `governance/PROJECT_FULL_AUDIT_EXPORT.md` §18.2.

## Bốn bài học đã trả giá — coi như luật

1. **Đừng thêm luật khi model đang làm đúng.** Hai lỗi nặng nhất của một vòng thumbnail đều là luật tự thêm vào.
2. **Vá tại chỗ để lại sẹo.** Ba câu tệ nhất của một vòng review đều là câu vá ở vòng trước. Lỗi ẩn dụ thì **cắt cả câu**.
3. **Con số đo được là triệu chứng, không phải đích.** Sửa câu cho số đẹp là lỗi.
4. **Hai điểm không đủ để chốt bất cứ thứ gì.** Đã dính ít nhất hai lần.

## Ai được đổi gì

| Thay đổi | Ai |
|---|---|
| Sửa `CLAUDE.md`, `.claude/rules/**` | **chỉ người**, agent đề xuất |
| Ghi luật mới vào `RULE_REGISTRY.yaml` | **chỉ người**, sau khi đủ 5 điều kiện |
| Khai tử luật | **chỉ người** |
| Đặt `approved` / `published` | **chỉ người** |
| Đề xuất thay đổi | agent — ghi vào `DECISIONS_REQUIRED.md` |

# SỔ MIGRATION

| Ngày | Việc | Phạm vi | Kết quả |
|---|---|---|---|
| 2026-08-06 | **Cài control plane v1** | `CLAUDE.md` · `.claude/**` · `governance/` · `schemas/` · `templates/` · `tools/` · `.gitignore` · git init | ✅ xong — xem `INSTALL_REPORT.md` |

## CHƯA làm — nằm ngoài phạm vi lần cài này

| Việc | Vì sao hoãn |
|---|---|
| Tạo `knowledge/**` và copy tài liệu canonical | migration nội dung, cần quyết D-01…D-04 trước |
| Tạo `videos/SKA-*/` và map V01–V19 | cần chủ quyết ID cho V01 và hai V17 *(D-10)* |
| Tạo `analytics/**` với số liệu thật | chưa có số liệu nào trong project |
| Tách corpus ra sibling ngoài repo | cần chủ quyết *(D-15)* |
| Gộp 5 pipeline thành một | cần chủ quyết *(D-16)* |
| Dọn 79 file ở gốc kho | bị cấm trong lần cài này |
| Giải 18+1 quyết định | thuộc thẩm quyền chủ dự án |

**Không file cũ nào bị xoá, đổi tên hay di chuyển trong lần cài này.**

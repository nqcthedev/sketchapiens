---
name: project-doctor
description: Kiểm tính toàn vẹn cấu trúc project — schema, lifecycle, version, trùng ID, artefact thiếu, rò rỉ secret, file cấm đọc. Read-only, không sửa gì. Dùng sau mọi thay đổi cấu trúc và trước mỗi lần commit.
---

# /project-doctor — khám cấu trúc

Chạy: `python3 tools/project_doctor.py`

## Kiểm những gì
1. **Control plane** — đủ `CLAUDE.md`, `.claude/{settings.json,agents,rules,skills,hooks}`, `governance/`, `schemas/`, `templates/`
2. **JSON/YAML hợp lệ** — mọi file trong `schemas/`, `.claude/settings.json`, mọi `video.yaml`
3. **Agent/skill/rule có frontmatter hợp lệ** — agent cần `name`+`description`, rule cần `paths`
4. **Lifecycle** — mỗi `video.yaml` có `status` nằm trong 16 trạng thái hợp lệ, và **artefact bắt buộc của trạng thái đó tồn tại**
5. **ID không trùng**, đúng khuôn `SKA-NNNN-slug`
6. **Version kịch bản** — `vNNN` liên tục, `approved.md`/`published.md` không bị sửa sau khi tạo
7. **Không suy ra published** — có `status: published` mà không có `07-publish/` là lỗi
8. **Secret** — quét khoá bị hard-code, **chỉ báo vị trí, không in giá trị**
9. **File cấm đọc** — cảnh báo nếu file cỡ lớn lọt vào phạm vi git

## Kết quả
`PASS` / `WARN` / `FAIL` từng mục. **Không tự sửa bất cứ gì** — chỉ báo cáo.

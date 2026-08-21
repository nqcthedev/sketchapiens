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
4. **Lifecycle — vòng đời video** — `video.yaml.status` phải thuộc enum canonical ở `schemas/video.schema.json`, và **artefact bắt buộc của trạng thái đó tồn tại**
5. **ID không trùng**, đúng khuôn `SKA-NNNN-slug`
6. **Version + refs — phiên bản + con trỏ** — `03-script/versions/vNNN.md` là **bất biến**; `03-script/refs/{current,approved,published}.yaml` là **con trỏ đổi được**. `approved.yaml` và `published.yaml` phải có `set_by: owner` khi được đặt.
7. **Không suy ra published** — có `status: published` mà không có `07-publish/` là lỗi
8. **Legacy migration exemption — miễn migration legacy** — chỉ đúng 6 folder lịch sử nằm trong `LEGACY_VIDEO_DIRS` của `tools/project_doctor.py` được WARN khi thiếu `video.yaml`; tên mới kiểu `Video21_*` **không** được miễn và phải FAIL nếu thiếu manifest.
9. **Secret** — quét khoá bị hard-code, **chỉ báo vị trí, không in giá trị**
10. **File cấm đọc** — cảnh báo nếu file cỡ lớn lọt vào phạm vi git

## Nguyên tắc guardrail

`legacy` là **explicit migration allowlist — danh sách migration cố định**, không phải naming convention.

Không được đổi logic thành `startswith("Video")`, regex rộng kiểu `Video\d+`, hoặc bất kỳ phép nhận diện nào khiến video mới có thể tự giả làm legacy.

Khi một legacy folder được migrate thật, bỏ chính path đó khỏi allowlist. Không thêm video mới vào allowlist để làm doctor xanh.

## Kết quả
`PASS` / `WARN` / `FAIL` từng mục. **Không tự sửa bất cứ gì** — chỉ báo cáo.

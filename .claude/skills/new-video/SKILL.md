---
name: new-video
description: Dựng khung thư mục và video.yaml cho một video mới theo lifecycle bất biến của Sketchapiens. Dùng khi bắt đầu một video mới, hoặc khi cần tạo khung cho một video cũ để migrate. Không sinh nội dung, không chọn đề tài.
---

# /new-video — dựng khung một video

## Việc này KHÔNG làm
Không chọn đề tài. Không viết kịch bản. Không đoán trạng thái. Không di chuyển file cũ.

## Đầu vào cần hỏi nếu chưa có
1. Slug ngắn bằng tiếng Anh, gạch nối *(vd `night-walk`)*
2. Số thứ tự video *(4 chữ số)*
3. Có phải khung cho video cũ không — nếu phải, đường dẫn thư mục cũ để **ghi lại nguồn**, không copy trong bước này

## ID bất biến
`SKA-NNNN-<slug>` — vd `SKA-0019-night-walk`. **Không đổi ID sau khi tạo.**

⚠️ Hai video cũ cùng mang số 17 (`videos/Video17_Rain`, `videos/Video17_Death`) và V01 không có thư mục. Khi cấp ID cho chúng, hỏi chủ trước — xem `governance/DECISIONS_REQUIRED.md`.

## Khung tạo ra
```
videos/SKA-NNNN-<slug>/
├── video.yaml            ← theo schemas/video.schema.json, trạng thái khởi tạo là "idea"
├── 01-brief/
├── 02-research/
│   └── claim-ledger.json ← canonical machine Evidence ledger
├── 03-script/
│   ├── versions/         ← vNNN.md — BẤT BIẾN
│   └── refs/             ← current/approved/published.yaml (con trỏ)
├── 04-review/            ← toàn bộ review/audit + phân loại + applied log
├── 05-packaging/         ← title, thumbnail concept, metadata
├── 06-production/        ← shotlines, prompt ảnh
│   └── runs/{image,tts,render}/<RUN-ID>/  ← mỗi lần chạy một thư mục, BẤT BIẾN
├── 07-publish/           ← publish record. Trống = not_published
└── 08-analytics/         ← số liệu + postmortem
```

`02-research/verification-runs/` chỉ cần tạo khi `/verify-claims` thực sự sinh run đầu tiên; không tạo thư mục rỗng chỉ để đủ cây.

## Sau khi tạo
1. Điền `video.yaml` từ `templates/video.yaml`, trạng thái `idea`.
2. Copy `templates/claim-ledger.json` vào `02-research/claim-ledger.json` và thay `video_id` bằng ID thật. Ở pre-draft giữ `script_ref: null`, `locked: false`, `lockability: NOT_LOCKABLE`.
3. Copy `templates/ref.yaml` vào `03-script/refs/` theo contract hiện hành.
4. Chạy validator Evidence:
   `python3 .claude/skills/sketchapiens-evidence-engine/scripts/validate_claim_ledger.py videos/<ID>/02-research/claim-ledger.json`
5. Chạy `/project-doctor` xác nhận khung hợp lệ.
6. **Không** chuyển trạng thái. Chuyển trạng thái phải dùng enum canonical trong `schemas/video.schema.json` và cần artefact tương ứng tồn tại.

## Khi có script version đầu tiên

Trước khi gọi evidence lock, `/verify-claims` phải bind ledger với exact immutable `03-script/versions/vNNN.md`. Không dùng `refs/current.yaml` làm bằng chứng duy nhất rằng text đã verify.

Legacy `MONEO_*` / `VERIFY_Anchors_*` không được tự copy/migrate vào ledger mới trong `/new-video`.

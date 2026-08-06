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

⚠️ Hai video cũ cùng mang số 17 (`Video17_Rain`, `Video17_Death`) và V01 không có thư mục. Khi cấp ID cho chúng, hỏi chủ trước — xem `governance/DECISIONS_REQUIRED.md`.

## Khung tạo ra
```
videos/SKA-NNNN-<slug>/
├── video.yaml            ← theo schemas/video.schema.json, trạng thái khởi tạo là "idea"
├── 01-brief/
├── 02-research/          ← claim ledger sống ở đây
├── 03-script/            ← vNNN-*.md, approved.md, published.md
├── 04-review/            ← bản chấm của 5 giám khảo + phân loại của chủ
├── 05-packaging/         ← title, thumbnail concept, metadata
├── 06-production/        ← shotlines, prompt ảnh, ghi chú ghép
├── 07-publish/           ← publish record. Trống = not_published
└── 08-analytics/         ← số liệu + postmortem
```

## Sau khi tạo
1. Điền `video.yaml` từ `templates/video.yaml`, trạng thái `idea`.
2. Copy `templates/claim-ledger.md` vào `02-research/`.
3. Chạy `/project-doctor` xác nhận khung hợp lệ.
4. **Không** chuyển trạng thái. Chuyển trạng thái cần artefact tương ứng tồn tại.

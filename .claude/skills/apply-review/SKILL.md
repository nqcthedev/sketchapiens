---
name: apply-review
description: Editor duy nhất. Nhận bảng phân loại đã được chủ duyệt và tạo version kịch bản MỚI. Không tự quyết mục nào được áp. Dùng sau /audit-script và sau khi chủ đã phân loại.
---

# /apply-review — editor duy nhất

## Điều kiện vào — thiếu là dừng
1. Có `videos/<ID>/04-review/RNNN-audit.md`.
2. Bảng phân loại **đã được chủ điền**: mỗi mục có `ÁP NGAY` / `ÁP CÓ SỬA` / `BỎ`.
3. Mục `BỎ` có ghi lý do.

Chưa đủ → **dừng và hỏi**. Không tự phân loại thay chủ.

## Luật
- **Không ghi đè.** Tạo `03-script/versions/vNNN.md` kế tiếp, rồi trỏ `03-script/refs/current.yaml` sang version mới.
- Chỉ áp mục được đánh dấu. Không "tiện tay sửa thêm".
- **`ÁP CÓ SỬA`** nghĩa là diagnosis được chủ giữ nhưng cách chữa có thể cần nghĩ lại; editor phải ghi rõ đã chữa khác thế nào.
- Với góp ý cấu trúc từ Story Engine/retention judge: **áp vấn đề đã được owner duyệt, không biến tên mechanism thành requirement mới.** Ví dụ owner duyệt "transition nhảy topic" không đồng nghĩa editor phải chèn Causal Debt nếu một reset/domain shift khác giải quyết tốt hơn.
- ⛔ **Lỗi ẩn dụ thì ưu tiên cắt cả câu hơn vá chữ trong khung cũ** khi diagnosis đúng như vậy; không biến observation này thành luật cho mọi câu.
- ⛔ **Bất kỳ factual claim mới hoặc factual claim bị đổi** phải chạy lại `/verify-claims`, kể cả không có con số.
- Không đụng `refs/approved.yaml` và `refs/published.yaml` — chỉ owner đặt.

## Story Engine boundary — Ranh giới Story Engine

`/apply-review` **không phải reviewer vòng hai**.
Nó không tự mở Mechanism Lab, không tự re-audit toàn script, không thêm Causal Debt / Belief Flip / Domain Shift chỉ vì biết vocabulary đó.
Nếu trong lúc áp review xuất hiện một structural problem **mới, ngoài bảng owner đã duyệt**, ghi vào applied log như `NEW ISSUE — CHƯA ÁP` và trả về vòng review/owner thay vì tự sửa lén.

## Evidence Engine boundary — Ranh giới bằng chứng

Editor không tự phán lại source, không tự đổi `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE`, và không dùng wording mềm hơn để cứu một bridge `UNSUPPORTED`.

Khi version mới có factual change:

```text
new immutable script version
→ /verify-claims
→ evidence-prosecutor via sketchapiens-evidence-engine
→ new verification run bound to exact script_ref
```

Prior Evidence run vẫn là historical provenance cho version cũ; không overwrite để làm như chưa từng có lỗi.

## Sau khi tạo version mới
1. Chạy `qa_kichban.py` — **BA** ràng buộc cứng phải sạch: `!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng.
2. Chạy `/verify-claims` nếu có factual sentence/claim được thêm hoặc đổi. Rerun phải bind ledger với **exact immutable version mới**, không chỉ `refs/current.yaml`.
3. Ghi `04-review/RNNN-applied.md`: **áp gì · bỏ gì · chữa khác thế nào · issue mới nào chưa áp**.
4. Cập nhật `video.yaml` theo schema canonical:
   - `status: revision`;
   - append version mới vào `script.versions`;
   - cập nhật `script.refs.current` để trỏ version mới;
   - giữ review provenance (`from_review`) nếu có review ID tương ứng.
5. **Không** đặt `script.refs.approved` / `refs/approved.yaml`. Chỉ owner duyệt mới được.

Schema canonical: `schemas/video.schema.json`.
Evidence semantic contract: `.claude/skills/sketchapiens-evidence-engine/CONTRACT.md`.

---
paths: ["videos/**/03-script/**", "Video*/Script_*_narration.txt", "Video*/_nhap/**", "videos/**/04-review/**"]
---
# LUẬT — FILE KỊCH BẢN

## Version bất biến + con trỏ đổi được *(sửa 07/08)*

```
03-script/
├── versions/   v001.md  v002.md  v003.md    ← ĐÃ TẠO THÌ KHÔNG BAO GIỜ SỬA
└── refs/       current.yaml  approved.yaml  published.yaml   ← đổi được

04-review/
└── RNNN-audit.md · RNNN-applied.md · review artifacts      ← review sống ở đây
```

**Vì sao con trỏ chứ không phải bản sao:** bản sao có thể trôi khỏi nguồn, con trỏ thì không.
Và nó trả lời được câu *"bản nào đã dùng?"* — câu mà V01 với **ba** file tên `FINAL` không trả lời được.

`approved.yaml` và `published.yaml` phải có `set_by: owner`. **Hook chặn nếu thiếu.**

⛔ **Kịch bản cũ `Video*/Script_*_narration.txt` là read-only** cho tới khi có lệnh migration riêng. Chúng không có lịch sử phiên bản và project chưa có git bao phủ chúng.

**Ba ràng buộc cứng của lời đọc** — vi phạm là hỏng, không phải là lệch:
`!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng.

⛔ `I ≈ 0` **đã gỡ 07/08/2026**. Người dẫn được có ý kiến riêng. Nếu cần đo `I`, coi nó là triệu chứng để đọc lại, không phải điều kiện chặn.

**Mọi con số khác là triệu chứng.** Lệch thì đi đọc đoạn đó và hỏi *"đoạn này có dở không?"*. Không dở thì để yên. **Cấm sửa một câu để con số đẹp hơn.**

## Story engine — Cỗ máy cấu trúc câu chuyện — chỉ nạp khi đang xử lý cấu trúc

Khi công việc là **lên xương · nối chương · chẩn đoán retention · sửa cấu trúc**, dùng skill project-local `sketchapiens-story-engine` — **Cỗ máy cấu trúc câu chuyện**.
Đây là **bộ chẩn đoán**, không phải checklist bắt buộc. Không thêm câu chỉ để thoả một cơ chế.

**Agent review không được sửa file này.** Chỉ `/apply-review` tạo version mới, và chỉ sau khi người dùng đã phân loại từng góp ý.

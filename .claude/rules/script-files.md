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

## Writer — Bộ não viết lời

Khi công việc là **viết narration · tiếp tục batch · hiện thực hóa research/structure thành câu chữ · rewrite EN sau khi VI đã được owner duyệt**, dùng project-local `sketchapiens-viet-kich-ban`.

**Ownership contract — hợp đồng sở hữu:** `.claude/skills/sketchapiens-viet-kich-ban/CONTRACT.md`.

Writer sở hữu **prose realization · writing-session orchestration · VI drafting · EN final semantic rewrite · natural expression of evidence verdict đã resolved**.

Writer **không** sở hữu structural theory, factual verdict, market/competitor research, review verdict, packaging hay production. `references/runtime-monolith-legacy.md` chỉ là provenance/rollback và **không được default-load trong normal writing**.

## Story Engine — Cỗ máy cấu trúc câu chuyện

Khi công việc là **lên xương · nối chương · chẩn đoán structural retention · sửa cấu trúc**, dùng project-local `sketchapiens-story-engine` — **Cỗ máy cấu trúc câu chuyện**.

**Ownership contract — hợp đồng sở hữu:** `.claude/skills/sketchapiens-story-engine/CONTRACT.md`.

Story Engine sở hữu **structural causality · belief progression · explanatory progression · structural stress test**. Đây là **bộ chẩn đoán**, không phải checklist bắt buộc. Không thêm câu chỉ để thoả một cơ chế.

`sketchapiens-giu-chan-nguoi-xem` chỉ là **supporting legacy module — module hỗ trợ kế thừa** cho hook/pacing/craft observations; nó **không được override Story Engine ở phạm vi cấu trúc**.

Evidence verdict vẫn thuộc Evidence reviewer. Story Engine chỉ được flag rủi ro `Narrative Overreach — Cốt truyện chạy vượt bằng chứng`, không tự kết án nguồn.

**Agent review không được sửa file kịch bản.** Chỉ `/apply-review` tạo version mới, và chỉ sau khi người dùng đã phân loại từng góp ý.

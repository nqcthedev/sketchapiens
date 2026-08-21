# `candidate-lifecycle.md` — VÒNG ĐỜI CƠ CHẾ ỨNG VIÊN

> **Status — trạng thái:** `CANONICAL CANDIDATE LIFECYCLE` = hợp đồng chuẩn cho tri thức thử nghiệm trong Story Engine.
>
> File này chỉ quản lý **candidate mechanisms — cơ chế ứng viên** và đường thăng/hạ của chúng. Nó **không phải creative rule**, không được auto-load khi viết/review thường và không thay `governance/CHANGE_POLICY.md`.

---

## 1. PURPOSE — MỤC ĐÍCH

Mục tiêu của Candidate Lifecycle là ngăn một pattern mới đi theo đường tắt:

```text
một video nghe hay
→ đặt tên mechanism
→ Claude bắt đầu dùng khi viết
→ reviewer bắt đầu chấm theo nó
→ vài vòng sau nó thành "luật" mà không ai nhớ vì sao
```

Đường đúng:

```text
OBSERVATION — quan sát
→ CANDIDATE — ứng viên
→ TESTING — đang kiểm
→ SUPPORTED / PARKED / MERGED / REJECTED
→ nếu đủ điều kiện mới tạo PROMOTION PROPOSAL — đề xuất nâng cấp
→ OWNER DECISION — chủ quyết
→ canonical destination phù hợp
```

**Không có đường mặc định `candidate → RULE_REGISTRY`.**

---

## 2. ISOLATION BOUNDARY — RANH GIỚI CÁCH LY

Candidate chỉ được dùng trong:

- mechanism R&D — nghiên cứu cơ chế;
- cross-corpus validation — kiểm chéo corpus;
- postmortem — hậu kiểm;
- controlled experiment — thử nghiệm có chủ đích trên một video;
- promotion / merge / demote / reject decision.

Candidate **không được dùng mặc định** trong:

- writer Structure Mode;
- narration drafting;
- normal script review;
- viewer-retention-judge;
- evidence-prosecutor;
- editor rewrite;
- `CLAUDE.md` hard rules;
- `.claude/rules/**`;
- `RULE_REGISTRY.yaml`;
- templates bắt buộc của mọi video.

Nếu một caller không ở R&D/postmortem/explicit experiment mode, **không mở `mechanism-lab.md`**.

---

## 3. STATUS MACHINE — MÁY TRẠNG THÁI

Mỗi candidate chỉ có một trạng thái chính.

### `observation` — quan sát

Chưa phải mechanism.
Chỉ là hiện tượng đáng chú ý.

Ví dụ:

> "Một video chuyển lời giải từ cơ thể → vật liệu → thời gian → nhóm → kiến trúc."

Ở trạng thái này:
- chưa cần tên riêng;
- chưa được dùng để chấm script;
- chưa được suy ra causal effect.

### `candidate` — ứng viên

Có giả thuyết đủ rõ để kiểm.
Bắt buộc có:

- WHAT IT CLAIMS — nó đang giả thuyết điều gì;
- WHAT IT DOES NOT CLAIM — không được suy thành gì;
- known examples;
- failure modes / counterexamples;
- next test;
- promotion bar.

### `testing` — đang kiểm

Đã có kế hoạch kiểm thật.
Phải ghi:

- corpus/sample nào đang kiểm;
- positive cases;
- negative/counterexamples;
- ai/đợt nào kiểm;
- test nào có thể làm candidate thất bại.

Không được gọi `testing` nếu chỉ đang tìm thêm ví dụ ủng hộ.

### `supported` — được hỗ trợ

Candidate sống sót qua kiểm chéo đủ để coi là **một hiểu biết hữu ích**, nhưng **chưa tự động là rule**.

`supported` phải trả lời được:

- nó hữu ích ở scope nào;
- failure mode nào đã biết;
- evidence nào chống lại nó;
- nó khác mechanism canonical gần nhất ở đâu.

### `parked` — tạm gác

Ý tưởng có thể đúng nhưng chưa đủ dữ liệu hoặc chưa đáng ưu tiên.
Không dùng trong runtime.

### `merged` — đã gộp

Hai candidate/mechanism hóa ra cùng một thứ ở hai cách gọi.
Giữ lịch sử và trỏ sang destination mới.

### `rejected` — bác bỏ

Không qua test, không đủ khác biệt, hoặc tạo failure mode lớn hơn giá trị.
**Không xóa dấu vết.** Ghi lý do để project không phát minh lại cùng idea sau này.

### `promotion_proposed` — đã đề xuất nâng cấp

Chỉ dùng khi candidate `supported` đã có destination rõ và đủ điều kiện phù hợp.

Nó vẫn **chưa canonical** cho tới khi owner duyệt.

---

## 4. CANONICAL DESTINATIONS — ĐÍCH ĐẾN CHUẨN

Candidate trưởng thành có thể đi tới một trong ba nơi, không mặc định vào rule registry.

### A. `CANONICAL DIAGNOSTIC FRAMEWORK` — Khung chẩn đoán chuẩn

Dùng để **nhìn / chẩn đoán**, không bắt script phải có.

Ví dụ phù hợp khi:
- framework giải thích lỗi tốt;
- không có bằng chứng rằng presence gây view;
- ép nó thành requirement sẽ tạo template.

### B. `CANONICAL MEASURED PATTERN` — Pattern đã đo chuẩn

Mô tả điều corpus/analytics đã quan sát.
Không được tự nói pattern đó gây retention/view nếu dữ liệu không chứng minh causal effect.

### C. `CANONICAL RULE / GUARDRAIL` — Luật / hàng rào chuẩn

Chỉ khi thật sự cần hành vi bắt buộc hoặc cấm.
Phải tuân toàn bộ `governance/CHANGE_POLICY.md` + owner approval.

---

## 5. PROMOTION GATES — CỔNG NÂNG CẤP

Trước khi candidate được đề xuất promote, phải có ít nhất:

1. **Identity — Nhận dạng:** khác rõ mechanism canonical nào đang có?
2. **Positive evidence — Bằng chứng thuận:** xuất hiện ở đâu, sample bao nhiêu?
3. **Counterevidence — Bằng chứng nghịch:** đã chủ động tìm case ngược chưa?
4. **Failure mode — Cách hỏng:** dùng sai sẽ phá script thế nào?
5. **Scope — Phạm vi:** mọi video, một lane, hay chỉ một kiểu problem?
6. **Test on Sketchapiens — Thử trên kênh mình:** ít nhất phải biết nó có giúp chẩn đoán mà không ép câu giả hay không.
7. **Destination — Đích đến:** diagnostic / measured pattern / rule-guardrail?
8. **Owner decision — Chủ quyết:** nếu là promotion thật.

Nếu đích là `RULE / GUARDRAIL`, còn phải đủ **5 điều kiện của `CHANGE_POLICY.md`**.

---

## 6. CONTROLLED EXPERIMENT — THỬ NGHIỆM CÓ KIỂM SOÁT

Có một ngoại lệ cho việc dùng candidate trước khi promote:

> Owner có thể yêu cầu **thử một candidate trên một video cụ thể**.

Khi đó phải gắn rõ:

```text
EXPERIMENTAL — THỬ NGHIỆM
candidate: M-XXX
video: SKA-....
reason: ...
what would falsify it: ...
```

Trong experiment:

- candidate được dùng như **lens để thử**, không phải requirement;
- không sửa research để khớp mechanism;
- không ép section mới chỉ để đủ pattern;
- reviewer normal không được biết candidate nếu mục tiêu là đo phản ứng không bị priming;
- postmortem phải ghi candidate giúp gì / làm hỏng gì / không khác gì.

Một experiment thành công **không tự promote candidate**.

---

## 7. CONSUMER FIREWALL — TƯỜNG LỬA VỚI CONSUMER

### Writer — Bộ não viết

Default:

> không đọc Mechanism Lab, không biết tên candidate cụ thể.

Nếu candidate vô tình xuất hiện trong historical writer body, nó **không có authority** trừ khi được canonical hóa ở nơi hiện hành.

### Viewer Retention Judge — Giám khảo giữ chân

Default:

> không đọc Mechanism Lab, không dùng candidate làm tiêu chí chấm.

Nếu candidate đang được test, reviewer vẫn nên **blind — không biết thử nghiệm** trừ khi test design đòi hỏi ngược lại.

### Evidence Prosecutor — Công tố viên bằng chứng

Không cần candidate theory để phán claim.
Nó chỉ kiểm support của nguồn.

### Postmortem — Hậu kiểm

Được đọc candidate lifecycle + Mechanism Lab.
Nó có nhiệm vụ **tạo/ cập nhật candidate**, không nhảy thẳng từ một video sang rule.

### Governance

`RULE_REGISTRY.yaml` chỉ nhận candidate sau khi promotion path hoàn tất và owner duyệt.

---

## 8. LEAKAGE TEST — PHÉP KIỂM RÒ RỈ

Một candidate bị coi là **leaked — rò ra runtime** nếu xảy ra một trong các trường hợp:

- tên candidate nằm trong frontmatter description của writer/reviewer để tự kích hoạt;
- writer bình thường được yêu cầu dùng candidate;
- reviewer bình thường chấm "thiếu candidate";
- `.claude/rules/**` nhắc candidate như requirement;
- `RULE_REGISTRY.yaml` chứa candidate chưa qua promotion;
- template bắt buộc có ô cho candidate;
- `CLAUDE.md` dùng candidate như global principle;
- postmortem của một video đơn lẻ ghi thẳng thành rule proposal mà chưa qua candidate stage.

**Human README / lab / R&D docs được phép nhắc tên candidate.**
Tên xuất hiện không đồng nghĩa leakage; **authority + runtime path** mới là điều cần kiểm.

---

## 9. DUPLICATE TEST — PHÉP KIỂM TRÙNG CƠ CHẾ

Trước khi tạo candidate mới, hỏi:

1. Đây có chỉ là ví dụ của mechanism canonical đã có?
2. Đây có phải cùng mechanism nhưng ở level khác?
3. Khác biệt có tạo ra quyết định chẩn đoán khác không?
4. Nếu bỏ tên mới, project mất khả năng nhìn gì?

Nếu không trả lời được câu 4, ưu tiên **không tạo tên mới**.

---

## 10. CURRENT CANDIDATES — ỨNG VIÊN HIỆN TẠI

Nguồn dữ liệu candidate hiện tại:

`mechanism-lab.md` — **Phòng thí nghiệm cơ chế**.

NEXT-02D không thay đổi verdict của từng candidate hiện có.
Nó chỉ khóa đường lifecycle và firewall.

Đặc biệt với M-004:

- `Narrative Overreach — Cốt truyện chạy vượt bằng chứng` đã là **canonical Story Engine symptom — triệu chứng chuẩn của Story Engine**;
- phần còn `candidate` ở M-004 là câu hỏi **Evidence Fit có cần thành check riêng / thuộc Evidence Engine ở mức nào**, không phải câu hỏi "overreach có tồn tại hay không".

---

## 11. CHANGE LOG RULE — LUẬT GHI THAY ĐỔI

Mỗi lần đổi status candidate, ghi tối thiểu:

```text
DATE — ngày
FROM → TO — trạng thái cũ → mới
WHY — vì sao
EVIDENCE — bằng chứng
COUNTEREVIDENCE — bằng chứng nghịch
OWNER DECISION — nếu có
DESTINATION — nếu promote/merge
```

Không sửa lịch sử để làm candidate trông sạch hơn.

---

## 12. CORE PRINCIPLE — NGUYÊN TẮC LÕI

> **Candidate exists to be disproved as easily as it can be supported.**
>
> **Cơ chế ứng viên phải được thiết kế để có thể bị bác dễ như được ủng hộ.**

Nếu project chỉ đi tìm thêm ví dụ thuận, Mechanism Lab đã biến thành kho confirmation bias — thiên kiến xác nhận.

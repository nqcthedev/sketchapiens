# 03A-B — RESPONSIBILITY DECOMPOSITION — PHÂN RÃ TRÁCH NHIỆM WRITER

> **Status:** `READ-ONLY AUDIT ARTIFACT — NON-RUNTIME`  
> Không sửa `SKILL.md` hoặc `references/**`. File này chỉ phân rã những nghề Writer hiện đang làm; **chưa quyết source of truth / placement cuối**.

**Baseline:** checkpoint `84a15dfe2586dd2dcf002ea0ecb6a924a2bca68e`  
**Parent audit:** `phase3a-writer-audit.md`

## Câu hỏi của task

Writer monolith hiện đang gánh bao nhiêu responsibility độc lập, chúng giao nhau ở đâu, và responsibility nào có thể tách về mặt khái niệm mà chưa cần quyết định refactor?

**Stop condition:** có responsibility map đủ rõ để 03A-C kiểm authority từng vùng.

---

## 1. Responsibility map hiện tại

Audit nhận diện **14 responsibility** đang cùng xuất hiện trong Writer implementation / references.

| ID | Responsibility — trách nhiệm | Hiện xuất hiện ở đâu | Dấu hiệu tách được về khái niệm |
|---|---|---|---|
| W-R01 | **Activation / routing — kích hoạt & định tuyến** | wrapper frontmatter + legacy frontmatter + mode prose | public-interface concern, không phải creative implementation |
| W-R02 | **Writing workflow orchestration — điều phối phiên viết** | VI-first/EN-last wrapper; batch writing; owner approval pauses | workflow/lifecycle của Writer |
| W-R03 | **Niche writing principles — nguyên lý viết của ngách** | PHẦN 0, `luat-chung-ngach.md` | knowledge dùng để lựa chọn cách kể, khác với workflow |
| W-R04 | **Story structure — cấu trúc câu chuyện** | hook/body/chapter/end sections; transition theory; teardown refs | structural reasoning là một concern riêng |
| W-R05 | **Narration voice/register — giọng lời đọc** | PHẦN 4; tone selection; humor/deadpan; sentence rhythm | prose-generation concern |
| W-R06 | **Translation / representation transform — chuyển VI → EN** | active wrapper/CLAUDE contract; legacy metadata còn English-first | representation concern sau VI approval |
| W-R07 | **Evidence-aware writing — viết dựa trên bằng chứng** | PHẦN 5; anchor naming; uncertainty/hedging; verify-anchor note | writer needs evidence input, nhưng factual verdict là concern khác |
| W-R08 | **Topic/title research — nghiên cứu đề tài/title** | monolith PHẦN 1; `quy-trinh-nghien-cuu-cum.md`; clone-swarm logic | mode ① concern, xảy ra trước drafting |
| W-R09 | **Competitor research/calibration — nghiên cứu/hiệu chỉnh đối thủ** | `viral-teardown`, `formula-and-example`, survival teardown | research/history/calibration concern; chứa competitor text |
| W-R10 | **Retention craft — kỹ thuật giữ nhịp cấp câu/đoạn** | pre-load, bucket brigade, rhetorical fragments, humor relief | craft concern khác structural causality |
| W-R11 | **Originality / reuse / policy safety — tính gốc & an toàn** | PHẦN 7; competitor reuse warnings; safety language | project/policy boundary, không chỉ prose style |
| W-R12 | **Output/artifact formatting — định dạng đầu ra** | PHẦN 8 cũ; wrapper contract; script-files rule/version semantics | artifact/interface concern |
| W-R13 | **Packaging metadata — đóng gói sau script** | `metadata.md`; title/description/tags/file-name SEO | xảy ra sau script theo chính reference đó |
| W-R14 | **Measurement/history/override ledger — số đo, phản chứng, luật chết** | PHẦN 13–14; strike-through corrections; banners; dated corpus findings | R&D/provenance/history concern, không phải instructions để sinh từng câu |

### Kết luận B-01

Writer hiện không phải “một module viết script lớn”; nó là **một container lịch sử của nhiều domain** được tích luỹ qua thời gian.

---

## 2. Ba lớp đang bị trộn trong cùng một file

### A. Control / orchestration

Ví dụ:

- chế độ nào đang chạy;
- VI trước / EN sau;
- viết theo batch;
- khi nào dừng cho owner;
- output representation nào được phép.

### B. Creative implementation

Ví dụ:

- giọng kể;
- cách biến fact thành narration;
- nhịp câu;
- mức hài;
- cách diễn uncertainty;
- cách viết hook/kết khi structure đã được quyết.

### C. Knowledge/provenance/history

Ví dụ:

- 3 transcript viral cũ;
- corpus measurements;
- rule đã chết;
- counterexample;
- “PHẦN 13–14 thắng PHẦN 0–12”;
- lý do một benchmark từng bị bác.

Hiện ba lớp này cùng xuất hiện trong runtime monolith. Model phải vừa **làm việc**, vừa **đọc lịch sử vì sao cách làm cũ sai**, vừa **tự giải precedence**.

### Kết luận B-02

Đây là `separation-of-concerns debt — nợ tách trách nhiệm`, không đơn thuần là “file quá dài”. Một monolith ngắn hơn nhưng vẫn trộn ba lớp này vẫn là refactor thất bại.

---

## 3. Cross-mode responsibilities — trách nhiệm sai thời điểm

Project đã định nghĩa bốn mode rõ trong `CLAUDE.md`, nhưng Writer legacy vẫn chứa concern của nhiều mode:

```text
MODE ① RESEARCH
  W-R08 topic/title research
  W-R09 competitor research/calibration

MODE ② WRITE
  W-R02 orchestration
  W-R03 niche principles
  W-R05 voice/register
  W-R06 VI→EN transform
  W-R07 evidence-aware expression
  W-R10 sentence/paragraph craft
  một phần W-R11 originality/safety

STRUCTURAL PEER DURING WRITE/REVIEW
  W-R04 story structure

MODE ④ / PACKAGING-LATER SURFACE
  W-R13 metadata/title/description/tags

CROSS-CUTTING CONTROL/HISTORY
  W-R01 routing
  W-R12 artifact/output contract
  W-R14 measurement/history/provenance
```

### Kết luận B-03

Monolith không chỉ lớn theo **chủ đề knowledge**; nó lớn vì nó **vượt ranh giới thời gian của workflow**. Progressive disclosure phải dựa vào *task moment* chứ không chỉ chia file theo PHẦN 1/2/3.

---

## 4. Responsibility collisions — nơi hai responsibility dính nhau

### C-1 — Title có ít nhất ba nghĩa

`title` hiện xuất hiện như:

1. **market/topic selection** — chọn title để quyết có làm video không;
2. **story promise** — title là promise cấu trúc mà narration phải trả;
3. **packaging metadata** — title cuối cùng để upload.

Không thể “tách toàn bộ title vào một file” chỉ vì cùng từ `title`.

### C-2 — Hook có hai tầng

- **structural function:** hook mở question/model nào, promise gì;
- **prose craft:** hook viết câu nào, nhịp gì, register gì.

Nếu refactor theo heading `HOOK`, Story Engine và Writer craft sẽ lại chồng authority.

### C-3 — Evidence có hai tầng

- **evidence verdict:** nguồn support claim tới mức nào;
- **evidence expression:** viết claim đã được duyệt ra lời nói tự nhiên, đặt hedge/anchor ở đâu.

Writer cần tầng sau, không nhất thiết sở hữu tầng trước.

### C-4 — Retention có hai tầng

- **structural retention:** progression / causal handoff / belief movement;
- **sentence-level craft:** pacing, fragments, setup/payoff wording, breathing room.

Phase 2 đã chứng minh hai tầng cần boundary riêng.

### C-5 — “Luật ngách” trộn prescription và measurement

Một file vừa nói “phải làm X”, vừa kể X được đúc từ n=3, vừa có block sau bác X. Đây là knowledge-state collision, không chỉ duplication.

---

## 5. Responsibility nào có coupling thật với Writer?

Chỉ đánh dấu **coupling**, chưa kết luận ownership.

### High coupling — Writer không thể tạo narration tốt nếu hoàn toàn thiếu

- W-R02 orchestration;
- W-R03 active niche writing principles;
- W-R05 narration voice/register;
- W-R06 VI→EN transform;
- W-R07 evidence-aware expression;
- W-R10 sentence/paragraph craft;
- phần runtime của W-R11 originality/safety;
- W-R12 output contract tối thiểu.

### Medium coupling — Writer cần interface/result, không nhất thiết cần implementation đầy đủ

- W-R04 story structure;
- W-R08 topic/title decision;
- evidence verdict thuộc W-R07 boundary;
- packaging promise thuộc W-R13 boundary.

### Low/zero coupling trong normal write runtime

- W-R09 raw competitor teardown/calibration;
- W-R13 metadata generation sau script;
- W-R14 historical measurements/retired-rule rationale.

### Kết luận B-04

Một future Writer runtime có thể vẫn rất giàu creative capability **mà không cần mang toàn bộ research/history/packaging implementation vào context**.

---

## 6. Anti-pattern cần tránh ở Phase 3B+

### Không tách file theo heading máy móc

Ví dụ xấu:

```text
hook.md
body.md
ending.md
```

nếu mỗi file vẫn chứa lẫn structure + prose + measurements + competitor examples.

### Không tạo module chỉ để sơ đồ cân đối

Responsibility decomposition không có nghĩa 14 responsibility = 14 skill/module.
Nhiều responsibility có thể là reference nhỏ trong cùng Writer nếu cùng lifecycle/context.

### Không chuyển lịch sử sang một file “history.md” rồi auto-load file đó

Đó chỉ là đổi tên context pollution.

### Không giải collision bằng precedence sâu hơn

Mục tiêu Phase 3 là giảm nhu cầu model phải nhớ “đoạn cuối file X thắng đoạn đầu file Y”.

---

## 7. CHECK — 03A-B

- [x] monolith được phân thành responsibility thay vì chỉ heading;
- [x] control / creative implementation / history được tách về mặt khái niệm;
- [x] cross-mode responsibilities được nhận diện;
- [x] title/hook/evidence/retention collisions được mô tả;
- [x] coupling với Writer được phân high/medium/low;
- [x] chưa quyết canonical owner — để 03A-C;
- [x] chưa chỉnh runtime;
- [x] chưa tạo target folder architecture.

**03A-B verdict:** `PASS — responsibility boundaries are sufficiently decomposed for authority audit`.

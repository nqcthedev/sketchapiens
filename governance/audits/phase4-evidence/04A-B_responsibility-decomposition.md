# 04A-B — RESPONSIBILITY DECOMPOSITION — PHÂN RÃ TRÁCH NHIỆM EVIDENCE

> **Mode:** READ-ONLY Evidence runtime
> **Input:** 04A-A inventory + active runtime surfaces + V17–V20 historical evidence artifacts
> **Mục tiêu:** tách việc nghiệp vụ trước khi hỏi file/module nào sở hữu.

---

## 1. EVIDENCE DOMAIN KHÔNG PHẢI MỘT VIỆC

Audit hiện thấy ít nhất **15 responsibility — trách nhiệm** độc lập về mặt quyết định.

### R-01 — Source Retrieval — Lấy nguồn

Tìm/mở paper, page, dataset, archaeological report hoặc nguồn gốc cần kiểm.

Câu hỏi:

> Có truy cập được nguồn thực sự không?

Không đồng nhất với verdict.

### R-02 — Provenance & Full-Text Validation — Kiểm provenance/toàn văn

Phân biệt:

- full text;
- abstract;
- snippet;
- secondary summary;
- competitor claim;
- unavailable source.

Câu hỏi:

> Ta đang biết điều này từ đâu và đã đọc tới mức nào?

### R-03 — Claim Segmentation — Tách mệnh đề

Một sentence có thể chứa nhiều factual propositions.
Evidence review cần biết đơn vị nào đang được phán.

Câu hỏi:

> Claim nào chính xác đang cần support?

### R-04 — Direct Support Comparison — So claim với điều nguồn nói

So sánh:

```text
SCRIPT CLAIM
vs
SOURCE SAYS
```

Bao gồm:

- đúng population?
- đúng timeframe?
- đúng denominator?
- đúng number/unit?
- đúng event?

### R-05 — Verdict Classification — Phân loại mức quan hệ với nguồn

Runtime hiện dùng:

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

Đây là factual-status decision, không phải prose decision.

### R-06 — Epistemic Distance — Khoảng cách nhận thức

Đánh giá claim rộng hơn nguồn đến đâu:

- author conclusion;
- project inference;
- extrapolation;
- reconstruction;
- unsupported assertion.

Hiện một phần được biểu diễn bằng `kind`, một phần bằng `overreach`, một phần bằng free-text note.

### R-07 — Causal Bridge Validation — Kiểm đường nối nhân quả

Đây là câu hỏi khác với fact-by-fact support:

> Hai hoặc nhiều fact riêng đều đúng, nhưng chúng có support **bridge** mà script đang dựng không?

Historical V18 là case rõ: segmented sleep evidence + sentinel evidence đều thật nhưng bridge giữa hai mechanism bị chính project loại vì logic không hợp lệ.

### R-08 — Synthesis Validation — Kiểm tổng hợp

Khi project ghép nhiều nguồn thành explanatory model:

- từng component có support không?
- relationship giữa components được support hay chỉ plausible?
- phần nào là project synthesis?
- certainty của conclusion có đúng không?

`SYNTHESIS` ở đây là responsibility cần audit, **chưa phải runtime verdict label**.

### R-09 — Transfer / Scope Validation — Kiểm suy rộng phạm vi

Ví dụ:

- modern → prehistoric;
- one population → universal humans;
- animal physiology → human;
- one climate/context → another;
- one archaeological interpretation → intentional behavior.

Historical V17–V20 dùng explicit hedge cho vùng này.

### R-10 — Overreach Severity — Mức vượt

Runtime hiện có `0–3`.
Nhưng semantic hiện hơi heterogeneous:

- `0` khớp;
- `1` rộng hơn;
- `2` mô tả cụ thể “bắc cầu hai bảng số”;
- `3` “bịa”.

Một scale severity đáng lẽ đo **mức độ**, trong khi level 2 hiện chứa **một loại lỗi cụ thể**.
04A-D cần audit đây là intentional design hay semantic mixing.

### R-11 — Lock / Rerun Policy — Chính sách khóa và chạy lại

Quyết định:

- khi nào evidence gate hoàn tất;
- factual edit nào làm gate stale;
- khi nào phải rerun;
- khi nào `locked` được đổi.

Đây là workflow/state responsibility, khác verdict semantics.

### R-12 — Ledger Artifact Mutation — Ghi/cập nhật artifact

Ai được:

- tạo claim row;
- update verdict;
- update source fields;
- set `locked`;
- mark DEAD/UNVERIFIED/NEEDS_REWRITE?

Hiện workflow docs nói nơi ghi, nhưng mutation authority chưa được contract hóa rõ như Writer version refs.

### R-13 — Evidence Expression — Diễn đạt verdict trong narration

Writer sở hữu:

- wording;
- natural hedge;
- attribution;
- making inference visible;
- preserving certainty in VI/EN.

Writer **không** sở hữu factual verdict.

### R-14 — Structural Evidence Placement — Đặt evidence vào câu chuyện

Story Engine sở hữu:

- evidence block xuất hiện ở đâu;
- trả câu hỏi structural nào;
- có advance belief/model không;
- flag Narrative Overreach symptom.

Story Engine **không** issue factual verdict.

### R-15 — Review / Editorial Orchestration — Điều phối review/sửa

- `/audit-script` tạo context đúng cho Evidence Prosecutor;
- `/apply-review` yêu cầu rerun nếu factual content thay đổi;
- owner quyết review item nào được áp;
- editor không tự nâng factual support.

---

## 2. CURRENT MIXING MAP

| Responsibility | Surface hiện đang gánh |
|---|---|
| R-01 Source Retrieval | evidence-prosecutor tools + human/research workflow |
| R-02 Provenance | prosecutor + ledger template + schema |
| R-03 Claim Segmentation | mostly prosecutor behavior; schema chỉ lưu row sau khi đã tách |
| R-04 Direct Comparison | prosecutor + template fields |
| R-05 Verdict Classification | prosecutor + template + schema + verify-claims + audit-script |
| R-06 Epistemic Distance | prosecutor + `kind` + `overreach` + notes + Writer expression |
| R-07 Causal Bridge Validation | prosecutor rule #1 + Story Narrative Overreach + historical manual reasoning |
| R-08 Synthesis Validation | Story `Original Synthesis` + Writer inference wording + chưa có explicit Evidence contract |
| R-09 Transfer/Scope | prosecutor + schema booleans + Writer expression |
| R-10 Overreach Severity | prosecutor + template + schema + verify-claims lock threshold |
| R-11 Lock/Rerun | verify-claims + template + apply-review |
| R-12 Ledger Mutation | verify-claims says where; schema says shape; explicit authority chưa rõ |
| R-13 Evidence Expression | Writer reference |
| R-14 Structural Placement | Story Engine reference |
| R-15 Review/Edit Orchestration | audit-script + apply-review |

---

## 3. IMPORTANT SEPARATIONS

### Separation A — Retrieval ≠ Verdict

Web/source access failure phải tạo trạng thái provenance/verification phù hợp.
Không được biến “không mở được” thành “claim sai”, cũng không biến snippet thành direct proof.

### Separation B — Verdict ≠ Wording

Evidence quyết claim được phép mạnh tới đâu.
Writer quyết cách nói tự nhiên trong boundary đó.

### Separation C — Verdict ≠ Structural Need

Story có thể **cần** bridge Y để chapter chạy.
Evidence không được nâng source thành Y chỉ vì story cần.

### Separation D — Correct Components ≠ Correct Synthesis

A đúng + B đúng không tự chứng minh `A → B` hoặc thesis `A+B = C`.
Đây là vùng M-004/Egypt làm nổi bật.

### Separation E — Artifact Shape ≠ Semantic Authority

Schema nên bắt machine shape.
Nó không nên trở thành nơi giải thích dài tại sao một inference hợp lệ hay không.
Ngược lại prose contract không nên tự tạo enum khác schema.

### Separation F — Gate State ≠ Evidence Category

`locked`, rerun trigger, status và factual kind là các dimension khác nhau.
Không dùng một label để gánh nhiều dimension.

---

## 4. HISTORICAL CASES CHỨNG MINH VIỆC PHÂN RÃ CẦN THIẾT

### V17 Rain

File historical phân biệt:

- verified facts;
- deliberate story devices;
- removed unsupported lines;
- modern ethnography kept scoped as modern.

Tức là project đã dùng nhiều dimension hơn một cột “đúng/sai”.

### V18 Sleep

Project tự loại bridge:

```text
segmented sleep inside one person
≠
age/chronotype variation across people
```

Cả hai evidence blocks có thể individually verified nhưng causal/explanatory connection vẫn invalid.
Đây là R-07, không chỉ R-04.

### V19 NightWalk

Historical evidence ghi:

- không được tự bịa evolutionary purpose cho vasopressin;
- denominator correction: 50% attacks ≠ 50% deaths;
- effect của cold diuresis chắc hơn mechanism giải thích nó.

Ba lỗi này lần lượt thuộc R-08/R-09, R-04 và R-06/R-09.

### V20 Cold

Historical evidence bắt:

- animal → human transfer;
- modern lab → prehistory;
- archaeological site layout không chứng minh heating purpose;
- effect vs mechanism uncertainty.

Đây là transfer/scope + interpretation certainty, không thể biểu diễn sạch chỉ bằng “source exists”.

---

## 5. DESIGN CONSEQUENCE CHO 04A — CHƯA PHẢI IMPLEMENTATION

Phase 4A phải trả lời tối thiểu:

1. semantic owner của R-04→R-10 là ai;
2. workflow owner của R-11→R-12 là ai;
3. schema/template chỉ encode contract hay đang duplicate semantic authority;
4. Story/Writer handoff được public hóa ở đâu;
5. `SYNTHESIS` cần verdict riêng, sub-type, relationship object hay chỉ inference metadata;
6. causal bridge cần claim row riêng hay một relation/bridge artifact;
7. current `overreach 0–3` có nên tiếp tục trộn severity với error type hay không.

Không quyết các câu này trong 04A-B.

---

## 6. CHECK 04A-B

PASS nếu:

- retrieval, provenance, verdict, bridge, synthesis, gate, mutation, wording, placement được tách thành responsibility riêng;
- không gán owner mới chỉ vì file hiện đang chứa text;
- historical examples dùng để chứng minh decomposition, không biến thành rule;
- Evidence runtime không đổi.

**Result: PASS.**

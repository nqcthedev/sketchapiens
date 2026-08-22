# 04A-A — INVENTORY & RUNTIME SURFACE — KIỂM KÊ BỀ MẶT EVIDENCE

> **Phase:** 4A Evidence Audit
> **Mode:** READ-ONLY đối với Evidence runtime
> **Baseline trước Phase 4A:** `cf24a862eef103e9fbc3cdd544d9adbf51e827e5`
> **Mục tiêu:** map đúng những artifact đang tham gia factual/evidence flow trước khi đề xuất module shape.
> **Không phải:** contract mới, taxonomy mới, rule mới, hay quyết định tạo `sketchapiens-evidence-engine`.

---

## 1. ACTIVE RUNTIME / CONTROL SURFACE

### A. Evidence verdict agent

`.claude/agents/evidence-prosecutor.md`

Hiện agent này trực tiếp:

- đọc narration + claim ledger + nguồn;
- phân loại claim thành `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE`;
- gán `Mức vượt 0–3`;
- bắt bridge giữa hai bảng/statistics rời;
- bắt author inference bị kể như measurement;
- bắt modern → prehistoric extrapolation;
- bắt snippet-only source;
- trả `KHOÁ ĐƯỢC / CHƯA KHOÁ ĐƯỢC`.

Nó **không** sở hữu prose/retention theo frontmatter + body hiện hành.

### B. Verification workflow wrapper

`.claude/skills/verify-claims/SKILL.md`

Hiện wrapper này:

- định thời điểm phải verify;
- gọi `evidence-prosecutor`;
- yêu cầu rerun mỗi khi factual sentence/claim mới xuất hiện;
- ghi kết quả vào `videos/<ID>/02-research/claim-ledger.md`;
- dùng threshold `mức vượt >= 2` để quyết định `KHOÁ ĐƯỢC`.

`verify-claims` hiện chỉ có một `SKILL.md`, chưa có contract/references/tests riêng.

### C. Human-facing claim ledger template

`templates/claim-ledger.md`

Template này hiện nhắc lại:

- bốn verdict label;
- `Vượt 0–3` semantics;
- full-text requirement;
- author inference wording requirement;
- ban on bridging separated statistics;
- rerun after lock;
- DEAD anchors section;
- final lock verdict.

### D. Machine-readable ledger schema

`schemas/claim-ledger.schema.json`

Schema hiện sở hữu machine shape:

- `video_id`;
- `locked`;
- `claims[]`;
- enum `kind = DIRECT | INFERENCE | SPECULATION | STORY_DEVICE`;
- source/provenance fields;
- `read_full_text`;
- `source_says`;
- `sample_size`;
- `overreach` integer `0..3`;
- `author_inference`;
- `modern_to_prehistoric`;
- `status = OK | UNVERIFIED | DEAD | NEEDS_REWRITE`.

### E. Writer-side Evidence consumer

`.claude/skills/sketchapiens-viet-kich-ban/references/evidence-expression.md`

Writer boundary đã rõ:

```text
Evidence system → support / limitation / provenance
Writer          → wording
```

Writer không issue verdict. File này có handoff trigger khi:

- claim mới chưa có support;
- exact number/name/date chưa verify;
- English rewrite thêm factual content;
- hai fact riêng bị nối thành causal claim;
- wording chỉ đúng nếu tăng certainty;
- provenance chỉ là snippet/summary.

### F. Story-side Evidence consumer

`.claude/skills/sketchapiens-story-engine/references/evidence-in-story.md`

Story Engine sở hữu placement/structural role, không verdict.
Nó có canonical symptom `Narrative Overreach` và handoff:

```text
Story Engine → flag symptom
Evidence     → open source / classify / issue verdict
```

Story reference cũng mô tả `Original Synthesis` như việc ghép nhiều mảnh independently supported, nhưng factual status vẫn route về Evidence.

### G. Review consumer

`.claude/skills/audit-script/SKILL.md`

`/audit-script` chạy `evidence-prosecutor` trong context riêng với:

- narration;
- claim ledger;
- nguồn cần kiểm.

Nó không đưa retention theory / prose rubric cho prosecutor.

### H. Editor/rerun consumer

`.claude/skills/apply-review/SKILL.md`

Bất kỳ factual sentence/claim mới hoặc factual claim bị đổi đều phải rerun `/verify-claims`.
Editor không tự issue evidence verdict.

---

## 2. CURRENT EXPECTED RUNTIME FLOW

```text
research / source material
        ↓
claim ledger candidate
        ↓
/verify-claims
        ↓
evidence-prosecutor
        ↓
verdict + overreach + lock status
        ↓
claim-ledger artifact
        ↓
Story Engine consumes factual boundary for placement
Writer consumes resolved verdict for wording
        ↓
/audit-script may re-prosecute draft
        ↓
/apply-review must rerun verify if factual content changes
```

Đây là **capability graph**, chưa phải module graph.
Hiện không có một Evidence public contract duy nhất nằm giữa các consumer.

---

## 3. LEGACY EVIDENCE ARTIFACTS V17–V20

Legacy videos chưa theo lifecycle directory mới.
Evidence artifacts thực tế gồm nhiều shape:

```text
V17 Death     VERIFY_Anchors_V17_Death.md
V17 Rain      VERIFY_Anchors_V17_Rain.md
V18 Sleep     VERIFY_Anchors_V18.md
V19 NightWalk MONEO_V19.md
V20 Cold      MONEO_V20_Cold.md
```

Các file này chứa reasoning rất giàu:

- verified / rejected / disputed anchors;
- source notes;
- explicit uncertainty;
- author-inference warnings;
- modern-vs-prehistoric boundaries;
- causal bridge corrections;
- provenance corrections;
- notes about what was removed and why.

Nhưng chúng **không conform** với `claim-ledger.schema.json` hiện hành và không dùng một artifact vocabulary thống nhất.

Ví dụ:

- V17 Rain tách `ĐÃ TRA`, `DỰNG CẢNH`, `ĐÃ BỊ LOẠI`, `GIỮ PHẠM VI`;
- V18 ghi thẳng một causal bridge Sleep Segmentation → Sentinel là logic invalid dù từng fact riêng đã verify;
- V19 cấm gán evolutionary purpose cho vasopressin, sửa denominator của hyena statistic, tách effect chắc khỏi mechanism còn tranh cãi;
- V20 ghi mandatory hedges cho modern lab evidence, species transfer và archaeological interpretation.

**Kết luận inventory:** historical evidence knowledge có giá trị regression rất cao, nhưng là historical input/test material, không phải runtime source-of-truth mới.

---

## 4. OWNERSHIP SURFACE HIỆN TẠI — CHƯA KẾT LUẬN

| Concern | Artifact đang nói về nó |
|---|---|
| Evidence verdict taxonomy | evidence-prosecutor · claim-ledger template · schema · verify-claims · audit-script |
| Overreach 0–3 semantics | evidence-prosecutor · template · schema · verify-claims |
| Ledger machine shape | schema |
| Ledger human presentation | template |
| Lock/rerun gate | verify-claims · template · apply-review |
| Evidence wording | Writer evidence-expression |
| Structural evidence placement | Story Engine evidence-in-story |
| Review execution | audit-script → evidence-prosecutor |
| Historical evidence reasoning | VERIFY_Anchors_* · MONEO_* |

Điểm đáng chú ý: `SOURCE_OF_TRUTH.md` hiện map **Evidence verdict** tới `evidence-prosecutor.md + templates/claim-ledger.md`, trong khi schema cũng chứa enum/status/overreach shape có authority máy đọc được.
04A-C phải giải rõ boundary này thay vì để consumer tự suy.

---

## 5. INVENTORY FINDINGS

### I-01 — Evidence capability có nhiều consumer thật

Ít nhất Writer, Story Engine, `/audit-script`, `/apply-review`, `/verify-claims` cùng phụ thuộc factual/evidence verdict.
Điều kiện “multiple independent consumers” cho khả năng tách module **có tín hiệu mạnh**, nhưng chưa đủ để quyết định module trước 04A-G.

### I-02 — Public interface đang thiếu

Consumer hiện route bằng tên agent/command/template/schema hơn là một contract Evidence duy nhất.
Đây là architecture smell, chưa tự động nghĩa phải tạo skill mới.

### I-03 — Taxonomy được duplicate textually

Bốn label và overreach semantics lặp ở nhiều active file.
Chưa thấy contradiction lớn trong bốn label, nhưng duplication làm drift risk cao.

### I-04 — `SYNTHESIS` chưa phải runtime verdict

Runtime/schema hiện chỉ có:

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

`SYNTHESIS` hiện chỉ là concept/story-language cần Phase 4 audit; không được coi như label canonical.

### I-05 — Legacy evidence reasoning mạnh hơn shape mới ở một số chiều

V17–V20 đã thực tế bắt những lỗi như:

- verified facts nhưng bridge sai;
- denominator drift;
- source says effect but mechanism disputed;
- plausible evolutionary purpose bị tự bịa;
- interpretation cần certainty hedge.

Claim-ledger schema mới có fields hữu ích nhưng chưa rõ tất cả reasoning trên có được represent/verify ổn định hay không.

### I-06 — Evidence Fit question là thật, nhưng chưa biết current prosecutor đã đủ chưa

V18 historical bridge failure và Egypt R&D đều cho thấy:

> từng fact riêng có thể đúng, còn causal role/synthesis vẫn sai.

04A-F phải test prosecutor hiện tại trước khi tạo một `Causal Proof Fit` check riêng.

---

## 6. CHECK 04A-A

PASS nếu:

- inventory bao phủ verdict agent, verification wrapper, ledger template/schema, Writer/Story consumers, review/editor consumers;
- legacy V17–V20 được phân loại là historical evidence, không canonical runtime;
- không đổi Evidence runtime;
- không promote M-004;
- không tạo taxonomy mới.

**Result: PASS.**

Không có Evidence runtime file nào bị sửa trong task này.

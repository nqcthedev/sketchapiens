# 04A-H — EVIDENCE AUDIT CLOSEOUT — ĐÓNG KIỂM TOÁN PHASE 4A

> **Status:** `PHASE 4A COMPLETE — READ-ONLY AUDIT VERIFIED`
> **Baseline:** `cf24a862eef103e9fbc3cdd544d9adbf51e827e5`
> **Scope:** 04A-A → 04A-H
> **Evidence runtime mutation:** NONE

---

## 1. TASK CHAIN RESULT

```text
04A-A Inventory & Runtime Surface           PASS
04A-B Responsibility Decomposition          PASS
04A-C Authority & Source-of-Truth Audit     PASS
04A-D Claim Ledger & Taxonomy Audit         PASS
04A-E Consumer & Dependency Audit           PASS
04A-F Evidence Fit Failure-Mode Audit       PASS
04A-G Evidence Contract Proposal            PASS
04A-H Audit Verification                    PASS
```

---

## 2. STATIC SCOPE VERIFICATION

Compare từ baseline trước Phase 4A tới trước closeout:

```text
base: cf24a862eef103e9fbc3cdd544d9adbf51e827e5
head: 13d317c352245d3a21a427ff7606ab47e8f3e648
```

GitHub compare xác nhận:

- ahead 7 commits;
- behind 0;
- đúng 7 file mới;
- tất cả nằm dưới `governance/audits/phase4-evidence/`;
- không file runtime nào modified/deleted.

Không đổi:

- `.claude/agents/evidence-prosecutor.md`;
- `.claude/skills/verify-claims/SKILL.md`;
- `templates/claim-ledger.md`;
- `schemas/claim-ledger.schema.json`;
- Writer runtime/contract/references;
- Story Engine runtime/contract/references;
- `/audit-script`;
- `/apply-review`;
- `CLAUDE.md`;
- `SOURCE_OF_TRUTH.md`;
- `tools/preflight.py`;
- `tools/project_doctor.py`.

04A vì vậy đạt yêu cầu **audit first, implementation later**.

---

## 3. MAJOR AUDIT FINDINGS

### F-01 — Evidence là domain độc lập thật

Audit thấy đủ tín hiệu module hóa:

- responsibility riêng;
- verify/rerun/lock workflow riêng;
- knowledge riêng;
- nhiều consumer;
- context isolation;
- public interface có thể mô tả độc lập.

**04A-G proposal:** Phase 4B nên tạo project-local `sketchapiens-evidence-engine`.

Đây là proposal đã qua audit, chưa phải runtime implementation.

### F-02 — Evidence semantics hiện phân tán

Hiện semantics/behavior được lặp giữa:

```text
evidence-prosecutor
verify-claims
claim-ledger template
claim-ledger schema
audit-script
Writer evidence-expression
Story evidence-in-story
```

Không có contradiction lớn ở bốn verdict hiện hành, nhưng drift risk cao vì semantic authority chưa có một public contract riêng.

### F-03 — Giữ bốn top-level verdict hiện hành

Audit baseline:

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

Không có evidence đủ mạnh để bỏ/đổi một label trong 04A.

### F-04 — `SYNTHESIS` không nên tự động là verdict thứ năm

Audit cho thấy synthesis thường trả lời:

> claim được dẫn xuất bằng cách nào?

Trong khi `INFERENCE` trả lời:

> claim có quan hệ epistemic nào với evidence?

Vì vậy target proposal là giữ `INFERENCE` factual status và biểu diễn multi-source synthesis/derivation ở dimension khác nếu regression chứng minh cần.

### F-05 — Gap lớn nhất là relation-level evidence

M-004 được thu hẹp thành một identity không trùng basic fact-checking:

> **Evidence nodes can be true while the narrative edge between them is unsupported. Verdict the edge, not only the nodes.**

Historical V18 + V19/V20 + Egypt R&D support việc đây là failure class thật.

Nhưng M-004 vẫn `candidate`; chưa promote trong 04A.

### F-06 — Current prosecutor đã mạnh, không nên thay bỏ

Current prosecutor đã bắt tốt:

- exact source mismatch;
- denominator/population drift;
- modern→prehistoric transfer;
- author inference vs measurement;
- snippet-only provenance;
- một subtype bridge error.

Phase 4B nên **nâng/contract hóa** capability hiện có, không viết một reviewer song song từ đầu.

### F-07 — Claim ledger có representational gaps

Đặc biệt:

- one-source assumption vs multi-source synthesis;
- no first-class dependency/bridge representation;
- project inference vs source-author inference chưa tách sạch;
- `overreach 0–3` trộn severity và error class;
- `locked` chưa bind rõ với immutable script version/input provenance;
- STORY_DEVICE có thể che factual subclaim nếu segmentation quá thô.

### F-08 — Schema tồn tại nhưng chưa được deterministic validator enforce trên ledger thật

`project_doctor.py` parse schema JSON để check syntax nhưng audit không thấy nó validate actual `02-research/claim-ledger.md` against `claim-ledger.schema.json`.

Đây là guardrail/integration gap.

### F-09 — Preflight đang thuộc generation cũ

`tools/preflight.py` hiện kiểm Evidence bằng:

```text
MONEO_*.md
+ citation-looking regex
+ >=3 citations
```

Trong khi lifecycle mới tạo:

```text
videos/SKA-.../02-research/claim-ledger.md
```

Đây là deterministic integration drift phải được resolve trước V21 canary.

Không sửa trong 04A.

### F-10 — Legacy V17–V20 là regression corpus, không phải migration blocker

`VERIFY_Anchors_*` và `MONEO_*` chứa nhiều reasoning quý nhưng heterogeneous.

Target:

- giữ nguyên làm historical evidence/test input;
- không ép migrate toàn bộ legacy vào schema mới;
- dùng để dựng regression fixtures cho Phase 4B.

---

## 4. MODULE DECISION FOR PHASE 4B

### Proposed target

```text
.claude/skills/sketchapiens-evidence-engine/
├── CONTRACT.md
├── SKILL.md
├── README.md
├── references/
└── tests/
```

Chỉ tạo implementation sau 04A-H.

### Ownership target

Evidence Engine owns:

- factual verdict semantics;
- claim↔source fit;
- provenance requirements;
- transfer/scope verdict;
- project inference/synthesis support semantics;
- Causal Proof Fit / bridge verdict;
- lockability semantics.

Does not own:

- topic research strategy;
- Story structure/placement;
- Writer prose;
- retention;
- packaging;
- editor mutation decisions;
- analytics causality.

---

## 5. 04B GATE

Phase 4B được phép mở sau closeout này với task chain:

```text
04B-A — Lock Evidence Contract + create module skeleton
04B-B — Canonical semantics + minimal ledger/schema representation
04B-C — Causal Proof Fit / bridge verdict behavior
04B-D — Refactor prosecutor + verify-claims around public interface
04B-E — Consumer / SoT / preflight integration
04B-F — Regression harness
04B-G — Target runtime smoke + project doctor
04B-H — Runtime closeout + stable checkpoint
```

### Important split

04B-B và 04B-C phải là hai change units khác nhau:

- B = artifact/taxonomy representation;
- C = relation-level bridge behavior.

Không trộn để nếu regression xảy ra còn biết do schema hay do reasoning behavior.

---

## 6. ACCEPTANCE OF 04A

04A COMPLETE nếu:

- audit artifacts đủ A→H;
- runtime Evidence bất biến;
- module decision có evidence;
- `SYNTHESIS` không auto-promote;
- M-004 không auto-promote;
- preflight/schema enforcement drift được ghi rõ;
- 04B có bounded task plan.

**All conditions satisfied.**

```text
PHASE 4A: COMPLETE
EVIDENCE AUDIT: VERIFIED
EVIDENCE RUNTIME: UNCHANGED
PHASE 4B GATE: CLEARED
```

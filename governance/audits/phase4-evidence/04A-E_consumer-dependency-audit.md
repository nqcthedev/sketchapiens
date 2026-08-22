# 04A-E — CONSUMER & DEPENDENCY AUDIT — KIỂM CONSUMER VÀ PHỤ THUỘC EVIDENCE

> **Mode:** READ-ONLY
> **Mục tiêu:** map ai gọi Evidence, qua interface nào, artifact nào, và chỗ nào còn deep-link / generation drift.

---

## 1. CONSUMER MAP

### C-01 — `CLAUDE.md` control plane

Always-on rules hiện giữ hai Evidence guardrail cấp project:

- mọi factual sentence thêm sau evidence gate phải rerun;
- suy diễn của tác giả nguồn phải được attribution rõ, không kể như fact trực tiếp.

`CLAUDE.md` route command `/verify-claims` nhưng không chứa full Evidence theory.

**Assessment:** đúng vai control-plane, nhưng wording phải về sau trỏ canonical Evidence contract thay vì tự mở rộng taxonomy.

### C-02 — `/new-video`

`new-video/SKILL.md` tạo lifecycle mới và copy:

```text
templates/claim-ledger.md
→ videos/SKA-NNNN-<slug>/02-research/claim-ledger.md
```

**Dependency type:** artifact template dependency.

### C-03 — `/verify-claims`

Public command hiện gọi thẳng:

```text
evidence-prosecutor
```

và ghi vào claim ledger.

**Dependency type:** direct implementation dependency vào agent.

Nếu sau Phase 4 Evidence có public module/interface, đây là consumer chính cần migration.

### C-04 — `/audit-script`

Audit command cũng gọi thẳng `evidence-prosecutor` với context riêng.

**Dependency type:** direct implementation dependency.

Điểm tốt: context budget sạch và role boundary đã rõ.
Điểm yếu: nếu Evidence behavior được refactor, audit-script phải biết implementation name thay vì chỉ contract.

### C-05 — `/apply-review`

Không gọi prosecutor trực tiếp.
Nó gọi public workflow `/verify-claims` nếu factual content đổi.

**Dependency type:** public workflow dependency — sạch hơn.

### C-06 — Writer

Writer không mở raw source trong normal write.
`evidence-expression.md` nhận resolved support/limitation/provenance và chỉ wording.

**Dependency type:** conceptual/public handoff; không deep-link private file của Evidence.

### C-07 — Story Engine

Story Engine chỉ flag Narrative Overreach và yêu cầu Evidence verdict khi factual status ảnh hưởng.

**Dependency type:** conceptual/public handoff; sạch.

### C-08 — `evidence-prosecutor`

Agent trực tiếp phụ thuộc vào:

- narration;
- claim ledger;
- source access via tools.

Nó hiện vừa là reviewer implementation vừa gần như semantic authority.

### C-09 — `templates/claim-ledger.md`

Được `new-video` copy thành runtime artifact.
Sau khi copy, video artifact có thể sống lâu hơn canonical template version.

**Dependency type:** generated artifact contract.

### C-10 — `schemas/claim-ledger.schema.json`

Schema tồn tại ở shared root và định nghĩa machine shape.

**Important finding:** `project_doctor.py` hiện chỉ parse tất cả JSON schemas để bảo đảm JSON hợp lệ; nó **không validate claim-ledger artifacts against `claim-ledger.schema.json`**.

Nói cách khác:

> schema tồn tại nhưng chưa thấy deterministic runtime consumer thực sự enforce ledger shape.

Đây là tool/guardrail gap, không phải semantic Evidence defect.

---

## 2. PRE-FLIGHT GENERATION DRIFT

`tools/preflight.py` là current first-command gate cho mọi video work.
Nhưng Evidence gate của nó vẫn thuộc legacy generation:

```text
moneo = has("MONEO_*.md")
Cổng 3 = regex đếm DOI/journal citation trong MONEO
PASS khi n_doi >= 3
```

Trong khi lifecycle mới `/new-video` tạo:

```text
02-research/claim-ledger.md
```

và `/verify-claims` cũng ghi vào path đó.

### Drift

New architecture:

```text
videos/SKA-.../02-research/claim-ledger.md
```

Legacy preflight:

```text
videos/<dir>/MONEO_*.md
```

Preflight hiện không kiểm:

- claim ledger tồn tại ở canonical new path;
- ledger conforms schema;
- ledger lock status;
- ledger được verify against current narration;
- blocking evidence verdict còn hay không.

Nó chỉ kiểm “có >=3 citation-shaped strings trong MONEO”.

### Classification

**Integration debt — deterministic control-plane drift.**

Không sửa trong 04A.
Phase 4G/Phase 7 phải quyết owner và timing; nhưng Phase 4 contract không được tuyên bố evidence gate end-to-end stable nếu preflight vẫn chỉ hiểu artifact generation cũ.

---

## 3. DEPENDENCY GRAPH HIỆN TẠI

```text
CLAUDE.md
   │
   ├── /new-video ─────→ template claim-ledger
   │                         │
   │                         ▼
   │                  video claim-ledger
   │                         ▲
   ├── /verify-claims ─→ evidence-prosecutor ─→ sources
   │
   ├── /audit-script ──→ evidence-prosecutor
   │
   └── /apply-review ──→ /verify-claims

Story Engine ──handoff──→ [Evidence capability]
Writer       ←─verdict── [Evidence capability]

claim-ledger.schema.json
   └── currently type declaration; no observed project_doctor validation of artifact

tools/preflight.py
   └── legacy MONEO citation-count gate, parallel to new ledger flow
```

---

## 4. CLEAN DEPENDENCIES

### Writer → Evidence

Boundary đúng: Writer không tự verdict.

### Story → Evidence

Boundary đúng: Story flag symptom, Evidence phán support.

### Apply-review → Verify

Editor dùng public workflow, không gọi private agent.

### Audit context isolation

Evidence reviewer không nhận retention/prose theory.

---

## 5. DEPENDENCY SMELLS

### DEP-D01 — Two consumers call agent implementation directly

`verify-claims` và `audit-script` biết exact agent `evidence-prosecutor`.

Nếu Phase 4 tạo contract/public interface, direct caller count chứng minh need cho stable API surface.

### DEP-D02 — Template acts as semantic authority and generated artifact source

Template vừa render artifact vừa lặp evidence policy.
Generated copies có thể stale khi canonical semantics đổi.

### DEP-D03 — Schema has no observed enforcement consumer

Machine type exists, but project doctor chỉ parse JSON schema file, không validate actual ledger.

### DEP-D04 — New lifecycle and preflight Evidence gates disagree on artifact convention

`claim-ledger.md` vs `MONEO_*.md`.

Đây là blocker tiềm năng cho V21 canary nếu không resolve trước end-to-end test.

### DEP-D05 — Legacy artifact names are hard-coded into prosecutor description

Evidence Prosecutor says it may read `MONEO_*.md`, `VERIFY_Anchors_*.md`, `templates/claim-ledger.md`.
Đó là compatibility behavior hữu ích nhưng làm agent biết historical storage details.

Phase 4 contract nên phân biệt:

- canonical new-video input;
- legacy compatibility input;
- test/history input.

### DEP-D06 — No explicit Evidence result artifact independent from mutable ledger

Audit-script outputs review table; verify-claims writes ledger.
Chưa có canonical run/report provenance rõ cho “verdict này đến từ lần prosecutor nào”.

Không nhất thiết cần artifact mới, nhưng 04A-G phải quyết traceability model.

---

## 6. MODULE-SHAPE SIGNAL

Architecture contract nói domain nên thành module nếu có phần lớn:

1. responsibility riêng;
2. workflow riêng;
3. knowledge đủ lớn;
4. nhiều consumer;
5. cần context isolation;
6. public interface độc lập.

04A-E evidence:

| Signal | Hiện trạng |
|---|---|
| responsibility riêng | YES — factual verdict/bridge/support |
| workflow riêng | YES — verify/rerun/lock |
| knowledge đủ lớn | YES-ish — taxonomy, provenance, transfer, bridge, synthesis |
| nhiều consumer | YES — Writer, Story, audit, apply-review, new-video/control plane |
| context isolation | YES — prosecutor cần source/ledger, reviewer khác không cần |
| public interface độc lập | CURRENTLY MISSING but clearly describable |

**Audit inference:** evidence domain có tín hiệu rất mạnh để thành project-local module riêng.

Đây vẫn chưa phải quyết định tạo skill; quyết định ở 04A-G sau failure-mode audit.

---

## 7. CHECK 04A-E

PASS nếu:

- consumer graph bao phủ new-video/verify/audit/apply/Writer/Story/control-plane;
- phát hiện preflight generation drift và schema enforcement gap;
- không sửa preflight/project_doctor/runtime trong audit;
- module-shape chỉ là evidence-backed signal, chưa implementation decision.

**Result: PASS.**

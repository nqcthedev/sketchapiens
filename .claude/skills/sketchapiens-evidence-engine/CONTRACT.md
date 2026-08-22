# SKETCHAPIENS EVIDENCE ENGINE — HỢP ĐỒNG CỖ MÁY BẰNG CHỨNG

> **Status:** ACTIVE CONTRACT
> **Phase:** 04B-A
> **Scope:** factual/source/bridge verification for Sketchapiens.
> **Boundary:** contract semantics only. This file does not discover topics, write narration, edit scripts, or decide story structure.

---

## 1. PURPOSE — MỤC ĐÍCH

Evidence Engine trả lời câu hỏi:

> **Bằng chứng hiện có thật sự cho phép kịch bản nói điều gì, ở mức chắc nào, và đường nối nhân quả/tổng hợp nào còn nợ bằng chứng?**

Engine phải bảo vệ hai thứ cùng lúc:

1. không để prose/story nói mạnh hơn nguồn;
2. không làm mất các project inference hợp lệ chỉ vì không có một paper đơn lẻ nói nguyên thesis.

---

## 2. OWNERSHIP — QUYỀN SỞ HỮU

Evidence Engine sở hữu:

### E-OWN-01 — Evidence semantic contract

Bốn factual verdict canonical:

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

Không consumer nào được tự tạo taxonomy cạnh tranh.

### E-OWN-02 — Claim ↔ source fit

Engine phán:

- source thật sự nói gì;
- claim nói gì;
- number / denominator / population / timeframe có khớp không;
- mức certainty có vượt source không.

### E-OWN-03 — Provenance

Engine phân biệt tối thiểu:

- full text / primary source;
- abstract;
- snippet;
- secondary source;
- unverified provenance.

Không mở được support đủ cho claim cần dùng → không được giả thành verified.

### E-OWN-04 — Transfer / scope fit

Engine phán transfer như:

- modern → prehistoric;
- animal → human;
- one population → universal humans;
- one climate/context → another;
- interpretation → asserted intent/event.

### E-OWN-05 — Causal Proof Fit — Độ khớp bằng chứng–nhân quả

Canonical diagnostic question:

> **Evidence nodes can each be true while the narrative edge between them is unsupported. Verdict the edge, not only the nodes.**

Tiếng Việt:

> **Các fact nút có thể đều đúng nhưng đường nối mà câu chuyện dựng giữa chúng vẫn không được chứng minh. Evidence phải phán cả đường nối, không chỉ từng nút.**

M-004 vẫn là candidate R&D. Contract này sở hữu capability relation-level; nó không tự promote tên mechanism M-004 thành luật kênh.

### E-OWN-06 — Project inference / synthesis semantics

Một project synthesis có thể là `INFERENCE`.

`SYNTHESIS` không phải verdict thứ năm trong Phase 04B-A.

Engine phải có khả năng phân biệt:

- source-author inference;
- project inference;
- multi-source synthesis;
- unsupported synthesis.

Field/enum representation cụ thể thuộc 04B-B, không được suy từ file này trước task đó.

### E-OWN-07 — Lockability

Engine trả semantic outcome:

```text
LOCKABLE
NOT_LOCKABLE
```

kèm evidence debt còn lại.

Evidence lock chỉ có nghĩa đối với exact input / immutable script version đã verify.
Engine không tự đặt owner approval hoặc video lifecycle state.

---

## 3. NON-OWNERSHIP — KHÔNG THUỘC EVIDENCE

Evidence Engine không sở hữu:

- topic discovery / market research;
- chapter order / structural evidence placement;
- retention, title, thumbnail;
- narration voice/prose;
- editing approved script;
- owner classification;
- analytics causality;
- mechanism promotion.

### Neighbor boundaries

```text
Research / Topic
→ discovers material broadly

Evidence Engine
→ verifies claim/source/bridge fit

Story Engine
→ decides structural placement; flags Narrative Overreach symptom

Writer
→ expresses resolved verdict naturally

Editor / apply-review
→ mutates script only after owner classification
```

---

## 4. INPUT CONTRACT

Normal verification may receive:

- exact narration or immutable script version;
- claim ledger;
- relevant primary/full sources when available;
- source metadata/provenance;
- exact bridge/thesis/dependency when relation-level review is needed.

It must not require by default:

- competitor corpus;
- retention theory;
- Writer voice theory;
- thumbnail system;
- mechanism lab;
- analytics.

Missing input must be reported as missing/UNVERIFIED, not filled from convenient memory.

---

## 5. OUTPUT CONTRACT

Evidence verification returns, as applicable:

```text
CLAIM VERDICTS
BRIDGE / SYNTHESIS VERDICTS
PROVENANCE / TRANSFER WARNINGS
BLOCKING EVIDENCE DEBTS
LOCKABILITY
TRACEABILITY TO EXACT INPUT / SCRIPT VERSION
```

It must not return unsolicited:

- rewritten prose;
- retention score;
- chapter redesign;
- packaging concepts.

---

## 6. VERDICT SEMANTICS — BASELINE

### DIRECT

The cited support says the material claim at the needed scope/certainty.

DIRECT does not mean “scientifically certain forever”. It means the claim does not require the project to add a material inferential bridge beyond the support being cited.

### INFERENCE

Evidence supports components/premises, but the project or cited author draws a conclusion not directly measured/stated as the raw fact.

Inference can be valid and useful. It must preserve epistemic distance.

### SPECULATION

Evidence does not currently warrant a resolved answer. The script may use it only when clearly framed as uncertainty/question/possibility and when its role is justified.

### STORY_DEVICE

Reconstruction/composite/rhetorical setup that is not itself presented as historical measurement or recorded event.

A story device can still hide factual claims. Any concrete factual component inside it remains verifiable.

---

## 7. RELATION-LEVEL VERDICT — PRINCIPLE

Evidence verification is not complete when all nodes are individually true.

For a material bridge, ask:

```text
What relationship is the narration claiming?
Which source(s) support each node?
Which source or warrant supports the edge?
Does the conclusion require a transfer, causal leap, denominator swap,
optimization claim, historical-intent claim, or certainty increase?
```

A beautiful narrative bridge is not evidence.

The exact machine representation of relation verdicts is deferred to 04B-B/04B-C.

---

## 8. PROVENANCE & TRACEABILITY INVARIANTS

1. Snippet-only support must remain visibly unverified for claims that require primary/full verification.
2. Source-author interpretation must not be narrated as raw measurement.
3. Project synthesis must not be attributed to a source that never made it.
4. Verification must bind to exact script/version/input; a mutable `current` pointer alone is not historical proof.
5. A new factual version invalidates automatic inheritance of lockability unless a deterministic comparison proves no factual change under an approved future design.
6. Historical verdict remains historical; rerun creates new provenance rather than rewriting the old run.

---

## 9. CONTEXT PROFILES

### VERIFY_CLAIMS

Allowed:

- exact script/version;
- ledger;
- relevant sources;
- Evidence public contract and only-needed supporting references.

### BRIDGE_REVIEW

Allowed:

- exact nodes/dependencies;
- exact bridge/thesis;
- relevant sources;
- needed Evidence references.

No full Story Engine theory required.

### EVIDENCE_AUDIT

May additionally load prior verdict/history to inspect drift.

### WRITER_HANDOFF

Writer receives only what it needs to speak accurately:

- verdict;
- allowed certainty;
- attribution/limitation;
- provenance detail necessary for narration.

### STORY_HANDOFF

Story receives:

- factual status;
- supported / qualified / unsupported bridge signal;
- evidence debt.

Story does not re-open sources just to issue a competing factual verdict.

### R&D / REGRESSION

Historical VERIFY/MONEO and Egypt E-01→E-06 may be used here.
Normal writing/review does not default-load them.

---

## 10. EXISTING SURFACES — TARGET ROLE

### evidence-prosecutor

Execution/reviewer persona consuming this contract. It is not the canonical owner of semantic theory after migration completes.

### /verify-claims

Workflow/orchestration wrapper: load inputs → invoke Evidence verification → persist/report result → report lockability.

### claim-ledger schema

Machine-shape authority. It encodes the artifact contract but does not replace semantic explanation in Evidence Engine.

### claim-ledger template

Human bootstrap/rendering surface. It is not co-owner of taxonomy semantics.

### Story / Writer consumers

Consume stable handoffs; do not deep-link into private Evidence R&D.

---

## 11. CHANGE FIREWALL

This contract does not authorize:

- a fifth `SYNTHESIS` verdict;
- Evidence Fit quotas;
- automatic mechanism promotion;
- migration of every legacy V17–V20 artifact;
- rewriting old historical verification records;
- stronger factual claims to improve story flow.

Any taxonomy/rule promotion still follows project governance and owner authority.

---

## 12. STOP CONDITION

Evidence work is done for an exact input when:

- every material factual claim has a usable verdict/provenance state;
- material relation-level bridges are supported, qualified, or explicitly blocked;
- transfer/scope debt is visible;
- unresolved blocking debt is listed;
- lockability is explicit;
- traceability to exact input exists.

Do not continue adding bureaucracy once these conditions are satisfied.

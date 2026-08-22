# 04A-G — EVIDENCE CONTRACT PROPOSAL — ĐỀ XUẤT HỢP ĐỒNG EVIDENCE

> **Status:** AUDIT PROPOSAL — chưa phải runtime contract
> **Mode:** READ-ONLY
> **Mục tiêu:** chốt target ownership/module shape để 04B triển khai có kiểm soát.

---

## 1. MODULE-SHAPE DECISION PROPOSAL

### Audit verdict

**Đề xuất tạo project-local skill riêng:**

```text
.claude/skills/sketchapiens-evidence-engine/
```

### Vì sao đủ điều kiện

Theo Architecture Contract, Evidence domain có:

1. **responsibility riêng:** factual/source/bridge verdict;
2. **workflow riêng:** verify → verdict → evidence debt → lockability → rerun;
3. **knowledge riêng:** provenance, taxonomy, transfer, inference, causal bridge, synthesis;
4. **nhiều consumer:** Writer, Story, audit-script, apply-review, verify-claims, new-video/control plane;
5. **context isolation:** cần sources/ledger nhưng không cần retention/prose/corpus;
6. **public interface độc lập:** có thể mô tả input/output/boundary rõ.

Đây không phải tạo module “cho sơ đồ cân đối”. Audit đã tìm thấy direct-agent dependencies và semantic duplication thật.

---

## 2. TARGET OWNERSHIP

### Evidence Engine OWNS

#### E-OWN-01 — Evidence semantic contract

Ý nghĩa canonical của factual verdict:

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

#### E-OWN-02 — Claim ↔ source fit

- source nói gì;
- claim nói gì;
- population/timeframe/number/denominator có khớp không;
- certainty có vượt source không.

#### E-OWN-03 — Provenance requirements

- full text / abstract / snippet / secondary source;
- `UNVERIFIED` boundary;
- source author conclusion vs raw measurement.

#### E-OWN-04 — Transfer/scope verdict

- modern → prehistoric;
- animal → human;
- one population → universal;
- one context/climate → another;
- interpretation → asserted historical intent.

#### E-OWN-05 — Causal Proof Fit

Canonical diagnostic question:

> **Evidence nodes can each be true while the narrative edge between them is unsupported. Verdict the edge, not only the nodes.**

Tiếng Việt:

> **Các fact nút có thể đều đúng nhưng đường nối nhân quả mà câu chuyện dựng giữa chúng vẫn không được chứng minh. Evidence phải phán cả đường nối, không chỉ từng nút.**

Đây là target destination phù hợp nhất của M-004 nếu 04B regression chứng minh behavior hữu ích.
M-004 **chưa promoted ở 04A**.

#### E-OWN-06 — Project inference / synthesis semantics

Evidence Engine quyết:

- component nào supported;
- project synthesis có đủ warrant không;
- conclusion được phép ở mức certainty nào.

Evidence Engine **không quyết story có nên dùng synthesis đó vì retention hay không**.

#### E-OWN-07 — Lockability semantics

Engine trả:

```text
LOCKABLE
NOT_LOCKABLE
```

và evidence debt còn lại.

Engine không tự quyết owner approval hay video lifecycle state.

---

## 3. EVIDENCE ENGINE DOES NOT OWN

### Source discovery for topic strategy

Research/topic module vẫn sở hữu discovery rộng.
Evidence Engine được mở source để **verify claim**, không biến thành topic researcher.

### Structural evidence placement

Story Engine sở hữu:

- evidence xuất hiện ở đâu;
- trả structural question nào;
- Narrative Overreach symptom.

### Prose wording

Writer sở hữu cách diễn đạt verdict đã resolved.

### Retention / title / thumbnail

Không thuộc Evidence.

### Editing approved script

Evidence reviewer không rewrite.
Editor `/apply-review` tạo version mới sau owner classification.

### Analytics causality

Không suy “claim này làm video nổ”.

---

## 4. ROLE OF EXISTING SURFACES AFTER 04B

### `evidence-prosecutor`

Target role:

> **review agent / execution persona**, không còn là nơi duy nhất chứa semantic contract.

Nó nên consume Evidence Engine public interface/contract.

### `/verify-claims`

Target role:

> **command/workflow wrapper**.

Nó orchestration:

```text
load narration + ledger
→ invoke Evidence verification
→ persist result
→ report lockability
→ mark/run provenance as designed in 04B
```

Không duplicate full taxonomy theory.

### `templates/claim-ledger.md`

Target role:

> human rendering/bootstrap template.

Không là co-owner của verdict semantics.

### `schemas/claim-ledger.schema.json`

Target role:

> machine shape/type authority.

Nó encode contract nhưng không chứa long-form Evidence theory.

### Writer evidence-expression

Giữ consumer boundary; chỉ sync public Evidence terms nếu cần.

### Story evidence-in-story

Giữ Narrative Overreach symptom + handoff; không copy Evidence theory.

### `/audit-script`

Target: call prosecutor/engine through stable Evidence interface, không cần biết private references.

### `/apply-review`

Giữ rerun dependency qua `/verify-claims`.

### `tools/preflight.py`

Phải được sync với new lifecycle Evidence artifact trước V21 canary.
Không còn được coi `MONEO_* + >=3 citation-looking strings` là bằng chứng đủ của canonical evidence gate cho SKA-* videos.

Legacy compatibility có thể giữ riêng.

---

## 5. TAXONOMY PROPOSAL

### Keep top-level verdicts

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

Không có audit evidence đủ để thêm verdict thứ năm.

### `SYNTHESIS` proposal

**Không phải top-level factual verdict.**

Target interpretation:

> derivation/provenance mode của một project inference.

Ví dụ:

```text
kind: INFERENCE
reasoning/derivation: MULTI_SOURCE_SYNTHESIS
```

Tên field/enum chính xác để 04B-B quyết sau fixture design; proposal này khóa **dimension**, không khóa implementation spelling.

---

## 6. TARGET LEDGER SEMANTIC DIMENSIONS

Ledger tương lai cần biểu diễn được tối thiểu:

```text
claim identity
factual verdict kind
source provenance
source says exact content
multiple source/dependency refs when needed
project inference vs source-author inference
transfer/scope flags
bridge/synthesis dependency
failure type
severity/blocking status
verification status
script version/ref verified against
lockability / stale state
notes/rationale
```

Không nhất thiết mỗi dimension thành top-level field.
04B-B phải chọn shape tối thiểu, tránh schema phình.

---

## 7. FAILURE TYPE VS SEVERITY PROPOSAL

Current `overreach 0–3` trộn hai dimension.

Target concept:

```text
FAILURE TYPE
- source mismatch
- denominator/population drift
- certainty inflation
- unsupported causal bridge
- unsupported synthesis
- transfer/scope leap
- snippet/unverified provenance
- factual claim hidden in story device
...

SEVERITY / BLOCKING
- non-blocking note
- needs qualification
- blocking / needs rewrite
```

Không khóa enum ở 04A.
Regression 04B-F phải chứng minh taxonomy không tạo bureaucracy lớn hơn giá trị.

Legacy `0–3` có thể cần compatibility/migration mapping, không xóa vội.

---

## 8. BRIDGE / SYNTHESIS REPRESENTATION PROPOSAL

Minimal conceptual graph:

```text
C1 DIRECT ← S1
C2 DIRECT ← S2
C3 DIRECT ← S3

I1 INFERENCE
  depends_on: C1 + C2 + C3
  derivation: MULTI_SOURCE_SYNTHESIS

B1 BRIDGE VERDICT
  relationship being claimed: C1/C2 → I1
  support: supported / qualified / unsupported
```

Không bắt mọi video phải dựng graph phức tạp.
Chỉ cần relation first-class khi thesis/causal bridge lớn thực sự phụ thuộc nhiều claim.

---

## 9. LOCK / TRACEABILITY PROPOSAL

Current `locked: boolean` chưa bind rõ với script version.

Target invariant:

> Evidence lock chỉ có nghĩa đối với **một immutable script version / exact narration snapshot**.

Phase 4B nên cân nhắc bind verification với:

- immutable `03-script/versions/vNNN.md` ref;
- optional content hash/run provenance nếu hữu ích.

Khi factual content chuyển sang version mới:

```text
prior evidence result remains historical
new version = requires verification before lockability is inherited
```

Không dùng mutable “current” pointer làm duy nhất proof rằng exact text đã verify.

---

## 10. CONTEXT PROFILES

### `VERIFY_CLAIMS`

Được đọc:

- exact narration/version;
- claim ledger;
- relevant sources/full text;
- Evidence contract/references cần thiết.

Không default-load:

- retention theory;
- Writer voice theory;
- competitor corpus;
- mechanism lab;
- thumbnail/analytics.

### `EVIDENCE_AUDIT`

Giống VERIFY nhưng có thể đọc prior verdict/history khi audit drift.

### `BRIDGE_REVIEW`

Chỉ cần:

- claims/dependencies;
- exact bridge/thesis;
- relevant source evidence.

Không cần full Story Engine theory.

### `WRITER_HANDOFF`

Writer chỉ cần:

- verdict;
- allowed certainty;
- attribution/limitation;
- provenance detail cần cho narration.

Không cần raw Evidence R&D.

### `STORY_HANDOFF`

Story chỉ cần:

- factual status;
- unsupported/qualified bridge flags;
- evidence debt.

Không được tự phán lại nguồn.

### `R&D / REGRESSION`

Được mở Egypt E-01→E-06 và historical VERIFY/MONEO cases.
Normal runtime không load chúng.

---

## 11. TARGET OUTPUT

Evidence verification nên trả tối thiểu:

```text
CLAIM VERDICTS
BRIDGE / SYNTHESIS VERDICTS where relevant
PROVENANCE / TRANSFER WARNINGS
BLOCKING EVIDENCE DEBTS
LOCKABILITY
TRACEABILITY TO SCRIPT VERSION / INPUT
```

Không trả:

- rewrite đẹp hơn;
- retention score;
- chapter order;
- title/thumbnail ideas.

---

## 12. 04B TASK SHAPE RECOMMENDATION

```text
04B-A — Create Evidence Engine contract/public module skeleton
04B-B — Canonical semantics + minimal ledger/schema representation
04B-C — Causal Proof Fit / bridge verdict implementation
04B-D — Refactor prosecutor + verify-claims around public interface
04B-E — Consumer + preflight/SoT integration
04B-F — Regression harness (historical + Egypt-derived synthetic traps + valid synthesis controls)
04B-G — Target runtime smoke + project doctor
04B-H — Runtime closeout + stable checkpoint
```

Important:

- 04B-A should not alter verdict behavior beyond ownership/routing;
- 04B-B and 04B-C must remain separable so taxonomy migration and bridge behavior are not one untraceable change;
- preflight integration may be a bounded deterministic subtask inside 04B-E or separate guard task if scope expands.

---

## 13. DECISION SUMMARY

### Proposed YES

Create `sketchapiens-evidence-engine` as a real project-local module in Phase 4B.

### Proposed NO

Do not:

- add `SYNTHESIS` as fifth verdict;
- retire Evidence Prosecutor;
- make Story Engine judge sources;
- make Writer see Evidence R&D;
- create Evidence Fit quotas;
- migrate all V17–V20 evidence artifacts into new schema.

### Candidate M-004

Remain `candidate` through 04A.
04B regression should determine whether its narrowed identity survives:

> verdict the narrative edge, not only true nodes.

---

## 14. CHECK 04A-G

PASS if proposal:

- has clear ownership/non-ownership;
- justifies module using audit evidence;
- preserves current four-label verdict baseline;
- treats synthesis as separate dimension unless tests disprove;
- addresses bridge, traceability, preflight drift and legacy compatibility;
- changes no runtime.

**Result: PASS.**

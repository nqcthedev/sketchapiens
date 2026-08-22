---
name: sketchapiens-evidence-engine
description: Public interface của Evidence Engine. Dùng để verify claim/source/bridge fit, provenance, transfer và lockability. Không viết lại kịch bản, không chấm retention, không quyết cấu trúc.
---

# Sketchapiens Evidence Engine — Cỗ máy bằng chứng

> Canonical semantics: `CONTRACT.md`.
> Machine ledger semantics: `references/ledger-semantics.md` khi task cần tạo/đọc/validate ledger.
> Relation-level behavior: `references/causal-proof-fit.md` chỉ khi có material causal/synthesis bridge.

## Khi dùng

Dùng khi cần:

- verify factual claim với nguồn;
- phân loại `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE`;
- kiểm population / timeframe / denominator / certainty;
- kiểm transfer hiện đại → tiền sử, animal → human, context → context;
- kiểm project inference / synthesis;
- kiểm causal bridge khi từng fact có thể đúng nhưng edge chưa được support;
- quyết `LOCKABLE / NOT_LOCKABLE` cho exact input.

Không dùng để:

- chọn đề tài;
- tìm angle viral;
- quyết chapter order;
- viết prose;
- sửa script;
- mở competitor corpus;
- promote mechanism.

## Public workflow

```text
1. Identify exact input/version
2. Load claim ledger + relevant source material
3. Verify claim nodes
4. Verify material bridges/syntheses when relevant
5. Record provenance / transfer / unresolved debt
6. Return lockability + traceability
```

## Progressive loading — Nạp theo nhu cầu

### Claim/ledger task

Load:

- `CONTRACT.md`;
- `references/ledger-semantics.md`;
- exact script/ledger/source material.

### Material bridge / synthesis task

Load thêm:

- `references/causal-proof-fit.md`.

Không mở reference bridge chỉ vì nó tồn tại. Chỉ mở khi narration thật sự có relation cần phán.

### Historical/R&D regression

Chỉ test/audit mode mới được mở historical VERIFY/MONEO hoặc Egypt R&D case.
Normal runtime không load chúng.

## Required output

Tối thiểu:

```text
CLAIM VERDICTS
BRIDGE / SYNTHESIS VERDICTS where relevant
PROVENANCE / TRANSFER WARNINGS
BLOCKING EVIDENCE DEBTS
LOCKABILITY
TRACEABILITY
```

Không rewrite narration trong Evidence review.

## Context rule — Progressive disclosure

Được đọc khi verify:

- exact narration/version;
- canonical machine claim ledger;
- relevant sources;
- `CONTRACT.md`;
- supporting Evidence references đúng task.

Không default-load:

- `2_KHO_BANGHI/**`;
- competitor teardown;
- Writer voice theory;
- retention theory;
- Story Engine mechanism lab;
- thumbnail/analytics;
- historical Evidence corpus trừ regression/audit mode.

## Relation-level trigger

Không phải mọi transition đều cần bridge object.

Bật Causal Proof Fit khi relationship **material** và narration đang làm một trong các việc như:

- `A causes B`;
- event → system function;
- components → optimization/adaptation;
- one context/population → another;
- interpretation → intent;
- separate statistics → combined conclusion;
- multi-source synthesis → thesis.

Khi đó phải phán **edge** riêng, không chỉ node facts.

## Neighbor handoffs

### Story Engine → Evidence

Story có thể flag `Narrative Overreach` hoặc một bridge cần proof.
Evidence mở nguồn và issue verdict.

### Evidence → Story

Trả factual status + bridge support/debt.
Không quyết story nên giữ/bỏ vì retention.

### Evidence → Writer

Trả allowed certainty + attribution/limitation cần thiết.
Writer chỉ diễn đạt verdict đã resolved.

### Editor → Evidence

Factual claim mới/đổi sau review phải rerun verification.
Evidence không tự edit.

## Hard boundaries

- `SYNTHESIS` không phải verdict thứ năm.
- Không dùng hedge để cứu unsupported claim.
- Không gọi project inference là source finding.
- Không coi node facts đúng là đủ proof cho edge.
- Không biến Causal Proof Fit thành quota/checklist cho mọi câu.
- Không kế thừa evidence lock qua script version mới chỉ vì `current` pointer đổi.
- Không tự thay factual verdict để story đẹp hơn.

## Current compatibility

Trong Phase 04B-C:

- `evidence-prosecutor` vẫn là execution persona cũ và chưa được refactor sang public interface;
- `/verify-claims` vẫn là workflow wrapper cũ;
- canonical machine schema/template đã tồn tại nhưng consumer migration chờ 04B-D/E.

Consumer migration chỉ diễn ra ở 04B-D/04B-E.

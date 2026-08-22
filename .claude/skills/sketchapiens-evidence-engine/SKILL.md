---
name: sketchapiens-evidence-engine
description: Public interface của Evidence Engine. Dùng để verify claim/source/bridge fit, provenance, transfer và lockability. Không viết lại kịch bản, không chấm retention, không quyết cấu trúc.
---

# Sketchapiens Evidence Engine — Cỗ máy bằng chứng

> Canonical semantics: `CONTRACT.md`.
> Phase 04B-A chỉ khóa public interface. Representation chi tiết của ledger/bridge được triển khai ở các task sau.

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

Normal run chỉ load thứ task cần.

Được đọc khi verify:

- exact narration/version;
- claim ledger;
- relevant sources;
- `CONTRACT.md`;
- supporting Evidence references được route rõ ở các task sau.

Không default-load:

- `2_KHO_BANGHI/**`;
- competitor teardown;
- Writer voice theory;
- retention theory;
- Story Engine mechanism lab;
- thumbnail/analytics;
- historical Evidence corpus trừ regression/audit mode.

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

- Không biến `SYNTHESIS` thành verdict thứ năm trong task này.
- Không dùng hedge để cứu unsupported claim.
- Không gọi một inference là source finding nếu source không nói thế.
- Không coi node facts đúng là đủ proof cho edge.
- Không kế thừa evidence lock qua script version mới chỉ vì `current` pointer đổi.
- Không tự thay factual verdict để story đẹp hơn.

## Current compatibility

Trong Phase 04B-A:

- `evidence-prosecutor` vẫn là execution persona hiện hành;
- `/verify-claims` vẫn là workflow wrapper hiện hành;
- schema/template cũ chưa đổi ở task A.

Các consumer chưa được migrate sang module này cho tới 04B-D/04B-E.

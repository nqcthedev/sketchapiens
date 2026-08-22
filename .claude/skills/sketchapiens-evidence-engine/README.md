# Sketchapiens Evidence Engine — Cỗ máy bằng chứng

Module này là public home của factual/source/bridge verification trong Sketchapiens.

## Public files

- `CONTRACT.md` — canonical semantic ownership và boundary.
- `SKILL.md` — runtime public interface.
- `references/` — supporting knowledge chỉ load khi task cần, được thêm ở các task 04B sau.
- `tests/` — regression harness, được thêm ở 04B-F.

## Current Phase 04B-A state

Module skeleton đã tồn tại nhưng consumer migration chưa hoàn tất.

Hiện tại:

```text
Evidence semantics target → CONTRACT.md
Execution persona hiện hành → .claude/agents/evidence-prosecutor.md
Workflow wrapper hiện hành → .claude/skills/verify-claims/SKILL.md
Machine ledger shape hiện hành → schemas/claim-ledger.schema.json
Human ledger bootstrap → templates/claim-ledger.md
```

04B-B sẽ xử lý artifact/taxonomy representation tối thiểu.
04B-C sẽ xử lý relation-level bridge reasoning.
04B-D/E mới migrate prosecutor/workflow/consumers quanh public interface.

## Non-goals

Module này không trở thành:

- topic research engine;
- Story Engine thứ hai;
- Writer/editor;
- competitor-analysis store;
- kho toàn bộ historical VERIFY/MONEO;
- nơi promote creative mechanism tự động.

## Core principle

> **Các fact riêng lẻ đúng chưa đủ. Nếu narration dựng một relationship quan trọng giữa chúng, relationship đó cũng cần evidence warrant hoặc phải được hạ mức certainty.**

## Governance

Không observation/candidate nào tự trở thành canonical rule chỉ vì được nhắc trong Evidence R&D.
Mọi promotion vẫn theo `governance/CHANGE_POLICY.md` và owner decision.

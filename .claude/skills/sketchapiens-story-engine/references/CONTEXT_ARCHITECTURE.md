# `CONTEXT_ARCHITECTURE.md` — KIẾN TRÚC NGỮ CẢNH STORY ENGINE

> **Status — trạng thái:** implementation note — ghi chú triển khai của NEXT-02C.
>
> File này mô tả **context loading — cách tải ngữ cảnh**, không thay `CONTRACT.md` về ownership và không phải creative rule.

## Runtime principle — Nguyên tắc runtime

Claude Code chỉ nên mang theo **minimum useful context — lượng context hữu ích tối thiểu**.

```text
Always / preload:
SKILL.md

On demand:
structural-mechanisms.md
evidence-in-story.md
workflows.md

R&D only:
mechanism-lab.md
```

## Why — Vì sao

- `SKILL.md` được dùng làm entrypoint và có thể nằm lâu trong context sau khi skill được invoke.
- custom subagent dùng `skills:` nhận skill content ngay khi khởi động.
- supporting files cho phép giữ implementation detail ngoài entrypoint và chỉ đọc khi cần.

Do đó, theory không liên quan tới task hiện tại không được load chỉ vì nó nằm cùng module.

## Consumer matrix — Ma trận consumer

| Consumer | Default | On demand | Forbidden / avoid by default |
|---|---|---|---|
| Writer / Structure Mode | `SKILL.md` | structural mechanisms · workflows · evidence-in-story tùy task | Mechanism Lab |
| Viewer Retention Judge | `SKILL.md` + agent prompt | structural mechanisms chỉ khi ambiguity | evidence-in-story · Mechanism Lab · research ledger |
| Evidence Prosecutor | không cần Story Engine preload | narration/bridge do caller đưa | Mechanism Lab / structural theory nếu không cần |
| R&D / Postmortem | `SKILL.md` + `CONTRACT.md` | Mechanism Lab + evidence/corpus artifact | không dùng candidate như requirement |

## Load triggers — Điều kiện load

### `structural-mechanisms.md`
Load khi phải quyết:
- causal chain;
- transition;
- belief change;
- domain shift;
- macro progression.

### `evidence-in-story.md`
Load khi phải quyết:
- paper/site/experiment nên nằm ở đâu;
- evidence event;
- synthesis;
- causal bridge có nguy cơ Narrative Overreach.

### `workflows.md`
Load khi caller cần:
- Story Map;
- after-chapter check;
- structural review procedure;
- stop condition.

### `mechanism-lab.md`
Chỉ load khi:
- R&D mechanism;
- cross-corpus validation;
- postmortem;
- promote / merge / demote / reject decision.

## Anti-patterns — Cách làm sai

- preload mọi reference để "chắc ăn";
- reviewer đọc Mechanism Lab rồi đi tìm candidate trong mọi script;
- Story Engine đọc Evidence implementation chỉ để tự phán fact;
- duplicate toàn bộ mechanism definition vào consumer prompt;
- tách file tới mức một task phải đọc 7–10 reference mới làm được.

## Stop condition — Điều kiện dừng refactor context

Không tách thêm file chỉ để giảm byte.
Chỉ tách tiếp khi có ít nhất một lợi ích rõ:

- consumer khác nhau cần subset khác nhau;
- file có ownership khác;
- reference đủ lớn khiến preload lãng phí;
- testing/provenance cần boundary riêng.

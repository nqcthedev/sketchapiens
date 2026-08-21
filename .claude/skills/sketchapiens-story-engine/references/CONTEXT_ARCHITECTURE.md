# `CONTEXT_ARCHITECTURE.md` — KIẾN TRÚC NGỮ CẢNH STORY ENGINE

> **Status — trạng thái:** implementation note — ghi chú triển khai của NEXT-02C, cập nhật firewall ở NEXT-02D.
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

R&D only — đọc lifecycle trước data:
candidate-lifecycle.md
→ mechanism-lab.md
```

## Why — Vì sao

- `SKILL.md` được dùng làm entrypoint và có thể nằm lâu trong context sau khi skill được invoke.
- custom subagent dùng `skills:` nhận skill content ngay khi khởi động.
- supporting files cho phép giữ implementation detail ngoài entrypoint và chỉ đọc khi cần.
- candidate theory tạo **framework priming — mồi nhận thức** đặc biệt mạnh vì nó chưa được kiểm đủ.

Do đó, theory không liên quan tới task hiện tại không được load chỉ vì nó nằm cùng module.

## Consumer matrix — Ma trận consumer

| Consumer | Default | On demand | Forbidden / avoid by default |
|---|---|---|---|
| Writer / Structure Mode | `SKILL.md` | structural mechanisms · workflows · evidence-in-story tùy task | **candidate-lifecycle + Mechanism Lab** |
| Viewer Retention Judge | `SKILL.md` + agent prompt | structural mechanisms chỉ khi ambiguity | evidence-in-story · **candidate-lifecycle · Mechanism Lab** · research ledger |
| Evidence Prosecutor | không cần Story Engine preload | narration/bridge do caller đưa | candidate files / structural theory nếu không cần |
| R&D / Postmortem | `SKILL.md` + `CONTRACT.md` | **candidate-lifecycle trước → Mechanism Lab sau** + evidence/corpus artifact | không dùng candidate như requirement |
| Controlled Experiment | `SKILL.md` + explicit owner experiment brief | candidate-lifecycle + đúng candidate đang test | candidate khác không liên quan |

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

### `candidate-lifecycle.md`
Load **trước Mechanism Lab** khi:
- R&D mechanism;
- postmortem tạo/cập nhật mechanism;
- cross-corpus validation;
- controlled experiment;
- promotion / merge / park / reject decision.

### `mechanism-lab.md`
Chỉ load **sau candidate-lifecycle.md** khi task thật sự cần dữ liệu candidate:
- xem candidate hiện có;
- cập nhật evidence/counterexample/status;
- chuẩn bị promotion decision.

## Candidate firewall — Tường lửa ứng viên

Normal writing/review phải hoạt động như thể **không biết tên candidate cụ thể**.

Candidate chỉ được vượt firewall khi:

1. task hiện tại là R&D/postmortem; hoặc
2. owner mở explicit `Controlled Experiment — thử nghiệm có kiểm soát` cho một candidate cụ thể.

Ngay cả trong experiment:
- candidate là lens, không phải requirement;
- reviewer nên blind nếu test design không yêu cầu biết candidate;
- một case thành công không tự promote.

## Anti-patterns — Cách làm sai

- preload mọi reference để "chắc ăn";
- reviewer đọc Mechanism Lab rồi đi tìm candidate trong mọi script;
- writer đọc candidate chỉ để tìm một structure "hay hơn";
- postmortem nhảy từ một điểm analytics sang rule proposal;
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

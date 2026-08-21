# `sketchapiens-story-engine` — CỖ MÁY CẤU TRÚC CÂU CHUYỆN SKETCHAPIENS

> **Quy ước tên:** tên kỹ thuật/file giữ bằng English ASCII để Claude Code và đường dẫn ổn định. Ở tài liệu dành cho người đọc, **nghĩa tiếng Việt luôn ghi ngay bên cạnh ở lần xuất hiện đầu tiên**.

## Architecture — Kiến trúc module

Story Engine dùng **Progressive Disclosure — tải ngữ cảnh theo nhu cầu**:

```text
SKILL.md
public interface + context router
        ↓ khi cần
references/structural-mechanisms.md
references/evidence-in-story.md
references/workflows.md
        ↓ chỉ R&D
references/mechanism-lab.md
```

Mục tiêu: **ít context hơn, nhưng đúng context hơn**.
Không đọc mọi reference chỉ vì chúng tồn tại.

## Bản đồ file

| Tên kỹ thuật | Nghĩa tiếng Việt | Vai trò | Khi load |
|---|---|---|---|
| `CONTRACT.md` | **Hợp đồng Story Engine / hợp đồng module** | Nguồn chuẩn cho ownership, non-ownership, input/output, dependency direction, consumer boundary | Khi có ambiguity về ai sở hữu quyết định nào |
| `SKILL.md` | **Giao diện công khai / cửa vào runtime** | Luôn giữ context tối thiểu + định tuyến tới supporting files | Khi skill được invoke/preload |
| `references/CONTEXT_ARCHITECTURE.md` | **Kiến trúc ngữ cảnh Story Engine** | Ghi rõ consumer matrix, load triggers, anti-patterns và stop condition của progressive disclosure | Khi refactor/debug context loading |
| `references/structural-mechanisms.md` | **Cơ chế cấu trúc** | Core Causal Engine · Causal Debt · Belief Engine · Domain Shift · Macro Map · Advance | Lên xương, nối chapter, chẩn đoán structural progression |
| `references/evidence-in-story.md` | **Bằng chứng trong câu chuyện** | Research-as-Entertainment · Original Synthesis · Narrative Overreach · evidence placement | Khi task có paper/site/experiment/synthesis/causal bridge |
| `references/workflows.md` | **Quy trình dùng Story Engine** | Story Map · after-chapter check · structural review · stop condition | Khi cần artifact/workflow cụ thể |
| `references/mechanism-lab.md` | **Phòng thí nghiệm cơ chế** | Candidate R&D | **Chỉ** research/postmortem/cross-corpus/promotion decision |

## Context Profiles — Hồ sơ ngữ cảnh

### Writer / Structure Mode — Bộ não viết / dựng cấu trúc

Default:

```text
SKILL.md
```

Thêm khi cần:

```text
structural problem        → structural-mechanisms.md
story/evidence placement  → evidence-in-story.md
Story Map / stress test   → workflows.md
```

**Không load `mechanism-lab.md` khi viết bình thường.**

### Viewer Retention Judge — Giám khảo giữ chân

Preload mặc định:

```text
SKILL.md only
+ agent's own prompt
```

Không tự mở toàn bộ reference.
Agent chỉ đọc supporting file nếu một mechanism cụ thể bị ambiguous.
Không đọc `evidence-in-story.md` để tự kết án nguồn và không đọc `mechanism-lab.md`.

### R&D / Postmortem — Nghiên cứu & hậu kiểm

Có thể load:

```text
SKILL.md
CONTRACT.md
mechanism-lab.md
+ evidence/corpus artifact liên quan
```

Nhưng candidate vẫn không tự biến thành requirement.

## Ownership — Phạm vi sở hữu

Story Engine sở hữu **Structural Retention — Giữ chân bằng cấu trúc**:

- `Structural Causality — Nhân quả cấu trúc`;
- `Belief Progression — Tiến triển niềm tin`;
- `Explanatory Progression — Tiến triển giải thích`;
- chapter/transition stress test;
- vị trí bằng chứng trong story, nhưng **không phán nguồn đúng hay sai**.

Chi tiết canonical: `CONTRACT.md`.

### Không sở hữu

- factual verification / evidence verdict — xác minh nguồn / phán bằng chứng;
- sentence-level prose / voice — câu chữ / giọng kể;
- topic / title / thumbnail — đề tài / title / thumbnail;
- analytics causality — nhân quả số liệu;
- auto-promotion of mechanisms — tự nâng cơ chế thành luật.

## Ranh giới với retention skill cũ

`sketchapiens-giu-chan-nguoi-xem` — **Kỹ thuật giữ chân người xem** là **supporting legacy module — module hỗ trợ kế thừa** cho hook/pacing/craft observations.

Nó **không phải structural authority**.
Khi hai module mâu thuẫn về cấu trúc, `CONTRACT.md` của Story Engine thắng trong phạm vi cấu trúc.

## Ranh giới với Evidence

Story Engine được **flag symptom — báo triệu chứng** `Narrative Overreach — Cốt truyện chạy vượt bằng chứng`.
Evidence reviewer mới được **issue verdict — ra phán quyết** bằng nguồn.

## Từ khóa chính

| English | Tiếng Việt |
|---|---|
| Story Engine | **Cỗ máy cấu trúc câu chuyện** |
| Progressive Disclosure | **Tải ngữ cảnh theo nhu cầu** |
| Context Router | **Bộ định tuyến ngữ cảnh** |
| Context Budget | **Ngân sách ngữ cảnh** |
| Core Causal Engine | **Cỗ máy nhân quả lõi** |
| Causal Debt | **Món nợ nhân quả** |
| Causal Handoff | **Bàn giao nhân quả** |
| Belief Engine | **Cỗ máy thay đổi niềm tin** |
| Belief Flip | **Cú lật niềm tin** |
| Domain Shift | **Đổi miền câu chuyện** |
| Research-as-Entertainment | **Biến nghiên cứu thành phần giải trí** |
| Original Synthesis | **Tổng hợp nguyên bản** |
| Narrative Overreach | **Cốt truyện chạy vượt bằng chứng** |
| Solution Ladder | **Bậc thang giải pháp** |
| Constraint Migration | **Dịch chuyển điểm nghẽn** |
| Scale-Out Escalation | **Leo thang bằng mở rộng quy mô** |
| Mechanism Lab | **Phòng thí nghiệm cơ chế** |
| Structural Retention | **Giữ chân bằng cấu trúc** |
| Module Ownership | **Quyền sở hữu module** |
| Public Interface | **Giao diện công khai** |

## Quy tắc dùng từ

Khi thêm thuật ngữ English mới:

```text
English term — Nghĩa tiếng Việt
```

Nếu thành tên file/folder/skill, giữ identifier kỹ thuật bằng English ASCII và ghi nghĩa Việt bên cạnh trong tài liệu người đọc.

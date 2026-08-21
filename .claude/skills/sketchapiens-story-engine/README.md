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
        ↓ chỉ R&D / postmortem / explicit experiment
references/candidate-lifecycle.md
        ↓ sau khi hiểu lifecycle mới đọc data
references/mechanism-lab.md

NON-RUNTIME / REGRESSION ONLY
tests/**
```

Mục tiêu: **ít context hơn, nhưng đúng context hơn**.
Không đọc mọi reference chỉ vì chúng tồn tại.

## Bản đồ file

| Tên kỹ thuật | Nghĩa tiếng Việt | Vai trò | Khi load |
|---|---|---|---|
| `CONTRACT.md` | **Hợp đồng Story Engine / hợp đồng module** | Nguồn chuẩn cho ownership, non-ownership, input/output, dependency direction, consumer boundary | Khi có ambiguity về ai sở hữu quyết định nào |
| `SKILL.md` | **Giao diện công khai / cửa vào runtime** | Luôn giữ context tối thiểu + định tuyến tới supporting files | Khi skill được invoke/preload |
| `references/CONTEXT_ARCHITECTURE.md` | **Kiến trúc ngữ cảnh Story Engine** | Consumer matrix, load triggers, context budget, candidate firewall | Khi refactor/debug context loading |
| `references/structural-mechanisms.md` | **Cơ chế cấu trúc** | Core Causal Engine · Causal Debt · Belief Engine · Domain Shift · Macro Map · Advance | Lên xương, nối chapter, chẩn đoán structural progression |
| `references/evidence-in-story.md` | **Bằng chứng trong câu chuyện** | Research-as-Entertainment · Original Synthesis · Narrative Overreach · evidence placement | Khi task có paper/site/experiment/synthesis/causal bridge |
| `references/workflows.md` | **Quy trình dùng Story Engine** | Story Map · after-chapter check · structural review · stop condition | Khi cần artifact/workflow cụ thể |
| `references/candidate-lifecycle.md` | **Vòng đời cơ chế ứng viên** | Status machine, promotion gates, controlled experiment, consumer firewall | **Đọc trước Mechanism Lab** trong R&D/postmortem/experiment |
| `references/mechanism-lab.md` | **Phòng thí nghiệm cơ chế** | Dữ liệu candidate cụ thể + evidence/counterexample/test | Chỉ sau `candidate-lifecycle.md`, khi task R&D thật sự cần |
| `tests/README.md` | **Kiến trúc bộ ca thử hồi quy** | Golden behavior, severity, context profiles, anti-overfit | Khi chạy/refactor smoke suite |
| `tests/fixtures/historical-cases.md` | **Ca thử lịch sử** | 5 snapshot V17–V20 pin bằng path + blob SHA | Smoke/regression only |
| `tests/fixtures/micro-cases.md` | **Ca thử vi mô** | 10 case cô lập false positive/boundary | Smoke/regression only |
| `tests/RUNBOOK.md` | **Cách chạy smoke test** | Blind-first protocol, pass/fail policy, report contract | Khi chạy suite |
| `tests/check_smoke_report.py` | **Máy kiểm báo cáo smoke** | Chỉ kiểm cấu trúc report + candidate leakage dễ bắt | Sau khi có report |

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

**Không load `candidate-lifecycle.md`, `mechanism-lab.md` hoặc `tests/**` khi viết bình thường.**
Writer bình thường phải hoạt động như thể **không biết tên candidate cụ thể**.

### Viewer Retention Judge — Giám khảo giữ chân

Preload mặc định:

```text
SKILL.md only
+ agent's own prompt
```

Không tự mở toàn bộ reference.
Agent chỉ đọc supporting canonical file nếu một mechanism cụ thể bị ambiguous.
Không đọc `evidence-in-story.md` để tự kết án nguồn.
**Không đọc candidate lifecycle, Mechanism Lab hoặc tests trong review thường.**

### R&D / Postmortem — Nghiên cứu & hậu kiểm

Load theo thứ tự:

```text
SKILL.md
CONTRACT.md nếu cần ownership
candidate-lifecycle.md       ← hiểu status + firewall trước
mechanism-lab.md             ← rồi mới xem candidate data
+ evidence/corpus artifact liên quan
```

Candidate vẫn không tự biến thành requirement.
Observation mới không tự thành candidate.
Candidate mới không tự thành canonical.

### Controlled Experiment — Thử nghiệm có kiểm soát

Chỉ khi owner mở rõ một experiment trên **một candidate cụ thể**.

Khi đó:
- candidate là lens thử nghiệm, không phải requirement;
- không đọc các candidate khác chỉ vì đang ở R&D;
- reviewer nên blind nếu test design không cần biết candidate;
- một case thành công không tự promote.

Chi tiết: `references/candidate-lifecycle.md`.

### Smoke / Regression — Ca thử hồi quy

Chỉ khi đang kiểm Story Engine/refactor:

```text
SKILL.md
+ reference tối thiểu theo tests/RUNBOOK.md
+ đúng một fixture input
```

Expected behavior **không được preload vào model đang được test** nếu mục tiêu là judgment blind.
`tests/**` không có runtime authority và không được dùng làm creative rule.

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

## Candidate Isolation — Cách ly cơ chế ứng viên

Current candidate names như:

- `Solution Ladder — Bậc thang giải pháp`;
- `Constraint Migration — Dịch chuyển điểm nghẽn`;
- `Scale-Out Escalation — Leo thang bằng mở rộng quy mô`;
- `Evidence Fit — Độ khớp bằng chứng–nhân quả`;

được phép xuất hiện trong **human map / R&D docs**, nhưng **không có runtime authority**.

Tên xuất hiện không đồng nghĩa mechanism đã canonical.
Authority chỉ đến từ destination + status + owner decision theo `candidate-lifecycle.md`.

## Regression Tests — Bộ test hồi quy

NEXT-02E thêm hai lớp fixture:

- **Historical — Lịch sử:** V17 Death · V17 Rain · V18 Sleep · V19 NightWalk · V20 Cold;
- **Micro — Vi mô:** true/false Causal Debt · valid Domain Shift · no-mystery case · false Belief Flip · Narrative Overreach handoff · candidate leak trap · additive evidence · packaging boundary · same-surface/different-function.

Bộ test bảo vệ **behavior**, không đóng băng wording.
Nếu test chỉ pass khi model lặp lại đúng thuật ngữ đã viết trong expectation, test đã overfit.

## Từ khóa chính

| English | Tiếng Việt |
|---|---|
| Story Engine | **Cỗ máy cấu trúc câu chuyện** |
| Progressive Disclosure | **Tải ngữ cảnh theo nhu cầu** |
| Context Router | **Bộ định tuyến ngữ cảnh** |
| Context Budget | **Ngân sách ngữ cảnh** |
| Candidate Lifecycle | **Vòng đời cơ chế ứng viên** |
| Candidate Firewall | **Tường lửa cơ chế ứng viên** |
| Controlled Experiment | **Thử nghiệm có kiểm soát** |
| Smoke Fixture | **Ca thử smoke / ca thử hồi quy** |
| Golden Behavior | **Hành vi chuẩn cần giữ** |
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

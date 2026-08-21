# Story Engine Tests — BỘ CA THỬ CỖ MÁY CẤU TRÚC CÂU CHUYỆN

> **Status — trạng thái:** regression harness — bộ khung kiểm hồi quy cho Story Engine.
>
> `tests/**` **KHÔNG phải runtime knowledge** và **KHÔNG auto-load khi viết/review video thật**.
> Chỉ mở khi đang chạy smoke test, refactor Story Engine hoặc kiểm regression.

## Mục tiêu

Bộ test này không kiểm Claude có dùng đúng một câu trả lời mẫu hay không.
Nó kiểm **behavioral invariants — các hành vi phải giữ ổn định**:

- nhận ra lỗi cấu trúc thật;
- nhận ra progression thật;
- không ép Causal Debt vào mọi transition;
- không bịa mystery / flaw / belief flip;
- không biến candidate mechanism thành requirement;
- chỉ **flag** Narrative Overreach rồi chuyển Evidence system, không tự kết án nguồn;
- không làm các script khác nhau bị chẩn đoán thành cùng một skeleton.

## Cấu trúc

```text
tests/
├── README.md                         file này
└── fixtures/
    ├── historical-cases.md           ca thật pin theo path + blob SHA
    └── micro-cases.md                ca ngắn tự tạo để cô lập behavior
```

## Golden behavior — Hành vi chuẩn

Mỗi fixture dùng năm nhóm expectation:

- **MUST DETECT — Phải nhận ra:** behavior lõi; bỏ sót = fail.
- **MAY DETECT — Có thể nhận ra:** hợp lý nhưng không bắt buộc; không dùng để fail test.
- **MUST NOT — Không được:** false positive / template forcing; xuất hiện = fail.
- **EVIDENCE HANDOFF — Bàn giao bằng chứng:** nếu có nguy cơ overreach, Story Engine chỉ flag + route sang Evidence.
- **CANDIDATE FIREWALL — Tường lửa candidate:** normal smoke run không được dùng `Solution Ladder`, `Constraint Migration`, `Scale-Out Escalation`, `Evidence Fit` như tiêu chí.

## Hai profile test

### A. `STRUCTURE_SMOKE` — Smoke test dựng/chẩn đoán cấu trúc

Load:

```text
SKILL.md
references/structural-mechanisms.md
references/workflows.md
fixture hiện tại
```

Chỉ load `references/evidence-in-story.md` nếu fixture yêu cầu evidence handoff.

**Không load:**

```text
references/mechanism-lab.md
references/candidate-lifecycle.md
raw competitor corpus
writer historical rationale
```

### B. `REVIEWER_SMOKE` — Smoke test reviewer

Load:

```text
SKILL.md
.claude/agents/viewer-retention-judge.md
fixture hiện tại
```

Không preload supporting theory ngoài thứ agent tự được phép đọc.
Không đọc Mechanism Lab.

## Cách chấm

Một fixture `PASS` khi:

1. mọi `MUST DETECT` xuất hiện về **ý**, không cần trùng từ;
2. không vi phạm `MUST NOT`;
3. evidence boundary đúng role;
4. candidate firewall không bị xuyên;
5. output không thêm mechanism chỉ để làm framework đẹp.

### Không chấm bằng số lượng keyword

Ví dụ output không cần viết đúng chữ `Causal Debt` nếu nó mô tả chính xác rằng:

> lời giải vừa trả tạo ra giới hạn khiến phần sau trở nên cần thiết.

Ngược lại, nhắc `Causal Debt` nhiều lần không làm output tốt hơn.

## Severity — Mức độ regression

- **P0 — Critical:** candidate leak thành requirement; Story Engine tự kết án fact; ép rewrite/template trái contract.
- **P1 — High:** bỏ sót lỗi cấu trúc chính hoặc chẩn đoán false positive làm đổi thesis.
- **P2 — Medium:** nhầm level mechanism, overdiagnose transition, bỏ sót secondary risk.
- **P3 — Low:** wording/format khác nhưng hành vi vẫn đúng.

## Khi nào chạy

Chạy toàn bộ smoke suite trước khi:

- đổi `SKILL.md` hoặc `CONTRACT.md` theo cách ảnh hưởng behavior;
- sửa `structural-mechanisms.md`;
- thay reviewer prompt;
- promote/merge một structural mechanism;
- kết thúc Phase 2;
- canary V21 nếu Story Engine vừa thay đổi.

Không cần chạy vì typo/README-only change không ảnh hưởng runtime.

## Nguyên tắc anti-overfit

> **Test bảo vệ behavior, không đóng băng style output.**

Nếu một fixture chỉ pass khi Claude dùng đúng taxonomy/từ ngữ ta đã viết trước, fixture đó đang test memorization chứ không test judgment.

Nếu Story Engine và fixture conflict, **không mặc định sửa engine để làm test xanh**. Trước tiên hỏi fixture có đang biến một preference thành requirement hay không.

# RUNBOOK — CÁCH CHẠY STORY ENGINE SMOKE TEST

> Bộ test này kiểm **judgment stability — độ ổn định phán đoán**, không kiểm exact wording.

## 1. Khi nào chạy full suite

Chạy cả historical + micro khi thay đổi một trong các vùng:

- `SKILL.md` behavior/boundary;
- `CONTRACT.md` ownership;
- `references/structural-mechanisms.md`;
- `references/workflows.md`;
- `viewer-retention-judge.md`;
- promotion/merge structural mechanism.

README-only / typo-only change không bắt buộc chạy full suite.

---

## 2. Context profile phải giữ cố định

### `STRUCTURE_SMOKE`

Load đúng:

```text
.claude/skills/sketchapiens-story-engine/SKILL.md
.claude/skills/sketchapiens-story-engine/references/structural-mechanisms.md
.claude/skills/sketchapiens-story-engine/references/workflows.md
fixture đang test
```

Chỉ thêm `evidence-in-story.md` nếu fixture có `EVIDENCE HANDOFF` cần chẩn đoán.

### Không load

```text
mechanism-lab.md
candidate-lifecycle.md
competitor corpus
writer rationale / notes
expected result của fixture khác
```

Lý do: nếu model đọc Mechanism Lab trước thì Candidate Firewall test mất ý nghĩa.

---

## 3. Prompt chuẩn cho một fixture

```text
Run Story Engine STRUCTURE_SMOKE on fixture <ID>.
Diagnose only what the supplied surface supports.
Do not rewrite.
Do not read Mechanism Lab or candidate lifecycle.
Return:
1. strongest structural diagnosis
2. progression / transition diagnosis
3. promise-payoff risk if packaging is supplied
4. possible evidence-boundary handoff if any
5. explicit list: what you deliberately did NOT diagnose
```

Sau khi model trả lời, **mới** mở expectation block của fixture để chấm.
Không cho model thấy expected behavior trước nếu mục tiêu là đo judgment thật.

---

## 4. Blind-first protocol — Quy trình chấm mù trước

Để giảm overfit:

1. evaluator A chỉ đưa input/surface của fixture;
2. model tạo diagnosis;
3. evaluator B hoặc pass thứ hai mới so với `MUST DETECT / MUST NOT`;
4. ghi fail theo behavior, không theo từ ngữ;
5. không sửa fixture hoặc engine ngay sau một fail duy nhất; xác định fail do test hay do engine.

Historical fixtures có expectation cùng file để bảo trì thuận tiện, nhưng khi chạy thật nên **copy input/path sang context riêng trước**, không preload cả file expectation.

---

## 5. Report format — Mẫu báo cáo

Tạo file tạm ngoài runtime hoặc trong working notes với format:

```text
SMOKE RUN: YYYY-MM-DD
ENGINE COMMIT: <sha>
PROFILE: STRUCTURE_SMOKE / REVIEWER_SMOKE

FIXTURE: H-01
RESULT: PASS / FAIL / REVIEW
SEVERITY: P0 / P1 / P2 / P3 / none
MUST DETECT: PASS / FAIL + note
MUST NOT: PASS / FAIL + note
EVIDENCE HANDOFF: PASS / FAIL / N/A
CANDIDATE FIREWALL: PASS / FAIL
OBSERVED DIAGNOSIS: ...

...

SUITE SUMMARY
PASS:
FAIL:
REVIEW:
P0:
P1:
```

## 6. PASS policy — Chính sách pass

### `PASS`

- tất cả core `MUST DETECT` đạt;
- không vi phạm `MUST NOT`;
- candidate firewall sạch;
- evidence boundary đúng role.

### `REVIEW`

Dùng khi diagnosis hợp lý nhưng fixture expectation có vẻ quá chặt hoặc script bản thân ambiguous.

`REVIEW` **không được tự đổi thành FAIL** chỉ vì model dùng taxonomy khác.

### `FAIL`

Behavior thật sự trái contract.

Ví dụ:
- ép Causal Debt vào M-03;
- gọi `Solution Ladder` trong M-07 normal mode;
- tự fact verdict ở M-06;
- đổi title thay owner ở M-09.

---

## 7. Regression policy — Chính sách hồi quy

Nếu suite fail sau refactor:

1. xác định **first bad commit — commit đầu tiên gây lỗi**;
2. hỏi fixture có đang bảo vệ principle hay preference;
3. nếu fixture đúng → sửa engine/reference nhỏ nhất có thể;
4. nếu fixture sai → sửa fixture và ghi lý do;
5. chạy lại **case fail + một case đối nghịch**, rồi mới full suite.

Không “tune” Story Engine bằng cách thêm một câu rule cho mỗi fixture fail.
Đó là cách test suite biến thành rule pile.

---

## 8. Deterministic checker — Máy kiểm phần máy kiểm được

`check_smoke_report.py` chỉ kiểm:

- fixture IDs bắt buộc có trong report;
- RESULT có giá trị hợp lệ;
- không có candidate names trong normal observed diagnosis;
- suite không tự ghi PASS nếu có P0/P1 fail.

Nó **không** cố đánh giá semantic quality.

Chạy:

```bash
python3 .claude/skills/sketchapiens-story-engine/tests/check_smoke_report.py <report.md>
```

Machine check PASS không đồng nghĩa Story Engine pass.
Nó chỉ nói report có cấu trúc hợp lệ và không có leakage dễ bắt bằng text.

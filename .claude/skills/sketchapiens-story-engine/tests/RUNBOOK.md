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

## 3. Input completeness gate — Cổng xác nhận input đầy đủ

**Historical fixture không được chẩn đoán trước khi chứng minh input đã nạp đủ.**

Trước diagnosis, ghi tối thiểu:

```text
FIXTURE: H-XX
SOURCE BLOB: <full pinned sha>
SOURCE TOTAL LINES: <n>
LOADED LINES: <n>
INPUT COMPLETE: YES / NO
```

Điều kiện:

- `LOADED LINES == SOURCE TOTAL LINES`;
- nếu có thể, chạy checksum / `git hash-object` trên file đã trích và xác nhận bằng pinned blob SHA;
- `INPUT COMPLETE: NO` → **DỪNG**, lượt chạy là `EXECUTION FAULT — lỗi thực thi`, không được chẩn đoán và không được tính FAIL cho engine.

Với micro fixture, phải cấp **toàn bộ INPUT/SURFACE block** của đúng fixture; không cắt theo token convenience.

Lý do: runtime verification 2026-08-21 từng nạp H-03 `80/158` dòng và H-04 `60/126` dòng, tạo một P1 giả và một REVIEW giả dù engine không đổi.

---

## 4. Prompt chuẩn cho một fixture

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

## 5. Blind-first protocol — Quy trình chấm mù trước

Để giảm overfit, tách ba vai rõ:

1. **Evaluator A — người cấp input:** chỉ đưa input/surface + context profile; xác nhận Input Completeness Gate trước khi gọi model.
2. **Diagnosis model — model chẩn đoán:** tạo diagnosis trong context chưa từng thấy `MUST DETECT / MUST NOT / EVIDENCE HANDOFF` của fixture đó.
3. **Evaluator B — người chấm:** chỉ sau khi diagnosis đã đóng mới mở expectation để so.
4. Ghi fail theo behavior, không theo từ ngữ.
5. Không sửa fixture hoặc engine ngay sau một fail duy nhất; trước hết phân loại nguồn lỗi.

Historical fixtures có expectation cùng file để bảo trì thuận tiện, nhưng khi chạy thật phải **copy input/path sang context riêng trước**, không preload cả file expectation.

### Corrective rerun — Chạy lại sửa lỗi thực thi

Nếu evaluator/model của lượt gốc **đã nhìn expectation**, context đó **không được tự rerun cùng fixture** rồi gọi là blind-first.

Corrective rerun phải dùng:

```text
Evaluator A có thể biết lịch sử / expectation
        ↓ chỉ cấp full input + context profile
CLEAN DIAGNOSIS CONTEXT chưa thấy expectation
        ↓ diagnosis đóng
Evaluator B mới mở expectation và chấm
```

Giữ nguyên kết quả lượt gốc trong lịch sử. Ghi:

```text
ORIGINAL RUN  → INVALID DUE TO EXECUTION FAULT
CORRECTIVE RUN → PASS / FAIL / REVIEW
```

Không rewrite lịch sử để lượt gốc trông như đã pass.

---

## 6. Report format — Mẫu báo cáo

Tạo file tạm ngoài runtime hoặc trong working notes với format:

```text
SMOKE RUN: YYYY-MM-DD
ENGINE COMMIT: <sha>
PROFILE: STRUCTURE_SMOKE / REVIEWER_SMOKE

FIXTURE: H-01
SOURCE BLOB: <sha or N/A>
SOURCE TOTAL LINES: <n or N/A>
LOADED LINES: <n or N/A>
INPUT COMPLETE: YES / NO / N/A
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

---

## 7. PASS policy — Chính sách pass

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

### `EXECUTION FAULT` — Lỗi thực thi

Không phải verdict semantic của fixture.
Dùng khi lượt chạy không đủ điều kiện để kết luận về engine, ví dụ:

- input bị cắt / thiếu dòng;
- pinned blob không khớp;
- model đã thấy expectation trước diagnosis;
- context profile vô tình preload Mechanism Lab/candidate;
- test chạy sai file hoặc sai version.

`EXECUTION FAULT` **không được tính PASS/FAIL cho engine**. Sửa execution rồi rerun đúng fixture bằng clean diagnosis context.

---

## 8. Regression policy — Chính sách hồi quy

Nếu suite xuất hiện FAIL/REVIEW sau refactor, **phân loại nguyên nhân trước khi sửa bất cứ thứ gì**:

### A. `ENGINE DEFECT — lỗi engine`

Fixture hợp lệ + execution hợp lệ + behavior trái contract.

→ xác định **first bad commit — commit đầu tiên gây lỗi**;
→ sửa engine/reference nhỏ nhất có thể;
→ chạy lại case fail + một case đối nghịch, rồi mới full suite nếu cần.

### B. `FIXTURE DEFECT — lỗi ca thử`

Expectation đang bảo vệ preference thay vì principle, hoặc script/fixture ambiguous hơn test giả định.

→ sửa fixture và ghi lý do;
→ không tune engine để làm test cũ xanh.

### C. `EXECUTION FAULT — lỗi thực thi`

Input/context/protocol không hợp lệ.

→ không sửa engine;
→ giữ lịch sử run lỗi;
→ sửa execution;
→ rerun bằng clean diagnosis context;
→ chỉ kết luận engine sau corrective run hợp lệ.

Không “tune” Story Engine bằng cách thêm một câu rule cho mỗi fixture fail.
Đó là cách test suite biến thành rule pile.

---

## 9. Deterministic checker — Máy kiểm phần máy kiểm được

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

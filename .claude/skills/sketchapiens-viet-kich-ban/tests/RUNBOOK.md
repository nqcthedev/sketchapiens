# WRITER REGRESSION RUNBOOK — HƯỚNG DẪN CHẠY TEST WRITER

> **Status:** `NON-RUNTIME / REGRESSION ONLY`

## 1. Principle — Nguyên tắc

Writer test phải trả lời:

> Sau khi bỏ legacy monolith khỏi default context, Writer có giữ đúng workflow/boundary/capability không?

Không dùng test để tối ưu văn theo gu evaluator.
Không sửa Writer trong cùng lượt chạy để làm report đẹp.

---

# 2. Blind-first protocol — Chẩn đoán trước, đáp án sau

Mỗi fixture có hai phần:

```text
INPUT / SURFACE
EXPECTED BEHAVIOR
```

Model Writer được test **chỉ thấy INPUT/SURFACE**.

Sau output:

1. khóa output;
2. evaluator khác hoặc context đánh giá riêng mới đọc EXPECTED;
3. chấm behavior;
4. không cho Writer sửa câu trả lời sau khi nhìn expectation rồi tính là pass.

Nếu cùng model/context đã thấy expectation trước output → lượt đó `EXECUTION FAULT`, không tính PASS/FAIL cho Writer.

---

# 3. Input completeness gate — Cổng đủ input

Trước historical fixture:

- verify path;
- verify pinned blob SHA;
- load đúng line range/surface được fixture chỉ định;
- nếu task yêu cầu full artifact thì xác nhận full artifact đã load.

Nếu source mismatch:

```text
EXECUTION FAULT — SOURCE DRIFT
```

Không chấm Writer trên input sai.

---

# 4. Context profiles

## `WRITER_SMOKE`

Allowed:

```text
Writer SKILL.md
Writer CONTRACT.md
prose-and-voice.md
current fixture input
current project control context auto-loaded by Claude Code
```

Conditional only:

```text
evidence-expression.md   # evidence expression task
english-final-rewrite.md # only after explicit VI approval
Story Engine             # only for real structural decision
Retention Craft          # only for sentence/paragraph craft trigger
```

Forbidden default context:

```text
runtime-monolith-legacy.md
luat-chung-ngach.md
viral-teardown.md
formula-and-example.md
teardown-survival-cluster.md
quy-trinh-nghien-cuu-cum.md
metadata.md
2_KHO_BANGHI/**
Story Engine mechanism-lab.md
Story Engine candidate-lifecycle.md
fixture EXPECTED block
```

## `EN_GATE_SMOKE`

Run M-W02 then M-W03 in **separate clean contexts**.

Reason:
If M-W03 approval context leaks into M-W02, gate test is invalid.

## `BOUNDARY_SMOKE`

Use M-W04/M-W05/M-W06/M-W09/M-W10.

Goal is not to see exact phrase “handoff”. Goal is correct ownership behavior.

---

# 5. Standard prompt — Prompt chuẩn

For one fixture:

```text
Run Writer <PROFILE> on fixture <ID>.
Use only the INPUT/SURFACE supplied for the fixture plus active Writer/project runtime context.
Do not read the fixture EXPECTED section before output.
Do not read Writer legacy/history or competitor teardown unless this is explicitly an audit/history fixture.
Return the Writer response exactly as it would behave in production.
Do not self-grade.
```

Evaluator pass:

```text
Evaluate locked Writer output for fixture <ID> against EXPECTED BEHAVIOR.
Do not rewrite the answer.
Return RESULT, SEVERITY, invariant checks, leakage checks, and short reasoning.
```

---

# 6. Historical-case procedure

For H-W01/H-W02/H-W03:

1. `git hash-object <source>` or equivalent verify against pinned SHA;
2. extract only declared surface unless fixture says full source;
3. Writer gets task + surface;
4. lock output;
5. evaluator reads expectation;
6. grade prose capability **and** boundary behavior.

Do not compare wording against historical English as a similarity target.
Meaning/function preservation is the target.

---

# 7. Corrective rerun protocol

If failure is due to incomplete input, wrong fixture exposure, wrong context profile or expectation leak:

```text
ORIGINAL RUN → EXECUTION FAULT
CORRECTIVE RUN → clean Writer context → locked output
              → separate evaluator context → grade
```

Do not rewrite history so original run looks PASS.

If Writer itself failed with valid execution:

- classify severity;
- identify smallest contract/router/reference defect;
- do not fix during diagnostic run;
- after fix, rerun failed case + an opposite/control case;
- then rerun full suite before stable checkpoint.

---

# 8. Opposite/control pairs — Cặp chống overfit

Use these pairs when fixing regressions:

| Failed tendency | Control pair |
|---|---|
| English too early | M-W02 + M-W03 |
| Always delegates structure | M-W04 + M-W12 |
| Always blocks facts | M-W05 + H-W03 |
| Removes all humor | M-W07 + a prose fixture where natural humor is allowed |
| Treats any external text as forbidden | M-W06 + own-channel historical H-W01 |
| Refuses all cross-mode mentions | M-W09 + explicit later packaging task outside Writer smoke |
| Overprotects artifacts | M-W10 + legitimate creation of a new current version in integration test |

The fix must solve the failure without breaking the opposite valid behavior.

---

# 9. Report fields

Each fixture record:

```text
FIXTURE:
PROFILE:
SOURCE PIN VERIFIED: YES / NO / N/A
RESULT: PASS / FAIL / REVIEW / EXECUTION_FAULT
SEVERITY: P0 / P1 / P2 / P3 / NONE
VI-FIRST: PASS / FAIL / N/A
EN-GATE: PASS / FAIL / N/A
STRUCTURE BOUNDARY: PASS / FAIL / N/A
EVIDENCE BOUNDARY: PASS / FAIL / N/A
COMPETITOR FIREWALL: PASS / FAIL / N/A
DEAD/PENDING RULE FIREWALL: PASS / FAIL / N/A
CROSS-MODE ISOLATION: PASS / FAIL / N/A
ARTIFACT SAFETY: PASS / FAIL / N/A
PROSE CAPABILITY: PASS / FAIL / N/A
OBSERVED BEHAVIOR:
NOTES:
```

Suite summary:

```text
ENGINE COMMIT:
WRITER CONTRACT SHA:
WRITER SKILL SHA:
TOTAL VALID RUNS:
PASS:
FAIL:
EXECUTION FAULT:
P0:
P1:
LEGACY LOADED IN NORMAL RUN: YES / NO
COMPETITOR LEAKAGE: YES / NO
D-27 LEAKAGE: YES / NO
PHASE 3B WRITER VERDICT:
```

---

# 10. Severity

## P0

- raw competitor/teardown used to generate normal script;
- Writer self-issues factual verdict and overclaims;
- pending/dead rule becomes hard requirement;
- overwrite immutable script version;
- Writer self-sets owner-only approved/published ref.

## P1

- English final before VI approval;
- Writer silently owns structural decision that should defer;
- Writer executes research/packaging/production in normal mode;
- prose capability collapses materially after legacy detachment.

## P2

- unnecessary context loading;
- over-prescriptive craft behavior without major output damage;
- unclear handoff.

## P3

- reporting wording / cosmetic inconsistency.

---

# 11. Full suite

Run:

```text
Historical: H-W01 → H-W03
Micro:      M-W01 → M-W12
```

Total = 15 fixtures.

A full regression run is valid only if each fixture has a locked blind-first output or explicit `EXECUTION_FAULT` that is later corrected.

---

# 12. Stable closure rule

Writer can be called `STABLE` only if:

- all 15 valid fixtures PASS or have explicit owner-accepted non-blocking REVIEW;
- P0 = 0;
- P1 = 0;
- competitor leakage = NO;
- D-27/dead-rule leakage = NO;
- legacy default-load = NO;
- EN gate behaves correctly both directions;
- structure/evidence boundaries pass;
- historical prose cases demonstrate non-trivial spoken capability;
- project doctor has no new FAIL from Phase 3B.

Do not lower fixture expectations merely to close the phase.

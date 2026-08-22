# 04A-C — AUTHORITY & SOURCE-OF-TRUTH AUDIT — KIỂM QUYỀN SỞ HỮU EVIDENCE

> **Mode:** READ-ONLY
> **Mục tiêu:** xác định authority hiện tại, duplication và unresolved ownership. Không sửa source-of-truth trong 04A.

---

## 1. CANONICAL MAP HIỆN HÀNH

`governance/SOURCE_OF_TRUTH.md` hiện ghi:

```text
Evidence verdict
→ .claude/agents/evidence-prosecutor.md
+ templates/claim-ledger.md
```

Ghi chú boundary:

- Story Engine chỉ flag `Narrative Overreach`;
- `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE` verdict thuộc Evidence reviewer cho tới Phase 4.

Đồng thời Architecture Contract trong roadmap nói:

```text
Schemas are the type system.
```

Vì vậy hiện có ít nhất ba loại authority phải tách:

1. **semantic authority** — label/verdict có nghĩa gì;
2. **machine-shape authority** — artifact có field/enum nào;
3. **workflow authority** — khi nào verify/rerun/lock.

---

## 2. AUTHORITY MAP HIỆN TẠI

### A-SEM-01 — Verdict semantics

Các định nghĩa `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE` xuất hiện ở:

- `evidence-prosecutor.md`;
- `templates/claim-ledger.md`;
- `schemas/claim-ledger.schema.json` enum;
- `verify-claims/SKILL.md` description;
- `audit-script/SKILL.md` output description;
- Writer evidence-expression;
- Story evidence-in-story.

**Current effective semantic owner:** Evidence Prosecutor + claim-ledger template theo SoT.

**Risk:** schema và consumers copy vocabulary; nếu semantic meaning đổi, drift có thể xảy ra dù enum vẫn validate.

### A-SHAPE-01 — Ledger machine shape

`schemas/claim-ledger.schema.json` là artifact-shape authority hợp lý theo Architecture Contract.

Nó định nghĩa fields/types/enums, nhưng hiện description text cũng chứa semantic policy, ví dụ:

- `author_inference`: narration “PHẢI” ghi rõ;
- `modern_to_prehistoric`: narration phải tự nhận giới hạn;
- `overreach`: mapping 0–3.

Đây là **semantic leakage into schema description**, không nhất thiết sai, nhưng làm boundary shape-vs-policy mờ.

### A-WF-01 — Verify/rerun/lock workflow

`.claude/skills/verify-claims/SKILL.md` hiện là effective workflow owner:

- trước evidence-locked milestone;
- sau factual additions;
- trước owner approval;
- gọi prosecutor;
- ghi claim ledger;
- lock được khi không còn `overreach >= 2`.

`apply-review` là consumer/enforcer của rerun rule, không nên là owner.

### A-ART-01 — Human ledger presentation

`templates/claim-ledger.md` vừa là template vừa lặp semantic rules + lock rule.

Do SoT đang liệt kê template như một phần của Evidence verdict owner, template hiện có authority lớn hơn một template thông thường.
Đây là architecture smell cần 04A-G giải quyết.

### A-WRITER-01 — Narration expression

Writer `CONTRACT.md` + `references/evidence-expression.md` sở hữu cách wording verdict đã resolved.

Không conflict authority lớn ở đây.

### A-STORY-01 — Structural placement / overreach symptom

Story `CONTRACT.md` + `references/evidence-in-story.md` sở hữu placement + Narrative Overreach symptom.

Không được issue factual verdict.

### A-REVIEW-01 — Review orchestration

`audit-script` chỉ orchestration/context boundary.
Nó không nên own Evidence taxonomy dù hiện nó copy tên output labels.

---

## 3. SOURCE-OF-TRUTH DRIFTS / AMBIGUITIES

### SOT-D01 — Verdict meaning bị copy ở quá nhiều active consumers

Hiện chưa thấy bốn label mâu thuẫn trực tiếp, nhưng cùng semantics được mô tả lặp ở nhiều file.

Đây là **latent drift**: một update tương lai có thể sửa agent mà quên template/schema/Writer/Story docs.

### SOT-D02 — Schema enum là machine authority nhưng semantic owner không rõ

Nếu Evidence taxonomy đổi:

- agent có thể phát verdict mới;
- schema có thể reject artifact;
- template có thể không có cột/legend tương ứng.

Không có contract hiện tại nói thứ tự migration giữa ba nơi.

### SOT-D03 — Lock semantics bị duplicate

`verify-claims` và template đều mô tả:

```text
KHOÁ ĐƯỢC khi không còn mức >= 2
```

Schema chỉ có `locked: boolean`, không encode precondition.

Chưa rõ ai có authority set `locked=true` và ai chỉ report “KHOÁ ĐƯỢC”.
Đây là distinction rất quan trọng giữa **verdict recommendation** và **artifact mutation**.

### SOT-D04 — “Một claim → đúng một nguồn” không khớp Original Synthesis

Schema description nói:

> mỗi mệnh đề trong lời đọc gắn với đúng một nguồn và đúng một nhãn.

Template cũng có một cột `Nguồn` singular.

Nhưng Story Engine canonical cho phép `Original Synthesis`:

```text
source A
+ source B
+ source C
→ project explanatory model
```

Một synthesis/bridge có thể cần nhiều source dependencies.

**Unresolved:** ledger hiện encode synthesis bằng cách nào?

- một row + source string chứa nhiều citations?
- nhiều rows + một bridge relation bên ngoài?
- inference row không có machine-readable dependency?

04A-D/F phải kiểm trước khi đề xuất shape.

### SOT-D05 — Overreach scale trộn severity và error class

Current definition:

```text
0 = khớp
1 = hơi rộng hơn
2 = bắc cầu giữa hai bảng số
3 = bịa
```

`2` là một **failure type**, không đơn thuần severity.

Một certainty-inflation rất nghiêm trọng nhưng không phải “hai bảng số” sẽ map bao nhiêu?
Một wrong causal role như Egypt E-01 sẽ map bao nhiêu?

Scale hiện hữu dụng như historical guardrail nhưng semantic dimension chưa clean.

### SOT-D06 — `author_inference` vs project inference dễ nhầm

Schema field `author_inference` mô tả “suy diễn của tác giả nguồn”.
Writer/Story lại nói tới **project inference / project synthesis**.

Hai khái niệm khác nhau:

```text
SOURCE AUTHOR INFERS X
PROJECT INFERS Y FROM SOURCE(S)
```

Current ledger không có explicit project-synthesis/dependency field.

### SOT-D07 — Legacy evidence artifacts không có migration contract

V17–V20 dùng VERIFY/MONEO với reasoning rất giàu nhưng shape riêng.

SoT mới trỏ future path `videos/<ID>/02-research/claim-ledger.md`.
Không có yêu cầu migrate legacy, và không nên giả vờ chúng conform.

**Recommended audit stance:** legacy = historical regression corpus, không phải migration blocker của Phase 4.

---

## 4. AUTHORITY KHÔNG CÓ CONFLICT LỚN

### Writer boundary

Writer chỉ wording verdict đã có → sạch.

### Story boundary

Story flag structural symptom, Evidence verdict → sạch.

### Audit-script role isolation

Evidence Prosecutor nhận evidence context riêng, không retention/prose theory → sạch.

### Apply-review rerun trigger

Editor không phán evidence, chỉ bắt rerun factual changes → sạch.

---

## 5. UNRESOLVED QUESTIONS CHUYỂN SANG 04A-D/G

1. Có cần một canonical Evidence semantic contract riêng không?
2. Schema nên chỉ encode shape hay được phép chứa semantic invariant nào?
3. Template có nên còn là co-owner của verdict hay chỉ render contract?
4. `SYNTHESIS` nên là verdict label, relation type, metadata hay vẫn nằm dưới `INFERENCE`?
5. Multi-source dependency encode ở đâu?
6. `overreach` nên là severity-only hay tách `failure_type` khỏi `severity`?
7. ai được set `locked=true`?
8. “KHOÁ ĐƯỢC” từ prosecutor là verdict hay mutation permission?

Không trả lời trong 04A-C.

---

## 6. CHECK 04A-C

PASS nếu:

- phân biệt semantic / shape / workflow authority;
- ghi rõ current SoT thay vì tự rewrite authority;
- nêu drift/ambiguity có evidence;
- không đổi `SOURCE_OF_TRUTH.md`, schema, template, agent hay workflow.

**Result: PASS.**

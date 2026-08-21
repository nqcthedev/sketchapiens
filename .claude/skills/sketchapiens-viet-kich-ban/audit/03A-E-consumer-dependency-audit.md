# 03A-E — CONSUMER & DEPENDENCY AUDIT — KIỂM CONSUMER / PHỤ THUỘC WRITER

> **Status:** `READ-ONLY AUDIT ARTIFACT — NON-RUNTIME`  
> Không đổi dependency graph. Task này kiểm caller/handoff/deep-link để refactor Writer sau này không làm gãy consumer hoặc tạo vòng phụ thuộc.

**Baseline:** checkpoint `702ec73956c7f0e167366ff472e8178036f4d966`

## Câu hỏi của task

Ai kích hoạt Writer, Writer cần nhận gì từ ai, output Writer được ai dùng, có consumer nào móc vào private legacy internals không, và target dependency direction nào phải giữ?

**Stop condition:** có consumer matrix + dependency graph + migration constraints đủ để 03A-F/G thiết kế contract mà không đoán caller.

---

# 1. DEPENDENCY TYPES — BA KIỂU PHỤ THUỘC

Audit phân biệt:

1. `ACTIVATION` — ai route/invoke Writer;
2. `DATA HANDOFF` — module trao artifact/result, không cần biết implementation của nhau;
3. `IMPLEMENTATION LINK` — consumer đọc/móc file private của module khác.

Mục tiêu architecture là ưu tiên **public API + data handoff**, giảm implementation links.

---

# 2. CURRENT CONSUMER MATRIX

| Surface | Quan hệ với Writer | Input/output boundary | Verdict |
|---|---|---|---|
| `CLAUDE.md` | direct router | mode ② → Writer; VI-first/EN-last/hard constraints | `HEALTHY ACTIVATION` |
| `sketchapiens-chon-de-tai` | upstream research | topic/title/research decision → write mode | `HEALTHY HANDOFF`, nhưng legacy Writer duplicate research concern |
| `/new-video` | upstream artifact shell | tạo `video.yaml` + script dirs/refs, không viết content | `HEALTHY HANDOFF` |
| Story Engine | peer dependency | Writer gửi core question/research/outline; nhận Story Map/diagnosis | `HEALTHY PUBLIC-INTERFACE DEPENDENCY` |
| Evidence system / `/verify-claims` | peer dependency | script/claim → verdict; Writer/editor diễn đạt theo verdict | `HEALTHY BOUNDARY`, có lifecycle wording drift riêng |
| Retention Craft | optional peer support | exact passage/craft problem → craft guidance | `HEALTHY IF TRIGGERED`, không default structure dependency |
| `sketchapiens-bien-tap` | downstream QA | narration artifact → machine/policy/prose QA; thiếu content trả debt về write mode | `HEALTHY ARTIFACT CONSUMER` |
| `/audit-script` | downstream review orchestrator | narration/title/thumbnail + role-specific context | `HEALTHY ARTIFACT CONSUMER`; không cần Writer internals |
| `/apply-review` | downstream editor | owner-classified review + current script → new immutable version | `HEALTHY ARTIFACT CONSUMER`; không gọi Writer implementation |
| Anti-AI critic | downstream prose reviewer | narration only | `HEALTHY SURFACE CONSUMER` |
| production/shot/thumbnail | downstream after approval | approved narration/packaging artifacts | `ARTIFACT DEPENDENCY`, không nên phụ thuộc Writer internals |
| postmortem/R&D | feedback loop | analytics/observations → candidate/governance, không mutate Writer trực tiếp | `HEALTHY INDIRECT LOOP` nếu promotion path được giữ |

---

# 3. CURRENT WRITER OUTBOUND DEPENDENCIES

## 3.1 Healthy / intended

```text
Writer
  → Story Engine public structural interface
  → current approved research / evidence artifacts
  → project control/schema/rules for artifact constraints
```

## 3.2 Compatibility/self-dependency debt

```text
Writer SKILL.md
  → runtime-monolith-legacy.md
       → luat-chung-ngach.md (read every write)
       → quy-trinh-nghien-cuu-cum.md
       → viral-teardown.md
       → survival teardown
       → formula/example
       → metadata.md
       → kho files / historical rules
```

Đây không phải dependency giữa modules rõ ràng; nó là **legacy internal graph** trong đó runtime, research, packaging và history cùng treo dưới Writer.

## 3.3 Dependencies Writer target không nên có

```text
Writer normal write
  X→ raw competitor corpus
  X→ competitor teardown implementation
  X→ packaging metadata implementation
  X→ Mechanism Lab candidates
  X→ reviewer internals
  X→ Evidence Prosecutor internal taxonomy implementation
  X→ Story Engine private mechanism references khi public interface đủ
```

---

# 4. DOWNSTREAM CONSUMERS CÓ CẦN WRITER INTERNALS KHÔNG?

## `/audit-script`

Chỉ cần narration/title/thumbnail/evidence theo từng reviewer. Nó cố ý context-isolate agents và **không preload Writer rationale**.

**Migration consequence:** Writer refactor có thể thay internal file layout mà không cần sửa `/audit-script`, miễn narration artifact contract giữ nguyên.

## `/apply-review`

Nhận owner-classified diagnosis và tạo version mới. Nó không re-run Writer skill, không deep-link monolith, không dùng mechanism name làm requirement.

**Migration consequence:** giữ immutable version/ref semantics; không cần expose Writer internals.

## `sketchapiens-bien-tap`

Đọc script để QA, không viết chapter mới. Nếu phát hiện content debt thì trả lại mode ②.

**Migration consequence:** refactor Writer không nên kéo editor/QA logic vào Writer để “tiện”.

## Production

Production phải consume **approved/published script artifacts**, không “latest file Writer vừa tạo”.

**Migration consequence:** public contract quan trọng là artifact/version state, không private prompt layout.

### Conclusion E-01

Downstream chính **không cần backward compatibility với legacy Writer references**. Đây là tín hiệu tốt: Phase 3B có thể refactor internal context architecture nếu giữ public Writer behavior + script artifacts.

---

# 5. UPSTREAM HANDOFF REQUIREMENTS

## Topic / Research → Writer

Writer không cần biết `sketchapiens-chon-de-tai` đã search clone thế nào. Nó cần **resolved outputs**, ví dụ:

```text
selected topic / title candidate
core promise
research/evidence packet
known overlap / forbidden reused beats
production constraints
```

Nếu upstream output chưa chuẩn hóa hoàn toàn, Writer contract nên mô tả required information chứ không deep-link vào research implementation.

## New Video → Writer

Writer cần:

```text
video path / ID
current lifecycle state
current script ref/version
research artifacts
```

Không cần `/new-video` implementation.

### Conclusion E-02

Target Writer nên phụ thuộc vào **artifact contracts**, không phụ thuộc cách upstream skill tạo artifact.

---

# 6. PEER DEPENDENCY CONTRACTS

## Writer ↔ Story Engine

Target direction:

```text
Writer ──request structure──> Story Engine
Writer <──Story Map/Diagnosis─ Story Engine
```

Cấm:

```text
Story Engine → Writer implementation → Story Engine
```

Current Story Engine CONTRACT đã khóa boundary này. **PASS.**

## Writer ↔ Evidence

```text
Writer/script → claims needing support → Evidence
Writer ← evidence verdict / locked claims ← Evidence
Writer → natural language expression
```

Writer không tự issue DIRECT/INFERENCE verdict. **PASS về ownership.**

## Writer ↔ Retention Craft

Optional, after issue is identified:

```text
Writer passage + sentence-level problem
→ Retention Craft
→ wording/pacing/landing guidance
```

Không dùng Retention Craft làm structural router. **PASS.**

---

# 7. INTEGRATION DRIFT FOUND OUTSIDE WRITER

## E-DRIFT-01 — `/verify-claims` dùng lifecycle state đã retire

`/verify-claims` hiện ghi:

> “Trước khi chuyển sang trạng thái `evidence_locked`”

Nhưng `schemas/video.schema.json` canonical lifecycle không có `evidence_locked`; Phase 1 đã phân loại **evidence locked là milestone/gate, không phải video state**.

### Classification

`INTEGRATION DRIFT — deterministic/documentation`, không phải Writer defect.

### Disposition

- không sửa trong 03A read-only;
- tạo follow-up integration fix trước V21/canary hoặc trước khi workflow mới dựa vào state wording;
- fix phải đổi wording thành evidence gate/artifact milestone, không thêm `evidence_locked` lại vào schema.

---

# 8. DEEP-LINK AUDIT

Các active consumer surfaces đã inspect trực tiếp:

- `CLAUDE.md`;
- `new-video`;
- `sketchapiens-chon-de-tai`;
- Story Engine CONTRACT;
- retention skill;
- `verify-claims`;
- Evidence Prosecutor;
- `sketchapiens-bien-tap`;
- `/audit-script`;
- `/apply-review`;
- Anti-AI critic;
- script/packaging rules.

**Không consumer active nào trong tập này deep-link vào:**

```text
runtime-monolith-legacy.md
luat-chung-ngach.md
viral-teardown.md
formula-and-example.md
teardown-survival-cluster.md
metadata.md
```

Các deep links chính nằm **từ monolith vào own legacy refs**, không phải từ downstream consumer vào Writer internals.

### Tool limitation

GitHub code-search index cho repo này không trả kết quả đáng tin trong phiên audit, và container không có network để clone repo. Vì vậy verdict trên dựa vào **full active consumer surfaces đã inspect**, không được trình bày như một repository-wide grep proof.

03A-H/03B verification nên có local deterministic grep trên checkout thật:

```bash
grep -RniE 'runtime-monolith-legacy|luat-chung-ngach|viral-teardown|formula-and-example|teardown-survival-cluster|metadata\.md' \
  .claude CLAUDE.md governance tools templates \
  --exclude-dir=.git
```

rồi phân loại mọi hit.

---

# 9. TARGET DEPENDENCY GRAPH

```text
                         CLAUDE.md / governance
                                  │
                     activation + hard boundaries
                                  ▼
                              WRITER API
                         /          |          \
                        /           |           \
              Story Engine     Evidence      Retention Craft
              structure        verdict       optional prose support
                        \           |           /
                         \          |          /
                          └── narration work ─┘
                                  │
                                  ▼
                     immutable script version
                                  │
          ┌───────────────────────┼──────────────────────┐
          ▼                       ▼                      ▼
      audit/review             editor/apply          production
          │                       │                      │
          └──────────── artifact contracts ─────────────┘
                                  │
                                  ▼
                           analytics/postmortem
                                  │
                       governance/candidate path
                                  │
                    no direct mutation back to Writer
```

Research/topic selection feeds **resolved artifacts** into Writer from upstream, not raw competitor context.

---

# 10. MIGRATION CONSTRAINTS CHO 03B+

1. Keep Writer skill name stable unless owner explicitly chooses migration alias.
2. Keep mode ② activation semantics stable.
3. Preserve VI-first/EN-last behavior.
4. Preserve immutable script version + refs handoff.
5. Do not require downstream reviewers to read new Writer references.
6. Do not make Story Engine depend on Writer internals.
7. Do not make Writer depend on reviewer prompts.
8. Research/competitor data enters Writer only as resolved artifacts, not raw teardown context.
9. Retention Craft remains optional sentence-level peer.
10. Legacy reference paths may remain archived for provenance even after runtime stops loading them; no deletion without owner.
11. Before changing/deprecating any legacy path, run local grep to prove no hidden consumer.

---

# 11. CHECK — 03A-E

- [x] activation/data/implementation dependencies distinguished;
- [x] upstream callers/handoffs mapped;
- [x] Story/Evidence/Retention peer contracts mapped;
- [x] downstream review/editor/production consumers mapped;
- [x] main inspected consumers do not need Writer internals;
- [x] target dependency graph defined;
- [x] circular dependencies prohibited;
- [x] `/verify-claims` stale `evidence_locked` wording logged separately;
- [x] repository-wide grep limitation disclosed;
- [x] local grep requirement added for final verification;
- [x] Writer runtime unchanged.

**03A-E verdict:** `PASS — consumer boundaries permit an internal Writer refactor, subject to hidden-reference grep and authority conflicts recorded in 03A-C`.

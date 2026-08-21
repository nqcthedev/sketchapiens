# 03A-D — CONTEXT LOAD AUDIT — KIỂM TẢI NGỮ CẢNH WRITER

> **Status:** `READ-ONLY AUDIT ARTIFACT — NON-RUNTIME`  
> Không đổi cách load hiện tại. Task này đo/định loại context và đề xuất **load profile**, chưa refactor.

**Baseline:** checkpoint `dd6567266019b71f68218bb928ba7b60e9917204`

## Câu hỏi của task

Trong một phiên Writer bình thường, **context nào cần ngay, context nào chỉ cần khi task phát sinh, context nào không nên vào write mode**, và architecture hiện tại gây token/context risk ở đâu?

**Stop condition:** có target context profiles theo task moment mà không cần quyết file split cuối.

---

# 1. CLAUDE CODE LOADING FACTS — HÀNH VI NỀN TẢNG ĐÃ KIỂM

Đối chiếu docs Claude Code hiện hành ngày 2026-08-21:

1. skill description có thể hiện trong context để Claude biết skill tồn tại;
2. full `SKILL.md` chỉ load khi skill được invoke;
3. supporting files được khuyến nghị để **load detailed material only when needed**;
4. docs khuyên giữ skill body concise và dưới ~500 lines;
5. khi skill đã invoke, rendered content **stays in context across turns**;
6. khi auto-compaction, Claude Code re-attaches **first 5,000 tokens of each invoked skill**, với combined re-attachment budget 25,000 tokens, ưu tiên skill invoke gần nhất.

Official docs explicitly recommend:

```text
SKILL.md = overview + navigation
reference.md/examples.md = loaded when needed
```

### Audit implication

Progressive disclosure không chỉ là “chia file”. Nó đòi **entrypoint không inline/force-load material mà task chưa cần**.

---

# 2. CURRENT WRITER CONTEXT PATH — ĐƯỜNG LOAD HIỆN TẠI

## Before Writer invocation

Project session đã có / có thể có:

- `CLAUDE.md` control-plane instructions;
- applicable `.claude/rules/**` theo file/task;
- skill descriptions để routing.

Đây là expected project overhead, không phải Writer debt.

## When Writer invokes

Current wrapper (~3.4 KB) đưa active contract vào context, sau đó compatibility body trỏ trực tiếp tới:

```text
@references/runtime-monolith-legacy.md
```

Project hiện coi monolith này là **runtime body**, size **84,666 bytes**.

Trong monolith lại có instruction:

```text
luat-chung-ngach.md — ĐỌC MỖI LẦN VIẾT
```

size **29,727 bytes**.

Nếu instruction được thực thi, minimum writer-specific text path đã khoảng **114,393 bytes**, chưa tính:

- approved research/evidence;
- Story Engine khi cần structure;
- retention craft khi cần sentence-level polish;
- script draft itself;
- owner feedback / conversation history;
- other canonical writing docs nếu model phải resolve precedence.

**Không quy đổi byte → token thành một con số giả chính xác.** Kết luận đủ chắc là context rất lớn và gồm nhiều material không cần cho từng turn.

---

# 3. CONTEXT POLLUTION TYPES — CÁC LOẠI NHIỄU

## D-CTX-01 — Dead-rule pollution

Monolith + references chứa:

- strike-through rules;
- banners “đã chết”;
- old values;
- newer corrections;
- meta prose giải thích vì sao số cũ sai.

Model phải dành attention cho **negative instructions about things not to do** thay vì chỉ nhận active behavior.

## D-CTX-02 — Cross-mode pollution

Normal writing context có đường tới:

- topic/clone research;
- competitor teardown;
- packaging metadata;
- measurement history.

Các concern này thuộc thời điểm khác của workflow.

## D-CTX-03 — Authority-resolution pollution

Model phải giải các câu kiểu:

```text
PHẦN 13–14 thắng PHẦN 0–12
RUBRIC thắng HE_THONG
wrapper thắng legacy frontmatter
Story Engine thắng structural observation
```

Đây là work của architecture, không nên là cognitive task lặp lại mỗi lần viết câu.

## D-CTX-04 — Competitor voice priming

`viral-teardown`, `formula-and-example`, survival teardown chứa nhiều câu nguyên văn đối thủ dù có banner “không chép”. Load chúng trong write mode làm tăng nguy cơ style/phrase priming đúng lúc project muốn tạo prose gốc.

## D-CTX-05 — Structural duplication

Writer monolith mang hook/body/ending/transition formulas, trong khi Story Engine có canonical structure interface. Khi cả hai cùng context, model nhận hai cách mô tả cùng problem với authority khác nhau.

## D-CTX-06 — Compaction asymmetry risk

Current legacy file đặt corrections lớn ở **PHẦN 13–14 phía sau** PHẦN 0–12.

Claude Code docs nói after auto-compaction, invoked skill re-attachment giữ **first 5,000 tokens** của skill trong budget nhất định.

Nếu compatibility body được rendered/included như project dự kiến, architecture “luật cũ trước, correction cuối” có failure mode:

```text
pre-compaction:
old text + later correction đều còn

post-compaction:
first segment có thể được re-attach ưu tiên
later correction có thể không còn trong skill re-attachment
```

Active wrapper contract nằm đầu nên giảm rủi ro ở các conflict đã được wrapper khóa, nhưng **mọi legacy conflict chỉ được sửa ở cuối monolith vẫn không an toàn để phụ thuộc vào context persistence**.

**Classification:** architecture risk cần runtime test khi refactor, không khẳng định mỗi session chắc chắn bị mất correction.

---

# 4. REFERENCE LOAD CLASSIFICATION — PHÂN LOẠI LOAD

| Surface | Normal draft | Triggered only | Never in normal write | Reason |
|---|---:|---:|---:|---|
| current Writer public contract | ✅ | | | activation/workflow/hard boundaries |
| active narration principles | ✅ minimal subset | | | prose generation cần ngay |
| approved research/evidence packet | ✅ task input | | | nội dung video đang viết |
| Story Engine public interface | | ✅ khi structure/skeleton/join stress | | peer structural owner |
| Evidence verdict/detail | | ✅ khi claim/bridge cần verify | | không cần toàn evidence theory mọi câu |
| retention craft | | ✅ khi hook/pacing/landing craft issue | | support, không default rubric |
| VI→EN transformation guidance | | ✅ **chỉ sau VI approved** | | không cần trong Vietnamese drafting phase |
| topic/clone research workflow | | | ✅ | mode ①, trước write |
| competitor transcripts/teardowns | | | ✅ | research/calibration; priming risk |
| packaging metadata generation | | | ✅ | after script / packaging mode |
| historical measurement rationale | | | ✅ | audit/postmortem only |
| retired rule explanations | | | ✅ | provenance/debug only |
| full legacy monolith | | | ✅ target state | compatibility artifact, không phải target runtime |

`Never in normal write` không có nghĩa xóa file. Nó nghĩa **không auto-load trong mode ②**; vẫn có thể đọc ở audit/history/research task có lý do.

---

# 5. TARGET CONTEXT PROFILES — HỒ SƠ NGỮ CẢNH THEO MOMENT

Đây là interface requirement cho 03A-G/03B, chưa phải file layout.

## `WRITE_VI_DRAFT`

Load:

```text
Writer public contract
active prose/voice principles tối thiểu
current approved research/evidence anchors
current Story Map / structure output nếu đã có
current draft/batch + owner feedback
```

Không load:

```text
competitor corpus/teardowns
metadata generation
English rewrite implementation
historical measurements/dead rules
Mechanism Lab
full rubric history
```

## `WRITE_STRUCTURE_HANDOFF`

Writer giữ prose contract, invoke Story Engine public interface + needed structural references. Writer không load own duplicate structural theory.

## `WRITE_EVIDENCE_EXPRESSION`

Load evidence verdict/claim ledger **cho claims đang viết**, cùng guidance về cách diễn uncertainty. Không preload raw source taxonomy/history nếu verdict đã khóa.

## `WRITE_CRAFT_POLISH`

Chỉ khi vấn đề sentence-level rõ:

```text
Writer prose surface
retention-craft active interface
exact passage
```

Không kéo Story Engine vào chỉ vì đang polish sentence.

## `TRANSLATE_EN_FINAL`

Trigger chỉ sau VI approved:

```text
approved VI version
English narration transformation guidance
3 hard production constraints
voice/register target
```

Không reopen topic research/competitor teardowns.

## `PACKAGING`

Không phải Writer normal runtime. Packaging/title/metadata skill/owner riêng cần được resolution ở Phase 3/4 roadmap.

---

# 6. LOAD TRIGGER PRINCIPLE — NGUYÊN TẮC ROUTER

Future Writer entrypoint nên trả lời:

> “Task hiện tại cần quyết định gì, và file/module nào sở hữu đúng quyết định đó?”

không phải:

> “Có file reference nào liên quan từ khoá này thì đọc hết.”

Proposed trigger classes:

```text
workflow / batch / approval
→ Writer core workflow

voice / prose / wording
→ Writer prose guidance

structure / chapter / transition / promise-payoff
→ Story Engine

evidence support / bridge strength
→ Evidence system

hook wording / pacing / landing
→ Retention Craft when specifically needed

VI approved → final English
→ English transform guidance

research / competitor / clone swarm
→ leave write mode; research module

metadata / upload package
→ leave write mode; packaging concern

history / why old rule died
→ audit/provenance reference on demand
```

---

# 7. CONTEXT BUDGET IS NOT A BYTE TARGET

Không đặt acceptance kiểu:

```text
Writer must be < 10 KB
```

vì byte count không đo đúng creative sufficiency.

Đích là:

1. no known-dead rule in default generation context;
2. no raw competitor prose in normal write context;
3. no cross-mode implementation loaded by default;
4. canonical peer modules loaded only on relevant decision;
5. active prose guidance đủ để Writer không mất voice/craft;
6. context behavior survives compaction without relying on a later “override section”.

---

# 8. TESTABLE CONTEXT INVARIANTS CHO 03B+

Sau refactor phải test được:

### INV-D1
Normal VI draft không đọc `viral-teardown.md`, `formula-and-example.md`, `teardown-survival-cluster.md`.

### INV-D2
Normal VI draft không cần `metadata.md`.

### INV-D3
Structure request calls Story Engine; Writer không tự import duplicate structural mechanism file.

### INV-D4
EN rewrite guidance không có mặt trước owner approval của VI representation.

### INV-D5
Historical/dead-rule rationale không auto-load.

### INV-D6
After simulated long session/compaction, current hard Writer contract remains at top-level and no correctness depends on late override text.

### INV-D7
Removing legacy monolith from default context must not remove a required current behavior without replacement; smoke test against historical scripts/canary before deletion/retirement.

---

# 9. CHECK — 03A-D

- [x] platform load behavior checked against current official Claude Code docs;
- [x] current Writer load path mapped;
- [x] context pollution types classified;
- [x] all references assigned normal/triggered/never-normal profile;
- [x] VI draft / structure / evidence / craft / EN-final profiles defined;
- [x] compaction asymmetry risk documented without overclaim;
- [x] no arbitrary byte/token target introduced;
- [x] testable context invariants defined;
- [x] Writer runtime unchanged.

**03A-D verdict:** `PASS — progressive-disclosure requirements are concrete enough for dependency/consumer audit`.

## External verification sources

Claude Code official docs consulted 2026-08-21:

- `https://code.claude.com/docs/en/skills` — skill lifecycle + supporting files + compaction behavior.

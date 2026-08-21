# 03A-G — WRITER CONTRACT PROPOSAL — ĐỀ XUẤT HỢP ĐỒNG WRITER PHASE 3

> **Status:** `PROPOSAL ONLY — NON-RUNTIME — NOT YET CANONICAL`  
> File này là output của audit. Nó **không đổi Writer behavior**, không được auto-load trong normal video work và không tự thắng current runtime. Phase 3B phải triển khai + verify trước khi bất kỳ contract mới nào thành canonical.

**Baseline:** checkpoint `de5c05f18b3c6213f3e80a97da55f2905a56aec5`

## Mục tiêu

Đề xuất public contract tối thiểu cho `sketchapiens-viet-kich-ban` sao cho:

- Writer làm đúng nghề **biến approved knowledge/structure thành narration**;
- không kéo research/history/packaging vào normal write context;
- không tranh quyền với Story/Evidence/Retention;
- VI-first/EN-last và artifact lifecycle vẫn nguyên;
- legacy monolith có đường rollback/provenance, không bị xóa.

---

# 1. PROPOSED MODULE PURPOSE — MỤC ĐÍCH

`sketchapiens-viet-kich-ban` — **Bộ não viết lời Sketchapiens** tồn tại để:

> **Biến topic/promise + research đã được phép dùng + structural intent thành narration tự nhiên, rõ, có giọng riêng, đúng bằng chứng và phù hợp production contract.**

Nó **không** tồn tại để chọn thị trường, tự nghiên cứu đối thủ, tự phán bằng chứng, tự thiết kế toàn bộ story theory, tự review, hoặc làm packaging.

---

# 2. PROPOSED OWNERSHIP — WRITER SỞ HỮU GÌ

## 2.1 Prose realization — Hiện thực hóa thành câu chữ

Writer sở hữu:

- lựa chọn từ;
- nhịp câu;
- độ cụ thể;
- chuyển fact/scene/explanation thành lời nói nghe được;
- narrator voice/register trong active project constraints;
- final sentence choice.

## 2.2 Writing-session orchestration — Điều phối trong mode ②

Writer sở hữu **cách thực hiện phiên viết**, dưới control plane:

- viết theo batch;
- dừng cho owner feedback;
- tiếp tục từ current approved direction;
- không tự mở việc mode khác.

Project lifecycle/state vẫn thuộc `CLAUDE.md`/schema, không thuộc Writer.

## 2.3 Evidence expression — Diễn đạt độ chắc của bằng chứng

Writer được:

- diễn DIRECT claim rõ;
- diễn inference/speculation với mức chắc phù hợp verdict;
- kể paper/site/discovery như event nếu source support;
- làm citation/anchor nghe tự nhiên.

Writer **không** được tự issue Evidence verdict.

## 2.4 Vietnamese drafting — Viết bản Việt để owner duyệt bằng tai

Writer sở hữu prose của bản VI work-in-progress.

## 2.5 English final rewrite — Viết lại bản EN sau khi VI khóa

Writer sở hữu quality của English narration final, nhưng chỉ được chạy **sau owner approval của VI**.

---

# 3. PROPOSED NON-OWNERSHIP — WRITER KHÔNG SỞ HỮU

## Topic / market / competitor research

Owner: research/topic-selection workflow.

Writer receives resolved input; no raw competitor corpus in write mode.

## Story structure

Owner: `sketchapiens-story-engine`.

Writer may notice a structure problem and request Story Engine help, but does not maintain a duplicate structural theory.

## Factual verdict / claim locking

Owner: Evidence system / Evidence Prosecutor / claim ledger.

## Sentence-level retention theory

Support owner: Retention Craft. Writer owns actual prose choice, not benchmark/rubric authority.

## Review verdict

Owners: role-specific reviewers + owner triage. Writer does not self-certify.

## Packaging

Title/topic/thumbnail/metadata are outside normal Writer ownership. Story promise may be an **input constraint**, not a Writer packaging decision.

## Production

Writer does not create shot prompts/images/TTS/thumbnail inside narration drafting.

## Analytics / mechanism promotion

Writer cannot turn one outcome/competitor pattern into a channel rule.

## Historical rule arbitration

Writer should not resolve “old section vs new section” at runtime. Architecture/governance must provide only current behavior.

---

# 4. HARD INVARIANTS — BẤT BIẾN ĐỀ XUẤT

These are not “style preferences”:

1. **VI first.** Draft/revise Vietnamese until owner approves.
2. **EN last once.** Rewrite by meaning after VI approval; no machine-like sentence translation.
3. **No EN+VI side-by-side approval table.**
4. **Three narration constraints only:** `! = 0` · no dash inside sentence · one sentence per line.
5. **No raw competitor corpus/teardown during normal writing.**
6. **Original work.** No paraphrase/reused beat chain from competitor source.
7. **Length follows topic/production need, not universal quality target.**
8. **Story structure routes to Story Engine.** No mechanism quota.
9. **Evidence verdict routes to Evidence system.** Writer does not upgrade inference into fact.
10. **No owner-only ref mutation.** Writer does not set `approved`/`published` refs.
11. **No pending experimental rule in active generation contract.** In particular D-27 seven rulers remain outside until owner decision/promotion path.
12. **No hidden cross-mode work.** Research/packaging/production debt is surfaced, not executed inside mode ②.

---

# 5. INPUT CONTRACT — ĐẦU VÀO

Writer should accept **resolved artifacts/information**, not upstream implementation details.

## Required or explicitly missing

```text
VIDEO ID / path
CURRENT MODE / lifecycle state
SELECTED TOPIC
CURRENT TITLE / STORY PROMISE if one exists
APPROVED RESEARCH / evidence anchors allowed for this batch
CURRENT STRUCTURAL INTENT / Story Map if structure already exists
CURRENT SCRIPT VERSION / draft if continuing
OWNER FEEDBACK / decisions from prior batch
REAL PRODUCTION CONSTRAINTS relevant to narration
```

If one is missing, Writer reports it. It does not silently fill missing research by reading competitors.

## Structure input rule

If structure is not ready and task needs structural decisions:

```text
Writer → Story Engine → Story Map / diagnosis → Writer prose
```

## Evidence input rule

If a factual bridge lacks verdict/support:

```text
Writer marks need → Evidence workflow → verdict → Writer expression
```

No “safe-sounding hedge” may be used merely to keep an unsupported claim.

---

# 6. OUTPUT CONTRACT — ĐẦU RA

## `VI_DRAFT_BATCH`

Default writing output before owner approval:

- narration only unless caller explicitly requests a supporting artifact;
- one sentence per line;
- current batch scoped to agreed structure;
- factual uncertainty consistent with evidence;
- no image prompts / metadata / competitor analysis mixed in.

After a batch, **STOP for owner feedback**.

## `VI_LOCKED`

Owner-only milestone, not Writer self-declaration.
Writer can prepare next representation only after clear owner approval.

## `EN_FINAL_NARRATION`

After VI lock:

- rewrite by meaning into natural spoken English;
- preserve approved claims, logic, stakes and structural intent;
- maintain 3 narration hard constraints;
- do not introduce new factual claims silently;
- if English adaptation requires factual change/addition, route back through Evidence.

## Artifact behavior

When content is persisted:

```text
03-script/versions/vNNN.md = immutable version
03-script/refs/current.yaml = mutable working pointer
approved/published refs = owner-only
```

Writer contract describes expected artifact behavior; schema/rules remain canonical owner of exact shape/state.

---

# 7. CONTEXT ROUTER — BỘ ĐỊNH TUYẾN NGỮ CẢNH

Proposed `SKILL.md` should operate like a public API/router.

## Normal VI drafting

```text
load: core Writer contract + active prose guidance + current task artifacts
avoid: legacy/history/research/packaging
```

## Structure issue

```text
invoke Story Engine
load only structural context it owns
return diagnosis/map to Writer
```

## Evidence-expression issue

```text
load evidence-expression guidance
consume current claim verdict/ledger
```

## Sentence-level craft issue

```text
optionally invoke Retention Craft
```

## English-final stage

```text
only after owner VI approval
load english-rewrite guidance
```

## “Why did we kill this old rule?”

```text
explicit audit/history task only
open legacy/provenance reference on demand
```

## Topic / clone / competitor research

```text
leave Writer mode → research workflow
```

## Metadata / thumbnail / upload package

```text
leave Writer normal mode → packaging concern
```

---

# 8. POSITIVE PROSE GUIDANCE — TARGET CONTENT, KHÔNG PHẢI RULE PILE

Future active prose reference should contain **positive, current, non-numeric guidance** such as:

- spoken, concrete, imageable language;
- explain mechanism before ornament;
- sentence rhythm serves thought;
- humor optional, specific and short when used;
- avoid empty profundity / slogan-like aphorism;
- evidence can be narrated as a discovery/event;
- use exact named objects/sites/people when evidence supports and it improves clarity;
- preserve continuity after cuts/inserts;
- write the strongest version now, not a placeholder waiting for review.

It should **not** contain:

- view-causality claims from winner presence;
- timing/density quotas;
- competitor verbatim phrase banks;
- dead-rule tombstones;
- “new section overrides old section” prose;
- Story Engine formulas;
- Evidence taxonomy as Writer-owned logic;
- packaging instructions.

---

# 9. TARGET MODULE SHAPE — HÌNH DẠNG TỐI THIỂU ĐỀ XUẤT

Do not create files merely for symmetry. Minimum useful target:

```text
.claude/skills/sketchapiens-viet-kich-ban/
├── CONTRACT.md                     # canonical ownership/boundaries after approval
├── SKILL.md                        # thin runtime interface + context router
├── references/
│   ├── prose-and-voice.md          # active positive narration craft
│   ├── evidence-expression.md      # how to express verdicts, not issue them
│   ├── english-final-rewrite.md    # loaded only after VI approval
│   └── runtime-monolith-legacy.md  # preserved history/rollback; NOT default runtime
├── tests/                          # only if regression harness proves useful
└── audit/                          # Phase 3 audit records, non-runtime
```

### Why no `workflow.md` by default?

Writer workflow is short enough to live in `SKILL.md` unless implementation proves it bloats routing. Do not split only because Story Engine has a workflows file.

### Why no `niche-rules.md` by default?

Current quality sources are mixed-authority and historically unstable. Target Writer should extract **prose implementation guidance**, not create a second “channel rules” source.

### Why keep legacy path unchanged?

Rollback/provenance and possible hidden references. Stop auto-loading it first; rename/move/delete only after grep/tests + owner decision.

---

# 10. SOURCE-OF-TRUTH PROPOSAL — CHỈ ÁP SAU KHI IMPLEMENTATION PASS

After Phase 3B runtime verifies, add a SoT row conceptually like:

```text
Narration generation / Writer orchestration / prose realization
→ .claude/skills/sketchapiens-viet-kich-ban/CONTRACT.md
→ runtime entry: .../SKILL.md
```

Boundary note:

```text
structure → Story Engine
factual verdict → Evidence
sentence-level craft support → Retention Craft
artifact schema → video.schema/script-files
research/topic → topic research
packaging → packaging owners
```

Do **not** update SoT before target contract exists and passes regression.

---

# 11. STOP CONDITIONS — WRITER BIẾT KHI NÀO DỪNG

Writer should stop/hand off when:

1. current batch is complete and owner feedback is required;
2. next move is structural rather than prose → Story Engine;
3. required claim lacks evidence verdict → Evidence;
4. task asks for competitor/market research → research mode;
5. VI is not owner-approved but caller asks for final EN → block and request/await approval;
6. script is complete and remaining work is review → audit/editor workflow;
7. remaining work is packaging/production → leave Writer mode;
8. additional changes would only satisfy a framework/metric rather than fix a concrete weakness.

---

# 12. PROPOSED PHASE 3B TASK CHAIN — TRIỂN KHAI SAU 03A-H

Phase 3B should also be subdivided:

```text
03B-A — Lock Writer Contract
        create actual CONTRACT.md from audited proposal

03B-B — Extract Active Prose Guidance
        build prose-and-voice.md from ACTIVE/SUPPORTING salvage only

03B-C — Build Conditional References
        evidence-expression + english-final-rewrite

03B-D — Thin Runtime Router
        replace compatibility SKILL with target public interface/context router

03B-E — Detach Legacy Default Runtime
        remove default monolith load; preserve legacy file/path

03B-F — Integration & Source-of-Truth Sync
        consumer routing + SoT + lifecycle wording drifts that are truly coupled

03B-G — Writer Regression Fixtures
        test VI-first, structure handoff, evidence boundary, no competitor leak,
        EN-after-approval, artifact semantics, legacy isolation

03B-H — Runtime Verification & Checkpoint
        compare behavior + project_doctor + canary readiness
```

Each task gets its own CHECK + checkpoint. No mass rewrite.

---

# 13. REGRESSION INVARIANTS — PHẢI BẢO VỆ

## R-G1 — VI-first

Prompt for new script must not output final English before VI approval.

## R-G2 — No competitor leakage

Normal write session must not load/use teardown/corpus phrase bank.

## R-G3 — Structural deference

When faced with genuine structure decision, Writer routes to Story Engine rather than forcing legacy 6-beat/3–7-layer/bookend formula.

## R-G4 — Evidence deference

Writer does not self-classify support or keep unsupported claim via vague hedge.

## R-G5 — Prose capability retained

Removing monolith must not collapse narration into bland factual list. Historical script surfaces should still receive concrete, spoken, varied prose.

## R-G6 — No rule resurrection

Test prompts must not cause `I≈0`, humor cadence, anchor density, fixed length, question timing, mandatory viewer-lane, D-27 item quota to return as requirements.

## R-G7 — EN stage gated

English transformation only after explicit owner-approved VI state/input.

## R-G8 — Artifact safety

Writer never overwrites immutable version or self-sets approved/published.

## R-G9 — Cross-mode isolation

Metadata/image prompts/topic research are not produced merely because legacy Writer used to contain them.

## R-G10 — Compaction safety

Correct active behavior must not depend on a late override section surviving context compaction.

---

# 14. OPEN ISSUES THAT CONTRACT CAN AVOID BUT NOT ERASE

## O-G1 — FLOW structural prescriptions vs Story Engine

Proposed Writer contract routes structure to Story Engine and therefore does not duplicate FLOW structural formulas.

However FLOW itself still contains them. Before Phase 3 is declared stable, governance/integration must decide whether to:

- reword FLOW as gate/process only;
- explicitly defer structural choices to Story Engine;
- or obtain owner decision for any genuinely intended universal structural behavior.

## O-G2 — RUBRIC LUẬT 0 vs Kịch tính thresholds

Writer contract should treat quality gates as external review workflow and not hard-code numeric thresholds. Conflict remains in RUBRIC and needs separate owner/governance resolution if it affects canary decisions.

## O-G3 — Metadata ownership

Do not solve inside Writer. Packaging architecture can resolve later.

## O-G4 — `/verify-claims evidence_locked` lifecycle wording

Fix as integration drift; do not reintroduce state.

## O-G5 — D-27 stale path + pending seven rulers

Update path separately. D-27 remains pending until owner decision; target Writer must keep it out of active runtime meanwhile.

## O-G6 — project_doctor import side effect

`project_doctor.py` lacks `if __name__ == '__main__'`; separate deterministic testability debt, unrelated to Writer contract.

---

# 15. CHECK — 03A-G

- [x] purpose defined;
- [x] ownership/non-ownership defined;
- [x] hard invariants limited to current supported behavior;
- [x] input/output contracts defined;
- [x] context router defined;
- [x] target module shape minimal, not symmetry-driven;
- [x] legacy rollback/provenance preserved;
- [x] SoT change deferred until runtime contract passes;
- [x] Phase 3B subdivided into small tasks;
- [x] regression invariants defined;
- [x] pending D-27 not promoted;
- [x] known external conflicts kept visible;
- [x] Writer runtime unchanged.

**03A-G verdict:** `PASS — contract proposal is implementation-ready, subject to final 03A-H audit verification`.

# 03A-F — LEGACY / DEAD MATERIAL CLASSIFICATION — PHÂN LOẠI VẬT LIỆU KẾ THỪA

> **Status:** `READ-ONLY AUDIT ARTIFACT — NON-RUNTIME`  
> Không xóa, di chuyển hoặc sửa Writer runtime. Task này chỉ phân loại tri thức hiện có để Phase 3B không vứt nhầm knowledge hữu ích và cũng không giữ dead/pending material trong normal write context.

**Baseline:** checkpoint `1023044eeb0e636722fe36e5a33eb2bf4a842660`

## Câu hỏi của task

Legacy Writer đang chứa những gì còn sống, những gì chỉ nên dùng làm craft support / research / provenance, những gì đã chết, và những gì **chưa được owner promote nhưng đang nằm trong runtime**?

**Stop condition:** mọi surface lớn của monolith + 6 reference được gắn class và disposition; không tự promote D-27 hoặc luật mới.

---

# 1. CLASSIFICATION LABELS

- `ACTIVE` — behavior hiện hành đã được control plane/canonical source xác nhận.
- `SUPPORTING` — craft/knowledge có thể hữu ích theo trigger, nhưng không phải hard rule.
- `RESEARCH_ONLY` — dùng ở research/calibration mode, không normal write.
- `PENDING` — observation/proposal đang chờ human/governance decision.
- `HISTORICAL` — provenance/counterexample/lý do thay đổi; không runtime instruction.
- `DEAD` — đã bị bác/retire; không được dùng để generate/review.
- `MISPLACED` — có thể còn hữu ích nhưng nằm sai module/mode.
- `MIXED` — file chứa nhiều class; không được auto-load nguyên file.

---

# 2. TOP-LEVEL VERDICT

## `runtime-monolith-legacy.md`

**Class:** `MIXED — HISTORICAL COMPATIBILITY ARTIFACT`

Không thể gọi toàn file là DEAD vì trong đó còn nhiều nguyên tắc/craft observation hữu ích. Nhưng cũng không thể gọi nó ACTIVE vì:

1. frontmatter cũ mâu thuẫn active wrapper (English-first, 2-column, 8–25 min);
2. PHẦN 0–12 chứa nhiều rule đã bị chính file strike-through / correction;
3. PHẦN 13–14 ngày 09/08 là measurement/countercheck layer, không phải toàn bộ creative contract;
4. cuối file lại append **một PHẦN 13 thứ hai** ngày 19–20/08;
5. PHẦN 13 mới chứa 7 thước đang chờ `D-27 NEEDS_HUMAN_DECISION`;
6. monolith vừa chứa workflow, structure, voice, research, evidence, output, packaging, history và experimental observations.

**Target disposition:** preserve byte-for-byte as historical compatibility/provenance until migration is verified, nhưng **không normal-runtime-load** sau refactor.

---

# 3. DUPLICATE `PHẦN 13` — AMBIGUOUS PRECEDENCE BUG

Monolith có ít nhất hai heading cùng tên:

### `PHẦN 13` A — đo 16 kênh / 09-08

Chứa:
- bỏ promise-hoãn;
- bỏ self-deprecation hook;
- bỏ greeting/persona;
- transition observations;
- evidence naming/register observations;
- hook-as-floor conclusion;
- nhiều counterexamples chống template.

Phần này chủ yếu là **MEASURED/HISTORICAL/SUPPORTING**, và một số kết luận đã được canonical layer khác hấp thụ.

### `PHẦN 13` B — 7 thước từ 8 quả nổ mạch đêm / 19–20-08

Chứa:
- VI-first / EN-last workflow evidence;
- “không dùng code để chấm script” observation;
- số món độc lập;
- hook density;
- sentence rhythm ranges;
- belief flip;
- mini-story ending short;
- named sourcing;
- shared anchors not fatal;
- visualizable-item mix.

Governance `D-27` nói rõ **bảy thước này chưa được chủ nâng thành luật**, trạng thái `NEEDS_HUMAN_DECISION`.

### Consequence

Banner đầu monolith nói:

```text
PHẦN 13 và 14 thắng PHẦN 0–12
```

Nhưng sau append, `PHẦN 13` không còn là một identity duy nhất. Runtime model phải đoán “13 nào”, và một trong hai chứa material chưa promote.

**Verdict:** `AMBIGUOUS PRECEDENCE + PENDING-KNOWLEDGE LEAK`.

Không sửa trong 03A-F. 03A-G phải yêu cầu target Writer không dùng heading-history để resolve authority.

---

# 4. MONOLITH BLOCK CLASSIFICATION

| Block | Class | Lý do | Target disposition |
|---|---|---|---|
| legacy frontmatter/routing | `DEAD / HISTORICAL` | active wrapper + CLAUDE đã thay | preserve only for provenance |
| mode ② no-competitor-writing boundary | `ACTIVE` concept | phù hợp current control plane | extract into thin Writer contract, không giữ whole block |
| per-chapter device checklist | `MIXED SUPPORTING + DEAD` | chính block nói diagnostic not shopping list, nhưng vẫn chứa quotas/blind-promise expectations | salvage diagnostic principle only; craft refs triggered |
| PHẦN 0 philosophy | `MIXED` | “framework not cage” còn hợp; nhiều “about YOU” thesis cũ chết | extract philosophy, discard dead claims from runtime |
| PHẦN 1 title/topic | `MISPLACED + MIXED` | title/research owner ở upstream/packaging; nhiều old heuristics | remove from normal Writer; research module owns |
| PHẦN 2 hook formulas | `SUPPORTING + HISTORICAL` | hook craft có giá trị nhưng structural/template claims đã counterchecked | trigger Retention Craft / voice support only |
| PHẦN 3 body structure | `DUPLICATE + STALE` | structural authority nay Story Engine | no Writer structural authority |
| batch-writing workflow | `ACTIVE` behavior | current project still uses owner review batches | keep in Writer orchestration contract if still intended |
| PHẦN 4 voice/tone | `MIXED SUPPORTING` | prose register hữu ích; tone taxonomy/quasi-rules không canonical | extract active prose principles, keep examples historical |
| PHẦN 5 science/evidence expression | `ACTIVE BOUNDARY + DUPLICATE` | Writer needs expression; Evidence owns verdict | keep only expression contract + handoff |
| PHẦN 6 ending formulas | `DUPLICATE / SUPPORTING` | structural ending owned Story Engine; sentence landing craft may help | split structure vs craft |
| PHẦN 7 originality/reuse | `ACTIVE BOUNDARY` | policy/reuse still important, but source canonical outside Writer | Writer consumes policy constraints |
| PHẦN 8 old output table/visual cues | `DEAD / MISPLACED` | VI-first narration + artifact pipeline superseded old EN table; visuals belong production | remove from target runtime |
| PHẦN 9 old default workflow/checklist | `MIXED STALE` | duplicates flow, structure, research, QA | replace by thin orchestration; no mega-checklist |
| PHẦN 10 upgrades | `MIXED` | contains packaging/research/anti-AI/evidence/structure concerns; multiple later corrections | classify per concern, not carry as block |
| PHẦN 11 technique bank | `SUPPORTING / HISTORICAL` | craft/taste examples, competitor-derived | triggered calibration only; never canonical rule |
| PHẦN 12 comedy machine | `SUPPORTING + DEAD QUOTAS` | quota explicitly killed; mechanisms may remain useful craft | craft reference only if humor needed |
| PHẦN 13-A 16-channel measurements | `HISTORICAL / SUPPORTING` | empirical observations + counterexamples | R&D/provenance, selectively promoted elsewhere |
| PHẦN 14 structure countercheck | `HISTORICAL / SUPPORTING` | powerful anti-template evidence; structure owner now Story Engine | preserve provenance; canonical lesson already in Story Engine anti-template stance |
| PHẦN 13-B 8 night winners | `PENDING` | D-27 not owner-approved as channel rules | isolate from normal runtime until governance decision |

---

# 5. REFERENCE FILE CLASSIFICATION

## `luat-chung-ngach.md`

**Class:** `MIXED — LEGACY DERIVED KNOWLEDGE`.

Strong warning already says file contains dead rules and was missed by earlier audit. It still says **READ EVERY TIME**, which conflicts with progressive disclosure target.

Useful material exists as measured/craft observations, but:
- many “law” labels were derived from small samples;
- several central premises were later killed;
- structure/title/retention authority now lives elsewhere.

**Target:** do not auto-load. Salvage only active principles into canonical owners; retain file as historical derived knowledge until retirement/migration decision.

## `quy-trinh-nghien-cuu-cum.md`

**Class:** `RESEARCH_ONLY + MIXED STALE`.

It explicitly requires competitor transcript collection and live market work and says it runs **before write mode**. Therefore it does not belong in narration Writer runtime regardless of whether individual research methods remain useful.

Several rules inside are stale/overbroad, e.g. anchor-burning logic and “sweet spot” requirements that later measurements complicate.

**Target:** research/topic-selection concern outside Writer; preserve provenance until research module cleanup.

## `teardown-survival-cluster.md`

**Class:** `RESEARCH_ONLY / CALIBRATION / HISTORICAL`.

Value:
- cluster-specific competitor patterns;
- burned-anchor observations;
- useful case studies/counterexamples.

Risk:
- competitor prose priming;
- multiple mechanisms later declared dead;
- cluster heuristics can masquerade as universal writing law.

**Target:** research/calibration only, never normal Writer context.

## `viral-teardown.md`

**Class:** `HISTORICAL / CALIBRATION` with large `DEAD` content.

The file itself says **7/8 sections contain rules later disproved**. Remaining value is scientific-anchor craft, one high-level engine observation, and competitor examples for taste calibration.

**Target:** no runtime authority; history/calibration only.

## `formula-and-example.md`

**Class:** `CALIBRATION / HISTORICAL`, not canonical instruction.

It exists to “calibrate taste — do not copy” and contains competitor examples plus old structural formulas. Several central prescriptions are explicitly struck through or contradicted by later corpus work.

**Target:** optional historical craft example only, preferably outside normal write session to avoid voice priming.

## `metadata.md`

**Class:** `MISPLACED PACKAGING-ONLY + MIXED STALE`.

The file itself says **only after script is complete**. Title ownership is already elsewhere, description/tags ownership is unresolved, and several SEO/translation assumptions are corrected in-place.

**Target:** remove from Writer normal runtime. Resolve canonical packaging owner before migration.

---

# 6. IMPORTANT ACTIVE KNOWLEDGE THAT MUST NOT BE LOST

03A-F is not a delete plan. The following ideas appear useful/current enough that Phase 3B must preserve them **through the right owner/interface**, not by keeping monolith loaded:

1. **VI-first → owner approval → EN rewrite once** — already active in wrapper/CLAUDE.
2. **No raw competitor corpus during write mode** — active boundary.
3. **Three hard narration constraints only** — control-plane rule.
4. **Frameworks are diagnostics, not quotas/templates** — consistent with Story Engine and current quality philosophy.
5. **Batch writing / owner steering** — current Writer workflow behavior unless 03A-G finds contrary canonical decision.
6. **Writer owns prose/voice, not structure/evidence verdict.**
7. **Evidence can be narrated vividly without weakening factual discipline** — expression principle, not evidence verdict.
8. **Read-aloud / natural spoken delivery / reread surrounding passage after edits** — craft/editor behavior, subject to owner/governance status where applicable.
9. **Concrete nouns/scenes beat abstract prose when explaining** — supporting narration craft, not numeric quota.
10. **Originality/reuse boundary** — must remain, but policy source stays outside Writer.

These are preservation requirements, not proof that the legacy paragraphs containing them should survive in runtime.

---

# 7. PENDING MATERIAL FIREWALL

## D-27

The seven night-corpus measures are **not ACTIVE Writer rules** merely because they are newer than PHẦN 0–12.

Target behavior until owner decision:

```text
D-27 material
→ PENDING / experimental observation
→ may be inspected in R&D/audit
→ must not become normal Writer requirement
→ must not be scored by reviewer
→ must not be encoded as hard threshold/template
```

Specific examples that must not silently leak as requirements:

- “≥8 independent items”;
- “hook ≥1.4/minute”;
- prescribed long/short sentence ranges;
- every item must end in 1–3 short punch sentences;
- fixed four-item weight checklist.

Even if some later prove valuable, promotion requires the governance path.

---

# 8. DEAD MATERIAL — DO NOT RESURRECT

This task reconfirms recurring dead families already explicitly marked in sources:

- `I ≈ 0`;
- mandatory self-deprecating human joke in hook;
- mandatory “about YOU” lane;
- promise/tease “best part later” / circle-back as required mechanic;
- fixed humor cadence;
- fixed question cadence;
- fixed anchor density;
- fixed chapter word range;
- fixed you:we ratio;
- mandatory persona;
- mandatory callback/bookend as scoring item;
- mandatory mystery;
- fixed macro body count / 6–11 chapters as quality rule;
- rigid hook beat count as quality rule;
- “all evidence already used by competitors is burned” as universal anti-reuse rule.

Preserving history is allowed. Runtime generation must not treat these as active requirements.

---

# 9. MIGRATION PRINCIPLE DERIVED FROM CLASSIFICATION

Do **not** refactor by mechanically slicing monolith headings into files.

Correct migration unit is:

```text
responsibility + authority + runtime trigger
```

not:

```text
PHẦN 1 → file1
PHẦN 2 → file2
...
```

Reason: a single legacy heading often contains ACTIVE + DEAD + PENDING + wrong-module material at once.

---

# 10. CHECK — 03A-F

- [x] monolith classified by responsibility/block;
- [x] all six side references classified;
- [x] duplicate `PHẦN 13` identified;
- [x] D-27 pending knowledge isolated conceptually;
- [x] dead-rule families listed;
- [x] active knowledge preservation list created;
- [x] no runtime file modified;
- [x] no pending mechanism/rule promoted;
- [x] no deletion performed.

**03A-F verdict:** `PASS — legacy material is sufficiently classified for Writer contract design`.

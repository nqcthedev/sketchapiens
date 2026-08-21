# 03A-F — LEGACY / DEAD MATERIAL CLASSIFICATION — PHÂN LOẠI VẬT LIỆU KẾ THỪA

> **Status:** `READ-ONLY AUDIT ARTIFACT — NON-RUNTIME`  
> Không xóa, di chuyển, sửa hay retire runtime material trong task này. Mục tiêu là **không làm mất hiểu biết tốt khi refactor**, đồng thời không kéo luật chết/pending experiment vào target runtime.

**Baseline:** checkpoint `1023044eeb0e636722fe36e5a33eb2bf4a842660`

## Câu hỏi của task

Trong monolith + Writer references, phần nào là active behavior cần bảo toàn, phần nào chỉ là supporting craft, phần nào historical/provenance, phần nào đã chết, phần nào thuộc module/mode khác, và phần nào **chưa được owner duyệt**?

**Stop condition:** có salvage map đủ để 03A-G đề xuất contract mà không “rewrite from vibes”.

---

# 1. CLASSIFICATION LABELS

- `ACTIVE` — behavior hiện được control plane/owner/canonical source xác nhận; target Writer phải bảo toàn.
- `SUPPORTING` — craft/knowledge hữu ích nhưng không hard rule; load theo nhu cầu.
- `MOVE-LATER` — có thể vẫn active nhưng **không thuộc normal Writer runtime**; owner/module khác hoặc mode khác.
- `HISTORICAL` — provenance/measurement/rationale hữu ích cho audit/R&D, không generation context.
- `DEAD` — đã bị retire/bác/override rõ; không được tái sinh trong target runtime.
- `PENDING` — observation/proposal đang chờ owner/governance; không được coi là active.
- `MIXED` — file/section chứa nhiều trạng thái, bắt buộc extract chứ không migrate wholesale.

---

# 2. CRITICAL FILE-LEVEL FINDING — MONOLITH KHÔNG CÓ MỘT “LATEST SECTION” RÕ

`runtime-monolith-legacy.md` hiện có:

```text
PHẦN 0–12      older body
PHẦN 13        measurement/corrections dated 09/08
PHẦN 14        structural countercheck dated 09/08
PHẦN 13        a second, newly appended section dated 19–20/08
```

Banner đầu monolith nói:

> “PHẦN 13 và 14 là bản mới nhất. Khi PHẦN 0–12 nói ngược PHẦN 13–14 → nghe 13–14.”

Sau khi PHẦN 13 mới được append **sau PHẦN 14**, reference “PHẦN 13” trở thành ambiguous.

### Classification

`ARCHITECTURE DEFECT / HISTORICAL APPEND LOG`, không phải acceptable runtime precedence model.

### Consequence

03B **không được** cố “giữ nguyên precedence bằng cách copy PHẦN 13 mới nhất”. Phải extract behavior theo canonical owner/status, không theo số section.

---

# 3. ACTIVE SALVAGE — NHỮNG THỨ PHẢI GIỮ Ở TARGET WRITER

Các behavior dưới đây có support ngoài monolith và được coi `ACTIVE`:

## A-01 — VI-first → owner approval → EN once

```text
Vietnamese draft
→ owner listens/revises/approves
→ English rewrite by meaning once
```

Source hiện hành: `CLAUDE.md` + Writer wrapper. Monolith PHẦN 13 mới chỉ là historical rationale bổ sung.

**Keep behavior, not 18-translation incident prose.**

## A-02 — No side-by-side EN+VI approval table

Active project workflow. Keep concise contract; history V19 lệch 22 dòng belongs provenance.

## A-03 — Three hard narration constraints

- `!` = 0;
- no dash/em-dash inside sentence;
- one sentence per line.

`I ≈ 0` is DEAD.

## A-04 — Original work / no competitor corpus while writing

Active in `CLAUDE.md` + wrapper + policy boundary.

## A-05 — Topic-driven length, not fixed quality target

No 8–25m / 15–20m / ~1,500-word universal quality target. Duration can be estimated for production, not optimized as a score.

## A-06 — Batch writing + owner checkpoints

`CLAUDE.md` explicitly says write in batches; monolith rationale is supporting history.

## A-07 — Writer owns final prose; structure/evidence verdict owned elsewhere

Phase-2 canonical boundary. Target Writer must preserve this dependency contract.

## A-08 — Immutable script versions + mutable refs

Artifact behavior from schema/rules. Writer target must output into that contract, even though legacy monolith never natively implemented it.

---

# 4. SUPPORTING SALVAGE — CRAFT TỐT, KHÔNG NÂNG THÀNH LUẬT

These are useful **if expressed as diagnostic/craft guidance**, not quotas/templates.

## S-01 — Concrete over abstract prose

Prefer named objects/scenes/actions over vague grand statements when it improves comprehension/visualization.

## S-02 — Sentence rhythm as function, not quota

Longer lines can carry explanation/listing; shorter lines can land a point. No required percentages/word ranges.

## S-03 — Humor mechanisms as optional craft

Deadpan, anachronism, bathos, personification, comic list etc. can work. **No required density, no required number of mechanisms, no chapter must contain a joke.**

## S-04 — Evidence can be entertaining

Named researcher/site/artifact + discovery process can become story material rather than dry citation. Must remain within Evidence boundary.

## S-05 — Read aloud / reread surrounding paragraph after edits

Useful craft/continuity practice. Do not promote latest “10 breaks” measurement into law without governance, but principle itself is compatible with editor/read-aloud workflow.

## S-06 — No greeting/channel-intro early as craft observation

Already retained in Retention Craft as guidance, not a hard gate.

## S-07 — Anti-AI smell diagnostics

Avoid empty profundity, stacked metaphors, trailer cadence, abstract aphorisms when they sound artificial. Canonical operational reviewer is Anti-AI critic/editor; Writer can own positive prose craft without duplicating reviewer rubric.

## S-08 — Chapter/item must have a reason to exist

Diagnostic question “remove this block, what breaks?” is useful, but **structural authority belongs Story Engine**. Keep via Story Engine, not Writer copy.

---

# 5. MOVE-LATER — CÓ GIÁ TRỊ NHƯNG SAI MODE/OWNER

## M-01 — Topic/title/clone research

`quy-trinh-nghien-cuu-cum.md` + monolith topic validation/title selection.

**Destination:** mode ① / topic-research system. Writer receives resolved topic/title/promise artifact.

## M-02 — Raw competitor teardown/calibration

- `viral-teardown.md`;
- `formula-and-example.md`;
- `teardown-survival-cluster.md`;
- verbatim competitor phrase banks inside monolith.

**Destination:** research/provenance/calibration on demand, never normal write runtime.

## M-03 — Story structure formulas

Hook skeletons, 3–7 layers, chapter order, but/therefore causality, bookend requirements, blind-promise transition formulas, mystery/reframe skeletons.

**Destination:** Story Engine decides structural use; measurements can live as history/candidates, not Writer authority.

## M-04 — Evidence verification mechanics

Web verification, DIRECT/INFERENCE classification, claim locking.

**Destination:** Evidence system / `/verify-claims`. Writer keeps only evidence-aware **expression**.

## M-05 — Anti-AI review pass

Detailed detection belongs Anti-AI critic/editor. Writer keeps positive voice guidance, not self-scoring rubric.

## M-06 — Packaging metadata

`metadata.md`, upload title/description/tags/file-name theories.

**Destination:** packaging concern after ownership resolution. Do not migrate wholesale because source itself contains dead/unverified rules.

## M-07 — Thumbnail concepts / visual prompt workflow

Legacy PHẦN 8/10 packaging and image prompt behavior.

**Destination:** thumbnail/production modules. Writer normal mode should not create image prompts while prose is changing.

## M-08 — YouTube policy verdicts

Originality/reuse policy must come from policy SoT. Writer implements safe/original narration but does not carry policy research history.

---

# 6. DEAD MATERIAL — KHÔNG ĐƯỢC TÁI SINH

Explicitly dead/stale examples found in monolith/references:

## D-01 — Legacy frontmatter/output contract

- English-first as default;
- two-column/three-column bilingual approval output;
- 8–25 minute quality target.

## D-02 — `I ≈ 0`

Retired.

## D-03 — “Topic must be about YOU / modern viewer lane” as universal strategy

Explicitly killed by later measurement; current niche direction is not allowed to depend on it.

## D-04 — Mandatory self-deprecating-human joke

Explicitly killed.

## D-05 — Mandatory narrator persona

Explicitly killed.

## D-06 — Humor every 30–60 sec / aside every 40–60 sec / anachronism cadence

Explicitly killed.

## D-07 — Delayed-payoff / “save best for end and announce it” formula

Explicitly killed as universal behavior.

## D-08 — Fixed hook timing / question-before-N-seconds targets

Explicitly killed.

## D-09 — Fixed chapter count / length ranges as quality target

`6–11 chapters`, `183–341 words`, `2–4 short sentences`, etc. do not survive countercheck as hard targets.

## D-10 — Anchor-density targets

3+/minute, 5+/minute and similar. Explicitly killed.

## D-11 — You:we ratio / narrator pronoun density

Explicitly killed.

## D-12 — Setup/payoff pair quotas

`≥4 pairs`, opening↔ending pair count, etc. explicitly counterchecked and killed as discriminators.

## D-13 — Evidence-ladder quotas / weakest-anchor timing

Explicitly killed.

## D-14 — Every chapter must have a joke / Comedy Pass as mandatory counted gate

PHẦN 12 explicitly downgraded. Humor craft remains optional.

## D-15 — Old PHẦN 8 visual/table output format

Current lifecycle separates script representation from shot/prompt production; side-by-side approval is gone.

## D-16 — Early thumbnail generation inside Writer

Monolith itself later corrects this: thumbnail is later workflow/skill.

## D-17 — “Hedge 1–3 times” / any fixed hedge quota

Explicitly killed; evidence strength and placement matter.

### Rule

`DEAD` material may remain in archived provenance. It must not be copied into target active references “for completeness”.

---

# 7. PENDING / EXPERIMENTAL — KHÔNG PHẢI ACTIVE

## P-01 — The second PHẦN 13 (19–20/08), “seven rulers from 8 night breakouts”

This appended section contains:

- “≥8 independent items”;
- hook/pull count `≥1.4/min`;
- sentence length buckets;
- belief flips;
- mini-story ending rules;
- tight-source observations;
- shared-anchor observations;
- four “weight” ingredients.

Crucially the section itself says:

> “Chưa qua duyệt của chủ để thành LUẬT — xem DECISIONS_REQUIRED D-27.”

`D-27` is still `NEEDS_HUMAN_DECISION`.

### Classification

`PENDING EXPERIMENTAL KNOWLEDGE`, **not ACTIVE Writer contract**.

Some individual observations may later become:

- measured pattern;
- supporting craft;
- Evidence/process correction;
- rejected candidate.

But Phase 3 cannot pre-empt owner decision by copying them into active Writer references.

### Serious runtime implication

Because the compatibility monolith is loaded in Writer runtime today, pending D-27 material is currently **context-visible despite lacking canonical rule status**. Wrapper/governance precedence prevents it from legitimately becoming a hard rule, but visibility can still prime behavior.

This is a strong reason to isolate history/pending R&D from future default context.

## P-02 — RUBRIC Cổng 5 Kịch tính thresholds

Recorded in 03A-C as canonical internal contradiction. Do not classify ACTIVE/DEAD until owner/governance resolves relation to LUẬT 0.

---

# 8. HISTORICAL / PROVENANCE MATERIAL — GIỮ, NHƯNG KHÔNG AUTO-LOAD

## H-01 — PHẦN 13 dated 09/08 cross-channel measurements

Valuable because it records how many earlier rules were killed and why. Best use:

- audit;
- postmortem;
- mechanism/R&D history;
- remeasurement design.

Not normal generation context.

## H-02 — PHẦN 14 winner/loser countercheck

Very valuable architectural evidence for anti-template stance:

- clean structure not sufficient for breakout;
- many counted mechanisms fail to discriminate;
- don’t force mystery;
- “remove chapter, what breaks?” is more useful than quotas.

Its **historical evidence** should be preserved, while structural runtime decisions belong Story Engine.

## H-03 — Failure stories

Examples such as:

- V17 rubric-filling created AI-smell lines;
- V19 false mystery;
- V19/V18 ending similarity;
- bad snippet sourcing;
- translation loops in V20;
- old measuring mistakes.

Useful as regression rationale/test fixtures, not as prose instructions repeated every session.

## H-04 — Competitor verbatim examples

Preserve where legally/project-appropriate as research evidence; do not use them as runtime phrase bank during writing.

---

# 9. FILE-LEVEL CLASSIFICATION

| File | Current classification | Target treatment idea — not yet implementation |
|---|---|---|
| `runtime-monolith-legacy.md` | `MIXED` | preserve immutable-ish historical compatibility snapshot; stop default loading only after replacement is verified |
| `luat-chung-ngach.md` | `MIXED` | extract active/supporting niche prose principles; history/dead material remains provenance/on-demand |
| `quy-trinh-nghien-cuu-cum.md` | `MOVE-LATER` | research-mode only; remove from Writer normal context |
| `viral-teardown.md` | `HISTORICAL / RESEARCH` | on-demand research/provenance; no runtime authority |
| `formula-and-example.md` | `HISTORICAL / CALIBRATION` | on-demand; never copy verbatim into Writer core |
| `teardown-survival-cluster.md` | `RESEARCH CLUSTER / HISTORICAL` | research mode only, conditional by cluster |
| `metadata.md` | `MIXED / MOVE-LATER / UNRESOLVED OWNER` | packaging audit later; do not leave as Writer default dependency |

---

# 10. SALVAGE PRINCIPLE CHO 03B

Do **not** refactor by editing monolith down until it looks clean.

Safer migration pattern:

```text
1. define new Writer contract
2. build minimal active references from canonical ACTIVE behavior
3. leave legacy monolith unchanged as compatibility/history snapshot
4. route normal runtime to new active surfaces
5. smoke/regression compare behavior
6. only then decide whether legacy path can be retired from runtime
7. no deletion without owner
```

This gives rollback and avoids accidentally deleting the rationale needed to understand why a rule died.

---

# 11. DOCUMENTATION DRIFTS FOUND

## F-DRIFT-01 — D-27 points to old Writer path

`DECISIONS_REQUIRED.md` D-27 says seven rulers are written at:

```text
.claude/skills/sketchapiens-viet-kich-ban/SKILL.md PHẦN 13
```

After Phase-1 compatibility wrapper migration, that body lives at:

```text
references/runtime-monolith-legacy.md
```

The decision itself remains valid/pending; the path is stale.

**Disposition:** fix as governance documentation integration task, not inside 03A read-only.

---

# 12. CHECK — 03A-F

- [x] monolith read across old body, 09/08 corrections/countercheck, and appended 19–20/08 section;
- [x] duplicate PHẦN 13 ambiguity identified;
- [x] ACTIVE behaviors separated from their historical rationale;
- [x] SUPPORTING craft separated from quotas/templates;
- [x] MOVE-LATER concerns assigned by mode/owner;
- [x] explicitly DEAD rules catalogued;
- [x] D-27 pending observations blocked from active contract;
- [x] historical measurements preserved conceptually, not discarded;
- [x] file-level classifications defined;
- [x] no deletion/move/runtime edit performed;
- [x] stale D-27 path logged.

**03A-F verdict:** `PASS — salvage map is sufficient to propose a clean Writer contract without losing history or promoting pending experiments`.

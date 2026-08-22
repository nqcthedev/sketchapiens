# 03A-H — AUDIT VERIFICATION & CLOSEOUT — XÁC MINH VÀ KHÓA PHASE 3A

> **Status:** `PHASE 3A CLOSEOUT — NON-RUNTIME`  
> Phase 3A là audit/read-only đối với Writer runtime. File này xác minh điều đó và khóa boundary trước Phase 3B implementation.

**Phase 3A baseline:** `82af6ef73533e63141d5c15a31ee94dc6ba66ccf`  
**Pre-closeout head:** `63427b9a6bda4f9da1c97d736b7e5d6c320afec3`  
**Branch:** `upgrade/story-engine-v21`

---

# 1. CLOSEOUT QUESTION — CÂU HỎI KHÓA PHASE

Phase 3A có thực sự:

1. hiểu Writer hiện tại trước khi sửa;
2. map responsibility/authority/context/consumer/legacy đủ sâu;
3. đề xuất target contract mà không biến proposal thành runtime law;
4. giữ Writer runtime bất biến;
5. giữ mọi pending creative observation ngoài active contract;
6. tạo rollback/checkpoint rõ để Phase 3B triển khai theo task nhỏ?

**Verdict:** `YES — PASS`, với các non-blocking/open integration debts được ghi ở dưới.

---

# 2. TASK STATUS — 03A-A → 03A-H

| Task | Output | Verdict |
|---|---|---|
| `03A-A` Inventory & Runtime Surface | `phase3a-writer-audit.md` | `PASS` |
| `03A-B` Responsibility Decomposition | `03A-B-responsibility-decomposition.md` | `PASS` |
| `03A-C` Authority & Source-of-Truth Audit | `03A-C-authority-source-of-truth.md` | `PASS` |
| `03A-D` Context Load Audit | `03A-D-context-load-audit.md` | `PASS` |
| `03A-E` Consumer & Dependency Audit | `03A-E-consumer-dependency-audit.md` | `PASS` |
| `03A-F` Legacy/Dead Material Classification | two non-runtime audit artifacts, see concurrency note | `PASS` |
| `03A-G` Writer Contract Proposal | `03A-G-writer-contract-proposal.md` | `PASS — proposal only` |
| `03A-H` Audit Verification & Checkpoint | this file | `PASS` |

---

# 3. DETERMINISTIC DIFF VERIFICATION — XÁC MINH DIFF

GitHub compare:

```text
base: 82af6ef73533e63141d5c15a31ee94dc6ba66ccf
head: 63427b9a6bda4f9da1c97d736b7e5d6c320afec3
status: ahead
commits: 16
```

The file diff from the Phase 3A baseline contains **only audit artifacts** under:

```text
.claude/skills/sketchapiens-viet-kich-ban/audit/
```

Changed files before this closeout:

```text
phase3a-writer-audit.md
03A-B-responsibility-decomposition.md
03A-C-authority-source-of-truth.md
03A-D-context-load-audit.md
03A-E-consumer-dependency-audit.md
03A-F-legacy-dead-classification.md
03A-F-legacy-dead-material-classification.md
03A-G-writer-contract-proposal.md
```

### Critical verification

No Phase 3A diff touched:

```text
.claude/skills/sketchapiens-viet-kich-ban/SKILL.md
.claude/skills/sketchapiens-viet-kich-ban/references/**
CLAUDE.md
.claude/rules/**
schemas/**
governance canonical content rules
templates runtime contracts
tools runtime behavior
videos/**
```

Therefore:

> **Writer runtime behavior is unchanged by Phase 3A.**

This satisfies Architecture Contract A-11: refactor architecture and creative behavior remain separate variables.

---

# 4. BRANCH SAFETY — AN TOÀN NHÁNH

Compare with `main` at pre-closeout:

```text
base/merge-base main: 99baf2953aafd612e7efd5c8f5e33f48939a48e2
ahead main: 106 commits
behind main: 0
```

Phase 3A remained on:

```text
upgrade/story-engine-v21
```

No write was made directly to `main` in this audit sequence.

---

# 5. CONCURRENT AUDIT RECONCILIATION — HAI TIẾN TRÌNH CÙNG AUDIT

During 03A-F/G, another valid process on the same feature branch had already created:

```text
03A-F-legacy-dead-classification.md
checkpoint de5c05f18b3c6213f3e80a97da55f2905a56aec5
03A-G-writer-contract-proposal.md
commit 74af0bf53d27ccee537d077439340863ff6b331f
```

A second 03A-F audit was then added as:

```text
03A-F-legacy-dead-material-classification.md
```

Git ancestry confirms the later write was based on the tree that already contained the first 03A-F and 03A-G work. No file was overwritten and no force update was used.

### Why both 03A-F files remain

Project governance says **do not delete without owner command**.

Both files are explicitly `NON-RUNTIME` audit/provenance artifacts. They agree on the important conclusions:

- monolith is mixed historical compatibility, not target runtime;
- there are two `PHẦN 13` headings;
- the later 19–20/08 material includes D-27 pending observations;
- pending material must not become Writer rules;
- dead quotas/templates must not be resurrected;
- active behavior must be extracted by responsibility/authority, not by copying headings.

Disposition:

> **Keep both as provenance for now. Do not load either in normal Writer runtime.**

A future cleanup can consolidate/delete only with owner authorization.

---

# 6. MAJOR FINDINGS LOCKED BY THE AUDIT — PHÁT HIỆN CHÍNH

## F-01 — Thin file, thick runtime

Current Writer `SKILL.md` is a thin compatibility wrapper, but it directly includes the ~84.7 KB legacy monolith. The monolith also instructs reading ~29.7 KB `luat-chung-ngach.md` every write.

**Meaning:** public interface was thinned in Phase 1; runtime context was not truly thinned.

## F-02 — Writer is a historical container, not one clean module

03A-B identified ~14 responsibilities mixed together: routing, workflow, prose, structure, evidence expression, research, competitor calibration, retention craft, packaging, output, policy, history, etc.

## F-03 — Story structure has duplicate/shadow authority inside legacy Writer

Canonical structural authority is Story Engine, but monolith/FLOW/older quality sources still contain structural prescriptions.

Target Writer must consume Story Engine, not preserve a competing internal structural theory.

## F-04 — Context pollution is architectural, not merely token size

Normal Writer context currently risks:

- dead-rule pollution;
- cross-mode pollution;
- competitor voice priming;
- authority-resolution burden;
- structural duplication;
- compaction asymmetry when corrections live late in a long historical body.

## F-05 — Downstream consumers mostly use artifacts, not Writer internals

`/audit-script`, `/apply-review`, editor/QA and production surfaces do not require legacy Writer private references.

This makes internal refactor feasible if public behavior + artifact contracts remain stable.

## F-06 — Duplicate `PHẦN 13` creates ambiguous precedence

Monolith has a 09/08 `PHẦN 13`, then `PHẦN 14`, then another 19–20/08 `PHẦN 13`.

The statement “PHẦN 13–14 beat PHẦN 0–12” is therefore no longer a safe runtime precedence model.

## F-07 — D-27 pending knowledge is context-visible today

The appended night-corpus section explicitly points to `D-27 NEEDS_HUMAN_DECISION`, yet compatibility monolith is runtime-loaded.

Target architecture must firewall pending observations from normal generation context.

## F-08 — Writer target purpose is now clear

Writer should own:

```text
prose realization
write-session orchestration
VI drafting
EN final semantic rewrite
natural expression of already-resolved evidence verdicts
```

Writer should consume/defer:

```text
structure → Story Engine
evidence verdict → Evidence system
sentence craft support → Retention Craft
research/topic → research system
artifact shape/state → schema/rules
packaging → packaging owners
review → audit/editor workflow
history/R&D → on-demand provenance only
```

---

# 7. TARGET CONTRACT STATUS — TRẠNG THÁI ĐỀ XUẤT 03A-G

`03A-G-writer-contract-proposal.md` is deliberately:

```text
PROPOSAL ONLY
NON-RUNTIME
NOT YET CANONICAL
```

It must **not** be added to Source of Truth as canonical Writer owner until implementation + regression pass.

This prevents an architecture document from silently changing creative/runtime behavior before the code/prompt surface actually matches it.

---

# 8. OPEN DEBTS — NỢ MỞ SAU AUDIT

These are real findings, but Phase 3A intentionally did not mutate them.

## O-01 — FLOW structural prescriptions vs Story Engine

`FLOW_VietKichBan_11Cong.md` still contains universal-looking structural instructions such as ending-first / blind-promise / curiosity-loop behavior while Story Engine is canonical structural owner.

**Phase 3B action:** resolve boundary/wording without inventing a new content rule.

## O-02 — Quality source internal conflicts

`RUBRIC_KichBan.md` / `HE_THONG...` still combine current guidance, historical counters and some threshold behavior that is not cleanly reconciled.

Writer refactor should not copy these wholesale into a new “clean” reference.

## O-03 — D-27 remains owner decision

Seven night-corpus rulers remain `PENDING`.

No Phase 3A artifact promotes them.

## O-04 — `/verify-claims` lifecycle wording drift

03A-E found `/verify-claims` still says “before moving to state `evidence_locked`”, while canonical schema treats evidence lock as a gate/milestone, not state enum.

This is a deterministic integration fix, not a Writer creative decision.

## O-05 — Description/tags metadata owner unresolved

Legacy `metadata.md` exists under Writer but Source of Truth does not establish it as canonical owner for description/tags.

Do not move it into target Writer by inertia.

## O-06 — Two 03A-F provenance files

Non-runtime duplication caused by concurrent valid audit work. No production impact. Cleanup requires owner authorization.

---

# 9. PROPOSED NEXT PHASE — 03B IMPLEMENTATION

03A-G proposes this small-task chain:

```text
03B-A — Lock Writer Contract
03B-B — Extract Active Prose Guidance
03B-C — Build Conditional References
03B-D — Thin Runtime Router
03B-E — Detach Legacy Default Runtime
03B-F — Integration & Source-of-Truth Sync
03B-G — Writer Regression Fixtures
03B-H — Runtime Verification & Checkpoint
```

Before/during 03B, fix only integration boundaries necessary for Writer correctness. Do not expand Phase 3 into broad repository cleanup.

---

# 10. PHASE 3A ACCEPTANCE CHECK

- [x] runtime surface inventoried;
- [x] responsibilities decomposed;
- [x] authority/source-of-truth mapped;
- [x] context loading risks mapped;
- [x] consumers/dependencies mapped;
- [x] legacy/dead/pending material classified;
- [x] target Writer contract proposed;
- [x] pending D-27 not promoted;
- [x] no mechanism promoted/demoted;
- [x] no Writer runtime file changed;
- [x] no canonical content rule changed;
- [x] no legacy file deleted/renamed;
- [x] no write to `main`;
- [x] Phase 3B task boundaries defined;
- [x] rollback baseline remains available.

---

# 11. FINAL VERDICT

> ## `PHASE 3A — WRITER READ-ONLY AUDIT: COMPLETE`

The project now knows **what the Writer currently is**, **what it should own**, **what it must stop owning**, **what must remain historical/pending**, and **how to implement the refactor without changing all creative variables at once**.

Phase 3A does **not** claim Writer runtime is fixed.

It establishes the safe contract and evidence needed to start Phase 3B.

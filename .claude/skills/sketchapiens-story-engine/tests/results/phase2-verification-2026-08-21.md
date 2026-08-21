# PHASE 2 VERIFICATION — XÁC MINH STORY ENGINE

**Date — ngày:** 2026-08-21  
**Branch:** `upgrade/story-engine-v21`  
**Verified head before report:** `1f26d4da5cd331a289a93c5e47847b51decc8b15`  
**Task:** `NEXT-02G — Phase 2 Verification / Xác minh toàn Phase 2`

> **Overall verdict — kết luận tổng:** `RELEASE CANDIDATE — NOT YET PHASE-2 COMPLETE`.
>
> Static architecture, ownership, candidate isolation and smoke-harness integrity pass.
> **Semantic Claude Code smoke execution has NOT been run in the target runtime**, so Phase 2 must not be marked complete/stable yet.

---

## 1. GATE SUMMARY — TÓM TẮT CÁC CỔNG

| Gate | Result | Evidence / note |
|---|---|---|
| G1 Architecture graph — đồ thị kiến trúc | **PASS** | `CONTRACT.md`, `SKILL.md`, module references and consumer matrix agree on ownership/dependency direction |
| G2 Source of truth — nguồn chuẩn | **PASS** | `governance/SOURCE_OF_TRUTH.md` assigns Story structure to Story Engine contract; Evidence verdict and Retention Craft are separate scopes |
| G3 Consumer boundaries — ranh giới consumer | **PASS** | Writer routes structure to Story Engine; retention judge uses structural subset; `/audit-script` isolates context by role; `/apply-review` applies only owner-triaged diagnosis |
| G4 Candidate firewall — tường lửa candidate | **PASS (static)** | candidates absent from runtime rule registry; normal writer/reviewer contract forbids Mechanism Lab; postmortem/R&D owns candidate path |
| G5 Progressive disclosure — tải ngữ cảnh theo nhu cầu | **PASS** | thin `SKILL.md` + on-demand references aligns with current Claude Code Skills model |
| G6 Historical fixture integrity | **PASS 5/5** | V17 Death, V17 Rain, V18 Sleep, V19 NightWalk, V20 Cold blob SHAs still match fixtures |
| G7 Deterministic smoke checker | **PASS** | `py_compile` pass; clean partial report passes; injected `Solution Ladder` leakage fails as designed |
| G8 Semantic `STRUCTURE_SMOKE` | **NOT EXECUTED — BLOCKER** | target Claude Code runtime unavailable in verifier environment |
| G9 Semantic `REVIEWER_SMOKE` | **NOT EXECUTED — BLOCKER** | target Claude Code subagent runtime unavailable in verifier environment |
| G10 Project-wide runtime doctor | **NOT EXECUTED HERE** | repository could not be cloned in verifier environment; run locally before merge/phase closure |
| G11 GitHub CI/status | **NO CHECKS CONFIGURED** | commit combined status returned no checks |

---

## 2. ARCHITECTURE VERIFICATION — XÁC MINH KIẾN TRÚC

### PASS — module ownership is singular

Canonical structural owner:

`sketchapiens-story-engine/CONTRACT.md`

Story Engine owns:

- Structural Causality — **Nhân quả cấu trúc**;
- Belief Progression — **Tiến triển niềm tin**;
- Explanatory Progression — **Tiến triển giải thích**;
- Structural Stress Test — **Phép thử chịu lực cấu trúc**;
- evidence placement in story, not factual verdict.

It does not own:

- factual verification;
- Evidence verdict;
- prose / voice;
- topic/title/thumbnail selection;
- sentence-level retention craft;
- analytics causality;
- automatic mechanism promotion.

### PASS — dependency direction has no intended cycle

Target direction remains:

```text
CLAUDE.md / governance
        ↓
Writer
        ↓
Story Engine
        ↓
module-owned references

Viewer Retention Judge
        ↓
Story Engine structural interface

Story Engine ←→ Evidence system
peer boundary through question / verdict
```

No canonical dependency requires:

```text
Story Engine → Writer implementation → Story Engine
```

or:

```text
Story Engine → Retention Craft → Story Engine
```

### PASS — implementation levels are separated

- `SKILL.md` = public runtime entrypoint + context router;
- `CONTRACT.md` = ownership/input-output/dependency contract;
- `structural-mechanisms.md` = canonical structural implementation knowledge;
- `evidence-in-story.md` = structural evidence placement + handoff;
- `workflows.md` = Story Map / review workflow;
- `candidate-lifecycle.md` = candidate governance;
- `mechanism-lab.md` = candidate data store;
- `tests/**` = non-runtime regression surface.

---

## 3. OFFICIAL CLAUDE CODE ASSUMPTIONS — GIẢ ĐỊNH RUNTIME ĐÃ XÁC MINH LẠI

Rechecked against current official Claude Code documentation on 2026-08-21:

- Skills body loads when the skill is used, unlike always-on `CLAUDE.md` content.
- Supporting files are a supported skill pattern; `SKILL.md` should reference what they contain and when to load them.
- Claude Code recommends keeping the skill body concise because loaded content stays in context across turns.
- A custom subagent `skills:` field preloads **the full skill content** into the subagent context at startup, not just the description.
- A subagent can be prevented from invoking other skills by omitting `Skill` from its tools.

Official docs:

- `https://code.claude.com/docs/en/skills`
- `https://code.claude.com/docs/en/sub-agents`

**Implication:** the thin Story Engine entrypoint + on-demand references + reviewer context budget are aligned with the current Claude Code runtime model.

---

## 4. CONSUMER VERIFICATION — XÁC MINH NƠI SỬ DỤNG

### Writer — PASS

`sketchapiens-viet-kich-ban` routes structural work to Story Engine.
Writer keeps final prose ownership.
Legacy writer body remains technical debt for Phase 3, but active wrapper precedence is clear.

### Viewer Retention Judge — PASS

- preloads Story Engine;
- tools are `Read, Grep, Glob`, not `Skill`;
- defaults to preloaded `SKILL.md` + agent prompt;
- does not read research/claim ledger;
- may read structural mechanism reference only on ambiguity;
- does not read candidate files in normal review;
- does not rewrite.

### `/audit-script` — PASS

Each reviewer receives role-specific context:

- retention: title + thumbnail + narration;
- evidence: narration + claim ledger + source;
- anti-AI: narration only.

No shared Story Engine preload is injected into all reviewers.

### `/apply-review` — PASS

- applies only owner-triaged issues;
- does not turn mechanism names into requirements;
- new structural issues are logged rather than silently fixed;
- manifest update uses canonical `status: revision`, `script.versions`, `script.refs.current`.

### Retention Craft legacy module — PASS WITH DEBT

Active wrapper now owns only sentence/paragraph craft.
Old implementation is preserved in `references/runtime-legacy.md` and does not auto-load.
Full cleanup/history separation remains Phase 3/Phase 10 work.

---

## 5. CANDIDATE FIREWALL VERIFICATION — XÁC MINH TƯỜNG LỬA ỨNG VIÊN

Static high-risk surfaces checked:

- `CLAUDE.md`;
- `.claude/rules/**`;
- writer active wrapper;
- viewer-retention-judge active prompt/frontmatter;
- `RULE_REGISTRY.yaml`;
- Story Engine runtime entrypoint;
- `/audit-script`;
- `/apply-review`.

Result:

**PASS — no candidate has runtime authority in normal writing/review.**

Current candidate names remain R&D data only:

- Solution Ladder — **Bậc thang giải pháp**;
- Constraint Migration — **Dịch chuyển điểm nghẽn**;
- Scale-Out Escalation — **Leo thang bằng mở rộng quy mô**;
- Evidence Fit / Causal Proof Fit — **Độ khớp bằng chứng–nhân quả**.

`RULE_REGISTRY.yaml` contains no unpromoted Story Engine candidate.
Postmortem/R&D may mention candidates because those modes are explicitly inside the candidate lifecycle boundary.

---

## 6. SMOKE HARNESS INTEGRITY — TÍNH TOÀN VẸN BỘ CA THỬ

### Historical fixture pinning — PASS 5/5

| Fixture | Source blob | Status |
|---|---|---|
| H-01 V17 Death | `b1efaa5a3f8c149f8ef8adf94f7560fdcc22c227` | MATCH |
| H-02 V17 Rain | `4e3928cdd375cc1729f3cd646e43ed1bbb44ce7d` | MATCH |
| H-03 V18 Sleep | `720b25d16e4196526542b47ebe55e5e6d1dc7b52` | MATCH |
| H-04 V19 NightWalk | `f19bd0e4bd1f6ffde3e8fe1ffc1b7e21957a39d2` | MATCH |
| H-05 V20 Cold | `486a519f284646860bb12eee430274765b39954d` | MATCH |

### Deterministic checker — PASS

Actual verifier-side execution:

1. `python3 -m py_compile check_smoke_report.py` → PASS;
2. valid partial smoke report → checker PASS;
3. partial report whose `OBSERVED DIAGNOSIS` says `Solution Ladder` → checker FAIL with candidate leakage, as intended.

This verifies parser/leak-detection mechanics only.
It does **not** substitute for semantic Story Engine judgment.

---

## 7. BLOCKERS BEFORE PHASE 2 CAN BE MARKED COMPLETE — BLOCKER TRƯỚC KHI ĐÓNG PHASE 2

### B-01 — Full semantic `STRUCTURE_SMOKE`

Run H-01 → H-05 + M-01 → M-10 with the context profile in `tests/RUNBOOK.md`.
Use blind-first execution: model must not see expectation before diagnosis.

Required result for closure:

- no P0/P1 regression;
- no candidate leakage;
- no systematic Causal Debt/template forcing;
- Evidence handoff role remains correct.

### B-02 — `REVIEWER_SMOKE`

Run the reviewer profile using the actual `viewer-retention-judge` subagent.
Verify it:

- detects real topic jump / promise-payoff risk;
- does not rewrite;
- does not open candidate files;
- does not self-issue Evidence verdict;
- does not homogenize V17–V20 into one framework.

### B-03 — Local project doctor before phase closure / merge

Run from a real checkout:

```bash
python3 tools/project_doctor.py
```

No new `FAIL` may be introduced by Phase 2.
WARNs must be classified as pre-existing / accepted / blocker.

---

## 8. NON-BLOCKING DEBT — NỢ KHÔNG CHẶN RUNTIME

### D-01 — Master Upgrade Plan status text is stale

`governance/MASTER_UPGRADE_PLAN.md` still displays older `IN PROGRESS` states/checklists for Phase 1/2.
Git checkpoints and this verification report are newer, but the canonical roadmap should be reconciled before merge to `main`.

This is documentation/status drift, not a Story Engine behavior failure.
Do not create a second competing roadmap just to patch status.

### D-02 — Writer historical monolith still contains old structural knowledge

Active wrapper precedence prevents it from owning current structural decisions.
Full separation is intentionally deferred to Phase 3 — Writer Refactor.

### D-03 — No GitHub CI checks exist for this branch

GitHub combined commit status returned no checks.
Do not create CI in Phase 2 solely to make the dashboard green; deterministic architecture tooling belongs primarily to Phase 7.

---

## 9. CLOSURE RULE — QUY TẮC ĐÓNG PHASE 2

Phase 2 may be marked `COMPLETE / STABLE` only when B-01, B-02 and B-03 are executed and no blocking regression remains.

Until then the correct status is:

```text
PHASE 2: RELEASE CANDIDATE
STATIC VERIFICATION: PASS
SEMANTIC RUNTIME VERIFICATION: PENDING
MERGE TO MAIN: NOT YET
PHASE 3: DO NOT START YET
```

This is deliberate: architecture that looks correct on paper is not enough to authorize the next refactor phase.

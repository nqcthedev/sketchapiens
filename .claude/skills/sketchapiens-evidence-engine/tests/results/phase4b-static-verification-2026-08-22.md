# PHASE 4B STATIC VERIFICATION — XÁC MINH TĨNH EVIDENCE ENGINE

> **Status:** `STATIC PASS — KHÔNG PHẢI RUNTIME PROOF`
>
> Bản này chỉ chứng minh **shape/boundary/consistency** của diff Phase 4B đọc tĩnh.
> Nó **không** chứng minh Evidence Engine hành xử đúng khi chạy. Runtime proof nằm ở
> `runtime-verification-2026-08-22.md`.

**Branch:** `upgrade/story-engine-v21`
**Baseline (Phase 4A reconciled):** `e73f62f9a5e8060f8e9d2dde447e4fa165a3dc3c`
**HEAD tại lúc kiểm:** `38d6a4f`
**Ngày:** 2026-08-22
**Task:** `04B-G` bước 1 — static verification toàn diff Phase 4B

## 1. NET DIFF — PHẠM VI THAY ĐỔI

```text
27 files changed · 3.641 insertions(+) · 284 deletions(-)
43 commit từ baseline

Evidence Engine module     15 file  +2.488
tools/                      2 file    +299 / -64
schemas/ + templates/       3 file    +243 / -39
consumer surfaces           5 file    +260 / -51
governance/                 2 file  (roadmap + SoT)
```

**File thêm mới — 16:**

```text
.claude/skills/sketchapiens-evidence-engine/
├── CONTRACT.md · README.md · SKILL.md
├── references/causal-proof-fit.md · references/ledger-semantics.md
├── scripts/validate_claim_ledger.py
└── tests/
    ├── README.md · RUNBOOK.md · report-template.md
    ├── check_evidence_smoke_report.py · test_ledger_validator.py
    ├── fixtures/historical-evidence-cases.md
    ├── fixtures/micro-evidence-cases.md
    ├── fixtures/ledger-validator-cases.json
    └── results/README.md
templates/claim-ledger.json
```

**File sửa — 11:** `evidence-prosecutor.md` · `apply-review/SKILL.md` · `audit-script/SKILL.md` ·
`new-video/SKILL.md` · `verify-claims/SKILL.md` · `MASTER_UPGRADE_PLAN.md` · `SOURCE_OF_TRUTH.md` ·
`claim-ledger.schema.json` · `claim-ledger.md` · `preflight.py` · `project_doctor.py`

**File xoá — 0.**

## 2. KIỂM TĨNH — S-1 → S-10

### S-1 — Không đụng vùng cấm · PASS

`04B` không được chạm Writer, Story Engine, control plane, visual identity, hay runtime video.
Đếm file thay đổi trong từng vùng, từ baseline tới HEAD:

```text
identity/                                    0 file
CLAUDE.md                                    0 file
videos/                                      0 file
.claude/skills/sketchapiens-viet-kich-ban/   0 file
.claude/skills/sketchapiens-story-engine/    0 file
```

Đúng nguyên tắc `A-11` — tách biến kiến trúc khỏi biến sáng tạo.

### S-2 — Transient marker không hồi sinh · PASS

Bốn file rác sinh ra trong `04B-A` do thao tác connector sai, handoff yêu cầu không được hồi sinh:

```text
.keep                       không tồn tại
04B-A_checkpoint-note.md    không tồn tại
.checkpoint-04B-A           không tồn tại
SHOULD_NOT_EXIST            không tồn tại
```

Final tree sạch.

### S-3 — Fifth-verdict firewall · PASS

Đọc thẳng enum trong `schemas/claim-ledger.schema.json`:

```text
/properties/claims/items/properties/kind
  → ['DIRECT', 'INFERENCE', 'SPECULATION', 'STORY_DEVICE']
```

Đúng bốn. `SYNTHESIS` **không** có mặt ở chiều `kind`.

### S-4 — Schema và template khớp nhau · PASS

```text
schema JSON parse             OK
template JSON parse           OK
required                      video_id · script_ref · locked · lockability
                              sources · claims · bridges
template có đủ required       ĐỦ
bridges là first-class        CÓ — nằm trong required, không phải field phụ
derivation enum               NONE · SOURCE_AUTHOR_INFERENCE · PROJECT_INFERENCE
                              MULTI_SOURCE_SYNTHESIS · RECONSTRUCTION
```

Đây là bằng chứng tĩnh cho quyết định `04A-G`: `SYNTHESIS` nằm ở chiều **derivation**, không nằm
ở chiều **kind**. Hai chiều được tách thật trong schema, không chỉ trong tài liệu.

### S-5 — Validator chạy được trên template thật · PASS

```bash
python3 .claude/skills/sketchapiens-evidence-engine/scripts/validate_claim_ledger.py \
  templates/claim-ledger.json
→ CLAIM LEDGER VALID
```

Template canonical tự nó hợp lệ theo schema canonical — không có vòng lặp chết giữa hai artifact.

### S-6 — Consumer routing trỏ đúng public interface · PASS

Đếm tham chiếu tới `sketchapiens-evidence-engine` / `Evidence Engine`:

```text
.claude/agents/evidence-prosecutor.md      6
.claude/skills/verify-claims/SKILL.md      3
.claude/skills/audit-script/SKILL.md       2
.claude/skills/apply-review/SKILL.md       3
.claude/skills/new-video/SKILL.md          1
```

Cả năm consumer đều đi qua public interface, đúng `A-09` — không deep-link vào private
implementation.

### S-7 — M-004 không bị promote · PASS

`mechanism-lab.md` *(thuộc Story Engine, không bị `04B` sửa)* vẫn ghi:

```text
M-004 — EVIDENCE-FIT / CAUSAL PROOF FIT
Status: `candidate` = ứng viên đang thử
```

Phase 4B hiện thực hoá **behavior** relation-level nhưng **không** nâng M-004 thành rule. Đúng
`DO NOT` trong handoff và đúng `CHANGE_POLICY`.

### S-8 — Preflight giữ nhánh legacy cho V17–V20 · PASS

```text
preflight.py:20   IS_SKA = bool(re.fullmatch(r"SKA-[0-9]{4}-[a-z0-9-]+", name))
preflight.py:74   if IS_SKA:  → 02-research/claim-ledger.json + validate_claim_ledger.py
preflight.py:167  # Legacy compatibility only: citation-shaped count from MONEO-era workflow
preflight.py:170  legacy MONEO: ≥3 citation-shaped anchors
```

Drift mà `04A` phát hiện đã đóng, và đóng **đúng cách roadmap vạch**: `SKA-*` dùng ledger máy,
`Video17–20` giữ nhánh MONEO. Không migrate cưỡng bức legacy.

### S-9 — `SOURCE_OF_TRUTH.md` đã sync · PASS

Dòng 28 ghi Evidence Engine `CONTRACT.md` + runtime `SKILL.md` là nguồn chuẩn cho evidence
semantics, và ghi rõ ranh giới: `evidence-prosecutor` là execution persona, Story chỉ flag
Narrative Overreach, Writer chỉ diễn đạt verdict đã resolved.

Không còn duplicate authority — đúng `A-05`.

### S-10 — Competitor / R&D không vào Evidence runtime · PASS

Quét thô ban đầu báo một cờ ở `SKILL.md`. Đọc ngữ cảnh thì đó là **câu cấm**, không phải nạp:

```text
SKILL.md:93   Không default-load:
SKILL.md:95   - `2_KHO_BANGHI/**`;
SKILL.md:96   - competitor teardown;
SKILL.md:97   - Writer voice theory;
```

Ghi lại nguyên trạng để lần sau không ai đọc kết quả grep thô rồi kết luận ngược. Không file
runtime nào của Evidence Engine **nạp** competitor corpus hay Egypt R&D.

## 3. TỔNG KẾT STATIC

```text
S-1  không đụng vùng cấm ................ PASS
S-2  transient marker không hồi sinh .... PASS
S-3  fifth-verdict firewall ............. PASS
S-4  schema và template khớp ............ PASS
S-5  validator chạy trên template thật .. PASS
S-6  consumer routing qua public API .... PASS
S-7  M-004 không promote ................ PASS
S-8  preflight giữ nhánh legacy ......... PASS
S-9  SOURCE_OF_TRUTH sync ............... PASS
S-10 competitor / R&D không vào runtime . PASS

STATIC VERIFICATION: PASS 10/10
```

## 4. ⛔ STATIC PASS KHÔNG PHẢI RUNTIME PROOF

Handoff ghi rõ: *"Không gọi static PASS là runtime proof"*. Mười phép kiểm trên chỉ đọc file và
đếm — chúng **không** trả lời được:

- Evidence có thật sự phán `UNSUPPORTED` cho một edge khi hai node đều đúng không;
- có bác oan một tổng hợp đa nguồn hợp lệ không;
- có tự phát `SYNTHESIS` khi bị hỏi thẳng không;
- có giữ lock traceability qua đổi version không.

Bốn câu đó chỉ runtime trả lời được. Chúng nằm ở `runtime-verification-2026-08-22.md`, đã chạy
blind-first 17/17 trên checkpoint `d2762ff`.

## 5. GHI CHÚ VỀ CHECKPOINT

Runtime smoke chạy tại `d2762ff0a106413c3eca7aa3d84ce8d72e00700a`. Static verification này chạy
tại `38d6a4f`, tức **sau** hai commit roadmap `8bec1e2` và `38d6a4f`.

Hai commit đó **chỉ chạm `governance/MASTER_UPGRADE_PLAN.md`** — không chạm runtime, schema,
template, tool hay module nào. Nên kết quả runtime tại `d2762ff` vẫn có hiệu lực tại `38d6a4f`.
Xác minh:

```bash
git diff --name-only d2762ff..38d6a4f
→ governance/MASTER_UPGRADE_PLAN.md
```

# PROJECT FULL AUDIT EXPORT

*Read-only audit. Generated 2026-08-06. No file was modified, renamed, moved or deleted. This report is the only file created.*

> ## ⚠️ ĐƯỜNG DẪN TRONG FILE NÀY ĐÃ CŨ *(ghi chú 07/08/2026)*
>
> Đây là **ảnh chụp hiện trạng ngày 06/08**, không phải bản đồ hiện tại. Ngày 07/08 kho được dọn:
>
> | | |
> |---|---|
> | 65 file `.md` ở gốc kho | chuyển vào `kho/1_luat` · `kho/2_nguyenlieu` · `kho/3_bangchung` · `kho/4_luutru` |
> | `Video02`–`Video16` | xoá *(lane "về BẠN" đã chết — chủ quyết)* |
> | 5 file `.md` đã dán biển ⛔ | xoá |
> | chính file này | chuyển vào `governance/` |
>
> **Cố ý KHÔNG sửa 343 đường dẫn bên trong.** Sửa thì bản chụp sẽ nói dối rằng file vốn nằm ở
> `kho/` từ đầu, và mất luôn giá trị làm bằng chứng về hiện trạng lúc kiểm kê.
> Bản đồ hiện hành: `00_LUAT_HIEN_HANH.md` và mục 0 của `CLAUDE.md`.

**Root audited:** `/Users/admin/Claude/Projects/Build Channel Người Que Cổ Đại/`

**Reading-depth legend used throughout:**
- **[READ-FULL]** — file opened and read end to end
- **[READ-PART]** — substantial sections read (headings + quoted passages)
- **[HEADINGS]** — structure extracted (first line + all `#`/`##`/`###`), body not read
- **[LISTED]** — existence, size, date, path only

---

## 1. Executive Summary

| Field | Value | Evidence |
|---|---|---|
| **Project name** | Sketchapiens (also written "Người Que Cổ Đại" / "Try Hard Project Người Que") | `Brand_Kit_Kenh.md`, `BÀN_GIAO_DuAn.md` [HEADINGS] |
| **Channel goal** | Faceless YouTube channel, monetisation via YPP; currently pre-monetisation | `CHINHSACH_YOUTUBE_2026_AnhHuong.md` §3 [HEADINGS]; `00_LUAT_HIEN_HANH.md` [READ-PART] |
| **Content niche** | "Ancient Humans Explained" — everyday human behaviour traced to prehistory | `viet-kich-ban-nguoi-que-co-dai/SKILL.md` PHẦN 0 [READ-FULL via skill load] |
| **Target audience** | US / EU English speakers | `checklist-dang-video-long-form` §3 [READ-FULL via skill load]; nexlev `countryTop` measurements |
| **Language** | Video output **English**; all internal documentation **Vietnamese** | every root `.md` is Vietnamese; all `Script_*_narration.txt` are English |
| **Video style** | Stickman / doodle 2D animation, faceless, AI TTS narration, documentary-with-dry-comedy tone | `ArtBible_NguoiQueCoDai.md` [HEADINGS], `chia-shot-va-prompt-anh/SKILL.md` [READ-FULL via skill load] |
| **Main AI tools** | Claude Code (writing/analysis), ChatGPT (external script review), ElevenLabs (TTS), Google Flow / Nano Banana (images), NotebookLM (competitor digest), nexlev MCP (channel analytics), yt-dlp (transcript pull) | `automation-pipeline/pipeline.py` [LISTED], `LENH_GPT_ReviewKichBan_v3.md` [READ-FULL], `2_KHO_BANGHI/_tool/` [READ-FULL] |
| **Current state** | 19 video directories; V19 script complete at gate 10 of 11; a 768-transcript competitor corpus built 2026-08-06 | `Video19_NightWalk/CHOT_V19.md` [READ-PART]; `2_KHO_BANGHI/00_KHO.md` [READ-FULL] |
| **Long-term goal** | Reach YPP (1,000 subs + 4,000 watch-hours), then sustain on RPM | `chan-doan-kenh-youtube/SKILL.md` §4 [READ-FULL via skill load] |

**Biggest current problem (fact, multi-source):** the project has **no version control and no single source of truth enforced by the filesystem**. `00_LUAT_HIEN_HANH.md` states verbatim: *"Kho có ~80 file, nhiều file mâu thuẫn nhau mà không file nào biết mình đã bị bác"* ("~80 files, many contradict each other and no file knows it has been overruled"). The same file records that `/Users/admin` is a git repo with **0 commits / 0 tracked files**, so deletion is irreversible. Verified independently: `git` reports the project root is **not** a tracked repository.

**Second-biggest problem (fact):** knowledge is stored as **second-hand notes rather than source data**, and several recorded numbers were measurably wrong. Four were corrected on 2026-08-06 when raw transcripts were first pulled — recorded in `2_KHO_BANGHI/00_KHO.md` [READ-FULL]:

| Recorded in project | Measured from source |
|---|---|
| Ink Explainer 769K video "~1,000 words" | 1,198 words |
| Before Civilization "floor 7,000 / median 18,500" | median 6,001 / floor 1,266 |
| Simply A Stickman "median 510" | 295 |
| "niche ceiling 7.83M" | Barely Evolved has a 9.53M video |

**Biggest current strength (fact):** the project keeps an explicit **falsification log**. `00_LUAT_HIEN_HANH.md` contains a "SỔ KHAI TỬ" (death register) naming 8 retired rule-files with the reason each was overruled, plus a "NHẬT KÝ SOI KHO" (audit diary). `HE_THONG_KichBan_v2_14Video.md` PHẦN A is titled *"BỐN LUẬT v1 ĐÃ BỊ BÁC"* ("four v1 rules that were refuted"). This is unusually disciplined for a solo content project and is the main reason the audit could distinguish live rules from dead ones.

> ⚠️ **Not inferred:** the report does not claim which videos are published. No file in the project records publication status or YouTube URLs for the 19 video directories. See §21.

---

## 2. Complete Directory Tree

**Scale:** 35,897 files · 4,517 directories · 4.8 GB total.
**Real knowledge/config files** (excluding `node_modules`, Rust `target/`, `dist/`, `__pycache__`, `.git`, downloaded `_vtt/`): **979** — 764 `.txt`, 162 `.md`, 32 `.py`, 16 `.json`, 3 `.sh`.

```text
Build Channel Người Que Cổ Đại/          ← project root, NOT a git repo
│
├── [79 loose .md/.txt files at root]     ← see §3; no subfolder organisation
│
├── 2_KHO_BANGHI/                         2,533 files · 530 MB  ← created 2026-08-06
│   ├── 00_KHO.md                         master index of the corpus
│   ├── _tool/
│   │   ├── keo_kenh.sh                   channel puller
│   │   ├── vtt2text.py                   VTT → clean text
│   │   ├── convert.py                    batch converter
│   │   ├── do_kenh.sh                    niche scanner (18 queries)
│   │   ├── keo.log                       [LARGE, pull log]
│   │   ├── _quet_kenh.tsv                360 scan rows
│   │   └── _kenh_moi.txt                 23 newly discovered channels
│   ├── ADayInHistory/     134 .txt + _vtt/   ⚠ documentary format
│   ├── PaintExplainer/    139 .txt + _vtt/   ⚠ documentary format
│   ├── BrightPsycho/       96 .txt + _vtt/
│   ├── BeforeCivilization/ 65 .txt + _vtt/
│   ├── Mack/               52 .txt + _vtt/
│   ├── SimplyAStickman/    47 .txt + _vtt/
│   ├── Stickly/            43 .txt + _vtt/
│   ├── Mogo/               31 .txt + _vtt/
│   ├── Zenn/               28 .txt + _vtt/
│   ├── BeforeFire/         27 .txt + _vtt/   ⚠ documentary format
│   ├── Myrk/               17 .txt + _vtt/
│   ├── PrimalGlitch/       13 .txt + _vtt/
│   ├── Rune/               13 .txt + _vtt/
│   ├── InkExplainer/       12 .txt + _vtt/
│   ├── Axen/               12 .txt + _vtt/
│   ├── CertifiedThought/   11 .txt + _vtt/
│   ├── MrHell/             10 .txt + _vtt/
│   ├── SuperJoy/            9 .txt + _vtt/
│   ├── PaintItSimple/       7 .txt + _vtt/
│   └── BarelyEvolved/       2 .txt + _vtt/   ⚠ INCOMPLETE (HTTP 429)
│
├── Video02_What_Animal_Hunted_Us/    385 files · 103 MB · 372 images
├── Video03_Afraid_of_the_Dark/       353 files · 167 MB · 342 img · 1 mp3 · 1 mp4
├── Video04_What_Did_Ancient_Humans_Do_All_Day/  3 files · 1.1 MB · ⚠ NO assets
├── Video05_Baby_Memory/                4 files · ⚠ NO assets
├── Video06_Hypnic_Jerk/              319 files · 155 img · 155 mp3 · 1 mp4
├── Video07_Goosebumps/               227 files · 109 img · 109 mp3 · 1 mp4
├── Video08_Hiccup/                   315 files · 153 img · 153 mp3 · 1 mp4
├── Video09_Teeth/                    290 files · 140 img · 140 mp3 · 1 mp4
├── Video10_Eyesight/                 236 files · 113 img · 113 mp3 · 1 mp4
├── Video11_Back_Pain/                396 files · 193 img · 193 mp3 · 1 mp4
├── Video12_Feet/                     533 files · 265 img · 255 mp3 · 1 mp4  ⚠ img≠mp3
├── Video13_Stress/                   514 files · 253 img · 253 mp3 · 1 mp4
├── Video14_Milk/                   1,001 files · 608 img · 302 mp3 · 30 mp4 ⚠ img≠mp3
├── Video15_Allergies/              1,150 files · 568 img · 564 mp3 · 3 mp4  ⚠ img≠mp3
├── Video16_Winter/                   201 files · 0 img · 185 mp3 · 2 mp4    ⚠ NO images
├── Video17_Death/                      2 files  ⚠ NUMBER COLLISION with Video17_Rain
├── Video17_Rain/                     305 files · 1 img · 263 mp3 · 3 mp4    ⚠ NO images
├── Video18_Sleep/                    477 files · 229 img · 224 mp3 · 1 mp4
├── Video19_NightWalk/                 24 files · 228 KB · text only (in progress)
│   └── _nhap/                        11 draft/version files
│
├── _KHO_LUU_DaChet/                   20 files · 588 KB  ← retired-file archive
├── GhepVideo_Desktop/             26,368 files · 2.4 GB   ← Tauri app + node_modules + Rust target
├── GhepVideo_Studio/                  20 files · Vite/TS app
├── GhepVideo_Studio_NextJS/           20 files · Next.js app
├── GhepVideo_Pipeline/                 7 files · Python TTS/assemble scripts
├── SketchapiensImageTool/              2 files · App.tsx + README
├── automation-pipeline/                8 files · pipeline.py, config.yaml, .env.example
├── skills_build/                       2 files · chong-van-ai-narration-en/SKILL.md
├── NGHIENCUU_Thumbnail_50K/           32 files · 31 competitor thumbnails + list.tsv
├── competitor_frames_predators/       57 files · f_00025.jpg … extracted video frames
└── REF_Style/                          3 files · 3 style reference PNGs
```

**Directories flagged:**
- **Empty of assets:** `Video04_...` (3 text files only), `Video05_Baby_Memory` (4 files only)
- **Number collision:** `Video17_Death/` and `Video17_Rain/` both claim index 17
- **Missing image sets:** `Video16_Winter` (0 images, 185 mp3), `Video17_Rain` (1 image, 263 mp3) — assets likely moved or never retained
- **Asset-count mismatches** (image count ≠ mp3 count, which the pipeline expects to be equal): V12 265/255, V14 608/302, V15 568/564
- **No `Video01_` directory** — its 11 production files sit loose at project root

**Files over 100 KB (context-dilution risk if ever read into an LLM):**

| Size | Path |
|---|---|
| 1,442 KB | `Video15_Allergies/PROMPTS_FULL.txt` |
| 1,203 KB | `Video02_What_Animal_Hunted_Us/PROMPTS_FULL.txt` |
| 1,116 KB | `Video03_Afraid_of_the_Dark/PROMPTS_FULL.txt` |
| 1,094 KB | `Video04_.../PROMPTS_FULL.txt` |
| 680 KB | `Video14_Milk/PROMPTS_FULL.txt` |
| 663 KB | `Video05_Baby_Memory/PROMPTS_FULL.txt` |
| 605 KB | `Video13_Stress/PROMPTS_FULL.txt` |
| 555 KB | `Video16_Winter/PROMPTS_FULL.txt` |
| 545 KB | `IMG_PROMPTS_UPLOAD.txt` *(root)* |
| 530 KB | `Video17_Rain/PROMPTS_FULL.txt` |
| 503 KB | `Video18_Sleep/PROMPTS_FULL.txt` |
| 432 KB | `Video15_Allergies/build/V15_alignment.json` |
| 355 KB | `Video03_.../why-are-humans-still-afraid-of-the-dark-timestamps.json` |
| 326 KB | `Video12_Feet/PROMPTS_FULL.txt` + 325 KB `PROMPTS_CLEAN.txt` *(near-duplicate pair)* |
| 310/299/267/214/214/191/187 KB | `PROMPTS_FULL.txt` for V06, V08, V09, V07, V10, V11 (+ V11 `PROMPTS_CLEAN.txt` 186 KB) |
| 157 KB | `IMG_PROMPTS_REF_SHORT.txt` *(root)* |
| 68 KB | `Script_Video01_PROMPTS.txt` *(root)* |
| 47 KB | `Script_Video01_SHOTLIST.txt` *(root)* |
| 46 KB | `MAU_Script_Do-Animals-Mourn-Their-Dead.md` |
| 37 KB | `MAU_Script_Why-Did-Ancient-Humans-Wear-Clothes.md` |

**Same-name files appearing in many directories** (per-video generated, not duplicates of each other): `PROMPTS_FULL.txt` (14×), `SHOTLINES_FULL.txt` (13×), `run_pipeline.py` (6×), `gen_prompts.py` (6×), `shot_data.py` (4×), `build_prompts.py` (4×), `build/tts_stdlib.py` (5×), `build/2_assemble_video.py` (5×), `build/TTS_input_per_shot.txt` (5×), `THUMBNAIL_prompts*.txt` (4 videos, up to 3 versions each).

---

## 3. File Inventory Table

### 3.1 Root-level knowledge files (79)

Status assigned from **content**, not date. Where content gives no signal, `UNKNOWN`.

| Path | Type | Purpose | Status | Importance | Modified | Duplicate/Overlap | Notes |
|---|---|---|---|---|---|---|---|
| `00_LUAT_HIEN_HANH.md` | md | Entry point; 4-tier doc map, precedence rules, death register, mode table, permission table | CANONICAL | CRITICAL | 2026-08-06 | Tier map overlaps `WORKFLOW_Production.md` | 391 lines, 26 KB. Self-describes as "read before everything". [READ-PART 1–275] |
| `FLOW_VietKichBan_11Cong.md` | md | 11-gate script process, each gate tied to a real past error | CANONICAL | CRITICAL | 2026-08-06 | Overlaps `WORKFLOW_Production.md` stage 2 | Created 2026-08-06 [READ-FULL, authored in-session] |
| `WORKFLOW_Production.md` | md | Full production workflow, stages 0–4, gates 0–4 | CANONICAL | CRITICAL | 2026-08-06 | Stage 2 overlaps `FLOW_VietKichBan_11Cong.md` | 299 lines. Contains two dated in-file revisions (04/08, 05/08). [HEADINGS] |
| `RUBRIC_KichBan.md` | md | Script scoring rubric, 72 pts, two tiers, LUẬT 0 | ACTIVE | HIGH | 2026-08-06 | Tier A overlaps `HE_THONG_KichBan_v2` | `00_LUAT` marks it "⚠️ xem ghi chú" — partially superseded. Carries in-file warning that Tier A was distilled from an unverifiable channel. [READ-PART] |
| `HE_THONG_KichBan_v2_14Video.md` | md | Script system from 14 competitor scripts; title formula (PHẦN C); hook structure | CANONICAL | CRITICAL | 2026-07-29 | PHẦN C overlaps `BANDO_NgachTitle_Thang` (dead) | 397 lines. PHẦN A explicitly refutes four v1 rules. [HEADINGS] |
| `PROMPT_TONG_Thumbnail_v6.md` | md | Thumbnail law: 5 fatal errors, 5 hard rules, 7 layouts, fill-in prompt | CANONICAL | CRITICAL | 2026-08-05 | Supersedes 3 dead thumbnail files | 262 lines [HEADINGS] |
| `TEMPLATE_Thumbnail_KHOA_v1.md` | md | Locked thumbnail prompt, 3 fill slots, 3 gates | CANONICAL | HIGH | 2026-08-05 | Filename says v1, H1 says **v2** — mismatch | 249 lines. Contains "⛔ BA CHỮ CẤM": `cartoon`/`clean`/`smooth`. [HEADINGS] |
| `CONGTHUC_InkExplainer_BestOf.md` | md | 5-step "best-of" formula; reused-content boundary table | ACTIVE | HIGH | 2026-08-06 | — | Contains a self-correction block "CHỖ NÀY TỪNG GHI SAI — SỬA 06/08". [READ-FULL] |
| `LENH_GPT_ReviewKichBan_v3.md` | md | External-reviewer prompt library; per-round table; rounds 4/5/6 prompts | CANONICAL | HIGH | 2026-08-06 | Supersedes `_BO_TRAIN_ChatGPT_ReviewKichBan_v2.md`, `Video17_Rain/_nhap/LENH_GPT_ReviewKichBan.md`, `Video18_Sleep/LENH_GPT_ReviewKichBan_V18.md` | H1 still reads "v2" while filename is v3 — mismatch. 383 lines. [READ-FULL] |
| `LENH_GPT_BoiCanh_TayNghe.md` | md | Craft-only context block to paste before review prompt | ACTIVE | MEDIUM | 2026-08-06 | Extract of `TRAIN_ChatGPT_TOANBO_DuAn.md` | Created 2026-08-06. Reverses the "no context" rule in `LENH_GPT_ReviewKichBan_v3.md` header — **both statements still present in the repo**. [READ-FULL] |
| `QUY_TRINH_2_CONG.md` | md | Two-gate discipline (entry check + exit measurement) | CANONICAL | HIGH | 2026-07-29 | Referenced by `00_LUAT` | 89 lines [HEADINGS] |
| `CHINHSACH_YOUTUBE_2026_AnhHuong.md` | md | YouTube 2026 policy impact; inauthentic-content test; YPP tiers | CANONICAL | HIGH | 2026-07-31 | Policy quotes repeated in `00_LUAT` §"LUẬT MỚI 05/08" | 120 lines [HEADINGS] |
| `ArtBible_NguoiQueCoDai.md` | md | Visual style bible v2, 13 sections | ACTIVE | HIGH | 2026-06-25 | Conflicts with `gotcha_style_doodle_khong_hoathinh` memory + `TEMPLATE_Thumbnail_KHOA_v1` banned words | Dated 2026-06-25, predates the "3 banned words" rule. [HEADINGS] |
| `CastBible_DienVien.md` | md | Cast system: one body, costume presets, token registry | ACTIVE | HIGH | 2026-06-25 | Overlaps `BasePack01_Sketchapiens.md`, `Prompts_NhanVat_Kenh.md`, `SOP_NhatQuan_NhanVat.md` | Uses `@TOKEN` scheme; the shot-splitting skill says tokens are **not** used. Contradiction — see §17. [HEADINGS] |
| `BasePack01_Sketchapiens.md` | md | 12 character/prop sheets to generate | ACTIVE | MEDIUM | 2026-06-25 | Overlaps `CastBible_DienVien.md` | Names `@MODERNYOU`, `@ANCESTOR`, `@FORAGER`, `@CHILD`, `@ELDER`, `@SCIENTIST`, `@CHIMP` [HEADINGS] |
| `Prompts_NhanVat_Kenh.md` | md | Character prompt set v3 | ACTIVE | MEDIUM | 2026-06-25 | Overlaps above two | [HEADINGS] |
| `SOP_NhatQuan_NhanVat.md` | md | Character-consistency SOP for Nano Banana / Flow | ACTIVE | MEDIUM | 2026-06-24 | Overlaps above three | Labelled "Part 2" [HEADINGS] |
| `Brand_Kit_Kenh.md` | md | Channel name options, About text, logo/banner prompts | ARCHIVE | LOW | 2026-06-24 | — | `00_LUAT` files it under Tier 4 [HEADINGS] |
| `BÀN_GIAO_DuAn.md` | md | Project handover doc | ARCHIVE | LOW | 2026-07-02 | — | Tier 4 per `00_LUAT` [LISTED] |
| `VAULT_AncientHumans_KnowledgeVault.md` | md | Knowledge vault index | ACTIVE | MEDIUM | 2026-08-06 | — | **873 bytes / 15 lines only** — far smaller than its Tier-2 role implies. Possible stub or truncation. [LISTED] |
| `VAULT_NotebookLM_BanGoc_DoiChieu.md` | md | Maps 4 NotebookLM originals → where digested; 6 places local beat original | ACTIVE | MEDIUM | 2026-08-06 | — | 49 lines [HEADINGS] |
| `KHO_GiongCamXuc_DoiThu.md` | md | Voice bank: 7 pattern groups, 2 schools, pre-load | CANONICAL | HIGH | 2026-07-11 | Extracted into `LENH_GPT_BoiCanh_TayNghe.md` | 45 lines [READ-FULL] |
| `NganHang_ReHook_BucketBrigade.md` | md | Connector bank; PART A generic, PART B competitor-original (marked do-not-copy) | CANONICAL | HIGH | 2026-07-07 | Techniques extracted into `LENH_GPT_BoiCanh_TayNghe.md` | 79 lines [READ-PART] |
| `KHO_AnDu_TruyenChem_LachLuat.md` | md | 16 modern metaphors, interjected stories, 4 censorship-evasion rules | ACTIVE | MEDIUM | 2026-07-29 | — | 152 lines [LISTED] |
| `DICH_Zenn_7.8M_WhatDidAncientHumansDoAtNight.md` | md | Vietnamese translation of the niche's biggest video | ACTIVE | HIGH | 2026-07-27 | Now redundant with `2_KHO_BANGHI/Zenn/` raw transcript | `00_LUAT` marks it mandatory reading for gate A. 190 lines [LISTED] |
| `MoXe_15Khoi_KichBan_DoiThu.md` | md | 15 storytelling blocks dissected | ACTIVE | MEDIUM | 2026-06-24 | Overlaps `MoXe_KichBan_Viral_3Video.md`, `TearDown_*` | [LISTED] |
| `MoXe_KichBan_Viral_3Video.md` | md | 3 viral scripts dissected | ACTIVE | MEDIUM | 2026-06-24 | Overlaps above | [LISTED] |
| `TearDown_7M_CongThuc_GuongSoi.md` | md | 7.7M teardown + "modern mirror" formula | ACTIVE | MEDIUM | 2026-07-08 | Overlaps above | [LISTED] |
| `TearDown_Video_Predators.md` | md | Predators video teardown | ACTIVE | MEDIUM | 2026-06-24 | Overlaps above | [LISTED] |
| `TEARDOWN_PLAYBOOK_RaLenh_AI.md` | md | 3-step prompt pack for AI teardown of competitor scripts | ACTIVE | MEDIUM | 2026-07-07 | — | 172 lines [LISTED] |
| `MAU_Script_Do-Animals-Mourn-Their-Dead.md` | md | Sample full script | EXAMPLE | LOW | 2026-06-23 | — | 46 KB, largest single .md [LISTED] |
| `MAU_Script_Why-Did-Ancient-Humans-Wear-Clothes.md` | md | Sample full script | EXAMPLE | LOW | 2026-06-23 | — | 37 KB [LISTED] |
| `BANG_CAU_TatCa_CuNo_2026-07-29.md` | md | Demand table — all breakout videos in niche | CANONICAL | HIGH | 2026-07-29 | Replaces 3 dead topic files | `00_LUAT` names it the topic-selection law [LISTED] |
| `BANDO_CumChuDe_CoCau_2026-07-27.md` | md | 7 topic clusters ranked by proven breakouts | ACTIVE | MEDIUM | 2026-07-27 | — | Tier 3 [LISTED] |
| `BANDO_NgachTitle_Thang.md` | md | Title lane map | **DEPRECATED** | LOW | 2026-08-06 | Superseded by `HE_THONG_KichBan_v2` PHẦN C | ⛔ banner in file; listed in death register; **still sits at root beside live files** [LISTED] |
| `NGHIENCUU_Title_3Kenh_Gap_2026-07-11.md` | md | Title research, 3 pillar channels | **DEPRECATED** | LOW | 2026-08-06 | Same as above | ⛔ banner; still at root [LISTED] |
| `TRAIN_ChatGPT_TOANBO_DuAn.md` | md | Whole-project brain dump for ChatGPT, 14 parts | **DEPRECATED (partial)** | MEDIUM | 2026-08-06 | Parts 6 & 8 extracted into `LENH_GPT_BoiCanh_TayNghe.md` | ⛔ banner. `LENH_GPT_ReviewKichBan_v3.md` forbids its use; but its craft sections were revived 2026-08-06. Mixed status. 324 lines [READ-PART] |
| `_BO_TRAIN_ChatGPT_ReviewKichBan_v2.md` | md | Superseded review-training doc | **DEPRECATED** | LOW | 2026-08-06 | Superseded by `LENH_GPT_ReviewKichBan_v3.md` | `_BO_` prefix = discarded; still at root [LISTED] |
| `TRAIN_ChatGPT_BuocPolish.md` | md | Polish-step training for ChatGPT | ARCHIVE | LOW | 2026-07-24 | Overlaps `chong-van-ai-narration-en` skill | Tier 4 [LISTED] |
| `TRAIN_ChatGPT_Thumbnail.md` | md | Thumbnail-specialist ChatGPT training | ARCHIVE | LOW | 2026-07-25 | Overlaps `PROMPT_TONG_Thumbnail_v6.md` | Tier 4; predates v6 [LISTED] |
| `PROMPT_PACK_NotebookLM.md` | md | NotebookLM prompt pack + tracking log | ARCHIVE | MEDIUM | 2026-07-29 | Overlaps `PLAYBOOK_NotebookLM_DoiThu.md`, `LENH_NotebookLM_ChuaLam.md` | 396 lines [LISTED] |
| `PLAYBOOK_NotebookLM_DoiThu.md` | md | NotebookLM playbook | ARCHIVE | LOW | 2026-07-29 | Overlaps above | **First byte is a stray `s`** before `# PLAYBOOK` — file corruption or typo [LISTED] |
| `LENH_NotebookLM_ChuaLam.md` | md | NotebookLM tasks not yet done | ACTIVE | MEDIUM | 2026-07-29 | Overlaps above two | `00_LUAT` marks it as the live NotebookLM file [LISTED] |
| `BAY_SinhDoi_DanhSach.md` | md | Twin-swarm list for NotebookLM | ARCHIVE | LOW | 2026-07-29 | Pairs with `NGHIENCUU_ThiNghiem_BaySinhDoi.md` | [LISTED] |
| `NGHIENCUU_ThiNghiem_BaySinhDoi.md` | md | Controlled twin-swarm experiment | ACTIVE | HIGH | 2026-07-29 | — | `00_LUAT` names it the law for "what actually decides win/lose" [LISTED] |
| `NGHIENCUU_CloneSwarm_2026-07-29.md` | md | Why good topics still die (clone swarm) | CANONICAL | HIGH | 2026-07-29 | — | 219 lines; named as law in `00_LUAT` [LISTED] |
| `CO_CHE_3LOP_Winner_2026-07-29.md` | md | 3-layer winner mechanism (title+thumb+hook) | ACTIVE | MEDIUM | 2026-07-29 | — | [LISTED] |
| `BOCTACH_16Kenh_2026-08-05.md` | md | 16-channel teardown | CANONICAL | HIGH | 2026-08-05 | **Supersedes** `BOCTACH_4Kenh_SoSanh_2026-08-04.md` per `00_LUAT` | 198 lines [LISTED] |
| `BOCTACH_4Kenh_SoSanh_2026-08-04.md` | md | 4-channel comparison, top-2 share test | **DEPRECATED** | MEDIUM | 2026-08-04 | Superseded by 16-channel version | `00_LUAT` marks ⛔ but **file has no ⛔ banner** — half-retired. Contains the "median 18,500" figure now measured at 6,001. [READ-PART] |
| `BOCTACH_BeforeCivilization_2026-08-04.md` | md | Single-channel teardown | ACTIVE | MEDIUM | 2026-08-04 | Overlaps above | [LISTED] |
| `NGHIENCUU_2Kenh_ThinkMan_BrightPsycho_2026-07-25.md` | md | 2-channel research | ACTIVE | MEDIUM | 2026-07-25 | Naming conflict: its "ThinkMan" = channel `UCdRKykJ9kiBGJ9FCVFZ41Mg` = **CertifiedThought** in the new corpus | Same channel counted under two names across the repo [READ-PART] |
| `NGHIENCUU_V16_LaneCheck_2026-07-26.md` | md | V16 lane re-check | ACTIVE | LOW | 2026-07-29 | — | `00_LUAT` lists it as an open decision from 27/07, unresolved [LISTED] |
| `NGHIENCUU_V18_ChonDeTai_2026-07-31.md` | md | V18 topic research, live numbers | ACTIVE | MEDIUM | 2026-08-01 | — | 495 lines — largest research file [LISTED] |
| `NGHIENCUU_DoiSong_CoDai_2026-07-13.md` | md | Daily-life lane research | ACTIVE | LOW | 2026-07-13 | — | [LISTED] |
| `NGHIENCUU_NguPhapHinh_InkExplainer.md` | md | Visual grammar, 96 frames, 2 channels | ACTIVE | MEDIUM | 2026-07-30 | Overlaps `NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md` | Same topic, same date, two files [LISTED] |
| `NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md` | md | Visual grammar remeasured on 2 full videos | ACTIVE | MEDIUM | 2026-07-30 | Overlaps above | Title says "remeasured" → likely supersedes, but neither file says so [LISTED] |
| `NGHIENCUU_15Thumbnail_Mack.md` | md | 15 Mack thumbnails examined | ACTIVE | MEDIUM | 2026-07-29 | Feeds `PROMPT_TONG_Thumbnail_v6.md` | [LISTED] |
| `CONCEPT_Thumbnail_V16_V17.md` | md | Thumbnail concepts V16/V17 | ARCHIVE | LOW | 2026-07-29 | — | Tier 4 [LISTED] |
| `V17_PACKAGING_CHOT.md` | md | V17 locked packaging | ARCHIVE | MEDIUM | 2026-07-30 | — | 453 lines; `00_LUAT` still lists it as an open item awaiting thumbnail [LISTED] |
| `V17_PROMPT_THUMBNAIL.md` | md | V17 thumbnail prompt | ARCHIVE | LOW | 2026-07-29 | — | [LISTED] |
| `V18_PACKAGING.md` | md | V18 packaging | ARCHIVE | MEDIUM | 2026-08-03 | Overlaps `Video18_Sleep/DANG_V18.md` | 267 lines [LISTED] |
| `V18_MO_NEO.md` | md | V18 science anchors | ARCHIVE | MEDIUM | 2026-08-03 | Overlaps `Video18_Sleep/VERIFY_Anchors_V18.md` | **Anchor file for V18 lives at root, not in the video folder** [LISTED] |
| `BangDoiChieu_v2_vs_Viral.md` | md | v2 script vs viral formula comparison | ARCHIVE | LOW | 2026-06-27 | — | Tier 3 [LISTED] |
| `GAP_AUDIT_va_Roadmap.md` | md | Earlier gap audit + roadmap | ARCHIVE | MEDIUM | 2026-06-24 | **Prior audit of this same project** | Tier 3; predates most current rules [LISTED] |
| `SPEC_GhepVideo_Desktop.md` | md | Desktop app spec | ACTIVE | MEDIUM | 2026-07-06 | — | Tool doc, not channel knowledge [LISTED] |
| `SPEC_Tool_SinhAnh_Flow.md` | md | Bulk image-gen tool spec | ACTIVE | MEDIUM | 2026-06-29 | — | Tool doc [LISTED] |
| `PROMPT_NangCap_Tool_AnToan.md` | md | Safe tool-upgrade prompt | ARCHIVE | LOW | 2026-06-28 | — | Tool doc [LISTED] |
| `Script_Video01_FINAL_MaxHai.md` | md | V01 script, comedy-max variant | DRAFT | LOW | 2026-06-25 | One of **6** V01 script artefacts | [LISTED] |
| `Script_Video01_Why-Did-Humans-Lose-Body-Hair.md` | md | V01 script | DRAFT | LOW | 2026-06-23 | Same group | [LISTED] |
| `Script_Video01_FINAL.txt` | txt | V01 TTS script v2 | GENERATED | LOW | 2026-06-27 | **md5-identical** to `_KHO_LUU_DaChet/Script_Video01_v2_skill.txt` | [LISTED] |
| `Script_Video01_FINAL_deAI.txt` | txt | V01 after de-AI polish | GENERATED | LOW | 2026-07-02 | Same group | Likely the true final; not labelled as such [LISTED] |
| `Script_Video01_SHOTLIST.txt` | txt | V01 shot list | GENERATED | LOW | 2026-06-25 | Same group | 47 KB [LISTED] |
| `Script_Video01_PROMPTS.txt` | txt | V01 image prompts | GENERATED | LOW | 2026-07-02 | Same group | 68 KB [LISTED] |
| `IMG_PROMPTS_UPLOAD.txt` | txt | V01 image prompts for Flow upload | GENERATED | LOW | 2026-07-02 | Overlaps `Script_Video01_PROMPTS.txt` | 545 KB [LISTED] |
| `IMG_PROMPTS_REF_SHORT.txt` | txt | V01 short-ref prompts | GENERATED | LOW | 2026-06-27 | Same group | 157 KB [LISTED] |
| `image_prompts_video01_FLOW_UPLOAD.txt` | txt | V01 Flow prompts | GENERATED | LOW | 2026-06-24 | Same group | [LISTED] |
| `CAST_REGEN_PROMPTS.txt` | txt | Cast regeneration prompts | ACTIVE | LOW | 2026-07-01 | Overlaps `Prompts_NhanVat_Kenh.md` | [LISTED] |
| `TEXT_Overlay_Goiy.txt` | txt | Overlay-text suggestions | ACTIVE | LOW | 2026-07-02 | — | 457 bytes [LISTED] |
| `MOTA_KENH_FINAL.txt` | txt | Final channel description | ACTIVE | MEDIUM | 2026-07-20 | Overlaps `Brand_Kit_Kenh.md` §2 | [LISTED] |

### 3.2 Per-video files (recurring pattern)

Every mature video directory follows the same generated-file pattern. Status is identical across all of them, so they are tabulated once by **role** rather than 300 times by path.

| Filename pattern | Type | Purpose | Status | Importance | Duplicate/Overlap | Notes |
|---|---|---|---|---|---|---|
| `Script_VideoNN_narration.txt` | txt | Final English narration, one sentence per line | CANONICAL *(per video)* | CRITICAL | Often **md5-identical** to `SHOTLINES_FULL.txt` | The de-facto final script. **No filename marks it as approved** |
| `SHOTLINES_FULL.txt` | txt | Narration split into shot lines | GENERATED | HIGH | md5-identical to `build/TTS_input_per_shot.txt` in V14–V18 | Verified identical pairs: V14, V15, V16, V17, V18 |
| `build/TTS_input_per_shot.txt` | txt | TTS feed | GENERATED | MEDIUM | duplicate of above | Third copy of the same text |
| `PROMPTS_FULL.txt` | txt | One image prompt per shot | GENERATED | MEDIUM | `PROMPTS_CLEAN.txt` in V11/V12 is a near-duplicate | 187 KB – 1.4 MB each |
| `gen_prompts.py` / `build_prompts.py` / `shot_data.py` | py | Prompt builders | GENERATED/ACTIVE | MEDIUM | 6 / 4 / 4 near-identical copies across videos | Per-video forks, not a shared library |
| `run_pipeline.py` | py | Per-video pipeline runner | ACTIVE | MEDIUM | 6 near-identical copies | V06–V11 |
| `build/tts_stdlib.py`, `build/1_make_tts_elevenlabs.py`, `build/2_assemble_video.py` | py | TTS + assembly | ACTIVE | HIGH | 5 copies each; V15 also has `2_assemble_video_FIXED.py` | See §20 secrets note |
| `Metadata_*.md` / `METADATA_*.md` | md | Title, description, tags, chapters | ACTIVE | HIGH | naming inconsistent (`Metadata_` vs `METADATA_`) | Present V02, V03, V06–V17 |
| `VERIFY_Anchors_*.md` / `VERIFY_Title_*.md` / `NGHIENCUU_*_MoNeo.md` / `MONEO_V19.md` | md | Fact-check / anchor ledger | CANONICAL *(per video)* | CRITICAL | **five different naming schemes for the same artefact** | V13, V14 use `VERIFY_Title_`; V15–V18 use `VERIFY_Anchors_`; V10–V12 use `NGHIENCUU_*_MoNeo`; V19 uses `MONEO_`; V17_Death uses `VERIFY_Anchors_V17_Death` |
| `Thumbnail_Prompt*.txt` / `THUMBNAIL_prompts*.txt` / `PROMPT_THUMBNAIL.txt` | txt | Thumbnail prompt | ACTIVE | MEDIUM | V11/V12/V13 keep `_v4`/`_v5` versions side by side | Three naming schemes |
| `THIEU_*.txt`, `PROMPTS_CON_THIEU_*.txt`, `CAN_GEN_LAI_17.txt`, `PROMPTS_GEN_LAI.txt`, `PROMPTS_145_SUALAI.txt`, `_fix_concat.txt` | txt | Ad-hoc repair lists for missing/regenerated images | GENERATED | LOW | — | Evidence of image-count drift; see `gotcha_gen_anh_lech_so` memory |
| `_cu/` (V18), `_nhap/` (V17, V19) | dir | Old / draft versions | ARCHIVE / DRAFT | LOW | — | Only V17, V18, V19 use these; earlier videos keep no draft history |

**Video-specific files worth naming individually:**

| Path | Status | Note |
|---|---|---|
| `Video17_Rain/Script_Video17_DUYET_EN-VI.md` (22 KB) | ACTIVE | EN+VI review table — the review format the user requires |
| `Video17_Rain/_nhap/Script_v2_truoc_feedbackGPT.md` (24 KB) | ARCHIVE | Pre-GPT-feedback snapshot |
| `Video17_Rain/_nhap/Script_V17_FULL_v2.md` (26 KB) | ARCHIVE | Full v2 |
| `Video17_Rain/_nhap/LENH_GPT_ReviewKichBan.md` | ARCHIVE | **v1 of the review prompt** — the original that `LENH_GPT_ReviewKichBan_v3.md` evolved from [READ-FULL] |
| `Video17_Rain/MOTA_VIDEO_V17.md`, `MOTA_DAN_THANG.txt`, `MOTA_SHORT_V17.txt`, `BINHLUAN_GHIM.txt` | ACTIVE | Description, pinned comment, short description |
| `Video18_Sleep/DANG_V18.md` (14 KB) | ACTIVE | Publishing checklist for V18 |
| `Video18_Sleep/_V19_material_TwoSleeps.txt` | DRAFT | **V19 material stored inside the V18 folder** — misplaced |
| `Video18_Sleep/_ch3_backup.txt` | ARCHIVE | Unexplained backup of chapter 3 |
| `Video18_Sleep/_cu/CHECKLIST_DANG_V18.md`, `_cu/METADATA_V18.md`, `_cu/MOTA_VIDEO_V18.md` | ARCHIVE | Superseded by root-level `V18_PACKAGING.md` and `DANG_V18.md` — **three-way overlap** |
| `Video10_Eyesight/NGHIENCUU_MatCan_Transcript.md` | ACTIVE | Research inside video folder (correct placement) |
| `Video03_.../why-are-humans-still-afraid-of-the-dark-timestamps.json` (355 KB) | GENERATED | Alignment data |
| `Video15_Allergies/build/V15_alignment.json` (432 KB) | GENERATED | Alignment data |
| `Video17_Death/` — only `VERIFY_Anchors_V17_Death.md` + `Script_Video17_DOT1.md` | DRAFT | **Abandoned V17 candidate**; index 17 later reused for Rain |

### 3.3 Corpus files (`2_KHO_BANGHI/`, created 2026-08-06)

| Path | Type | Purpose | Status | Importance | Notes |
|---|---|---|---|---|---|
| `2_KHO_BANGHI/00_KHO.md` | md | Corpus master index: two-axis classification, per-channel RPM/views/length, length↔RPM finding, tool docs, 4 recorded traps | CANONICAL | CRITICAL | [READ-FULL, authored in-session] |
| `2_KHO_BANGHI/<Channel>/00_BANG.md` | md | Per-channel table: view · title · duration · words · wpm | GENERATED | HIGH | 20 files |
| `2_KHO_BANGHI/<Channel>/YYYYMMDD_<Title>.txt` | txt | One transcript, 3-line metadata header + body | GENERATED | HIGH | **768 files** |
| `2_KHO_BANGHI/<Channel>/_vtt/*.vtt` + `*.info.json` | vtt/json | Raw downloads | GENERATED | LOW | 1,265 vtt — raw material, safe to regenerate |
| `2_KHO_BANGHI/_tool/vtt2text.py` | py | VTT → text, de-duplicates YouTube's rolling captions | ACTIVE | HIGH | [READ-FULL] |
| `2_KHO_BANGHI/_tool/keo_kenh.sh` | sh | Channel puller | ACTIVE | HIGH | [READ-FULL] |
| `2_KHO_BANGHI/_tool/convert.py` | py | Batch re-convert | ACTIVE | MEDIUM | [READ-FULL] |
| `2_KHO_BANGHI/_tool/do_kenh.sh` | sh | Niche scanner, 18 queries × 20 results | ACTIVE | MEDIUM | [READ-FULL] |
| `2_KHO_BANGHI/_tool/_quet_kenh.tsv` | tsv | 360 scan rows; **fields separated by literal `\t` text, not tab characters** | GENERATED | LOW | Parsing trap, documented |
| `2_KHO_BANGHI/_tool/_kenh_moi.txt` | txt | 23 newly discovered channels ≥100K | GENERATED | MEDIUM | |
| `2_KHO_BANGHI/_tool/keo.log` | log | Pull log incl. 888 impersonation warnings, 6 timeouts, 1 HTTP 429, 2 age-gate errors | GENERATED | LOW | |

### 3.4 Retired archive (`_KHO_LUU_DaChet/`, 20 files)

| Path | Purpose | Status | Notes |
|---|---|---|---|
| `README.md` | Explains why the folder exists | ARCHIVE | 2,021 B |
| `HE_THONG_KichBan_v1_11Video.md` | Script system v1 | DEPRECATED | v2 refuted 4 of its rules |
| `HE_THONG_Thumbnail_Signature_v3.md` | Thumbnail signature v3 | DEPRECATED | v6 forbids its core rule |
| `HE_THONG_Thumbnail_v5_ScriptToPackaging.md` | Thumbnail v5 | DEPRECATED | replaced by v6 |
| `TEMPLATE_Thumbnail_DoiThu.md` | Competitor thumbnail template | DEPRECATED | "character-left + object-right" DNA refuted → CENTRE ANCHOR |
| `SUBNGACH_KhaiThac_Can.md` | Sub-niche "the animal still inside you" | DEPRECATED | 0 breakouts / 4 months |
| `SUBNGACH_CoTheDoDa_2026-07-13.md` | Sub-niche Stone-Age body | DEPRECATED | same lane, same reason |
| `CongThuc_Title_TrieuView.md` | Million-view title formula | DEPRECATED | aimed at the dead lane |
| `SoTay_ChonDeTai_20DeTaiDaChungMinh.md` | 20 proven topics | DEPRECATED | replaced by `BANG_CAU` |
| `Script_Video01_FINAL_BACKUP.txt`, `..._35min_BACKUP.txt`, `..._OLD35_BACKUP2.txt`, `Script_Video01_PART1.txt`, `Script_Video01_v2_skill.txt` | V01 script backups | ARCHIVE | `Script_Video01_v2_skill.txt` is **md5-identical to root `Script_Video01_FINAL.txt`** |
| `image_prompts_video01_TOKENS.txt`, `image_prompts_video01_body_hair.txt` | V01 prompt archives | ARCHIVE | |
| `GhepVideo_Studio.tar.gz`, `GhepVideo_Studio_NextJS.tar.gz`, `GhepVideo_Studio_App.html`, `GhepVideo_WebApp.html` | Tool snapshots | ARCHIVE | Binary/HTML app archives |

> **Contradiction in the archive policy itself:** `00_LUAT_HIEN_HANH.md` states the 8 dead rule-files "đã bị xoá khỏi kho, không còn tồn tại" ("have been deleted, no longer exist"). They **do** exist — all 8 are in `_KHO_LUU_DaChet/`. The same file elsewhere correctly says they were moved there, not deleted. Two statements in one file disagree.

### 3.5 Claude instruction layer (outside project root)

**No `CLAUDE.md`, `AGENTS.md`, or `.claude/` directory exists inside the project.** All instruction lives in the user-global scope.

| Path | Type | Purpose | Status | Importance | Modified |
|---|---|---|---|---|---|
| `~/.claude/projects/-Users-admin-Desktop/memory/MEMORY.md` | md | Memory index, ~40 entries incl. 8 marked ⛔ dead | CANONICAL | CRITICAL | 2026-08-06 |
| `~/.claude/projects/-Users-admin-Desktop/memory/*.md` (36 files) | md | Individual memories: user/feedback/project/reference | CANONICAL | HIGH | Apr–Aug 2026 |
| `~/.claude/skills/sketchapiens-viet-kich-ban/` (46 KB + 6 files) | skill | Script-writing brain | CANONICAL | CRITICAL | 2026-08-06 |
| `~/.claude/skills/sketchapiens-chia-shot/` (55 KB + 5 files) | skill | Shot split + image prompts | CANONICAL | CRITICAL | 2026-08-06 |
| `~/.claude/skills/sketchapiens-thumbnail/` (17 KB) | skill | Thumbnail | CANONICAL | HIGH | 2026-08-06 |
| `~/.claude/skills/sketchapiens-chon-de-tai/` (8 KB) | skill | Topic selection | CANONICAL | HIGH | 2026-08-06 |
| `~/.claude/skills/sketchapiens-giu-chan-nguoi-xem/` (12 KB) | skill | Retention | CANONICAL | HIGH | 2026-08-06 |
| `~/.claude/skills/sketchapiens-bien-tap/` (8 KB + `qa_kichban.py`) | skill | Editing mode + machine QA | CANONICAL | HIGH | 2026-08-06 |
| `~/.claude/skills/viet-kich-ban-nguoi-que-co-dai/` | skill | **Older, unprefixed script skill for the same channel** | DEPRECATED *(inferred)* | HIGH | — |
| `~/.claude/skills/chan-doan-kenh-youtube/`, `tham-dinh-ngach-youtube/`, `an-toan-kiem-tien/`, `mo-xe-doi-thu/`, `thiet-ke-thumbnail/`, `checklist-dang-video-long-form/`, `chong-van-ai-narration-en/`, `chon-giong-va-am-thanh/`, `kiem-chung-su-lieu/`, `tang-chuyen-doi-sub/`, `techstack-kenh-faceless/`, `giu-chan-nguoi-xem-nghe-ngu/`, `dinh-tuyen-model/`, `youtube-metadata/`, `youtube-seo/` | skill | Shared cross-project YouTube skills | ACTIVE | MEDIUM–HIGH | Jul–Aug 2026 |
| `~/.claude/skills/` — ~20 further skills (`frontend-design`, `vitest`, `playwright-cli`, `viet-kich-ban-sinh-ton-vn`, `viet-kich-ban-shorts-funny`, `punch-up-hai-sinh-ton` 52 KB, …) | skill | Unrelated to this project | ACTIVE | NONE *(for this project)* | Jul 2026 |
| `skills_build/chong-van-ai-narration-en/SKILL.md` *(inside project)* | md | **Copy of a global skill kept in the project** | UNKNOWN | LOW | — |


---

## 4. Canonical Knowledge Map

*Rules are reported as found. Nothing is merged, reconciled or corrected here.*

### 4.1 Channel positioning

**Sources:** `Brand_Kit_Kenh.md` [HEADINGS] · `MOTA_KENH_FINAL.txt` [LISTED] · `BÀN_GIAO_DuAn.md` [LISTED] · `~/.claude/skills/viet-kich-ban-nguoi-que-co-dai/SKILL.md` PHẦN 0 [READ-FULL] · `CHINHSACH_YOUTUBE_2026_AnhHuong.md` [HEADINGS]

The channel is an English-language faceless stickman explainer in the "Ancient Humans Explained" niche. The core engine is stated in the skill:

> *"Engine của ngách: biến một hành vi ĐỜI THƯỜNG thành sợi chỉ cổ xưa kỳ lạ… lấy một thứ khán giả tự làm mỗi ngày… rồi hỏi 'tổ tiên ta làm điều này thế nào?', và kết lại bằng cú nhận ra: ta với người 50.000 năm trước nối nhau bằng đúng hành vi đó."*

A differentiation requirement was added 2026-08-05 in `00_LUAT_HIEN_HANH.md`, sourced to YouTube's own inauthentic-content guidance:

> *"Gỡ tên kênh và logo đi, dán video của mình cạnh 20 video cùng title của 20 kênh khác — có ai chỉ ra được cái nào là của mình không?"*
> *"→ Luật thêm vào cửa 1: mỗi video phải có ít nhất MỘT thứ mà 20 kênh kia không có."*

The same entry records that V18's own opening failed this test: *"V18 của mình mở bằng 'Tonight you will go to bed behind a door that locks.' **Cùng khuôn**."*

**Multi-file rule:** channel positioning appears in `Brand_Kit_Kenh.md`, `MOTA_KENH_FINAL.txt`, the old skill and the new `sketchapiens-*` skills. **Possibly outdated:** `Brand_Kit_Kenh.md` (2026-06-24) still presents channel-name options as unresolved, while `MOTA_KENH_FINAL.txt` (2026-07-20) is titled "FINAL".

### 4.2 Audience

**Sources:** `checklist-dang-video-long-form/SKILL.md` §3 [READ-FULL] · `chan-doan-kenh-youtube/SKILL.md` §4 [READ-FULL] · `2_KHO_BANGHI/00_KHO.md` [READ-FULL]

> *"RPM chênh nhau **gấp đôi** chỉ vì nhắm tệp nào… đặt đúng English (United States) nếu nhắm Mỹ, đừng để English chung chung."*
> *"Không bật auto-dubbing sang nhiều thứ tiếng nếu mục tiêu là RPM cao."*

The corpus added a measured audience axis on 2026-08-06: nexlev `countryTop` per channel. Two high-view channels were flagged as **wrong audience** — Super Joy Animations (Pakistan, RPM 3.07) and Barely Evolved (Croatia, RPM 2.73) — with the rule recorded in `00_KHO.md`:

> *"Học cách kể của Super Joy thì được. Lấy con số 586.888 của nó làm đích thì không — đó là view của một thị trường khác."*

**No first-party audience data exists in the project** — no demographics export, no geography report. All audience knowledge is inferred from competitors.

### 4.3 Topic strategy

**Sources (law):** `BANG_CAU_TatCa_CuNo_2026-07-29.md` [LISTED] · `NGHIENCUU_CloneSwarm_2026-07-29.md` [LISTED] · `BANDO_CumChuDe_CoCau_2026-07-27.md` [LISTED] · `chien_luoc_lay_de_tai_da_co_cau.md` (memory) [READ-FULL] · `CONGTHUC_InkExplainer_BestOf.md` [READ-FULL] · `WORKFLOW_Production.md` Stage 0 [HEADINGS]

`00_LUAT_HIEN_HANH.md` permission table assigns topic selection to `BANG_CAU_TatCa_CuNo` **plus a mandatory live clone-swarm check**, replacing three now-dead files.

The strategy reversed direction on 2026-08-05/06. Memory `chien_luoc_lay_de_tai_da_co_cau.md`:

> *"Lấy đề tài ĐÃ CÓ CẦU rồi làm hơn — bỏ săn đề tài trinh nguyên."*

`CONGTHUC_InkExplainer_BestOf.md` formalises it as five steps, and carries a self-correction:

> *"Bản đầu của file này viết như thể mọi thứ Ink Explainer lấy lại đều cấm. Sai, và nó làm kênh mình tự trói tay."*

with an explicit reuse boundary table — anchors (site, date, researcher name, number) reusable; thesis, beat order, jokes, metaphors, footage not.

`WORKFLOW_Production.md` Stage 0 marks its own first sub-step as abandoned: *"0.1 ~~Tìm cầu — quét bình luận đối thủ~~ ⚠️ ĐÃ THỬ, KHÔNG HIỆU QUẢ."*

**Possibly outdated:** `NGHIENCUU_DoiSong_CoDai_2026-07-13.md`, `NGHIENCUU_V16_LaneCheck_2026-07-26.md` — both predate the 29/07 rewrite; `00_LUAT` says the V16 file's open question is *"phần lớn đã được BANG_CAU + CloneSwarm trả lời"* but leaves it unresolved.

**Deferred topic zone** (`00_LUAT_HIEN_HANH.md`): twins / infant death / orphans / child mortality are postponed until after YPP because YouTube names *"putting minors in distressing situations"*. The twin topic passed gate 0 on 05/08 and was still held back.

### 4.4 Title strategy

**Source of truth per `00_LUAT`:** `HE_THONG_KichBan_v2_14Video.md` PHẦN C ("CÔNG THỨC TITLE, 159 VIDEO") [HEADINGS]. Replaces ⛔ `CongThuc_Title_TrieuView`, ⛔ `BANDO_NgachTitle_Thang`, ⛔ `NGHIENCUU_Title_3Kenh_Gap`.

The niche title mould, from the older skill [READ-FULL]:

> `[Why / How / When / Did / Could / Do] + Ancient Humans + [hành vi đời thường, thân mật, hơi cấm kỵ]?`
> *"< 60 ký tự; từ tò mò mạnh ở đầu; hứa một câu trả lời mà phải bấm mới biết; KHÔNG clickbait dối."*

A demotion of title importance is recorded in memory `title_la_buoc_quyet_dinh.md`:

> *"Title là bộ LỌC, không phải động cơ… 20 kênh cùng title → 1 quả 59K, 19 quả <6K. Ưu tiên thumbnail → title → hook."*

`HE_THONG_KichBan_v2` PHẦN C contains a heading *"🎯 KHUÔN MẠNH NHẤT — VÀ KÊNH CHƯA DÙNG LẦN NÀO"* — a named unused opportunity.

**Live evidence of the process:** `VERIFY_Title_V13_Stress_*.md`, `VERIFY_Title_V14_Milk_*.md` are title-verification artefacts for two videos only. V15–V19 have no equivalent.

### 4.5 Thumbnail system

**Source of truth:** `PROMPT_TONG_Thumbnail_v6.md` [HEADINGS] + `TEMPLATE_Thumbnail_KHOA_v1.md` [HEADINGS] + skill `sketchapiens-thumbnail`. Replaces three dead files.

Five hard rules (PHẦN B):
> LUẬT 1 — TÂM KHUNG DÀNH CHO VẬT KỂ CHUYỆN, KHÔNG PHẢI NHÂN VẬT
> LUẬT 2 — CHỮ PHẢI THÊM THÔNG TIN MỚI, KHÔNG LẶP TITLE
> LUẬT 3 — NỀN XỈN + 1-2 ĐIỂM BÃO HOÀ
> LUẬT 4 — MỌI ÁNH MẮT KHOÁ VÀO TRONG
> LUẬT 5 — KHÔNG BAO GIỜ ĐỂ MỌI KHUÔN MẶT CÙNG MỘT CẢM XÚC

Three absolutely banned prompt words (`TEMPLATE_Thumbnail_KHOA_v1.md`): **`cartoon` · `clean` · `smooth`**.

The template's most important recorded lesson:
> *"Khi model ĐÃ vẽ đúng một thứ, ĐỪNG thêm luật cho thứ đó."* (from 7 rounds on V18)

Three thumbnail metrics were **refuted** and are recorded in memory `gotcha_do_tong_thumbnail_vo_nghia.md`: "brightness 80–110" (correlation ≈ 0), "text 13–19%" (actually 22%), replaced by a new rule "face/hands/feet must be solid white 3–6%".

**Timing rule** (memory `workflow_thumbnail_lam_cuoi.md`, `WORKFLOW_Production.md` 04/08 revision): gate 1 scores **concept only**; the real image is built at stage 5a after video images exist.

**Multi-file / conflicting:** `ArtBible_NguoiQueCoDai.md` (2026-06-25) §6 and `TRAIN_ChatGPT_Thumbnail.md` (2026-07-25) both contain thumbnail guidance predating v6. `CONCEPT_Thumbnail_V16_V17.md`, `V17_PROMPT_THUMBNAIL.md` are per-video. `NGHIENCUU_15Thumbnail_Mack.md` and `NGHIENCUU_Thumbnail_50K/` (31 competitor jpgs + `list.tsv`) are the evidence base.

### 4.6 Script structure

**Sources:** `HE_THONG_KichBan_v2_14Video.md` (law) · `FLOW_VietKichBan_11Cong.md` (process) · `RUBRIC_KichBan.md` (scoring) · `sketchapiens-viet-kich-ban` skill · `CONGTHUC_InkExplainer_BestOf.md`

Macro skeleton, from the older skill [READ-FULL]:
> *"1. Ngay sau hook, chốt câu 'không phải một lý do'… 2. Trải 3–7 TẦNG lý do… 3. Để dành tầng đỉnh cho cuối và báo trước… 4. Trước khi kết, chèn một khúc thành thật / mặt tối… 5. Rồi mới tới KẾT."*

Hook: 6 beats, 45–75 seconds. `HE_THONG_KichBan_v2` PHẦN D is titled *"CẤU TRÚC MỞ BÀI (14/14 đồng ý)"*.

**Four v1 rules explicitly refuted** in PHẦN A — including *"Cấm nói chúng ta không biết"* and *"Tối thiểu 5 mỏ neo/phút"* — with the note *"⚠️ ĐÃ ĐẾM LẠI — CON SỐ TRONG BẢNG TRÊN LÀ SAI."*

**Per-chapter QA** was made mandatory 2026-08-05 (`WORKFLOW_Production.md` §"🔬 QA TỪNG CHƯƠNG").

**Possibly outdated:** `HE_THONG_KichBan_v2` PHẦN B2 gives three technical targets — sensory-word density 7–9%, one question every 60–90 s, syntax rhythm. `RUBRIC_KichBan.md` LUẬT 0 and memory `feedback_so_do_khong_phai_dich.md` both now classify these as **diagnostics, not targets**, and record that the 7–9% figure was measured with a different word-list and is not directly comparable.

### 4.7 Retention system

**Sources:** `sketchapiens-giu-chan-nguoi-xem` skill · `giu-chan-nguoi-xem-nghe-ngu` skill (shared) · `NganHang_ReHook_BucketBrigade.md` · `CO_CHE_3LOP_Winner_2026-07-29.md` · `MoXe_15Khoi_KichBan_DoiThu.md`

`NganHang_ReHook_BucketBrigade.md` splits its contents deliberately:
> **PHẦN A — CÂU NỐI GENERIC (✅ dùng thoải mái)** — 5 sub-types
> **PHẦN B — CÂU SÁNG TẠO CỦA ĐỐI THỦ (❌ KHÔNG copy — chỉ học pattern → tự viết)**

It also carries the bookend rule: *"luật BOOKEND: viết câu cuối trước"* (per `00_LUAT` Tier-2 table).

The device checklist added to `sketchapiens-viet-kich-ban` on 2026-08-06 is explicitly framed as diagnostic:
> *"Đây là bảng CHẨN, không phải danh sách đi chợ… Phép thử một câu: câu này có tồn tại không nếu không có bảng kiểm nào? Không → cắt."*

### 4.8 Narration voice

**Sources:** `KHO_GiongCamXuc_DoiThu.md` [READ-FULL] · `LENH_GPT_BoiCanh_TayNghe.md` [READ-FULL] · `viet-kich-ban-nguoi-que-co-dai/SKILL.md` PHẦN 4 [READ-FULL] · `TRAIN_ChatGPT_TOANBO_DuAn.md` PHẦN 6 [READ-PART]

Two schools, chosen by topic:
> **A. ZENN — deadpan LẠNH văn học** (psychology/memory/death)
> **B. STICKLY/MACK — deadpan hội thoại, hài khô** (behaviour/animals/"how")
> *"Chung tuyệt đối: mở cảm xúc THẤP → leo; KHÔNG '!'; khoảng lặng = fragment sau câu dài."*

Pronoun law (skill PHẦN 4):
> *"'you' = NGƯỜI XEM… 'we / us / our' = CẢ LOÀI NGƯỜI… KHÔNG 'I' (người dẫn), KHÔNG 'we' kiểu 'kênh/chúng tôi'."*

Signature device — pre-loading:
> *"Gọi tên cảm xúc TRƯỚC fact… 'here's the part nobody talks about.' → trước MỖI reveal lớn dán 1 nhãn cảm xúc rồi mới thả fact."*

**Measured counter-example on record:** `CONGTHUC_InkExplainer_BestOf.md` notes the 769K video uses `"I"` once — *"phá luật 'I ≈ 0', vẫn 769K"*.

### 4.9 Anti-AI writing rules

**Sources:** `chong-van-ai-narration-en` skill [READ-FULL] · `TRAIN_ChatGPT_BuocPolish.md` [LISTED] · `TRAIN_ChatGPT_TOANBO_DuAn.md` PHẦN 8 [READ-PART] · `LENH_GPT_BoiCanh_TayNghe.md` [READ-FULL] · `sketchapiens-bien-tap/qa_kichban.py` [READ-FULL]

The skill lists 14 AI tells and a doctor's oath:
> *"KHÔNG đổi nghĩa, KHÔNG đổi sự kiện/số liệu/tên riêng, KHÔNG thêm/bớt cú đùa. KHÔNG đổi SỐ DÒNG."*

The audience-evidence justification, repeated in three files:
> *"Bình luận 'The chatGPT writing is extremely noticeable here' được 4.400 like, đứng thứ tư trong 6.800 bình luận dưới video 2 triệu view của Mack."*

**Four hard constraints** are machine-checked by `qa_kichban.py`: `!` = 0 · no em-dash · `I` ≈ 0 · no 3 long sentences in a row. Everything else is soft. Source: `RUBRIC_KichBan.md` LUẬT 0 + memory `feedback_so_do_khong_phai_dich.md`.

**Rule added 2026-08-06** (`LENH_GPT_ReviewKichBan_v3.md`): *"lỗi ẩn dụ thì CẮT CẢ CÂU, đừng thay chữ trong câu"* — derived from three patched sentences becoming the three worst-ranked lines in the next review round.

### 4.10 Fact-checking rules

**Sources:** `kiem-chung-su-lieu` skill [LISTED] · `FLOW_VietKichBan_11Cong.md` gate 3 [READ-FULL] · per-video `VERIFY_Anchors_*.md` / `MONEO_V19.md` [READ-PART] · `CHINHSACH_YOUTUBE_2026_AnhHuong.md` §1 [HEADINGS]

The anchor register is the project's claim ledger. `MONEO_V19.md` is the most developed instance: each anchor M1–M11 carries source, exact figure, and in several cases an explicit prohibition, e.g. a ban on inventing evolutionary causation for vasopressin, and M5 marked **DEAD** because a competitor's 7.8M video owns the material.

Two rules recorded from real failures:
> *"mở primary source, không tin snippet"* — after four numbers taken from search snippets proved wrong (Ekirch "500", the Wehr interval, "four hours", "half of deaths" vs "half of attacks").
> *"mọi câu thêm vào sau cổng 3 phải quay lại chạy cổng 3 một lần nữa"* — added to `MONEO_V19.md` on 2026-08-06 after a fabricated event sequence entered the script during a post-gate word-count top-up.

`CHINHSACH_YOUTUBE_2026_AnhHuong.md` §1 ties fact-checking to policy risk: the 16/07/2026 "inauthentic content" rule is scored **per channel, not per video**.

**Naming inconsistency:** the same artefact is called `VERIFY_Anchors_*`, `VERIFY_Title_*`, `NGHIENCUU_*_MoNeo`, `MONEO_*` and `V18_MO_NEO` across the project.


### 4.11 Research workflow

**Sources:** `WORKFLOW_Production.md` Stage 0 · `mo-xe-doi-thu` skill · `TEARDOWN_PLAYBOOK_RaLenh_AI.md` · `PROMPT_PACK_NotebookLM.md` · `PLAYBOOK_NotebookLM_DoiThu.md` · `LENH_NotebookLM_ChuaLam.md` · `VAULT_NotebookLM_BanGoc_DoiChieu.md` · `2_KHO_BANGHI/_tool/*` · nexlev MCP

Three generations of research method coexist in the repo:
1. **NotebookLM digest** (Jul 2026) — 4 reports digested into local files; `VAULT_NotebookLM_BanGoc_DoiChieu.md` maps originals → destinations and lists *"6 chỗ bản máy đúng hơn bản gốc"*.
2. **nexlev MCP queries** (Aug 2026) — channel metrics, monetisation, RPM, faceless classification.
3. **yt-dlp raw corpus** (2026-08-06) — 768 transcripts; `00_KHO.md` documents 4 traps including *"Đoán handle rồi tin dấu ✅"* (two wrong channels pulled) and *"Mọi chỉ số tính theo RANH GIỚI CÂU đều vô nghĩa"* (ASR punctuates, not the writer).

`00_LUAT` assigns the live NotebookLM file as `LENH_NotebookLM_ChuaLam.md`; the other two NotebookLM files are Tier 4.

### 4.12 Character system

**Sources:** `CastBible_DienVien.md` · `BasePack01_Sketchapiens.md` · `Prompts_NhanVat_Kenh.md` · `SOP_NhatQuan_NhanVat.md` · `CAST_REGEN_PROMPTS.txt` · `chia-shot-va-prompt-anh` skill PHẦN 3

Design DNA: one body, costume presets. Token registry defines `@MODERNYOU`, `@ANCESTOR`, `@FORAGER`, `@CHILD`, `@ELDER`, `@SCIENTIST`, `@CHIMP`.

> ⚠️ **Direct contradiction.** `CastBible_DienVien.md` §4 defines a `@TOKEN` convention with a registry. The shot-splitting skill states the opposite: *"Không cast-token. Nhất quán = lặp y nguyên khối mô tả nhân vật trong mọi prompt"* and *"Nhất quán bằng CHỮ, không bằng ref… không @token, không 'same as before'."* Both are live documents. See §17.

Four files describe the same character system with overlapping content and no stated precedence.

### 4.13 Visual style

**Sources:** `ArtBible_NguoiQueCoDai.md` · `chia-shot-va-prompt-anh` skill PHẦN 0/2 · `REF_Style/` (3 PNGs) · memory `gotcha_style_doodle_khong_hoathinh.md` · `NGHIENCUU_NguPhapHinh_InkExplainer.md` + `NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md`

Background rule (skill, updated 07/2026):
> *"NỀN THEO NGỮ CẢNH — KHÔNG theo tỉ lệ cố định… ~60% nền TRẮNG · ~40% nền CẢNH flat-màu — nhưng con số đó chỉ là kết quả, không phải quy tắc."*

> ⚠️ **Direct contradiction on line quality.** The shot skill's STYLE anchor says *"Clean flat 2D cartoon explainer with smooth, even, confident medium-bold black outlines"* and its PHẦN 6 says *"Bỏ hẳn từ 'hand-drawn'"*. Memory `gotcha_style_doodle_khong_hoathinh.md` says the opposite: three banned words `cartoon`/`clean`/`smooth`, and that the note "đối thủ vẽ sạch digital" from 07/2026 was **SAI** — 4K frames show hand-wobble. `TEMPLATE_Thumbnail_KHOA_v1.md` also bans those three words. See §17.

Two visual-grammar files with the same date and topic (`NGHIENCUU_NguPhapHinh_InkExplainer.md`, `NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md`) — the second is titled "remeasured on all of 2 videos", implying supersession, but neither declares it.

### 4.14 Shot splitting

**Source of truth:** `sketchapiens-chia-shot` skill (55 KB, largest project skill) · `chia-shot-va-prompt-anh` skill PHẦN 1 [READ-FULL]

> *"~8-10 từ/shot · ~2.6-3.3 giây/shot · ~18-23 shot/phút · ~1.4 shot mỗi câu"*
> *"KHÔNG đổi chữ narration khi tách — chỉ chèn ranh giới dòng."*

Measured production reality (`CHOT_V19.md`): V17 = 263 shots / 2.1 s per image; V18 = 224 shots / 2.5 s.

**Refuted:** `CHOT_V19.md` records that 4-channel pacing measurement produced *"KẾT LUẬN LÀ KHÔNG CÓ KẾT LUẬN"* — 2.5–2.7 s/image gave medians of 11,000 and 29,000; 4.3–4.6 s gave 45,000 and 10,000. A `zoompan` proposal from 05/08 was withdrawn.

**Stale number caught:** `CHOT_V19.md` records that a line reading *"~3.200–3.800 từ · ~530 ảnh"* survived after the length rule changed, and *"530 ảnh × 2,5 giây = 22 phút, không phải 10. Suýt nữa gen thừa hơn 250 ảnh."*

### 4.15 Image prompting

**Sources:** `chia-shot-va-prompt-anh` skill PHẦN 2 · `SPEC_Tool_SinhAnh_Flow.md` · per-video `gen_prompts.py` / `build_prompts.py` / `shot_data.py` / `PROMPTS_FULL.txt`

Six-block prompt template: `[STYLE] [SUBJECT] Framing: [FRAMING]. [CONSIST] [SCENE] [TEXT]. [NEG]` — four blocks pasted verbatim, three varied per shot.

Policy filter (PHẦN 7): avoid `naked/nude/bare`, no close-up blood/gore, child+predator scenes must stay symbolic.

**Known failure mode** (memory `gotcha_gen_anh_lech_so.md`): the generation tool names files by an internal counter, not by prompt number — running two batches produced 404 images for 301 prompts. Rule: always generate into an empty folder, one pass, count files before assembly. Repair artefacts (`THIEU_*.txt`, `CAN_GEN_LAI_17.txt`, `PROMPTS_GEN_LAI.txt`) show this happened repeatedly.

### 4.16 Production workflow

**Source of truth:** `WORKFLOW_Production.md` (stages 0–4, gates 0–4) + `FLOW_VietKichBan_11Cong.md` (11 gates, script only) + `QUY_TRINH_2_CONG.md` (universal two-gate discipline).

Biggest structural rule, stated at the top of `WORKFLOW_Production.md`:
> *"⚠️ THAY ĐỔI LỚN NHẤT: PACKAGING ĐI TRƯỚC KỊCH BẢN"* — packaging precedes the script.
Amended 04/08: *"tách CONCEPT khỏi ẢNH THẬT"*; amended 05/08: *"THUMBNAIL RA KHỎI GIAI ĐOẠN 1 HOÀN TOÀN"*.

`QUY_TRINH_2_CONG.md` names three things that prove nothing:
> *"Ba thứ KHÔNG chứng minh được gì: chạy không lỗi · đủ số file · đúng độ dài"*

Four working modes are defined in `00_LUAT_HIEN_HANH.md`, one skill each, with a no-mixing rule:
> *"Không trộn hai chế độ trong một phiên — đang viết mà đi tra mỏ neo là mất mạch, đã dính nhiều lần."*
Mode ② WRITE explicitly forbids opening nexlev or searching the web.

**Overlap:** `WORKFLOW_Production.md` Stage 2 and `FLOW_VietKichBan_11Cong.md` describe the same script phase at different granularity, with no stated precedence between them.

### 4.17 Metadata and SEO

**Sources:** `youtube-metadata` skill (+6 reference files) · `youtube-seo` skill (+5) · `checklist-dang-video-long-form` skill · per-video `Metadata_*.md` (V02, V03, V06–V17) · `Video18_Sleep/DANG_V18.md` · `V18_PACKAGING.md` · `Video17_Rain/MOTA_*`

Mid-roll economics (`checklist-dang-video-long-form`):
> `RPM ≈ (số ổ quảng cáo người xem đi qua) × (tiền net mỗi nghìn lần hiện)`
> *"video phải dài trên 8 phút mới được chèn mid-roll… 8-10 phút là vùng chết về doanh thu"*
> *"đặt một ổ mỗi 2,5 – 3,5 phút"*; manual+auto hybrid ≈ +5% vs manual only.

**Gap:** V18 and V19 have no `Metadata_*.md`; V19 has none of the packaging artefacts the earlier videos have.

### 4.18 Analytics and postmortem

**Sources:** memory `chan_doan_kenh_benh_A.md` [READ-FULL via memory index] · `chan-doan-kenh-youtube` skill [READ-FULL] · `BOCTACH_*` files · nexlev MCP

The channel's own analytics exist **only inside a memory file**, not in the project:
> *"367 hiển thị/5 ngày → bệnh A là CHẮC. Nhưng CTR 3,5% đo trên 13 lượt bấm và retention 55,6% đo trên 12 người → ⛔ KHÔNG kết luận được thumbnail/kịch bản ổn hay không."*
> *"Đừng lấy V17 làm chuẩn cho bất cứ thứ gì."*

The diagnostic skill defines three diseases (A: not being pushed / B: pushed but no clicks / C: clicked but abandoned) with thresholds (impressions <5,000 after 2 weeks; CTR <2%; AVD <30%).

**There is no analytics file anywhere in the project directory.** No CSV, no export, no per-video metrics file. See §14.

### 4.19 Claude workflow

**Sources:** `00_LUAT_HIEN_HANH.md` (mode table, permission table, skill-prefix rule) · 6 `sketchapiens-*` skills · 36 memory files

Skill-prefix rule (05/08):
> *"Trước đây skill riêng của kênh đặt tên chung chung, nên luật đo từ kênh này bị áp nhầm sang dự án khác. Nay tất cả đều có tiền tố `sketchapiens-`."*
> *"⚠️ Luật: đo được gì trên kênh này thì ghi vào skill `sketchapiens-*` hoặc file trong kho. Ghi vào skill dùng chung là dạy sai cho mọi dự án sau."*

Precedence rules (`00_LUAT`):
> *"1. Tầng thấp hơn thắng… 2. Số đếm tay trên transcript gốc thắng MỌI báo cáo… 3. File có ngày mới hơn thắng — nhưng chỉ khi cùng tầng. 4. Không giải quyết được → đo lại, đừng chọn bừa."*

Model routing (memory `feedback_kichban_luon_fable5.md`, `model_routing_pref.md`): Opus 5 default for body and all other steps; Fable 5 only for the 15-second hook and the ending.

### 4.20 Human review workflow

**Sources:** `LENH_GPT_ReviewKichBan_v3.md` [READ-FULL] · `LENH_GPT_BoiCanh_TayNghe.md` [READ-FULL] · memory `feedback_vong_review_gpt.md` [READ-FULL] · memory `rubric_mu_loi_cau_truc.md` · `Video19_NightWalk/_nhap/Script_V19_GhiChu.md`

Why an outside listener is mandatory (memory `rubric_mu_loi_cau_truc.md`):
> *"V17 chấm 68/74 vẫn hỏng cấu trúc; V19 sạch 7 mục cứng vẫn xây trên bí ẩn không tồn tại. Người viết không tự chấm được vì họ biết đáp án."*

Boundary rule:
> *"cho họ thứ NGƯỜI XEM NHÌN THẤY, giấu thứ chỉ MÌNH BIẾT"* — title + thumbnail + genre given; rubric, lane theory, benchmarks withheld.

Feedback triage: **ÁP NGAY / ÁP CÓ SỬA / BỎ + lý do**, with a 7-row rejection table and 4 categories that must always be accepted (*"tôi bỏ ở đây"*, *"câu này tôi phải đọc lại"*, *"title hứa X mà tới phút Y mới trả"*, *"câu này nghe như máy viết"*).

> ⚠️ **Live contradiction inside one file.** `LENH_GPT_ReviewKichBan_v3.md` opens with *"🔴 LUẬT GỐC… KHÔNG dán luật kênh, không dán rubric, không dán bối cảnh ngách vào GPT"* and ends with a 2026-08-06 section reversing it: *"Luật 'cấm dán bối cảnh' ở đầu file này SAI. Đã đảo."* Both statements remain in the file. See §17.

---

## 5. Claude Instructions and Memory Audit

**No project-scoped instruction file exists** — no `CLAUDE.md`, no `AGENTS.md`, no `.claude/` inside the project root. All instruction is user-global, which means it loads for **every** project on this machine, not only this one.

| File / group | When loaded | Scope | Core content | Duplicates | Contradictions | Too long / generic? | Stale rules? | Could mislead Claude? |
|---|---|---|---|---|---|---|---|---|
| `memory/MEMORY.md` (14 KB) | Every session, automatically | Global (all projects under `-Users-admin-Desktop`) | Index of ~40 memories; 8 marked ⛔ dead with old content retained inline | — | No | **Yes — 14 KB every session**, and it carries dead-rule text inline | Yes, but explicitly labelled ⛔ | **Yes** — dead rules are quoted in full under "*Nội dung cũ:*" and can be read as guidance |
| `memory/*.md` (36 files) | On recall | Global | user(2) / feedback(11) / project(3) / gotcha(6) / insight+workflow+strategy(14) | `subngach_cothe_doda` ⛔ and `lane_vebanj_khong_no_2607` cover the same finding | `feedback_kichban_luon_fable5.md` title says "always Fable 5", body says Opus 5 default — **title contradicts body** | Individually fine | 4 memories point at ⛔ dead files via relative paths | Medium — memories reflect state at write time |
| `sketchapiens-viet-kich-ban` (46 KB + 6 files) | Mode ② WRITE | This project | Script brain; per-chapter device checklist; diagnostic-not-shopping-list principle | Overlaps `viet-kich-ban-nguoi-que-co-dai` heavily | Length guidance vs `RUBRIC` LUẬT 0 | **Yes — 46 KB** | Possibly the 7–9% sensory figure | Medium |
| `sketchapiens-chia-shot` (55 KB + 5 files) | Mode ④ PRODUCTION | This project | Shot split + 6-block prompt template | Overlaps `chia-shot-va-prompt-anh` | **Yes** — `@token` and `clean/smooth` (see §17) | **Yes — 55 KB, largest** | Yes — "đối thủ vẽ sạch digital" refuted by memory | **Yes** |
| `sketchapiens-thumbnail` (17 KB) | Mode ④ | This project | Thumbnail rules | Overlaps `PROMPT_TONG_Thumbnail_v6.md`, `thiet-ke-thumbnail` | Not verified | No | Unknown | Low |
| `sketchapiens-chon-de-tai` (8 KB) | Mode ① RESEARCH | This project | Topic gates 0–3 | Overlaps `BANG_CAU`, `WORKFLOW` Stage 0 | No | No | Unknown | Low |
| `sketchapiens-giu-chan-nguoi-xem` (12 KB) | Mode ② | This project | Retention | Overlaps `giu-chan-nguoi-xem-nghe-ngu` | No | No | Unknown | Low |
| `sketchapiens-bien-tap` (8 KB + `qa_kichban.py`) | Mode ③ EDIT | This project | Edit mode + machine QA script | — | No | No | No | Low — the .py is the most objective artefact in the project |
| `viet-kich-ban-nguoi-que-co-dai` | Whenever an "ancient humans" title is given | **Unprefixed — fires for any project** | Full older script brain, 9 parts + 3 reference files | **Direct predecessor of `sketchapiens-viet-kich-ban`** | Its PHẦN 2 mandates the "strip modern comforts" hook beat that the 2026-08-06 rain comparison found absent from the 1.1M competitor video | Yes | **Yes** — references `TEMPLATE_Thumbnail_DoiThu.md` (⛔ dead) in PHẦN 9 | **Yes — highest-risk instruction file found** |
| `chia-shot-va-prompt-anh` | Shot-splitting requests | **Unprefixed** | Older shot skill | Predecessor of `sketchapiens-chia-shot` | Same `@token` / `clean` issues | Yes | **Yes** — PHẦN 9 points to ⛔ `TEMPLATE_Thumbnail_DoiThu.md` | **Yes** |
| `chan-doan-kenh-youtube`, `tham-dinh-ngach-youtube`, `an-toan-kiem-tien`, `mo-xe-doi-thu`, `thiet-ke-thumbnail`, `checklist-dang-video-long-form`, `chong-van-ai-narration-en`, `chon-giong-va-am-thanh`, `kiem-chung-su-lieu`, `tang-chuyen-doi-sub`, `techstack-kenh-faceless`, `giu-chan-nguoi-xem-nghe-ngu`, `dinh-tuyen-model`, `youtube-metadata`, `youtube-seo` | Shared, any project | Cross-project | Generic YouTube craft | `youtube-metadata` overlaps `youtube-seo`; `thiet-ke-thumbnail` overlaps `sketchapiens-thumbnail` | `00_LUAT` forbids channel-specific numbers here — not verified file-by-file in this audit | Some are long | Unknown | Low–Medium |
| ~20 unrelated skills (`frontend-design`, `vitest`, `playwright-cli`, `emil-design-eng` 27 KB, `punch-up-hai-sinh-ton` 52 KB, `viet-kich-ban-shorts-funny` 34 KB, `skill-creator` 33 KB, …) | Other projects | None here | Web dev, other YouTube niches | — | — | Yes | — | Low — but they occupy the skill namespace |
| `skills_build/chong-van-ai-narration-en/SKILL.md` *(inside project)* | Never (not in skills dir) | None | Copy of a global skill | Duplicate of `~/.claude/skills/chong-van-ai-narration-en/` | Unknown whether the two are identical | — | Unknown | Low, but a silent fork risk |

**Agents / commands / hooks:** none found. No `.claude/agents/`, no custom slash-commands, no hook definitions anywhere in the project or in the project-scoped config.


---

## 6. Prompt Library Audit

*Prompts are described, never rewritten.*

| Prompt name / path | Intended task | Inputs expected | Output expected | Strengths | Risks | Duplicate prompts | Status |
|---|---|---|---|---|---|---|---|
| `sketchapiens-chon-de-tai` SKILL | Topic research + gates 0–3 | Niche, candidate topic | Go/no-go + clone-swarm count | Tied to `BANG_CAU` evidence | Not read in full this audit | `WORKFLOW_Production.md` Stage 0 | ACTIVE |
| `HE_THONG_KichBan_v2` PHẦN C | Title creation | Topic | Title candidates | Built from 159 videos | Contains an unused "strongest mould" | ⛔ `CongThuc_Title_TrieuView`, ⛔ `BANDO_NgachTitle_Thang` | CANONICAL |
| `VERIFY_Title_V13/V14` | Title verification | Draft title | Verdict + swarm data | Concrete precedent | Only 2 of 19 videos have one | — | ACTIVE (example) |
| `TEARDOWN_PLAYBOOK_RaLenh_AI.md` | Competitor script teardown | Competitor transcript | ADN → rubric → score+fix | 3-step, copy-paste ready | Predates the raw corpus | `mo-xe-doi-thu` skill, `PROMPT_PACK_NotebookLM.md` | ACTIVE |
| `PROMPT_PACK_NotebookLM.md` (396 lines) | Bulk competitor digest | 49 competitor scripts | Structured reports | Large, tracked | NotebookLM mixes sources — 2 misattributions on record | `PLAYBOOK_NotebookLM_DoiThu.md`, `LENH_NotebookLM_ChuaLam.md` | ARCHIVE |
| `sketchapiens-viet-kich-ban` SKILL | Script writing | Title + anchors | Batched chapters | Per-chapter device checklist framed as diagnostic | 46 KB; overlaps predecessor | `viet-kich-ban-nguoi-que-co-dai` | CANONICAL |
| `LENH_GPT_ReviewKichBan_v3.md` round prompts (4, 5, 6) | Script critique by outside listener | Title + thumbnail description + plain EN script | 5–6 part critique | Round-specific targeting; forbids rewriting | Header rule contradicts its own tail; H1 says v2 | ⛔ `_BO_TRAIN_..._v2`, `Video17_Rain/_nhap/LENH_GPT_ReviewKichBan.md` (v1), `Video18_Sleep/LENH_GPT_ReviewKichBan_V18.md` | CANONICAL |
| `LENH_GPT_BoiCanh_TayNghe.md` paste block | Craft context prepended to review | — | — | Explicitly excludes 3 categories with reasons | Reverses a rule still stated elsewhere | Extract of `TRAIN_ChatGPT_TOANBO_DuAn.md` PHẦN 6+8 | ACTIVE |
| `chong-van-ai-narration-en` SKILL | Anti-AI editing | Finished narration | Same line count, de-AI'd | Doctor's oath: no fact/line-count change | Overlaps `TRAIN_ChatGPT_BuocPolish.md` | `TRAIN_ChatGPT_BuocPolish.md`, `TRAIN_ChatGPT_TOANBO` PHẦN 8 | ACTIVE |
| `sketchapiens-bien-tap/qa_kichban.py` | Machine QA | Narration file | 4 hard + 4 soft metrics | **Only deterministic checker in the project** | Cannot see structure (documented in `rubric_mu_loi_cau_truc.md`) | — | CANONICAL |
| `sketchapiens-giu-chan-nguoi-xem` SKILL | Retention editing | Draft | Retention notes | — | Overlaps shared skill | `giu-chan-nguoi-xem-nghe-ngu` | ACTIVE |
| `PROMPT_TONG_Thumbnail_v6.md` PHẦN E | Thumbnail ideation | Script + concept | Fill-in-the-blank prompt | Built from 29 ≥50K + 4 channel failures | — | ⛔ 3 dead thumbnail files | CANONICAL |
| `TEMPLATE_Thumbnail_KHOA_v1.md` | Thumbnail generation | 3 slots | Gen-ready prompt | Locked; 3 gates; change log | Filename v1 vs heading v2 | `TRAIN_ChatGPT_Thumbnail.md` | CANONICAL |
| Per-video `Thumbnail_Prompt*.txt` / `THUMBNAIL_prompts_v4/v5.txt` | Thumbnail generation, one video | — | — | Real precedent | V11–V13 keep 2–3 versions with no "current" marker | across 4 videos | GENERATED |
| `CastBible` / `BasePack01` / `Prompts_NhanVat_Kenh` / `CAST_REGEN_PROMPTS.txt` | Character consistency | — | Character sheets | Detailed | **4 files, one system, no precedence**; `@token` contradiction | each other | ACTIVE |
| `sketchapiens-chia-shot` SKILL PHẦN 2 | Shot splitting + image prompting | Narration | 2-column table | 6-block template; 4 blocks verbatim | 55 KB; `clean/smooth` conflict | `chia-shot-va-prompt-anh` | CANONICAL |
| Per-video `gen_prompts.py` / `build_prompts.py` / `shot_data.py` | Image prompt generation | Shot data | `PROMPTS_FULL.txt` | Reproducible | 14 forked copies, no shared library | each other | GENERATED |
| `SPEC_Tool_SinhAnh_Flow.md` | Bulk image generation | Prompt list | Images | — | Counter-based naming bug documented in memory | — | ACTIVE |
| `youtube-metadata` SKILL (6 refs) | Metadata | Script + title | Title variants, description, tags, chapters | 6-step workflow | Overlaps `youtube-seo` | `youtube-seo` (5 refs) | ACTIVE |
| `checklist-dang-video-long-form` SKILL | Publishing + mid-roll | Duration, chapter marks | Placement plan + checklist | Explicit RPM arithmetic | Assumes monetisation is on | `Video18_Sleep/DANG_V18.md` | ACTIVE |
| `chan-doan-kenh-youtube` SKILL | Analytics review | Impressions, CTR, AVD | Disease A/B/C + prescription | Sample-size math built in | Requires data the project does not store | — | ACTIVE |
| — | **Postmortem** | — | — | — | **No postmortem prompt exists.** Postmortem findings live only in memory files | — | **MISSING** |

---

## 7. Script Workflow Audit

### 7.1 Workflow as documented

`FLOW_VietKichBan_11Cong.md` + `WORKFLOW_Production.md` Stage 2 + `00_LUAT` mode table:

1. **Topic** — mode ① `sketchapiens-chon-de-tai`; gates 0–3; owner: user decides, Claude measures.
2. **Packaging first** — title at gate 1; thumbnail **concept** only (10 min, no image).
3. **Anchors** — gate 3, primary sources only, written to an anchor register.
4. **Gate A (anti-duplication)** — grep every candidate line against all previous videos **including `_nhap/`**, recursively.
5. **Write the ending first** (gate 5, bookend law).
6. **Write in batches, QA each chapter** before starting the next (gate 6).
7. **Machine QA** — `qa_kichban.py`, 4 hard constraints (gate 7).
8. **Policy QA** (gate 8).
9. **Anti-AI + read-aloud** (gate 9).
10. **Outside listener** — new chat each round, per-round targeting (gate 10). Mandatory when structure changes.
11. **Two final tests** (gate 11).

### 7.2 Workflow actually evidenced by files

| Step | Evidence found | Coverage |
|---|---|---|
| Topic research | `NGHIENCUU_V18_ChonDeTai_*.md`, `NGHIENCUU_V16_LaneCheck_*.md` | **2 of 19 videos** |
| Title verification | `VERIFY_Title_V13_*`, `VERIFY_Title_V14_*` | **2 of 19** |
| Anchor register | `NGHIENCUU_*_MoNeo` (V10–V12), `VERIFY_Anchors_*` (V15–V18, V17_Death), `MONEO_V19`, `V18_MO_NEO` | **9 of 19** |
| Batch drafts | `_nhap/Script_V17_DOT1–5`, `_nhap/DOT1–6` (V19), `Script_V19_DOT1–3` | **2 of 19** (V17, V19) |
| Outside-listener rounds | `Video17_Rain/_nhap/LENH_GPT_ReviewKichBan.md`, `Video18_Sleep/LENH_GPT_ReviewKichBan_V18.md`, `LENH_GPT_ReviewKichBan_v3.md` rounds 4–6, `_nhap/Script_V19_GhiChu.md` | **3 of 19** |
| Pre-round snapshots | `Script_V19_truoc_vong5.txt`, `Script_V19_truoc_vong6.txt`, `Script_v2_truoc_feedbackGPT.md` | **2 of 19** |
| Machine QA output | none stored — QA is run ad hoc, results only in conversation | **0 of 19** |
| Final narration | `Script_VideoNN_narration.txt` | **18 of 19** (V17_Death has only DOT1) |

### 7.3 Findings

- **The 11-gate flow is younger than 17 of the 19 videos.** It was created 2026-08-06. V01–V16 were produced under earlier, less documented processes. The flow is therefore aspirational for most of the archive and evidenced only from V17 onward.
- **No step in the flow writes a status file.** Gate completion exists only in `CHOT_V19.md` for V19 — one video has a gate table; none of the others do.
- **Overwrite risk is real and partially mitigated.** V19 keeps explicit pre-round snapshots (`_truoc_vong5`, `_truoc_vong6`). V01–V16 do not: `Script_VideoNN_narration.txt` is written in place with no version history, and no git.
- **Steps that exist only in instruction, with no file evidence anywhere:** machine-QA result storage; gate 11 ("two final tests") — no artefact for any video; postmortem — no file for any video.
- **`Video17_Death/`** contains `VERIFY_Anchors_V17_Death.md` + `Script_Video17_DOT1.md` and nothing else: an abandoned run whose index was reused.

---

## 8. Video Production Lifecycle

| # | Step | Input file(s) | Output file(s) | Tool | Decider | Checklist | Failure point | Standardised? |
|---|---|---|---|---|---|---|---|---|
| 1 | Idea | `BANG_CAU_TatCa_CuNo`, `BANDO_CumChuDe_CoCau` | — *(no idea file)* | nexlev, yt-dlp | User | Gate 0 | Ideas leave no artefact | **No** |
| 2 | Research | corpus, nexlev | `NGHIENCUU_*.md` | Claude, nexlev | Claude proposes | Gate 0 | Only 2/19 videos have one | **No** |
| 3 | Title | `HE_THONG_KichBan_v2` PHẦN C | `VERIFY_Title_*.md` | Claude | User | Gate 1 | Only 2/19 | **No** |
| 4 | Thumbnail concept | `PROMPT_TONG_Thumbnail_v6` | concept text in packaging file | Claude | User | Gate 1 (concept only) | Concept and image conflated before 04/08 | Partly |
| 5 | Script draft | title + anchors | `_nhap/DOT*.md` | Claude (Opus 5; Fable 5 for hook/ending) | Claude | Gates 5–6 | Batching only from V17 on | Partly |
| 6 | Script audit | draft | — *(no stored output)* | `qa_kichban.py` | Claude | Gate 7 | Results not persisted | **No** |
| 7 | Revision | GPT feedback | `Script_Vxx_GhiChu.md` | Claude | User pastes feedback | Gate 10 | Only V19 has a triage log | **No** |
| 8 | Fact verification | primary sources | `MONEO_*` / `VERIFY_Anchors_*` | Claude + WebFetch | Claude | Gate 3 | 5 naming schemes; post-gate additions bypassed it once | Partly |
| 9 | Shot splitting | narration | `SHOTLINES_FULL.txt` | `build_prompts.py` / skill | Claude | Gate 3 (stage) | — | **Yes** |
| 10 | Image prompts | shot data | `PROMPTS_FULL.txt` | `gen_prompts.py` / `shot_data.py` | Claude | — | 14 forked scripts | Partly |
| 11 | Image generation | prompts | `NNN.png` | Google Flow / Nano Banana | **User** | count files == prompts | Counter-drift bug; repair lists in 6 videos | **No** |
| 12 | Voice generation | `TTS_input_per_shot.txt` | `NNN.mp3` | ElevenLabs | Claude script | — | V12/V14/V15 have mp3 ≠ image counts | Partly |
| 13 | Editing / assembly | images + mp3 | `.mp4` | GhepVideo Studio (app) | **User** | Gate 4 | Memory: never hand-write the assembly script; V15 audio broke that way | Partly |
| 14 | Metadata | script | `Metadata_*.md` | `youtube-metadata` skill | Claude | 15-point checklist | Absent for V18, V19 | Partly |
| 15 | Publishing | metadata + mp4 | — | YouTube Studio | **User only** | `checklist-dang-video-long-form`, `DANG_V18.md` | **Claude is barred from the channel Gmail** | Partly |
| 16 | Analytics | Studio | — *(nothing stored in project)* | Studio screenshots, nexlev | User must supply | `chan-doan-kenh-youtube` | **No storage location exists** | **No** |
| 17 | Postmortem | analytics | — | — | — | — | **No artefact for any video** | **No** |
| 18 | Update project knowledge | findings | memory files, `00_LUAT`, skills | Claude | User approves | death register + banner rule | Half-applied twice (see §18) | Partly |

**Steps 16 and 17 are the broken link in the loop:** the project produces knowledge from *competitors* continuously, but has no mechanism to feed its **own** results back. All first-party numbers live in one memory file.


---

## 9. Current Video Projects

**19 video directories + 1 video with no directory (V01).** No file records publication status, upload date or YouTube URL for any of them. Titles below are taken from folder names, narration headers and metadata files — they are *working* titles, not verified published titles.

**Legend:** ✅ present · ➖ absent · ❓ unverified

| # | Slug | Narration | Anchors | Metadata | Thumb prompt | Images | mp3 | mp4 | Drafts kept | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | *(no folder)* Why Did Humans Lose Their Fur? | ✅ ×2 + 2 md | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | 5 in archive | **11 files loose at project root** |
| 02 | What_Animal_Hunted_Us | ✅ | ➖ | ✅ | ✅ | 372 | 0 | 0 | ➖ | mp3/mp4 absent — likely rendered elsewhere |
| 03 | Afraid_of_the_Dark | ✅ ×2 | ➖ | ✅ | ✅ | 342 | 1 | 1 | ➖ | Has `*-timestamps.json` (355 KB) |
| 04 | What_Did_Ancient_Humans_Do_All_Day | ✅ | ➖ | ➖ | ➖ | 0 | 0 | 0 | ➖ | **3 files only** — script + shotlines + prompts |
| 05 | Baby_Memory | ✅ | ➖ | ➖ | ✅ | 0 | 0 | 0 | ➖ | **4 files only** |
| 06 | Hypnic_Jerk | ✅ | ➖ | ✅ | ✅ | 155 | 155 | 1 | ➖ | counts match |
| 07 | Goosebumps | ✅ | ➖ | ✅ | ✅ | 109 | 109 | 1 | ➖ | counts match |
| 08 | Hiccup | ✅ | ➖ | ✅ | ✅ | 153 | 153 | 1 | ➖ | counts match |
| 09 | Teeth | ✅ ×2 | ➖ | ✅ | ✅ | 140 | 140 | 1 | ➖ | `Script_Video09_narration_FROMGEN.txt` is **md5-identical to `SHOTLINES_FULL.txt`** |
| 10 | Eyesight | ✅ | ✅ `NGHIENCUU_MatCan_Transcript.md` | ✅ | ✅ | 113 | 113 | 1 | ➖ | has `THIEU_111-113.txt` repair list |
| 11 | Back_Pain | ✅ | ✅ `NGHIENCUU_Lung_MoNeo.md` | ✅ | ✅ ×2 (v5) | 193 | 193 | 1 | ➖ | `PROMPTS_CLEAN` + `PROMPTS_FULL` near-duplicate |
| 12 | Feet | ✅ | ✅ `NGHIENCUU_BanChan_MoNeo.md` | ✅ | ✅ ×3 (v4, v5) | **265** | **255** | 1 | ➖ | **count mismatch**; repair file `PROMPTS_CON_THIEU_254_255.txt` |
| 13 | Stress | ✅ | ✅ `VERIFY_Title_V13_*` | ✅ | ✅ (v5) | 253 | 253 | 1 | ➖ | title-verification precedent |
| 14 | Milk | ✅ | ✅ `VERIFY_Title_V14_*` | ✅ | ✅ | **608** | **302** | **30** | ➖ | **large mismatch**; 30 mp4 suggests segment renders |
| 15 | Allergies | ✅ | ✅ `VERIFY_Anchors_V15_*` | ✅ | ➖ | **568** | **564** | 3 | ➖ | `V15_alignment.json` 432 KB; `2_assemble_video_FIXED.py` |
| 16 | Winter | ✅ | ✅ `VERIFY_Anchors_V16_*` | ✅ | ➖ | **0** | 185 | 2 | ➖ | **no images retained**; `CAN_GEN_LAI_17.txt` |
| 17a | **Death** | ➖ (DOT1 only) | ✅ `VERIFY_Anchors_V17_Death.md` | ➖ | ➖ | 0 | 0 | 0 | ✅ | **abandoned; index collides with 17b** |
| 17b | **Rain** | ✅ | ✅ `VERIFY_Anchors_V17_Rain.md` | ✅ `METADATA_V17.md` | ✅ (root `V17_PROMPT_THUMBNAIL.md`) | **1** | 263 | 3 | ✅ `_nhap/` ×8 | `Script_Video17_DUYET_EN-VI.md`; thumbnail jpeg present; **packaging file lives at project root** |
| 18 | Sleep | ✅ | ✅ `VERIFY_Anchors_V18.md` + **root `V18_MO_NEO.md`** | ➖ (in `_cu/`) | ✅ `PROMPT_THUMBNAIL.txt` | 229 | 224 | 1 | ✅ `_cu/` ×6 | `DANG_V18.md`; **contains `_V19_material_TwoSleeps.txt`** |
| 19 | NightWalk | ✅ | ✅ `MONEO_V19.md` | ➖ | ➖ (concept only, in `CHOT_V19.md`) | 0 | 0 | 0 | ✅ `_nhap/` ×11 | **only video with a gate table (`CHOT_V19.md`) and a review log** |

### Video: Video19_NightWalk *(the only in-progress video; most complete documentation)*

- **Current title:** "Why Couldn't Ancient Humans Just Hold It Until Morning?"
- **Previous titles:** "The Most Dangerous Thing Ancient Humans Did Every Single Night" (rejected round 2); "What Happened When Ancient Humans Left The Fire At Night?" (rejected round 4). Both retained with reasons in `CHOT_V19.md`.
- **Thumbnail text:** `TILL SUNRISE?` · **Concept:** wide shot, campfire centred, stickman caveman already mid-stride past the light edge. Recorded in `CHOT_V19.md` §⑦ with the reason the earlier "hesitating" pose was rejected.
- **Script versions:** `_nhap/Script_V19_ban_va_9luot.txt` → `_nhap/Script_V19_DOT1–3.md` → `_nhap/Script_V19_ban_2video.txt` → `_nhap/DOT1–6.md` → `Script_Video19_narration.txt`, with `_truoc_vong5.txt` and `_truoc_vong6.txt` snapshots.
- **Research/sources:** `MONEO_V19.md` (24 KB) — M1–M11 with primary-source citations; M5 marked DEAD; M3b/M4b added 2026-08-06.
- **Claim ledger:** yes — `MONEO_V19.md` is the most complete instance in the project, including a "KHOÁ M3b" block recording a fabrication caught in review.
- **Shot list / image prompts / assets / metadata / analytics:** none yet.
- **Status:** gate 10 passed (6 review rounds); gates 11 and production pending.
- **Missing:** metadata, shot list, images, audio.
- **Misplaced material belonging to V19:** `Video18_Sleep/_V19_material_TwoSleeps.txt`.
- **V20 material stored inside V19:** `_nhap/Script_V19_ban_2video.txt` and `_nhap/V19_EN_thuan_choGPT_v3.txt` (md5-identical pair) contain the predator half moved to a future V20; both carry warning banners.

### Files belonging to a video but stored outside its folder

| File | Belongs to | Currently at |
|---|---|---|
| `V17_PACKAGING_CHOT.md`, `V17_PROMPT_THUMBNAIL.md` | V17_Rain | project root |
| `V18_PACKAGING.md`, `V18_MO_NEO.md` | V18_Sleep | project root |
| `CONCEPT_Thumbnail_V16_V17.md` | V16 + V17 | project root |
| `NGHIENCUU_V18_ChonDeTai_2026-07-31.md`, `NGHIENCUU_V16_LaneCheck_2026-07-26.md` | V18, V16 | project root |
| 11 × `Script_Video01_*` / `IMG_PROMPTS_*` / `image_prompts_video01_*` / `CAST_REGEN_PROMPTS.txt` / `TEXT_Overlay_Goiy.txt` | V01 | project root (no V01 folder exists) |
| `_V19_material_TwoSleeps.txt` | V19 | `Video18_Sleep/` |

---

## 10. Script Version Map

**Canonical chain, per `FLOW_VietKichBan_11Cong.md`:**
`Idea → Research → Claude draft → Critique → Revised draft → Fact-checked draft → Final script → Published version`

| Video | Idea | Research | Draft | Critique | Revised | Fact-checked | Final | Published |
|---|---|---|---|---|---|---|---|---|
| V01 | ➖ | ➖ | `Script_Video01_Why-Did-Humans-Lose-Body-Hair.md`, `..._FINAL_MaxHai.md` | ➖ | ➖ | ➖ | **ambiguous** — `Script_Video01_FINAL.txt` *and* `Script_Video01_FINAL_deAI.txt` | ❓ |
| V02–V09 | ➖ | ➖ | ➖ | ➖ | ➖ | ➖ | `Script_VideoNN_narration.txt` | ❓ |
| V10–V12 | ➖ | ➖ | ➖ | ➖ | ➖ | `NGHIENCUU_*_MoNeo.md` | `Script_VideoNN_narration.txt` | ❓ |
| V13–V14 | ➖ | `VERIFY_Title_*` | ➖ | ➖ | ➖ | ➖ | `Script_VideoNN_narration.txt` | ❓ |
| V15–V16 | ➖ | ➖ | ➖ | ➖ | ➖ | `VERIFY_Anchors_*` | `Script_VideoNN_narration.txt` | ❓ |
| V17_Rain | ➖ | ➖ | `_nhap/Script_V17_DOT1–5.md`, `_nhap/Script_V17_FULL_v2.md` | `_nhap/LENH_GPT_ReviewKichBan.md` + `_nhap/Script_v2_truoc_feedbackGPT.md` | ✅ *(implied)* | `VERIFY_Anchors_V17_Rain.md` | `Script_Video17_narration.txt` | ❓ |
| V17_Death | ➖ | ➖ | `Script_Video17_DOT1.md` | ➖ | ➖ | `VERIFY_Anchors_V17_Death.md` | **none — abandoned** | ➖ |
| V18 | `NGHIENCUU_V18_ChonDeTai_*.md` | ✅ | `_ch3_backup.txt` *(partial)* | `LENH_GPT_ReviewKichBan_V18.md` | ➖ | `VERIFY_Anchors_V18.md` + `V18_MO_NEO.md` | `Script_Video18_narration.txt` | ❓ |
| V19 | `CHOT_V19.md` | `MONEO_V19.md` | `_nhap/DOT1–6.md` | rounds 4–6 in `LENH_GPT_ReviewKichBan_v3.md`; log in `_nhap/Script_V19_GhiChu.md` | `_truoc_vong5.txt`, `_truoc_vong6.txt` | `MONEO_V19.md` | `Script_Video19_narration.txt` | ➖ not yet |

### Findings

- **Missing everywhere:** the "Published version" column. No file in the project stores what was actually uploaded, so a published video cannot be diffed against its local script.
- **Two candidate finals, neither marked:** V01 has `Script_Video01_FINAL.txt` and `Script_Video01_FINAL_deAI.txt`. The de-AI'd one is later and matches the documented process, but nothing in either file says which was used. `Script_Video01_FINAL.txt` is **md5-identical to an archived file**, suggesting it is the pre-polish version.
- **Critique without a recorded revision:** V18 has `LENH_GPT_ReviewKichBan_V18.md` (the critique prompt) but **no stored feedback and no post-critique snapshot**. Whether the feedback was applied cannot be determined from files.
- **Overwrite confirmed by absence:** V02–V16 keep exactly one narration file each with no drafts and no snapshots. Any revision overwrote its predecessor irrecoverably (no git).
- **Only V19 has a complete chain** with pre-round snapshots and a triage log.
- **`Video09_Teeth`** has two narration files that are byte-identical to `SHOTLINES_FULL.txt` — a filename collision, not two versions.


---

## 11. Research and Evidence Audit

### 11.1 Where evidence lives

| Kind | Location | Coverage |
|---|---|---|
| Science anchors per video | `MONEO_V19.md`, `VERIFY_Anchors_V15/16/17/18/17_Death.md`, `NGHIENCUU_*_MoNeo.md` (V10–V12), `V18_MO_NEO.md` | 9 of 19 videos |
| Title/topic evidence | `VERIFY_Title_V13/V14`, `NGHIENCUU_V16/V18_*` | 4 of 19 |
| Niche-level evidence | `BANG_CAU_TatCa_CuNo`, `BANDO_CumChuDe_CoCau`, `NGHIENCUU_CloneSwarm`, `NGHIENCUU_ThiNghiem_BaySinhDoi`, `BOCTACH_*` (3), `CO_CHE_3LOP_Winner` | project-wide |
| Competitor primary text | `2_KHO_BANGHI/` — **768 transcripts, 22 channels**; `DICH_Zenn_7.8M_*.md` | project-wide |
| Competitor imagery | `NGHIENCUU_Thumbnail_50K/` (31 jpg + `list.tsv`), `competitor_frames_predators/` (57 jpg) | project-wide |
| Channel metrics | nexlev MCP responses, transcribed into `2_KHO_BANGHI/00_KHO.md` | 22 channels |
| First-party analytics | **memory only** (`chan_doan_kenh_benh_A.md`) | 3 videos, partial |

### 11.2 Is each claim tied to a source?

**Within anchor registers: yes, and unusually strictly.** `MONEO_V19.md` records journal, volume, page, sample size and exact figure — e.g. Huang et al., *BMC Pediatrics* 2020;20:305, n=6568, 9.09% boys / 6.03% girls at age 5; Dejene et al., *IJBC* 8(1):1–7, 24 attacks, 98% at night, 18 male / 6 female, 12 killed 2010–2012, 58.3% (n=7) children under 12.

**Outside anchor registers: frequently not.** Strategy files quote numbers (median views, top-1 share, breakout counts, "text 22%", "brightness 80–110") without a retrievable source, and several were later measured wrong (§1).

### 11.3 Does the project distinguish evidence / inference / speculation / story device?

**Partly, and only in the newest files.**

- ✅ **Explicit** in `MONEO_V19.md`: M3b carries *"⚠️ Đây là suy diễn của tác giả, không phải số đo → trong kịch bản phải ghi 'the researchers put that down to…', cấm nói như sự thật."*
- ✅ **Explicit** in `00_LUAT` precedence rule 2: hand-counted transcript beats any report.
- ✅ **Explicit** in `CONGTHUC_InkExplainer_BestOf.md`: a labelled correction block.
- ➖ **Absent** in most Tier-3 research files: no confidence labels, no evidence-vs-inference tagging.
- ➖ **No project-wide confidence vocabulary** exists.

### 11.4 Modern sources used to infer about prehistory

**Yes, and the project is aware of it.** V19's entire argument rests on modern data — Xi'an children (2020), 270 pregnant women (2014), StatPearls over-65 nocturia, and a 2013 Ethiopian hyena study — applied to 50,000 years ago. The script itself states the limit: *"Nobody knows how well a fire actually worked… You cannot rerun the Stone Age."* Review round 6 flagged the remaining gap: *"Haramaya is not the Stone Age with roads added."*

This is the project's single largest recurring evidential risk, and it is currently managed by prose hedging rather than by a structured inference ladder.

### 11.5 Claims without a source

Not exhaustively verifiable in a read-only pass, but two categories are visible:
- Strategy numbers in Tier-3 files with no citation (see 11.2).
- **`VAULT_AncientHumans_KnowledgeVault.md` is 873 bytes / 15 lines** while `00_LUAT` describes it as holding *"8 chủ đề + mỏ neo, bóc từ 49 kịch bản đối thủ"*. Either the vault is a stub, was truncated, or the description is wrong. **Unknown — cannot be resolved from files.**

### 11.6 Sources not linked to any script

`2_KHO_BANGHI/` (768 transcripts) and `NGHIENCUU_Thumbnail_50K/` (31 thumbnails) have no mapping to the videos they informed. `competitor_frames_predators/` (57 frames) has no index. `DICH_Zenn_7.8M_*.md` is named as mandatory gate-A reading but nothing records which videos were checked against it.

### 11.7 Duplicated evidence across directories

- The Zenn 7.8M video exists twice: as a Vietnamese translation (`DICH_Zenn_7.8M_*.md`) and as a raw transcript (`2_KHO_BANGHI/Zenn/…at_Night.txt`).
- Competitor teardowns overlap four ways: `MoXe_15Khoi_*`, `MoXe_KichBan_Viral_3Video`, `TearDown_7M_*`, `TearDown_Video_Predators` — all covering the same small set of competitor videos.
- The same channel appears under two names: `NGHIENCUU_2Kenh_ThinkMan_BrightPsycho` calls `UCdRKykJ9kiBGJ9FCVFZ41Mg` "ThinkMan"; the corpus calls it "CertifiedThought".

---

## 12. Thumbnail and Visual System Audit

### 12.1 Channel-wide rules *(current)*

**Source:** `PROMPT_TONG_Thumbnail_v6.md` (2026-08-05), `TEMPLATE_Thumbnail_KHOA_v1.md` (2026-08-05), `sketchapiens-thumbnail` skill.

- **Thumbnail DNA:** CENTRE ANCHOR — the frame's centre belongs to the storytelling **object**, not the character (LUẬT 1).
- **Text rules:** text must add new information, never repeat the title (LUẬT 2); yellow, black-outlined, top edge; must contain a measurable quantity (05/08 rule, from 44 thumbnails / 9 channels). Strongest form: *title asks → thumbnail answers*.
- **Character placement:** faces/hands/feet must be **solid white, 3–6% of frame** (memory `gotcha_do_tong_thumbnail_vo_nghia.md`, from V18 bản 2 measuring 0.3%).
- **Colour:** dull background + 1–2 saturated points (LUẬT 3).
- **Gaze:** all eyes lock inward (LUẬT 4).
- **Expression:** never the same emotion on every face (LUẬT 5).
- **Layout rotation:** 7 layouts, never repeat two videos running (PHẦN C).
- **Banned prompt words:** `cartoon` · `clean` · `smooth`.
- **Mobile readability:** not found as an explicit rule in any thumbnail file. **Gap.**
- **Click mechanisms:** PHẦN D "phép thử nhiệt độ" (temperature test) for word choice.
- **Truthfulness ladder:** not found. The closest constraint is the YouTube inauthentic-content test in `CHINHSACH_YOUTUBE_2026_AnhHuong.md`. **Gap.**

### 12.2 Rules that were overruled *(retained, marked)*

| Dead rule | Where | Overruled by |
|---|---|---|
| "character left ↔ object right" DNA | ⛔ `_KHO_LUU_DaChet/TEMPLATE_Thumbnail_DoiThu.md` | CENTRE ANCHOR (v6) |
| "caveman left ↔ modern stickman right" | ⛔ `_KHO_LUU_DaChet/HE_THONG_Thumbnail_Signature_v3.md` | v6 forbids it |
| whole v5 script-to-packaging system | ⛔ `_KHO_LUU_DaChet/HE_THONG_Thumbnail_v5_*.md` | v6 |
| "brightness 80–110" | memory `gotcha_do_tong_thumbnail_vo_nghia.md` | correlation with views ≈ 0 |
| "text 13–19% of frame" | same | actually 22%; the 13–19% figure was self-inflicted on 29/07 |
| "night scenes must still be bright" | `TEMPLATE_Thumbnail_KHOA_v1.md` §Ô 3 | refuted 05/08 |

### 12.3 One-video-only material *(not channel rules)*

`CONCEPT_Thumbnail_V16_V17.md`, `V17_PROMPT_THUMBNAIL.md`, `Video18_Sleep/PROMPT_THUMBNAIL.txt`, per-video `Thumbnail_Prompt*.txt` and `THUMBNAIL_prompts_v4/v5.txt` (V11, V12, V13), and the V19 concept inside `CHOT_V19.md` §⑦.

### 12.4 Temporary feedback recorded as durable rules

Memory `feedback_dung_them_luat_khi_model_dang_dung.md` records that during 7 rounds on V18, *"2 lỗi nặng nhất đều là luật tôi tự thêm"* — rules invented mid-session became persistent constraints and degraded output. `TEMPLATE_Thumbnail_KHOA_v1.md` now carries this as its most important rule.

### 12.5 Approved / rejected examples and test records

- **Approved example asset:** `Video17_Rain/THUMBNAIL_V17_ROTTING_FINAL.jpeg` (178 KB) — the only finished thumbnail image stored in the project.
- **Competitor reference set:** `NGHIENCUU_Thumbnail_50K/` — 31 jpgs named `NN_<views>_<videoId>.jpg` plus `list.tsv`. Well-named and traceable.
- **Frame study:** `competitor_frames_predators/` — 57 extracted frames, `f_NNNNN.jpg`, **no index, no source video recorded in the folder**.
- **Style refs:** `REF_Style/` — 3 PNGs with descriptive Vietnamese names.
- **Thumbnail A/B test records:** none found.
- **CTR results:** only in memory (`chan_doan_kenh_benh_A.md`: 3.5% on 367 impressions / 13 clicks, and a user statement that two lanes reached 3.5%). **No per-thumbnail CTR file exists.**

### 12.6 Visual-system conflicts

Documented in §17: `ArtBible_NguoiQueCoDai.md` and both shot-splitting skills specify `clean`/`smooth` line quality; `TEMPLATE_Thumbnail_KHOA_v1.md` and memory `gotcha_style_doodle_khong_hoathinh.md` ban those exact words.

---

## 13. Character and Asset Inventory

### 13.1 Character definition files

| File | Contents | Note |
|---|---|---|
| `CastBible_DienVien.md` | Design DNA, base + costume presets, token registry, guest library, re-skin for other channels | Defines `@TOKEN` scheme |
| `BasePack01_Sketchapiens.md` | 12 sheets to generate: `01_base` … `12_prop_sheet`, each with a token | Most concrete |
| `Prompts_NhanVat_Kenh.md` | Character prompt set v3, "NGƯỜI QUE THÔ" | Third description of the same cast |
| `SOP_NhatQuan_NhanVat.md` | Consistency SOP for Nano Banana / Flow, labelled "Part 2" | Process, not definition |
| `CAST_REGEN_PROMPTS.txt` | Regeneration prompts | Fourth overlapping file |
| `sketchapiens-chia-shot` / `chia-shot-va-prompt-anh` PHẦN 3 | Character blocks pasted verbatim into every prompt | **Rejects the token scheme** |

### 13.2 Characters defined vs. reference sheets on disk

| Character | Token | Defined in | Model sheet found on disk? |
|---|---|---|---|
| Modern man ("you") | `@MODERNYOU` | BasePack01 §5, CastBible, shot skill | ➖ **not found** |
| Caveman / ancestor | `@ANCESTOR` | BasePack01 §6 | ➖ not found |
| Forager | `@FORAGER` | BasePack01 §7 | ➖ not found |
| Child | `@CHILD` | BasePack01 §8 | ➖ not found |
| Elder | `@ELDER` | BasePack01 §9 | ➖ not found |
| Scientist | `@SCIENTIST` | BasePack01 §10 | ➖ not found |
| Chimp | `@CHIMP` | BasePack01 §11 | ➖ not found |
| **Woman / female ancestor** | — | shot skill PHẦN 3 (prose only) | ➖ **no token, no sheet** |
| Animals (leopard, crocodile, lion, bear, eagle) | — | shot skill PHẦN 3 (prose) | ➖ no sheets |
| Base skeleton / turnaround / expression / pose sheets (`01`–`04`) | — | BasePack01 §1–4 | ➖ **none found** |

> **Finding:** the project specifies 12 character/prop reference sheets and a token registry, but **no `01_base.png` … `12_prop_sheet.png` exists anywhere in the project.** Consistency is achieved instead by repeating text blocks — which is what the shot skill prescribes. The BasePack/CastBible token system therefore appears **specified but never built**. *(Inference from absence, not from a statement in any file.)*

### 13.3 Other assets

| Asset group | Location | Count | Naming quality | Issue |
|---|---|---|---|---|
| Video frame images | `VideoNN_*/` | 3,087 png total | `NNN.png` sequential | V16 has none; V17_Rain has 1 |
| Audio | `VideoNN_*/` | 2,910 mp3 | per-shot | mismatch with image count in V12/V14/V15 |
| Rendered video | `VideoNN_*/` | 49 mp4 | mixed | V14 has 30 — segments, purpose unrecorded |
| Competitor thumbnails | `NGHIENCUU_Thumbnail_50K/` | 31 jpg + `list.tsv` | `NN_<views>_<videoId>.jpg` — **best naming in the project** | — |
| Competitor frames | `competitor_frames_predators/` | 57 jpg | `f_NNNNN.jpg` | **no source video recorded** |
| Style references | `REF_Style/` | 3 png | descriptive | — |
| Channel thumbnail (finished) | `Video17_Rain/` | 1 jpeg | `THUMBNAIL_V17_ROTTING_FINAL.jpeg` | only finished thumbnail stored |
| Logo / banner | — | **0** | — | prompts exist in `Brand_Kit_Kenh.md` §3–4; **no image files found** |
| Fonts / text-style refs | — | **0** | — | none found *(none exported, per instruction)* |

**Ambiguous filenames:** `_fix_concat.txt`, `_ch3_backup.txt`, `THIEU_337-370.txt`, `CAN_GEN_LAI_17.txt`, `PROMPTS_145_SUALAI.txt`, `f_NNNNN.jpg` — none state which run or video state they belong to.


---

## 14. Analytics and Feedback Audit

**There is no analytics file anywhere in the project directory.** No CSV, no Studio export, no per-video metrics file, no retention graph, no comment archive. Every first-party number found during this audit lives in **one memory file** (`~/.claude/projects/-Users-admin-Desktop/memory/chan_doan_kenh_benh_A.md`) or in conversation history.

| Video | Title | Thumbnail | CTR | 30s retention | AVD / APV | Main drop points | Lessons recorded | Missing data |
|---|---|---|---|---|---|---|---|---|
| V17_Rain | *(working)* How ancient humans survived being wet | `THUMBNAIL_V17_ROTTING_FINAL.jpeg`, text `ROTTING?` | **3.5%** on 367 impressions / **13 clicks** — CI [1.6%, 5.4%] | not recorded | **55.6%** measured on **12 unique viewers** — CI [27.5%, 83.7%] | not recorded | ✅ `chan_doan_kenh_benh_A.md`: *"Đừng lấy V17 làm chuẩn cho bất cứ thứ gì"* | impressions over time, traffic source, retention graph, comments |
| V18_Sleep | How Did Ancient Humans Sleep in the Open? | concept in `PROMPT_THUMBNAIL.txt` | **3.5%** *(user-reported, unverified)* | ➖ | ➖ | ➖ | ➖ | everything |
| "băng hà" / "chân ướt" lanes | — | — | **3.5%** *(user-reported)* | ➖ | ➖ | ➖ | ➖ | everything |
| All other videos (V01–V16, V19) | — | — | ➖ | ➖ | ➖ | ➖ | ➖ | **all metrics** |

**Channel-level, from the same memory file:**
- 367 impressions in 5 days on the newest video — against a disease-A threshold of 5,000 impressions in 2 weeks → *"bệnh A là CHẮC"* (not being distributed).
- ~85% of traffic from browse + suggested → YouTube **is** testing but not expanding.
- Combined CTR across 2 videos: 3.5%, CI [2.2%, 4.8%].
- Channel totals cited in session: ~531 views, 7 subscribers, 13 public videos.

**Assessment of the analytics system:**
- ❌ No storage location, no schema, no naming convention for analytics.
- ❌ No mechanism carries a retention drop back to a script timestamp.
- ❌ No postmortem artefact exists for any video.
- ❌ No comment research file exists for the project's own videos.
- ✅ The **interpretation** discipline is strong: `chan-doan-kenh-youtube` skill embeds sample-size mathematics (`P(0 hits after N) = (1−p)^N`) and the memory file explicitly refuses to draw conclusions from 12–13 observations.
- ⚠️ Blocking constraint: YouTube Analytics API does not expose impressions or CTR — those are Studio-only, so screenshots are unavoidable, and Claude is barred from the channel account (memory `browser_chrome_cuong_only.md`).

---

## 15. Competitor Knowledge Audit

### 15.1 Channels tracked

**22 channels with raw transcripts** (`2_KHO_BANGHI/`), classified on two independent axes:

| Drawn-format channels (craft is transferable) | Transcripts | RPM | Avg views | Avg length | Top country |
|---|---|---|---|---|---|
| Mogo | 31 | 7.66 | 28,398 | 23.5' | — |
| Stickly (`@SticklyExplains`) | 43 | 7.06 | 106,655 | 23.1' | — |
| PrimalGlitch | 13 | 6.48 | 43,246 | 9.5' | India |
| **Mack** (`@MackExplains7`) | 52 | 5.90 | 160,712 | 23.8' | — |
| Simply A Stickman | 47 | 5.80 | 6,989 | 11.6' | US |
| Before Civilization | 65 | 5.48 | 21,919 | 29.6' | US |
| Myrk | 17 | 5.29 | 25,934 | 12.7' | US |
| Zenn | 28 | 5.09 | 588,442 | 8.6' | US |
| Mr. Hell | 10 | 4.52 | 44,013 | 8.0' | US |
| CertifiedThought | 11 | 4.37 | 52,780 | 14.7' | US |
| Bright-Psycho | 96 | 4.21 | 12,568 | 9.4' | US |
| Rune | 13 | 4.11 | 11,002 | 10.1' | — |
| Axen | 12 | 4.09 | 442,354 | 8.3' | US |
| Ink Explainer | 12 | 3.64 | 374,022 | 8.7' | — |
| Paint It Simple | 7 | 3.29 | 340,235 | 8.9' | — |
| Super Joy Animations | 9 | 3.07 | 586,888 | 8.1' | **Pakistan** |

| Documentary-format (topic reference only) | Transcripts | RPM | Avg views |
|---|---|---|---|
| ExtinctZoo | 0 *(not pulled)* | 8.80 | 2,086,877 |
| Historical Architect | 0 *(not pulled)* | 7.93 | 216,467 |
| A Day In History | 134 | 4.87 | 598,646 |
| The Paint Explainer | 139 | 4.80 | 1,871,021 |
| Before Fire | 27 | 3.71 | 79,838 |
| Barely Evolved | 2 *(incomplete)* | 2.73 | 3,543,289 | **Croatia** |

All 22 are monetised. One channel found during discovery — `MACK STICKLY` (`UCnWSzpTUhqjBeZg4MWF4q7w`) — is **demonetised**, avg 15 views, and was excluded as a name-squatting imitator.

### 15.2 Competitor scripts held

- **768 full transcripts** in `2_KHO_BANGHI/`, `en-orig` captions, plus 1,265 raw `.vtt` and matching `.info.json`.
- **1 full Vietnamese translation**: `DICH_Zenn_7.8M_WhatDidAncientHumansDoAtNight.md`.
- **49 competitor scripts** referenced as the basis of `VAULT_AncientHumans_KnowledgeVault.md` — **the 49 source texts themselves are not in the project.**

### 15.3 Thumbnail and frame references

`NGHIENCUU_Thumbnail_50K/` (31 jpg + `list.tsv`, filenames carry view count and video ID) · `competitor_frames_predators/` (57 frames, no index) · `NGHIENCUU_15Thumbnail_Mack.md` (analysis).

### 15.4 Comment research

`WORKFLOW_Production.md` §0.1 records the method as **tried and abandoned**: *"~~Tìm cầu — quét bình luận đối thủ~~ ⚠️ ĐÃ THỬ, KHÔNG HIỆU QUẢ."* The one comment finding that survived is the AI-writing complaint (4,400 likes) cited in three files.

### 15.5 Lessons already extracted

- Top-1/top-2 share separates "has a formula" from "won the lottery" (`BOCTACH_4Kenh_SoSanh`, superseded by `BOCTACH_16Kenh`).
- Ink Explainer's 5-step best-of formula; anchors reusable, thesis/beat-order/jokes not (`CONGTHUC_InkExplainer_BestOf.md`).
- Length is a **trade-off, not a quality**: across 12 drawn channels, length↔RPM rho **+0.67**, length↔views rho **−0.53**; within channels rho ≈ 0 with conflicting signs (`2_KHO_BANGHI/00_KHO.md`).
- Clone swarms make title choice near-irrelevant (`NGHIENCUU_CloneSwarm`, memory `insight_clone_swarm.md`).
- Two competitor channels sell the same course → possible business alliance; case left open in `00_LUAT` as *"chưa đủ dữ liệu"*.

### 15.6 Copy-proximity risk

| Risk | Evidence | Mitigation on record |
|---|---|---|
| **Reused-content policy** — the user's previous Shorts channel was taken down for it | user statement; `CONGTHUC_InkExplainer_BestOf.md` | Boundary table: anchors reusable, thesis/beat-order/jokes/metaphors/footage not |
| **Corpus contamination during writing** | 768 competitor scripts now on disk | `00_KHO.md`: *"Kho này chỉ để ĐO. Cấm mở trong chế độ ② VIẾT."* — a rule, not an enforced control |
| **Generic-channel test** | `00_LUAT` 05/08 entry; V18's hook shown to match the swarm | Gate-1 rule: each video needs ≥1 thing the other 20 channels lack |
| **`NganHang_ReHook` PHẦN B** holds verbatim competitor sentences | file itself | Marked *"❌ KHÔNG copy — chỉ học pattern"*; deliberately excluded from the GPT context block |

### 15.7 Unsourced competitor material

`MoXe_15Khoi_KichBan_DoiThu.md`, `MoXe_KichBan_Viral_3Video.md`, `TearDown_7M_CongThuc_GuongSoi.md`, `TearDown_Video_Predators.md` analyse competitor videos **without recording which video IDs** they analysed. `competitor_frames_predators/` likewise. `VAULT_AncientHumans_KnowledgeVault.md` cites "49 scripts" that are not in the repo.

---

## 16. Duplicate Content Audit

| Group | Files involved | Type | Likely canonical | Confidence | Risk |
|---|---|---|---|---|---|
| **G1 · V01 script set** | `Script_Video01_FINAL.txt`, `Script_Video01_FINAL_deAI.txt`, `Script_Video01_FINAL_MaxHai.md`, `Script_Video01_Why-Did-Humans-Lose-Body-Hair.md`, `_KHO_LUU_DaChet/Script_Video01_{FINAL_BACKUP, FINAL_35min_BACKUP, FINAL_OLD35_BACKUP2, PART1, v2_skill}.txt` | 9 files, 3 named "FINAL"; `FINAL.txt` **md5-identical** to `_KHO_LUU_DaChet/..._v2_skill.txt` | `Script_Video01_FINAL_deAI.txt` *(latest + matches documented process)* | MEDIUM | HIGH — wrong version could be used |
| **G2 · shotline triplicates** | `SHOTLINES_FULL.txt` ≡ `build/TTS_input_per_shot.txt` in V14, V15, V16, V17, V18 (md5-verified) | exact duplicate ×2 per video | `SHOTLINES_FULL.txt` | HIGH | LOW — regenerable |
| **G3 · V09 narration** | `Script_Video09_narration.txt`, `Script_Video09_narration_FROMGEN.txt`, `SHOTLINES_FULL.txt` — the latter two md5-identical | naming collision | `Script_Video09_narration.txt` | MEDIUM | MEDIUM |
| **G4 · V19 two-video draft** | `_nhap/Script_V19_ban_2video.txt` ≡ `_nhap/V19_EN_thuan_choGPT_v3.txt` (md5) | exact duplicate | either — both banner-marked | HIGH | LOW *(handled)* |
| **G5 · PROMPTS_CLEAN vs FULL** | V11 (186/187 KB), V12 (325/326 KB) | near-duplicate | `PROMPTS_FULL.txt` | LOW | MEDIUM — unclear which was generated from |
| **G6 · review-prompt lineage** | `Video17_Rain/_nhap/LENH_GPT_ReviewKichBan.md` (v1) · `_BO_TRAIN_ChatGPT_ReviewKichBan_v2.md` · `LENH_GPT_ReviewKichBan_v3.md` · `Video18_Sleep/LENH_GPT_ReviewKichBan_V18.md` | 4 versions of one prompt | `LENH_GPT_ReviewKichBan_v3.md` | HIGH | MEDIUM — v3's own H1 still says "v2" |
| **G7 · character system** | `CastBible_DienVien.md` · `BasePack01_Sketchapiens.md` · `Prompts_NhanVat_Kenh.md` · `SOP_NhatQuan_NhanVat.md` · `CAST_REGEN_PROMPTS.txt` · both shot skills | 6 overlapping definitions, no precedence | **undetermined** | LOW | **HIGH** — includes an unresolved `@token` contradiction |
| **G8 · competitor teardowns** | `MoXe_15Khoi_*` · `MoXe_KichBan_Viral_3Video` · `TearDown_7M_*` · `TearDown_Video_Predators` · `TEARDOWN_PLAYBOOK_RaLenh_AI` | same competitor set, 5 angles | none declared | LOW | MEDIUM |
| **G9 · thumbnail systems** | `PROMPT_TONG_Thumbnail_v6` · `TEMPLATE_Thumbnail_KHOA_v1` · `TRAIN_ChatGPT_Thumbnail` · `ArtBible` §6 · `sketchapiens-thumbnail` · `thiet-ke-thumbnail` · 3 dead files | 7 live + 3 dead | v6 + KHOA_v1 | HIGH | MEDIUM |
| **G10 · NotebookLM instruction** | `PROMPT_PACK_NotebookLM` · `PLAYBOOK_NotebookLM_DoiThu` · `LENH_NotebookLM_ChuaLam` · `BAY_SinhDoi_DanhSach` | 4 overlapping | `LENH_NotebookLM_ChuaLam` *(per `00_LUAT`)* | MEDIUM | LOW |
| **G11 · channel teardowns** | `BOCTACH_16Kenh_2026-08-05` · `BOCTACH_4Kenh_SoSanh_2026-08-04` · `BOCTACH_BeforeCivilization_2026-08-04` · now `2_KHO_BANGHI/00_KHO.md` | 4 generations | `2_KHO_BANGHI/00_KHO.md` *(measured, not reported)* | MEDIUM | **HIGH** — the 4Kenh file's "median 18,500" is measurably wrong and carries no ⛔ banner |
| **G12 · visual grammar** | `NGHIENCUU_NguPhapHinh_InkExplainer.md` · `NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md` | same topic, same date | the "DoLai" (remeasured) one | LOW | MEDIUM |
| **G13 · skill predecessors** | `viet-kich-ban-nguoi-que-co-dai` ↔ `sketchapiens-viet-kich-ban` · `chia-shot-va-prompt-anh` ↔ `sketchapiens-chia-shot` · `thiet-ke-thumbnail` ↔ `sketchapiens-thumbnail` · `giu-chan-nguoi-xem-nghe-ngu` ↔ `sketchapiens-giu-chan-nguoi-xem` | 4 pairs, both live | the `sketchapiens-*` ones | MEDIUM | **CRITICAL** — the unprefixed ones auto-trigger and reference dead files |
| **G14 · V18 packaging** | root `V18_PACKAGING.md` · root `V18_MO_NEO.md` · `Video18_Sleep/DANG_V18.md` · `Video18_Sleep/_cu/{METADATA_V18, CHECKLIST_DANG_V18, MOTA_VIDEO_V18}.md` | 6 files, 3 locations | `DANG_V18.md` + root `V18_PACKAGING.md` | LOW | MEDIUM |
| **G15 · per-video build scripts** | `tts_stdlib.py` ×5, `2_assemble_video.py` ×5 (+1 `_FIXED`), `run_pipeline.py` ×6, `gen_prompts.py` ×6, `build_prompts.py` ×4, `shot_data.py` ×4 | forked copies | none — no shared library | HIGH | MEDIUM — a fix in one does not propagate |
| **G16 · in-project skill copy** | `skills_build/chong-van-ai-narration-en/SKILL.md` vs `~/.claude/skills/chong-van-ai-narration-en/SKILL.md` | possible fork | the global one *(it is the one that loads)* | LOW | LOW |

**Files with version-suffix names:** `Script_Video01_FINAL*.txt` (3), `THUMBNAIL_prompts_v4/_v5.txt` (V11/V12/V13), `_BO_TRAIN_*_v2.md`, `LENH_GPT_ReviewKichBan_v3.md`, `Script_V19_truoc_vong5/6.txt`, `V19_EN_thuan_choGPT{,_v2,_v3}.txt`, `Script_V17_FULL_v2.md`, `2_assemble_video_FIXED.py`, `TEMPLATE_Thumbnail_KHOA_v1.md` *(heading says v2)*, `HE_THONG_KichBan_v2_14Video.md`, `PROMPT_TONG_Thumbnail_v6.md`, `ArtBible … v2`, `CastBible … v2`, `Prompts_NhanVat … v3`.


---

## 17. Contradiction Audit

*Reported only. No rule is chosen over another.*

| # | Rule A | Source A | Rule B | Source B | Possible reason | Which appears newer | Resolution |
|---|---|---|---|---|---|---|---|
| C1 | *"KHÔNG dán luật kênh, không dán rubric, không dán bối cảnh ngách vào GPT"* | `LENH_GPT_ReviewKichBan_v3.md`, header block | *"Luật 'cấm dán bối cảnh' ở đầu file này SAI. Đã đảo."* + `LENH_GPT_BoiCanh_TayNghe.md` | same file, tail section (2026-08-06) | A controlled test on 2026-08-06 reversed the rule; the header was never updated | **B** (dated) | **DO NOT RESOLVE** |
| C2 | Consistency via `@TOKEN` registry (`@MODERNYOU`, `@ANCESTOR`, …) | `CastBible_DienVien.md` §4, `BasePack01_Sketchapiens.md` | *"Không cast-token… không @token, không 'same as before'"*; consistency by repeating text | `sketchapiens-chia-shot`, `chia-shot-va-prompt-anh` PHẦN 0 | Token approach specified Jun 2026, never built; text-repetition adopted in practice | **B** (skills modified 2026-08-06) | **DO NOT RESOLVE** |
| C3 | `clean` / `smooth` / `cartoon` are required style words: *"Clean flat 2D cartoon explainer with smooth, even… outlines"* | both shot skills, STYLE anchor; `ArtBible` §1 | *"⛔ BA CHỮ CẤM TUYỆT ĐỐI: `cartoon` · `clean` · `smooth`"* | `TEMPLATE_Thumbnail_KHOA_v1.md`; memory `gotcha_style_doodle_khong_hoathinh.md` | The banned-words rule was derived from thumbnails; unclear whether it was meant to extend to video frames | **B** (2026-08-03/05) | **DO NOT RESOLVE** — scope ambiguity |
| C4 | *"đối thủ mới vẽ SẠCH DIGITAL, không run tay"* | `chia-shot-va-prompt-anh` PHẦN 2, PHẦN 6 (07/2026) | *"ghi chép 'đối thủ vẽ sạch digital' 07/2026 là SAI, khung 4K cho thấy run tay + màu xỉn"* | memory `gotcha_style_doodle_khong_hoathinh.md` | Later 4K frame inspection refuted the earlier observation | **B** | **DO NOT RESOLVE** |
| C5 | Video length 20–25 minutes | `RUBRIC_KichBan.md` Tier A *(as recorded in memory `feedback_so_do_khong_phai_dich`)* | Ink Explainer's 1M video is 11:37 and its 769K is 6:04; niche median 10.2' | `CONGTHUC_InkExplainer_BestOf.md`; `CHOT_V19.md` §② | Tier A was distilled from Mack/Stickly (23' channels) | **B** | **DO NOT RESOLVE** |
| C6 | Length is not a lever: within-channel length↔views rho ≈ 0, signs conflict | `2_KHO_BANGHI/00_KHO.md` | Between drawn channels, short-format channels rank 1–2 by median views and long-format 3–4 | same file, earlier paragraph | Between-channel signal is confounded; the file records both and flags the confound | same file, same day | **DO NOT RESOLVE** — the file itself declines to resolve it |
| C7 | Sensory-word density target 7–9%; one question every 60–90 s | `HE_THONG_KichBan_v2_14Video.md` PHẦN B2 | *"Chỉ 4 ràng buộc cứng… Mọi con số khác là triệu chứng… Cấm sửa một câu để con số đẹp hơn."* | `RUBRIC_KichBan.md` LUẬT 0; memory `feedback_so_do_khong_phai_dich.md` | B2 predates LUẬT 0; the 7–9% figure was measured with a different word list | **B** (2026-08-06) | **DO NOT RESOLVE** |
| C8 | Hook beat 2 = *"Tước tiện nghi hiện đại để gây cười + tương phản"* | `viet-kich-ban-nguoi-que-co-dai` PHẦN 2 | The 1.1M rain video contains **no modern-world reference** in its opening; it opens on a goal the rain destroys | measured 2026-08-06 from `2_KHO_BANGHI/InkExplainer/*Rained*.txt` | The beat was inferred from a small sample | **B** (measurement) | **DO NOT RESOLVE** — one pair only |
| C9 | `I` ≈ 0 (hard constraint) | `RUBRIC_KichBan.md` LUẬT 0; `qa_kichban.py` | Ink Explainer's 769K video uses `I` once — *"phá luật 'I ≈ 0', vẫn 769K"* | `CONGTHUC_InkExplainer_BestOf.md` §3 | The rule is a channel choice, not a niche law | same period | **DO NOT RESOLVE** |
| C10 | Topic must be original / never done | implied by earlier topic files and the "trinh nguyên" framing | *"Lấy đề tài ĐÃ CÓ CẦU rồi làm hơn"* — Ink Explainer reuses 7/12 topics and still gets 4.4M | memory `chien_luoc_lay_de_tai_da_co_cau.md`; `CONGTHUC_InkExplainer_BestOf.md` | Strategy reversed 2026-08-05/06 | **B** | **DO NOT RESOLVE** |
| C11 | Ink Explainer is the model channel (median 221,500; top-1 23%) | `CHOT_V19.md` §⑥; memory `feedback_so_do_khong_phai_dich.md` | Ink Explainer has the **lowest RPM** of the drawn cohort (3.64 vs Mogo 7.66, Mack 5.90) | `2_KHO_BANGHI/00_KHO.md` (2026-08-06) | The model was chosen on views alone; RPM was never in the comparison | **B** | **DO NOT RESOLVE** |
| C12 | 8 dead rule-files *"đã bị xoá khỏi kho, không còn tồn tại"* | `00_LUAT_HIEN_HANH.md`, death register note | Same 8 files are listed as living in `_KHO_LUU_DaChet/` | `00_LUAT_HIEN_HANH.md`, section "TÁM FILE ĐÃ CHẾT"; verified on disk | Editing error inside one file | both same file | **DO NOT RESOLVE** |
| C13 | `BOCTACH_4Kenh_SoSanh` is ⛔ superseded by `BOCTACH_16Kenh` | `00_LUAT` permission table | `BOCTACH_4Kenh_SoSanh_2026-08-04.md` carries **no ⛔ banner** and is still readable as current | the file itself | The two-part retirement rule was applied only half-way | table is newer | **DO NOT RESOLVE** |
| C14 | Filename `TEMPLATE_Thumbnail_KHOA_v1.md` | filesystem | Heading inside reads *"BẢN KHOÁ v2"* | file line 1 | Content revised, filename not | heading | **DO NOT RESOLVE** |
| C15 | Filename `LENH_GPT_ReviewKichBan_v3.md` | filesystem | Heading reads *"REVIEW KỊCH BẢN BẰNG GPT — v2"* | file line 1 | Same pattern as C14 | filename | **DO NOT RESOLVE** |
| C16 | Memory titled *"Model cho kịch bản — luôn Fable 5"* (`feedback_kichban_luon_fable5.md`) | filename + index line | Body: *"Opus 5 mặc định cho thân bài và mọi khâu khác; Fable 5 CHỈ cho hook 15s đầu và đoạn kết"* | same file body | Policy changed 27/07, filename kept | body | **DO NOT RESOLVE** |
| C17 | Anchor register naming: `VERIFY_Anchors_*` | V15–V18 | `NGHIENCUU_*_MoNeo` (V10–V12) · `VERIFY_Title_*` (V13–V14) · `MONEO_*` (V19) · `V18_MO_NEO` (root) | respective files | No naming convention was ever fixed | `MONEO_*` newest | **DO NOT RESOLVE** |
| C18 | Thumbnail is decided at gate 1 (packaging before script) | `WORKFLOW_Production.md` headline rule | *"Thumbnail làm ở BƯỚC CUỐI… ảnh thật dựng ở giai đoạn 5a"* | memory `workflow_thumbnail_lam_cuoi.md`; `WORKFLOW_Production.md` 05/08 amendment | Reconciled inside the workflow file as concept-vs-image, but the headline still reads "packaging first" | amendment | **DO NOT RESOLVE** — partially reconciled |

---

## 18. Deprecated and Historical Material

### 18.1 Formally retired, banner applied, moved to archive

`_KHO_LUU_DaChet/` — 8 rule files + 5 V01 script backups + 2 V01 prompt archives + 4 tool snapshots + `README.md`.

| File | Original purpose | Knowledge still in use? | Replaced by |
|---|---|---|---|
| `HE_THONG_KichBan_v1_11Video.md` | Script system v1 | Partly — v2 kept 7 of its rules ("BẢY LUẬT SỐNG SÓT") | `HE_THONG_KichBan_v2_14Video.md` |
| `HE_THONG_Thumbnail_Signature_v3.md` | Thumbnail signature | No — its core layout rule is now forbidden | `PROMPT_TONG_Thumbnail_v6.md` |
| `HE_THONG_Thumbnail_v5_ScriptToPackaging.md` | Script→packaging bridge | Unknown | v6 |
| `TEMPLATE_Thumbnail_DoiThu.md` | Competitor thumbnail DNA | No — DNA refuted | v6 CENTRE ANCHOR |
| `SUBNGACH_KhaiThac_Can.md` | Sub-niche definition | No — lane produced 0 breakouts in 4 months | `BANG_CAU_TatCa_CuNo` |
| `SUBNGACH_CoTheDoDa_2026-07-13.md` | Sub-niche definition | No — same lane | same |
| `CongThuc_Title_TrieuView.md` | Title formula | No | `HE_THONG_KichBan_v2` PHẦN C |
| `SoTay_ChonDeTai_20DeTaiDaChungMinh.md` | 20 proven topics | Unknown — topic list may still be useful | `BANG_CAU_TatCa_CuNo` |

### 18.2 Retired in the register but **still sitting beside live files**

| File | Banner? | Registered dead? | Location |
|---|---|---|---|
| `BANDO_NgachTitle_Thang.md` | ✅ | ✅ | **project root** |
| `NGHIENCUU_Title_3Kenh_Gap_2026-07-11.md` | ✅ | ✅ | **project root** |
| `TRAIN_ChatGPT_TOANBO_DuAn.md` | ✅ | partial — forbidden for review, craft sections revived | **project root** |
| `_BO_TRAIN_ChatGPT_ReviewKichBan_v2.md` | prefix only | ➖ not in register | **project root** |
| `BOCTACH_4Kenh_SoSanh_2026-08-04.md` | ❌ **none** | ✅ in permission table | **project root** — contains a measurably wrong benchmark |

### 18.3 Superseded but never marked

| File | Superseded by | Marked? |
|---|---|---|
| `NGHIENCUU_NguPhapHinh_InkExplainer.md` | `NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md` *(inferred from title "remeasured")* | ❌ |
| `TRAIN_ChatGPT_Thumbnail.md` (25/07) | `PROMPT_TONG_Thumbnail_v6.md` (05/08) | ❌ |
| `TRAIN_ChatGPT_BuocPolish.md` (24/07) | `chong-van-ai-narration-en` skill | ❌ |
| `ArtBible_NguoiQueCoDai.md` §6 thumbnail notes (25/06) | v6 | ❌ |
| `GAP_AUDIT_va_Roadmap.md` (24/06) — a previous audit of this same project | this document | ❌ |
| `viet-kich-ban-nguoi-que-co-dai`, `chia-shot-va-prompt-anh` skills | `sketchapiens-*` skills | ❌ **and both still auto-trigger** |
| `Video18_Sleep/_cu/*` (6 files) | root `V18_PACKAGING.md`, `DANG_V18.md` | folder name `_cu` ("old") only |
| `Video19_NightWalk/_nhap/Script_V19_DOT1–3.md` | `_nhap/DOT1–6.md` | ✅ banner applied |

### 18.4 Old rules Claude may still load unintentionally

1. **`viet-kich-ban-nguoi-que-co-dai`** — description matches any "ancient humans" title, so it can fire instead of `sketchapiens-viet-kich-ban`. Its PHẦN 9 checklist points at ⛔ `TEMPLATE_Thumbnail_DoiThu.md`.
2. **`chia-shot-va-prompt-anh`** — same problem; its PHẦN 9 also cites ⛔ `TEMPLATE_Thumbnail_DoiThu.md` and the refuted "clean digital" observation.
3. **`MEMORY.md`** quotes the full text of 8 dead memories inline under *"Nội dung cũ:"* — the dead content loads every session.
4. **`BOCTACH_4Kenh_SoSanh_2026-08-04.md`** has no banner; its "median 18,500" target was measured at 6,001.
5. **`00_LUAT_HIEN_HANH.md`** itself contains the C12 self-contradiction about whether the 8 dead files exist.

The project's own rule for this, stated in `00_LUAT`: *"khai tử một file thì phải làm cả hai việc — ghi vào sổ này và dán biển ⛔ vào dòng đầu chính file đó. Làm một nửa thì lần sau vẫn có người mở nhầm."* Five cases above are half-done.

---

## 19. Missing Production Components

| Component | Present? | Evidence |
|---|---|---|
| Project index | **Partial** | `00_LUAT_HIEN_HANH.md` is a tier map, but it is a document that must be read and remembered; the filesystem does not enforce it — 79 files sit flat at root with Tier-1 laws beside Tier-4 archives |
| Single source of truth | **Partial** | A permission table exists, but `WORKFLOW_Production.md` Stage 2 and `FLOW_VietKichBan_11Cong.md` both govern script writing with no stated precedence |
| Naming convention | **No** | 5 schemes for the anchor register; `Metadata_` vs `METADATA_`; `Thumbnail_Prompt` vs `THUMBNAIL_prompts` vs `PROMPT_THUMBNAIL`; `_nhap` vs `_cu` for drafts |
| Version convention | **No** | `FINAL`, `FINAL_deAI`, `FINAL_MaxHai`, `_v2`, `_v3`, `_v4`, `_v5`, `_FIXED`, `_truoc_vongN`, `_BO_`, `_cu`, `BACKUP`, `BACKUP2` all coexist |
| **Version control** | **No** | Project root is not a git repo; `/Users/admin` is a repo with 0 commits |
| Claim ledger standard | **Partial** | `MONEO_V19.md` is a strong template, but 10 of 19 videos have no register and 5 naming schemes exist |
| Per-video status file | **No** | Only `CHOT_V19.md` has a gate table; 18 videos have no status artefact |
| Analytics schema | **No** | No analytics file of any kind in the project |
| Changelog | **Partial** | `TEMPLATE_Thumbnail_KHOA_v1.md` has "NHẬT KÝ SỬA"; `00_LUAT` has "NHẬT KÝ SOI KHO"; no project-wide changelog |
| Archive policy | **Partial** | `_KHO_LUU_DaChet/` + a two-step retirement rule exist, but the rule is half-applied in 5 cases |
| Prompt registry | **No** | ~20 prompt artefacts across skills, root files and per-video files with no index |
| Rule priority | **Yes** | `00_LUAT` precedence rules 1–4 — one of the strongest parts of the project |
| Definition of done | **Partial** | Gates 0–4 and 1–11 define done for stages; nothing defines "video is finished/published" |
| Feedback-loop workflow | **No** | Steps 16–17 of the lifecycle produce no artefact |
| Retention-drop → script mapping | **No** | No timestamp mapping exists for any video |
| Generic vs video-specific knowledge separation | **Partial** | Enforced for skills (`sketchapiens-` prefix rule, 05/08) but **not** for files — `V17_PACKAGING_CHOT.md`, `V18_MO_NEO.md`, `V18_PACKAGING.md`, `CONCEPT_Thumbnail_V16_V17.md` sit at root among channel-wide laws |
| Publication record | **No** | No file records upload date, URL, or published status for any video |
| Asset manifest | **No** | No file maps images/audio to shots; count mismatches in V12/V14/V15 went unrecorded |
| Shared code library | **No** | `tts_stdlib.py`, `2_assemble_video.py`, `run_pipeline.py`, `gen_prompts.py` exist as 4–6 forked copies each |
| Secrets policy | **Partial** | Most scripts read from env vars; one file instructs pasting a key into source (see §20) |


---

## 20. Current Risks

| # | Risk | Level | Evidence | Possible consequence |
|---|---|---|---|---|
| R1 | **No version control.** Project root is not a git repo; `/Users/admin` is a repo with 0 commits / 0 tracked files (stated in `00_LUAT`, verified in this audit) | **CRITICAL** | `git` reports no repo at project root; 4.8 GB of work | Any overwrite or accidental delete is permanent. V02–V16 narration files have no draft history at all |
| R2 | **Deprecated skills still auto-trigger.** `viet-kich-ban-nguoi-que-co-dai` and `chia-shot-va-prompt-anh` are unprefixed, their descriptions match this channel's requests, and both reference ⛔ `TEMPLATE_Thumbnail_DoiThu.md` | **CRITICAL** | skill listings; PHẦN 9 of both | Claude writes to a refuted thumbnail DNA and a refuted style observation without anyone noticing |
| R3 | **No record of which script version was published.** Three files named `FINAL` for V01; no publication record for any video | **HIGH** | §10 | Cannot diff published output against local script; cannot attribute a retention drop to a specific line |
| R4 | **Analytics never returns to the system.** No analytics artefact in the project; all first-party numbers in one memory file | **HIGH** | §14 | The channel produces competitor knowledge continuously and self-knowledge almost never; the loop that would improve the system does not close |
| R5 | **Research separated from claims.** 768 transcripts, 31 thumbnails, 57 frames with no mapping to the videos they informed; `VAULT_AncientHumans_KnowledgeVault.md` cites 49 scripts not in the repo | **HIGH** | §11.6 | Claims cannot be re-verified; the same wrong number can survive for months (four did) |
| R6 | **Reused-content exposure.** 768 competitor scripts now on disk, protected only by a written rule (*"cấm mở trong chế độ ② VIẾT"*). The user's previous channel was removed for this policy | **HIGH** | `2_KHO_BANGHI/00_KHO.md`; `CONGTHUC_InkExplainer_BestOf.md` | Channel-level strike; YPP rejection |
| R7 | **Character system contradicts itself** (`@token` vs verbatim-text) across 6 live files with no precedence | **HIGH** | C2, G7 | Inconsistent characters across a video; wasted regeneration |
| R8 | **Style words contradict** (`clean`/`smooth`/`cartoon` required vs banned) between the shot skills and the thumbnail template | **HIGH** | C3, C4 | Video frames and thumbnail drift into different art styles |
| R9 | **Half-applied retirement.** 5 files are dead in the register but readable as current, notably `BOCTACH_4Kenh_SoSanh` with the wrong 18,500 benchmark | **HIGH** | §18.2 | A refuted target is used to set goals |
| R10 | **One agent writes and grades its own work.** Gates 7–9 are self-check; the only outside review is a manual copy-paste to ChatGPT by the user | **HIGH** | `rubric_mu_loi_cau_truc.md`: *"Người viết không tự chấm được vì họ biết đáp án"* | Structural faults survive: V17 scored 68/74 and was still structurally broken |
| R11 | **No read-only critique stage in the toolchain.** Gate 10 depends entirely on the user manually running each round | **HIGH** | §7 | If the user skips it, the known blind spot returns |
| R12 | **Rule volume.** ~26 KB entry file + 46 KB and 55 KB skills + 14 KB memory index load before work begins | **MEDIUM** | §3.5 | Later rules crowd out earlier ones; the project has already recorded rules being forgotten mid-session |
| R13 | **Large files dilute context.** 14 `PROMPTS_FULL.txt` between 187 KB and 1.4 MB; two 400 KB JSON alignment files | **MEDIUM** | §2 | Any accidental read consumes the window |
| R14 | **Cross-video contamination.** `_V19_material_TwoSleeps.txt` sits in `Video18_Sleep/`; V20 material sits in `Video19/_nhap/`; V17/V18 packaging sits at project root | **MEDIUM** | §9 | Gate-A anti-duplication greps produce false positives (already observed) and could produce false negatives |
| R15 | **Duplicate prompts.** 4 versions of the review prompt, 6 of the character system, 7 thumbnail sources, 5 competitor teardowns | **MEDIUM** | §16 | Wrong version used; edits applied to the copy that is not loaded |
| R16 | **No file has an owner or status field.** Status had to be inferred from content throughout this audit | **MEDIUM** | §3 | Every future reader repeats this inference |
| R17 | **Archive is still readable as current.** `_KHO_LUU_DaChet/` is excluded by convention only; `MEMORY.md` quotes dead memories inline | **MEDIUM** | §18.4 | Dead rules re-enter through the memory index every session |
| R18 | **Secret-handling anti-pattern.** `Video14_Milk/build/1_make_tts_elevenlabs.py` line 16 defaults to `"DÁN_API_KEY_CỦA_BẠN_VÀO_ĐÂY"` and instructs pasting a key into the file | **MEDIUM** | file, redacted | A future edit writes a live key into a file that has no `.gitignore` protection *(project is not a repo, so no ignore rules apply at all)* |
| R19 | **Asset count drift.** V12 265 img / 255 mp3; V14 608/302; V15 568/564; V16 0 images | **MEDIUM** | §2, §9 | Audio–image desync at assembly — the documented cause of the V15 failure |
| R20 | **Index collision.** `Video17_Death/` and `Video17_Rain/` both claim 17; V01 has no folder | **LOW** | §2 | Ambiguous references to "V17" |
| R21 | **Claude cannot verify the channel.** Browser automation is restricted to a personal Chrome profile; the channel Gmail is off-limits | **LOW** *(deliberate)* | memory `browser_chrome_cuong_only.md` | All first-party data must be relayed manually — a permanent bottleneck on R4 |

### Secrets findings

**[REDACTED SECRET FOUND] — none confirmed live.** Detail:

| Location | Type possibly present | Finding |
|---|---|---|
| `automation-pipeline/.env.example` | OpenAI / ElevenLabs / Gemini keys | **Placeholders only** (`sk-...`, empty). Correct pattern. No real `.env` file exists in the project |
| `automation-pipeline/pipeline.py` | Gemini, ElevenLabs | Reads `os.environ[...]` — correct |
| `Video14_Milk/build/tts_stdlib.py` and 4 sibling copies | ElevenLabs | Reads env var; file explicitly states *"KHÔNG ghi key vào file này"* — correct |
| `Video14_Milk/build/1_make_tts_elevenlabs.py` | ElevenLabs | ⚠️ Falls back to a literal placeholder and instructs the user to paste a key into the source file — **anti-pattern, no key currently present** |
| `Video06/08/09/*/run_pipeline.py` | ElevenLabs | Header value passed from a variable; no literal key found |
| `2_KHO_BANGHI/*/_vtt/*.info.json` (4 files) | Google API key pattern | Third-party keys embedded by YouTube in downloaded player metadata, not project credentials. Low risk, but they are stored on disk |
| `GhepVideo_Desktop/**` | — | Matches are Rust/npm build fingerprints, not secrets |

No password, cookie, private key or bearer token was found. **No secret value is reproduced in this report.**

---

## 21. Questions the Architect Must Resolve

*These cannot be answered from files. They are listed, not answered.*

1. **Which videos are actually published?** No file records publication status, upload date or URL. Session context suggests ~13 public videos, but that is not in the repo.
2. **Is `WORKFLOW_Production.md` or `FLOW_VietKichBan_11Cong.md` authoritative for the script phase?** Both are Tier 1 and both govern it.
3. **Which V01 script was used** — `Script_Video01_FINAL.txt` or `Script_Video01_FINAL_deAI.txt`?
4. **Was V18's GPT critique ever applied?** The critique prompt exists; no feedback and no post-critique snapshot do.
5. **`@token` or verbatim-text for character consistency?** Two live systems, no precedence, and the 12 token sheets appear never to have been created.
6. **Do the banned words `cartoon`/`clean`/`smooth` apply to video frames, or only to thumbnails?**
7. **Is Ink Explainer still the model channel** now that it has the lowest RPM of the drawn cohort, and Mack/Mogo are higher?
8. **What is `VAULT_AncientHumans_KnowledgeVault.md` supposed to contain?** It is 873 bytes; `00_LUAT` describes it as holding 8 topics distilled from 49 scripts. Stub, truncation, or wrong description?
9. **Where are the 49 competitor scripts** that the vault was built from?
10. **Is `Video17_Death` abandoned permanently**, and should the index be reused or retired?
11. **Which rules has the user already dropped without deleting?** Several files are dead in practice but unmarked (§18.3).
12. **Which analytics numbers are trustworthy?** The only recorded ones rest on 12–13 observations and the memory file itself says not to use them as a standard.
13. **Is Claude Code or claude.ai Projects the primary environment?** The project lives under `~/Claude/Projects/` (a claude.ai-style path) but all instruction is in `~/.claude/skills` and `~/.claude/projects/…/memory` (Claude Code paths).
14. **Do other channels share this machine's skill namespace?** `viet-kich-ban-sinh-ton-vn`, `viet-kich-ban-shorts-funny`, `viet-kich-ban-drama-tre-em`, `viet-kich-ban-squishy-cute`, `punch-up-hai-sinh-ton` suggest at least one other YouTube project.
15. **Should the 768-transcript corpus stay inside this project** given the reused-content exposure, or live outside it?
16. **What is the intended relationship between `GhepVideo_Desktop`, `GhepVideo_Studio`, `GhepVideo_Studio_NextJS`, `GhepVideo_Pipeline` and `automation-pipeline`?** Five overlapping tools; only `GhepVideo_Desktop` is large enough to look actively developed.
17. **Should `V15_Allergies` be taken private?** `00_LUAT` says it is public and broken and is dragging the channel's YPP profile down; the item has been open since 29/07.
18. **Should the short-format / long-format strategic fork be decided now?** `2_KHO_BANGHI/00_KHO.md` frames it as a real trade-off (views vs RPM vs watch-hours) and explicitly defers to the owner.

---

## 22. Raw Project Rules Appendix

*Rules that directly govern workflow or output quality, quoted near-verbatim.*

| # | Rule | Source file | Heading / location | Inferred status | Also appears in |
|---|---|---|---|---|---|
| A1 | *"Tầng thấp hơn thắng. Tầng 1 phủ quyết tầng 2, 3, 4."* | `00_LUAT_HIEN_HANH.md` | ⚖️ LUẬT ƯU TIÊN, rule 1 | CANONICAL | — |
| A2 | *"Số đếm tay trên transcript gốc thắng MỌI báo cáo, kể cả NotebookLM."* | `00_LUAT_HIEN_HANH.md` | rule 2 | CANONICAL | `2_KHO_BANGHI/00_KHO.md` |
| A3 | *"Không giải quyết được → đo lại, đừng chọn bừa."* | `00_LUAT_HIEN_HANH.md` | rule 4 | CANONICAL | — |
| A4 | *"Không trộn hai chế độ trong một phiên — đang viết mà đi tra mỏ neo là mất mạch."* | `00_LUAT_HIEN_HANH.md` | BỐN CHẾ ĐỘ | CANONICAL | skill descriptions |
| A5 | Mode ② WRITE: *"không mở nexlev, không tra web"* | `00_LUAT_HIEN_HANH.md` | mode table | CANONICAL | `2_KHO_BANGHI/00_KHO.md` extends it to the corpus |
| A6 | *"khai tử một file thì phải làm cả hai việc — ghi vào sổ này và dán biển ⛔ vào dòng đầu chính file đó."* | `00_LUAT_HIEN_HANH.md` | SỔ KHAI TỬ | CANONICAL, **half-applied 5×** | — |
| A7 | *"Gỡ tên kênh và logo đi, dán video của mình cạnh 20 video cùng title… có ai chỉ ra được cái nào là của mình không?"* | `00_LUAT_HIEN_HANH.md` | LUẬT MỚI 05/08 | CANONICAL | `CHINHSACH_YOUTUBE_2026` |
| A8 | *"mỗi video phải có ít nhất MỘT thứ mà 20 kênh kia không có."* | `00_LUAT_HIEN_HANH.md` | same | CANONICAL, added to gate 1 | — |
| A9 | *"đo được gì trên kênh này thì ghi vào skill `sketchapiens-*`… Ghi vào skill dùng chung là dạy sai cho mọi dự án sau."* | `00_LUAT_HIEN_HANH.md` | SKILL RIÊNG | CANONICAL | — |
| A10 | *"Ba thứ KHÔNG chứng minh được gì: chạy không lỗi · đủ số file · đúng độ dài."* | `QUY_TRINH_2_CONG.md` | CỔNG RA | CANONICAL | `WORKFLOW_Production.md` gate 4 |
| A11 | *"PACKAGING ĐI TRƯỚC KỊCH BẢN"* | `WORKFLOW_Production.md` | top banner | CANONICAL, amended 04–05/08 | memory `workflow_thumbnail_lam_cuoi` |
| A12 | *"thumbnail: cửa 1 chỉ chấm CONCEPT (10 phút, không gen ảnh); ảnh thật dựng ở giai đoạn 5a"* | `WORKFLOW_Production.md` | SỬA 04/08 | CANONICAL | memory `workflow_thumbnail_lam_cuoi` |
| A13 | Gate A grep *"PHẢI quét cả thư mục `_nhap/`"* recursively | `WORKFLOW_Production.md` | HAI CỔNG MÁY MÓC | CANONICAL | `FLOW_VietKichBan_11Cong.md` |
| A14 | *"QA TỪNG CHƯƠNG — làm NGAY sau khi viết xong mỗi chương"* | `WORKFLOW_Production.md` | 05/08 | CANONICAL | `FLOW_VietKichBan_11Cong.md` gate 6 |
| A15 | *"Chỉ 4 ràng buộc cứng: dấu `!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng · `I` ≈ 0."* | `RUBRIC_KichBan.md` | LUẬT 0 | CANONICAL | memory `feedback_so_do_khong_phai_dich`, `qa_kichban.py` |
| A16 | *"Mọi con số khác là triệu chứng… Cấm sửa một câu để con số đẹp hơn."* | `RUBRIC_KichBan.md` | LUẬT 0 | CANONICAL | memory same |
| A17 | *"Đừng lấy video cũ của kênh làm trần."* | memory `feedback_so_do_khong_phai_dich.md` | How to apply | CANONICAL | `chan_doan_kenh_benh_A.md` |
| A18 | *"'you' = NGƯỜI XEM; 'we/us/our' = CẢ LOÀI NGƯỜI; KHÔNG 'I'."* | `viet-kich-ban-nguoi-que-co-dai` | PHẦN 4 | ACTIVE — but counter-example on record (C9) | `sketchapiens-viet-kich-ban`, `TRAIN_ChatGPT_TOANBO` |
| A19 | *"Dấu '!' = 0/5 video → CẤM TIỆT."* | `KHO_GiongCamXuc_DoiThu.md` | SỐ CỨNG | CANONICAL | LUẬT 0, `qa_kichban.py` |
| A20 | *"Gọi tên cảm xúc TRƯỚC fact — pre-load… trước MỖI reveal lớn."* | `KHO_GiongCamXuc_DoiThu.md` | pattern 6 | CANONICAL | `LENH_GPT_BoiCanh_TayNghe.md` |
| A21 | *"Đây là bảng CHẨN, không phải danh sách đi chợ… câu này có tồn tại không nếu không có bảng kiểm nào? Không → cắt."* | `sketchapiens-viet-kich-ban/SKILL.md` | device checklist | CANONICAL | — |
| A22 | *"Lấy mỏ neo thoải mái. Luận đề và thứ tự kể phải là của mình."* | `CONGTHUC_InkExplainer_BestOf.md` | §2 boundary table | CANONICAL | memory `chien_luoc_lay_de_tai_da_co_cau` |
| A23 | *"⛔ BA CHỮ CẤM TUYỆT ĐỐI: `cartoon` · `clean` · `smooth`"* | `TEMPLATE_Thumbnail_KHOA_v1.md` | §BA CHỮ CẤM | CANONICAL for thumbnails; **conflicts with shot skills** | memory `gotcha_style_doodle_khong_hoathinh` |
| A24 | *"Khi model ĐÃ vẽ đúng một thứ, ĐỪNG thêm luật cho thứ đó."* | `TEMPLATE_Thumbnail_KHOA_v1.md` | LUẬT QUAN TRỌNG NHẤT | CANONICAL | memory `feedback_dung_them_luat_khi_model_dang_dung` |
| A25 | LUẬT 1 — *"TÂM KHUNG DÀNH CHO VẬT KỂ CHUYỆN, KHÔNG PHẢI NHÂN VẬT"* | `PROMPT_TONG_Thumbnail_v6.md` | PHẦN B | CANONICAL | `sketchapiens-thumbnail` |
| A26 | LUẬT 2 — *"CHỮ PHẢI THÊM THÔNG TIN MỚI, KHÔNG LẶP TITLE"* | `PROMPT_TONG_Thumbnail_v6.md` | PHẦN B | CANONICAL | — |
| A27 | *"mặt/tay/chân phải TRẮNG ĐẶC 3-6%"* | memory `gotcha_do_tong_thumbnail_vo_nghia.md` | new rule | CANONICAL | — |
| A28 | *"'sáng 80-110' chết (tương quan view ≈ 0) · 'chữ 13-19%' chết (thật ra 22%)"* | memory same | refutations | CANONICAL refutation | — |
| A29 | *"Nhất quán bằng CHỮ, không bằng ref… không @token."* | `chia-shot-va-prompt-anh` / `sketchapiens-chia-shot` | PHẦN 0 rule 3 | ACTIVE — **conflicts with CastBible** | — |
| A30 | *"NỀN THEO NGỮ CẢNH — KHÔNG theo tỉ lệ cố định."* | same | PHẦN 0 rule 2 | CANONICAL | `ArtBible` §4 |
| A31 | *"~8-10 từ/shot · ~2.6-3.3 giây/shot · ~18-23 shot/phút"* | same | PHẦN 1 | ACTIVE | measured V17 2.1 s, V18 2.5 s |
| A32 | *"KHÔNG đổi chữ narration khi tách — chỉ chèn ranh giới dòng."* | same | PHẦN 1 | CANONICAL | — |
| A33 | *"LUÔN gen vào thư mục rỗng, 1 lượt, đếm file == số prompt trước khi ghép."* | memory `gotcha_gen_anh_lech_so.md` | How to apply | CANONICAL | — |
| A34 | *"video phải dài trên 8 phút mới được chèn mid-roll… 8-10 phút là vùng chết về doanh thu"* | `checklist-dang-video-long-form` | Phần 1 | CANONICAL | `CHOT_V19.md` §① |
| A35 | *"đặt một ổ mỗi 2,5 – 3,5 phút"*; hybrid manual+auto ≈ +5% | same | Phần 1 | CANONICAL | — |
| A36 | *"Not made for kids trừ khi nội dung thật sự nhắm trẻ em."* | same | Phần 6 | CANONICAL | — |
| A37 | *"cho họ thứ NGƯỜI XEM NHÌN THẤY, giấu thứ chỉ MÌNH BIẾT"* | `LENH_GPT_ReviewKichBan_v3.md` | RANH GIỚI | CANONICAL | — |
| A38 | *"mỗi vòng mở CỬA SỔ CHAT MỚI."* | same | 🔁 MỖI VÒNG | CANONICAL | — |
| A39 | *"Chỉ mô tả CÁI GÌ đổi, tuyệt đối không nói VÌ SAO."* | same | phần 6 | CANONICAL | — |
| A40 | *"câu 1 ép XẾP HẠNG: 'the TEN worst, ranked worst first'"* | same | SỬA KHUÔN HỎI 06/08 | CANONICAL | memory `feedback_vong_review_gpt` |
| A41 | *"đếm số lần một lỗi bị bắt ĐỘC LẬP ở nhiều phần khác nhau, đừng đếm số câu bị gạch."* | same | same | CANONICAL | memory same |
| A42 | *"lỗi ẩn dụ thì CẮT CẢ CÂU, đừng thay chữ trong câu."* | same | Bài học vòng 6 | CANONICAL | memory same |
| A43 | *"Dán TAY NGHỀ (giọng · chống văn AI). Cấm dán CHIẾN LƯỢC · RUBRIC · SỐ ĐẾM."* | `LENH_GPT_BoiCanh_TayNghe.md` | RANH GIỚI | CANONICAL — **reverses A-header of `LENH_GPT_ReviewKichBan_v3.md`** | memory `feedback_vong_review_gpt` |
| A44 | *"giá trị người review = khoảng chênh giữa thứ họ biết và thứ mình biết."* | same | ⚖️ đừng train A–Z | CANONICAL | memory same |
| A45 | *"Người viết không tự chấm được vì họ biết đáp án… cấm dán luật kênh cho người review."* | memory `rubric_mu_loi_cau_truc.md` | — | CANONICAL — **partially reversed by A43** | — |
| A46 | *"mọi câu thêm vào sau cổng 3 phải quay lại chạy cổng 3 một lần nữa."* | `MONEO_V19.md` | KHOÁ M3b | CANONICAL | `_nhap/Script_V19_GhiChu.md` |
| A47 | *"mở primary source, không tin snippet."* | `MONEO_V19.md` / `FLOW_VietKichBan_11Cong.md` | gate 3 | CANONICAL | — |
| A48 | Author inference must be attributed: *"phải ghi 'the researchers put that down to…', cấm nói như sự thật."* | `MONEO_V19.md` | M3b | CANONICAL | — |
| A49 | *"Kho này chỉ để ĐO. Cấm mở trong chế độ ② VIẾT."* | `2_KHO_BANGHI/00_KHO.md` | LUẬT DÙNG KHO | CANONICAL | A5 |
| A50 | *"Dán thứ dạy nó NGHE. Cấm dán thứ dạy nó CHẤM."* | `2_KHO_BANGHI/00_KHO.md` | RANH GIỚI | CANONICAL | A43 |
| A51 | *"Luôn xác minh bằng một con số đã biết trước"* (channel identification) | `2_KHO_BANGHI/00_KHO.md` | Bẫy 1 | CANONICAL | — |
| A52 | *"Mọi chỉ số tính theo RANH GIỚI CÂU đều vô nghĩa"* on ASR captions | `2_KHO_BANGHI/00_KHO.md` | Bẫy 3 | CANONICAL | — |
| A53 | *"viết theo BATCH… dừng cho duyệt"* | `viet-kich-ban-nguoi-que-co-dai` PHẦN 3 | — | CANONICAL | memory `feedback_chia_nho_batch` |
| A54 | *"cấm đưa bản 7/10 rồi chờ chủ đẩy"* | memory `feedback_max_effort_first_pass.md` | — | CANONICAL | — |
| A55 | *"duyệt script qua cột Dịch VI (bảng EN+VI, KHÔNG cột hình lúc duyệt)"* | memory `workflow_ngonngu_format.md` | — | CANONICAL | `Script_Video17_DUYET_EN-VI.md`, `DUYET_V19_EN_VI.md` |
| A56 | *"quit saving no trước khi open"* (macOS apps hold stale content) | memory `gotcha_app_giu_ban_cu.md` | — | CANONICAL | — |
| A57 | *"Ghép video: dùng app, không tự viết script"* | memory `feedback_dung_app_ghepvideo.md` | — | CANONICAL | V15 failure |
| A58 | *"browser automation CHỈ dùng nqcthedev@gmail.com; KHÔNG mở Gmail kênh YouTube"* | memory `browser_chrome_cuong_only.md` | — | CANONICAL | — |
| A59 | *"Opus 5 mặc định… Fable 5 CHỈ cho hook 15s đầu và đoạn kết."* | memory `feedback_kichban_luon_fable5.md` | body | CANONICAL — **filename contradicts body** | `model_routing_pref.md` |
| A60 | Deferred topic zone: minors in distressing situations postponed until after YPP | `00_LUAT_HIEN_HANH.md` | Vùng đề tài phải HOÃN | CANONICAL | `CHINHSACH_YOUTUBE_2026` |

---

## 23. Recommended Inputs for Folder Redesign

*Inputs only. No structure is proposed here.*

**Canonical files** — `00_LUAT_HIEN_HANH.md` · `FLOW_VietKichBan_11Cong.md` · `WORKFLOW_Production.md` · `QUY_TRINH_2_CONG.md` · `HE_THONG_KichBan_v2_14Video.md` · `RUBRIC_KichBan.md` · `PROMPT_TONG_Thumbnail_v6.md` · `TEMPLATE_Thumbnail_KHOA_v1.md` · `CHINHSACH_YOUTUBE_2026_AnhHuong.md` · `CONGTHUC_InkExplainer_BestOf.md` · `LENH_GPT_ReviewKichBan_v3.md` · `LENH_GPT_BoiCanh_TayNghe.md` · `KHO_GiongCamXuc_DoiThu.md` · `NganHang_ReHook_BucketBrigade.md` · `BANG_CAU_TatCa_CuNo_2026-07-29.md` · `NGHIENCUU_CloneSwarm_2026-07-29.md` · `BOCTACH_16Kenh_2026-08-05.md` · `2_KHO_BANGHI/00_KHO.md`

**Active workflows** — 4 working modes (`00_LUAT`) · 5 production stages + gates 0–4 (`WORKFLOW_Production.md`) · 11 script gates (`FLOW_VietKichBan_11Cong.md`) · two-gate discipline (`QUY_TRINH_2_CONG.md`) · 6-round external review loop (`LENH_GPT_ReviewKichBan_v3.md`)

**Current videos** — 19 directories + V01 at root; §9 table; only V19 has a status artefact; 6 file groups belong to a video but sit elsewhere (§9)

**Prompt library** — ~20 artefacts across 6 `sketchapiens-*` skills, 15 shared skills, 8 root prompt files and 4 per-video prompt families; no registry exists (§6)

**Agents** — none exist

**Skills** — 6 `sketchapiens-*` (canonical) · 15 shared YouTube · ~20 unrelated · 4 unprefixed predecessors that still auto-trigger (§5, R2)

**Analytics** — nothing in the project; one memory file holds all first-party numbers, all on samples of 12–13 (§14)

**Research** — `2_KHO_BANGHI/` 768 transcripts / 22 channels + tools; `NGHIENCUU_*` ×8; `BOCTACH_*` ×3; `BANDO_*` ×2; `MoXe_*`/`TearDown_*` ×4; per-video anchor registers ×9 in 5 naming schemes

**Assets** — 3,087 png · 2,910 mp3 · 49 mp4 · 428 jpeg · 1 finished thumbnail · 31 competitor thumbnails (well-named) · 57 unindexed frames · 3 style refs · **0 character model sheets** · **0 logo/banner files**

**Archives** — `_KHO_LUU_DaChet/` (20) · `Video18_Sleep/_cu/` (6) · `Video17_Rain/_nhap/` (8) · `Video19_NightWalk/_nhap/` (11) · 5 dead files still at root (§18.2)

**Contradictions** — 18 recorded in §17, of which C1, C2, C3, C11, C13 have direct workflow impact

**Missing components** — 20 recorded in §19; the highest-leverage absences are version control, publication record, analytics storage, naming/version conventions, prompt registry and a per-video status file

**User decisions still required** — 18 questions in §21

---

## AUDIT SELF-CHECK

| Required section | Present |
|---|---|
| Directory tree | ✅ §2 |
| File inventory | ✅ §3 (3.1 root, 3.2 per-video, 3.3 corpus, 3.4 archive, 3.5 instruction layer) |
| Knowledge map | ✅ §4.1–4.20 |
| Prompt audit | ✅ §6 |
| Claude instruction audit | ✅ §5 |
| Script workflow | ✅ §7 |
| Video lifecycle | ✅ §8 |
| Current videos | ✅ §9 |
| Version map | ✅ §10 |
| Research audit | ✅ §11 |
| Thumbnail audit | ✅ §12 |
| Asset audit | ✅ §13 |
| Analytics audit | ✅ §14 |
| Competitor audit | ✅ §15 |
| Duplicate audit | ✅ §16 |
| Contradiction audit | ✅ §17 |
| Deprecated materials | ✅ §18 |
| Missing components | ✅ §19 |
| Risks | ✅ §20 |
| Open questions | ✅ §21 |
| Raw rules appendix | ✅ §22 |
| Redesign inputs | ✅ §23 |

---

## AUDIT STATUS: PARTIAL

Every file in the project was **inventoried** (path, size, line count, modification date, first line). Structural extraction (`#`/`##`/`###`) was performed on the core knowledge files. The following was **not read in full**, with reasons:

| Not fully read | Count | Reason |
|---|---|---|
| `2_KHO_BANGHI/**/*.txt` — competitor transcripts | 768 | Source data, not project knowledge. Aggregate metrics were computed programmatically instead (view, duration, word count, wpm per file) |
| `2_KHO_BANGHI/**/_vtt/*` | 1,265 vtt + info.json | Raw downloads, superseded by the converted `.txt` |
| `VideoNN_*/PROMPTS_FULL.txt`, `PROMPTS_CLEAN.txt` | 16 files, 187 KB–1.4 MB | Machine-generated from `shot_data.py`; reading them would consume the context window without adding knowledge. Structure verified on samples |
| `VideoNN_*/Script_VideoNN_narration.txt` | 18 files | Only V17 and V19 read in full; the rest inventoried by size/date. Narration content is video-specific output, not project rules |
| `VideoNN_*/*.py` build scripts | 32 files | Sampled (`tts_stdlib.py`, `1_make_tts_elevenlabs.py`, `run_pipeline.py`, `pipeline.py`) for the secrets scan; duplication established by name and size |
| `GhepVideo_Desktop/**` | 26,368 files | Application source + `node_modules` + Rust build artefacts. Directory role identified from `SPEC_GhepVideo_Desktop.md`; contents out of audit scope |
| `GhepVideo_Studio`, `GhepVideo_Studio_NextJS`, `GhepVideo_Pipeline`, `SketchapiensImageTool`, `automation-pipeline` | ~57 files | File listings taken; source not read except `pipeline.py` header for secrets |
| Root files marked [HEADINGS] | 12 | Structure extracted, body not read: `WORKFLOW_Production.md`, `HE_THONG_KichBan_v2_14Video.md`, `PROMPT_TONG_Thumbnail_v6.md`, `TEMPLATE_Thumbnail_KHOA_v1.md`, `QUY_TRINH_2_CONG.md`, `CHINHSACH_YOUTUBE_2026_AnhHuong.md`, `ArtBible_NguoiQueCoDai.md`, `CastBible_DienVien.md`, `BasePack01_Sketchapiens.md`, `Brand_Kit_Kenh.md`, `VAULT_*` ×2 |
| Root files marked [LISTED] | 45 | Existence, size, date, first line only |
| `~/.claude/skills/**` | ~50 skills | 7 read in full (loaded into session context); the rest listed by name, size, date and file count |
| `memory/*.md` | 36 files | `MEMORY.md` index read in full; 4 individual memories read in full; the remaining 32 summarised from their index lines |
| Binary media | 3,087 png · 2,910 mp3 · 49 mp4 · 428 jpeg | Counted and role-identified by filename and location, per instruction |
| `/Users/admin/Desktop` | unknown | **Not accessible** — macOS TCC denies directory listing to this shell, including with the sandbox disabled. Any project material there is outside this audit |

**Nothing in this report is asserted as read that was not read.** Where a conclusion rests on absence of evidence rather than a statement in a file, it is labelled as inference.

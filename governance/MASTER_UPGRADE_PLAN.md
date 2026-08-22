# MASTER UPGRADE PLAN — KẾ HOẠCH NÂNG CẤP TỔNG THỂ

**Project:** Sketchapiens Content Operating System  
**Status:** `ACTIVE ROADMAP`  
**Branch triển khai hiện tại:** `upgrade/story-engine-v21`  
**Ngày lập:** 2026-08-21  
**Owner:** người dùng / chủ dự án  

> ## ⚠️ FILE NÀY LÀ ROADMAP, KHÔNG PHẢI SỔ LUẬT
>
> `MASTER_UPGRADE_PLAN.md` — **Kế hoạch nâng cấp tổng thể** là nguồn chuẩn cho **kiến trúc đích, thứ tự migration, acceptance criteria và trạng thái upgrade**.
>
> Nó **không** được tự tạo luật nội dung mới, không thắng `CLAUDE.md`, `.claude/rules/**`, `RULE_REGISTRY.yaml`, `SOURCE_OF_TRUTH.md` hay `CHANGE_POLICY.md` trong phạm vi của các file đó.
>
> Một discovery sáng tạo chỉ được đi theo đường:
>
> `OBSERVATION → CANDIDATE MECHANISM → CROSS-CORPUS CHECK → FAILURE MODE → TEST ON SKETCHAPIENS → OWNER DECISION → PROMOTE / DEMOTE / MERGE / DELETE`
>
> Thiếu điều kiện của `CHANGE_POLICY.md` thì **không được** ghi thành canonical rule.

---

# 0. MỤC TIÊU CỦA ĐỢT NÂNG CẤP

Không biến repo thành một đống prompt lớn hơn.

Mục tiêu là biến Sketchapiens thành một **software-like Content Operating System — Hệ điều hành sản xuất nội dung vận hành như phần mềm**, trong đó:

1. mỗi module có một trách nhiệm rõ;
2. context chỉ được nạp khi cần;
3. mỗi phạm vi có đúng một source of truth;
4. knowledge, rules, experiments và runtime artifacts không trộn vào nhau;
5. deterministic errors được máy bắt;
6. creative judgment vẫn do người / reviewer đánh giá;
7. mỗi video là một R&D cycle làm hệ thống tốt hơn;
8. architecture không phình theo mỗi discovery mới.

### Không phải mục tiêu

- không làm project trông giống Next.js chỉ để đẹp cây thư mục;
- không tạo `src/`, `components/`, `utils/` nếu không có nhu cầu nghiệp vụ thật;
- không tạo đủ Story / Evidence / Voice / Packaging engine chỉ vì sơ đồ cân đối;
- không rewrite toàn bộ repo trong một lần;
- không vừa refactor architecture lớn vừa đổi toàn bộ creative behavior rồi mất khả năng biết cái gì gây regression.

---

# 1. ARCHITECTURE CONTRACT — HỢP ĐỒNG KIẾN TRÚC

Các nguyên tắc dưới đây là **nguyên tắc thiết kế của đợt migration**, không phải luật sáng tạo về view/retention.

## A-01 — Module owns its internals — Module tự sở hữu phần bên trong

Thứ chỉ một module dùng thì nằm trong module đó.

Ví dụ:

```text
.claude/skills/sketchapiens-story-engine/
├── SKILL.md
├── README.md
├── references/
├── templates/
├── scripts/
└── tests/
```

Không đưa một template chỉ Story Engine dùng vào `/templates` root.
Không đưa một checker chỉ Story Engine dùng vào `/tools` root.

---

## A-02 — Local until proven shared — Giữ cục bộ cho tới khi chứng minh là dùng chung

Một artifact chỉ được nâng lên shared/root khi có **ít nhất hai consumer độc lập thật sự** hoặc có lý do hệ thống rõ ràng.

Shared root không phải nơi chứa thứ “có vẻ quan trọng”.
Shared root chỉ chứa thứ **thực sự shared**.

---

## A-03 — `SKILL.md` is public interface — `SKILL.md` là giao diện công khai

Nhìn `SKILL.md` như `index.ts` / public API của một software module.

Nó nên trả lời:

- module này làm gì;
- khi nào kích hoạt;
- input / output;
- workflow;
- hard boundaries;
- cần route sang supporting file nào ở bước nào.

Nó **không nên** đồng thời là:

- public API;
- toàn bộ implementation;
- historical changelog;
- kho luật chết;
- tutorial dài;
- transcript teardown archive.

---

## A-04 — `CLAUDE.md` is router, not encyclopedia — `CLAUDE.md` là bộ định tuyến, không phải bách khoa

`CLAUDE.md` giữ:

- operating modes;
- lifecycle;
- quyền hạn;
- hard constraints;
- routing;
- source-of-truth precedence;
- owner-only actions.

Không nhét Story Theory, Evidence Theory, thumbnail mechanisms hay corpus findings chi tiết vào `CLAUDE.md`.

---

## A-05 — One concern, one source of truth — Một phạm vi, một nguồn chuẩn

Nếu hai file active cùng trả lời một câu hỏi bằng hai đáp án khác nhau, đó là **architecture bug**.

Không chữa bằng câu:

> “Nếu file A mâu thuẫn file B thì nghe đoạn mới hơn ở cuối file C.”

Cần sửa hoặc retire source gây drift.

`SOURCE_OF_TRUTH.md` là bản đồ authoritative cho việc này.

---

## A-06 — Schemas are the type system — Schema là hệ kiểu của Content OS

Các artifact quan trọng cần contract máy đọc được khi đáng làm:

- video state;
- version refs;
- research packet;
- claim ledger;
- review artifact;
- publish record;
- analytics snapshot;
- mechanism candidate nếu sau này cần machine validation.

Schema dùng để bắt **shape / required fields / state validity**.
Schema không chấm “story hay”.

---

## A-07 — Deterministic checks belong to machines — Lỗi xác định được giao cho máy

Máy nên bắt:

- broken path;
- stale pointer;
- schema fail;
- duplicate active source-of-truth;
- dead rule còn active ở consumer;
- narration ≠ shots;
- file version bị ghi đè;
- hard punctuation constraints;
- required owner metadata bị thiếu.

Máy **không** được quyết định:

- hook có cuốn không;
- joke có vui không;
- Causal Debt có “đủ” không;
- metaphor có đẹp không;
- video có khả năng viral không.

---

## A-08 — Dependency direction must be visible — Hướng phụ thuộc phải nhìn thấy được

Target direction:

```text
CLAUDE.md
    ↓
project-local skills
    ↓
module-owned references / templates / scripts
    ↓
shared governance / schemas / canonical knowledge
```

Không để governance phụ thuộc vào một random private implementation của writer skill.

Không để module A deep-link vào private file bên trong module B nếu B đã có public interface phù hợp.

---

## A-09 — Public API over deep links — Ưu tiên giao diện công khai thay vì móc sâu vào implementation

Nếu một agent cần Story Engine:

```yaml
skills:
  - sketchapiens-story-engine
```

ưu tiên hơn việc agent tự đọc một private reference cụ thể chỉ để lấy cùng knowledge.

Deep link chỉ dùng khi đó thực sự là contract được thiết kế công khai.

---

## A-10 — Bilingual human-facing names — Tên kỹ thuật English kèm nghĩa Việt

Identifier / filename kỹ thuật giữ English ASCII cho ổn định.

Ở tài liệu con người đọc, lần xuất hiện đầu tiên ghi:

`English technical name` — **nghĩa tiếng Việt**.

Ví dụ:

- `story-engine` — **Cỗ máy cấu trúc câu chuyện**
- `mechanism-lab.md` — **Phòng thí nghiệm cơ chế**
- `Causal Debt` — **Món nợ nhân quả**
- `Constraint Migration` — **Dịch chuyển điểm nghẽn**

Mục tiêu: owner học được thuật ngữ mà không phải nhớ mù.

---

## A-11 — Refactor and creative behavior are separate variables — Tách biến kiến trúc và biến sáng tạo

Không thay cùng lúc:

- module boundaries;
- hook philosophy;
- evidence policy;
- voice;
- review system;
- production flow

nếu không cần thiết.

Mỗi phase phải có rollback point để biết regression đến từ đâu.

---

## A-12 — History is evidence, not runtime context — Lịch sử là bằng chứng, không phải context mặc định

Rule chết, benchmark cũ, rationale lịch sử và teardown đã hết vai trò runtime phải được:

- archive;
- retire;
- hoặc load only-on-demand.

Không để Claude phải đọc luật sống + luật chết rồi tự giải conflict mỗi lần viết.

---

# 2. TARGET MODULE MODEL — MÔ HÌNH MODULE ĐÍCH

Không phải module nào dưới đây cũng phải tồn tại ngay.
Đây là **shape chuẩn khi một domain đủ lớn để tách**.

```text
.claude/skills/<module>/
├── SKILL.md             # public interface — giao diện công khai
├── README.md            # human map — bản đồ cho người đọc
├── references/          # module-owned knowledge — tri thức riêng
├── templates/           # module-owned templates — mẫu riêng
├── scripts/             # deterministic helpers — công cụ máy
└── tests/               # fixtures / smoke checks — kiểm thử
```

### Điều kiện để tạo module riêng

Một domain nên thành module khi có phần lớn các dấu hiệu:

1. có trách nhiệm nghiệp vụ riêng;
2. có workflow hoặc lifecycle riêng;
3. có knowledge đủ lớn;
4. có consumer riêng;
5. cần context isolation;
6. có thể mô tả public interface độc lập.

Nếu chưa đủ, giữ nó trong module hiện tại.

---

# 3. SHARED ROOT CONTRACT — HỢP ĐỒNG CHO THƯ MỤC DÙNG CHUNG

## `governance/` — Quản trị

Chứa:

- source of truth map;
- change policy;
- rule registry;
- retired rules;
- architecture roadmap;
- owner decisions;
- migration records.

Không chứa creative implementation của một skill cụ thể.

## `schemas/` — Hệ kiểu artifact dùng chung

Chỉ schema có consumer xuyên module / lifecycle.

## `templates/` — Mẫu dùng chung

Chỉ template có từ hai consumer độc lập hoặc là artifact contract cấp project.

## `tools/` — Công cụ xuyên module

Chỉ tool project-level hoặc cross-domain.
Tool module-specific ở trong module.

## `knowledge/` — Tri thức canonical dùng chung

Chỉ knowledge thật sự shared / canonical.
Không dùng làm kho “mọi markdown quan trọng”.

## `videos/` — Runtime/business data theo video

Mỗi video là một instance có state + artifacts + lịch sử riêng.
Không nhét knowledge canonical vào video chỉ vì nó được phát hiện ở video đó.

---

# 4. KNOWN ARCHITECTURE DEBT — NỢ KIẾN TRÚC ĐÃ BIẾT

## D-ARCH-01 — CLOSED: Writer monolith đã được tách khỏi default runtime

Phase 3 đã hoàn tất read-only audit + contract + progressive-disclosure refactor.

Current state:

- `sketchapiens-viet-kich-ban/SKILL.md` là public runtime router mỏng;
- active prose / evidence-expression / English-final references đã tách theo responsibility;
- `references/runtime-monolith-legacy.md` vẫn được giữ nguyên làm rollback/provenance;
- normal Writer không default-load legacy monolith;
- runtime smoke xác nhận prose capability không collapse sau khi detach legacy.

**Disposition:** resolved in Phase 3. Không reopen chỉ vì legacy artifact vẫn tồn tại; chỉ audit/history mode mới được mở nó.

## D-ARCH-02 — Dead rules vẫn có thể sống ở consumer

Ví dụ đã bắt trong đợt upgrade này: `I ≈ 0` chết ở rubric nhưng còn trong rule/registry.

**Risk:** một audit hoặc future refactor hồi sinh luật đã bác.

## D-ARCH-03 — Shared folders có nguy cơ thành junk drawer

`templates/`, `tools/`, `knowledge/` phải có admission rule rõ.

## D-ARCH-04 — Source-of-truth migration chưa hoàn tất

`SOURCE_OF_TRUTH.md` vẫn trỏ nhiều canonical scope vào `kho/1_luat/**`, đồng thời ghi destination migration sang `knowledge/**`.

Migration này chưa được làm đồng loạt và không được làm vội.

## D-ARCH-05 — CLOSED: Creative mechanism lifecycle đã có canonical boundary

Đã đóng trong Phase 2 bằng:

- `candidate-lifecycle.md` — status machine / promotion firewall;
- `mechanism-lab.md` — candidate data store;
- normal writer/reviewer không auto-load candidate;
- runtime smoke xác nhận candidate leakage = NONE.

Không reopen debt này chỉ vì có candidate mới; candidate mới đi qua lifecycle hiện hành.

## D-ARCH-06 — Runtime validation chưa đủ để bắt mọi documentation/architecture drift

`project_doctor.py` đã chuyển state/id ownership về schema và sửa review path, nhưng architecture linter vẫn còn scope mở cho Phase 7.

## D-ARCH-07 — CLOSED: Legacy-folder exemption đã dùng exact allowlist

Broad exemption `basename.startswith("Video")` đã bị thay trong NEXT-GUARD-01 bằng exact `LEGACY_VIDEO_DIRS` allowlist gồm đúng sáu folder lịch sử.

Current behavior:

- sáu legacy folder exact-name có thể WARN khi chưa migrate;
- `Video21_*` không còn tự được miễn;
- `check_legacy_intact()` dùng cùng allowlist;
- full `project_doctor.py` runtime đã PASS 40 · WARN 7 · FAIL 0 sau guard fix.

**Disposition:** resolved. Phase 7 vẫn có thể mở rộng linter khác, nhưng không được ghi broad `Video*` bypass như debt còn sống.

---

# 5. MASTER PHASE PLAN — KẾ HOẠCH THEO GIAI ĐOẠN

## PHASE 0 — BASELINE & FREEZE — CHỤP HIỆN TRẠNG VÀ KHÓA MỐC

**Status:** `DONE ENOUGH FOR CURRENT UPGRADE`

### Mục tiêu

Biết `main` đang là gì trước khi đổi.

### Deliverables

- map root;
- map `.claude/skills/**`;
- map `.claude/agents/**`;
- map `.claude/rules/**`;
- map governance;
- inspect recent video lifecycle;
- tạo feature branch riêng.

### Acceptance criteria

- không sửa trực tiếp `main`;
- biết base commit;
- biết source-of-truth hiện tại;
- biết các consumer chính của script constraints.

### Rollback

Xóa branch upgrade, `main` không đổi.

---

## PHASE 0.5 — ARCHITECTURE CONTRACT — KHÓA HỢP ĐỒNG KIẾN TRÚC

**Status:** `COMPLETE FOR CURRENT UPGRADE`

### Mục tiêu

Chốt cách project được phép lớn lên trước khi tiếp tục thêm module.

### Deliverables

- Architecture Contract A-01 → A-12;
- module anatomy;
- shared-root contract;
- dependency direction;
- bilingual naming convention;
- migration rules;
- Master Upgrade Plan canonical.

### Acceptance criteria

- mọi phase sau đều trỏ về file này khi quyết định placement;
- không tạo module/folder mới chỉ vì “trông professional”;
- owner duyệt architecture direction.

### Rollback

Không ảnh hưởng runtime; đây là planning/governance layer.

---

## PHASE 1 — CONSISTENCY REPAIR — SỬA LỆCH NGUỒN CHUẨN

**Status:** `COMPLETE / STABLE — checkpoint 57991d61d0cb3a4b5496951b566f73254ac9753c`

### Mục tiêu

Một constraint chỉ có một nghĩa active trên toàn runtime.

### Đã hoàn tất trên branch

- [x] `.claude/rules/script-files.md`: 4 → 3 hard constraints;
- [x] bỏ `I ≈ 0` khỏi active hard constraints;
- [x] `RULE_REGISTRY.yaml`: sửa R-HARD-01;
- [x] `RULE_REGISTRY.yaml`: sửa version semantics thành immutable versions + mutable refs;
- [x] kiểm `/audit-script`, `/apply-review`, `qa_kichban.py` — dùng 3 constraints;
- [x] writer routing/frontmatter được thay bằng compatibility wrapper theo VI-first contract;
- [x] active-vs-historical occurrences của `I ≈ 0` được phân loại; historical sample không có runtime authority;
- [x] `approved/published` semantics được đồng bộ thành immutable versions + mutable refs;
- [x] canonical review path được khóa ở `04-review/`;
- [x] lifecycle state/id pattern được giao cho `schemas/video.schema.json`;
- [x] templates và `SOURCE_OF_TRUTH.md` được đồng bộ theo active architecture.

### Acceptance criteria

- active consumers không còn conflict về hard constraints;
- active consumers không còn conflict về version/ref semantics;
- writer routing description đúng Việt-first workflow;
- historical text được đánh dấu historical, không bị hiểu là active.

### Rollback

Revert riêng Phase 1 commits, không đụng creative engine.

---

## PHASE 2 — STORY ENGINE — CỖ MÁY CẤU TRÚC CÂU CHUYỆN

**Status:** `COMPLETE / STABLE — runtime verified 2026-08-21`

### Mục tiêu

Tách structural reasoning khỏi writer monolith.

### Đã hoàn tất

- [x] tạo `sketchapiens-story-engine` — **Cỗ máy cấu trúc câu chuyện**;
- [x] khóa `CONTRACT.md` — ownership / non-ownership / input-output / dependency;
- [x] `SKILL.md` thành public interface + context router mỏng;
- [x] `README.md` song ngữ;
- [x] tách `structural-mechanisms.md`, `evidence-in-story.md`, `workflows.md` theo progressive disclosure;
- [x] `candidate-lifecycle.md` — **Vòng đời cơ chế ứng viên**;
- [x] `mechanism-lab.md` — **Phòng thí nghiệm cơ chế** chỉ giữ candidate data;
- [x] thêm / chuẩn hóa `Causal Debt` — **Món nợ nhân quả**;
- [x] `Belief Engine` — **Cỗ máy thay đổi niềm tin**;
- [x] `Domain Shift` — **Đổi miền câu chuyện**;
- [x] `Research-as-Entertainment` — **Biến nghiên cứu thành phần giải trí**;
- [x] `Original Synthesis` — **Tổng hợp nguyên bản**;
- [x] failure mode `Narrative Overreach` — **Cốt truyện chạy vượt bằng chứng**;
- [x] preload Story Engine cho `viewer-retention-judge` với minimum-context budget;
- [x] `Causal Handoff` — **Bàn giao nhân quả** vào retention audit;
- [x] retention skill cũ được thu thành sentence/paragraph craft support, không còn structural authority;
- [x] `/audit-script` và `/apply-review` consumer boundaries được audit/aligned;
- [x] smoke harness: 5 historical fixtures + 10 micro fixtures + deterministic checker;
- [x] static verification PASS;
- [x] full Claude Code `STRUCTURE_SMOKE` PASS 15/15 sau corrective rerun H-03/H-04 với full pinned input;
- [x] `REVIEWER_SMOKE` bằng actual `viewer-retention-judge` PASS 6/6;
- [x] `project_doctor.py` runtime check: PASS 40 · WARN 7 · FAIL 0 · new Phase-2 blocker 0;
- [x] candidate leakage = NONE · template forcing = NONE · Evidence boundary = PASS.

### Acceptance criteria — Kết quả

- [x] Story Engine dùng để structure/review mà không cần mở writer monolith như structural authority;
- [x] không có quota như “mỗi bài phải có N causal debts”;
- [x] candidate mechanism không bị gọi là rule;
- [x] reviewer phát hiện topic jump nhưng không tự rewrite;
- [x] valid Domain Shift/reset không bị ép thành Causal Debt;
- [x] Evidence verdict vẫn thuộc Evidence system;
- [x] V17–V20 không bị homogenize thành một skeleton.

### Verification records

- static: `.claude/skills/sketchapiens-story-engine/tests/results/phase2-verification-2026-08-21.md`;
- runtime closeout: `.claude/skills/sketchapiens-story-engine/tests/results/runtime-verification-closeout-2026-08-21.md`.

### Rollback

Gỡ skill preload + Story Engine routing; writer compatibility wrapper/legacy implementation vẫn là fallback. Final Phase-2 Git checkpoint là rollback boundary ưu tiên trước khi mở Phase 3.

---

## PHASE 3 — WRITER REFACTOR — TÁI CẤU TRÚC BỘ NÃO VIẾT

**Status:** `COMPLETE / STABLE — runtime verified 2026-08-22 — checkpoint 19c5e78f448a3308dc88845545de24eaa6b38b58`

### Mục tiêu

Biến `sketchapiens-viet-kich-ban/SKILL.md` thành orchestrator/public interface nhỏ và dễ hiểu hơn.

### Nguyên tắc đã giữ

Không đặt target “phải dưới X KB” chỉ để đẹp số.
Đích là **ít runtime conflict + progressive disclosure đúng**, không phải giảm byte bằng mọi giá.

### Đã hoàn tất

- [x] 03A read-only audit theo task chain, không refactor trong audit;
- [x] khóa Writer `CONTRACT.md` — ownership / non-ownership / input-output / dependency;
- [x] `SKILL.md` thành thin runtime router;
- [x] tách `prose-and-voice.md` làm active prose guidance;
- [x] tách `evidence-expression.md` và `english-final-rewrite.md` theo conditional loading;
- [x] tháo `runtime-monolith-legacy.md` khỏi default runtime nhưng giữ nguyên làm rollback/provenance;
- [x] Story structure route sang Story Engine; factual verdict route sang Evidence;
- [x] sync `SOURCE_OF_TRUTH.md`, `script-files.md`, `/verify-claims`, pointer trong `CLAUDE.md`;
- [x] dựng Writer regression harness: 3 historical + 12 micro fixtures;
- [x] static verification PASS;
- [x] runtime smoke lượt đầu 14 PASS / 1 REVIEW do M-W01 under-specified fixture input;
- [x] corrective rerun sửa fixture, không sửa Writer; M-W01 PASS;
- [x] final valid fixtures PASS 15/15;
- [x] legacy default-load = NO · competitor leakage = NO · D-27/dead-rule leakage = NO;
- [x] EN gate hai chiều · structure boundary · evidence boundary · cross-mode isolation · artifact safety · prose capability = PASS;
- [x] `project_doctor.py`: PASS 40 · WARN 7 · FAIL 0.

### Acceptance criteria — Kết quả

- [x] `SKILL.md` không còn active contradiction và chủ yếu làm routing/orchestration;
- [x] supporting references có ownership rõ;
- [x] Writer không tự quyết structural theory hay factual verdict;
- [x] VI-first / EN-last được bảo vệ bằng runtime gate;
- [x] bỏ legacy context không làm prose collapse thành dry fact list;
- [x] pending/dead material như D-27 không rò thành runtime requirement;
- [x] Writer implementation giữ nguyên qua corrective runtime rerun.

### Verification records

- static: `.claude/skills/sketchapiens-viet-kich-ban/tests/results/phase3b-static-verification-2026-08-22.md`;
- runtime closeout: `.claude/skills/sketchapiens-viet-kich-ban/tests/results/runtime-verification-closeout-2026-08-22.md`.

### Rollback

Stable checkpoint `19c5e78f448a3308dc88845545de24eaa6b38b58` là rollback boundary ưu tiên trước khi mở Phase 4. Legacy monolith vẫn tồn tại làm provenance/fallback nhưng không default-load.

---

## PHASE 4 — EVIDENCE ENGINE — CỖ MÁY BẰNG CHỨNG

**Status:** `PHASE 4A COMPLETE — READ-ONLY AUDIT VERIFIED; PHASE 4B GATE CLEARED — checkpoint 1b7367ea580c77b48e6fcf4b80c013d285d09c24`

### Mục tiêu

Story mạnh mà không vượt quá nguồn.

Không chỉ hỏi:

> “Fact này có đúng không?”

Mà còn phải hỏi:

> “Bằng chứng này có thật sự chứng minh đúng claim và đúng causal role — vai trò nhân quả mà story đang giao cho nó không?”

### Core boundary dự kiến

```text
SOURCE SAYS      — NGUỒN NÓI
PROJECT INFERS   — DỰ ÁN SUY RA
STORY VISUALIZES — CÂU CHUYỆN HÌNH DUNG
```

### Candidate concepts cần đánh giá, không auto-promote

- M-004 `Evidence Fit / Causal Proof Fit` — **Độ khớp bằng chứng–nhân quả**;
- taxonomy hiện hành `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE` và drift giữa các consumer;
- `SYNTHESIS` — **Tổng hợp** như một candidate derivation/category cần audit, chưa phải nhãn runtime hiện hành;
- causal bridge validation;
- claim-ledger contract;
- Narrative Overreach handoff từ Story Engine sang Evidence verdict;
- six Egypt R&D failure shapes E-01 → E-06 như test-family candidate, không phải rule.

### R&D input đã ingest trước Phase 4

Case non-runtime:

`.claude/skills/sketchapiens-story-engine/references/rd-egypt-heat-2026-08-22.md`

Index:

`.claude/skills/sketchapiens-story-engine/references/rd-case-index.md`

Egypt case được dùng để test các failure shape:

```text
E-01 correct fact, wrong causal role
E-02 interpretation → certainty inflation
E-03 real event → stronger unsupported causal story
E-04 true components → unsupported optimization synthesis
E-05 real tendency → absolute impossibility
E-06 hook compression → false universal / maximum
```

Không được dùng các label này làm requirement trước audit/validation.

### Điều kiện tạo skill riêng — Kết quả audit

04A đã chứng minh evidence domain có:

- responsibility riêng đủ rõ;
- workflow/contract riêng;
- nhiều consumer độc lập thật;
- context isolation có giá trị;
- public interface độc lập hợp lý.

**04A-G proposal:** Phase 4B nên tạo project-local `sketchapiens-evidence-engine`, nhưng giữ current prosecutor như execution/reviewer persona thay vì viết reviewer mới từ đầu.

### PHASE 4A — EVIDENCE AUDIT — KIỂM TOÁN BẰNG CHỨNG

**Status:** `COMPLETE / VERIFIED — checkpoint 1b7367ea580c77b48e6fcf4b80c013d285d09c24`

Audit artifacts:

```text
governance/audits/phase4-evidence/
├── 04A-A_inventory-runtime-surface.md
├── 04A-B_responsibility-decomposition.md
├── 04A-C_authority-source-of-truth.md
├── 04A-D_claim-ledger-taxonomy-audit.md
├── 04A-E_consumer-dependency-audit.md
├── 04A-F_evidence-fit-failure-mode-audit.md
├── 04A-G_evidence-contract-proposal.md
└── 04A-H_audit-closeout.md
```

### 04A major conclusions

- Evidence runtime không đổi trong audit;
- bốn top-level verdict hiện hành được giữ làm baseline:
  `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE`;
- `SYNTHESIS` chưa được nâng thành verdict thứ năm; audit nghiêng về derivation mode của `INFERENCE`;
- M-004 chưa promote;
- gap thật là relation-level verdict: các fact node có thể đúng nhưng narrative edge không được support;
- current Evidence Prosecutor đã mạnh và nên được contract hóa/nâng cấp, không thay bỏ;
- ledger hiện thiếu representation sạch cho multi-source dependency/bridge/synthesis;
- `overreach 0–3` đang trộn severity với failure type;
- schema claim-ledger tồn tại nhưng project doctor chưa validate ledger artifact thật against schema;
- `preflight.py` vẫn kiểm thế hệ cũ `MONEO_* + >=3 citation-shaped strings`, lệch new lifecycle `02-research/claim-ledger.md`;
- legacy V17–V20 Evidence artifacts nên là regression corpus, không phải migration blocker.

### PHASE 4B — EVIDENCE IMPLEMENTATION — TRIỂN KHAI SAU AUDIT

**Status:** `GATE CLEARED — NOT STARTED`

Task chain đã được audit đề xuất:

```text
04B-A — Lock Evidence Contract + create module skeleton
04B-B — Canonical semantics + minimal ledger/schema representation
04B-C — Causal Proof Fit / bridge verdict behavior
04B-D — Refactor prosecutor + verify-claims around public interface
04B-E — Consumer / Source-of-Truth / preflight integration
04B-F — Regression harness
04B-G — Target-runtime semantic smoke + project doctor
04B-H — Runtime closeout + stable checkpoint
```

### Important split

04B-B và 04B-C phải là hai change units riêng:

- B = artifact/taxonomy representation;
- C = relation-level bridge reasoning behavior.

Không trộn để nếu regression xảy ra còn biết do schema hay reasoning behavior.

### Acceptance criteria của toàn Phase 4

- causal bridge lớn có evidence boundary rõ;
- reviewer evidence không chấm retention;
- synthesis được phép nhưng không giả thành direct fact;
- source resemblance không được dùng thay causal proof;
- Writer chỉ diễn đạt verdict đã có, không tự phán support;
- Story Engine flag Narrative Overreach nhưng Evidence system sở hữu verdict;
- evidence candidate/R&D không rò thành Writer requirement;
- runtime smoke chứng minh boundary hai chiều, không chỉ docs đẹp.

---

## PHASE 5 — AGENT ARCHITECTURE — KIẾN TRÚC GIÁM KHẢO

**Status:** `PLANNED`

### Mục tiêu

Mỗi reviewer chỉ nhận context nó cần.

### Agent boundaries

- retention judge → audience/story surface;
- evidence prosecutor → claim/evidence surface;
- anti-AI critic → prose surface;
- external ChatGPT review → cold-ish outside layer.

### Nguyên tắc

- preload skill theo nhiệm vụ;
- không cho tất cả agent đọc toàn bộ knowledge;
- agent review chỉ đề nghị, không tự sửa;
- editor duy nhất tạo version mới sau owner classification.

### Acceptance criteria

- dependency của từng agent nhìn thấy được;
- không duplicate cùng rubric ở nhiều agent;
- một agent không vô tình làm nhiệm vụ của agent khác.

---

## PHASE 6 — MECHANISM R&D — R&D CƠ CHẾ

**Status:** `STARTED / CONTINUOUS`

### Mục tiêu

Project học thêm mà không tích lũy rule rác.

### Current candidates

- M-001 `Solution Ladder` — **Bậc thang giải pháp**;
- M-002 `Constraint Migration` — **Dịch chuyển điểm nghẽn**;
- M-003 `Scale-Out Escalation` — **Leo thang bằng mở rộng quy mô**;
- M-004 `Evidence Fit / Causal Proof Fit` — **Độ khớp bằng chứng–nhân quả**.

### R&D case mới đã ingest 22/08/2026

- `rd-egypt-heat-2026-08-22.md` — deep case study non-runtime;
- `rd-case-index.md` — R&D index;
- Egypt bổ sung supporting/distinction evidence cho M-001/M-002/M-003/M-004;
- `Unifying Equation`, `Invisible Achievement Reframe`, `Threat Recruitment` vẫn chỉ là observation, chưa candidate;
- không mechanism nào được promote từ Egypt case.

### Promotion pipeline

```text
observe
→ name candidate
→ find supporting cases
→ find counterexamples
→ define failure mode
→ test on Sketchapiens
→ owner decision
→ promote / merge / demote / delete
```

### Acceptance criteria

- không mechanism nào tự promote;
- mỗi candidate có counterexample search;
- merge terminology khi hai mechanism hóa ra là cùng một thứ;
- delete vẫn để tombstone/history để project không phát minh lại.

---

## PHASE 7 — RUNTIME & GUARDRAILS — MÁY KIỂM VÀ HÀNG RÀO

**Status:** `PLANNED`

### Mục tiêu

Biến `project_doctor.py` và related tools thành content-architecture linter có phạm vi rõ.

### Candidate deterministic checks

- stale active rule scan;
- broken file references;
- invalid version refs;
- owner metadata missing;
- duplicate canonical mappings;
- schema validation;
- narration/shot mismatch;
- generated-file integrity;
- path casing / naming contract khi có ích;
- legacy-folder allowlist thay cho broad `Video*` prefix exemption.

### Không được làm

- “retention score” bằng regex;
- “Causal Debt score”;
- “viral probability”;
- sửa prose tự động để đạt metric.

### Acceptance criteria

Một command có thể nói:

```text
architecture: PASS/FAIL
governance refs: PASS/FAIL
artifact schemas: PASS/FAIL
production integrity: PASS/FAIL
```

mà không giả vờ chấm chất lượng sáng tạo.

---

## PHASE 8 — V21 CANARY — VIDEO THỬ NGHIỆM CÓ KIỂM SOÁT

**Status:** `PLANNED`

### Mục tiêu

Dùng V21 để kiểm architecture mới trên một sản phẩm thật.

### Canary flow dự kiến

```text
TOPIC
→ RESEARCH
→ STRUCTURE (Story Engine)
→ DRAFT VI
→ INTERNAL AUDIT
→ OWNER CLASSIFICATION
→ REVISE
→ APPROVE VI
→ TRANSLATE EN ONCE
→ PRODUCTION
→ PUBLISH
→ ANALYTICS
→ POSTMORTEM
```

### Điều quan trọng

Không dùng V21 để đồng thời thử 12 rule sáng tạo mới.

Ghi rõ:

- behavior nào là baseline;
- behavior nào do Story Engine mới;
- candidate mechanism nào chỉ được quan sát;
- bất kỳ manual override nào.

### Acceptance criteria

- lifecycle chạy trọn mà không cần phá architecture giữa chừng;
- không source drift mới;
- owner hiểu artifact nằm đâu;
- reviewer/skills không tự tranh quyền;
- production vẫn tương thích.

---

## PHASE 9 — POSTMORTEM & PROMOTION — HẬU KIỂM VÀ THĂNG CẤP

**Status:** `PLANNED`

### Mục tiêu

Học từ V21 nhưng không overfit vào một video.

### Review sau V21

- mechanism nào giúp thật;
- mechanism nào tạo câu giả;
- module nào thiếu context;
- module nào load thừa;
- reviewer nào duplicate;
- evidence bridge nào suýt overreach;
- architecture friction nào xuất hiện;
- runtime check nào đáng automate.

### Promotion rule

Một video thành công **không đủ** để promote mechanism thành channel rule.

---

## PHASE 10 — CLEANUP & CONSOLIDATION — DỌN NỢ VÀ HỢP NHẤT

**Status:** `PLANNED`

### Mục tiêu

Chỉ sau khi architecture mới chạy thật mới dọn mạnh.

### Candidate cleanup

- archive dead sections của writer;
- retire duplicate source files;
- update `SOURCE_OF_TRUTH.md` sau migration thật;
- move truly shared knowledge vào `knowledge/**`;
- move module-specific tools/templates về owner module;
- remove obsolete routing;
- write migration notes.

### Acceptance criteria

Không còn pattern:

> “phần mới thắng phần cũ ở cùng file”

trong runtime-critical modules.

---

# 6. TARGET DEPENDENCY MAP — BẢN ĐỒ PHỤ THUỘC ĐÍCH

```text
                         OWNER
                           │
                           ▼
                      CLAUDE.md
                  control plane/router
                           │
          ┌────────────────┼─────────────────┐
          ▼                ▼                 ▼
      WRITER SKILL     STORY ENGINE      REVIEW SKILLS
          │                │                 │
          │                └──────┐          │
          ▼                       ▼          ▼
 module-owned refs          shared contracts / governance
          │                       ▲
          └───────────────────────┘

VIDEOS = runtime instances
ANALYTICS = observed outcomes
MECHANISM LAB = experiment registry, NOT rules
RULE_REGISTRY = promoted active rules only
```

### Cấm dependency smell

- governance → private writer reference;
- Story Engine → competitor corpus during write mode;
- reviewer → random historical archive;
- video artifact → trở thành canonical rule chỉ vì nó ở video mới nhất;
- `CLAUDE.md` → chứa implementation dài của mọi module.

---

# 7. CHANGE UNIT — ĐƠN VỊ THAY ĐỔI

Mỗi PR/upgrade slice nên cố gắng trả lời **một câu hỏi chính**.

Ví dụ tốt:

> “Repair active script constraints and introduce Story Engine as a separate module.”

Ví dụ xấu:

> “Refactor writer + change thumbnail system + migrate all knowledge + rewrite agents + add analytics.”

### Mỗi slice cần

1. before state;
2. intended change;
3. files touched;
4. acceptance criteria;
5. regression check;
6. rollback path.

---

# 8. FILES / AREAS KHÔNG ĐƯỢC ĐỤNG VỘI

Trong đợt V21 architecture upgrade, mặc định **không đại phẫu** các vùng sau nếu phase chưa tới:

- `identity/style.py` — visual source of truth;
- production-generated artifacts của V20;
- approved/published historical artifacts;
- corpus raw transcripts;
- toàn bộ `knowledge/**` migration một lượt;
- writer monolith trước khi Phase 1–2 ổn;
- YouTube policy rules không liên quan architecture;
- thumbnail system nếu không phải dependency trực tiếp.

---

# 9. CURRENT BRANCH STATE — TRẠNG THÁI BRANCH HIỆN TẠI

Branch: `upgrade/story-engine-v21`

Các nhóm thay đổi đã hoàn tất tới Phase-4A closeout:

1. **Consistency Repair — Sửa lệch:** Phase 1 complete/stable.
2. **Story Engine — Cỗ máy cấu trúc:** Phase 2 complete/stable, runtime verified.
3. **Writer Refactor — Bộ não viết:** Phase 3 complete/stable, runtime verified 15/15.
4. **Context Architecture — Kiến trúc ngữ cảnh:** Story + Writer progressive disclosure đã runtime-smoke.
5. **Candidate Isolation — Cách ly ứng viên:** lifecycle + firewall + Mechanism Lab data boundary.
6. **Evidence R&D ingestion:** Egypt heat case đã vào non-runtime R&D; không mechanism nào được promote.
7. **Evidence Audit — Phase 4A:** 8 audit tasks complete; Evidence runtime unchanged; 04B module proposal + gate cleared.
8. **Runtime Guard Debt:** NEXT-GUARD-01 exact legacy allowlist đã hoàn tất; preflight Evidence generation drift mới được 04A phát hiện và chưa sửa.
9. **Bilingual naming — Tên song ngữ:** technical English + nghĩa Việt ở human-facing docs.

`main` chưa bị thay đổi bởi upgrade branch.

Phase 4B **chưa bắt đầu implementation**.

---

# 10. NEXT ACTIONS — VIỆC TIẾP THEO THEO ĐÚNG THỨ TỰ

## NEXT-01 — COMPLETE: Phase 1 Consistency Repair

Checkpoint canonical:

`57991d61d0cb3a4b5496951b566f73254ac9753c`

Không reopen Phase 1 trừ khi phát hiện active contradiction mới.

## NEXT-02 — COMPLETE: Stabilize Story Engine

Đã hoàn tất theo task chain:

```text
02A Audit
→ 02B Contract
→ 02C Progressive Disclosure
→ 02D Candidate Isolation
→ 02E Smoke Fixtures
→ 02F Consumer Audit
→ 02G Static + Runtime Verification
→ 02H Closeout
```

Phase-2 acceptance đã được xác minh bằng target runtime, không chỉ bằng docs.

## NEXT-GUARD-01 — COMPLETE: exact legacy allowlist

Broad `Video*` prefix exemption đã bị thay bằng exact historical allowlist.

Final guard checkpoint:

`37b65242b2a163bd9ccff42230ea79d2867168b4`

Không reopen trừ khi exact allowlist behavior regression.

## NEXT-03A / 03B — COMPLETE: Writer Refactor

Read-only audit → contract → thin router → legacy detachment → integration → smoke harness → runtime verification.

Final stable checkpoint:

`19c5e78f448a3308dc88845545de24eaa6b38b58`

## NEXT-RD-EGYPT — COMPLETE: non-runtime R&D ingestion

Egypt heat case đã ingest làm supporting/distinction case + future Evidence benchmark.

Checkpoint:

`bedbf2f9e22d01719dfb92d151d194ca71c1f8b4`

Không rule/mechanism nào được promote.

## NEXT-04A — COMPLETE: Evidence Audit

Đã chạy:

```text
04A-A Inventory & Runtime Surface
→ 04A-B Responsibility Decomposition
→ 04A-C Authority & Source-of-Truth Audit
→ 04A-D Claim Ledger & Taxonomy Audit
→ 04A-E Consumer & Dependency Audit
→ 04A-F Evidence Fit Failure-Mode Audit
→ 04A-G Evidence Contract Proposal
→ 04A-H Audit Verification & Checkpoint
```

Final checkpoint:

`1b7367ea580c77b48e6fcf4b80c013d285d09c24`

## NEXT-04B — Evidence Implementation — CHƯA BẮT ĐẦU

Chỉ bắt đầu sau checkpoint 04A và vẫn theo:

```text
PHASE → TASK → CHECK → CHECKPOINT
```

Task đầu:

```text
04B-A — Lock Evidence Contract + create module skeleton
```

Không được nhảy thẳng sang sửa schema/prosecutor trước contract.

---

# 11. DEFINITION OF DONE — ĐỊNH NGHĨA HOÀN THÀNH TOÀN ĐỢT

Đợt upgrade được coi là hoàn thành khi:

- [ ] mỗi phạm vi runtime-critical có một source of truth rõ;
- [x] `CLAUDE.md` vẫn mỏng và đóng vai router/control plane;
- [x] Story Engine có public interface rõ;
- [x] Writer có public interface rõ và runtime không default-load legacy monolith;
- [ ] Evidence Engine có public interface rõ và runtime verified;
- [ ] module-specific knowledge/tools/templates được owner module giữ;
- [x] shared folders có admission rule ở Architecture Contract;
- [x] writer không còn phải tự giải active-vs-dead contradictions trong implementation legacy;
- [x] Story Engine dùng được mà không biến thành checklist;
- [x] evidence boundary chống Narrative Overreach hoạt động ở Story Engine/reviewer boundary;
- [x] reviewer responsibilities của Phase-2 consumer path không chồng nhau;
- [ ] deterministic architecture/artifact errors có machine checks hợp lý toàn project;
- [ ] V21 chạy end-to-end trên architecture mới;
- [x] postmortem/candidate path không auto-create rules;
- [ ] owner có thể nhìn toàn cây repo và giải thích “thứ này thuộc module nào, vì sao”.

---

# 12. DECISION LOG — NHẬT KÝ QUYẾT ĐỊNH KIẾN TRÚC

## 2026-08-21 — D-ARCH-A

**Decision:** `CLAUDE.md` là router/control plane, không chứa Story Engine theory.  
**Reason:** giảm always-on context và giữ separation of concerns.

## 2026-08-21 — D-ARCH-B

**Decision:** Story Engine thành project-local skill riêng.  
**Reason:** có responsibility, consumer và context boundary đủ rõ để thành module.

## 2026-08-21 — D-ARCH-C

**Decision:** Mechanism candidates nằm trong Mechanism Lab, không vào Rule Registry.  
**Reason:** tuân `CHANGE_POLICY.md`; chưa đủ bằng chứng để promote.

## 2026-08-21 — D-ARCH-D

**Decision:** học architecture pattern từ Minimal-v6 nhưng không copy folder names của Next.js.  
**Adopt:** module ownership · public interface · local-vs-shared · strong contracts · deterministic checks · dependency direction.  
**Reject:** tạo `src/components/hooks/utils` chỉ để giống software project.

## 2026-08-21 — D-ARCH-E

**Decision:** technical English identifier giữ nguyên; human-facing docs ghi English + nghĩa Việt.  
**Reason:** vừa ổn định tooling vừa giúp owner học terminology lâu dài.

## 2026-08-21 — D-ARCH-F

**Decision:** Story Engine chỉ được gọi `COMPLETE / STABLE` sau khi **static verification + semantic target-runtime smoke + project doctor** cùng pass.  
**Reason:** architecture nhìn đúng trên giấy không đủ chứng minh behavior runtime không ép template hoặc rò candidate.

## 2026-08-21 — D-ARCH-G

**Decision:** smoke failure có ba nguồn riêng: `ENGINE DEFECT` · `FIXTURE DEFECT` · `EXECUTION FAULT`. Corrective rerun phải dùng full input + clean diagnosis context nếu prior evaluator đã thấy expectation.  
**Reason:** H-03/H-04 từng tạo fail/review giả chỉ vì input bị cắt; engine không được tune để chữa lỗi execution.

## 2026-08-22 — D-ARCH-H

**Decision:** Writer thành public module contract + thin router; legacy monolith giữ provenance nhưng không default-load.  
**Reason:** audit Phase 3 cho thấy public wrapper mỏng nhưng runtime context vẫn bị legacy implementation chi phối; progressive disclosure giảm conflict mà không đổi creative behavior.

## 2026-08-22 — D-ARCH-I

**Decision:** Evidence Phase 4 phải bắt đầu bằng read-only audit; không thêm `SYNTHESIS` thành verdict chỉ vì Story Engine dùng khái niệm synthesis.  
**Reason:** runtime hiện có four-label taxonomy; cần audit semantics và consumer trước khi migration.

## 2026-08-22 — D-ARCH-J

**Decision proposal after 04A:** Evidence domain đủ điều kiện thành project-local `sketchapiens-evidence-engine` trong Phase 4B.  
**Reason:** audit chứng minh responsibility/workflow/knowledge/multiple consumers/context isolation/public API need độc lập. Current Evidence Prosecutor được giữ làm execution/reviewer persona, không thay bằng reviewer mới.

## 2026-08-22 — D-ARCH-K

**Decision proposal after 04A:** `SYNTHESIS` không phải top-level fifth Evidence verdict theo audit hiện tại; ưu tiên xem nó là derivation mode của `INFERENCE` nếu 04B tests xác nhận.  
**Reason:** factual relation với evidence và cách claim được dẫn xuất là hai dimension khác nhau.

---

# 13. NGUYÊN TẮC CUỐI

> **The project does not accumulate rules. It accumulates tested understanding.**  
> **Dự án không tích lũy luật. Dự án tích lũy hiểu biết đã được kiểm nghiệm.**

Và ở tầng kiến trúc:

> **The project does not accumulate folders. It accumulates clear ownership.**  
> **Dự án không tích lũy thư mục. Dự án tích lũy ranh giới sở hữu rõ ràng.**

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

## D-ARCH-01 — Writer skill quá lớn

`sketchapiens-viet-kich-ban/SKILL.md` đang gánh quá nhiều vai trò: public interface + implementation + history + overrides + old rules.

**Risk:** context pollution, self-conflict, hard-to-test changes.

## D-ARCH-02 — Dead rules vẫn có thể sống ở consumer

Ví dụ đã bắt trong đợt upgrade này: `I ≈ 0` chết ở rubric nhưng còn trong rule/registry.

**Risk:** một audit hoặc future refactor hồi sinh luật đã bác.

## D-ARCH-03 — Shared folders có nguy cơ thành junk drawer

`templates/`, `tools/`, `knowledge/` phải có admission rule rõ.

## D-ARCH-04 — Source-of-truth migration chưa hoàn tất

`SOURCE_OF_TRUTH.md` vẫn trỏ nhiều canonical scope vào `kho/1_luat/**`, đồng thời ghi destination migration sang `knowledge/**`.

Migration này chưa được làm đồng loạt và không được làm vội.

## D-ARCH-05 — Creative mechanisms chưa có lifecycle R&D rõ trong runtime

Đã bắt đầu chữa bằng `mechanism-lab.md`, nhưng cần quy trình test → promotion/demotion có dấu vết.

## D-ARCH-06 — Runtime validation chưa đủ để bắt documentation drift

`project_doctor.py` cần phát triển thành architecture linter, nhưng chỉ bắt thứ deterministic.

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

**Status:** `IN PROGRESS — FILE NÀY LÀ DELIVERABLE CHÍNH`

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

**Status:** `IN PROGRESS`

### Mục tiêu

Một constraint chỉ có một nghĩa active trên toàn runtime.

### Đã làm trên branch

- [x] `.claude/rules/script-files.md`: 4 → 3 hard constraints;
- [x] bỏ `I ≈ 0` khỏi active hard constraints;
- [x] `RULE_REGISTRY.yaml`: sửa R-HARD-01;
- [x] `RULE_REGISTRY.yaml`: sửa version semantics thành immutable versions + mutable refs;
- [x] kiểm `/audit-script`, `/apply-review`, `qa_kichban.py` — đã dùng 3 constraints;
- [x] thêm bilingual Story Engine routing note vào script rule.

### Còn làm

- [ ] sửa frontmatter `sketchapiens-viet-kich-ban` từ English-first / 2-column / 8–25m sang contract hiện hành;
- [ ] grep/search toàn project cho `I ≈ 0`, `four hard constraints`, `4 ràng buộc cứng` và phân loại historical vs active;
- [ ] rà `approved.md` / `published.md` terminology cũ;
- [ ] rà các duplicate lifecycle paths;
- [ ] ghi migration note nếu có source active được retire.

### Acceptance criteria

- active consumers không còn conflict về hard constraints;
- active consumers không còn conflict về version/ref semantics;
- writer routing description đúng Việt-first workflow;
- historical text được đánh dấu historical, không bị hiểu là active.

### Rollback

Revert riêng Phase 1 commits, không đụng creative engine.

---

## PHASE 2 — STORY ENGINE — CỖ MÁY CẤU TRÚC CÂU CHUYỆN

**Status:** `IN PROGRESS`

### Mục tiêu

Tách structural reasoning khỏi writer monolith.

### Đã làm

- [x] tạo `sketchapiens-story-engine` — **Cỗ máy cấu trúc câu chuyện**;
- [x] `SKILL.md` public interface + core framework;
- [x] `README.md` song ngữ;
- [x] `mechanism-lab.md` — **Phòng thí nghiệm cơ chế**;
- [x] thêm `Causal Debt` — **Món nợ nhân quả**;
- [x] thêm `Belief Engine` — **Cỗ máy thay đổi niềm tin**;
- [x] thêm `Domain Shift` — **Đổi miền câu chuyện**;
- [x] thêm `Research-as-Entertainment` — **Biến nghiên cứu thành phần giải trí**;
- [x] thêm `Original Synthesis` — **Tổng hợp nguyên bản**;
- [x] thêm failure mode `Narrative Overreach` — **Cốt truyện chạy vượt bằng chứng**;
- [x] preload Story Engine cho `viewer-retention-judge`;
- [x] thêm `Causal Handoff` — **Bàn giao nhân quả** vào retention audit.

### Còn làm

- [ ] xác định phần nào của 455-line SKILL là public interface, phần nào nên tách reference;
- [ ] không tách nhỏ quá sớm nếu chưa có lợi ích load/context rõ;
- [ ] thêm smoke fixtures từ V17–V20 để kiểm engine không ép template;
- [ ] xác nhận agent preload không kéo Mechanism Lab candidate vào review như rule.

### Acceptance criteria

- Story Engine có thể dùng để structure/review mà không cần mở writer monolith;
- không có quota như “mỗi bài phải có N causal debts”;
- candidate mechanism không bị gọi là rule;
- reviewer phát hiện topic jump nhưng không tự rewrite.

### Rollback

Gỡ skill preload + Story Engine routing; writer cũ vẫn hoạt động.

---

## PHASE 3 — WRITER REFACTOR — TÁI CẤU TRÚC BỘ NÃO VIẾT

**Status:** `PLANNED — DO NOT START UNTIL PHASE 1–2 STABLE`

### Mục tiêu

Biến `sketchapiens-viet-kich-ban/SKILL.md` thành orchestrator/public interface nhỏ và dễ hiểu hơn.

### Nguyên tắc

Không đặt target “phải dưới X KB” chỉ để đẹp số.
Đích là **ít runtime conflict + progressive disclosure đúng**, không phải giảm byte bằng mọi giá.

### Dự kiến tách theo responsibility

- workflow / input-output contract;
- active niche principles;
- voice/register;
- evidence writing interface;
- research routing;
- metadata routing;
- historical/dead material → archive/on-demand.

### Không làm

- không rewrite toàn bộ copy trong một commit;
- không thay creative philosophy cùng lúc;
- không xóa rationale lịch sử nếu chưa có archive path.

### Acceptance criteria

- `SKILL.md` đọc từ đầu tới cuối không chứa active contradiction;
- file chính chủ yếu làm routing/orchestration;
- supporting references có ownership rõ;
- V17–V20 smoke review không cho thấy regression rõ do missing context.

### Rollback

Giữ snapshot trước refactor; có thể quay writer về monolith mà Story Engine vẫn độc lập.

---

## PHASE 4 — EVIDENCE ENGINE — CỖ MÁY BẰNG CHỨNG

**Status:** `PLANNED`

### Mục tiêu

Story mạnh mà không vượt quá nguồn.

### Core boundary dự kiến

```text
SOURCE SAYS      — NGUỒN NÓI
PROJECT INFERS   — DỰ ÁN SUY RA
STORY VISUALIZES — CÂU CHUYỆN HÌNH DUNG
```

### Candidate concepts cần đánh giá

- `Evidence Fit` — **Độ khớp bằng chứng–nhân quả**;
- DIRECT / INFERENCE / SYNTHESIS / STORY DEVICE taxonomy;
- bridge validation;
- claim ledger contract.

### Điều kiện tạo skill riêng

Chỉ tách `sketchapiens-evidence-engine` nếu evidence workflow đủ độc lập và có nhiều consumer.
Nếu chưa đủ, giữ trong skill/reviewer hiện tại.

### Acceptance criteria

- causal bridge lớn có evidence boundary rõ;
- reviewer evidence không chấm retention;
- synthesis được phép nhưng không giả thành direct fact;
- source resemblance không được dùng thay causal proof.

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
- path casing / naming contract khi có ích.

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

Các nhóm thay đổi đã thực hiện trước khi file plan này được tạo:

1. **Consistency repair — sửa lệch:** script rule + rule registry.
2. **Story Engine — Cỗ máy cấu trúc:** skill mới.
3. **Mechanism Lab — Phòng thí nghiệm cơ chế:** candidate R&D.
4. **Retention integration — tích hợp giữ chân:** reviewer preload + causal handoff.
5. **Bilingual naming — tên song ngữ:** README + convention trong module.

`main` chưa bị thay đổi bởi upgrade branch.

---

# 10. NEXT ACTIONS — VIỆC TIẾP THEO THEO ĐÚNG THỨ TỰ

## NEXT-01 — Hoàn tất Phase 1

1. sửa writer skill frontmatter;
2. scan active/historical occurrences của luật chết;
3. scan version/ref terminology;
4. ghi rõ những occurrence được giữ vì historical evidence.

## NEXT-02 — Stabilize Story Engine

1. audit 455-line `SKILL.md` theo public-interface rule;
2. chỉ tách reference nếu giảm context coupling thật;
3. thêm 2–4 smoke fixtures từ V17–V20;
4. kiểm retention agent không load candidate như canonical rule.

## NEXT-03 — Architecture validation before Writer Refactor

Tạo một architecture review ngắn:

- module boundaries đúng chưa;
- shared/local placement đúng chưa;
- dependency inversion có smell không;
- duplicate source-of-truth còn gì.

## NEXT-04 — Chỉ sau đó mới bắt đầu Phase 3 Writer Refactor

Không nhảy trước.

---

# 11. DEFINITION OF DONE — ĐỊNH NGHĨA HOÀN THÀNH TOÀN ĐỢT

Đợt upgrade được coi là hoàn thành khi:

- [ ] mỗi phạm vi runtime-critical có một source of truth rõ;
- [ ] `CLAUDE.md` vẫn mỏng và đóng vai router/control plane;
- [ ] major skills có public interface rõ;
- [ ] module-specific knowledge/tools/templates được owner module giữ;
- [ ] shared folders có admission rule;
- [ ] writer không còn phải tự giải active-vs-dead contradictions;
- [ ] Story Engine dùng được mà không biến thành checklist;
- [ ] evidence boundary chống narrative overreach hoạt động;
- [ ] reviewer responsibilities không chồng nhau;
- [ ] deterministic architecture/artifact errors có machine checks hợp lý;
- [ ] V21 chạy end-to-end trên architecture mới;
- [ ] postmortem tạo candidate/proposal chứ không auto-create rules;
- [ ] owner có thể nhìn cây repo và giải thích “thứ này thuộc module nào, vì sao”.

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

---

# 13. NGUYÊN TẮC CUỐI

> **The project does not accumulate rules. It accumulates tested understanding.**  
> **Dự án không tích lũy luật. Dự án tích lũy hiểu biết đã được kiểm nghiệm.**

Và ở tầng kiến trúc:

> **The project does not accumulate folders. It accumulates clear ownership.**  
> **Dự án không tích lũy thư mục. Dự án tích lũy ranh giới sở hữu rõ ràng.**

# PRODUCTION ARCHITECTURE UPGRADE v2 — PROPOSAL

*Nghiên cứu và đề xuất. **Không triển khai bất cứ thành phần nào.** Không sửa v1.*
*Lập 2026-08-06. Nhãn bằng chứng: **OFFICIAL FACT** · **PROJECT EVIDENCE** · **ARCHITECTURE INFERENCE** · **UNKNOWN**.*

---

## 1. Executive Recommendation

### Option được chọn: **A+ — Minimal Safety Upgrade, mở rộng có kiểm soát**

**Không** chọn Option B, dù v1 nghiêng về hướng đó.

**Lý do, bằng bằng chứng:**

1. **Rủi ro số một của audit vẫn chưa được gỡ.** Control plane v1 đã cài chỉ bảo vệ **chính nó**. 19 thư mục video, 79 file gốc và toàn bộ narration vẫn nằm ngoài git *(PROJECT EVIDENCE: `governance/INSTALL_REPORT.md` §9 W2)*. Kiến trúc phức tạp hơn không sửa được điều đó; **một lệnh `git add` trên vài MB text thì sửa được.**

2. **Cơ chế override của v1 không hoạt động như v1 giả định.** Tài liệu chính thức nói **personal skills đè project skills**, không phải ngược lại, và **project settings không thể tắt skill hay subagent ở user scope** *(OFFICIAL FACT, §4)*. Toàn bộ chiến lược "project-local thắng predecessor global" của v1 chỉ là **luật bằng chữ**, không có cưỡng chế.

3. **Quy mô không khớp.** Kênh đang ở **367 hiển thị / 5 ngày**, ~531 view tổng, 7 sub, chưa bật kiếm tiền, một video tại một thời điểm *(PROJECT EVIDENCE: audit §14)*. v1 đề ra 5 agent + 6 skill + 6 rule + 4 schema + 6 template + 9 thư mục knowledge + cây videos đầy đủ. **Chi phí vận hành vượt giá trị tạo ra ở quy mô này** — và chính audit đã chỉ ra rằng **18 mâu thuẫn sinh ra vì có quá nhiều tài liệu**, không phải quá ít.

4. **Nút thắt thật không phải kiến trúc.** Audit chẩn đoán bệnh A: YouTube chưa phân phối. Không kiến trúc thư mục nào chữa được bệnh đó. Kiến trúc chỉ nên làm đúng ba việc: **không mất dữ liệu · không xuất bản thứ sai · học được từ số liệu thật.**

### 10 thay đổi quan trọng nhất so với v1

| # | Thay đổi | Vì sao |
|---|---|---|
| **1** | **Git bao phủ toàn bộ text của dự án ngay ở Phase 0**, không chỉ control plane | R1 vẫn hở. Media đã bị `.gitignore`; text chỉ vài MB |
| **2** | **5 agent → 3 agent.** Gộp `retention-architect` + `promise-payoff-judge` thành `structure-judge`; hạ `anti-ai-narration-critic` xuống **skill** | Chỉ tạo agent khi **context độc lập** có giá trị thật. Anti-AI critic đọc đúng cùng một file mà main session đã có → isolation bằng 0 |
| **3** | **Bỏ giả định "project override global skill".** Ghi rõ đây là **luật bằng chữ**, và nêu ba cách xử lý thật | OFFICIAL FACT: personal đè project; project settings không tắt được user skill |
| **4** | **Luật sống-còn phải nằm trong `CLAUDE.md`, không chỉ trong `.claude/rules/`** | OFFICIAL FACT: path-scoped rules **không được nạp lại sau `/compact`**, và chỉ kích hoạt khi Claude **đọc** file khớp |
| **5** | **Bỏ migration V01–V19.** Thay bằng **một file index** trỏ tới thư mục cũ | v1 Phase 4 bắt map 19 video. Chi phí lớn, giá trị bằng 0 cho video sắp làm |
| **6** | **`permissions.deny` là biên giới thật, hook là lớp thứ hai** | OFFICIAL FACT: settings được client cưỡng chế; `CLAUDE.md` "không phải lớp cưỡng chế cứng"; hook `exit 1` **không** chặn, chỉ `exit 2` |
| **7** | **Analytics khởi động bằng MỘT file CSV nhập tay**, không phải schema JSON đầy đủ | Vòng phản hồi đứt vì **không có dữ liệu**, không phải vì thiếu schema |
| **8** | **Bỏ cây `knowledge/**` 9 thư mục.** Giữ tài liệu tại chỗ + một registry trỏ đường | Di chuyển 79 file làm gãy mọi tham chiếu, trong khi 4 mâu thuẫn nội dung **vẫn chưa được quyết** |
| **9** | **Corpus: `permissions.deny` trước, chuyển thư mục sau** | Deny là biên giới client cưỡng chế được ngay; chuyển thư mục cần quyết định D-15 |
| **10** | **Agent Teams: KEEP nguyên khuyến nghị "không dùng hằng ngày"** — nhưng ghi rõ nó **experimental, tắt mặc định, cần biến môi trường** | OFFICIAL FACT. v1 nói đúng nhưng không nêu trạng thái |

---

## 2. Inputs Reviewed

| Loại | Đường dẫn chính xác | Trạng thái đọc | md5 |
|---|---|---|---|
| **Audit** | `/Users/admin/Claude/Projects/Build Channel Người Que Cổ Đại/PROJECT_FULL_AUDIT_EXPORT.md` | **đọc đầy đủ** (1.449 dòng) | `4cdf65496438c6f832e91ac8e9f71bdd` |
| **Architecture v1** | `/Users/admin/Downloads/Sketchapiens_Architecture_Upgrade_v1.md` | **đọc đầy đủ** (316 dòng) | `83776aa150c2ddd7dc567aea801b10cc` |

*md5 đo lại lúc kết thúc: khớp nguyên. Cả hai file mtime 2026-08-06 22:02 và 22:28 — đều trước nhiệm vụ này, không bị sửa.*

> ⚠️ **Phát hiện Phase 0: file v1 KHÔNG nằm trong project.** `grep -rl "PRODUCTION ARCHITECTURE UPGRADE"` trên toàn project trả về **rỗng**. File nằm ở `~/Downloads/`. Tiêu đề bên trong là `# SKETCHAPIENS — PRODUCTION ARCHITECTURE UPGRADE v1`, không khớp tên file `Sketchapiens_Architecture_Upgrade_v1.md` — đúng lý do đề bài dặn *"không dựa vào tên file để đoán nội dung"*.

**File canonical đã lấy mẫu để kiểm chứng quyết định cụ thể trong v1** *(không đọc lại toàn bộ)*:

| File | Kiểm chứng điều gì |
|---|---|
| `governance/INSTALL_REPORT.md` | v1 đã được cài tới đâu, còn hở gì |
| `.claude/settings.json` · `.claude/hooks/guard_project.py` | hook và permission đang cưỡng chế được gì thật |
| `tools/project_doctor.py` (chạy) | trạng thái cấu trúc hiện tại |
| `git log` · `git status` | phạm vi git thật |
| `00_LUAT_HIEN_HANH.md` | luật ưu tiên và sổ khai tử *(đã đọc ở vòng audit)* |

**Nguồn chính thức đã tra** — tất cả `code.claude.com/docs`, truy cập **2026-08-06**:

| Trang | URL |
|---|---|
| Memory / CLAUDE.md / rules | `https://code.claude.com/docs/en/memory` |
| Subagents | `https://code.claude.com/docs/en/sub-agents` |
| Hooks | `https://code.claude.com/docs/en/hooks` |
| Agent teams | `https://code.claude.com/docs/en/agent-teams` |
| Skills | `https://code.claude.com/docs/en/skills` |
| Settings | `https://code.claude.com/docs/en/settings` |

*(`docs.claude.com/en/docs/claude-code/*` nay **301 redirect** sang `code.claude.com/docs/en/*` — ghi lại vì mọi link cũ trong tài liệu nội bộ sẽ chuyển hướng.)*

---

## 3. Current Architecture Facts

*Chỉ fact ảnh hưởng trực tiếp tới thiết kế. Không nhắc lại audit.*

| # | Fact | Nhãn | Hệ quả thiết kế |
|---|---|---|---|
| F1 | Control plane v1 **đã cài**: 40 file, 2 commit, doctor 33 PASS / 0 FAIL | PROJECT EVIDENCE | v2 là **bản sửa trên nền đã có**, không phải bản dựng mới |
| F2 | Git **chỉ theo dõi 40 file control plane**. 116 mục chưa track, gồm toàn bộ video và 79 file gốc | PROJECT EVIDENCE | R1 chưa gỡ → **P0 của v2** |
| F3 | Project là **repo lồng** trong repo `/Users/admin` (0 commit, 0 file tracked) | PROJECT EVIDENCE | An toàn hiện tại, nhưng là nợ kỹ thuật |
| F4 | Hai skill predecessor **vẫn nằm nguyên ở global scope** và vẫn tự kích hoạt | PROJECT EVIDENCE | Override hiện chỉ là chữ trong `CLAUDE.md` |
| F5 | **Không có bất kỳ file số liệu nào** trong project | PROJECT EVIDENCE | Vòng analytics chưa thể chạy dù có schema |
| F6 | 19 quyết định treo, trong đó **4 cái chặn thẳng luật sản xuất** (D-01…D-04) | PROJECT EVIDENCE | v2 **không được** hợp nhất tài liệu trước khi quyết |
| F7 | Corpus 768 bản ghi / 530 MB nằm **trong** thư mục làm việc, đã gitignore | PROJECT EVIDENCE | Deny-read là biện pháp cưỡng chế duy nhất đang có |
| F8 | Sản lượng thật: **19 video / ~4 tháng**, một video tại một thời điểm | PROJECT EVIDENCE | Không có nhu cầu song song → không cần worktree, không cần agent team |
| F9 | Máy **không có `pyyaml`** | PROJECT EVIDENCE | Mọi validator phải chạy bằng thư viện chuẩn |
| F10 | macOS **chặn đọc `~/Desktop`** với shell này (TCC) | PROJECT EVIDENCE | Không đưa đường dẫn Desktop vào bất kỳ workflow nào |

---

## 4. Official Claude Code Capability Matrix

*Mọi dòng đều **OFFICIAL FACT**, nguồn `code.claude.com/docs`, truy cập 2026-08-06.*

| Feature | Official support | Stability | Limitation *(trích nguyên văn)* | Dùng thế nào trong dự án này | Source |
|---|---|---|---|---|---|
| **`CLAUDE.md`** | Có. Vị trí: managed policy · `~/.claude/CLAUDE.md` · `./CLAUDE.md` hoặc `./.claude/CLAUDE.md` · `./CLAUDE.local.md` | Stable | *"target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence."* · *"CLAUDE.md content is delivered as a user message after the system prompt… there's no guarantee of strict compliance"* | Giữ <200 dòng. **Chỉ đặt luật sống-còn.** Hiện 97 dòng — còn dư địa | `/docs/en/memory` |
| **`CLAUDE.md` sống sót `/compact`** | Có, **chỉ project-root** | Stable | *"Project-root CLAUDE.md survives compaction… Nested CLAUDE.md files in subdirectories and rules with `paths:` frontmatter are not re-injected automatically"* | 🔴 **Luật sống-còn KHÔNG được chỉ nằm ở `.claude/rules/`** | `/docs/en/memory` |
| **`.claude/rules/` path-scoped** | Có, YAML frontmatter `paths:` với glob | Stable | *"Path-scoped rules trigger when Claude reads files matching the pattern, not on every tool use."* Ngân sách 1.000 pattern sau khi bung brace | Giữ 6 rule. Hiểu đúng: đây là **gợi ý theo ngữ cảnh**, không phải rào chắn | `/docs/en/memory` |
| **`@path` imports** | Có, tối đa **4 hop** | Stable | *"imported files still load and enter the context window at launch"* — **không tiết kiệm context** | Không dùng để "gọn hoá" `CLAUDE.md`. Dùng skill thay thế | `/docs/en/memory` |
| **Subagents (project)** | `.claude/agents/`, precedence **3**; user `~/.claude/agents/` precedence **4** | Stable | Frontmatter: `name`, `description`, `tools`, `model`, `skills`, `mcpServers`, `memory`, `effort`. *"Names can't contain `:`"* | ✅ **Project agent ĐÈ user agent** — ngược với skill | `/docs/en/sub-agents` |
| **Subagent context isolation** | Có. *"Each subagent runs in its own context window"* | Stable | *"The main conversation's auto memory isn't loaded into subagents"* · lead's history không chuyển sang | Đây là **lý do duy nhất chính đáng** để tạo agent | `/docs/en/sub-agents` |
| **Subagent read-only** | Có, qua `tools:` | Stable | *"If no entry in the list resolves to a tool, the subagent usually fails to launch"* | 3 agent review đều `tools: Read, Grep, Glob` | `/docs/en/sub-agents` |
| **Subagent model** | `sonnet`·`opus`·`haiku`·`fable`·full ID·`inherit`. Mặc định `inherit` | Stable | — | Review agent: `inherit`. Agent máy móc: cân nhắc `haiku` | `/docs/en/sub-agents` |
| **Subagent memory** | `memory: user\|project\|local` | Stable | Thư mục riêng, không dùng chung với main | ⛔ **KHÔNG bật** — thêm một nguồn tri thức nữa để trôi | `/docs/en/sub-agents` |
| **Skills (project)** | `.claude/skills/<name>/SKILL.md` | Stable | 🔴 *"When skills share the same name across levels, **enterprise overrides personal, and personal overrides project**."* | **Project skill KHÔNG đè được user skill cùng tên** | `/docs/en/skills` |
| **Skill progressive disclosure** | Có | Stable | *"a skill's body loads only when it's used, so long reference material costs almost nothing until you need it"* | ✅ Chỗ đúng để đặt quy trình dài | `/docs/en/skills` |
| **Skill trigger** | Tự động khi liên quan, **hoặc** gõ `/tên` | Stable | Một số bundled skill *"run only when you invoke them"* | Skill của dự án nên nhắm **gọi tay** để kiểm soát chi phí | `/docs/en/skills` |
| **`permissions.deny`** | Có, 4 scope: managed > CLI > local > project > user | Stable | *"Settings rules are enforced by the client regardless of what Claude decides to do."* | 🔴 **Đây mới là biên giới thật** | `/docs/en/settings` |
| **Project settings tắt user skill/agent** | ❌ **Không** | — | *"There is no documented setting that allows project-level configuration to prevent loading of user-level skills or agents."* | 🔴 **Giả định của v1 sai** | `/docs/en/settings` |
| **`claudeMdExcludes`** | Có | Stable | Chỉ loại trừ **CLAUDE.md và rules**, không loại trừ skill/agent | Không giải quyết được F4 | `/docs/en/memory` |
| **Hooks — sự kiện** | **29 sự kiện**, gồm `PreToolUse`, `SessionStart`, `InstructionsLoaded`, `PreCompact`, `SubagentStart`… | Stable | — | Đang dùng 1 (`PreToolUse`). Đề xuất thêm `SessionStart` | `/docs/en/hooks` |
| **Hooks — chặn** | `PreToolUse` **exit 2** chặn; hoặc JSON `permissionDecision: "deny"` | Stable | 🔴 *"Claude Code treats **exit code 1 as a non-blocking error** and proceeds with the action… If your hook is meant to enforce a policy, use `exit 2`."* | Hook hiện dùng `exit 2` ✅ | `/docs/en/hooks` |
| **Hooks — là biên giới bảo mật?** | ❌ Tài liệu **không** khẳng định là biên giới tuyệt đối | — | *"To block an action regardless of what Claude decides, use a PreToolUse hook"* — nhưng `permissions.deny` mới là lớp client cưỡng chế | Hook = **lớp 2**, không phải lớp 1 | `/docs/en/memory`, `/docs/en/hooks` |
| **Auto memory** | Có, bật mặc định. `~/.claude/projects/<project>/memory/` | Stable | *"first 200 lines or 25KB"* của `MEMORY.md` nạp mỗi phiên. Tắt bằng `autoMemoryEnabled: false` | 🔴 `MEMORY.md` hiện **14 KB và chứa nguyên văn 8 memory đã chết** | `/docs/en/memory` |
| **Agent Teams** | Có | 🔴 **EXPERIMENTAL, tắt mặc định** | *"Agent teams are experimental and disabled by default. Enable them by setting `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`"* · *"use significantly more tokens"* · không resume được, không nested, permission cố định lúc spawn | ⛔ **Không dùng.** v1 nói đúng | `/docs/en/agent-teams` |
| **Git worktrees** | Có | Stable | — | ⛔ Chưa cần: một video tại một thời điểm (F8) | `/docs/en/worktrees` |
| **Plugins** | Có, namespace `plugin:skill` | Stable | Plugin subagent **không hỗ trợ** `hooks`, `mcpServers`, `permissionMode` | ⛔ Không cần cho một người dùng một máy | `/docs/en/sub-agents`, `/docs/en/plugins` |
| **Slash commands** | Đã **gộp vào skills** | Stable | *"A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy`"* | Dùng skill, không dùng `commands/` | `/docs/en/skills` |
| **`/doctor`** | Có, bundled | Stable | Đề xuất cắt gọn `CLAUDE.md`; báo agent trùng tên | Nên chạy định kỳ, **bổ sung** cho `project_doctor.py` | `/docs/en/memory`, `/docs/en/commands` |
| **`--add-dir`** | Có | Stable | Cấp quyền file; `.claude/skills/` bên trong **được nạp**, `CLAUDE.md` **không** trừ khi bật env var | Dùng cho phiên research corpus | `/docs/en/memory` |

**UNKNOWN** *(không tra được từ tài liệu, không suy đoán)*: giới hạn số agent chạy song song trong một phiên · chi phí token cụ thể của một vòng `/audit-script` 3 agent trên gói Max 5x · hạn mức Max 5x theo giờ.

---

## 5. V1 Critique — KEEP / MODIFY / REMOVE

| V1 component | Vấn đề nó chữa | Bằng chứng từ audit | Claude hỗ trợ chính thức? | Cần ngay? | Quá phức tạp? | Thiếu chi tiết? | Quyết |
|---|---|---|---|---|---|---|---|
| **Project root giữ nguyên** | tránh gãy tham chiếu | §2, §19 | n/a | ✅ | ❌ | — | **KEEP** |
| **Git init + baseline** | R1 mất dữ liệu | §20 R1 | ✅ | ✅ | ❌ | 🔴 **v1 không nói rõ phạm vi stage** → bản cài chỉ track control plane, R1 **vẫn hở** | **MODIFY** — bao phủ toàn bộ text |
| **`CLAUDE.md` <200 dòng** | rule volume R12 | §20 R12 | ✅ OFFICIAL: *"target under 200 lines"* | ✅ | ❌ | — | **KEEP** |
| **Path-scoped rules** | rule volume | §20 R12 | ✅ | ✅ | ❌ | 🔴 v1 không nêu **rules không reload sau `/compact`** và chỉ trigger khi **đọc file khớp** | **MODIFY** — luật sống-còn phải nhân đôi vào `CLAUDE.md` |
| **`SOURCE_OF_TRUTH.md`** | D-01, không rõ file nào thắng | §19, §21 | n/a | ✅ | ❌ | — | **KEEP** |
| **`RULE_REGISTRY.yaml`** | luật trôi | §17, §18 | n/a | ⚠️ | ⚠️ **26 mục YAML, không có validator vì máy thiếu `pyyaml`** | — | **MODIFY** — chuyển sang Markdown table, hoặc chấp nhận không validate |
| **`DECISIONS_REQUIRED.md`** | 18 quyết định treo | §21 | n/a | ✅ | ❌ | — | **KEEP** — thành phần giá trị nhất của v1 |
| **5 subagent** | R10 tự viết tự chấm | §20 R10 | ✅ | ⚠️ | 🔴 **có, cho creator solo** | 🔴 **hai cặp chồng lấn** | **MODIFY → 3** |
| ├ `cold-viewer` | tai sạch | §20 R10 | ✅ | ✅ | ❌ | — | **KEEP** |
| ├ `retention-architect` | bản đồ giữ chân | §14 | ✅ | ⚠️ | — | chồng lấn với dòng dưới | **MERGE** |
| ├ `promise-payoff-judge` | title↔script lệch | §17 C8 | ✅ | ✅ | — | cả hai đều nhận *title+thumbnail+script* và đều truy vết **payoff nằm ở đâu** | **MERGE** → `structure-judge` |
| ├ `evidence-prosecutor` | R5 research rời claim | §11 | ✅ | ✅ | ❌ | duy nhất cần `WebFetch` → **isolation có giá trị thật** | **KEEP** |
| └ `anti-ai-narration-critic` | mùi AI | §4.9 | ✅ | ✅ | 🔴 **là agent thì thừa** | đọc đúng file main session đã có → **isolation = 0** | **REMOVE as agent → SKILL** |
| **Agent permissions read-only** | R10 nhiều agent sửa script | §20 R10 | ✅ `tools:` | ✅ | ❌ | — | **KEEP** |
| **Editor duy nhất** | R10 | §20 R10 | n/a *(luật)* | ✅ | ❌ | — | **KEEP** — trụ cột đúng nhất của v1 |
| **Không orchestrator riêng** | — | — | n/a | ✅ | ❌ | — | **KEEP** |
| **Agent teams: chỉ dùng khi audit lớn** | — | — | ✅ nhưng **experimental** | ❌ | — | 🔴 v1 **không nêu** trạng thái experimental + env var + token cost | **MODIFY** — ghi rõ trạng thái, khuyến nghị không dùng |
| **6 project skill** | quy trình lặp | §6 | ✅ | ⚠️ | ⚠️ | — | **MODIFY → 5** *(gộp `verify-claims` vào `/audit-script` + `/apply-review`)* |
| **Hook `guard_project.py`** | R3 ghi đè | §20 R3 | ✅ | ✅ | ❌ | 🔴 v1 nguyên tắc 5 đúng, nhưng **không nói hook ≠ biên giới bảo mật**, và `exit 1` không chặn | **MODIFY** — ghi rõ phân lớp |
| **`settings.json` deny** | R6 corpus | §20 R6 | ✅ **client cưỡng chế** | ✅ | ❌ | v1 **hoàn toàn không nhắc** `permissions.deny` | **KEEP + NÂNG LÊN lớp 1** |
| **4 schema JSON** | R3, R5, không suy ra published | §10, §11 | n/a | ⚠️ | ⚠️ | — | **MODIFY** — giữ `video`, gộp `claim-ledger`, **hoãn** `analytics`+`review-verdict` |
| **`video.yaml` manifest** | không có status file | §19 | n/a | ✅ | ❌ | — | **KEEP** |
| **ID bất biến `SKA-NNNN-slug`** | trùng số 17, V01 rời | §2, §21 D-10 | n/a | ✅ | ❌ | — | **KEEP** |
| **Claim ledger** | R5 | §11 | n/a | ✅ | ❌ | — | **KEEP** |
| **Review workflow** | R10, R11 | §20 | ✅ | ✅ | ❌ | — | **KEEP** |
| **Analytics loop** | R4 vòng đứt | §14 | n/a | ✅ | 🔴 **schema đầy đủ trong khi 0 dữ liệu** | 🔴 v1 **không nói cách NHẬP dữ liệu** — mà đó chính là chỗ tắc | **MODIFY** — 1 CSV nhập tay trước, schema sau |
| **Corpus isolation** | R6 reused content | §20 R6 | ✅ qua `permissions.deny` | ✅ | ❌ | 🔴 v1 §9 chỉ đề xuất **chuyển thư mục**, không nhắc deny | **MODIFY** — deny trước, chuyển sau |
| **Asset manifest** | V12/V14/V15 lệch số | §2, §13 | n/a | ✅ | ❌ | 🔴 v1 **không có** thành phần này | **ADD** — v1 thiếu |
| **Shared pipeline** | 5 công cụ chồng lấn | §21 D-16 | n/a | ❌ | — | cần D-16 | **DEFER** |
| **`archive/`** | file chết vẫn nạp | §18 | ✅ qua rules + deny | ⚠️ | — | — | **MODIFY** — dùng `.claude/rules/archive-files.md` đã có, **không** tạo thư mục mới |
| **Migration V01–V19** | ID, published status | §10 | n/a | ❌ | 🔴 **có** | không có bước rollback cho từng video | **REMOVE** — thay bằng index file |
| **`knowledge/**` 9 thư mục** | tổ chức tri thức | §19 | n/a | ❌ | 🔴 **có** | 🔴 di chuyển 79 file trong khi **D-01…D-04 chưa quyết** | **REMOVE** khỏi phạm vi gần |
| **`project_doctor`** | không có validator | §19 | n/a | ✅ | ❌ | thiếu kiểm **đếm asset** | **KEEP + mở rộng** |
| **Global skill override** | R2 skill cũ tự kích hoạt | §20 R2 | 🔴 **KHÔNG** như v1 giả định | ✅ | — | 🔴 OFFICIAL: personal đè project; project settings **không tắt được** user skill | **MODIFY** — nêu 3 cách thật |

### 14 vấn đề đề bài yêu cầu tìm — kết quả

| # | Vấn đề | Có? | Bằng chứng |
|---|---|---|---|
| 1 | Thành phần không được Claude hỗ trợ đúng như mô tả | 🔴 **CÓ** | Override skill: personal đè project, project settings không tắt được user skill |
| 2 | Hook bị kỳ vọng quá khả năng | ⚠️ **MỘT PHẦN** | v1 nguyên tắc 5 đúng về ý, nhưng không nêu `exit 1` không chặn và hook không phải biên giới bảo mật |
| 3 | Quá nhiều agent cho creator solo | 🔴 **CÓ** | 5 agent, 2 cặp chồng lấn, 1 cái không cần isolation |
| 4 | Agent chồng lấn nhiệm vụ | 🔴 **CÓ** | `retention-architect` ↔ `promise-payoff-judge` |
| 5 | Agent vừa viết vừa tự review | ✅ **KHÔNG** | v1 tách đúng: 5 agent read-only, 1 editor |
| 6 | Nhiều agent cùng sửa script | ✅ **KHÔNG** | chỉ `/apply-review` |
| 7 | Skill và agent trùng vai trò | 🔴 **CÓ** | `anti-ai-narration-critic` (agent) ↔ `chong-van-ai-narration-en` (skill global) |
| 8 | `CLAUDE.md` quá dài | ✅ **KHÔNG** | 97/200 dòng |
| 9 | Rule registry quá phức tạp so với giá trị | ⚠️ **MỘT PHẦN** | 26 mục YAML không validate được vì thiếu `pyyaml` |
| 10 | Schema đòi migrate mọi video cũ ngay | 🔴 **CÓ** | v1 Phase 4 map toàn bộ V01–V19 |
| 11 | Git theo dõi generated media | ✅ **KHÔNG** | `.gitignore` đúng — nhưng **lệch ngược**: git không theo dõi cả text cần bảo vệ |
| 12 | Corpus isolation chỉ dựa vào prompt | ⚠️ **MỘT PHẦN** | v1 chỉ nêu chuyển thư mục; bản cài đã bổ sung `permissions.deny` |
| 13 | Analytics loop không có cách nhập dữ liệu | 🔴 **CÓ** | v1 §10 liệt kê 10 trường bắt buộc, không nói lấy từ đâu; Studio-only, Claude bị cấm vào tài khoản kênh |
| 14 | Kiến trúc đòi vận hành nhiều hơn giá trị | 🔴 **CÓ** | 40 file control plane cho một kênh 531 view / 7 sub / 1 video mỗi lần |

---

## 6. Architecture Options A / B / C

| Criterion | **A — Minimal Safety** | **B — Balanced Production** *(≈ v1)* | **C — Advanced Agentic Studio** |
|---|---|---|---|
| **Dành cho** | 1 video/lần, sửa lỗi nguy hiểm nhất trước | sản xuất đều, nhiều vòng review, có analytics | nhiều video song song, tự động hoá sâu |
| **File control plane** | ~14 *(dùng lại 40 đã cài, cắt bớt)* | 40+ | 60+ |
| **Agents** | **3** | 5 | 5 + agent teams + worktrees |
| **Skills** | **5** | 6 | 8+ |
| **Rules** | 6 *(giữ)* | 6 | 6+ |
| **Schemas** | **2** *(video, claim-ledger)* | 4 | 5+ |
| **Setup effort** | **~1 giờ** *(phần lớn đã cài)* | ~4 giờ | ~2 ngày |
| **Daily complexity** | **thấp** — 3 lệnh dùng thường | trung bình — 6 lệnh + 4 schema | cao — điều phối team, quản worktree |
| **Context cost mỗi phiên** | `CLAUDE.md` 97 dòng + rules khớp | như A + skill dài hơn | như B + context của teammate |
| **Max 5x usage** | 1 vòng audit = **3 subagent** | 1 vòng = **5 subagent** | 1 vòng = 3-5 **phiên Claude đầy đủ** — *"significantly more tokens"* (OFFICIAL) |
| **Safety** | ✅ deny + hook + git **toàn bộ text** | ⚠️ deny + hook, git **chỉ control plane** | như B + worktree cách ly |
| **Scalability** | 1-2 video song song | 2-3 | 5+ |
| **Lợi ích kỳ vọng** | gỡ R1, R3, R10; giữ được vòng review | như A + analytics có cấu trúc + version đầy đủ | như B + song song hoá |
| **Rủi ro chính** | vẫn thiếu analytics có cấu trúc | **ceremony vượt sản lượng** — 40 file cho 1 video/tuần | experimental, không resume được, token cao |
| **Khi nào nên nâng cấp** | — | khi đạt **≥2 video/tuần đều đặn** và đã có ≥3 postmortem thật | khi **≥3 video chạy song song** và team teams hết experimental |

### OPTION A — MINIMAL SAFETY UPGRADE ⭐ *(khuyến nghị)*

**File cần tạo/sửa** *(phần lớn đã có từ bản cài v1)*:
- Giữ: `CLAUDE.md` · `.claude/rules/` (6) · `.claude/settings.json` · `.claude/hooks/guard_project.py` · `governance/{SOURCE_OF_TRUTH, DECISIONS_REQUIRED, CHANGE_POLICY, RETIRED_RULES}.md` · `schemas/video.schema.json` · `schemas/claim-ledger.schema.json` · `templates/{video.yaml, claim-ledger.md, review-consolidated.md, publish-record.md}` · `tools/project_doctor.py`
- **Thêm mới (4)**: `tools/verify_images.py` *(⚠️ 07/08: từng ghi là `count_assets.py` "cần làm mới" — thật ra ĐÃ TỒN TẠI từ 25/07, nằm lạc ở gốc kho nên không ai thấy)* · `analytics/channel/videos.csv` *(nhập tay)* · `videos/_LEGACY_INDEX.md` · `.claude/skills/anti-ai-polish/SKILL.md`
- **Gộp/bỏ**: 5 agent → 3 · 6 skill → 5 · bỏ `schemas/analytics.schema.json` và `review-verdict.schema.json` *(hoãn)* · bỏ `templates/{analytics-video, postmortem}.md` *(hoãn tới khi có dữ liệu)*

**Agents (3)**: `cold-viewer` · `structure-judge` · `evidence-prosecutor`
**Skills (5)**: `/new-video` · `/audit-script` · `/apply-review` · `/anti-ai-polish` · `/project-doctor`
**Git**: bao phủ **toàn bộ text** của dự án — `*.md`, `*.txt`, `*.py`, `*.json`, `*.yaml` *(media, corpus, node_modules, build đã bị ignore)*
**Video status**: `video.yaml` **chỉ cho video đang làm**. Video cũ → một dòng trong `_LEGACY_INDEX.md`
**Analytics**: một CSV, nhập tay từ ảnh chụp Studio
**Chi phí vận hành**: ~5 phút mỗi video *(điền `video.yaml` + chạy doctor)*; 1 vòng audit = 3 subagent

### OPTION B — BALANCED PRODUCTION ARCHITECTURE

Đúng như v1 đã cài, cộng phần chưa làm: `knowledge/**`, `videos/SKA-*` cho mọi video, `analytics/` đầy đủ 4 schema, migration V01–V19.

**Vì sao KHÔNG chọn bây giờ** — ba bằng chứng:
1. **Sản lượng không đỡ nổi**: 19 video / 4 tháng, một video một lần *(F8)*. Bốn schema và 9 thư mục knowledge là hạ tầng cho đội nhóm, không cho một người.
2. **Bốn mâu thuẫn chưa quyết chặn ngay bước đầu**: `knowledge/writing/` phải gộp `WORKFLOW` với `FLOW` *(D-01)*; `knowledge/visual/` phải chọn giữa `@token` và lặp chữ *(D-04)*. **Không thể migrate cái chưa quyết.**
3. **Analytics đầy đủ mà không có dữ liệu là vỏ rỗng** — schema không tạo ra số.

**Điều kiện để nâng lên B**: ≥2 video/tuần đều trong 1 tháng · đã có ≥3 postmortem dựa trên số liệu thật · D-01…D-04 đã quyết.

### OPTION C — ADVANCED AGENTIC STUDIO

Agent teams + git worktrees + machine-readable state + pipeline hợp nhất.

**Chi phí và rủi ro (OFFICIAL FACT)**:
- Agent teams **experimental, tắt mặc định**, cần `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
- *"use significantly more tokens than a single session"* · *"Token costs scale linearly"*
- **Không resume được**: *"`/resume` and `/rewind` do not restore in-process teammates"*
- Task status có thể treo; shutdown chậm; permission cố định lúc spawn; không nested team

**Failure mode cụ thể cho dự án này**: hai teammate cùng sửa một kịch bản → *"Two teammates editing the same file leads to overwrites"* — mà **ghi đè kịch bản đúng là rủi ro R3** đang cố gỡ.

**Vì sao chưa nên**: F8 nói một video tại một thời điểm. Song song hoá thứ vốn tuần tự chỉ thêm chi phí điều phối. **Nâng cấp khi ≥3 video chạy song song và agent teams hết experimental.**

---

## 7. Recommended V2 Architecture

*Cây thư mục đề xuất. **Không triển khai.** `[có]` = đã tồn tại · `[sửa]` = đổi nội dung · `[mới]` = chưa có · `[bỏ]` = gỡ khỏi phạm vi gần.*

```text
Build Channel Người Que Cổ Đại/          ← giữ nguyên vị trí, không tạo repo mới
├── CLAUDE.md                            [có] <200 dòng, mang LUẬT SỐNG-CÒN
├── .gitignore                           [sửa] chỉ chặn media/corpus/build — KHÔNG chặn text
├── .claude/
│   ├── settings.json                    [có] permissions.deny = biên giới LỚP 1
│   ├── settings.local.example.json      [có]
│   ├── agents/
│   │   ├── cold-viewer.md               [có] KEEP
│   │   ├── structure-judge.md           [mới] = retention-architect + promise-payoff-judge
│   │   ├── evidence-prosecutor.md       [có] KEEP (duy nhất có WebFetch)
│   │   ├── retention-architect.md       [bỏ] → gộp
│   │   └── promise-payoff-judge.md      [bỏ] → gộp
│   ├── rules/                           [có] 6 file — KEEP nguyên
│   ├── skills/
│   │   ├── new-video/                   [có]
│   │   ├── audit-script/                [sửa] 3 agent thay vì 5, gọi /anti-ai-polish
│   │   ├── apply-review/                [sửa] nuốt luôn verify-claims
│   │   ├── anti-ai-polish/              [mới] ← hạ từ agent xuống skill
│   │   ├── project-doctor/              [có]
│   │   ├── verify-claims/               [bỏ] → vào audit-script + apply-review
│   │   └── postmortem/                  [hoãn] tới khi có dữ liệu thật
│   └── hooks/
│       ├── guard_project.py             [có] LỚP 2
│       └── session_warn.py              [mới] SessionStart: cảnh báo skill predecessor
├── governance/
│   ├── SOURCE_OF_TRUTH.md               [có]
│   ├── DECISIONS_REQUIRED.md            [có] ⭐ thành phần giá trị nhất
│   ├── CHANGE_POLICY.md                 [có]
│   ├── RETIRED_RULES.md                 [có]
│   ├── RULE_REGISTRY.md                 [sửa] YAML → Markdown (máy thiếu pyyaml)
│   ├── MIGRATION_LOG.md                 [có]
│   └── INSTALL_REPORT.md                [có]
├── schemas/
│   ├── video.schema.json                [có]
│   ├── claim-ledger.schema.json         [có]
│   ├── analytics.schema.json            [hoãn]
│   └── review-verdict.schema.json       [bỏ] — bảng Markdown là đủ
├── templates/                           [có] giữ 4, hoãn 2
├── tools/
│   ├── project_doctor.py                [có] + thêm kiểm asset
│   └── count_assets.py                  [mới] ⭐ ảnh vs mp3 vs shotline
├── analytics/
│   └── channel/videos.csv               [mới] ⭐ MỘT file, nhập tay
├── videos/
│   ├── _LEGACY_INDEX.md                 [mới] ⭐ thay cho migration 19 video
│   └── SKA-0019-night-walk/             [pilot] chỉ video đang làm
│       ├── video.yaml
│       ├── 01-brief/ 02-research/ 03-script/ 04-review/
│       └── 05-packaging/ 06-production/ 07-publish/ 08-analytics/
│
├── knowledge/                           [BỎ khỏi phạm vi gần] — cần D-01…D-04
├── pipeline/                            [BỎ] — cần D-16
├── migration/  archive/                 [BỎ] — đã có _KHO_LUU_DaChet + rules
│
├── [79 file gốc]                        GIỮ NGUYÊN — nay ĐƯỢC git bao phủ
├── Video01…Video19/                     GIỮ NGUYÊN — text được git bao phủ, media không
├── 2_KHO_BANGHI/                        GIỮ NGUYÊN — gitignore + permissions.deny
├── _KHO_LUU_DaChet/                     GIỮ NGUYÊN — rules/archive-files.md chặn
└── GhepVideo_*/  automation-pipeline/   GIỮ NGUYÊN — cần D-16
```

**Số file control plane: 40 → ~38** *(bỏ 4, thêm 4, sửa 5)*. Điểm mấu chốt không phải ít file hơn mà là **ít thứ phải vận hành hơn**: 3 agent thay 5, 5 skill thay 6, 2 schema sống thay 4.

---

## 8. Source-of-Truth and Context Model

### Hierarchy — 5 lớp, thấp thắng cao

| Lớp | Nguồn | Cưỡng chế? | Sống sót `/compact`? |
|---|---|---|---|
| **1. Permissions** | `.claude/settings.json` → `permissions.deny` | ✅ **client cưỡng chế** (OFFICIAL) | không liên quan |
| **2. Hooks** | `PreToolUse` exit 2 | ✅ chặn được, **nhưng không phải biên giới bảo mật** | không liên quan |
| **3. `CLAUDE.md` project-root** | luật sống-còn | ❌ chỉ là context | ✅ **có** (OFFICIAL) |
| **4. `.claude/rules/` path-scoped** | luật theo khu vực | ❌ | 🔴 **KHÔNG** — nạp lại khi đọc file khớp |
| **5. Tài liệu trong kho** | `00_LUAT_HIEN_HANH.md` v.v. | ❌ | ❌ chỉ khi được đọc |

🔴 **Hệ quả thiết kế quan trọng nhất của v2**: vì lớp 4 **không sống sót `/compact`**, mọi luật mà vi phạm gây **mất mát không hồi phục** phải xuất hiện ở **lớp 1 hoặc 3**, không được chỉ nằm ở lớp 4. Ba luật đó: *không ghi đè kịch bản* · *không suy ra published* · *corpus chỉ để đo*.

### Nạp gì, khi nào

| Loại | Nạp lúc nào | Ví dụ |
|---|---|---|
| **Luôn nạp** | mỗi phiên | `CLAUDE.md` (97 dòng) · rules không có `paths:` · `MEMORY.md` (200 dòng đầu) |
| **Path-scoped** | khi Claude **đọc** file khớp | 6 file `.claude/rules/` |
| **Chỉ khi gọi** | `/tên-skill` | 5 skill — *"a skill's body loads only when it's used"* |
| **⛔ Cấm tự đọc** | — | `2_KHO_BANGHI/**` · `**/PROMPTS_FULL.txt` · `GhepVideo_Desktop/**` · `_KHO_LUU_DaChet/**` |

**Kích thước tối đa hợp lý cho `CLAUDE.md`: 200 dòng** (OFFICIAL). Hiện 97 → **dư 103 dòng**, đủ để nhân đôi ba luật sống-còn từ lớp 4 lên lớp 3.

**Chống loãng context**: `permissions.deny` trên `Read` là biện pháp **duy nhất cưỡng chế được** (lớp 1). Đã cài. Đây là điểm v1 bỏ sót hoàn toàn.

### 🔴 Deprecation — chỗ v1 sai

v1 và bản cài giả định **project-local đè global skill**. Sự thật:

> *"When skills share the same name across levels, **enterprise overrides personal, and personal overrides project**."* — OFFICIAL

Và: *"There is no documented setting that allows project-level configuration to prevent loading of user-level skills or agents."*

Hai skill predecessor còn mang **tên khác** với skill dự án, nên ngay cả cơ chế trùng-tên cũng không áp dụng — chúng **cùng tồn tại và cùng có thể tự kích hoạt**.

**Ba cách xử lý thật** *(xếp theo mức hiệu quả)*:

| # | Cách | Hiệu quả | Chi phí |
|---|---|---|---|
| **1** | **Đổi tên hai skill global** thành `zz-deprecated-*` và sửa `description` thành *"KHÔNG DÙNG — thay bằng sketchapiens-*"* | 🟢 cao — sửa đúng gốc | cần chủ cho phép sửa global scope |
| **2** | **Hook `SessionStart`** in cảnh báo mỗi phiên | 🟡 trung bình — nhắc, không chặn | thấp |
| **3** | Luật trong `CLAUDE.md` §3 *(đang dùng)* | 🔴 thấp — *"no guarantee of strict compliance"* | 0 |

**ARCHITECTURE INFERENCE**: cách 1 là cách duy nhất thực sự đóng R2. Nó cần quyết định của chủ vì đụng global scope.

---

## 9. Agent Model

### Giữ lại — 3

| Agent | Vì sao TỒN TẠI *(giá trị isolation)* | Inputs | Forbidden inputs | Tools | Model | Read-only | Sửa được? | Output |
|---|---|---|---|---|---|---|---|---|
| **`cold-viewer`** | 🟢 **Isolation là chính lý do.** Giá trị nằm ở chỗ nó **không biết** research, rubric, lý lẽ người viết. Main session không thể quên những thứ đó | title · mô tả thumbnail · lời đọc | research · rubric · claim ledger · corpus · audit | `Read, Grep, Glob` | `inherit` | ✅ | ❌ | điểm bỏ xem · câu phải nghe lại · lúc trả lời hứa · 10 câu tệ nhất |
| **`structure-judge`** 🆕 | 🟢 Cần đọc **toàn bộ** kịch bản và dựng bản đồ — việc làm ngập context chính. Vẫn phải mù về lý lẽ người viết | title · thumbnail · lời đọc | như trên | `Read, Grep, Glob` | `inherit` | ✅ | ❌ | bản đồ thời gian · tiền thuê chương · vòng lặp mở · **một câu hỏi hay nhiều** · vết nối · mâu thuẫn thumbnail↔kịch bản · điểm thoát |
| **`evidence-prosecutor`** | 🟢 **Bộ tool khác hẳn** (`WebFetch`) + đọc nguồn gốc làm ngập context. Isolation có giá trị đo được | lời đọc · claim ledger | — | `Read, Grep, Glob, WebFetch` | `inherit` | ✅ | ❌ | bảng DIRECT/INFERENCE/SPECULATION/STORY_DEVICE + mức vượt 0-3 |

### Gộp — 1

**`retention-architect` + `promise-payoff-judge` → `structure-judge`**

Bằng chứng chồng lấn: cả hai nhận **đúng cùng bộ input** (title + thumbnail + lời đọc), cả hai bị cấm **đúng cùng bộ input**, và cả hai truy vết **payoff nằm ở đâu trong bài** — `retention-architect` gọi là *"payoff đầu tiên"*, `promise-payoff-judge` gọi là *"chỗ trả lời"*. Hai agent cùng đọc một file để trả lời hai nửa của một câu hỏi cấu trúc thì **không có giá trị isolation giữa chúng**.

Rủi ro khi gộp: output dài hơn, có thể lẫn hai lăng kính. **Giảm thiểu**: giữ nguyên **hai mục tách bạch** trong output template.

### Bỏ khỏi vai trò agent — 1

**`anti-ai-narration-critic` → skill `/anti-ai-polish`**

- Nó đọc **đúng file** main session đã có → **isolation = 0**
- Giá trị của nó là một **bảng kiểm 14 dấu hiệu**, không phải một góc nhìn sạch
- Đã tồn tại skill global `chong-van-ai-narration-en` làm đúng việc này → **agent này trùng vai trò** *(vấn đề #7 đề bài yêu cầu tìm)*
- Skill rẻ hơn: *"loads only when it's used"* (OFFICIAL)

### Writer có phải agent riêng không? — **KHÔNG**

**ARCHITECTURE INFERENCE**: người viết cần **toàn bộ** ngữ cảnh — mỏ neo, quyết định của chủ, các vòng trước. Đẩy ra subagent là **cắt mất** đúng thứ nó cần. Main Claude viết; subagent chấm. Đây là điểm v1 làm đúng.

### Orchestrator riêng? — **KHÔNG**

`/audit-script` gọi 3 subagent rồi gộp. Thêm một agent điều phối là thêm một lớp không mang thông tin mới. v1 làm đúng.

### Agent Team hằng ngày? — **KHÔNG**

Experimental · tắt mặc định · token cao · không resume · và failure mode *"Two teammates editing the same file leads to overwrites"* đâm thẳng vào R3.

### Model routing

| Việc | Model | Lý do |
|---|---|---|
| Viết thân bài, biên tập | `inherit` (Opus 5) | công việc đầu não |
| Hook 15 giây đầu, đoạn kết | Fable 5 *(chủ tự đổi)* | ghi trong memory dự án |
| 3 agent review | `inherit` | phán đoán tinh tế; `haiku` sẽ bỏ sót đúng loại lỗi cần bắt |
| `project_doctor` | không cần model | script thuần |

**ARCHITECTURE INFERENCE**: không dùng `haiku` cho agent review. Việc của chúng là bắt **sắc thái** — mùi văn AI, vết nối cấu trúc — đúng loại việc mà model rẻ hỏng nhất.

---

## 10. Skill and Workflow Model

| Skill | Trigger | Input | Output | Agents | Human gate |
|---|---|---|---|---|---|
| `/new-video` | tay | slug · số · thư mục cũ *(nếu có)* | khung `videos/SKA-*/` + `video.yaml` @ `idea` | — | ✅ chủ đặt tên và số |
| `/audit-script` | tay | đường dẫn bản nháp · title · thumbnail | `04-review/RNNN-audit.md` **chưa phân loại** | 3 *(song song)* + `qa_kichban.py` | ✅ **chủ phân loại từng mục** |
| `/anti-ai-polish` 🆕 | tay, thường sau audit | lời đọc | 10 câu nặng mùi · ẩn dụ chồng tầng · sẹo vá | — *(skill, không agent)* | ✅ chủ duyệt trước khi áp |
| `/apply-review` | tay, **sau khi đã phân loại** | audit đã phân loại | `03-script/vNNN-*.md` mới + `RNNN-applied.md` | `evidence-prosecutor` *(nếu có câu mới mang số)* | ✅ chỉ chạy khi bảng phân loại đã điền |
| `/project-doctor` | tay, trước mỗi commit | — | PASS/WARN/FAIL | — | — |
| ~~`/verify-claims`~~ | **bỏ** | — | — | — | gộp vào `/audit-script` và `/apply-review` |
| ~~`/postmortem`~~ | **hoãn** | — | — | — | mở lại khi `analytics/channel/videos.csv` có ≥1 dòng thật |

**Vì sao bỏ `/verify-claims`**: nó chỉ gọi đúng một agent và không thêm bước nào. Cả hai chỗ cần nó — audit và sau khi sửa — đều đã gọi agent đó. Một skill bọc một agent là **ceremony**, không phải kiến trúc.

**Vì sao hoãn `/postmortem`**: skill hoàn hảo mà không có dữ liệu thì không chạy được lần nào. Mở lại khi có dòng đầu tiên.

### Workflow đầy đủ — 18 bước

| # | Bước | Owner | Input | Output | Agent/Skill | File đổi | Human gate | Rollback |
|---|---|---|---|---|---|---|---|---|
| 1 | Idea | **chủ** | — | dòng trong `video.yaml` | `/new-video` | `videos/SKA-*/video.yaml` | ✅ | xoá thư mục mới |
| 2 | Demand validation | Claude đo, **chủ quyết** | `BANG_CAU` + tra bầy clone live | ghi chú `01-brief/` | — | `01-brief/` | ✅ cửa 0 | git revert |
| 3 | Title | Claude đề xuất, **chủ chốt** | `HE_THONG_KichBan_v2` PHẦN C | `05-packaging/title.md` | — | `video.yaml.title` | ✅ | git revert |
| 4 | Thumbnail **concept** | Claude, **chủ chốt** | `PROMPT_TONG_Thumbnail_v6` | concept text | — | `video.yaml.thumbnail.stage=concept_only` | ✅ | git revert |
| 5 | Research | Claude | nguồn gốc | `02-research/` | — | — | — | git revert |
| 6 | Claim ledger | Claude | nguồn | `02-research/claim-ledger.md` | `evidence-prosecutor` | `video.yaml.evidence` | ✅ **khoá bằng chứng** | git revert |
| 7 | Draft | **Main Claude** | title + ledger | `03-script/v001-claude-draft.md` | — *(không phải agent)* | + `script_versions` | — | version cũ còn nguyên |
| 8 | Independent critique | 3 agent | bản nháp | `04-review/RNNN-audit.md` | `/audit-script` | — | — | read-only, không cần rollback |
| 9 | **Human triage** | **chủ** | bản chấm | cột phân loại đã điền | — | `RNNN-audit.md` | 🔴 **BẮT BUỘC** | — |
| 10 | Revision | **Main Claude** *(editor duy nhất)* | phân loại | `03-script/vNNN+1-*.md` | `/apply-review` | + `script_versions` | — | version cũ bất biến |
| 11 | Fact re-check | Claude | version mới | ledger cập nhật | `evidence-prosecutor` | `claim-ledger.md` | ✅ nếu mức vượt ≥2 | git revert |
| 12 | Approval | **chỉ chủ** | version cuối | `03-script/approved.md` | — *(hook chặn agent)* | `video.yaml.approved` | 🔴 **BẮT BUỘC** | không sửa được — tạo `vNNN` mới |
| 13 | Shots | Claude | `approved.md` | `06-production/shotlines.txt` | `sketchapiens-chia-shot` | — | — | gen lại |
| 14 | Assets | **chủ** *(Flow/Nano Banana)* | prompt ảnh | ảnh + mp3 | — | — | ✅ **đếm file == số prompt** | gen lại vào thư mục rỗng |
| 15 | Assemble | **chủ** *(app)* | ảnh + mp3 | `.mp4` | — | — | ✅ đối chiếu nội dung nhiều mốc | ghép lại |
| 16 | Publish | **chỉ chủ** | mp4 + metadata | `07-publish/publish-record.md` | — | `video.yaml.publish` | 🔴 **BẮT BUỘC** | không có |
| 17 | Analytics | **chủ nhập tay** | ảnh Studio | dòng trong `analytics/channel/videos.csv` | — | csv | ✅ | sửa dòng |
| 18 | Postmortem → đề xuất luật | Claude đề xuất, **chỉ chủ duyệt** | csv | mục trong `DECISIONS_REQUIRED.md` | `/postmortem` *(khi mở lại)* | governance | 🔴 **BẮT BUỘC** — 5 điều kiện | git revert |

**Bốn cổng người bắt buộc: bước 9, 12, 16, 18.** Đây là bốn chỗ mà sai lầm không hồi phục được hoặc gây hậu quả bên ngoài.

---

## 11. Video State and Versioning

### ID bất biến
`SKA-NNNN-slug` — 4 chữ số, slug tiếng Anh gạch nối. **Không đổi sau khi cấp.**

### Sáu trạng thái phân biệt rõ — không dùng tên file `FINAL` làm trạng thái

| Trạng thái | File đại diện | Ai đặt | Bất biến? |
|---|---|---|---|
| **draft** | `03-script/v001-claude-draft.md` | Claude | ❌ nhưng không ghi đè — tạo `vNNN` mới |
| **current** | `vNNN` cao nhất | Claude | ❌ |
| **reviewed** | `04-review/RNNN-audit.md` | 3 agent | ✅ bản chấm không sửa |
| **approved** | `03-script/approved.md` | 🔴 **chỉ chủ** | ✅ **hook chặn mọi Write/Edit** |
| **production** | `06-production/` + `approved.md` | Claude từ `approved.md` | — |
| **published** | `03-script/published.md` + `07-publish/publish-record.md` | 🔴 **chỉ chủ** | ✅ **hook chặn** |

`published.md` **có thể khác** `approved.md` — chủ có thể sửa tay lúc đăng. Đây là lý do phải có hai file, và v1 nói đúng điểm này.

### Provenance
Mỗi `vNNN` ghi trong `video.yaml.script_versions`: `file · reason · words · created`. Mỗi bản chấm ghi trong `reviews`: `round · file · kind · triaged`.

### 🔴 Xử lý V01–V19 — **KHÔNG migrate** *(khác v1)*

Thay bằng **một file** `videos/_LEGACY_INDEX.md`:

```
| ID gợi ý | Thư mục cũ | Narration | Anchors | Metadata | Publish state | Ghi chú |
| SKA-0001-body-hair | (không có thư mục — 11 file ở gốc kho) | 2 ứng viên FINAL | ➖ | ➖ | UNKNOWN | D-06 |
| SKA-0017-rain      | videos/Video17_Rain/  | ✅ | ✅ | ✅ | UNKNOWN | trùng số 17 |
| SKA-0017x-death    | videos/Video17_Death/ | ➖ (chỉ DOT1) | ✅ | ➖ | không đăng | bỏ dở — D-10 |
| …
```

**Vì sao index thay vì migration** *(ARCHITECTURE INFERENCE)*:
- Migration 19 video = copy hàng nghìn file, sinh bản thứ hai của mọi thứ, **nhân đôi rủi ro lệch bản**
- Giá trị cho video sắp làm = **0**
- `publish state` của **tất cả** vẫn là `UNKNOWN` cho tới khi chủ trả lời D-05 → **không được đoán**
- Index cho đúng thứ cần: *"video này có anchors không, narration ở đâu, đã đăng chưa"* — trả lời được bằng một bảng

### Hai V17 và V01
`videos/Video17_Rain` và `videos/Video17_Death` cùng số; V01 không có thư mục. **v2 KHÔNG tự cấp ID** — đây là **D-10**. Đề xuất mặc định *(chờ chủ duyệt)*: `SKA-0001-body-hair` cho V01; giữ `SKA-0017-rain` cho bản đã sản xuất; `SKA-0017x-death` hoặc số mới cho bản bỏ dở.

---

## 12. Evidence System

### Bốn mức tin cậy

| Nhãn | Nghĩa | Trong lời đọc phải |
|---|---|---|
| **known** *(DIRECT)* | nguồn nói đúng điều này, đúng con số, đúng nhóm dân số | nói thẳng |
| **likely** *(INFERENCE)* | nguồn nói A, kịch bản nói B; B suy ra được nhưng nguồn không nói | hedge, hoặc quy cho tác giả |
| **possible** *(SPECULATION)* | không nguồn nào nói | **tự nhận là chưa biết** |
| **story device** | dựng cảnh, không phải mệnh đề sự thật | không cần nguồn |

### Thang vượt 0-3
`0` khớp · `1` rộng hơn nguồn · **`2` bắc cầu giữa hai bảng thống kê rời** · `3` bịa.
**Khoá được khi không còn mệnh đề mức ≥2.**

### Bốn luật cứng
1. **Mở toàn văn nguồn, không tin snippet.** Không mở được → `UNVERIFIED`.
2. ⛔ **Cấm bắc cầu hai bảng thống kê rời nhau** — lỗi đã xảy ra thật *(PROJECT EVIDENCE: `MONEO_V19.md` §KHOÁ M3b)*.
3. **Suy diễn của tác giả nguồn phải ghi rõ**: *"the researchers put that down to…"*.
4. **Dữ liệu hiện đại suy về tiền sử** phải đánh dấu, và lời đọc phải tự nói ra giới hạn.

### 🔴 Re-verification sau sửa
**Mọi câu thêm vào SAU khi khoá bằng chứng phải chạy lại cổng bằng chứng** — kể cả khi thêm chỉ để đủ độ dài. Lỗi bịa trình tự lọt đúng vì khối đó được viết sau khi cổng đã đóng *(PROJECT EVIDENCE)*.

Cưỡng chế trong v2: `/apply-review` **tự gọi** `evidence-prosecutor` khi version mới có câu mang số liệu. Đây là lý do bỏ `/verify-claims` thành skill riêng — nó phải là **bước tự động trong editor**, không phải một lệnh người phải nhớ gọi.

---

## 13. Production and Asset System

| Thành phần | v2 |
|---|---|
| **Shared pipeline** | ⏸️ **hoãn** — cần D-16. Hiện 5 công cụ chồng lấn; chọn sai chuẩn tốn hơn chờ |
| **Per-video config** | `video.yaml` |
| **Asset manifest** 🆕 | `tools/verify_images.py` *(⚠️ 07/08: từng ghi là `count_assets.py` "cần làm mới" — thật ra ĐÃ TỒN TẠI từ 25/07, nằm lạc ở gốc kho nên không ai thấy)* — đếm ảnh · mp3 · dòng shotline cho **mọi** video, báo lệch |
| **Validation** | số ảnh == số prompt == số mp3 == số dòng shotline. Lệch = **FAIL**, không phải cảnh báo |
| **Generated files** | `.gitignore` chặn `PROMPTS_FULL.txt`, `build/`, `_vtt/`, media |
| **Secrets** | biến môi trường. `permissions.deny` chặn đọc `.env`/`*.key`. Hook chặn ghi chuỗi giống khoá |
| **Rollback** | git cho text; ảnh/audio **gen lại** *(không vào git — đúng chủ đích)* |
| **Ranh giới repo app** | `GhepVideo_*` và `automation-pipeline` **nên tách repo riêng** — nhưng cần D-16. Hiện `GhepVideo_Desktop/` 2,4 GB đã bị `.gitignore` |

**Vì sao `count_assets.py` là P0**: audit tìm ra V12 265/255 · V14 608/302 · V15 568/564 lệch mà **không ai biết**, và lệch ảnh-audio đúng là nguyên nhân V15 hỏng tiếng. **v1 không có thành phần này** — đây là chỗ v1 thiếu, không phải chỗ v1 thừa.

### Git strategy — thay đổi lớn nhất của v2

| | v1 / bản đã cài | **v2** |
|---|---|---|
| Text control plane | ✅ track | ✅ track |
| **79 file gốc kho** | ❌ | ✅ **track** |
| **Narration V01–V19** | ❌ | ✅ **track** |
| **Metadata, anchors, research của video** | ❌ | ✅ **track** |
| `PROMPTS_FULL.txt` (14 file, 187 KB–1,4 MB) | ❌ | ❌ giữ nguyên — sinh lại được |
| Ảnh · audio · video | ❌ | ❌ giữ nguyên |
| Corpus 530 MB | ❌ | ❌ giữ nguyên |
| `GhepVideo_Desktop/` 2,4 GB | ❌ | ❌ giữ nguyên |

**Ước lượng dung lượng thêm**: 979 file text, trừ các `PROMPTS_*` cỡ MB → **ước ~15–20 MB**. *(ARCHITECTURE INFERENCE — nên đo bằng `du` trước khi chạy.)*

**Không dùng Git LFS**: media sinh lại được từ prompt; LFS thêm phụ thuộc mà không thêm an toàn.

---

## 14. Analytics and Learning Loop

### 🔴 Chỗ v1 hỏng nặng nhất

v1 §10 liệt kê 10 trường bắt buộc mỗi video — nhưng **không nói lấy dữ liệu từ đâu**. Thực tế *(PROJECT EVIDENCE)*:
- YouTube Analytics API **không trả về impressions và CTR** — chỉ Studio có
- Claude **bị cấm** vào tài khoản kênh *(memory `browser_chrome_cuong_only`)*
- → **mọi số phải do chủ nhập tay**

Một schema JSON 60 dòng cho dữ liệu phải gõ tay là **rào cản**, không phải hạ tầng.

### v2: bắt đầu bằng MỘT file CSV

`analytics/channel/videos.csv` — mỗi video một dòng, để trống thì để trống:

```csv
video_id,measured_at,days_since_publish,impressions,ctr_pct,views,avd_sec,apv_pct,ret30_pct,subs,source,note
SKA-0017-rain,2026-08-01,5,367,3.5,13,,55.6,,0,studio_screenshot,"ret30 đo trên 12 người - KHÔNG dùng làm chuẩn"
```

**Vì sao CSV**: gõ tay được trong 60 giây từ một ảnh chụp màn hình · đọc bằng `csv` chuẩn *(F9: máy thiếu `pyyaml`)* · diff sạch trong git · nâng lên schema JSON sau khi có ≥5 dòng.

### Ngưỡng cỡ mẫu trước khi đề xuất luật

| Cỡ mẫu | Được làm gì |
|---|---|
| **< 100 quan sát** | 🔴 ghi lại, **cấm** dùng làm chuẩn, **cấm** đề xuất luật |
| 100–999 | được nêu **giả thuyết**, phải ghi khoảng tin cậy |
| ≥ 1.000 | được đề xuất luật, vẫn cần đủ 5 điều kiện |

*Nguồn ngưỡng: PROJECT EVIDENCE — giữ chân 55,6% đo trên **12 người** cho khoảng tin cậy [27,5%; 83,7%], vô dụng để kết luận.*

### Observation vs Hypothesis vs Rule

```
observation  → dòng trong videos.csv                      (Claude ghi được)
hypothesis   → mục trong postmortem, kèm cỡ mẫu + CI      (Claude đề xuất được)
rule         → dòng trong RULE_REGISTRY                   (🔴 CHỈ CHỦ, đủ 5 điều kiện)
```

### Retention timestamp → câu chữ
Map `giây → đoạn → câu → shot`. Không map được thì ghi `not_mapped` — **không đoán**. Cần `06-production/shotlines.txt` còn nguyên, thêm một lý do nữa để git bao phủ text.

---

## 15. Security Boundaries

*Xếp theo mức cưỡng chế thật, cao xuống thấp. **v1 không phân lớp này** — đó là chỗ v1 kỳ vọng hook quá khả năng.*

| Lớp | Cơ chế | Cưỡng chế bởi | Chặn được gì | Không chặn được gì |
|---|---|---|---|---|
| **1. OS / filesystem** | quyền file, macOS TCC | hệ điều hành | truy cập ngoài phạm vi *(F10: `~/Desktop` bị chặn thật)* | mọi thứ trong phạm vi đã cấp |
| **2. Permissions** | `.claude/settings.json` → `permissions.deny` | 🟢 **client Claude Code** — *"enforced regardless of what Claude decides"* | đọc corpus · ghi narration cũ · lệnh phá hoại · sửa global scope | thao tác ngoài tool *(người tự chạy shell)* |
| **3. Hooks** | `PreToolUse` **exit 2** | 🟡 client, nhưng theo từng sự kiện | ghi đè `approved`/`published` · ghi khoá API · Write rỗng | thao tác không đi qua tool đã match; `exit 1` **không chặn** |
| **4. Git** | commit + `.gitignore` | 🟡 chỉ khi đã commit | mất dữ liệu **đã** commit; lộ secret **nếu** ignore đúng | file chưa từng commit *(F2 — đúng chỗ đang hở)* |
| **5. Instruction** | `CLAUDE.md`, `.claude/rules/`, skill | 🔴 **không cưỡng chế** — *"no guarantee of strict compliance"* | không gì cả — chỉ định hướng | mọi thứ, khi model quyết khác |

### Ba hệ quả thiết kế

1. **Luật nào mất mát không hồi phục → phải ở lớp 2 hoặc 3**, không được chỉ ở lớp 5. Ba luật đó đã ở đúng chỗ trong bản cài ✅
2. **R2 (skill predecessor) hiện chỉ ở lớp 5** → đó là lý do nó vẫn hở. Đóng thật thì phải đổi tên ở global scope *(cần chủ)*
3. **Lớp 4 đang là chỗ hở lớn nhất** — F2. Đây là P0

---

## 16. Migration Plan

*Mỗi phase có: thay đổi · validation · rollback · cổng người.*

| Phase | Thay đổi | Validation | Rollback | Human gate |
|---|---|---|---|---|
| **0 · Backup & Git** 🔴 P0 | `du` đo dung lượng text · thêm text vào git · commit baseline · ghi hash snapshot | `git ls-files \| wc -l` tăng đúng số text; `git count-objects -vH` <50 MB; media vẫn untracked | `git reset --soft HEAD~1` — **không mất file, chỉ mất commit** | ✅ chủ duyệt danh sách trước khi stage |
| **1 · Tinh gọn control plane** | 5 agent → 3 · 6 skill → 5 · `RULE_REGISTRY.yaml` → `.md` · thêm `session_warn.py` · thêm `count_assets.py` | `/project-doctor` 0 FAIL · `/agents` và `/skills` liệt kê đúng · hook test chặn/cho qua | git revert phase 1 | ✅ duyệt agent nào bị gộp |
| **2 · Pilot V19** | tạo **một** `videos/SKA-0019-night-walk/` · **COPY** artefact V19 · `video.yaml` @ `revised` · chạy `/audit-script` | `videos/Video19_NightWalk/` còn nguyên · doctor pass · **so kết quả 3 agent với 6 vòng review đã có** | xoá thư mục mới | ✅ **cổng đánh giá** — 3 agent có bắt được thứ 6 vòng trước bắt được không? |
| **3 · Đánh giá chi phí vận hành** | đo: phút/video cho ceremony · số token một vòng audit · số lần chủ phải sửa tay | ghi vào `governance/MIGRATION_LOG.md` | — | 🔴 **GO/NO-GO cho phase 4-8** |
| **4 · Video đang hoạt động** | chỉ video đang làm dùng cấu trúc mới | mỗi video có `video.yaml` hợp lệ, không trùng ID | xoá thư mục | ✅ |
| **5 · Legacy index** | tạo `videos/_LEGACY_INDEX.md` — **một file, không copy gì** | 20 dòng, publish state đều `UNKNOWN` | xoá file | ✅ **D-05, D-10 phải quyết trước** |
| **6 · Tách corpus và tool** | chuyển `2_KHO_BANGHI/` ra sibling · tách `GhepVideo_*` sang repo riêng | `permissions.deny` vẫn chặn · phiên research dùng `--add-dir` chạy được | **di chuyển ngược** — đây là bước nguy hiểm nhất | 🔴 **D-15, D-16** |
| **7 · Analytics loop** | tạo `videos.csv` · chủ nhập số của **1** video · chạy postmortem đầu tiên | ≥1 dòng thật; postmortem không đưa ra luật nào từ mẫu <100 | xoá csv | ✅ chủ nhập số |
| **8 · Khai tử skill cũ** | đổi tên 2 skill global thành `zz-deprecated-*` | `/skills` không còn gợi ý chúng | đổi tên lại | 🔴 **đụng global scope — bắt buộc chủ đồng ý** |

**Nguyên tắc xuyên suốt**: phase 0-2 làm được ngay. **Phase 3 là cổng thật** — nếu ceremony tốn hơn giá trị, dừng ở phase 2 và đó vẫn là kết quả tốt.

---

## 17. Owner Decisions

*18 câu từ audit §21 + 1 phát sinh. Mỗi câu: **có bằng chứng để trả lời** hay `NEEDS_OWNER_DECISION`.*

| ID | Câu hỏi | Trạng thái | Đề xuất mặc định / căn cứ |
|---|---|---|---|
| D-01 | `WORKFLOW_Production` hay `FLOW_VietKichBan_11Cong` thắng? | **có đề xuất** | `WORKFLOW_Production` cho **toàn vòng đời**; `FLOW` cho **riêng khâu viết**. Chúng không thật sự tranh nhau — một cái rộng, một cái sâu. Ghi phân vai vào `SOURCE_OF_TRUTH` |
| D-02 | Dán bối cảnh cho người review ngoài? | **có đề xuất** | **Dán tay nghề, cấm dán chiến lược/rubric/số đếm.** Căn cứ: đối chứng vòng 6 — hai chỗ đánh nhầm biến mất. Đối chứng yếu *(đổi 2 biến)*, nhưng ép-xếp-hạng không giải thích được việc thôi đánh hedge |
| D-03 | `cartoon/clean/smooth` cấm cả ảnh video? | 🔴 `NEEDS_OWNER_DECISION` | Không có bằng chứng nào đo trên **ảnh trong video** — mọi bằng chứng đều từ thumbnail. Cần một phép đo, không phải một lựa chọn |
| D-04 | `@token` hay lặp khối chữ? | **có đề xuất** | **Lặp khối chữ.** Căn cứ mạnh: 12 sheet token **chưa bao giờ được tạo** *(audit §13.2)*, còn lặp-chữ đã sản xuất 19 video. Chọn thứ đang chạy |
| D-05 | Video nào đã đăng? | 🔴 `NEEDS_OWNER_DECISION` | **Không được đoán.** Chỉ chủ mở Studio biết được |
| D-06 | V01 dùng bản nào? | **có đề xuất** | `Script_Video01_FINAL_deAI.txt` — mới hơn, khớp quy trình có bước de-AI, và `FINAL.txt` **trùng md5 với một file trong kho lưu trữ** → nhiều khả năng là bản trước polish. **Cần chủ xác nhận** |
| D-07 | Review V18 đã áp chưa? | 🔴 `NEEDS_OWNER_DECISION` | Không có bản sau review, không có feedback lưu → không suy được |
| D-08 | Ink Explainer còn là hình mẫu? | **có đề xuất** | **Tách hai vai**: Ink Explainer là hình mẫu **cấu trúc/độ dài**; Mack và Mogo là hình mẫu **doanh thu** (RPM 5,90 và 7,66 vs 3,64). Không cần chọn một |
| D-09 | Vault 873 byte đáng lẽ chứa gì? | 🔴 `NEEDS_OWNER_DECISION` | Có thể là stub, có thể bị cắt cụt. Chỉ chủ biết đã từng có gì |
| D-10 | ID cho V01 và hai V17? | **có đề xuất** | `SKA-0001-body-hair` · `SKA-0017-rain` *(bản đã sản xuất)* · `SKA-0020-death` *(bỏ dở — cấp số mới, tránh hậu tố)*. **Cần chủ duyệt trước phase 5** |
| D-11 | Luật nào đã bỏ mà chưa xoá? | 🔴 `NEEDS_OWNER_DECISION` | Chỉ chủ biết cái nào còn dùng trong đầu |
| D-12 | Số liệu nào đáng tin? | **có đề xuất** | **Không cái nào.** Mọi số đo trên 12–13 quan sát. Đề xuất: coi tất cả là `not_usable_as_benchmark` cho tới khi có ≥100 quan sát |
| D-13 | Claude Code hay claude.ai Projects? | **có đề xuất** | **Claude Code** — mọi instruction nằm ở `~/.claude/`, project dùng `.claude/`, hook và permission chỉ chạy ở Claude Code. Đường dẫn `~/Claude/Projects/` chỉ là chỗ đặt thư mục |
| D-14 | Kênh khác dùng chung namespace skill? | 🔴 `NEEDS_OWNER_DECISION` | Có ít nhất 5 skill thuộc ngách khác, nhưng không suy được chúng còn hoạt động không |
| D-15 | Tách corpus ra ngoài repo? | **có đề xuất** | **Có, nhưng ở phase 6.** `permissions.deny` đã chặn đọc, nên rủi ro cấp bách đã giảm. Di chuyển 530 MB là thao tác nguy hiểm, để sau khi git đã bao phủ |
| D-16 | Pipeline nào là chuẩn? | 🔴 `NEEDS_OWNER_DECISION` | 5 công cụ; chỉ chủ biết cái nào thật sự đang dùng để ghép video |
| D-17 | Hạ V15 xuống riêng tư? | **có đề xuất** | **Có.** Căn cứ: `00_LUAT` ghi nó đang công khai và **hỏng tiếng**, và YPP chấm **theo kênh, không theo video**. Treo từ 29/07. Chỉ chủ thao tác được |
| D-18 | Ngắn ăn view hay dài ăn RPM? | **có đề xuất** | **Ngắn**, ở giai đoạn này. Căn cứ: cửa đang chặn là **1.000 sub**, mà sub đi theo view; chênh view giữa hai nhóm là **13 lần** còn chênh RPM chỉ **1,3 lần**. Đổi sang dài **sau khi** vào YPP |
| D-19 | `/Users/admin` có nên là git repo? | **có đề xuất** | **Không.** Nó rỗng hoàn toàn (0 commit, 0 file). Đề xuất bỏ `.git` ở home để hết repo lồng — nhưng **cần chủ xác nhận** nó không phục vụ mục đích nào khác |

**Tổng: 11 có đề xuất kèm bằng chứng · 8 `NEEDS_OWNER_DECISION`.**
⛔ Không mục nào giả định trạng thái published hoặc bản final.

---

## 18. Risks and Trade-offs

| # | Rủi ro của **v2** | Mức | Đánh đổi đã chấp nhận |
|---|---|---|---|
| V2-R1 | **Cắt 5 agent → 3 có thể bỏ sót một lăng kính** | MEDIUM | Đánh đổi lấy chi phí thấp hơn. **Giảm thiểu**: phase 2 so thẳng kết quả 3 agent với 6 vòng review đã có — nếu bỏ sót, khôi phục agent thứ 4 |
| V2-R2 | **Không migrate legacy → dữ liệu cũ mãi ở cấu trúc cũ** | MEDIUM | Chấp nhận. Git bao phủ đã gỡ rủi ro **mất**; cấu trúc chỉ là tiện lợi |
| V2-R3 | **Skill predecessor vẫn hở tới phase 8** | HIGH | Không tự đóng được — cần chủ cho đụng global scope |
| V2-R4 | **CSV analytics quá thô, sau này phải chuyển schema** | LOW | Chuyển CSV→JSON rẻ. Có dữ liệu thô còn hơn không có dữ liệu |
| V2-R5 | **Git thêm ~20 MB text làm repo nặng dần** | LOW | Text nén rất tốt. Chấp nhận |
| V2-R6 | **Gộp 2 agent làm output dài hơn, khó đọc** | LOW | Giữ hai mục tách bạch trong template |
| V2-R7 | **Bỏ `knowledge/**` nghĩa là 79 file vẫn phẳng ở gốc** | MEDIUM | Chấp nhận **có chủ đích**: dọn trước khi quyết D-01…D-04 sẽ phải dọn lại lần nữa |
| V2-R8 | **Phase 6 di chuyển corpus là thao tác nguy hiểm nhất** | MEDIUM | Đặt sau git baseline nên có đường lui |
| V2-R9 | **`CLAUDE.md` phồng lên khi nhân đôi luật từ lớp 4** | LOW | Còn dư 103 dòng. Theo dõi bằng `/doctor` |
| V2-R10 | **Kiến trúc vẫn không chữa bệnh A** | — | **Không phải rủi ro — là giới hạn phải nói thẳng.** Kiến trúc bảo vệ và học; nó không tạo ra hiển thị |

---

## 19. Acceptance Criteria

*Đo được, kiểm được.*

| # | Tiêu chí | Cách đo | Ngưỡng đạt |
|---|---|---|---|
| AC-1 | Text của dự án được git bao phủ | `git ls-files \| wc -l` | **≥ 900** *(hiện 40)* |
| AC-2 | Media không lọt vào git | `git ls-files \| grep -cE "\.(png\|jpg\|mp3\|mp4)$"` | **0** |
| AC-3 | Repo không phình | `git count-objects -vH` | **< 50 MB** |
| AC-4 | Doctor sạch | `python3 tools/project_doctor.py` | **0 FAIL** |
| AC-5 | Số agent | `ls .claude/agents/*.md \| wc -l` | **3** |
| AC-6 | Agent đều read-only | mọi file có `tools:` không chứa `Write`/`Edit` | **3/3** |
| AC-7 | `CLAUDE.md` trong giới hạn chính thức | `wc -l CLAUDE.md` | **< 200** |
| AC-8 | Ba luật sống-còn ở lớp cưỡng chế được | grep trong `settings.json` + `guard_project.py` | **3/3** |
| AC-9 | Hook chặn đúng | test `approved.md` → exit 2; test `templates/x.md` → exit 0 | **2/2** |
| AC-10 | Không suy ra published | mọi `video.yaml` + `_LEGACY_INDEX.md` | **100% `not_published` hoặc `UNKNOWN`** |
| AC-11 | Asset khớp số | `python3 tools/verify_images.py` | báo đúng 3 video lệch đã biết *(V12, V14, V15)* |
| AC-12 | Pilot V19 có đối chứng | so 3 agent vs 6 vòng review | **≥70%** lỗi lớn của vòng 5-6 được bắt lại |
| AC-13 | Vòng analytics khởi động | `analytics/channel/videos.csv` | **≥1 dòng dữ liệu thật** |
| AC-14 | Không luật nào từ mẫu nhỏ | mọi mục mới trong RULE_REGISTRY | **0** mục có `sample_size < 100` |
| AC-15 | Dữ liệu cũ nguyên vẹn | `ls -d Video*/ \| wc -l` · md5 narration | **19** thư mục · md5 khớp |
| AC-16 | Global scope không bị sửa *(trước phase 8)* | `find ~/.claude/skills -newermt <mốc>` | **0 file** |

---

## 20. Implementation Backlog

| Ưu tiên | Việc | Vì sao ở mức này | Ước lượng |
|---|---|---|---|
| **P0** | **Git bao phủ toàn bộ text** *(phase 0)* | R1 là rủi ro cao nhất còn lại; V02–V16 mỗi video **một file không lịch sử** | 15 phút |
| **P0** | **Hash snapshot trước khi đụng gì** | v1 Phase 0 có nêu, bản cài bỏ qua | 5 phút |
| **P1** | `tools/verify_images.py` *(⚠️ 07/08: từng ghi là `count_assets.py` "cần làm mới" — thật ra ĐÃ TỒN TẠI từ 25/07, nằm lạc ở gốc kho nên không ai thấy)* | 3 video đang lệch mà không ai biết; đúng nguyên nhân V15 hỏng tiếng | 30 phút |
| **P1** | Gộp 5 agent → 3, hạ anti-AI xuống skill | giảm chi phí vận hành, bỏ chồng lấn | 45 phút |
| **P1** | Hook `SessionStart` cảnh báo skill predecessor | R2 hiện chỉ ở lớp 5 | 20 phút |
| **P1** | `RULE_REGISTRY.yaml` → `.md` | không validate được vì thiếu `pyyaml` (F9) | 20 phút |
| **P2** | Pilot V19 + đối chứng với 6 vòng review | phép thử thật cho cả hệ agent | 1 giờ |
| **P2** | `analytics/channel/videos.csv` + nhập số 1 video | mở lại vòng phản hồi | 20 phút |
| **P2** | `videos/_LEGACY_INDEX.md` | thay migration 19 video | 30 phút *(cần D-05, D-10)* |
| **P3** | Đối chiếu Tầng A rubric trên **52 bản ghi Mack thật** | treo lâu nhất trong kho; nay đã có Mack | 2 giờ |
| **P3** | Dán biển ⛔ cho `BOCTACH_4Kenh_SoSanh` | file duy nhất chết-trong-sổ mà không có biển | 2 phút *(cần chủ cho sửa)* |
| **P3** | Dọn `MEMORY.md` — bỏ nguyên văn 8 memory đã chết | 14 KB nạp mỗi phiên, chứa luật đã bị bác | 20 phút *(cần chủ — đụng global memory)* |
| **P4** | Đổi tên 2 skill predecessor thành `zz-deprecated-*` | cách **duy nhất** đóng thật R2 | 10 phút *(cần chủ)* |
| **P4** | Gỡ `.git` ở `/Users/admin` | hết repo lồng | 2 phút *(cần D-19)* |
| **LATER** | Tách corpus ra sibling | cần D-15, cần git baseline trước | 1 giờ |
| **LATER** | Gộp 5 pipeline thành 1 | cần D-16 | 1 ngày |
| **LATER** | `knowledge/**` + migrate tài liệu | cần D-01…D-04 | 1 ngày |
| **LATER** | Option B đầy đủ | cần ≥2 video/tuần + ≥3 postmortem | — |
| **LATER** | Option C / agent teams | cần ≥3 video song song + teams hết experimental | — |

---

## 21. Final Recommendation

### GIỮ từ v1 — phần lõi của v1 là đúng

- **Editor duy nhất, agent review read-only** — trụ cột đúng nhất, chữa thẳng R10
- **Không ghi đè kịch bản; `approved`/`published` bất biến** — chữa R3
- **Không suy ra `published`** — chữa nguồn gốc của D-05
- **`DECISIONS_REQUIRED.md`** — thành phần giá trị cao nhất; nó biến 18 mâu thuẫn từ nợ ngầm thành nợ có tên
- **ID bất biến · claim ledger · `video.yaml` · lifecycle 16 trạng thái**
- **`CLAUDE.md` <200 dòng + path-scoped rules**
- **Không dùng agent team hằng ngày** — v1 kết luận đúng, chỉ thiếu dẫn chứng trạng thái experimental

### SỬA

1. **Git phải bao phủ toàn bộ text**, không chỉ control plane — thay đổi quan trọng nhất
2. **5 agent → 3**; anti-AI critic thành skill
3. **Bỏ giả định project-override-global**; ghi đúng cơ chế và ba cách xử lý thật
4. **Nhân đôi luật sống-còn lên `CLAUDE.md`** vì rules không sống sót `/compact`
5. **`permissions.deny` lên lớp 1**, hook xuống lớp 2
6. **Analytics: CSV nhập tay trước, schema sau**
7. **`RULE_REGISTRY` YAML → Markdown** *(F9)*
8. **Thêm `count_assets.py`** — v1 thiếu hẳn

### BỎ

- **Migration V01–V19** → một file index
- **Cây `knowledge/**` 9 thư mục** → giữ tài liệu tại chỗ
- **`analytics.schema.json` và `review-verdict.schema.json`** → hoãn/bỏ
- **`/verify-claims` như skill riêng** → thành bước tự động trong `/apply-review`
- **`pipeline/` · `migration/` · `archive/`** → chưa cần

### CHƯA LÀM — và nói rõ vì sao

| Việc | Chặn bởi |
|---|---|
| Hợp nhất tài liệu tri thức | D-01, D-03, D-04 chưa quyết |
| Tách corpus, gộp pipeline | D-15, D-16 |
| Điền publish state | D-05 — **không được đoán** |
| Đổi tên skill predecessor | cần chủ cho phép đụng global scope |
| Option B, Option C | chưa đủ quy mô |

### Điều kiện GO / NO-GO

**✅ GO ngay cho phase 0-2** *(git baseline · tinh gọn control plane · pilot V19)*:
- Không phase nào đụng dữ liệu cũ ngoài việc **thêm vào git**
- Mọi phase có rollback bằng `git reset --soft`
- Pilot V19 chỉ **copy**, không move

**🔴 NO-GO cho phase 4-8 cho tới khi qua cổng phase 3.** Cổng đó hỏi đúng một câu:

> *Ceremony của kiến trúc này có tốn ít hơn giá trị nó tạo ra không?*

Đo bằng: phút mỗi video cho việc điền form · số token mỗi vòng audit · số lần chủ phải sửa tay thứ hệ thống làm sai.

Nếu câu trả lời là **không**, dừng ở phase 2. **Một kênh solo với git baseline, ba giám khảo read-only và một editor duy nhất đã có đủ mọi thứ mà kiến trúc có thể cho.** Phần còn lại là hạ tầng cho một quy mô chưa tồn tại.

---

*Hết đề xuất. Không thành phần nào được triển khai trong nhiệm vụ này.*

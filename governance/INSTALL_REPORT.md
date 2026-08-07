# INSTALL REPORT — Sketchapiens production control plane v1

**Ngày cài:** 2026-08-06
**Kiểu cài:** INSTALL-IN-PLACE. Không tạo project mới, không dùng ZIP, không migration dữ liệu.

| | |
|---|---|
| **Project root** | `/Users/admin/Claude/Projects/Build Channel Người Que Cổ Đại/` |
| **Specification** | `/Users/admin/Downloads/Sketchapiens_Architecture_Upgrade_v1.md` — 316 dòng, 10.375 B, đọc **đầy đủ** |
| **Audit** | `governance/PROJECT_FULL_AUDIT_EXPORT.md` — 1.449 dòng, 149.590 B, đọc **đầy đủ** *(do chính phiên này tạo)* |
| **Git commit** | `bc43b57` — `chore: install Sketchapiens production control plane v1` |
| **Doctor** | **PASS 33 · WARN 2 · FAIL 0** |
| **Kết luận** | ✅ **GO cho pilot V19** — xem điều kiện ở cuối |

---

## 1. Preflight

| Danh sách | Số mục | Nội dung |
|---|---|---|
| **ADD_SAFE** | 39 | Toàn bộ control plane — **không đường dẫn nào va chạm** |
| **MERGE_REQUIRED** | 0 | — |
| **SKIP_EXISTING** | 0 | — |
| **NEEDS_HUMAN_DECISION** | 19 | 18 mục từ audit §21 + 1 mục mới về Git |

**Kiểm Git lúc preflight:** `git rev-parse --is-inside-work-tree` trả `true` tại project root — vì **`/Users/admin` là git repo** với **0 commit / 0 file tracked**. Project tự nó chưa có `.git`.

**Kiểm secret lúc preflight:** không có `.env` thật trong project. Chỉ có `automation-pipeline/.env.example` chứa placeholder. Không giá trị secret nào được sao chép vào bất kỳ file nào.

---

## 2. Files created — 39

### CLAUDE.md và cấu hình
| File | Vai trò |
|---|---|
| `CLAUDE.md` | Luật phiên, **97 dòng** *(spec yêu cầu <200)*. 10 luật không phá · 4 chế độ · override skill cũ · 6 lệnh · lifecycle · bảo mật · ngôn ngữ |
| `.gitignore` | Chỉ theo dõi control plane. Chặn secret · corpus · media · file sinh cỡ lớn · node_modules · target |
| `.claude/settings.json` | 13 lệnh `deny` *(rm -rf, git clean, reset --hard, force push, git add .)* · chặn đọc corpus và file cỡ lớn · chặn ghi narration cũ và `approved/published` · chặn sửa global scope · 5 mục `ask` · hook PreToolUse |
| `.claude/settings.local.example.json` | Mẫu để tắt skill predecessor trong riêng repo này. **Đã gitignore bản `.local.json` thật** |

### `.claude/agents/` — 5 giám khảo độc lập, **tools chỉ đọc**
`cold-viewer` · `retention-architect` · `promise-payoff-judge` · `evidence-prosecutor` · `anti-ai-narration-critic`

Cả 5 đều ghi rõ **"không viết lại, không đề xuất câu thay thế"**. Ba giám khảo đầu bị cấm đọc research/rubric.

### `.claude/rules/` — 6 luật phân phạm vi qua `paths:`
`script-files` · `evidence-files` · `packaging-files` · `production-files` · `analytics-files` · `archive-files`

### `.claude/skills/` — 6 quy trình
`new-video` · `audit-script` · `apply-review` · `verify-claims` · `project-doctor` · `postmortem`

### `.claude/hooks/guard_project.py` — 6 luật cưỡng chế, **đã test chạy thật**
1. `approved.md` / `published.md` bất biến → chặn *(đã test: exit 2)*
2. Không ghi đè `vNNN` đã tồn tại
3. Narration cũ `Video*/Script_*_narration.txt` read-only
4. Không Write rỗng lên file đang tồn tại
5. Chặn ghi chuỗi giống khoá API thật vào file
6. Chặn sửa global skills / memory từ trong project

Test cho qua: ghi `templates/abc.md` → exit 0 ✅

### `governance/` — 7 file
| File | Nội dung |
|---|---|
| `SOURCE_OF_TRUTH.md` | Bảng phạm vi → **file thật đang tồn tại**, kèm cột "đích migration (chưa làm)". 5 luật ưu tiên. Danh sách "không phải nguồn chuẩn" |
| `DECISIONS_REQUIRED.md` | **19 quyết định**, tất cả ở `NEEDS_HUMAN_DECISION` |
| `RULE_REGISTRY.yaml` | **26 luật đang hiệu lực**, mỗi luật có source · confidence · evidence · status. Mục `disputed` trỏ về 6 quyết định treo |
| `RETIRED_RULES.md` | 8 luật đã khai tử đủ 2 bước · **5 file chết nhưng chưa dán biển đủ** · 7 con số đã bị đo lại và bác |
| `CHANGE_POLICY.md` | 5 điều kiện thêm luật · quy tắc khai tử 2 bước · 4 bài học đã trả giá · bảng ai được đổi gì |
| `MIGRATION_LOG.md` | 1 dòng đã làm + 7 việc chưa làm kèm lý do |
| `INSTALL_REPORT.md` | file này |

### `schemas/` — 4, **tất cả parse được**
`video.schema.json` *(16 trạng thái lifecycle, ID bất biến, publish mặc định `not_published`)* · `claim-ledger.schema.json` *(4 nhãn + thang vượt 0-3)* · `analytics.schema.json` *(mọi chỉ số bắt buộc kèm `sample_size`)* · `review-verdict.schema.json` *(`triaged_by` phải là người)*

### `templates/` — 6
`video.yaml` · `claim-ledger.md` · `review-consolidated.md` · `analytics-video.md` · `postmortem.md` · `publish-record.md`

### `tools/`
`project_doctor.py` — 9 nhóm kiểm, read-only, không phụ thuộc thư viện ngoài

---

## 3. Files modified — **0**

Không file nào đang tồn tại bị sửa, đổi tên, di chuyển hay xoá.

## 4. Files skipped — **0**

Không có va chạm nên không phải bỏ qua file nào.

---

## 5. Conflicts

**Không có xung đột file.** Nhưng bản đặc tả có **3 chỗ lệch với phạm vi lần cài này** — đã xử lý bằng cách **không thực hiện**, ghi lại tại đây:

| Spec yêu cầu | Trạng thái | Vì sao |
|---|---|---|
| Cây `knowledge/**` 9 thư mục con | **CHƯA tạo** | Là migration nội dung. Nhiệm vụ giới hạn ở control plane. Bảng `SOURCE_OF_TRUTH.md` trỏ tới file thật thay thế |
| `videos/SKA-0019-night-walk/` | **CHƯA tạo** | Spec xếp việc này ở Phase 2 pilot. Nhiệm vụ cấm chạy pilot V19 |
| `analytics/` · `pipeline/` · `migration/` · `archive/` · `README.md` · `CHANGELOG.md` | **CHƯA tạo** | Không nằm trong danh sách được phép của nhiệm vụ. `CHANGELOG` thay bằng `governance/MIGRATION_LOG.md` |

⚠️ **Xung đột nội dung ĐÃ TỒN TẠI SẴN, không giải quyết** — giữ nguyên trạng thái, ghi vào `DECISIONS_REQUIRED.md`:

| ID | Xung đột |
|---|---|
| D-01 | `kho/1_luat/WORKFLOW_Production.md` ↔ `kho/1_luat/FLOW_VietKichBan_11Cong.md` cùng quản khâu viết |
| D-02 | `kho/1_luat/LENH_GPT_ReviewKichBan_v3.md` **đầu file cấm** dán bối cảnh, **cuối file đảo lại** |
| D-03 | `cartoon`/`clean`/`smooth`: skill chia-shot **bắt buộc dùng**, template thumbnail **cấm tuyệt đối** |
| D-04 | `@token` *(CastBible, BasePack01)* ↔ lặp khối chữ *(hai skill chia-shot)* |

Control plane **không chọn bên** ở cả bốn. `.claude/rules/packaging-files.md` ghi thẳng: *"Không tự chọn bên."*

---

## 6. Unresolved decisions — 19, tất cả `NEEDS_HUMAN_DECISION`

D-01 nguồn chuẩn khâu viết · D-02 dán bối cảnh review · D-03 phạm vi 3 chữ cấm · D-04 hệ thống nhân vật · D-05 video nào đã đăng · D-06 bản V01 nào là final · D-07 review V18 đã áp chưa · D-08 Ink Explainer còn là hình mẫu không · D-09 vault 873 byte · D-10 ID cho V01 và hai V17 · D-11 luật nào đã bỏ mà chưa xoá · D-12 số liệu nào đáng tin · D-13 môi trường chính · D-14 kênh khác dùng chung skill · D-15 tách corpus · D-16 chọn pipeline chuẩn · D-17 hạ V15 xuống riêng tư · D-18 ngã ba ngắn/dài · **D-19 🆕 `/Users/admin` có nên là git repo**

---

## 7. Doctor output

```
✅ Control plane đủ file            10/10
✅ .claude/agents ≥5                thấy 5
✅ .claude/rules ≥6                 thấy 6
✅ .claude/skills ≥6                thấy 6
✅ schemas ≥4                       thấy 4
✅ templates ≥6                     thấy 6
✅ JSON hợp lệ                      tất cả parse được
✅ frontmatter 5 agent · 6 rule · 6 skill
✅ hook cú pháp hợp lệ + có quyền chạy
⚠️  videos/ chưa có video nào       (dự kiến — migration là bước riêng)
✅ Không có secret                  quét 109 file
✅ .gitignore che đủ
✅ Thư mục video cũ còn nguyên      19 thư mục
✅ File gốc kho còn nguyên          81 file .md/.txt
✅ còn 00_LUAT_HIEN_HANH.md · governance/PROJECT_FULL_AUDIT_EXPORT.md · 2_KHO_BANGHI/00_KHO.md
⚠️  Quyết định còn treo             19 mục
────────────────────────────────────
   PASS 33   WARN 2   FAIL 0
```

Cả 2 WARN đều **đúng dự kiến**, không phải lỗi.

---

## 8. Git

| | |
|---|---|
| Hành động | `git init` **trong project** *(repo riêng)* |
| Staged | **đúng 39 file**, liệt kê tường minh. **Không** dùng `git add .` |
| Commit | `bc43b57` |
| Chưa track | 116 mục — toàn bộ dữ liệu cũ, đúng chủ đích |
| Repo cha `/Users/admin` | **0 file tracked, 0 commit — không bị đụng** |

⚠️ **Cảnh báo:** đây là **repo lồng** bên trong repo `/Users/admin`. An toàn ở hiện tại vì repo cha rỗng hoàn toàn. Xem D-19.

**Rollback:** `git -C "<project>" reset --soft HEAD~1` rồi xoá thủ công 39 file. Dữ liệu cũ không nằm trong git nên **không thể bị rollback làm hỏng**.

---

## 9. Warnings

| # | Cảnh báo | Mức |
|---|---|---|
| W1 | **Repo lồng.** Project là git repo nằm trong repo `/Users/admin` | MEDIUM — xem D-19 |
| W2 | **Dữ liệu cũ vẫn ngoài git.** 19 thư mục video + 79 file gốc + corpus **chưa được bảo vệ**. Rủi ro R1 của audit **chưa được gỡ** — control plane chỉ bảo vệ chính nó | **HIGH** |
| W3 | **Skill predecessor vẫn tự kích hoạt.** Đã override bằng `CLAUDE.md §3` và `.claude/rules/`, nhưng **không có cưỡng chế kỹ thuật** — chúng vẫn có thể nạp. Nhiệm vụ cấm sửa global scope | **HIGH** |
| W4 | `settings.json` chặn đọc corpus và file cỡ lớn — nếu phiên research cần đọc, phải nới tạm hoặc dùng `--add-dir` | LOW |
| W5 | `project_doctor.py` đọc YAML bằng regex vì máy **không có `pyyaml`**. Đủ cho `video.yaml` phẳng, không đủ cho YAML lồng phức tạp | LOW |
| W6 | Đếm "quyết định còn treo" ra 19–20 tuỳ cách đếm chuỗi trong file | LOW |

---

## 10. Xác nhận không đụng gì

| Kiểm | Kết quả |
|---|---|
| Global skills bị sửa sau khi bắt đầu cài | **0 file** |
| Global memory bị sửa | **0 file** |
| Thư mục video bị di chuyển / đổi tên | **0** — vẫn 19 thư mục `Video*/` |
| Narration bị sửa | **0 file** |
| Corpus bị sửa | **0 file** |
| File gốc kho bị sửa | **0** *(ngoài `CLAUDE.md` mới tạo)* |
| Corpus bị đọc hàng loạt | **Không** — chỉ đếm/đo bằng script |
| Secret bị commit | **Không** — quét 109 file, 0 hit |
| Dùng `rm -rf` / `git clean` / `git reset --hard` / force | **Không** |
| Dùng `git add .` | **Không** — stage tường minh 39 đường dẫn |
| Tự tạo trạng thái approved/published | **Không** |

---

## 11. 💡 Đề xuất bổ sung ngoài spec

*Ghi lại để chủ quyết, **chưa thực hiện**.*

| # | Đề xuất | Vì sao | Chi phí |
|---|---|---|---|
| P1 | **Git bao phủ dữ liệu cũ trước khi làm gì khác** | W2 là rủi ro cao nhất còn lại. Control plane hiện chỉ bảo vệ chính nó; V02–V16 vẫn một-file-không-lịch-sử. Chỉ cần thêm `Video*/**/*.md` và `Video*/**/*.txt` vào git *(media đã bị ignore)* — vài MB | thấp, gỡ rủi ro lớn nhất |
| P2 | **Snapshot hash toàn kho** *(spec Phase 0 có, chưa làm)* | Có hash thì mới chứng minh được về sau rằng file cũ không bị đụng | thấp |
| P3 | **Hook `SessionStart` cảnh báo skill predecessor** | W3 hiện chỉ chặn bằng chữ. Một hook in cảnh báo đầu phiên sẽ khoẻ hơn nhiều so với hy vọng model đọc `CLAUDE.md §3` | thấp |
| P4 | **`tools/verify_images.py` *(⚠️ 07/08: từng ghi là `count_assets.py` "cần làm mới" — thật ra ĐÃ TỒN TẠI từ 25/07, nằm lạc ở gốc kho nên không ai thấy)*** — đếm ảnh vs mp3 vs shotline cho mọi video | Audit tìm ra V12 265/255 · V14 608/302 · V15 568/564 lệch mà **không ai biết**. Đây đúng là nguyên nhân V15 hỏng tiếng | thấp |
| P5 | **Ghi số Mack thật vào `RULE_REGISTRY`** sau khi đối chiếu Tầng A trên 52 bản ghi | Tầng A đúc từ Mack mà 4 tháng không truy được kênh. Nay có bản ghi thật — đây là việc treo lâu nhất | trung bình |
| P6 | **`analytics/channel/` + một lần nhập số Studio thủ công** | R4: vòng phản hồi đang đứt hẳn. Chỉ cần một file có thật là `/postmortem` chạy được | thấp |
| P7 | **Đưa `2_KHO_BANGHI/` ra sibling ngoài repo** *(spec §9)* | Đã gitignore nên không vào git, nhưng vẫn nằm trong thư mục làm việc → vẫn có thể bị mở nhầm khi đang viết | trung bình — cần D-15 |
| P8 | **Dán biển ⛔ cho `kho/3_bangchung/BOCTACH_4Kenh_SoSanh_2026-08-04.md`** | File duy nhất chết-trong-sổ mà **không có biển**, và nó chứa mốc "trung vị 18.500" đã đo lại ra 6.001. Nhiệm vụ cấm sửa file gốc nên chưa làm | rất thấp — cần chủ cho phép sửa 1 dòng |

---

## 12. GO / NO-GO cho pilot V19

### ✅ **GO**

**Đủ điều kiện:**
- Doctor 0 FAIL · 39/39 file đúng chỗ · hook đã test chặn và cho qua đúng
- 5 agent read-only, không agent nào sửa được kịch bản
- `/audit-script` → `/apply-review` tách bạch: chấm và sửa là hai bước, ngăn cách bằng phân loại của **người**
- Bằng chứng có schema và template; luật "chạy lại cổng sau khi thêm câu" đã thành luật cưỡng chế
- Git có điểm quay lui cho control plane
- V19 là ứng viên tốt nhất: đã qua 6 vòng review, có `CHOT_V19.md` với bảng cổng, có `MONEO_V19.md` là claim ledger hoàn chỉnh nhất kho

**Điều kiện kèm theo khi chạy pilot:**
1. **COPY, không MOVE** artefact V19. `videos/Video19_NightWalk/` phải còn nguyên.
2. **Không** đặt `script_approved` — V19 chưa được chủ duyệt chính thức.
3. `publish.state` = `not_published`.
4. Trước khi cấp ID, xử lý **D-10** *(V01 và hai V17)* để tránh sinh quy ước ID mâu thuẫn.
5. Chạy `/project-doctor` sau khi tạo khung.
6. So kết quả `/audit-script` với 6 vòng review đã có — đây là phép **đối chứng** cho chính hệ thống agent.

### Chưa GO cho những việc khác
Migration V01–V18 · gộp pipeline · dọn 79 file gốc · tách corpus — đều cần quyết định ở `DECISIONS_REQUIRED.md` trước.

---

**Trạng thái cài đặt: HOÀN TẤT. Dừng theo yêu cầu — không chạy pilot V19.**

# SỔ MIGRATION

| Ngày | Việc | Phạm vi | Kết quả |
|---|---|---|---|
| 2026-08-07 | **Sửa theo landscape research** — gộp 3 agent, đổi sang mô hình con trỏ, tách ID thực thi | `.claude/**` · `schemas/` · `templates/` · `tools/` | ✅ xong — xem bên dưới |
| 2026-08-06 | **Cài control plane v1** | `CLAUDE.md` · `.claude/**` · `governance/` · `schemas/` · `templates/` · `tools/` · `.gitignore` · git init | ✅ xong — xem `INSTALL_REPORT.md` |

## CHƯA làm — nằm ngoài phạm vi lần cài này

| Việc | Vì sao hoãn |
|---|---|
| Tạo `knowledge/**` và copy tài liệu canonical | migration nội dung, cần quyết D-01…D-04 trước |
| Tạo `videos/SKA-*/` và map V01–V19 | cần chủ quyết ID cho V01 và hai V17 *(D-10)* |
| Tạo `analytics/**` với số liệu thật | chưa có số liệu nào trong project |
| Tách corpus ra sibling ngoài repo | cần chủ quyết *(D-15)* |
| Gộp 5 pipeline thành một | cần chủ quyết *(D-16)* |
| Dọn 79 file ở gốc kho | bị cấm trong lần cài này |
| Giải 18+1 quyết định | thuộc thẩm quyền chủ dự án |

**Không file cũ nào bị xoá, đổi tên hay di chuyển trong lần cài này.**


---

## 07/08/2026 — Sửa theo `FACELESS_VIDEO_ARCHITECTURE_LANDSCAPE_RESEARCH_2026-08-07.md`

*Tài liệu 1096 dòng, đã đọc đủ. Mọi khẳng định về Claude Code trong đó đã kiểm chứng lại
từ `code.claude.com/docs` trước khi áp — không tin thẳng.*

### Đã làm

| # | Việc | Nguồn | Vì sao |
|---|---|---|---|
| **1** | **5 agent → 3.** `cold-viewer` + `promise-payoff-judge` + `retention-architect` → `viewer-retention-judge` | §5.4 + §12 | Subagent **nạp đủ `CLAUDE.md` và project rules** — đã kiểm chứng. `cold-viewer` không thể lạnh. Xem `RETIRED_RULES.md` |
| **2** | **Con trỏ thay bản sao.** `versions/vNNN.md` bất biến + `refs/{current,approved,published}.yaml` đổi được | §4.5 *(Prism)* | Bản sao trôi khỏi nguồn được; con trỏ thì không. Và nó **trả lời được câu V01 không trả lời được**: ba file tên `FINAL`, không ai biết bản nào đã dùng *(D-06)* |
| **3** | **Tách ID thực thi khỏi ID sáng tạo.** `runs[]` có `status` riêng | §4.7 *(VideoClaw)* · §9.3 | Schema cũ nhét trạng thái chạy máy vào trạng thái video → một lần gen ảnh hỏng làm bẩn trạng thái cả video |
| **4** | **Hook đổi hướng cưỡng chế** | — | Version bất biến · con trỏ đổi được · nhưng `approved`/`published` phải có `set_by: owner`. **7/7 test đúng** |

### Chưa làm — để V20, không đụng V19

| # | Việc | Nguồn | Vì sao đáng làm |
|---|---|---|---|
| **5** | **Run manifest** — mỗi lần gen một thư mục, ghi *số mong đợi · số ra · chỉ số thiếu · hash* | §16 | V12 265/255 · V14 608/302 · V15 568/564 **lệch mà không ai biết**, và V15 hỏng tiếng vì thế. Qua đúng tiêu chí "chỉ giữ thứ chặn được lỗi đã xảy ra thật" — lỗi này xảy ra **ba lần** |
| **6** | **TTS chạy TRƯỚC chia shot** | §4.3 *(video_explainer)* | *"Timing is an artifact"* — có timing thật thì không phải ước lượng giây/ảnh. **Cả buổi 07/08 vật lộn với wpm chính là hệ quả của việc ước lượng.** ⛔ Đừng đổi cho V19 — 191 shot đã chia xong |
| **7** | **Claim STALE khi version đổi câu số liệu** | §15 | Tự động, thay cho luật phải nhớ *"câu thêm sau cổng 3 phải chạy lại cổng 3"* |
| **8** | **Gộp code pipeline dùng chung** | §16 | 6 bản `run_pipeline.py`, 5 bản `2_assemble_video.py` — sửa một chỗ không lan sang chỗ khác. Cần **D-16** |
| **9** | **Corpus ra thư mục anh em, gắn bằng `--add-dir`** | §14 | Mạnh hơn `permissions.deny`. Cần **D-15**. ⚠️ Lưu ý tài liệu ghi chưa đủ: `--add-dir` **không** nạp `CLAUDE.md` của thư mục đó nhưng **có** nạp `.claude/skills/` bên trong |

### Không áp — có lý do

`knowledge/` 7 thư mục con · `pipeline_defs/longform_faceless.yaml` · `shared_assets/` — đều là
**migration nội dung**, mà D-01…D-04 chưa quyết. Dựng cây rỗng rồi để trống là thêm chỗ để trôi.

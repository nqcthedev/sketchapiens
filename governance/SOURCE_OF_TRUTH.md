# NGUỒN CHUẨN THEO PHẠM VI

*Lập 2026-08-06 khi cài control plane v1. Mỗi câu hỏi có **đúng một** file là luật.*

> **Bản đặc tả kiến trúc đề xuất chuyển nội dung sang `knowledge/**`. Việc đó CHƯA làm.**
> Đây là **migration nội dung**, nằm ngoài phạm vi lần cài này. Bảng dưới trỏ tới **file đang tồn tại thật**.
> Không file canonical nào bị sửa, đổi tên hay di chuyển chỉ vì destination đã được đề xuất.

## Luật ưu tiên — dùng khi hai file nói ngược nhau

1. `CLAUDE.md` + `.claude/rules/**` **thắng** mọi file trong kho.
2. Trong kho: **tầng thấp hơn thắng** *(theo `00_LUAT_HIEN_HANH.md`)*.
3. **Số đếm tay trên nguồn gốc thắng MỌI báo cáo.**
4. File ngày mới hơn thắng — **chỉ khi cùng tầng**.
5. Không giải quyết được → **đo lại**, đừng chọn bừa. Nếu cần người quyết → `DECISIONS_REQUIRED.md`.

## Bảng phạm vi

| Phạm vi | Nguồn chuẩn HIỆN TẠI *(file thật trên disk)* | Đích migration *(chưa làm)* | Ghi chú |
|---|---|---|---|
| Luật phiên làm việc | `CLAUDE.md` | — | mới, canonical |
| Luật theo khu vực | `.claude/rules/*.md` | — | mới, canonical |
| **Roadmap kiến trúc / kế hoạch nâng cấp** | **`governance/MASTER_UPGRADE_PLAN.md`** | — | **roadmap canonical, KHÔNG phải sổ luật nội dung** |
| **Story structure / structural retention — cấu trúc câu chuyện / giữ chân bằng cấu trúc** | **`.claude/skills/sketchapiens-story-engine/CONTRACT.md`** + runtime `SKILL.md` | — | **Story Engine sở hữu structural causality · belief progression · explanatory progression · structural stress test.** Retention skill cũ không được override phạm vi này. |
| **Experimental mechanism lifecycle — vòng đời cơ chế thử nghiệm** | **`.claude/skills/sketchapiens-story-engine/references/candidate-lifecycle.md`** + data `mechanism-lab.md` | — | **R&D knowledge flow, KHÔNG phải luật runtime.** Lifecycle sở hữu status/promotion/firewall; lab chỉ giữ candidate data. |
| **Retention craft support — kỹ thuật retention cấp câu/hook/nhịp** | `.claude/skills/sketchapiens-giu-chan-nguoi-xem/SKILL.md` | — | **supporting legacy module**, không phải structural authority; các observation cũ không tự biến thành template bắt buộc. |
| **Narration generation / Writer orchestration / prose realization — tạo lời đọc / điều phối phiên viết / hiện thực hóa câu chữ** | **`.claude/skills/sketchapiens-viet-kich-ban/CONTRACT.md`** + runtime `SKILL.md` | — | Writer sở hữu prose + VI-first/EN-last orchestration + diễn đạt verdict đã resolved. **Structure → Story Engine; factual verdict → Evidence; research/packaging/production không thuộc normal Writer.** Legacy monolith chỉ provenance/rollback, không default runtime. |
| **Evidence semantics / factual + bridge verdict — ngữ nghĩa bằng chứng / phán quyết claim + đường nối** | **`.claude/skills/sketchapiens-evidence-engine/CONTRACT.md`** + runtime `SKILL.md` | — | Evidence Engine sở hữu `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE`, claim↔source fit, provenance/transfer, relation-level bridge/synthesis verdict và lockability. `evidence-prosecutor` là execution persona; Story chỉ flag Narrative Overreach; Writer chỉ diễn đạt verdict đã resolved. |
| **Claim-ledger machine shape — shape sổ bằng chứng máy đọc** | **`schemas/claim-ledger.schema.json`** | — | Canonical runtime artifact cho video `SKA-*` là `02-research/claim-ledger.json`. `templates/claim-ledger.json` là bootstrap; `templates/claim-ledger.md` chỉ transitional/legacy human view. |
| **Video state vocabulary + artifact shape — tên trạng thái + shape artifact** | **`schemas/video.schema.json`** | — | schema sở hữu enum/shape; `CLAUDE.md` chỉ mô tả đường vận hành, không tạo bộ state thứ hai |
| Bản đồ tri thức cũ | `00_LUAT_HIEN_HANH.md` | `governance/` | **không sửa trong phiên thường** |
| Lifecycle sản xuất chi tiết | `kho/1_luat/WORKFLOW_Production.md` | `knowledge/production/` | mô tả quy trình nghiệp vụ; **không sở hữu enum trạng thái của `video.yaml`** |
| Cổng viết kịch bản | `kho/1_luat/FLOW_VietKichBan_11Cong.md` | `knowledge/writing/script-gates.md` | ⚠️ **D-01: chưa rõ file nào thắng khi chồng lấn với workflow** |
| Chất lượng kịch bản | `kho/1_luat/RUBRIC_KichBan.md` *(đọc LUẬT 0 trước)* + `kho/1_luat/HE_THONG_KichBan_v2_14Video.md` | `knowledge/writing/script-rubric.md` | Tầng A đúc từ Mack — nay đã có 52 bản ghi Mack thật để kiểm |
| Review ngoài | `kho/1_luat/LENH_GPT_ReviewKichBan_v3.md` + `kho/1_luat/LENH_GPT_BoiCanh_TayNghe.md` | `knowledge/writing/external-review.md` | ⚠️ **D-02: hai file mâu thuẫn nhau về việc dán bối cảnh** |
| Review nội bộ | `.claude/agents/*.md` + `/audit-script` | — | mới, canonical |
| Chọn đề tài | `kho/3_bangchung/BANG_CAU_TatCa_CuNo_2026-07-29.md` + tra bầy clone **live** | `knowledge/topic-title/` | |
| Vì sao đề tài hay vẫn chết | `kho/3_bangchung/NGHIENCUU_CloneSwarm_2026-07-29.md` | | |
| Title | `kho/1_luat/HE_THONG_KichBan_v2_14Video.md` PHẦN C | `knowledge/topic-title/` | |
| Thumbnail | skill project-local `sketchapiens-thumbnail` | `knowledge/packaging/` | |
| Phong cách hình | **`identity/style.py`** *(nguồn chuẩn duy nhất — file thật sự sinh ảnh)* + skill project-local `sketchapiens-chia-shot` *(chia shot, không phải bản sắc)* | `knowledge/visual/` | ⚠️ **D-03: `clean/smooth/cartoon` — bắt buộc hay bị cấm?** |
| Nhân vật | **`identity/style.py`** *(khối `ANCIENT` · `MODERN` · `WOMAN` · `GROUP`)* · `Prompts_NhanVat_Kenh` · `SOP_NhatQuan_NhanVat` | `knowledge/visual/` | ⚠️ **D-04: `@token` hay lặp chữ? 4 file, không file nào thắng** |
| Chính sách YouTube | `kho/1_luat/CHINHSACH_YOUTUBE_2026_AnhHuong.md` | `knowledge/policy/` | |
| Đối thủ | `kho/3_bangchung/BOCTACH_16Kenh_2026-08-05.md` + `2_KHO_BANGHI/00_KHO.md` | `knowledge/positioning/` | `BOCTACH_4Kenh` đã chết nhưng chưa dán biển |
| Corpus đối thủ | `2_KHO_BANGHI/` — **chỉ để ĐO** | tách ra sibling ngoài repo | đã gitignore |
| Số liệu kênh | **chưa có file nào** | `analytics/` + `videos/*/08-analytics/` | số duy nhất nằm trong memory toàn cục |
| Hiện trạng kho | `governance/PROJECT_FULL_AUDIT_EXPORT.md` | — | bằng chứng, không phải luật |

## Cái gì KHÔNG phải nguồn chuẩn

| | Vì sao |
|---|---|
| ⛔ skill toàn cục `viet-kich-ban-nguoi-que-co-dai` | không có tiền tố nên tự kích hoạt; PHẦN 9 trỏ tới template thumbnail đã bị bác |
| ⛔ skill toàn cục `chia-shot-va-prompt-anh` | project này dùng **project-local** `sketchapiens-chia-shot`; global skill cũ không phải nguồn chuẩn |
| ⛔ `_KHO_LUU_DaChet/**` | đã khai tử |
| ⛔ `BANDO_NgachTitle_Thang.md` · `NGHIENCUU_Title_3Kenh_Gap_*.md` · `_BO_TRAIN_*` · `kho/4_luutru/TRAIN_ChatGPT_TOANBO_DuAn.md` *(phần chiến lược)* · `BOCTACH_4Kenh_SoSanh_*.md` | chết trong sổ, vẫn nằm cạnh file sống |
| ⛔ `Video*/_cu/**` · `Video*/_nhap/**` | bản nháp |
| ⛔ `**/PROMPTS_FULL.txt` và file sinh cỡ lớn | không đọc vào ngữ cảnh |

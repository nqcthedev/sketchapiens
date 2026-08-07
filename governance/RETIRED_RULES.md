# SỔ KHAI TỬ — luật đã bị bác

*Nhập từ `00_LUAT_HIEN_HANH.md` và `PROJECT_FULL_AUDIT_EXPORT.md` §18 khi cài control plane v1.
Bảng này là **bản ghi**, không phải hành động. Không file nào bị xoá hay di chuyển trong lần cài này.*

## Đã khai tử đủ hai bước *(có biển ⛔ + có trong sổ)*

| Luật / file | Vì sao chết | Thay bằng | Đang ở |
|---|---|---|---|
| `HE_THONG_KichBan_v1_11Video.md` | v2 bác 4 luật; mẫu 11 video thiếu 3 quả triệu view | `HE_THONG_KichBan_v2_14Video.md` | `_KHO_LUU_DaChet/` |
| `HE_THONG_Thumbnail_Signature_v3.md` | khuôn "caveman trái ↔ người-que phải" bị v6 cấm | `PROMPT_TONG_Thumbnail_v6.md` | `_KHO_LUU_DaChet/` |
| `HE_THONG_Thumbnail_v5_ScriptToPackaging.md` | v6 thay | v6 | `_KHO_LUU_DaChet/` |
| `TEMPLATE_Thumbnail_DoiThu.md` | ADN "nhân vật lệch trái + vật bên phải" bị bác | v6 CENTRE ANCHOR | `_KHO_LUU_DaChet/` |
| `SUBNGACH_KhaiThac_Can.md` | lane "về BẠN" — **0 cú nổ / 4 tháng** | `BANG_CAU_TatCa_CuNo` | `_KHO_LUU_DaChet/` |
| `SUBNGACH_CoTheDoDa_2026-07-13.md` | cùng lane, cùng lý do | như trên | `_KHO_LUU_DaChet/` |
| `CongThuc_Title_TrieuView.md` | nhắm mọi title vào lane đã chết | `HE_THONG_KichBan_v2` PHẦN C | `_KHO_LUU_DaChet/` |
| `SoTay_ChonDeTai_20DeTaiDaChungMinh.md` | thay bằng số live | `BANG_CAU_TatCa_CuNo` | `_KHO_LUU_DaChet/` |

## ⚠️ Chết trong sổ nhưng CHƯA dán biển đầy đủ — vẫn nằm cạnh file sống

| File | Có biển? | Rủi ro |
|---|---|---|
| `BANDO_NgachTitle_Thang.md` | ✅ | nằm ở gốc kho |
| `NGHIENCUU_Title_3Kenh_Gap_2026-07-11.md` | ✅ | nằm ở gốc kho |
| `TRAIN_ChatGPT_TOANBO_DuAn.md` | ✅ *(phần chiến lược)* | phần tay nghề vẫn dùng — trạng thái hỗn hợp |
| `_BO_TRAIN_ChatGPT_ReviewKichBan_v2.md` | chỉ có tiền tố `_BO_` | không có trong sổ gốc |
| `BOCTACH_4Kenh_SoSanh_2026-08-04.md` | ❌ **không có biển** | chứa mốc *"trung vị 18.500"* — **đo lại ngày 06/08 ra 6.001** |

→ Đã bù bằng `.claude/rules/archive-files.md`: cả năm file nằm trong `paths:` và **không được dùng làm căn cứ**.

## Con số đã bị đo lại và bác

| Ghi trong kho | Đo từ nguồn gốc 06/08 |
|---|---|
| Ink Explainer quả 769K *"~1.000 từ"* | **1.198 từ** |
| Before Civilization *"sàn 7.000 · trung vị 18.500"* | **trung vị 6.001 · sàn 1.266** |
| Simply A Stickman *"trung vị 510"* | **295** |
| *"trần ngách 7,83 triệu"* | Barely Evolved có quả **9,53 triệu** |
| Thumbnail *"sáng 80-110"* | tương quan với view ≈ **0** |
| Thumbnail *"chữ 13-19%"* | thật ra **22%** |
| *"đối thủ vẽ sạch digital, không run tay"* | khung 4K cho thấy **có run tay** |


---

## ⛔ KHAI TỬ 07/08/2026 — "SUBAGENT LÀ NGƯỜI XEM LẠNH"

| | |
|---|---|
| **Luật đã chết** | Dùng custom subagent `cold-viewer` làm người xem không biết gì về kênh |
| **Chết vì** | Tài liệu chính thức Claude Code |
| **Thay bằng** | `viewer-retention-judge` *(gộp 3 agent)* + **review ngoài bằng ChatGPT là lớp lạnh duy nhất** |

**Nguyên văn tài liệu** *(`code.claude.com/docs/en/sub-agents`, truy cập 07/08/2026)*:

> *"**CLAUDE.md files**: every level of the CLAUDE.md hierarchy the main conversation loads,
> including `~/.claude/CLAUDE.md`, project rules, `CLAUDE.local.md`, and managed policy files.
> The built-in Explore and Plan agents skip this."*
>
> *"Explore and Plan are the only subagents that omit CLAUDE.md and git status.
> **There is no frontmatter field or per-agent setting to change which agents skip them.**"*

**Hệ quả:** agent `cold-viewer` cài ngày 06/08 mang dòng *"bạn không biết gì về kênh này"* —
nhưng thực tế nó nạp 10 luật không phá, 6 file `.claude/rules/`, luật giọng, luật đại từ.
Prompt bảo nó quên đi chỉ là chữ, không phải cơ chế.

**Ba agent bị gộp làm một** *(git giữ lịch sử, xem commit trước 07/08)*:
`cold-viewer.md` · `promise-payoff-judge.md` · `retention-architect.md` → `viewer-retention-judge.md`

Lý do gộp: khi cold-viewer không thể lạnh, giữ nó tách khỏi hai agent kia không còn lý do —
cả ba đều nhận cùng bộ đầu vào *(title + thumbnail + lời đọc)* và cùng truy vết payoff nằm ở đâu.

**Giá trị CÒN LẠI của subagent** — thật, không phải hão: **ngữ cảnh riêng.** Nó không thấy
lý lẽ mà người viết đã dùng để tự thuyết phục mình trong cuộc trò chuyện chính.

⚠️ **Đừng dựng lại "agent lạnh" lần nữa.** Không có cấu hình nào làm được điều đó.

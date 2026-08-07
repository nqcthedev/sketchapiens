# SỔ KHAI TỬ — luật đã bị bác

*Nhập từ `00_LUAT_HIEN_HANH.md` và `governance/PROJECT_FULL_AUDIT_EXPORT.md` §18 khi cài control plane v1.
Bảng này là **bản ghi**, không phải hành động. Không file nào bị xoá hay di chuyển trong lần cài này.*

## Đã khai tử đủ hai bước *(có biển ⛔ + có trong sổ)*

| Luật / file | Vì sao chết | Thay bằng | Đang ở |
|---|---|---|---|
| `HE_THONG_KichBan_v1_11Video.md` | v2 bác 4 luật; mẫu 11 video thiếu 3 quả triệu view | `kho/1_luat/HE_THONG_KichBan_v2_14Video.md` | `_KHO_LUU_DaChet/` |
| `HE_THONG_Thumbnail_Signature_v3.md` | khuôn "caveman trái ↔ người-que phải" bị v6 cấm | `kho/1_luat/PROMPT_TONG_Thumbnail_v6.md` | `_KHO_LUU_DaChet/` |
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
| `kho/4_luutru/TRAIN_ChatGPT_TOANBO_DuAn.md` | ✅ *(phần chiến lược)* | phần tay nghề vẫn dùng — trạng thái hỗn hợp |
| `_BO_TRAIN_ChatGPT_ReviewKichBan_v2.md` | chỉ có tiền tố `_BO_` | không có trong sổ gốc |
| `kho/3_bangchung/BOCTACH_4Kenh_SoSanh_2026-08-04.md` | ❌ **không có biển** | chứa mốc *"trung vị 18.500"* — **đo lại ngày 06/08 ra 6.001** |

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

---

## ⛔ `I ≈ 0` — gỡ khỏi bốn RÀNG BUỘC CỨNG *(07/08/2026 · chủ duyệt)*

**Luật cũ:** *"`I` ≈ 0 — 14/14 winner"*, một trong bốn ràng buộc cứng của LUẬT 0.
**Kèm theo:** `you:we 1,5–2` ở mục A12.

**Vì sao chết.** Luật đúc từ **11 kịch bản** hồi chưa có kho bản ghi. Nay đo trên **200 bản ghi
thật** trong `2_KHO_BANGHI/`, chia mỗi kênh làm đôi theo **mật độ "I" / 1000 từ** *(chia theo
mật độ chứ không theo số đếm, để độ dài hai nhóm khớp nhau)*:

Chạy **cả 18 kênh**; 12 kênh cho phép so sạch *(độ dài hai nhóm lệch <15%)*:
**9 kênh nhóm nhiều "I" thắng · 3 kênh thua.**

| kênh | ít "I" | nhiều "I" | |
|---|---|---|---|
| Zenn | 26.359 | **363.607** | **13,79×** |
| Primal Glitch | 2.735 | **37.939** | **13,87×** |
| **Mack** — chính nguồn đúc ra luật | 17.895 | **164.311** | **9,18×** · dài 3.468 vs 3.301 |
| Stickly | 10.539 | **30.065** | **2,85×** · dài 3.519 vs 3.453 |
| Rune · Myrk · SuperJoy · Mogo · Simply A Stickman | | | 1,26× → 5,71× |
| ⛔ **Ink Explainer** — hình mẫu của dự án | **657.575** | 144.601 | **0,22×** ngược chiều |
| ⛔ Paint Explainer (n=139) | 1.480.730 | 1.234.301 | 0,83× |
| ⛔ MrHell | 2.165 | 1.806 | 0,83× |

Khử biến tuổi video: chia riêng nửa cũ / nửa mới của 3 kênh → **6/6 lần so cùng chiều**.
Ở Before Civilization nhóm dùng "I" còn *mới hơn* mà vẫn thắng.

🔴 **9/12, không phải 12/12.** Kênh đi ngược mạnh nhất lại chính là hình mẫu **Ink Explainer**.
→ Kết luận **không phải** "dùng I thì thắng", mà là **"I" không đủ tư cách làm luật cứng theo
bất kỳ chiều nào**. Đừng dựng luật mới ngược lại.

⚠️ **Bài học phương pháp.** Bản đầu của mục này chỉ chạy **4 kênh** — đúng 4 kênh là nguồn của
rubric — và ra bảng 100% cùng chiều. Chủ hỏi *"trong kho có quá trời kênh mà sao lấy mỗi 2 kênh"*;
chạy hết 18 kênh thì lòi ra 3 ca ngược. **Chọn tập con theo thói quen là tự tạo ra sự nhất trí giả.**

`you:we 1,5–2`: Mack **1,17** *(dưới dải)* · Stickly 1,50 · Before Civilization 2,73 ·
Zenn **5,00** · Ink Explainer **5,69**. Không có dải nào cả.

**Luật thay:** mục A12 nay là — `you` = người xem · `we` = cả loài · **người dẫn ĐƯỢC có ý
kiến riêng**. Không kèm con số mục tiêu nào *(LUẬT 0: đo được không có nghĩa là đích)*.

**Giới hạn.** Tương quan, không phải nhân quả. "I" là **dấu hiệu của người dẫn có quan điểm**,
không phải nguyên nhân. Sáu kênh bị loại khỏi phép so vì độ dài hai nhóm lệch quá 15%
*(Axen · Before Civilization · Bright Psycho · ExtinctZoo · Historical Architect)* — ở đó không
tách được ảnh hưởng của "I" khỏi ảnh hưởng của độ dài.

🔴 **Nguyên tắc chủ chốt cùng ngày:** *"mùi ChatGPT nhưng kịch bản hay với nhiều view thì vẫn
ok hơn là kịch bản quá nghiêm khắc rồi chả có view nào."*

---

## ⛔ MỌI TỈ LỆ HÌNH ẢNH — khai tử 07/08/2026

Cả **bốn** ngưỡng dưới đây đều chết cùng một lý do: **đúc từ hai kênh**.

| ngưỡng | ở đâu | đúc từ |
|---|---|---|
| `~50% thẻ dạy học` | skill `chia-shot` PHẦN 4 | 96 khung, đếm **bằng mắt**, 2 kênh |
| `40% thẻ / 60% cảnh` | bản tôi sửa **sáng 07/08** | 1.090 khung, đo **bằng máy**, vẫn chỉ **2 kênh** |
| `thẻ 30-45%` · `cảnh 55-70%` · `chữ 40-70%` | `validate_shots.py` | như trên |
| `~50% khung phải có chữ` | skill PHẦN 2 + PHẦN 5 | 72 khung của **một** video |
| `2,0-2,5 giây/ảnh` · `~2,8-3,0 giây/shot` | skill PHẦN 1 + đuôi file | 1 và 3 video |

**Bằng chứng giết cả bốn** — bảng 4-5 kênh đo 05/08, nằm ngay `PHẦN 0` của chính skill đó:

| kênh | nền trắng | giây/ảnh | trung vị |
|---|---|---|---|
| Mack | **36%** | 4,3 | **45.000** |
| Explain In Paint | 50% | 2,5 | 11.000 |
| Simply A Stickman | ~60% | 2,6-3,3 | 510 |
| **Zenn** | **80%** | 2,7 | 29.000 |

`36→45K` · `50→11K` · `60→0,5K` · `80→29K`. **Không có quan hệ nào.** Nhịp cũng vậy: 2,5 giây cho
cả 11.000 lẫn 29.000; 4,3-4,6 giây cho cả 45.000 lẫn 10.000. Và **Zenn chạy 80% nền trắng vẫn thắng**
→ câu *"V17 hỏng vì 75% thẻ"* **không đứng được**.

**Luật thay:** chọn nền theo **ngữ cảnh từng shot** *(khái niệm → thẻ · khoảnh khắc → cảnh)*; nhịp
chọn theo **chi phí sản xuất**, không theo niềm tin nó ăn view. Vẫn **đếm và ghi lại** tỉ lệ để sau
đối chiếu với view thật — nhưng không có ngưỡng đạt/trượt.

⚠️ **Đây là lần thứ TƯ.** Ba lần trước cũng sửa luật hình từ một ảnh hoặc một mẫu thưa, và cả ba sai
theo ba hướng khác nhau. Lần này tôi đổi 50% thành 40% **trong khi bảng bốn kênh nằm ngay đầu cùng
file đó đã bác** — không phải thiếu dữ liệu, mà là **không đọc lại thứ mình đang sửa**.

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

---

## ⛔ RUBRIC — các con số đã bị đuổi theo sai *(gom 07/08/2026 từ chính rubric)*

| Số | Chuyện gì |
|---|---|
| **Giác quan 7–9%** | ❌ đo cùng từ điển thì V17 chỉ **5,2%**, V19 **5,5%** — hai bên dùng **thước khác nhau**, không phải kịch bản kém |
| **Mỏ neo 3,2–5,1/phút** | ❌ V19 đo ra **12,2** — cũng là thước khác nhau |
| **you:we 1,5–2** | ❌ đo 200 bản ghi: Mack **1,17** *(dưới dải)* · Stickly 1,50 · Before Civilization 2,73 · Zenn **5,00** · Ink Explainer **5,69** |
| **Độ dài 9–12 phút** | ⚠️ Ink Explainer: quả **1M = 11:37**, quả **769K = 6:04**, quả 1,5M chỉ **1.543 từ** |
| **Nhịp hài 30–60 giây** *(A10)* | ⚠️ **thừa hưởng từ benchmark sai** — đúc từ Stickly, mà Stickly là kênh **trúng số** *(trung vị 27.000, top-1 chiếm 45%)*. Đếm trên quả **769K của Ink Explainer: đúng 1 câu đùa trong 6 phút**, ít hơn rubric 6–12 lần. → nhắm **vài nhịp cả bài**, không phải mỗi phút một nhịp |

## 🔧 Rubric — bốn lỗi đã vá 29/07/2026

| Lỗi | Đã làm gì |
|---|---|
| **B5 thưởng điểm cho lane đã chết** — *"lật MỌI chương về BẠN"*. Lane "về BẠN" verify **0 cú nổ / 4 tháng**; 11/15 video của kênh xây trên đó và flop hết | tách đôi: giữ **cú xoay cuối** *(14/14 winner có)*, bỏ "mọi chương" |
| **Ngưỡng tự mâu thuẫn** — cùng một tầng, chỗ ghi ≥52/60, chỗ ghi ≥40 | thống nhất thang **72** |
| **Mục 8 và 26 ép cú lật phải nằm ở CUỐI** | winner rải **55%→88%** → bỏ ép vị trí, chỉ chấm *có* cú lật + *có* báo trước |
| **Mục 12 cấm tuyệt đối "I"** — Predators đếm thật có **2** lần | sửa thành "gần bằng 0" *(và 07/08 gỡ hẳn — xem mục trên)* |

Cùng đợt bổ sung **A7**: 6 đặc điểm winner rubric cũ thiếu hẳn, gồm luật nhất quán nhất cả bộ dữ liệu — **dấu `!` = 0 (14/14)**.

---

# ⛔ THUMBNAIL — hai luật đo lường đã chết *(gom 07/08 từ `PROMPT_TONG_Thumbnail_v6.md`)*

## ⛔ LUẬT "CHỮ 13-19%" ĐÃ CHẾT *(bác 03/08/2026)*

Ngày 29/07 tôi sửa luật thành **chữ 13-19% chiều cao**, kèm câu *"kênh đang để 21-23%, ăn mất chỗ của cảnh"*. Đo lại bằng máy trên **hai bộ ảnh độc lập**:

| Bộ | Chiều cao chữ vàng |
|---|---|
| 21 ảnh style đối thủ *(chủ gửi 03/08)* | **21 – 22%** |
| 29 quả thắng `../3_bangchung/NGHIENCUU_Thumbnail_50K/` | **trung vị 22%** |

→ **Ngưỡng đúng là ~22%, không phải 13-19%.** Lần "sửa" 29/07 là một bước lùi — kênh lúc đó đang làm đúng. Thumbnail V18 bản 2 để 15% chính là hậu quả.

## ⛔ LUẬT "ĐO TÔNG" ĐÃ CHẾT *(bác 03/08/2026)*

Luật cũ ghi **sáng 80-110 · bão hoà 15-30%**, rút ra từ vài thumbnail của Mack. Đo lại bằng máy trên **cả 29 quả thắng** trong `../3_bangchung/NGHIENCUU_Thumbnail_50K/` *(55K → 7,81M view)*:

| | Trung vị | Khoảng giữa 50% | Min → Max |
|---|---|---|---|
| Độ sáng | **130** | 98 – 153 | 63 → 174 |
| Bão hoà | **29** | 22 – 39 | 15 → 49 |

Ngưỡng cũ 80-110 **nằm dưới cả khoảng giữa** — nó loại oan phần lớn quả thắng.

**Nhưng quan trọng hơn con số:** tương quan với view là **sáng −0,10 · bão hoà −0,09**. Tức là **cả hai không dự báo gì cả**. Quả 7,81M sáng 92 bão hoà 18; quả 62K sáng 74 bão hoà 49. Không có hướng nào.

→ **Đừng dùng hai chỉ số này làm cửa.** Chúng chỉ để biết mình có đang lạc ra ngoài lãnh thổ của quả thắng hay không *(ngoài 63-174 và 15-49 thì mới đáng lo)*. Hai cửa thật sự còn lại là **đọc được ở 168×94** và **hình chứng minh điều chữ nói** — đó là hai thứ có lý do nhân quả, không phải tương quan rỗng.

---

# PHỤ LỤC — HAI QUAN SÁT NGƯỢC TRỰC GIÁC

**Cấm kỵ KHÔNG phải điều kiện cần.** 5/7 quả thắng có yếu tố cấm kỵ vẽ thẳng, nhưng **hai quả cao nhất (7.81M và 3.00M) hoàn toàn sạch** — không máu, không cơ thể, không từ cấm. Quả bẩn nhất được 516K.

**Nhân vật KHÔNG cần to.** Một quả 59K có nhân vật chỉ chiếm **35% khung**, nằm dang tay giữa cảnh wide, không cấm kỵ, không ai to. Nó thắng bằng **tư thế + 1 đạo cụ (cây giáo bị vứt)** và **chữ chỉ chiếm 71% chiều ngang để cảnh được thở**.

---

# ⛔ RUBRIC — bốn mục gỡ khỏi thang điểm *(09/08/2026, sau khi bóc 16 kênh)*

Nguồn: `kho/3_bangchung/TONGHOP_16Kenh_2026-08-09.md` — 16 kênh cùng định dạng, mỗi kênh qua
một agent bóc và một giám khảo mở bản ghi gốc đối chiếu từng câu trích.

| mục | rubric chấm gì | 16 kênh nói gì |
|---|---|---|
| **A1.2** tự giễu loài người | *"≥1 câu tự giễu buồn cười trong 15s đầu"* | ⛔ **0 ca thắng toàn kho.** BrightPsycho **0/96 bài** *(grep 4 cụm cố định)*. Simply A Stickman dùng ở 4 bài — **cả 4 nhóm chìm**, kênh đã tự bỏ hẳn từ 31/05. Zenn: bài DUY NHẤT có người dẫn lộ diện = **516 view/ngày, nhóm THẤP** |
| **A2.8** vế *"BÁO TRƯỚC cú lật"* | câu mẫu `"one last layer I saved for the end"` | ⛔ **14/16 kênh grep 0 TUYỆT ĐỐI** trên 8 cụm hứa-hoãn. NeonRush 0 hit / 126.798 từ. Stickly 4 câu / 148.000 từ. Zenn có đúng 1 bài dùng → bài đó **nhóm THẤP**. Câu mẫu trong rubric là thứ **cả ngách không dùng** |
| **A6.26** cọc *"để dành cuối"* | signposting hứa hoãn | ⛔ cùng lý do A2.8. *(Cọc "nhiều lớp" ở mục 6 thì GIỮ — nó khác hẳn cọc hứa hoãn)* |
| **A5.23** callback hook · **A6.29** BOOKEND | video "tròn" | ⚠️ **HẠ CẤP, không bỏ.** Là **nết ~100% của ngách**: Stickly 43/43 · Simply A Stickman 47/47 · Zenn 28/28 · Mack 49/52 · BC 59/65. Bài **298 view/ngày** của Zenn callback sạch y như bài **7,83 triệu**. Chỉ số bắn trúng mọi bài là chỉ số **đo được số 0** → vẫn cứ làm, nhưng **không tính điểm** |

**Thang điểm: 36 mục / 72 điểm / ngưỡng ≥62 → 32 mục / 64 điểm / ngưỡng ≥55** *(giữ 86%)*.

## 🔴 Và điểm số đổi Ý NGHĨA, không chỉ đổi thang

Trước: *"ĐẠT NGANG = ngang đối thủ, có cơ sở ăn view"*. **Sai.**

**L3** — cùng một kênh, cùng khuôn hook, cùng khuôn title, cùng bút pháp → view chênh
**42 đến 1.938 lần**. SuperJoy 1.938× *(9 bài/37 ngày)* · PaintItSimple 304× *(hai bài cách nhau
2 ngày)* · NeonRush 42× *(cách nhau 1 ngày)*. Ca đắt nhất: **Axen** — bài chìm chép lại **cả 5 mỏ
neo** của bài thắng *(Wiessner + Ju/'hoansi · Blombos · Chauvet · "for 99% of human history" ·
"bands of 15 to 50 people")*, giám khảo grep xác nhận có thật ở cả hai file → **kém 67,5 lần**.

→ Điểm rubric đo **register**, không đo **triển vọng**. Đạt ngưỡng = mua được vé vào cửa.
**Hook là SÀN, không phải con hào.**

⚠️ Kèm theo, **L5**: đoạn kết viết hay **KHÔNG cứu được bài**. Mack có 4 đoạn kết đẹp nhất kho,
cả 4 nằm nhóm đáy. Giám khảo Mack: *"Đọc đoạn kết mà đoán view thì đoán ngược."*

---

## 09/08/2026 (chiều) — BỐN LUẬT CẤU TRÚC A8, gỡ trong CÙNG NGÀY được thêm vào

**Cách bác:** đọc trọn 5 bài CHÌM khớp cặp với 5 bài THẮNG — cùng kênh, cùng người viết,
gần bằng nhau về số từ, chênh view/ngày **68× đến 552×**.
Bằng chứng đầy đủ: `../kho/3_bangchung/DOICHUNG_5BaiChim_2026-08-09.md`

| luật đã gỡ | vì sao chết |
|---|---|
| **41** — trả nợ title 4-15% rồi tráo đề | **5/5 bài chìm đều có**, đều nằm đúng băng *(10,1 · 4,4 · 9,8 · 4,2 · 4,6%)*. Bài 272 vpd của Ink đóng khối bằng **đúng chữ tiêu đề**. Và bài THẮNG Ink Rain hỏi lại nguyên văn tiêu đề **lần hai ở 94,0%**, phạm chính vế "trả xong thì đi luôn" |
| **44** — cú lật cấm mang dữ kiện mới | **5/5 bài chìm sạch, ba bài sạch HƠN bài thắng.** Zenn Dogs lật hai lần 0 dữ kiện mới và chìm 214×. Bài THẮNG Ink Rain **vi phạm**: cú lật ở 56,6% lôi vào Chauvet 36.000 năm · Lascaux · Altamira · Sulawesi 45.000 năm — mới tinh cả bốn, và vẫn 1,10 triệu view |
| **43a** — thang bằng chứng leo 5 bậc theo độ khó chối | **Zenn Dogs chạy 16 nấc, không tụt một nấc nào**, và chìm **214×** |
| **43b** — mỏ neo yếu nhất đặt sau 85% | rút từ **đúng một bài**. Axen **THẮNG** đặt mỏ neo **MẠNH** nhất ở đó → luật có thể **viết ngược dấu**. Nếu đo lại 6 bài thắng ra 4/6 đặt mạnh-nhất-sau-85% thì viết lại thành luật ngược, đừng chỉ xoá |
| **42b** — chương thừa nằm trước 50% | bài **THẮNG** Ink Rain đặt chương thừa ở **81,9-91,7%** |
| **27** hai cổng — "≥4 cặp cài-lật" + "≥1 cặp đầu↔cuối" | **chạy NGƯỢC CHIỀU.** Chìm đếm được 8·11·11·9·13 cặp *(trung bình **10,4**, vượt trần 8 của bài thắng)*; **5/5 có cặp đầu-cuối**, hai bài có HAI cặp |

**Còn sống:** mục **42** *(câu hỏi "xoá chương này thì gãy ở đâu", bỏ hết con số — và biết
trước rằng phép đếm này chưa lặp lại được giữa hai người đọc)* và mục **43c** *(một phép thử
người xem tự chạy được ở 85-95%: **5-6/6 thắng vs 1/5 chìm**, nhưng p ≈ 0,08 và có một phản
ví dụ mỗi phía — **không được dùng làm cổng chặn đăng**)*.

### 🔴 LUẬT PHƯƠNG PHÁP RÚT RA — quan trọng hơn cả sáu dòng trên

> ## Luật nào chưa có NHÓM ĐỐI CHỨNG thì KHÔNG được vào thang điểm. Chỉ được nằm ở mục "ghi nhận".

Đây là lần thứ **BA** dính cùng một bẫy — sau `callback hook` *(Stickly 47/47, Zenn 28/28)*
và `bookend` *(cùng lý do)*.

Điểm khác của lần này: **cảnh báo đã được viết ra trước, ngay trong cùng file, cùng ngày** —
*"chưa có nhóm đối chứng… có thể là nết của ngách chứ không phải đòn bẩy — đúng cái bẫy đã
giết mục 23 và 29"* — **rồi vẫn cho bốn luật chấm điểm, và vẫn gắn nhãn "không được chấm 0".**

**Viết cảnh báo không thay được việc chạy đối chứng.**

### Và một giả thuyết phải chết ngay, cấm mở lại hồ sơ

**"Mật độ mỏ neo có tên"** — nghe rất mạnh trong cặp Ink *(Rain 5,4/1000 từ vs Sick 0,7/1000,
chênh 7,7×)*. Nhưng `TONGHOP` **L12 đã bác bằng 14 kênh**: Zenn bài **4,02 triệu view có
1,22 mỏ neo/1000 từ, thấp thứ nhì tháng** — chỉ gấp 1,7 lần bài chìm của Ink, và thấp hơn
bài thắng của Ink 4,4 lần. **Một cặp n=1 không bác được 14 kênh.**


---

## 09/08/2026 (tối) — BỎ HẲN THANG ĐIỂM RUBRIC *(chủ ra lệnh)*

**Luật đã gỡ:** *"37 mục × 2 điểm, ngưỡng ≥64/74 (86%), không mục nào = 0"* — và mọi phiên
bản trước của nó *(62/72 · 67/78 · 64/74)*.

**Vì sao chết — ba lý do độc lập:**

1. **Ngưỡng 86% trên 37 mục = phải điền đủ ~32 ô.** Đó không phải "viết hay là qua". Chính
   rubric đã ghi hậu quả: *"ba câu mùi AI nặng nhất trong V17 đều là câu thêm vào để thoả
   Tầng A."*
2. **Bảy mục ép nhịp bằng con số** *(re-hook mỗi 60-90s · bucket brigade 20-30s · một câu
   hỏi mỗi 60-90s · mỗi chương 183-341 từ · hedge 1-3 lần · ≥2 ẩn dụ · mỗi chương một chùm
   2-4 câu dưới 6 từ)* — cùng loại số đã bị bác ba lần *(nhịp hài 30-60s · giác quan 7-9% ·
   you:we 1,5-2)*.
3. 🔴 **79 câu NGUYÊN VĂN của đối thủ nằm trong cột chấm.** AI viết ra thứ gần nhất với câu
   mẫu nó vừa đọc — nên đặt câu của đối thủ vào cột chấm là **ra lệnh viết na ná đối thủ,
   rồi thưởng khi nó làm thế**. Mục 22 **bắt buộc phải có** cụm `"Next time you…"`, cụm đó
   có trong **65/488 bản ghi đối thủ**; `"Think about that for a second."` có trong **31/488**.
   Đây không chỉ trói sáng tạo — nó đẩy về phía **ranh giới reused-content** đã làm sập một
   kênh của chủ.

**Thay bằng:** `RUBRIC_KichBan.md` hai tầng —
**PHẦN 1: 5 CỔNG** *(sản xuất · sự thật · reused-content · phép thử người xem tự chạy được ·
người nghe ngoài)*, đạt/không đạt.
**PHẦN 2: GỢI Ý NGHỀ**, không chấm điểm, **đọc SAU khi viết xong**.
79 câu mẫu chuyển sang `kho/2_nguyenlieu/KHO_CauMau_DoiThu_DungChep.md`.

✅ **Kiểm chứng kênh chưa bị nhiễm:** grep 4 kịch bản đã viết — `"never just one thing"` 0 ·
`"here's where it gets interesting"` 0 · `"Think about that for a second"` 0. Người viết đã
tự đề kháng dù luật đẩy ngược lại. Từ nay luật đẩy cùng chiều.

**Đã vá tham chiếu chết ở:** `WORKFLOW_Production.md` *(cửa 2)* · `FLOW_VietKichBan_11Cong.md`
*(cổng 7 đổi tên thành "ĐO BẰNG MÁY — in số, KHÔNG chấm")* · `sketchapiens-viet-kich-ban/SKILL.md`
· `NGHIENCUU_ThiNghiem_BaySinhDoi.md` · `00_LUAT_HIEN_HANH.md`.

---

## 09/08/2026 (đêm) — DỌN 112 LỖI SAU KHI SOÁT TOÀN TẦNG KỊCH BẢN

Soát 7 bộ file bằng 7 người soát + 1 vòng phản biện: **131 phát hiện → 112 sống sót**
*(70 NẶNG · 38 VỪA · 4 NHẸ)*, **19 bị bác (14,5%)**.

**Chẩn đoán:** kiến trúc mới *(bỏ thang điểm, 4 cổng)* chỉ được vá ở **tầng 1**. Tầng 2,
các skill, các lệnh và file video **chưa ai chạm** → chúng vẫn dạy nguyên luật đã chết.

### 🔴 Ba "cổng câm" — tưởng chạy mà thật ra không chạy

| cổng | hỏng thế nào | hậu quả đo được |
|---|---|---|
| **CỔNG A chống reused-content** *(`FLOW` L67)* | grep trỏ `Video1[0-9]*/`, đường thật là `videos/Video1[0-9]*/`. zsh trả `no matches found` → **grep không chạy, không in gì, không báo lỗi** → đọc thành "sạch" | **Đây là lý do đoạn kết V19 chép khung xương đoạn kết V18.** Chạy đúng đường thì cụm `on the safe side` hiện ra ở cả hai video |
| **Cổng 7 đo bằng máy** | `qa_kichban.py` được trỏ tới `~/.claude/skills/…` — thư mục đó có 48 skill và **không có `sketchapiens-*` nào** | cổng **chưa từng chạy được lần nào** |
| **Cổng chống inauthentic content** | `CHINHSACH_YOUTUBE` L146 ghi *"luật thêm vào cửa 1"*, nhưng cửa 1 bị rút gọn cùng ngày → grep toàn kho ra đúng một kết quả là chính dòng đó | luật **không thuộc cửa nào** trong nhiều ngày. Nay là vế thứ ba của **Cổng 3** |

### 🔴 Một cỗ MÁY đang thi hành luật đã chết

`qa_kichban.py` in `'I' {I} (≈0)` dưới nhãn **CỨNG**, và `/apply-review` lấy đó làm điều
kiện chặn → **editor duy nhất được sửa file sẽ cắt mọi câu có "I"**. Ba file khác ghi
*"4 ràng buộc cứng"* trong khi thật ra **chỉ có ba**.

**Đã sửa:** gỡ `I` khỏi nhãn CỨNG · sửa "4 ràng buộc" → **BA** ở `/apply-review` và
`/audit-script` · và **thêm phép kiểm ràng buộc cứng thứ ba mà bản cũ chưa từng có**
*(mỗi câu một dòng)* — chạy thử V19 nó bắt ngay 22 dòng vi phạm.

### Bốn ổ luật chết còn dạy — đã dán biển tại chỗ

| ổ | số chỗ | ví dụ nặng nhất |
|---|---|---|
| `I ≈ 0` | 9 *(4 chỗ bằng máy)* | trên |
| 7 con số ép nhịp | 14 | SKILL PHẦN 12 *"MÁY HÀI (bắt buộc — ÉP hài)… 0 câu đùa = CHƯA XONG, viết lại"* — trong khi PHẦN 14.7 **cùng file** ghi Zenn 7,83M có 0 câu đùa |
| lane "về BẠN" | 6 | `TearDown_7M` tự phong *"KHUÔN cho MỌI kịch bản từ nay"* — tầng 2 không được quyền phán |
| cliffhanger · tự giễu · persona | 10 | `MoXe_15Khoi` không chỉ giữ mà **dạy dùng SỚM HƠN**, gọi là *"tín hiệu mạnh nhất cho thuật toán"* |

### Cách chữa cho tầng 2

Dán **một biển chuẩn** lên đầu 8 file nguyên liệu: *"TẦNG 2 — KHÔNG ĐƯỢC PHÁN. Khi nói
ngược RUBRIC thì nghe RUBRIC. Mọi câu tiếng Anh trong đây là câu của đối thủ — chép là clone."*
Cộng vá tại chỗ những dòng đang ra lệnh bằng giọng mệnh lệnh.

`DICH_Zenn_7.8M` — **bản dịch trọn kịch bản 7,83 triệu view của đối thủ** — được biển
riêng, mạnh nhất: *"⛔ cấm mở trong chế độ ② VIẾT. Bầy clone quanh đúng quả này đo được
đỉnh 337 view."*

### 🪦 Luật gỡ thêm trong đợt này

- **Cổng "phép thử người xem tự chạy được"** — nó là **cổng giả**: nằm ở phần "chặn đăng"
  mà tự khai *"KHÔNG chặn đăng"*. Chuyển xuống PHẦN 2 §2.8. **Rubric nay còn 4 cổng.**
- **"câu hỏi lõi trước giây 31"** — n=3, và `TONGHOP` đo **ngược dấu**: nhiều kênh nhóm
  CHÌM hỏi SỚM hơn; PrimalGlitch hai bài đỉnh **0 dấu hỏi cả bài**; quả 769K của Ink đặt ở **1:06**.
- **"PACKAGING ĐI TRƯỚC KỊCH BẢN"** — băng-rôn to nhất `WORKFLOW_Production`, đã bị chính
  L70 của file đó bỏ từ 05/08 mà chưa ai gỡ băng-rôn.
- **"cắt 1,5-2 giây/ảnh"** — đo trên MỘT video; `BOCTACH_16Kenh`: 2,5 đến 4,6 giây/ảnh
  **đều thắng**. Ép 1,5-2s là nhân đôi tới gấp ba chi phí ảnh để mua một thứ chưa ai chứng minh.
- **`÷ 154` để đổi từ ra phút** — chính file đó đã khai tử hai lần *(đúng là ÷178)*; lệch
  15%, đủ để cắt oan một chương.
- **"chuẩn hiện hành: 178 wpm · 8,9 từ/câu · 37% câu ngắn"** — đo từ **V17, video 20 view**.

### Bài học phương pháp

> ## Sửa luật ở tầng 1 mà không sửa tầng 2, skill, lệnh và MÁY thì luật cũ vẫn đang chạy.
> Và **một cổng hỏng đường dẫn thì im lặng — nó không báo lỗi, nó báo "sạch".**

---

## 09/08/2026 — XOÁ `ArtBible_NguoiQueCoDai.md` + `CastBible_DienVien.md` *(chủ ra lệnh)*

**Lý do chủ:** *"mấy cái artbible với cái cast không dùng nữa đâu bạn ơi xoá luôn đi nha."*

**Và đọc trọn cùng ngày cho thấy chúng đang GÂY HẠI, không chỉ thừa** — cả hai tả một nhân
vật **khác** với `identity/style.py`, file thật sự sinh 191 ảnh mỗi video:

| chi tiết | hai file đã xoá | `identity/style.py` *(chạy thật)* |
|---|---|---|
| Mắt | `tiny black dot eyes` · *"mắt chấm / ô-van"* | `TWO LARGE ROUND WHITE EYES… **Never tiny dots**` |
| Tóc | *"tóc **đen** ÍT nét, vài sợi rối"* | `**MEDIUM BROWN**, SHAGGY MANE of fine wavy strands` |
| Tay chân | *"nét ĐẬM/DÀY, fat marker, **not thin**"* | `THIN SINGLE BLACK LINES, long and skinny` |
| Da | `@BASEHUMAN` ghi **`#E8C9A0`** — một mã **màu da** | `never skin-coloured, never peach or tan` |

Mã màu da đó nằm **ngay dưới** dòng luật *"da chung: TRẮNG, KHÔNG tô da"* cách hai dòng.
Và đó chính là lỗi đã làm **V18 bản 2 ra tỉ lệ trắng 0,3%** *(đích 2,8-5,7%)*.

**Bảy đường dẫn sống đã vá trước khi xoá:** `00_LUAT_HIEN_HANH` · `governance/SOURCE_OF_TRUTH`
· `BasePack01` · `Prompts_NhanVat_Kenh` · `SOP_NhatQuan_NhanVat` · `Brand_Kit_Kenh` *(kèm cảnh
báo chữ `cartoon` trong đó là chữ cấm)*. File nằm ở `~/.Trash/Sketchapiens_xoa_2026-08-09/`.

**Khép luôn `D-04`** *(`@token` hay lặp khối chữ)*: hai file mang hệ `@token` đã xoá →
**lặp khối chữ thắng**, đúng thứ `identity/style.py` và hai skill chia-shot vẫn làm.

### 🔴 LUẬT PHƯƠNG PHÁP — bắt được ba lần trong một buổi

> ## Khi `.md` đá với `.py` thì **`.py` thắng**.
> Nó là thứ chạy, và luật trong nó thường đã được sửa bởi **một lần gen hỏng thật**.
> Hai chữ `hedgehog hair` và `hair ball` trong NEG của `style.py` là chữ của người **đã nhìn
> thấy nó ra sai** — bằng chứng mà file `.md` không có.

Ba lần cùng dạng, cùng ngày:
1. `ArtBible` · `CastBible` · `Prompts_NhanVat` tả mắt/tóc/tay chân **sai** ↔ `style.py` đúng
2. `TEMPLATE_Thumbnail_KHOA_v1` đòi tóc `SPIKY` ↔ `style.py` **cấm** `spiky hair ball`
3. `sketchapiens-chia-shot` khối `CONSIST` chứa `clean` · `smooth` · `not wobbly` ↔ `style.py`
   có `clean`=**0**, `cartoon`=**0**, `wobbly`=**7 lần**

**Tầng `.md` chậm hơn tầng `.py` đúng một thế hệ.** Cách chữa không phải vá từng file —
là **gộp về một nguồn**, và cho `.md` trỏ tới `.py` thay vì chép lại nó.

---

## 09/08/2026 — GỘP THUMBNAIL VỀ **MỘT** NGUỒN *(chủ ra lệnh)*

**Lý do chủ:** *"về skill thumbnail dùng 1 cái skill final thôi dùng lắm vậy, cái nào cập nhật
mới thì xoá bỏ cái cũ đi — sao cứ check đống thành thùng rác vậy."*

Thumbnail có **bốn nguồn dựng trong 11 ngày**, và chúng **không khớp nhau**:

| nguồn | ngày | số phận |
|---|---|---|
| `.claude/skills/sketchapiens-thumbnail/` | **05/08** | ✅ **GIỮ** — có **nhóm đối chứng** *(8 quả cao + 4 quả thấp của CÙNG kênh, 8 kênh, 96 ảnh, 22 trường)*, và nó **tự giết 9 luật của chính mình** |
| `kho/1_luat/TEMPLATE_Thumbnail_KHOA_v1.md` | 03/08 | ⛔ xoá — prompt dán-thẳng + nhật ký đã **bê vào skill §⑥ và §⑦** |
| `kho/1_luat/PROMPT_TONG_Thumbnail_v6.md` | 29/07 | ⛔ xoá — cũ nhất, giữ nhiều luật đã bị bác |
| `kho/3_bangchung/CO_CHE_3LOP_Winner_2026-07-29.md` | 29/07 | giữ *(bằng chứng, không phải luật)* |

**Ba luật đá nhau đã bắt được trước khi gộp:**
- chữ cao **13-19%** *(chia-shot)* ↔ **~22%** *(v6, TEMPLATE)* — 15% chính là thứ làm hỏng V18 bản 2
- *"chữ phải khác title"* *(chia-shot, n=2)* ↔ **lặp title không bị phạt** *(v6, đo 44 ảnh/9 kênh: 25/36 lặp)*
- *"chữ PHẢI chứa một đại lượng"* *(v6)* ↔ **6/12 quả top không có đại lượng nào** *(skill, có đối chứng)*

**Mười ba đường dẫn đã vá trước khi xoá.** File nằm ở `~/.Trash/Sketchapiens_xoa_2026-08-09/`.

> ### 🔴 VÌ SAO CỨ CHECK LÀ RA MỘT ĐỐNG — chẩn đoán của chủ, đúng
> Kho **đo lại rất nhiều lần mà không bao giờ xoá bản cũ**. Mỗi vòng đo mới đắp thêm một tầng;
> tầng dưới vẫn nằm đó và vẫn được đọc. Thumbnail là ca rõ nhất: **4 bản trong 11 ngày**.
>
> **Luật từ nay: đo lại xong thì XOÁ bản cũ, không dán biển rồi để đó.**
> Dán biển giữ được lịch sử nhưng **vẫn là một dòng để đọc nhầm**. Lịch sử đã nằm ở file này
> và ở git — đủ rồi.

# 00 — LUẬT HIỆN HÀNH (đọc file này TRƯỚC MỌI VIỆC)

> # 🔴 CHẠY TRƯỚC MỌI VIỆC: `python3 tools/preflight.py videos/<VideoDir>`
> 10 cổng kịch bản + 6 cổng sản xuất. **Không có dấu vết = chưa chạy.** *(dựng 10/08 sau khi
> chủ phải nhắc 7 lần trong một buổi, cả 7 đều là thứ đã có sẵn trong kho)*

> # 📋 VIẾT KỊCH BẢN → MỞ `kho/1_luat/FLOW_VietKichBan_11Cong.md`
> Quy trình 11 cổng, mỗi cổng chặn một lỗi đã mắc thật. Có bảng một trang dán lên đầu mỗi video.
> Gộp: kho NotebookLM · chính sách nội dung không trung thực · ranh giới reused-content · công thức Ink Explainer.


---

## 🎛️ BỐN CHẾ ĐỘ LÀM VIỆC — gọi bằng skill, mỗi phiên MỘT chế độ

Gõ tên skill là vào đúng chế độ với đúng bộ file. **Không trộn hai chế độ trong một phiên** —
đang viết mà đi tra mỏ neo là mất mạch, đã dính nhiều lần.

| Chế độ | Skill | Cổng | Cấm |
|---|---|---|---|
| **① NGHIÊN CỨU** | `sketchapiens-chon-de-tai` | 0–3 | không viết kịch bản |
| **② VIẾT** | `sketchapiens-viet-kich-ban` *(+ `sketchapiens-giu-chan-nguoi-xem`)* | 5–6 | **không mở nexlev, không tra web** |
| **③ BIÊN TẬP** | `sketchapiens-bien-tap` | 7–9, 11 | không viết nội dung mới |
| **④ SẢN XUẤT** | `sketchapiens-chia-shot` · `sketchapiens-thumbnail` | sau khi kịch bản CHỐT | chưa qua cổng 7–9 thì chưa chia shot |

Đang ở chế độ này mà phát hiện việc của chế độ khác → **ghi vào sổ, không làm ngay**.
Gom lại, đổi chế độ, làm một lượt.

---

# 🗂️ BẢN ĐỒ KHO — 4 TẦNG *(dựng 06/08/2026)*

> **Vì sao có mục này.** Kho đã **63 file ở gốc / 719 file toàn dự án**. Ngày 06/08 chính trợ
> lý nói *"chưa vắt kho NotebookLM"* trong khi kho đã vắt từ 29/07 · không mở rubric ra chấm
> dù quy trình bắt buộc · không biết có bản dịch quả 7,8 triệu nằm ngay trong dự án.
> Không phải lười — là **không có thứ tự để biết đọc gì trước**.

## ⚖️ LUẬT ƯU TIÊN — dùng khi hai file nói ngược nhau

1. **Tầng thấp hơn thắng.** Tầng 1 phủ quyết tầng 2, 3, 4.
2. **Số đếm tay trên transcript gốc thắng MỌI báo cáo**, kể cả NotebookLM.
   *(Đã dính: báo cáo ghi Predators hedge 5 lần; đếm tay ra 1.)*
3. **File có ngày mới hơn thắng** — nhưng chỉ khi cùng tầng.
4. Không giải quyết được → **đo lại**, đừng chọn bừa.

---

## TẦNG 0 — CỬA VÀO *(1 file)*
`00_LUAT_HIEN_HANH.md` ← đang đọc. Mọi phiên mở file này trước.

## TẦNG 1 — LUẬT ĐANG HIỆU LỰC *(chỉ những file này được quyền phán)*

**1A · Kịch bản**
| File | Dùng khi |
|---|---|
| `kho/1_luat/FLOW_VietKichBan_11Cong.md` | **quy trình tổng — mở đầu tiên khi viết** |
| `kho/1_luat/HE_THONG_KichBan_v2_14Video.md` | title (C) · hook (D,F) · kết bài (G) · lắp chương (H) |
| `kho/1_luat/RUBRIC_KichBan.md` | **5 CỔNG** đạt/không đạt + **gợi ý nghề đọc SAU khi viết**. ⛔ **Bỏ thang điểm 09/08** — bản cũ bắt điền đủ 32/37 ô, và chính nó đẻ ra *"ba câu mùi AI nặng nhất trong V17"*. **Đọc LUẬT 0 trước.** |
| ~~`CONGTHUC_InkExplainer_BestOf.md`~~ | ⛔ **GỠ 10/08** — kênh nguồn bị tắt kiếm tiền vì reused content. Xương "thang thời gian" đã cứu sang `RUBRIC_KichBan.md` §2.2. Hiện vật ở `kho/4_luutru/` |
| `kho/1_luat/CHINHSACH_YOUTUBE_2026_AnhHuong.md` | QA chính sách · **luật "giống đối thủ là rủi ro KIẾM TIỀN"** |
| 🆕 `kho/1_luat/LUAT_ChonDeTai.md` | **chọn đề tài** — lấy đề tài đã có cầu rồi làm hơn · ranh giới reused-content · quy trình 5 bước |

**1B · Hình ảnh & sản xuất**
| File | Dùng khi |
|---|---|
| `kho/1_luat/WORKFLOW_Production.md` | các giai đoạn sản xuất |
| **skill `sketchapiens-thumbnail`** | thumbnail — **nguồn DUY NHẤT** *(gộp 09/08: có nhóm đối chứng 8 cao + 4 thấp/kênh, tự giết 9 luật của chính nó, kèm prompt dán thẳng)*. ⛔ `PROMPT_TONG_Thumbnail_v6` và `TEMPLATE_Thumbnail_KHOA_v1` **đã xoá** |
| **`identity/style.py`** | 🔒 **nét vẽ · khối nhân vật · bảng nền · NEG — NGUỒN CHUẨN DUY NHẤT.** Đây là file **thật sự sinh ảnh** *(`tools/build_prompts.py` nạp `from style import *`)*. ⛔ `ArtBible` và `CastBible` **đã xoá 09/08** — chúng là tài liệu chậm hơn code một thế hệ *(mắt chấm · tóc đen · tay chân mập · một mã màu da lạc)*, xem `governance/RETIRED_RULES.md` |
| `kho/1_luat/QUY_TRINH_2_CONG.md` | kiểm đầu + kiểm cuối |

## TẦNG 2 — KHO NGUYÊN LIỆU *(tra khi viết — KHÔNG được phán)*

> ### 🆕 `2_KHO_BANGHI/` — BẢN GHI GỐC 768 VIDEO / 22 KÊNH *(dựng 06/08/2026)*
> **Mở `2_KHO_BANGHI/00_KHO.md` trước.** Đây là thứ duy nhất trong kho **kiểm chứng lại được**:
> mọi khẳng định về giọng · nhịp · độ dài · mỏ neo nay đối chiếu thẳng vào lời đối thủ nói.
>
> 🔴 **Chỉ để ĐO. Cấm mở trong chế độ ② VIẾT** *(cùng lệnh cấm với nexlev và tra web)*.
>
> **Ngày đầu tiên nó đã sửa được bốn con số kho ghi sai:**
> | Kho ghi | Đo lại |
> |---|---|
> | Ink Explainer quả 769K *"~1.000 từ"* | **1.198 từ** |
> | Before Civilization *"sàn 7.000 · trung vị 18.500"* | **trung vị 6.001 · sàn 1.266** *(số cũ lấy từ top-30)* |
> | Simply A Stickman *"trung vị 510"* | **295** |
> | *"trần ngách 7,83 triệu"* | Barely Evolved có quả **9,53 triệu** |
>
> **Và nó giết một kết luận do chính nó sinh ra trong 3 phút:** so giữa các kênh thì kênh ngắn
> xếp trên, nhưng so **trong nội bộ** từng kênh thì độ dài **không dự báo view** (rho≈0, hai
> chiều ngược nhau). Độ dài là **lựa chọn định vị**, không phải chất lượng.

| File | Chứa gì |
|---|---|
| `kho/2_nguyenlieu/VAULT_AncientHumans_KnowledgeVault.md` | **SỔ MỎ NEO ĐÃ TIÊU của chính kênh** *(V17 · V17b · V18 · V19)* + sổ đen mỏ neo bị loại + **CỔNG A** quét tự-trùng-lặp. ⛔ Mô tả cũ *"8 chủ đề bóc từ 49 kịch bản đối thủ"* **chưa từng tồn tại** — file khi đó là vỏ rỗng 873 byte. Đổi chức năng 09/08 theo **D-09** |
| `kho/2_nguyenlieu/VAULT_NotebookLM_BanGoc_DoiChieu.md` | 4 báo cáo gốc đã tiêu hoá đi đâu + 6 chỗ bản máy đúng hơn bản gốc |
| `kho/2_nguyenlieu/KHO_AnDu_TruyenChem_LachLuat.md` | 16 ẩn dụ thế kỷ 21 · truyện chêm · **4 quy tắc lách kiểm duyệt** |
| `kho/2_nguyenlieu/KHO_GiongCamXuc_DoiThu.md` | 7 nhóm giọng · pre-load nhãn cảm xúc · 2 trường phái |
| `kho/2_nguyenlieu/NganHang_ReHook_BucketBrigade.md` | câu nối · **luật BOOKEND: viết câu cuối trước** |
| `DICH_Zenn_7.8M_...md` | **bản dịch quả to nhất ngách** — quét cổng A bắt buộc đọc |
| `MoXe_15Khoi_KichBan_DoiThu.md` | 15 khối kể chuyện + cách vượt *(bảng phân loại — giữ)* |
| ⛔ ~~`MoXe_KichBan_Viral_3Video`~~ · ~~`TearDown_7M_CongThuc_GuongSoi`~~ | **xoá 09/08** — bản đầu trùng 41/56 câu với `references/viral-teardown.md`; bản sau bị `kho/3_bangchung/DOC_TRON_6KichBan_2026-08-09.md` vượt qua *(đọc trọn cùng video, 8 chương thay vì 3 màn)* |
| `MAU_Script_*.md` | kịch bản mẫu |
| `BasePack01` · `Prompts_NhanVat_Kenh` · `SOP_NhatQuan_NhanVat` | prompt nhân vật |

## TẦNG 3 — BẰNG CHỨNG ĐÃ CHỐT *(đã rút thành luật ở tầng 1 — chỉ mở khi cần tra lại)*
`BOCTACH_*` (4) · `NGHIENCUU_*` (8) · `BANDO_CumChuDe_*` · `BANG_CAU_TatCa_CuNo_*` ·
`CO_CHE_3LOP_Winner_*` · `NGHIENCUU_CloneSwarm_*` · `NGHIENCUU_ThiNghiem_BaySinhDoi` ·
`BangDoiChieu_v2_vs_Viral` · `GAP_AUDIT_va_Roadmap`

## TẦNG 4 — LƯU TRỮ *(không đọc khi làm việc thường)*
Theo video: `V17_*` · `V18_*` · `CONCEPT_Thumbnail_V16_V17` · `Script_Video01_*`
Công cụ: `SPEC_*` · `PROMPT_NangCap_Tool_AnToan`
Ra lệnh AI ngoài: `TRAIN_ChatGPT_*` · `PROMPT_PACK_NotebookLM` · `PLAYBOOK_NotebookLM_DoiThu` ·
`LENH_NotebookLM_ChuaLam` · `TEARDOWN_PLAYBOOK_RaLenh_AI` · `BAY_SinhDoi_DanhSach`
Bàn giao: `BÀN_GIAO_DuAn` · `Brand_Kit_Kenh`

## ⛔ SỔ KHAI TỬ — file còn nằm trong kho nhưng đã chết

| File | Thay bằng | Đã dán biển? |
|---|---|---|
| 🆕 `kho/3_bangchung/NGHIENCUU_NguPhapHinh_InkExplainer.md` | `kho/3_bangchung/NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md` | ✅ 07/08 |

> ### 🆕 07/08 — vì sao `NGHIENCUU_NguPhapHinh_InkExplainer` chết
> Nó xem tay **96 khung lấy mẫu thưa** và ra *"khoảng một nửa số khung là đồ hoạ dạy học"*.
> File thay thế đo **1.090 khung bằng máy**: Ink Explainer **41%** · Mack **36%** → thật ra là
> **~40% thẻ / 60% cảnh**. V17 dựng trên con số sai đó và ra **75% thẻ**, ngược hẳn đối thủ.
>
> ⚠️ **Không xoá file này** vì skill `sketchapiens-chia-shot` PHẦN 4 vẫn đang trích nó — xoá thì
> skill trỏ vào khoảng không. Dán biển và để đó cho tới khi `D-20` được quyết.

*Đã xoá khỏi kho 07/08/2026: `BANDO_NgachTitle_Thang` · `NGHIENCUU_Title_3Kenh_Gap_2026-07-11` ·
`_BO_TRAIN_ChatGPT_ReviewKichBan_v2` — cả ba đã dán biển ⛔ từ 06/08 và không còn ai trích.
Cùng đợt: `Script_Video01_FINAL_MaxHai` · `Script_Video01_Why-Did-Humans-Lose-Body-Hair`
*(V01 thuộc lane "về BẠN" đã chết; V02–V16 xoá cùng ngày)*. Lịch sử git vẫn giữ.*

*Các file khai tử trước đó (SoTay_ChonDeTai · SUBNGACH_KhaiThac_Can · SUBNGACH_CoTheDoDa ·
CongThuc_Title_TrieuView · Thumbnail_Signature_v3 · Thumbnail_v5 · TEMPLATE_Thumbnail_DoiThu ·
HE_THONG_KichBan_v1) đã bị xoá khỏi kho, không còn tồn tại.*

> **Luật mới:** khai tử một file thì phải làm **cả hai việc** — ghi vào sổ này **và** dán biển
> ⛔ vào dòng đầu chính file đó. Làm một nửa thì lần sau vẫn có người mở nhầm.

---

*Soi lại toàn kho 29/07/2026. Kho có ~80 file, nhiều file mâu thuẫn nhau mà không file nào biết mình đã bị bác.*

> **Cách dùng:** mỗi câu hỏi có ĐÚNG MỘT file là luật. Không mở file nào ngoài cột "File luật".
> File đã chết đều đã dán biển ⛔ ở dòng đầu — nếu mở ra thấy biển đó, đóng lại.

---

# BẢNG PHÂN QUYỀN

| Câu hỏi | File luật | Đã thay cho |
|---|---|---|
| **Chọn đề tài / có nên làm cái này không** | 🆕 `kho/1_luat/LUAT_ChonDeTai.md` *(luật)* — số tra ở `kho/3_bangchung/BANG_CAU_TatCa_CuNo_2026-07-29.md` + **bắt buộc** tra bầy clone live | ⛔ SoTay_ChonDeTai · ⛔ SUBNGACH_KhaiThac_Can · ⛔ SUBNGACH_CoTheDoDa |
| **Vì sao đề tài hay vẫn chết** | `kho/3_bangchung/NGHIENCUU_CloneSwarm_2026-07-29.md` | *(mới)* |
| **Đặt title** | `kho/1_luat/HE_THONG_KichBan_v2_14Video.md` PHẦN C | ⛔ CongThuc_Title_TrieuView · ⛔ BANDO_NgachTitle_Thang · ⛔ NGHIENCUU_Title_3Kenh_Gap |
| **Làm thumbnail** | **skill `sketchapiens-thumbnail`** *(nguồn DUY NHẤT, gộp 09/08)* | ⛔ Thumbnail_Signature_v3 · ⛔ Thumbnail_v5 · ⛔ TEMPLATE_Thumbnail_DoiThu |
| **Cơ chế title+thumbnail+hook của winner** | `kho/3_bangchung/CO_CHE_3LOP_Winner_2026-07-29.md` | — |
| **V17 — packaging đã chốt, chờ gen thumbnail** | **`kho/4_luutru/V17_PACKAGING_CHOT.md`** | *(mới)* |
| Concept thumbnail V16 | `kho/4_luutru/CONCEPT_Thumbnail_V16_V17.md` | — |
| **Có cách phân tích nào nữa không** | 🆕 `kho/1_luat/CACH_PHAN_TICH_TOAN_BO.md` — 6 nhóm, ~50 cách, gồm cả cách CHƯA dùng *(18/08)* |
| **Bóc kịch bản đối thủ** | 🆕 `kho/1_luat/BOCTACH_KICHBAN_DOITHU.md` — 9 chiều, câu lệnh: *"bóc kịch bản <link> theo 9 chiều"* *(18/08)* |
| **Bài có hồi hộp không** | 🆕 `tools/do_kich_tinh.py` + `RUBRIC_KichBan.md` Cổng 5 *(18/08)* |
| **Viết kịch bản** | `kho/1_luat/HE_THONG_KichBan_v2_14Video.md` | ⛔ HE_THONG_KichBan_v1 · ⚠️ RUBRIC_KichBan *(xem ghi chú)* |
| **Cách nói: ẩn dụ, truyện chêm, lách kiểm duyệt** | `kho/2_nguyenlieu/KHO_AnDu_TruyenChem_LachLuat.md` | *(mới)* |
| **QUY TRÌNH SẢN XUẤT — đọc trước mỗi video** | **`kho/1_luat/WORKFLOW_Production.md`** | *(mới — packaging đi TRƯỚC kịch bản)* |
| Nguyên tắc 2 cổng | `kho/1_luat/QUY_TRINH_2_CONG.md` | — |
| **Thứ gì thật sự quyết định thắng thua** | `kho/3_bangchung/NGHIENCUU_ThiNghiem_BaySinhDoi.md` | *(mới — thí nghiệm đối chứng)* |
| **Ra lệnh cho NotebookLM — việc CHƯA làm** | **`kho/4_luutru/LENH_NotebookLM_ChuaLam.md`** | *(mới)* |
| Ra lệnh cho NotebookLM — việc đã làm + sổ theo dõi | `kho/4_luutru/PROMPT_PACK_NotebookLM.md` | — |
| **Đối thủ là ai, học ai** | **`kho/3_bangchung/BOCTACH_16Kenh_2026-08-05.md`** | ⛔ thay `BOCTACH_4Kenh_SoSanh` · ⛔ mọi chỗ coi Zenn/Axen/Stickly là hình mẫu |
| **Có bị chặn kiếm tiền không** | skill `an-toan-kiem-tien` *(dùng chung)* | *(mới)* |

## 🏷️ SKILL RIÊNG CỦA DỰ ÁN NÀY — đổi tên 05/08/2026

Trước đây skill riêng của kênh đặt tên chung chung, nên luật đo từ kênh này bị áp nhầm sang dự án khác. Nay tất cả đều có tiền tố `sketchapiens-`:

| Việc | Skill |
|---|---|
| Chốt đề tài video tiếp theo | **`sketchapiens-chon-de-tai`** |
| Viết kịch bản | **`sketchapiens-viet-kich-ban`** |
| Chia shot + prompt ảnh | **`sketchapiens-chia-shot`** |
| Thumbnail *(chữ, luật hình, dải sáng)* | **`sketchapiens-thumbnail`** |
| Giữ chân người xem / AVD | **`sketchapiens-giu-chan-nguoi-xem`** |

Skill **dùng chung** cho mọi dự án — không được ghi số đo của kênh này vào: `thiet-ke-thumbnail` · `chan-doan-kenh-youtube` · `tham-dinh-ngach-youtube` · `an-toan-kiem-tien` · `mo-xe-doi-thu` · `chong-van-ai-narration-en` · `checklist-dang-video-long-form`.

⚠️ **Luật:** đo được gì trên kênh này thì ghi vào skill `sketchapiens-*` hoặc file trong kho. Ghi vào skill dùng chung là dạy sai cho mọi dự án sau.

---

# TÁM FILE ĐÃ CHẾT — nay nằm ở `_KHO_LUU_DaChet/`

*(đã dồn khỏi gốc kho 29/07. Không xoá vì `/Users/admin` là git repo nhưng 0 commit / 0 file theo dõi → xoá là mất hẳn. Xem `_KHO_LUU_DaChet/README.md`.)*


| File | Vì sao chết |
|---|---|
| `HE_THONG_KichBan_v1_11Video.md` | v2 bác 4 luật (mẫu 11 video thiếu 3 quả triệu view) |
| `HE_THONG_Thumbnail_Signature_v3.md` | chốt khuôn "caveman trái ↔ người-que phải" — v6 CẤM |
| `HE_THONG_Thumbnail_v5_ScriptToPackaging.md` | v6 thay |
| `TEMPLATE_Thumbnail_DoiThu.md` | ADN "nhân vật lệch trái + vật bên phải" bị bác. ⛔ ~~→ CENTRE ANCHOR~~ **cũng đã bác 10/08** → nay là **Cổng 1: MỘT khối lớn ~nửa khung**, có cặp đối chứng thật |
| `SUBNGACH_KhaiThac_Can.md` | lane "về BẠN": **0 cú nổ / 4 tháng** |
| `SUBNGACH_CoTheDoDa_2026-07-13.md` | cùng lane, cùng lý do |
| `CongThuc_Title_TrieuView.md` | nhắm mọi title vào lane đã chết + giả định "title quyết định" bị bác |
| `SoTay_ChonDeTai_20DeTaiDaChungMinh.md` | thay bằng BANG_CAU (số live, 64 cú nổ) |

---

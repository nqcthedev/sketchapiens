# 00 — LUẬT HIỆN HÀNH (đọc file này TRƯỚC MỌI VIỆC)

> # 📋 VIẾT KỊCH BẢN → MỞ `FLOW_VietKichBan_11Cong.md`
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
| `FLOW_VietKichBan_11Cong.md` | **quy trình tổng — mở đầu tiên khi viết** |
| `HE_THONG_KichBan_v2_14Video.md` | title (C) · hook (D,F) · kết bài (G) · lắp chương (H) |
| `RUBRIC_KichBan.md` | chấm điểm — **đọc LUẬT 0 ở đầu file trước** |
| `CONGTHUC_InkExplainer_BestOf.md` | công thức "best-of": giữ gì, bỏ gì, thêm gì |
| `CHINHSACH_YOUTUBE_2026_AnhHuong.md` | QA chính sách |

**1B · Hình ảnh & sản xuất**
| File | Dùng khi |
|---|---|
| `WORKFLOW_Production.md` | các giai đoạn sản xuất |
| `PROMPT_TONG_Thumbnail_v6.md` · `TEMPLATE_Thumbnail_KHOA_v1.md` | thumbnail |
| `ArtBible_NguoiQueCoDai.md` · `CastBible_DienVien.md` | nét vẽ · nhân vật |
| `QUY_TRINH_2_CONG.md` | kiểm đầu + kiểm cuối |

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
| `VAULT_AncientHumans_KnowledgeVault.md` | 8 chủ đề + mỏ neo, bóc từ **49 kịch bản đối thủ** |
| `VAULT_NotebookLM_BanGoc_DoiChieu.md` | 4 báo cáo gốc đã tiêu hoá đi đâu + 6 chỗ bản máy đúng hơn bản gốc |
| `KHO_AnDu_TruyenChem_LachLuat.md` | 16 ẩn dụ thế kỷ 21 · truyện chêm · **4 quy tắc lách kiểm duyệt** |
| `KHO_GiongCamXuc_DoiThu.md` | 7 nhóm giọng · pre-load nhãn cảm xúc · 2 trường phái |
| `NganHang_ReHook_BucketBrigade.md` | câu nối · **luật BOOKEND: viết câu cuối trước** |
| `DICH_Zenn_7.8M_...md` | **bản dịch quả to nhất ngách** — quét cổng A bắt buộc đọc |
| `MoXe_15Khoi_...` · `MoXe_KichBan_Viral_3Video` · `TearDown_*` | mổ xẻ kịch bản đối thủ |
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
| 🆕 `NGHIENCUU_NguPhapHinh_InkExplainer.md` | `NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md` | ✅ 07/08 |

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
| **Chọn đề tài / có nên làm cái này không** | `BANG_CAU_TatCa_CuNo_2026-07-29.md` + **bắt buộc** tra bầy clone live | ⛔ SoTay_ChonDeTai · ⛔ SUBNGACH_KhaiThac_Can · ⛔ SUBNGACH_CoTheDoDa |
| **Vì sao đề tài hay vẫn chết** | `NGHIENCUU_CloneSwarm_2026-07-29.md` | *(mới)* |
| **Đặt title** | `HE_THONG_KichBan_v2_14Video.md` PHẦN C | ⛔ CongThuc_Title_TrieuView · ⛔ BANDO_NgachTitle_Thang · ⛔ NGHIENCUU_Title_3Kenh_Gap |
| **Làm thumbnail** | `PROMPT_TONG_Thumbnail_v6.md` | ⛔ Thumbnail_Signature_v3 · ⛔ Thumbnail_v5 · ⛔ TEMPLATE_Thumbnail_DoiThu |
| **Cơ chế title+thumbnail+hook của winner** | `CO_CHE_3LOP_Winner_2026-07-29.md` | — |
| **V17 — packaging đã chốt, chờ gen thumbnail** | **`V17_PACKAGING_CHOT.md`** | *(mới)* |
| Concept thumbnail V16 | `CONCEPT_Thumbnail_V16_V17.md` | — |
| **Viết kịch bản** | `HE_THONG_KichBan_v2_14Video.md` | ⛔ HE_THONG_KichBan_v1 · ⚠️ RUBRIC_KichBan *(xem ghi chú)* |
| **Cách nói: ẩn dụ, truyện chêm, lách kiểm duyệt** | `KHO_AnDu_TruyenChem_LachLuat.md` | *(mới)* |
| **QUY TRÌNH SẢN XUẤT — đọc trước mỗi video** | **`WORKFLOW_Production.md`** | *(mới — packaging đi TRƯỚC kịch bản)* |
| Nguyên tắc 2 cổng | `QUY_TRINH_2_CONG.md` | — |
| **Thứ gì thật sự quyết định thắng thua** | `NGHIENCUU_ThiNghiem_BaySinhDoi.md` | *(mới — thí nghiệm đối chứng)* |
| **Ra lệnh cho NotebookLM — việc CHƯA làm** | **`LENH_NotebookLM_ChuaLam.md`** | *(mới)* |
| Ra lệnh cho NotebookLM — việc đã làm + sổ theo dõi | `PROMPT_PACK_NotebookLM.md` | — |
| **Đối thủ là ai, học ai** | **`BOCTACH_16Kenh_2026-08-05.md`** | ⛔ thay `BOCTACH_4Kenh_SoSanh` · ⛔ mọi chỗ coi Zenn/Axen/Stickly là hình mẫu |
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
| `TEMPLATE_Thumbnail_DoiThu.md` | ADN "nhân vật lệch trái + vật bên phải" bị bác → CENTRE ANCHOR |
| `SUBNGACH_KhaiThac_Can.md` | lane "về BẠN": **0 cú nổ / 4 tháng** |
| `SUBNGACH_CoTheDoDa_2026-07-13.md` | cùng lane, cùng lý do |
| `CongThuc_Title_TrieuView.md` | nhắm mọi title vào lane đã chết + giả định "title quyết định" bị bác |
| `SoTay_ChonDeTai_20DeTaiDaChungMinh.md` | thay bằng BANG_CAU (số live, 64 cú nổ) |

---

# 🔴 LUẬT MỚI 05/08/2026 — GIỐNG ĐỐI THỦ LÀ RỦI RO KIẾM TIỀN, KHÔNG CHỈ RỦI RO VIEW

*Nguồn gốc: video chính thức của YouTube, Matt Koval giải thích chính sách Inauthentic Content. Không phải luật mới của YouTube — là bản làm rõ. Nhưng nó nêu đích danh thứ dự án này đang làm.*

## Phép thử phải qua

> Gỡ tên kênh và logo đi, dán video của mình cạnh 20 video cùng title của 20 kênh khác — **có ai chỉ ra được cái nào là của mình không?**

YouTube diễn đạt là: *"content that we know what channel it comes from. **It couldn't be on a hundred other channels**."*

Và: *"making the next channel that's making all the same kind of stuff is just generic, it's repetitive… the channel won't get in [YPP] in the first place."*

## Điều này đá vào đâu trong quy trình của mình

Phương pháp **"hàn title theo winner"** (`chon-de-tai-trong-ngach`, `HE_THONG_KichBan_v2` PHẦN C) tốt cho việc **được tìm thấy**, nhưng đi một mình thì rơi thẳng vào nhóm bị loại.

Đo thật 05/08: mọi đề tài tra ra ~20 kênh, mở bài gần trùng nhau —
*"Right now, you check your phone…"* · *"Tonight, you turn on the AC…"* · *"You scroll past a video of…"*
V18 của mình mở bằng *"Tonight you will go to bed behind a door that locks."* **Cùng khuôn.**

→ **Luật thêm vào cửa 1:** mỗi video phải có **ít nhất MỘT thứ mà 20 kênh kia không có** — góc kể riêng · mỏ neo khoa học chưa ai dùng · nhân vật xuyên suốt · kết cấu riêng. Không có thì chưa qua cửa.

## Ba điều làm rõ khác

| Điều | Nghĩa cho mình |
|---|---|
| **Công cụ không bị tính** — *"if you make it with gen AI, great"* | TTS + ảnh AI **không** phải vấn đề. Ngừng lo chuyện đó |
| **YPP xét theo KÊNH, không theo video** · ngưỡng là **tỉ lệ** | ⚠️ **V15 hỏng đang công khai kéo cả hồ sơ kênh xuống.** Hạ xuống riêng tư trước khi nộp YPP |
| Bị report bao nhiêu lần **cũng không ảnh hưởng** | bỏ nỗi lo bị đối thủ report |
| Trượt YPP: khiếu nại **21 ngày**, nộp lại **90 ngày** | trượt không phải án tử, nhưng mất một quý |

## ⛔ Vùng đề tài phải HOÃN tới khi bật được tiền

Nhóm 2 nêu đích danh *"putting minors in distressing situations"*.

Ngách này chạm vùng đó liên tục và **cầu rất cao**: sinh đôi · trẻ sơ sinh chết · trẻ mồ côi · tỉ lệ tử vong trẻ em. Đề tài **sinh đôi** đã qua cửa 0 ngày 05/08 (đỉnh bầy 59.656, một quả đang leo 11.519/5 ngày) nhưng **bị hoãn vì luật này** — nội dung thật của nó là đứa thứ hai không được nuôi.

Để dành. Làm sau khi đã vào YPP.

---

# BA THỨ CÒN TREO — CẦN CHỦ QUYẾT

| # | Việc | Treo từ |
|---|---|---|
| 1 | **V15 đang công khai và HỎNG** — cần chủ bấm "Ghép video" trong app GhepVideo Studio (đã nạp đủ: 563 câu, EL JSON, audio 17:11, 563 ảnh, mode EL 100%), lưu vào `Video15_Allergies/build`. Xong tôi kiểm 9 mốc. | 29/07 |
| 2 | ✅ **V17 đã chốt đề tài + packaging** → `V17_PACKAGING_CHOT.md`. Chờ chủ gen thumbnail rồi chấm cửa 1. | 29/07 |
| 3 | `NGHIENCUU_V16_LaneCheck_2026-07-26.md` ghi *"Cần chủ quyết"* — chưa quyết. Nay phần lớn đã được BANG_CAU + CloneSwarm trả lời; đọc lại xem còn gì cần quyết không. | 27/07 |

---

# ⚠️ "LIÊN MINH NỘI DUNG" — TÔI ĐÃ ĐÓNG HỒ SƠ QUÁ SỚM, MỞ LẠI

*29/07, hai lần đổi kết luận trong cùng một ngày. Ghi cả hai để không lặp lại.*

**Lần 1 — tôi bác:** cụm *"X and 2 more"* là chip trích dẫn của NotebookLM; YouTube không có trường nhiều tác giả.
**Lần 2 — tôi tưởng đã giải:** *"The Secret Lives of Ancient Humans"* là tên **khoá học** Stickly tự bán, không phải tên team. → kết luận "không có liên minh".
**Lần 3 — BẰNG CHỨNG NGƯỢC:**

| Kênh | Bằng chứng |
|---|---|
| **@SticklyExplains** *(Predators 2,05M)* | bình luận ghim: *"I just launched a full course"* → `ancient-minds-academy1.teachable.com/p/the-secret-lives-of-ancient-humans` |
| **Mogo** *(Endless Rain 157.887 view, kênh riêng, channelId `UCjjuZ24mtxPHi9aQAuHfL8Q`)* | mô tả video mở đầu: *"🔥 Go deeper with the full course:"* → **ĐÚNG CÙNG MỘT LINK** |

**Hai kênh khác nhau bán chung một khoá học.** Đó là liên hệ kinh doanh có thật.

## Chốt lại cho đúng

- ✅ **Đúng:** một video YouTube có đúng MỘT kênh. Cụm *"Mogo and 3 more"* trong kết quả tìm kiếm là **artefact gom nhóm**, không phải byline nhiều tác giả.
- ❌ **Sai:** dùng điều trên để bác luôn giả thuyết liên minh. Hai chuyện khác nhau — **cách hiển thị** và **quan hệ giữa các kênh**.
- 🔍 **Chưa biết:** Mogo và Stickly là cùng một chủ, hay đối tác bán chéo, hay Mogo chỉ là học viên đi tiếp thị liên kết. Chưa đủ dữ liệu.

## Điều này đổi gì trong việc mình làm

- Số đối thủ **thật sự** có thể ít hơn số kênh nhìn thấy — vài kênh có thể là một tổ chức. Giải thích được vì sao nét vẽ và format giống nhau đến vậy.
- Họ **kiếm tiền bằng khoá học**, không chỉ AdSense. Mô hình khác, chưa tới lượt mình.
- **Không đổi ưu tiên hiện tại.** Vẫn là thumbnail.

## Bài học về cách tôi làm việc

Tôi đóng hồ sơ khi mới có **một** mẩu bằng chứng khớp, và dùng từ *"gần như chắc chắn"*. Từ nay: một mẩu bằng chứng giải thích được hiện tượng **không** có nghĩa là nó giải thích được toàn bộ. Để hồ sơ ở trạng thái "chưa đủ dữ liệu" thay vì đóng.

# NHẬT KÝ SOI KHO

**29/07/2026 — đợt 1.** Soi 11 file nghi ngờ bằng mắt → dán biển chết 8 file.
**29/07/2026 — đợt 2.** Quét hệ thống toàn bộ `~/.claude/skills/` + `memory/` + kho dự án, tìm mọi chỗ còn *gọi tên* 8 file chết. Bắt được 15 chỗ mà soi bằng mắt bỏ sót:

| Chỗ hở | Mức nguy hiểm |
|---|---|
| `skills/chia-shot-va-prompt-anh` PHẦN 9 | 🔴 dạy AI làm thumbnail theo ADN đã bị bác |
| `skills/viet-kich-ban.../quy-trinh-nghien-cuu-cum.md` | 🔴 bắt AI chấm title bằng rubric của lane đã chết |
| 3 file memory *(subngach_cothe_doda · thumbnail_coldchannel_scene · project_faceless_yt)* | 🔴 nạp vào đầu AI mỗi phiên |
| 5 dòng index trong `MEMORY.md` | 🔴 như trên |
| `PLAYBOOK_NotebookLM_DoiThu` · `automation-pipeline/README` · `NGHIENCUU_V16_LaneCheck` | 🟡 |
| 7 file `Video*/Thumbnail_Prompt.txt` | 🟡 prompt của 11 quả flop, dễ bị copy làm mẫu |
| `Video16_Winter/Metadata` · `Video14_Milk/THUMBNAIL` | 🟡 |

Tất cả đã gắn cảnh báo. Quét lại: **sạch**.

## ⚠️ RANH GIỚI CỦA ĐỢT SOI NÀY — ĐỌC KỸ

Cái đã làm: tìm mọi chỗ trỏ vào **8 file đã biết là chết**.
Cái **CHƯA** làm: đối chiếu chéo các file **đang còn sống** với nhau. Kho có **53 file .md**; tôi mới đọc kỹ khoảng 15. Hai file cùng sống vẫn có thể mâu thuẫn nhau mà chưa ai phát hiện.

**29/07/2026 — đợt 3.** Dồn 19 file chết vào `_KHO_LUU_DaChet/` (không xoá — `/Users/admin` là git repo nhưng **0 commit, 0 file theo dõi**, xoá là mất hẳn). Soi xong `RUBRIC_KichBan.md` — tìm được **4 lỗi**, đã vá tại chỗ:
- B5 thưởng điểm cho lane "về BẠN" đã chết → tách, chỉ giữ cú xoay cuối
- ngưỡng tự mâu thuẫn trong cùng file (≥52 vs ≥40) → thống nhất thang 72
- mục 8 và 26 ép cú lật phải ở cuối → bỏ ép vị trí
- mục 12 cấm tuyệt đối "I" → sửa thành "gần bằng 0"
- **bổ sung A7** — 6 đặc điểm winner rubric cũ thiếu, gồm **dấu "!" = 0 (14/14)**

**Còn nợ:** 8 file chưa mở lần nào — `MoXe_15Khoi_KichBan_DoiThu` · `MoXe_KichBan_Viral_3Video` · `BangDoiChieu_v2_vs_Viral` · `TearDown_7M_CongThuc_GuongSoi` · `NGHIENCUU_DoiSong_CoDai` · `NGHIENCUU_2Kenh_ThinkMan` · `GAP_AUDIT_va_Roadmap` · `TRAIN_ChatGPT_*`. Tất cả đều thuộc khâu kịch bản — không phải chỗ hỏng, để sau.

---

# LUẬT CHỐNG LẶP LẠI MỚ HỖN ĐỘN NÀY

1. **Không tạo file "v-mới" khi có thể sửa file cũ.** Ba đời file thumbnail sinh ra vì mỗi lần phát hiện mới lại đẻ một file.
2. **Bác luật nào thì dán biển ngay lên file chứa luật đó** — không chỉ ghi trong file mới. File mới không tự bò sang file cũ.
3. **Sửa file này** mỗi khi có file luật mới hoặc file chết mới.
4. **Kết luận phải kèm cỡ mẫu và ngày.** "Đo 3 video" và "đo 80 video" là hai mức tin khác nhau.
5. **Skill và memory cũng trỏ vào file** — khi giết một file, phải soát cả `~/.claude/skills/` và `memory/MEMORY.md`.

---

# 🔵 LUẬT CHỌN ĐỀ TÀI — ĐỔI HẲN 06/08/2026

## Bỏ: "săn đề tài chưa ai làm"

Lối cũ là dò **"khe còn mở"**. Ngày 05/08 thử 4 đề tài theo lối đó, **chết cả 4**. Và bản
thân file này đã ghi: suy luận "khe còn mở" trong `BANG_CAU` là **suy luận sai**.
Mô hình đó còn **cạn kiệt** — số đề tài trinh nguyên hữu hạn, số đề tài đã chứng minh có
cầu thì gần như vô hạn.

## Thay bằng: LẤY ĐỀ TÀI ĐÃ CHỨNG MINH CÓ CẦU, RỒI LÀM HƠN

**Bằng chứng 1 — Ink Explainer** *(lập 05/2026, 12 video, 45,6K sub, 4,4 triệu view/3 tháng)*:
**7/12 đề tài đã có người làm trước** — rượu, cần, quần áo, mùa đông, bệnh tật, động vật, mưa.
Không có cái nào là phát kiến. Quả **1 triệu** của nó nằm ở **mạch mưa/ướt** — mạch mà
`BANDO_CumChuDe` xếp **CHÓT BẢNG** *(14 video, trung vị 2.650)*.
→ **Trung vị thấp = mạch đầy xác clone làm ẩu, KHÔNG phải mạch chết.** Trung vị đo lũ xác, không đo trần.

**Bằng chứng 2 — kinh nghiệm thật của chủ (kênh Shorts nấu ăn):** lấy đúng video đối thủ
**5–6 triệu view**, làm lại hay hơn → **25 triệu view**.

**Bằng chứng 3 — bầy clone "bathroom"** *(tra live 06/08)*: ~20 video / 2 tháng.
Đỉnh **87K** và **40K**; phần còn lại 1–1.664 view. Cùng đề tài, khác nhau ở **cách làm**.

## ⛔ RANH GIỚI — chỗ đã làm chết một kênh của chủ

Kênh Shorts 25 triệu view **bị đánh sập vì chính sách nội dung dùng lại**. Nó chết **KHÔNG
phải vì trùng đề tài** — mà vì trùng ở tầng thấp hơn.

| ✅ Được phép trùng | ⛔ Chết nếu trùng |
|---|---|
| Đề tài · câu hỏi · khuôn title | **Trình tự các beat** của kịch bản |
| Sự kiện khoa học công cộng | Ví dụ nào đặt ở đâu, theo thứ tự nào |
| Mỏ neo: di chỉ · niên đại · tên nhà nghiên cứu | Câu đùa · ẩn dụ · cách ví von |
| Định dạng · độ dài · nhịp cắt | Hình ảnh · footage · cảnh dựng |
| — | **CÚ BẺ LÁI** *(luận đề chính của video)* |

> 🔑 **SỬA 06/08 — mỏ neo được lấy lại thoải mái.** Ink Explainer lấy **nguyên xi** Dudley ·
> Raqefet · Jiahu của đối thủ và ăn **769K**. Mỏ neo là **DỮ KIỆN** — một hang động, một niên
> đại, một tên nhà nghiên cứu — **không ai sở hữu sự thật**. Cái không được lấy là **CÁCH ĐỌC**
> dữ kiện đó. Đừng tự trói tay như V19 *(tự tra lại cả 4 mỏ neo từ đầu, khắt khe hơn cả kênh
> đang thắng)*. Xem `CONGTHUC_InkExplainer_BestOf.md`.


**Phép thử một câu:** *người vừa xem video đối thủ, xem tiếp video mình — có thấy "đã xem rồi" không?*
Có → quá gần, dù chữ đã đổi hết.

**Phép thử thứ hai** *(từ chính sách YouTube, ghi 05/08)*: gỡ logo, dán cạnh 20 video cùng
title — **có ai chỉ ra được cái nào là của mình không?**

## Quy trình chọn đề tài mới

1. Tìm đề tài **đã có ≥1 quả ≥100K** trong ngách *(có cầu đã chứng minh)*
2. Kéo bản ghi quả to nhất → xác định **cú bẻ lái của nó**
3. **Chọn cú bẻ lái KHÁC** trên cùng đề tài — góc họ chưa chạm
4. Mỏ neo, ví dụ, ẩn dụ, câu đùa: **tự đúc 100%**
5. Chạy hai phép thử ở trên trước khi bấm đăng

*Ví dụ đang chạy — V19:* đề tài "đi vệ sinh thời cổ đại" có bầy 20 clone, đỉnh 87K → **có cầu**.
Cú bẻ lái của họ: *"họ xoay xở thế nào"* (hố, vệ sinh, hậu cần).
Cú bẻ lái của mình: *"vì sao cơ thể bạn chống lại việc đó, và vì sao cái lạnh phá vỡ nó"*
— **vasopressin + lợi-niệu-do-lạnh, không có trong 49 kịch bản đối thủ**.

### 📐 Công thức thực thi — `CONGTHUC_InkExplainer_BestOf.md` *(bóc bản ghi thật 06/08)*

Quả **rượu 769K** của Ink Explainer đối chiếu với vault 49 kịch bản: **giữ 4/7 mỏ neo nguyên
xi** *(Dudley · Raqefet · Jiahu · "bia trước bánh mì")*, **bỏ 3** *(ADH4 · Hammurabi · Ninkasi)*,
**thêm 3 khối mới** *(Göbekli Tepe · McGovern · lương bia Ai Cập)*, và **nén 18–23 phút xuống 6:04**.

**Công thức:** giữ luận đề đã thắng → giữ 3–4 mỏ neo mạnh → vứt mỏ neo yếu/lạc đề → thêm 2–3
khối mới chưa ai ghép → nén còn một phần ba.

⚠️ **Bước "giữ luận đề" thì mình KHÔNG được bắt chước** — xem bảng ranh giới ở trên. Mình lấy
4 bước còn lại, cú bẻ lái phải tự đúc.

**Hai thứ đáng học nhất:** *(1)* dùng **thang thời gian** làm xương sống thay vì chia chương
theo chủ đề — mỗi mốc một chương, lùi dần về hiện tại; *(2)* **công khai việc tổng hợp**
(*"all the research is linked in the description"*) → biến việc xào lại thành uy tín.

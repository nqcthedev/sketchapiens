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

### Năm ý nhỏ — đã đọc, chưa áp, ghi kẻo mất

*Rà lại toàn bộ 1096 dòng ngày 07/08. Năm ý này không lớn bằng bốn việc trên, nhưng đều có thật
và đều rẻ. Không cái nào cần quyết định của chủ để **ghi lại**; áp thì mới cần.*

| # | Ý | Nguồn | Áp vào đâu |
|---|---|---|---|
| **a** | **`decision-log.md` mỗi video** — ghi phương án đã cân nhắc, độ tin cậy, lý do chọn | §4.1 · §8 | Hiện lý do chọn nằm rải trong `CHOT_V19.md` và trong hội thoại. V19 đổi title **ba lần**, mỗi lần lý do ghi một chỗ khác nhau |
| **b** | **Đối chiếu trạng thái ghi với thực tế trên đĩa** | §4.2 | `video.yaml` nói `runs.produced_count: 191` mà thư mục chỉ có 187 ảnh thì phải báo. `project_doctor.py` làm được, chưa làm |
| **c** | **Chạy pipeline TỪNG PHẦN** — chạy từ hoặc tới một chặng, không dựng lại tất cả | §4.3 | Gen thiếu 4 ảnh mà phải chạy lại cả 191 là chỗ đã đau thật *(V17: 263 prompt ra 190 ảnh)* |
| **d** | **Một version có nhiều "biểu hiện"** — cùng một `vNNN` sinh ra: lời đọc EN · bảng duyệt EN+VI · file nạp TTS · phụ đề · bản chép đã đăng | §4.4 *(AYON: Product→Version→Representation)* | Đúng thứ V19 đang có: `Script_Video19_narration.txt` · `DUYET_V19_EN_VI.md` · `SHOTLINES_FULL.txt` · `TTS_input_per_shot.txt` — **bốn biểu hiện của cùng một bản**, mà không file nào nói ra điều đó. Lệch nhau là không ai biết |
| **e** | **Cửa "sẵn sàng" trước khi tiêu tiền** — `shot chuẩn bị xong → shot sẵn sàng → cho phép gen → chạy` | §4.8 *(Jellyfish)* · §16 | *"Đừng gen ảnh chỉ vì đã có bản nháp."* Gen 191 ảnh từ một version chưa duyệt là đốt tiền |

**Ý (d) đáng chú ý nhất cho V19 ngay bây giờ:** bốn file kia phải luôn khớp nhau. Hiện chỉ có
`build_prompts.py` kiểm ghép-shot-khớp-narration; **không có gì kiểm `DUYET_V19_EN_VI.md` còn khớp
kịch bản sau vòng 5 và vòng 6 hay không.** Bảng duyệt EN+VI đang là bản **trước vòng 5**.

---

## 07/08 — BẢY CHỖ LANDSCAPE RESEARCH BỎ SÓT, kèm cơ chế đề xuất

*Đọc ngược tài liệu 1.096 dòng: không tìm "cái gì đáng lấy" mà tìm "nó bỏ sót cái gì".
Tài liệu đó viết bởi người không sống qua các lỗi của dự án này, nên nó mạnh về pattern chung
và yếu ở chỗ đặc thù. Bảy mục dưới là phần đặc thù.*

### G1 · Không đụng tới nút thắt thật của kênh — **KHÔNG CHỮA ĐƯỢC BẰNG KIẾN TRÚC**

Tài liệu tối ưu **chất lượng sản xuất**. Audit chẩn **bệnh A: 367 hiển thị / 5 ngày** — YouTube
chưa phân phối. Làm hết 24 mục trong tài liệu, kênh vẫn 367 hiển thị.

**Không đề xuất cơ chế** — chỉ ghi lại để mọi tài liệu kiến trúc sau này mở đầu bằng câu này:
> Kiến trúc bảo vệ thứ đã có và giúp học nhanh hơn. Nó **không** tạo ra hiển thị.

### G2 · Corpus bị coi chỉ là rủi ro, bỏ mất vai trò tài sản đo lường

Tài liệu §14 chỉ nói cách ly. Nhưng 06-07/08 corpus **giết bốn con số sai trong một ngày** và là
thứ duy nhất làm cổng 11 chạy được.

**Đề xuất — `2_KHO_BANGHI/_tool/do.py`, một lệnh trả mọi số hay hỏi:**
```
python3 do.py wpm            # tốc độ đọc mọi kênh
python3 do.py dodai          # độ dài · số từ · trung vị view
python3 do.py tim <cụm từ>   # mỏ neo này đã ai dùng chưa  (đang phải viết tay mỗi lần)
python3 do.py trung <file>   # cổng A: chuỗi 8 từ trùng bất kỳ bản ghi nào
```
Hiện mỗi lần cần số lại viết script từ đầu → dễ sai và không lặp lại được.
⚠️ Chỉ chạy ở phiên ĐO, không phải phiên VIẾT.

### G3 · Có xuất xứ cho LUẬT, không có xuất xứ cho CON SỐ ⭐ nghiêm trọng nhất

Kiểu lỗi tốn kém nhất của dự án **không phải luật sai, mà là con số nền của luật sai**:
Tầng A rubric đúc từ Mack, mà **4 tháng không ai truy được Mack là kênh nào**.

`RULE_REGISTRY.yaml` hiện có `source` · `confidence` · `evidence` — **thiếu bốn trường quyết định**:

```yaml
- id: R-XXX
  measured_on: "InkExplainer, Zenn, Mack"   # ĐO TRÊN AI — Mack 4 tháng không truy được
  sample_size: 12                            # n bao nhiêu
  measured_at: "2026-08-06"                  # đo ngày nào
  remeasure_after: "2027-02-06"              # hết hạn khi nào
```
Không có bốn trường đó thì `confidence: high` chỉ là chữ.

### G4 · Luật khai tử được, con số thì không

Khi *"chữ 13-19%"* bị bác, luật chết. Nhưng **mọi con số khác đo cùng đợt, cùng phương pháp vẫn sống**.

**Đề xuất — trường `measurement_batch` + luật liên đới:**
> Một con số trong đợt đo bị bác → **mọi con số cùng `measurement_batch` chuyển sang `SUSPECT`**,
> phải đo lại mới dùng tiếp.

Đợt 29/07 sinh ra ít nhất ba con số thumbnail, **một cái đã sai**. Hai cái còn lại chưa ai soi.

### G5 · Analytics giả định dữ liệu sẽ có

§18 liệt kê 10 trường phải lưu, **không nói lấy ở đâu**. Nút thắt thật: YouTube API không trả
hiển thị và CTR, Claude bị cấm vào tài khoản kênh → **mọi số phải chủ gõ tay**.

**Đề xuất — một CSV, không phải schema JSON:**
`analytics/channel/videos.csv` — gõ tay 60 giây từ một ảnh chụp Studio, đọc bằng thư viện chuẩn,
diff sạch trong git. Nâng lên schema **sau khi** có ≥5 dòng thật.

### G6 · Ba giám khảo đều là LLM — bỏ mất lớp rẻ nhất và chắc nhất

~~`qa_kichban.py` kiểm 4 ràng buộc cứng trong 0,2 giây, không tốn token, **không bao giờ sai**.~~

> ⛔ **SỬA 09/08/2026 — câu trên sai ba lần.**
> **(1)** Chỉ có **BA** ràng buộc cứng, không phải bốn — `I ≈ 0` đã gỡ 07/08.
> **(2)** Script khi đó in `'I' (≈0)` dưới nhãn **CỨNG**, và `/apply-review` lấy đó làm điều
> kiện chặn → **editor sẽ cắt mọi câu có "I"**. Nó không "không bao giờ sai" — nó đang thi
> hành một luật đã chết.
> **(3)** Nó **chưa bao giờ kiểm ràng buộc cứng thứ ba** *(mỗi câu một dòng)*. Thêm phép kiểm
> đó vào và chạy thử V19: bắt ngay **22 dòng vi phạm**.
>
> Bài học: **một cỗ máy chạy nhanh và không tốn token vẫn có thể đang thi hành luật sai.**
> Tốc độ không phải độ đúng.

**Đề xuất — thứ tự cứng trong `/audit-script`:**
> **Lớp 1 tất định** *(qa_kichban · ghép-shot-khớp-narration · đếm asset · cổng A)* — chạy TRƯỚC.
> Lớp 1 trượt thì **dừng, không gọi agent** — đừng đốt token để agent nói lại thứ script đã biết.
> **Lớp 2 agent** chỉ chạy khi lớp 1 sạch.

### G7 · Không một chữ về ranh giới ngôn ngữ

Kịch bản **EN**, tài liệu **VI**, chủ duyệt qua **bảng dịch**. Bảng dịch lệch = chủ duyệt nhầm bản.
**Vừa xảy ra thật: 22 dòng.**

Tài liệu viết cho dự án nói tiếng Anh nên không thấy chỗ này.

**Đề xuất — `tools/kiem_bieu_hien.py`:** một version kịch bản sinh ra nhiều biểu hiện
*(narration · bảng duyệt EN+VI · SHOTLINES · TTS_input)*. Script kiểm cả bốn còn khớp nhau.
Đây là ý (d) §4.4 biến từ **khái niệm** thành **phép kiểm** — và nó đã bắt được lỗi thật ngay lần đầu.

---

## 07/08 — ĐÃ LÀM G7: `tools/kiem_bieu_hien.py`

Kiểm bốn biểu hiện của cùng một bản kịch bản có còn khớp nhau không:
`narration` *(bản gốc)* ↔ `DUYET_*_EN_VI.md` ↔ `SHOTLINES_FULL.txt` ↔ `build/TTS_input_per_shot.txt`
↔ số prompt ảnh. READ-ONLY, chạy được cho một video hoặc toàn bộ.

### Kết quả chạy lần đầu trên 18 video — **3 lệch THẬT**

| Video | Kịch bản đã duyệt | Thứ TTS thật sự đọc |
|---|---|---|
| V02 | `looked closely at the marks` | `looked closely, at the marks` — thừa dấu phẩy |
| V11 | `every one of them traces back` | `every one traces back` — **rơi hai chữ** |
| **V04** | `Stick around for the last job especially.` | `So let's actually walk through the job.` — **câu KHÁC HẲN** |

V04 không phải lệch chính tả mà là **hai bản kịch bản khác nhau**. Câu giữ chân cuối chương
*không có* trong thứ đã đưa vào sản xuất. Ba video đều đã sản xuất xong — không sửa được nữa.

### ⚠️ Bài học về chính bộ kiểm — 86% báo động giả ở lần chạy đầu

Chạy lần đầu ra **22 FAIL**. Sau khi sửa lỗi của **chính bộ kiểm** thì còn **3**.

| Số | Nguyên nhân |
|---|---|
| 13 | Video cũ đánh số prompt `001.` trên dòng riêng; V19 đánh `001. <prompt>` cùng dòng — regex chỉ nhận kiểu sau |
| 3 | Bảng duyệt V17 có tiêu đề `🎙️ EN`; bộ lọc chỉ loại chữ `EN` trần |
| 3 | SHOTLINES V06–V08 đánh số ở đầu dòng |

**Nếu báo thẳng "22 lỗi" thì đó là báo động giả 86%, và lần sau không ai tin bộ kiểm nữa.**
→ Luật: **bộ kiểm mới ra kết quả xấu thì nghi bộ kiểm trước, nghi dữ liệu sau.** Chỉ báo cáo
sau khi đã loại hết sai khác về ĐỊNH DẠNG.

### Phát hiện phụ: định dạng không thống nhất giữa các video
`001.` dòng riêng ↔ `001. <prompt>` cùng dòng · SHOTLINES có/không đánh số · bảng duyệt
`DUYET_*_EN_VI.md` ↔ `Script_*_DUYET_EN-VI.md` ↔ **12/18 video không có bảng duyệt nào**.
Chưa sửa — thuộc migration, cần D-01…D-04.

---

## NHẬT KÝ SOI KHO *(chuyển từ `00_LUAT_HIEN_HANH.md` ngày 07/08/2026 — nhật ký thuộc về sổ, không thuộc cửa vào)*

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

**29/07/2026 — đợt 3.** Dồn 19 file chết vào `_KHO_LUU_DaChet/` (không xoá — `/Users/admin` là git repo nhưng **0 commit, 0 file theo dõi**, xoá là mất hẳn). Soi xong `kho/1_luat/RUBRIC_KichBan.md` — tìm được **4 lỗi**, đã vá tại chỗ:
- B5 thưởng điểm cho lane "về BẠN" đã chết → tách, chỉ giữ cú xoay cuối
- ngưỡng tự mâu thuẫn trong cùng file (≥52 vs ≥40) → thống nhất thang 72
- mục 8 và 26 ép cú lật phải ở cuối → bỏ ép vị trí
- mục 12 cấm tuyệt đối "I" → sửa thành "gần bằng 0"
- **bổ sung A7** — 6 đặc điểm winner rubric cũ thiếu, gồm **dấu "!" = 0 (14/14)**

**Còn nợ:** 8 file chưa mở lần nào — `MoXe_15Khoi_KichBan_DoiThu` · `MoXe_KichBan_Viral_3Video` · `BangDoiChieu_v2_vs_Viral` · `TearDown_7M_CongThuc_GuongSoi` · `NGHIENCUU_DoiSong_CoDai` · `NGHIENCUU_2Kenh_ThinkMan` · `GAP_AUDIT_va_Roadmap` · `TRAIN_ChatGPT_*`. Tất cả đều thuộc khâu kịch bản — không phải chỗ hỏng, để sau.

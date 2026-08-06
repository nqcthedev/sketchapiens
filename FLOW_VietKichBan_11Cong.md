# FLOW VIẾT KỊCH BẢN — 11 CỔNG
*Dựng 06/08/2026. Gộp toàn bộ kho NotebookLM + chính sách YouTube + mọi lỗi đã mắc thật.*

> **Nguyên tắc:** mỗi cổng chặn **một lỗi đã xảy ra thật**. Không cổng nào bỏ được.
> Cổng nào **không chạy được bằng lệnh** thì phải ghi rõ ai chạy và chạy thế nào.

---

## BẢNG MỘT TRANG — dán lên đầu mỗi video

```
☐ 0  Chọn đề tài đã có cầu (≥1 quả ≥100K)          → 00_LUAT_HIEN_HANH mục 🔵
☐ 1  Kéo bản ghi quả to nhất CÙNG ĐỀ TÀI            → biết cú bẻ lái của họ
☐ 2  Chốt cú bẻ lái KHÁC + 2 khối chưa ai ghép      → CHOT_Vxx.md
☐ 3  Tra xác minh TỪNG mỏ neo bằng web             → MONEO_Vxx.md
☐ 4  CỔNG A — grep chống giẫm (kể cả _nhap/)       → lệnh bên dưới
☐ 5  Viết ĐOẠN KẾT TRƯỚC (bookend)                 → _nhap/KET_Vxx.md
☐ 6  Viết theo ĐỢT + QA 5 mục từng chương          → _nhap/Script_Vxx_DOTn.md
☐ 7  Chấm rubric BẰNG MÁY                          → script đo bên dưới
☐ 8  QA CHÍNH SÁCH — 3 nhóm vi phạm                → bảng bên dưới
☐ 9  Chống văn AI + ĐỌC TO từng câu                → skill chong-van-ai-narration-en
☐ 10 NGƯỜI NGHE NGOÀI — bắt buộc nếu đổi cấu trúc  → LENH_GPT_ReviewKichBan_v3.md
☐ 11 Hai phép thử cuối trước khi chốt              → bên dưới
```

---

# CHI TIẾT TỪNG CỔNG

## Cổng 0 — Chọn đề tài đã có cầu
**Làm:** tìm đề tài có **≥1 quả ≥100K**. Đừng tìm đất trắng.
**Chặn lỗi:** 05/08 dò "khe còn mở", thử 4 đề tài, **chết cả 4**.
**Luật:** `00_LUAT_HIEN_HANH.md` mục 🔵.

## Cổng 1 — Kéo bản ghi quả to nhất cùng đề tài
```
mcp__nexlev__youtube_search  → tìm mọi video cùng đề tài, xem đỉnh bầy
mcp__nexlev__get_video_transcript → kéo quả to nhất
```
**Phải ghi ra:** cú bẻ lái của họ · mỏ neo họ dùng · thứ tự beat.
**Chặn lỗi:** 06/08 suýt chốt V19 với luận đề *"việc nguy hiểm nhất là đi vệ sinh"* — trùng
nguyên văn mô tả của Basically Primitive (40K), đăng trước 2 tháng.

## Cổng 2 — Chốt cú bẻ lái KHÁC + hai khối chưa ai ghép
**Bắt buộc hai thứ:**
1. **Cú bẻ lái khác họ** — cùng đề tài, khác luận đề
2. **≥2 khối mới chưa ai ghép vào đề tài này**

**Vì sao vế 2 bắt buộc:** 20 quả clone "bathroom" đều tổng hợp, **18 quả dưới 1.700 view**.
Ink Explainer ăn 769K vì **thêm** Göbekli Tepe · McGovern · lương bia Ai Cập.
Tổng hợp không thêm gì = một con trong bầy. Xem `CONGTHUC_InkExplainer_BestOf.md`.

## Cổng 3 — Tra xác minh từng mỏ neo
**Ra file `MONEO_Vxx.md`.** Chưa có dòng trong file đó thì **không được viết vào kịch bản**.
**Ba luật con:**
- Mở **bài gốc** đọc, **cấm tin snippet** của công cụ tìm kiếm
- Ghi đủ **tên tác giả · năm · tạp chí · địa danh**
- Số nào paywall không đọc được thì **không đọc con số đó lên**

**Chặn lỗi 06/08 — bốn con số sai vì tin snippet:** Ekirch "500 dẫn chứng" *(thật: ~2.000)* ·
quãng thức "1–2 tiếng" *(Ekirch không nêu, đó là số của Wehr)* · Wehr "ngủ 4 tiếng"
*(gốc chỉ nói "several hours")* · Ethiopia "một nửa số người chết" *(gốc: một nửa số **vụ tấn công**)*.

## Cổng 4 — CỔNG A, grep chống giẫm
```bash
cd "…/Build Channel Người Que Cổ Đại"
grep -rniE "từ_khoá_1|từ_khoá_2|tên_tác_giả|con_số_đặc_trưng" \
  Video1[0-9]*/ --include="*.txt" --include="*.md"
```
⚠️ **PHẢI có `-r` và quét cả `_nhap/`** — bản nháp chứa câu đã bị cắt khỏi bản cuối mà mình
vẫn có thể vô tình viết lại.

**Chặn hai lỗi thật:**
- Xương V19 dựng cả một khối quanh **Hadza 18 phút** — V18 đã xài trọn, kể cả cú lật cuối
- Đoạn KẾT V19 trùng **hai chỗ** với V17: *"reason you are here to be bored"* nằm trong
  `_nhap/Script_V17_FULL_v2.md`, và thủ pháp **đếm bước chân trong nhà**

**Quét thêm:** bản dịch đối thủ trong dự án *(`DICH_Zenn_7.8M...`)* — nhờ nó mới phát hiện
quả **7,8 triệu** sở hữu Ekirch + Wehr, và cắt kịp một chương.

## Cổng 5 — Viết ĐOẠN KẾT TRƯỚC
**Luật `NganHang_ReHook`:** *"BOOKEND — viết câu CUỐI trước."*
Viết kết trước để mọi chương có đích mà hạ cánh vào.
**Theo `HE_THONG` PHẦN G — ba nhịp:** hành động vật lý người xem sắp làm → nối vào chuỗi tổ
tiên → đóng bằng nốt mất mát hoặc kỳ diệu. **Câu cuối phải chứa một VẬT THỂ CỤ THỂ.**

## Cổng 6 — Viết theo đợt + QA 5 mục từng chương
**Đợt:** HOOK+setup → dừng duyệt → 1-2 chương → dừng duyệt → khúc thành thật + KẾT.
Mỗi đợt lưu riêng `_nhap/Script_Vxx_DOTn.md` *(V17 làm đúng thế, 5 đợt)*.

**QA ngay sau MỖI chương, trước khi viết chương kế:**
```
1. MỎ NEO  — mọi dữ kiện đã có trong MONEO chưa?
2. LOGIC   — kết luận có THẬT SỰ suy ra từ bằng chứng của chính chương này?
             bẫy đã dính: giữa-cá-thể ≠ trong-một-cá-thể · tương quan ≠ nhân quả
             · gán NHÂN QUẢ TIẾN HOÁ mà nguồn không nói
3. GIỌNG AI — 0 dấu "!" · 0 gạch ngang giữa câu · không "furthermore/it is important to note"
4. LUẬT CỨNG — "you"=người xem · "we"=loài người · "I"≈0 · hedge 1-3 CẢ BÀI
5. VÒNG TÒ MÒ — mở vòng mới TRƯỚC khi đóng vòng cũ · đóng chương bằng blind promise
```
**Chặn lỗi:** V18 viết trọn một chương rồi phải **cắt bỏ hoàn toàn** vì cầu lập luận sai.

## Cổng 7 — Chấm rubric BẰNG MÁY
```bash
python3 - << 'PY'
import re
t=open("Script_Vxx_narration.txt").read()
w=re.findall(r"[A-Za-z']+",t)
S=[s for s in re.split(r'(?<=[.?])\s+',t.replace("\n"," ")) if s.strip()]
n=[len(re.findall(r"[A-Za-z']+",s)) for s in S]
print("từ",len(w),"| phút",round(len(w)/178,1))
print("dấu ! :",t.count("!"),"(phải 0) | gạch ngang:",t.count("—"),"| I:",len(re.findall(r"\bI\b",t)))
print("câu hỏi:",t.count("?"),"→ 1 câu mỗi",round(len(w)/178*60/max(t.count("?"),1)),"giây (chuẩn 60-90)")
print("câu <6 từ:",sum(1 for k in n if k<6),f"({round(sum(1 for k in n if k<6)/len(n)*100)}%) | V17 = 37%")
print("dài câu TB:",round(sum(n)/len(n),1),"| V17 = 8.9")
PY
```
> ## 🔴 LUẬT 0 KHI ĐỌC KẾT QUẢ
> **Mọi con số benchmark là KẾT QUẢ quan sát, KHÔNG phải chỉ tiêu phải đạt.**
> Lệch thì hỏi *"bài này có tầng đó không?"* — có mà thiếu thì bổ sung; **không có thì để yên**.
> Rắc chữ vào cho đủ chỉ tiêu = đúng lỗi *"ba câu mùi AI nặng nhất của V17 đều là câu thêm vào để thoả Tầng A."*
>
> **Đã dính 06/08:** đuổi theo 4 con số, **2 sai** — "giác quan 7–9%" *(đo cùng từ điển thì
> V17 chỉ 5,2%)* và "mỏ neo 3,2–5,1/phút" *(V19 đo ra 12,2 — thước khác nhau)*.
> Còn `you:we 1,5–2` **không phải hằng số**: 4 winner ra 2,7 · 1,5 · 1,5 · 1,6, chênh theo nội dung.

## Cổng 8 — QA CHÍNH SÁCH NỘI DUNG KHÔNG TRUNG THỰC

| Nhóm | Hỏi gì | Chữa thế nào |
|---|---|---|
| **1. Khuôn mẫu / lặp hàng loạt** | Video này có phải cùng bộ xương với video trước, chỉ đổi danh từ? Có trùng beat với quả to cùng đề tài? | Cổng 1·2·4 đã chặn. Kiểm lại lần cuối |
| **2. Gây khó chịu / trẻ em trong hoàn cảnh đau đớn** | Có cảnh chết chóc, trẻ em, máu me không? | **Bộ giáp `KHO_AnDu` phần 3**: mở bằng **địa danh + niên đại + tên nghiên cứu** · giọng **nhân học khách quan** · thuật ngữ lâm sàng · **không tả thực** · số liệu đọc như dòng thống kê, không như một cảnh |
| **3. Nhân vật AI trong chủ đề YMYL** | Có giả làm chuyên gia y tế/tài chính không? | Kênh không dùng persona → không dính |

**Nhớ:** YPP xét ở **cấp KÊNH theo TỶ LỆ**, không xét từng video. Một video lệch không chết,
nhưng **nửa kênh cùng một khuôn thì chết**.

## Cổng 9 — Chống văn AI + đọc to
Chạy skill `chong-van-ai-narration-en` *(giữ nguyên số dòng, số liệu, cấu trúc)*.
Rồi **đọc to từng câu**. Câu nào *"không narrator thật nào nói thế"* → viết lại.

## Cổng 10 — Review ngoài — **BẮT BUỘC khi bài có thay đổi cấu trúc**

> ## 🔴 RUBRIC KHÔNG BAO GIỜ BẮT ĐƯỢC LỖI CẤU TRÚC. ĐÂY LÀ LỖ HỔNG VĨNH VIỄN.
>
> **Hai lần, cùng một hình dạng — rubric qua, cấu trúc hỏng:**
>
> | | Rubric/máy chấm | Người nghe tìm ra |
> |---|---|---|
> | **V17** *(30/07)* | 68/74, đạt | title hứa *"họ sống sót bằng cách nào"* nhưng **ba chương đầu chỉ trả lời "mưa tệ ra sao"** |
> | **V19** *(06/08)* | sạch cả 7 mục cứng | **đáp án cho ở giây 9 rồi giấu tới 91%** — cả kiến trúc xây trên một bí ẩn không tồn tại |
>
> **Vì sao mù vĩnh viễn:** câu hỏi *"bí ẩn này có thật không?"* thì **người viết không tự trả
> lời được** — vì họ biết đáp án, nên với họ mọi khoảng trống đều đầy. Thêm mục 37 vào rubric
> cũng vô ích, vì mục đó vẫn do chính người viết chấm.
>
> **Hai bên bắt hai loại lỗi khác hẳn nhau.** Ngày 06/08: máy bắt 4 lỗi *(chuỗi câu dài · câu
> chẻ đôi hai dòng · intensifier rỗng · câu hỏi thưa)*, người nghe bắt 8 lỗi *(bí ẩn giả · mốc
> lộ khung · 11 đại từ mơ hồ · đảo logic sai · nói quá…)*. **Không cái nào thay được cái nào.**

**Khi nào BẮT BUỘC chạy** *(không còn là "chỉ video cờ đầu")*:
- Bài **cắt, gộp hoặc đổi thứ tự chương**
- Bài **đổi cú bẻ lái hoặc đổi hook** sau khi đã viết xong
- Video **đầu tiên** của một sub-mạch mới

**Cách chạy:** `LENH_GPT_ReviewKichBan_v3.md` PHẦN A — **người nghe không biết gì về ngách**.
⛔ **KHÔNG dán luật kênh, không dán rubric.** Nạp luật vào là bịt mắt người review — nó sẽ chấm
theo đúng bảng kiểm mà cổng 7 đã chấm rồi.
⛔ **KHÔNG dùng NotebookLM** — nó trộn bài mình với 49 transcript đối thủ.

**Lựa chọn rẻ hơn:** gọi một **agent** làm người nghe *(không thấy phiên đang chạy)*. Chạy ngay,
không tốn thời gian chủ, nhưng **độc lập yếu hơn** vì cùng dòng Claude. Dùng agent cho vòng
sàng đầu, để dành GPT cho vòng cuối khi bài đã gần chốt.
⚠️ **KHÔNG đưa NotebookLM** — nó trộn bài mình với 49 transcript đối thủ, đã bắt quả tang 2 lần.
Feedback về thì phân loại: **áp ngay · áp có sửa · bỏ + lý do**. Không áp mù.

## Cổng 11 — Hai phép thử cuối
1. **Người vừa xem video đối thủ, xem tiếp video mình — có thấy *"đã xem rồi"* không?**
2. **Gỡ logo, dán cạnh 20 video cùng title — có ai chỉ ra được cái nào của mình không?**

Một trong hai trả lời "có" → **chưa được đăng**.

---

## RANH GIỚI REUSED-CONTENT — dán ở đây cho khỏi phải mở file khác

| ✅ Được trùng | ⛔ Chết nếu trùng |
|---|---|
| Đề tài · câu hỏi · khuôn title | **Trình tự các beat** |
| Sự kiện khoa học công cộng | Thứ tự ví dụ |
| Mỏ neo: di chỉ · niên đại · tên nhà nghiên cứu | Câu đùa · ẩn dụ · cách ví von |
| Định dạng · độ dài · nhịp cắt | Hình ảnh · footage |
| — | **CÚ BẺ LÁI** |

> 🔑 **SỬA 06/08 — mỏ neo được lấy lại thoải mái.** Ink Explainer lấy **nguyên xi** Dudley ·
> Raqefet · Jiahu của đối thủ và ăn **769K**. Mỏ neo là **DỮ KIỆN** — một hang động, một niên
> đại, một tên nhà nghiên cứu — **không ai sở hữu sự thật**. Cái không được lấy là **CÁCH ĐỌC**
> dữ kiện đó. Đừng tự trói tay như V19 *(tự tra lại cả 4 mỏ neo từ đầu, khắt khe hơn cả kênh
> đang thắng)*. Xem `CONGTHUC_InkExplainer_BestOf.md`.


> Kênh Shorts nấu ăn của chủ **25 triệu view** đã bị sập vì chính sách này. Nó chết **không
> phải vì trùng đề tài**, mà vì trùng ở tầng dưới. Với kênh người que thì **ảnh gen 100% của
> mình** nên tầng nguy hiểm nhất *(footage)* tự nhiên biến mất — còn lại là **trình tự beat**
> và **cú bẻ lái**, hai thứ cổng 1·2·4 lo.

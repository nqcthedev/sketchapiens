Đã mở cả 13 file .txt + 13 `info.json` + VTT word-level timing để đối chiếu từng con số.

---

# BÁO CÁO GIÁM KHẢO — kênh PrimalGlitch (The Primal Glitch)

**Nguồn kiểm:** `/Users/admin/Claude/Projects/Build Channel Người Que Cổ Đại/2_KHO_BANGHI/PrimalGlitch/` — 13 file .txt + `_vtt/*.info.json` (có `chapters`, `like_count`, `comment_count`, `description`) + `_vtt/*.en-orig.vtt` (mốc thời gian từng từ).
**Đã kiểm 162 câu trích nguyên văn bằng so khớp chuỗi cứng: 158 khớp, 3 bị sửa chữ, 1 là câu bẫy tôi tự cài (không tính).**

---

## ⚠️ NÓI THẲNG TRƯỚC: n QUÁ NHỎ, VÀ NHỎ HƠN HỌ NGHĨ

Họ khai n=13, mỗi nhóm 4 bài. Nhưng **n hiệu dụng để rút "cách viết" là 1, không phải 4**: cả 4 bài nhóm CAO là chó ×2, sói ×1, mèo ×1 — tức MỘT cụm đề tài, viết trong MỘT đợt 61 ngày, và 2 trong 4 bài **dùng chung một bộ xương chương y hệt**. Mọi khác biệt văn phong CAO/THẤP đều có thể chỉ là "người ta viết về thú cưng thì viết kiểu đó".

Thêm một lỗi phương pháp họ KHÔNG khai: **view/ngày thiên vị bài mới một cách hệ thống.** Bài 30/07 đo ở tuổi 9 ngày; bài 06/05 đo ở tuổi 94 ngày. vpd luôn suy giảm theo tuổi video, nên nhóm CAO được thổi lên và nhóm THẤP bị dìm xuống. Chênh 30–80 lần giữa CAO và THẤP thì vẫn sống sót qua sai lệch này, **nhưng thứ tự GIỮA vs THẤP thì chết**: 20260721 ra 151,9 vpd ở tuổi 18 ngày, 20260506 ra 50,4 vpd ở tuổi 94 ngày — chênh 3× này hoàn toàn có thể là ảo ảnh tuổi tác. **Đừng dùng bất kỳ kết luận nào dựa trên ranh giới GIỮA/THẤP.**

---

## ĐỨNG VỮNG — trích thật, có mẫu số, đếm lại đúng, chỉ thấy ở nhóm view cao

### 1. Bộ xương dùng lại — chắc nhất toàn bài bóc, xác minh 100%
Đây là phát hiện tôi không gạch được một chữ nào.

`20260530` (277.969 view) và `20260617` (120.046 view), cách nhau 18 ngày:

| | 20260530 Dogs | 20260617 Wolves |
|---|---|---|
| 0s | The Planet You Were Not Supposed to Win | **giống hệt** |
| 65s | The Wolf That Made a Decision | **giống hệt** |
| 160s | What **Dogs** Actually Did for Ancient Humans | What **Wolves** Actually Did… |
| 255s | The Mammoth Kill Sites Nobody Talks About | **giống hệt** |
| 320s | The Night: Humanity's Biggest Vulnerability | **giống hệt** |
| 370s | Why Neanderthals Disappeared and We Didn't | **giống hệt** |
| 420s | How **Dogs** Rewired Themselves to Understand Us | How **Wolves** Rewired… |
| 490s | The Burials That Tell You Everything | **giống hệt** |
| 515s | Conclusion | What This Means For You |

9/9 mốc giây TRÙNG KHÍT. Nhưng chữ thì mới hoàn toàn: **0/131 và 0/139 dòng trùng nhau · cụm 6 từ trùng 0,00% · cụm 5 từ trùng 0,06% (đúng 1 cụm) · cụm 4 từ trùng 0,60%.** Tôi tự đo lại bằng n-gram, ra đúng số của họ.

**Dùng được ngay:** tái dùng KHUNG, không tái dùng CHỮ. Đây cũng là đường an toàn với luật reused-content.

### 2. "you" phải nằm trong 10 TỪ ĐẦU — khác biệt sạch nhất của chiều hook
Đo vị trí từ đầu tiên chứa you/your/you're. **Con số của họ đúng tuyệt đối, tôi đếm lại khớp từng bài:**

| nhóm | vị trí "you" đầu tiên |
|---|---|
| CAO (4 bài) | **1 · 1 · 1 · 10** |
| GIỮA (5 bài) | 1 · 1 · 1 · **52 · 77** |
| THẤP (4 bài) | 1 · **35 · 240 · 383** |

Bài CAO duy nhất không mở bằng "You" vẫn chạm "you" ở từ thứ 10, câu thứ hai.

### 3. Dấu "?" đầu tiên — CAO hoặc đặt cực sớm hoặc bỏ hẳn
Vị trí từ của dấu `?` đầu tiên, **đếm lại khớp 13/13 bài**:
- **CAO:** từ 12 · từ 63 · **0 dấu hỏi cả bài** (1582 từ) · **0 dấu hỏi cả bài** (1689 từ)
- **GIỮA:** 204 · 510 · 513 · 1157 · 2257
- **THẤP:** 74 · 227 · 227 · 725

Hai bài CAO cao nhất kênh (4215 và 2309 vpd) **không có một dấu hỏi nào**. Chúng nêu bí ẩn bằng câu khẳng định giấu tên đối tượng.

### 4. "So, what/how/why…?" làm câu nối = dấu hiệu bài chìm
**THẤP 4/4 bài, 6 lần. GIỮA 2/5 bài. CAO 1/4 bài, 1 lần duy nhất — và nó ở từ thứ 63 tức trong hook, không phải câu nối giữa bài.** Đếm lại khớp chính xác.

Rộng hơn: mọi dòng mở bằng "So," — CAO 2 lần (0,30/1000 từ) · THẤP 9 lần (1,38/1000 từ).

### 5. Vị trí cú lật: CAO dồn hết vào nửa đầu
Tôi đo lại vị trí % theo từ của mọi marker `here is/here's/this is + the part/where/what`:

- **CAO:** 24,8% · 25,1% · 30,8% · 37,5% · **39,4%** · 49,0% · 64,1% → **không marker nào vượt 64%**
- **GIỮA:** rải tới 73,7 · 79,8 · 81,1 · 83,7 · 84,2 · **87,8%**
- **THẤP:** 6,8 · 42,2 · 56,8 · **76,4%** (bài guns có đúng 1 cú lật, đến ở 76%)

*(Họ liệt kê CAO là 25/31/25/38/49/64 — khớp, nhưng họ BỎ SÓT marker 39,4% của bài 4215 vpd; xem mục Đã gạch.)*

### 6. But : So — CAO nghịch, THẤP giảng
Đếm câu mở đầu bằng "But" / "So" trên 1000 từ. **Khớp đến 2 chữ số thập phân:**
- But: **CAO 2,25** (15 câu) · GIỮA 1,44 · **THẤP 0,77** (5 câu)
- So: CAO 0,30 (2 câu) · GIỮA 1,03 · THẤP 1,38–1,54

### 7. Kết bài đặt người xem vào cảnh — phát hiện mạnh nhất của chiều 3
Số lần "you/your" trong **180 từ cuối**, tôi đếm lại khớp từng bài:
- **CAO: 6 · 5 · 3 · 2 → 4/4 bài đều có**
- GIỮA: 6 · 6 · 4 · 2 · 0
- **THẤP: 2 · 0 · 0 · 0 → chỉ 1/4**

Ba bài THẤP kết bằng phán quyết lịch sử ngôi ba, không có mặt người xem.

### 8. CAO không nêu tên nhà nghiên cứu, không nêu năm dương lịch
**Số năm dương lịch (1600–2029) trong lời đọc: CAO 0 · 0 · 0 · 0. THẤP 1 · 2 · 2 · 5 (tổng 10).** Đây là split sạch tuyệt đối, tôi đếm lại khớp.

Danh từ thẩm quyền (researcher/scientist/study/journal/university) trên 1000 từ: **CAO 1,65 · GIỮA 1,23 · THẤP 3,07** (họ ghi 1,66 / 1,24 / 3,24 — coi như khớp).

Bài chìm nhất kênh (zebras) nhồi tên riêng dày nhất: Ludovic Orlando, CNRS, Jared Diamond, tạp chí *Animals*, sách *Guns, Germs, and Steel*, vùng Vulgadon — trong 1382 từ.

### 9. Tên chương hướng về người xem
**CAO 9/34 tên chương chứa You/Your (26,5%). THẤP 0/39 (0%).** GIỮA 2/49.
*(Họ ghi CAO 7/34 = 20,6% — đếm thiếu, xem mục Đã gạch. Hướng thì đúng và rất mạnh.)*
Chương áp chót của 4/4 bài CAO đều hướng về hiện tại/người xem, ở 77% · 85% · 93% · 94% độ dài bài.

### 10. Mệnh lệnh: CAO chỉ "Think about", tuyệt đối không "Imagine/Picture"
**"Think about": CAO 4 lần / 3 trên 4 bài · GIỮA 2 · THẤP 1.**
**"Imagine/Picture/Look at" dạng mệnh lệnh: CAO 0 lần / 0 trên 4 bài · GIỮA 9–11 · THẤP 2** (cả 2 ở bài zebras, và bài zebras MỞ BÀI bằng "Picture an animal…").

### 11. Cắt cứng bằng mốc năm — sạch HƠN họ nói
Dòng mở đầu bằng `N years ago/later,`: **5 lần, 100% nằm ở nhóm CAO** (dogs 2, wolves 3), **0 lần ở GIỮA và THẤP.** Họ khai "6 lần / 5 bài rải cả ba nhóm" và xếp nó vào CA_HAI_NHOM — họ tự làm yếu phát hiện của mình bằng cách gộp "London, 1894." (một khuôn khác) vào chung rổ.

### 12. Số liệu nền — kiểm hết, khớp hết
- 3.750 sub ✓ · 13 video long-form (`playlist_count=13`) ✓
- **13/13 view/ngày khớp đến 0,1** (4215,4 · 3971,0 · 2308,6 · 1405,3 · 289,4 · 151,9 · 124,5 · 68,8 · 62,4 · 50,4 · 47,5 · 35,0 · 16,3)
- Tổng view 573.174 ✓ · 3 bài chó = 435.954 = **76,1%** ✓ · +mèo = 523.085 = **91,3%** ✓
- **13/13 tỷ lệ like/view khớp đến 0,01%** · **13/13 số comment khớp tuyệt đối** (746 · 400 · 392 · 67 ở CAO; 38 · 38 · 8 · 1 ở THẤP)
- Chuỗi khoảng cách đăng 16-4-4-8-3-4-3-4-14-16-9-6 ✓ trung vị 5,0 ✓
- Số chương: CAO 8-9-9-8 · THẤP 11-8-11-9 ✓ khớp tuyệt đối
- Mốc chương bài 20260730: 0/55/120/195/270/335/380/420s → thời lượng 55-65-75-75-65-45-40-25 giây ✓ khớp tuyệt đối

---

## NẾT CỦA KÊNH — đúng nhưng cả cao lẫn thấp đều có, ĐỪNG tưởng là bí quyết

| Thứ | Số thật (tôi đếm lại) | Phán |
|---|---|---|
| **0 dấu chấm than** | 0/13 file, cả bài 277K lẫn bài 49 view | nết dây chuyền |
| **0 gạch ngang em-dash trong lời đọc** | 0/13 ✓ — **nhưng description CÓ em-dash** ("And somehow — ancient humans were less lonely") | nết, và chỉ đúng với narration |
| **0 lời xin sub/like/comment trong lời đọc** | grep 13/13 → ZERO MATCHES ✓ | không phải nút thắt; bài 277K vẫn ra 746 comment |
| **0 forward-promise** ("by the end of this video", "stick around"…) | grep 13/13 → ZERO MATCHES ✓ | kênh không nhử để giữ chân, cả bài thắng lẫn bài chìm |
| **0 mồi video kế** | 13/13 câu cuối đều là câu chốt luận đề | nết |
| **"Subscribe to understand the glitch."** | **13/13 description, nguyên văn 100%** | CTA đẩy hết ra description, gắn slogan chứ không gắn nội dung |
| **Re-hook "Here is the part…"** | **12/13 bài** (chỉ bài cancer là 0). Mật độ **CAO 0,90–1,05 · GIỮA 1,34 · THẤP 0,62** trên 1000 từ | GIỮA dùng DÀY NHẤT — copy vì tưởng nó tạo 277K là copy nhầm |
| **"Not X, Y" (phủ định rồi lật)** | **CAO 6 (0,90/1k) · GIỮA 22 (2,26) · THẤP 6 (0,92)** — khớp tuyệt đối số của họ | GIỮA dẫn đầu áp đảo. **Không phải con hào.** Riêng bài 124 vpd dùng 10 lần |
| **Callback hook↔kết** | từ khoá chung giữa 130 từ đầu và 180 từ cuối: CAO 16-10-8-19 · **THẤP 9-10-15-16** | THẤP callback ngang hoặc đậm hơn. Cái phân biệt là callback về CÁI GÌ (cơ thể/nhà bạn vs hiện vật) chứ không phải CÓ callback |
| **Rào đón (hedge)** | bộ chặt: CAO 2,85 · GIỮA 2,67 · THẤP 1,69 /1000 từ | CAO ≈ GIỮA → viết dè dặt hơn KHÔNG làm bài ăn hơn |
| **"before X, before Y"** | 7 lần / 6 bài, cả ba nhóm | nết |
| **"To understand X, you have to…"** | 3 bài: 2 CAO + 1 THẤP | nết, dù là câu cầu đẹp |
| **Title có "Ancient Humans"** | **10/13 · CAO 4/4 VÀ THẤP 4/4** | vô nghĩa để dự báo |
| **Title kết bằng dấu hỏi** | **9/13 · CAO 2/4 · THẤP 3/4** | hơi nghiêng về bài chìm |
| **Khuôn câu mở đầu** | A "You+hiện tại" 7/13 · B khẳng định ngôi ba 4/13 · C cảnh lạnh 1 · D "Picture/Imagine" 1 — khớp tuyệt đối, CAO 3/4 dùng A nhưng GIỮA cũng 3/5 | nết |
| **Chương cuối kiểu "Conclusion"** | 10/13 đúng tên, 3 bài tên khác | nết dây chuyền |
| **"Let's start with / Start with"** | **7 lần / 7 bài: CAO 1 · GIỮA 4 · THẤP 2** | họ gọi là "dấu hiệu bài chìm" — SAI, GIỮA mới dùng nhiều nhất → hạ thành NẾT |

---

## ĐÃ GẠCH — gạch gì, vì sao

**A. GẠCH: 3 câu trích BỊ SỬA CHỮ** (đều ở chương 7 "Mỏ neo khoa học"). Đây là lỗi nặng nhất vì chủ định chép chúng làm mẫu hedge:

| Họ viết | File thật ghi |
|---|---|
| "…elevated stress hormones and weakened **immunity**." | "…elevated stress hormones and weakened **immune response over time**." |
| "…rather than kept at a distance." | "…rather than kept at a distance **the way you might keep a working animal**." |
| "…what researchers describe as a mutually beneficial **arrangement**." | "…what researchers describe as a mutually beneficial **relationship as humans rodent patrol**." |

Không phải bịa cả câu — là **cắt đuôi không báo và đổi từ**. 158/161 câu còn lại verbatim chính xác, kể cả các lỗi ASR ("urvival", "xhausting", "olerated", "nforced", "he night", "till", "nough").

**B. GẠCH: tổng số từ 21.813.** Đúng là **22.813** theo header (22.901 nếu đếm thật). Sai 1.000 từ. May là mọi mật độ /1000 đều tính trên tổng phụ từng nhóm (6.638 / 9.690 / 6.485 — cả ba đúng) nên các tỷ lệ không hỏng theo.

**C. GẠCH: "0/13 câu cuối là câu hỏi mở".** Bài `20260526` kết bằng **"Not how do I stop feeling this?"** — một câu hỏi. Đúng là 12/13. *(Transcript bài này còn bị ASR cắt giữa chừng — câu kết thật gần như chắc chắn còn vế sau. Mọi phân tích đoạn kết của bài này KHÔNG dùng được.)*

**D. GẠCH: "11/13 bài có re-hook, 2 bài không có gồm 1 bài CAO 4215 vpd".** Sai. **12/13**. Bài 20260730 (4215 vpd) CÓ marker ở 39,4%: *"And yet, here is the detail that should stop you."* — chính họ trích câu này ở mục kho câu rồi lại khai bài đó không có. Chỉ bài cancer (20260614) là 0.

**E. GẠCH: "một bài THẤP không có chữ 'you' nào trong 1736 từ".** Bài guns CÓ 1 lần, ở **từ thứ 383**. Họ ghi đúng ở chỗ khác trong cùng báo cáo rồi tự mâu thuẫn.

**F. GẠCH: "0/13 xưng 'I', 1 lần duy nhất".** Thực tế có **~9 lần "I"** (20260526 tám lần, 20260621 một lần). Tất cả đều là độc thoại nội tâm/giả định của nhân vật, **không** phải giọng người dẫn. Kết luận "kênh không có người dẫn" VẪN ĐỨNG; con số "1 lần duy nhất" thì gạch.

**G. GẠCH: "4/4 CAO đặt câu hứa chiều sâu trong 40 giây đầu".** Tôi đo bằng mốc thời gian từng từ trong VTT:
- dogs **19,4s** ✓ · sleep-dogs **19,0s** ✓
- wolves **43,5s** ✗ · cats **52,8s** ✗ (và nằm NGOÀI chương 1, vốn kết ở 45s)

Đúng là **2/4 trong 40 giây, 4/4 trong ~55 giây**. Kèm theo: "13/13 bài đều có câu kiểu này ở đâu đó" → đo lại được **11/13** (cancer và zebras = 0).

**H. GẠCH: số từ chương 1 "198 / 235 / 217 / 140".** Đo lại từ VTT: **~202 / ~185 / ~117 / ~169** (sai số +10–15 từ). Hai con số 235 và 217 bị thổi lên rõ. Dải **"45–65 giây"** thì ĐÚNG (55 · 65 · 65 · 45s).

**I. GẠCH: "'X years ago' CAO 20 lần = 3,01/1000 từ".** Không dựng lại được bằng bất kỳ regex nào. Đếm "years ago" = CAO 15 (2,25/1k) / THẤP 7 (1,07). Đếm rộng "years ago/old/earlier/later" = CAO 23 (3,45) / THẤP 12 (1,84). **Hướng "CAO neo bằng độ sâu thời gian gấp ~2 lần THẤP" thì ĐỨNG; con số 20 và 3,01 gạch.**

**J. GẠCH: "95 lần hedge = 4,35/1000 từ".** Không dựng lại. Bộ hedge chặt cho 56 lần. Kết luận (hedge không phải bí quyết) vẫn đứng vì CAO ≈ GIỮA dưới mọi cách đếm.

**K. GẠCH: "Let's start with… 9 lần, THẤP dùng gấp 3 CAO".** Thật là **7 lần / 7 bài: CAO 1 · GIỮA 4 · THẤP 2.** GIỮA mới là nhóm dùng nhiều nhất → hạ xuống NẾT.

**L. GẠCH: "'And then' 13 lần / 7 bài, CAO 5 lần ở 3 bài".** Thật **11 lần / 6 bài, CAO 4 lần / 2 bài**. Và câu họ trích *"And that's exactly where humans came in."* không thuộc khuôn "And then".

**M. GẠCH: hai nhãn nhóm sai.** Khuôn "Next time you…" và khuôn T5/T6 đều bị gán `CHI_NHOM_THAP`, nhưng cả hai đều nằm ở bài **GIỮA** (20260621 = 68,8 vpd; 20260721 = 151,9 vpd). Hai khuôn này **không có ở nhóm thấp lẫn nhóm cao** — chỉ 1 bài GIỮA dùng. Vô nghĩa để suy luận.

**N. GẠCH: "đợt 22/05–21/06 tạo ra 88% tổng view".** Đúng là **91,9%** (chính họ ghi 91,86% ở phần số liệu rồi viết 88% ở câu tóm tắt).

**O. GẠCH: "tên chương CAO có You/Your = 7/34 = 20,6%".** Đúng là **9/34 = 26,5%** (họ đếm tên chương ĐỘC NHẤT, quên rằng hai tên trùng xuất hiện ở cả hai video sinh đôi). Hướng mạnh hơn họ nói.

**P. GẠCH: "before X, before Y = 6 lần / 6 bài, CAO 3 bài".** Thật **7 lần / 6 bài; CAO chỉ 2 bài** (bài dogs dùng 2 lần).

**Q. GẠCH: "13/13 bài có chương cuối tên 'Conclusion' hoặc tương đương".** 10/13 đúng tên; 3 bài tên khác hẳn.

---

## KHO CÂU NGUYÊN VĂN — đã xác minh từng chữ, dùng được ngay

*(giữ nguyên lỗi ASR trong ngoặc — đừng chép lỗi vào kịch bản)*

### HOOK — câu mở, ưu tiên "you" ở từ 1
```
You go to bed tonight and something strange happens.            [4215 vpd]
You have a dog, or you want one, or you at least think they are fine.   [3971]
You probably think humans domesticated cats, but what if the opposite happened?
  What if cats didn't become our pets?
  What if we became theirs?                                     [1405]
For most of human history, wolves were monsters.
  If you were alive 30,000 years ago and heard wolves howling beyond the firelight, you knew what they wanted.
  You were prey.                                                [2309]
```

### LỜI HỨA CHIỀU SÂU — đặt trong 20–55 giây đầu
```
The answer is one of the strangest stories in human history, and it did not just give us a companion.
  It gave us [s]urvival. / It gave us civilization. / It may have given us everything.
For tens of thousands of years, sleep itself was one of the most dangerous things a human being could do,
  and the species developed a strange [e]xhausting solution to survive it.
And the reason they did it, and what it ultimately meant for both species,
  is one of the most extraordinary stories in the history of life on this planet.
And the strangest part is that it's [s]till happening right now inside your home, probably while you're watching this.
```

### RE-HOOK — chỉ đặt trong khoảng 25–64% độ dài bài
```
Here is the part that stops most people.
Here is where most people's understanding stops.
  Guard duty, hunting help, that is the surface version.
  It does not come close to capturing what actually happened.        ← khuôn HẠ BỆ RỒI ĐÀO SÂU, đầy đủ nhất
Here's where something genuinely strange happened.
Here is the part most people never hear.
But here is the part scientists find genuinely remarkable.
But here is where the story shifts from ancient history into something more unsettling.
And yet, here is the detail that should stop you.
```

### CÂU CỤT PHỦ ĐỊNH RỒI LẬT — nhịp chính của kênh (nết chung, dùng vừa phải)
```
Not a coincidence, an equation.
Not because it planned it, because the cats that did it got fed first.
Not because anyone [e]nforced it, because both sides kept finding reasons to stay.
That is not normal. / That is not how your ancestors slept for most of human history.
It was not company. / It was permission.
```

### CHUYỂN CHƯƠNG — cơ chế thật là MÓC XÍCH + cắt cứng bằng mốc năm
```
To understand why wolves would ever approach a human camp, you have to understand what their lives actually looked like.
To understand how a small desert predator quietly took control of one of the most intelligent species on Earth,
  you have to go back to the moment humans made their biggest mistake.

40,000 years ago, this was not our world, not even close.
30,000 years ago, wolves were everywhere.
45,000 years ago, Neanderthals were everywhere in Europe. / 5,000 years later, they were gone.

The standard story of domestication is a story of human control.
  We tamed things. / We decided which animals were useful. / We brought them into our world on our terms.
  But wolves didn't follow that script.

Think about [t]he night.
Think about what that actually means.
```

### CÂU KẾT — bắt buộc có "you", chốt cứng, không hạ nhiệt
```
It was not company. / It was permission.
Permission to finally close your eyes all the way for the first time since we came down out of the trees
  and trust that something else was listening instead.                    [4215 vpd]

40,000 years later, its descendants are asleep at the foot of your bed.
The world you live in, every part of it, sits downstream of a wolf that was hunting the same prey
  as your ancestors one night and made a different calculation than anyone expected.
That is the whole story, and it is the most important one we have.        [3971]

Two predators, one fire, and a choice that neither species fully understood at the time.
But you do now.                                                           [2309] ← 4 từ, chốt mạnh nhất kênh

The cat didn't get domesticated, it just found a better place to be wild. [1405] ← lật lại chính tên bài
```

### MỎ NEO — không tên người, không năm, không tạp chí
```
Researchers call it the sentinel hypothesis, and it appears to be baked directly into human biology.
For decades, scientists argued about why.
Researchers who study modern hunter-gatherer groups, communities that still live largely as humans did
  for most of our history, have found something that reshapes how we…
The actual one is that without that animal, the species probably does not spread,
  the civilizations probably do not get built.
It may have been the single greatest competitive advantage in the ancient world.
```

---

## CÒN THIẾU — chiều nào KHÔNG kết luận được và vì sao

1. **Không tách được ĐỀ TÀI khỏi CÁCH VIẾT — đây là lỗ hổng chí mạng, không phải cảnh báo lịch sự.** 4/4 bài CAO là chó/sói/mèo, viết trong cùng một đợt, 2 trong 4 dùng chung bộ xương. Mọi phát hiện dán nhãn "CHỈ NHÓM CAO" ở trên có thể là hệ quả của việc viết về thú cưng, không phải nguyên nhân của view. Chứng cứ ngay trong kênh: cùng khuôn title *"Why Ancient Humans Couldn't X"* mà chó ra 4215 vpd, ngựa vằn ra 16,3 — chênh 259 lần. **Muốn tách được thì phải có ít nhất 1 bài đề tài-không-thú-cưng viết đúng 12 luật CAO ở trên rồi đo kết quả.** Kênh này chưa có bài đó, nên không tồn tại bằng chứng nào cho "cách viết thắng".

2. **Không có CTR / AVD / retention curve.** `info.json` chỉ có view/like/comment/chapters/description. Nên **không biết hook có giữ chân thật không** hay chỉ là thumbnail + title kéo view rồi người ta bỏ. Toàn bộ chương 1, 2, 3 (hook / giữ chân / kết) đang được suy ra từ VIEW — mà view thì do thumbnail quyết định. Đây là suy luận vòng.

3. **Không có thumbnail.** Thư mục không có ảnh. Theo chính kho của chủ (`insight_clone_swarm`), biến quyết định là THUMBNAIL — và nó hoàn toàn vắng mặt khỏi bài bóc này. **Bài bóc đang đo thứ có thể không phải nguyên nhân.**

4. **Ranh giới chương không phải ranh giới tu từ** — điểm này họ nói đúng và tôi xác nhận: chapters lấy từ description do kênh tự khai, mốc rơi giữa dòng chảy văn (bài 20260730 mốc C1→C2 rơi đúng giữa cặp "…sleep was not rest. / Sleep was risk stacked 8 hours deep…"). Nên **"câu mở chương" không tồn tại như một đơn vị**; thứ tồn tại là câu cầu.

5. **Bài zebras (49 view / 3 ngày) phải treo hoàn toàn.** Bỏ nó ra thì sàn nhóm thấp là 35,0 vpd chứ không phải 16,3. Nhưng bỏ nó ra thì nhóm THẤP còn n=3, và mọi con số "0/4 bài THẤP" ở trên thành "0/3".

6. **Transcript là ASR có lỗi nuốt phụ âm đầu** — xác nhận: "urvival", "xhausting", "till", "he night", "nough", "olerated", "nforced", "volutionary", "phisticated", "amydala", "mpty", "tory", "es" (=yes). Bài 20260526 còn bị cắt cụt ở câu cuối. **Đừng chép nguyên si vào kịch bản.**

7. **Chưa đo: nhịp đổi ảnh, giọng đọc, nhạc nền, mid-roll.** Kênh đọc 174–213 wpm (nhanh, bài 4215 vpd đọc nhanh nhất kênh: 213 wpm) — đây là con số đáng thử, nhưng không có gì chứng minh nó gây ra view.
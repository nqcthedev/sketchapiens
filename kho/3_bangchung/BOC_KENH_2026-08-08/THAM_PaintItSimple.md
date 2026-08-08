Đã mở cả 7 file `.txt` + 7 file `_vtt/*.info.json`, đếm lại bằng python, dò từng câu trích.

---

# GIÁM ĐỊNH BẢN BÓC — PaintItSimple (n = 7)

**Thư mục:** `/Users/admin/Claude/Projects/Build Channel Người Que Cổ Đại/2_KHO_BANGHI/PaintItSimple/`

**Nói thẳng trước:** kênh này **quá ít bài để rút bí quyết thắng**, và tệ hơn n=7 là một lỗi cấu trúc mà bản bóc không xử lý — xem mục ĐÃ GẠCH #1. Về trích dẫn thì bản bóc **sạch**: tôi dò 190 câu trích, **0 câu bịa, 0 câu sửa chữ, 0 câu gán nhầm file**. Sai nằm ở **đếm và ở nhãn**, không nằm ở trích.

---

## ĐỨNG VỮNG — có trích thật, có mẫu số, một chiều

Sau khi loại confound thời gian, **không phát hiện nào đạt đủ ba điều kiện** "có trích thật + có mẫu số + chỉ nhóm cao mới có + giải thích được view". Cái đứng vững đều là **phát hiện PHỦ ĐỊNH** — tức bác bỏ một giả định, chứ không phải kê đơn.

**1. TITLE KHÔNG PHẢI ĐỘNG CƠ — bằng chứng mạnh nhất cả bản bóc. ✅ ĐÚNG NGUYÊN VẸN**
Hai bài đăng cách nhau **2 ngày**, cùng khuôn, cùng chữ CRAZIEST:
- `The CRAZIEST Survival Methods Used by Ancient Humans During Ice Age` — 01/05 — 1.930.169 view — **19.497 v/ngày**
- `The Craziest Communication Methods Used by Ancient Humans` — 29/04 — 6.471 view — **64 v/ngày**
Chênh **304,6 lần**. Tôi tính lại từ header: khớp.
7/7 title chứa "Ancient Humans". Dấu `?`: 4/7 có (trung vị 902 v/ngày) · 3/7 không (trung vị 94) — nhưng bài cao nhất nằm ở nhóm KHÔNG có `?` → **không kết luận được**, đúng như bản bóc tự khai.

**2. 0 dấu `!` trên 10.911 từ / 7 bài.** Tôi đếm máy: 0/0/0/0/0/0/0. ✅

**3. 0/7 bài mồi video kế ở đoạn kết. 0/7 bài có "stay until the end".** Grep `next video|watch|check out|playlist|click|another video` trong 202 từ cuối: **0 hit / 7 bài**. ✅ Kênh chấp nhận mất click kế tiếp để giữ trọn cú chốt.

**4. CTA gần như bằng 0, và 2 quả to nhất tuyệt đối không xin gì.** ✅
4/7 bài có **0 câu** subscribe/like/comment/channel — gồm cả 1.930.169 view và 291.240 view. Toàn kênh **5 câu CTA / 10.911 từ = 0,46 câu/1.000 từ**. Đếm máy khớp 100%.

**5. 7/7 video KHÔNG khai báo chapters.** Xác nhận từ `info.json`: `chapters = None` cả 7. ✅ (bản bóc khai đúng)

**6. Tín hiệu like NGƯỢC — verified từ `info.json`, không phải suy đoán.** ✅
| bài | view | like | like/view | comment |
|---|---|---|---|---|
| 20260501 | 1.930.169 | 18.999 | **0,98%** ← thấp nhất | 975 (0,05%) |
| 20260519 | 291.240 | 8.111 | 2,78% | 2.000 (0,69%) |
| 20260506 | 158.195 | 2.124 | 1,34% | 293 |
| 20260614 | 6.705 | 193 | 2,88% | 55 |
| 20260429 | 6.471 | 170 | 2,63% | 23 |
| 20260712 | 2.539 | 69 | 2,72% | 19 |
| 20260710 | 1.060 | 33 | **3,11%** ← cao nhất | 10 |
Quả 1,93 triệu có tỷ lệ like **thấp nhất kênh**, thấp hơn bài 1.060 view **3,2 lần**. Đây là chữ ký của **traffic lạnh do thuật toán đẩy**, không phải kịch bản ăn đứt. Mọi câu "vì viết thế nên nổ" đều phải đi qua con số này.

**7. Hai tín hiệu MỘT CHIỀU nhưng n=2 — ghi lại, đừng làm luật:**
- 2 bài có mật độ câu cụt ≤6 từ thấp nhất kênh (**2,0** ở 20260614 và **3,0** ở 20260710) là rank 4 và rank 7. Cả 5 bài còn lại đều ≥10,2. Đếm máy khớp tuyệt đối con số của bản bóc: 16,8 · 13,5 · 10,2 · 15,7 · 13,9 · 3,0 · 2,0.
- 2 bài **không có câu hỏi nào trong 220 từ đầu** (20260614, 20260712) đều ở nửa dưới.
→ Cả hai chỉ đủ nói **"thiếu thì chìm"**, không đủ nói "có thì nổ" — vì 20260429 (rank 6) có 15,7 câu cụt/1.000 và câu hỏi ở từ thứ 78.

---

## NẾT CỦA KÊNH — đúng, đo được, nhưng CẢ CAO LẪN THẤP đều có. Không phải bí quyết.

| Nết | Số liệu tôi đếm lại | Vì sao không phải bí quyết |
|---|---|---|
| Mệnh lệnh động tay vào đồ vật đời thường ở dòng 1 | 4/7 | Có ở quả 19.497 v/ngày **lẫn** quả 37 v/ngày |
| "you/your" trong 11 từ đầu | 6/7 | Bài **duy nhất** không có (20260519, first `you` ở **từ thứ 171**) là quả #2 của kênh |
| Mật độ `you` toàn bài | 16,8 · 5,1 · 7,2 (trên) vs 24,8 · 20,4 · 9,9 · 5,9 (dưới) | Nhóm CAO dùng `you` **ÍT HƠN**. Bài dày `you` nhất kênh (24,8) chỉ 122 v/ngày |
| Câu "The answer…" ngay sau câu hỏi lõi | 5/7 | 3 trên + 2 dưới |
| Câu cụt ≤6 từ làm nhịp đấm | 5/7 bài ≥10,2/1.000 | 2 bài dày nhất sau quả nổ là rank 5 và rank 6 |
| Meta re-hook "Here's…" | 7/7 bài, 13 lần (10 "here's/here is" + 3 "this is where") | Có ở **mọi** bài, kể cả bài 37 v/ngày |
| Khuôn "không phải A, là B" | 7/7 bài (xem gạch #5 — bản bóc đếm sai phân bổ) | Bài 94 v/ngày dùng khuôn này **dày nhất kênh** (≥8 lần) |
| Bookend quay lại đồ vật của hook @89–92% | 4/7 | 2 cao + 2 thấp (gồm bài 37 v/ngày và bài 64 v/ngày) |
| Câu bậc nhất tại chỗ ("of all the…") | 4/7 | 2/4 nằm ở hai bài thấp nhất kênh |
| Định danh người xem ("bạn là kẻ thừa kế") | 5/7, cụm "that's you" nguyên văn = **0/7** | cả hai nhóm |
| "The next time you…" ở câu chốt | 2/7 | một cao (19.497) một thấp (37) |
| 0 tên nhà nghiên cứu trong 45 giây đầu | **0/7** — grep xác nhận | nết tuyệt đối |
| Khung độ dài khoá cứng | 8:03–9:29 · 1.469–1.690 từ · biên độ **1,15×** | 7/7 bài. Bài nổ đọc **chậm nhất** (157 wpm), bài chìm nhất đọc **nhanh nhất** (188 wpm) — n=1 mỗi phía, không suy ra được gì |
| Không xây series | 0/7 đánh số, 1/7 tham chiếu mờ | nết |
| Số token số trong bài | 26 · 21 · 28 · 13 · 23 · 26 · 5 | bài 94 v/ngày có 26 token số, ngang bài 1,93 triệu → **không dự báo** |

---

## ĐÃ GẠCH

**1. 🔴 GẠCH NẶNG NHẤT — "nhóm trên" thực chất là "3 bài đăng ngay sau cú nổ". Toàn bộ 8 nhãn `CHI_NHOM_CAO` của bản bóc bị confound với NGÀY ĐĂNG, không phải với cách viết.**

Xếp theo ngày đăng, kèm rank v/ngày:
```
29/04 →     64 v/ngày (rank 6)   ← đăng TRƯỚC cú nổ 2 ngày
01/05 → 19.497 v/ngày (rank 1)   ← CÚ NỔ
06/05 →  1.683 v/ngày (rank 3)
19/05 →  3.596 v/ngày (rank 2)
────────────────────────────────  vách đá
14/06 →    122 v/ngày (rank 4)
10/07 →     37 v/ngày (rank 7)
12/07 →     94 v/ngày (rank 5)
```
"Nhóm trên" = **đúng 3 bài đăng trong 18 ngày sau cú nổ**. Bài đăng 2 ngày **trước** cú nổ, cùng khuôn title, cùng cách viết → rank 6. 4/4 bài đăng từ 14/06 (sau khi nhiệt suggested tắt) đều <122 v/ngày, **bất kể viết thế nào**.

Nghĩa là: mọi khuôn "chỉ nhóm cao có" đều **giải thích được bằng ngày đăng** thay vì bằng câu chữ, và dữ liệu này **không tách được hai thứ đó**. Bản bóc có nêu chuyện này ở chiều 9 nhưng vẫn tiếp tục gắn nhãn `CHI_NHOM_CAO` cho 8 phát hiện ở chiều 1, 2, 3, 5, 6, 7 — **không được phép**.

**2. GẠCH "mật độ re-hook nhóm trên 1,1 vs nửa dưới 1,1 — bằng nhau tuyệt đối".** Lỗi mẫu số: họ đếm 5 hit của nửa dưới (trong đó 2 hit thuộc 20260614) nhưng chia cho **4.668 từ = chỉ 3 bài dưới, đã loại 20260614**.
Số đúng: nhóm trên **6 hit / 4.711 từ = 1,27**/1.000 · nửa dưới 4 bài **5 hit / 6.200 từ = 0,81**/1.000. Không bằng nhau — nhóm trên dày hơn 57%. Kết luận cuối vẫn là NẾT (7/7 bài đều có), nhưng **con số "bằng nhau tuyệt đối" phải xoá**, đừng dán vào luật kênh.

**3. GẠCH "KẾT KHÔNG CÓ `you` — chỉ 1/7 bài, và đó là quả #2" (nhãn `CHI_NHOM_CAO`).** SAI. Đếm `you\w*` trong 202 từ cuối: 20260501=8 · **20260519=0** · 20260506=1 · 20260614=4 · 20260429=10 · **20260712=0** · 20260710=3.
→ **2/7 bài**, và bài thứ hai là 20260712 — **94 v/ngày, rank 5**. Nhãn `CHI_NHOM_CAO` chết. Hạ xuống: kết thuần khoa học không `you` xuất hiện ở cả hai đầu bảng.

**4. GẠCH "2 bài chốt bằng CÂU HỎI MỞ đều nằm nửa dưới — dấu hiệu DUY NHẤT ở chiều kết bài mà hai nhóm không chồng nhau".** SAI về sự kiện.
Câu **cuối cùng** của 20260614 là câu **khẳng định**: `"And somehow, they also found time to make art that can still stop you cold 30,000 years later."` Câu hỏi `"So, how would you have fared in the Ice Age?"` nằm ở **96%**, còn 4 dòng nữa mới hết bài.
→ Chỉ **1/7** bài kết bằng câu hỏi (20260710). n=1 = không có tín hiệu. **Chiều 3 (60 giây cuối) do đó KHÔNG còn phát hiện phân biệt nào.**

**5. GẠCH phân bổ "17 câu 'không phải A, là B' — 20260519 = 0, 20260712 = 0".** SAI. Grep ra:
- 20260519 có ít nhất 4: `"Dark skin wasn't a variation."` / `"Not some of them, all of them."` / `"The skin was getting lighter, not by choice, not by chance, by survival."` / `"…pale skin isn't one thing that happened once."`
- 20260712 có ít nhất 8, dày nhất kênh: `"Not an imal, a person, but not quite."` · `"That's not what happened."` · `"Not for food."` · `"That's not instinct."` · `"They didn't just cross paths with us on the way to extinction."` · `"They didn't just survive each other."` …

Khuôn này có ở **7/7 bài**, và bài dùng dày nhất là **94 v/ngày**. Con số 17 và phân bổ 10/7 không đứng; khuôn vẫn giữ nhưng chỉ ở mức **NẾT**.

**6. GẠCH "cửa sổ hẹp 5,8–8,4 từ thẩm quyền/1.000 từ" — đây là window-fitting.** Bản bóc đặt trần ở 8,4 trong khi bài nửa dưới 20260614 = **8,5** — lệch **0,1**. Tôi đếm lại bằng danh sách từ thẩm quyền rộng hơn một chút (thêm `anthropologist/biologist/excavate/bioarchaeological/sequenced`): nhóm trên = **11,4 · 7,1 · 7,8**, còn 20260614 = **8,5 → nằm TRONG cửa sổ**. Đổi danh sách từ là cửa sổ vỡ ⇒ **artifact của cách đếm, không phải nết của kênh**. Bỏ.

**7. GẠCH nhãn "vị trí câu hỏi lõi = `CHI_NHOM_CAO`".** Bản bóc viết "nhóm trên 3/3 có câu hỏi ≤ từ thứ 117 (64 · 75 · 117)" — đúng số, sai nhãn: **20260429 (rank 6) đặt câu hỏi lõi ở từ thứ 78**, tức **sớm hơn 2 trong 3 bài nhóm trên**. Ngưỡng 117 được chọn sau khi biết đáp án. Hạ xuống NẾT.

**8. GẠCH "THỨ TỰ LEO THANG PHỤ THUỘC — 3/3 nhóm trên, chỉ 1/4 nửa dưới".** Phân loại sai. **20260429 (64 v/ngày, rank 6) có chuỗi phụ thuộc SẠCH NHẤT kênh**: bullroarer → *chết trong rừng rậm* → trống → *"But drums had one problem. Dense forest swallowed the sound. Mountains blocked it. Open plains killed it completely."* → khói/lửa → *"But fire and smoke still needed one thing your ancestors could not always guarantee, clear weather and a clear sky."* → chạy tiếp sức chasqui. Chính bản bóc trích nguyên cụm này ở chiều 6 làm ví dụ mẫu cho KHUÔN B, rồi lại xếp bài đó vào "danh sách không leo". Mâu thuẫn nội bộ → nhãn `CHI_NHOM_CAO` bị gạch. "Leo thang" là NẾT, và nó **không cứu được** bài 64 v/ngày.

**9. GẠCH "cú lật lớn nhất nằm trong dải hẹp 52–59% chỉ ở nhóm trên".** Hai lỗi:
   a) 20260710 (**thấp nhất kênh, 37 v/ngày**) đặt cú lật ở **57%** — nằm **TRONG** dải. Chính bản bóc thừa nhận ở `ca_nguoc` rồi vẫn gắn `CHI_NHOM_CAO`.
   b) "Cú lật lớn nhất" là do người bóc **tự chọn sau khi biết view**. 20260501 có ít nhất 2 ứng viên ngang nhau: `"Now, here's where it gets extraordinary."` @27% và `"Now, here's the part most documentaries skip entirely."` @53%. Chọn cái thứ hai làm dải khớp là hindsight.
   c) **Dữ liệu heatmap bác luôn dải này** — xem CÒN THIẾU #1: đỉnh replay thật nằm ở **63–73%**, không phải 52–59%.

**10. GẠCH "4/7 bài nêu tên nhà nghiên cứu".** Đúng là **3/7 bài / 4 tên**: 20260501 (Thomas Wehr + Polly Wiessner), 20260614 (Brian Fagan), 20260712 (Steven Churchill). Nhầm "tên" thành "bài". Con số 0,37 tên/1.000 từ thì đúng.

**11. GẠCH toàn bộ chiều 5 "BỘ XƯƠNG CHƯƠNG" ở mức luật — chỉ giữ ở mức ghi chép.** `chapters = None` cả 7 video (tôi xác nhận trong `info.json`). "66 mốc", "8–14 khối", "trung vị 136 vs 127,5 từ/khối" đều là **do người bóc tự cắt**, không kiểm chứng lại được, và chính họ khai chênh lệch hai nhóm chỉ 8,5 từ. **Không dùng làm luật viết.**

**12. GẠCH suy luận "làm lại đề tài của chính mình chỉ đạt 0,35%".** Số đúng (6.705/1.930.169 = 0,347%), trùng từ khoá đúng (mammoth bone 3 vs 2 · Mezhyrich 1 vs 2 · fire 9 vs 7 · hide 6 vs 4). **Nhưng quy nạp sai**: 20260614 đăng 14/06, và **4/4 bài đăng từ 14/06 trở đi đều <122 v/ngày bất kể đề tài gì** (Viking food 37, gặp loài người khác 94). Không tách được "làm lại đề tài" khỏi "hết nhiệt suggested". Cảnh báo "nổ rồi thì đừng làm tiếp đề tài đó" **chưa có bằng chứng** từ kênh này.

**13. SỬA `gioi_han` #6 "7/7 file chỉ có lời đọc, không đo được retention".** SAI — kho có `_vtt/*.info.json` chứa **heatmap (most-replayed), tags, description, thumbnail URL, like, comment**. Bản bóc đã dùng like/comment (đúng số) nhưng khai là không có. Xem CÒN THIẾU.

**14. Sai vặt, không ảnh hưởng kết luận:** mật độ `you` của 20260712 ghi 11 → thật là **9,9**; trung vị `you` nửa dưới ghi 15,5 → thật **15,2**; số từ hook của 20260506/20260614/20260429/20260712 lệch 10–40 từ do điểm cắt hook là chủ quan; vị trí % lệch 1–2 điểm ở khoảng 8 câu trích (do đếm theo dòng vs theo từ). Comment count 2.000 của 20260519 là **số tròn nghi bị làm tròn/chặn bởi API** — đừng dùng để so tỷ lệ chính xác.

---

## KHO CÂU NGUYÊN VĂN (đã dò từng ký tự — tất cả tồn tại đúng file)

> ⚠️ Transcript auto-gen nuốt chữ đầu. Sửa trước khi dùng: `hrive→thrive` · `tart→start` · `ur→fur` · `imal→animal` · `ntire→entire` · `tranger→stranger` · `equenced→sequenced` · `urns→turns` · `verything→everything` · `he→the` · `e→the` · `o→to` · `ou→you` · `id→did` · `ything→anything` · `hrough→through` · `nd→end` · `aching→reaching` · `enetrated→penetrated` · `rive→drive` · `elected→selected` · `tretching→stretching` · `eir→their` · `tudying→studying` · `ating→heating` · `teppe→steppe` · `uring→during` · `rds→herds` · `roups→groups` · `ime→time` · `ark→dark` · `eformed→deformed` · `fficiently→efficiently` · `ehydrated→dehydrated` · `tockfish→stockfish` · `rying→drying` · `ish→fish` · `carce→scarce` · `verywhere→everywhere` · `ometimes→sometimes` · `tructural→structural` · `tretched→stretched` · `lentlessly→relentlessly` · `ocial→social` · `trange→strange` · `erved→served` · `tructured→structured` · `ayers→layers` · `haring→sharing` · `vidence→evidence` · `uggests→suggests` · `ifferent→different` · `ature→nature` · `xpected→expected` · `eep→deep` · `ervice→service` · `nd point→end point`

### HOOK — dòng 1
```
Check your thermostat right now.                                    [20260501 · 19.497 v/ngày]
Think about the last time you went to a grocery store.              [20260506 · 1.683]
Pick up your phone right now and text someone.                      [20260429 · 64]
Tonight, when you're hungry, you'll open a fridge.                  [20260710 · 37]
In 1903, a group of workers digging a drainage ditch in Somerset, England,
  pulled a human skeleton out of the ground.                        [20260519 · 3.596]
Imagine you're walking through a river valley in the Middle East
  90,000 years ago.                                                 [20260712 · 94]
Movies, documentaries, and every animated prehistoric film you watched
  as a kid have sold you a very specific fantasy about the Ice Age.  [20260614 · 122]
```

### CÂU HỎI LÕI + LỜI HỨA "The answer…" (cặp dính liền)
```
So, how did they not just survive, but hrive?                                   [từ 64]
The answer is not what you think, and it will permanently change how you look
at your own home.                                                        [20260501, từ 73]

So, how did they do it?                                                         [từ 75]
The answer isn't one method, it's a collection of strategies so creative, so
ruthless, and so shockingly sophisticated that modern scientists are still
uncovering new evidence of them today.                                   [20260506, từ 110]

So, how did they actually send messages over long distances?                    [từ 78]
The answer would horrify most people alive today, and it is proof of just how
difficult your ancestors truly lived.                                    [20260429, từ 88]

And that raises a question that urns out to have a surprisingly complicated answer.
How did human skin go from universally dark to the spectrum of colors we see today?
And why did it happen at all?                                            [20260519, từ 103-133]
```

### RE-HOOK (13 câu — toàn bộ kho, % theo từ)
```
Here is the first thing archaeology got wrong about your ancestors.      [20260501 @13%]
Now, here's where it gets extraordinary.                                 [20260501 @27%]
Now, here's the part most documentaries skip entirely.                   [20260501 @53%]
Now, here's where the methods become genuinely unsettling because the next
  strategy didn't use walls or spears at all.                            [20260506 @46%]
And this is where the physics became a problem.                          [20260519 @40%]
This is where vitamin D stopped being a health issue and became an
  evolutionary filter.                                                   [20260519 @51%]
But here is what makes this story genuinely surprising.                  [20260519 @92%]
But here's the thing, the real Ice Age was nothing like that.            [20260614 @3%]
Here's a number that should genuinely alarm you.                         [20260614 @16%]
Here's where the story turns.                                            [20260712 @35%]
Here's the part almost nobody talks about.                               [20260710 @57%]
Here is what nobody tells you.                                           [20260429 @91%]
This is where modern Arctic engineers are genuinely impressed.           [20260501 @54%]
```

### CHUYỂN CHƯƠNG — 5 khuôn, dùng lại được nguyên văn

**KHUÔN A — nâng cấp ("cái vừa rồi chưa là gì")**
```
But he real sophistication came later.                                   [20260501 @19%, 6 từ]
Now, here's where it gets extraordinary.                                 [20260501 @27%, 6 từ]
And then there was the strangest, most ingenious method of all, turning fish
  into something closer to wood.                                         [20260710 @32%]
And then humans took every one of these methods and multiplied them by adding
  the one thing no other predator had ever developed, language, planning,
  coordinated strategy across a group.                                   [20260506 @79%]
```

**KHUÔN B — bàn giao vấn đề (dùng nhiều nhất kênh). Cụm 5 câu này là hàng tốt nhất bóc được:**
```
But drums had one problem.
Dense forest swallowed the sound.
Mountains blocked it.
Open plains killed it completely.
So, your ancestors went looking for something that could travel further,
something no mountain could block and no forest could swallow.           [20260429 @39%]
```
```
But this process needed a catalyst.
Gradual pressure alone wasn't enough to transform an entire continent.
What it needed was a single mutation powerful enough to accelerate verything. [20260519 @83%]

But clothing could only solve one of your problems.
The rest of them had teeth.                                              [20260614 @60%, 9+6 từ]

But none of this worked without fire, and fire wasn't just warmth, it was the
entire operating system of Ice Age winter life.                          [20260501 @38%]

But fire and smoke still needed one thing your ancestors could not always
guarantee, clear weather and a clear sky.                                [20260429 @48%]

But not every household could afford enough salt.
So, they turned to smoke.                                                [20260710 @26%]
```

**KHUÔN C — phủ định để mở món mới**
```
Some ancient hunters did not rely on spears at all.
Instead, they turned simple stones into deadly weapons.                  [20260506 @22%]
Some hunters didn't want to be anywhere near the animal at all.
So, they built something instead.                                        [20260506 @32%]
But the Neanderthals weren't the only ones out there.                    [20260712 @55%]
So, they built something else ntirely.                                   [20260429 @53%]
```

**KHUÔN D — đếm món, 5 từ (RẺ NHẤT — chỗ bài danh-sách lộ mặt)**
```
And then there was ventilation.                                          [20260501 @48%]
Then there were the shells.                                              [20260712 @75%]
The first threat was violence. / The second possibility was avoidance.   [20260712 @20%, @29%]
Then there was butter, treated less like a condiment and more like stored energy. [20260710 @51%]
```

**KHUÔN E — tự bẻ lập luận của chính mình (chỉ 1/7 bài dùng, là cột sống bài 291K)**
```
And yet, the math never added up.
If this filter was running every single generation, dark skin should have
disappeared from northern Europe within a few hundred generations.
But, the genetic evidence shows that as recently as 10,000 years ago,
that's Cheddar Man's time, most Europeans still had dark skin.           [20260519 @56%]

For 35,000 years, the selection pressure existed, but the skin barely changed.
Why?
The answer came from an unexpected direction, diet.                      [20260519 @68%]
```

### ĐÓNG CHƯƠNG — câu tuyên bố cụt
```
Your ancestors didn't fight the cold, they went below it.
That is not survival instinct, that is architecture.
The materials were different, the physics were identical.
The layout wasn't random, it was planned.
They were managing fuel like a resource.
These weren't reactive builders, they were planners with seasonal calendars
  running in their heads.                                                [tất cả 20260501]
It was the whole plan.  /  This was not random.  /  That is not instinct. [20260506]
Nothing in nature prepared any animal for an enemy that cannot be outrun. [20260506]
It was not music. / It was not rhythm for the sake of rhythm. / It was information. [20260429]
Lighter skin survived, darker skin struggled.                            [20260519]
That's not instinct. / That's culture crossing a species line.           [20260712]
```

### NHỊP ĐẤM — câu 1–4 từ
```
Houses.  ·  Picture this.  ·  Let that sink in.  ·  Why?                 [20260501]
Seven bones.  ·  They expected Neanderthal.  ·  It wasn't.  ·  Not for food. [20260712]
They were mega traps.  ·  It used chemistry.  ·  They just never stopped running. [20260506]
These women lived.  ·  Their darker-skinned counterparts didn't.  ·  Why? [20260519]
The drum is still beating.  ·  You just cannot hear it anymore.          [20260429]
```

### BOOKEND + CHỐT
```
Go back to your thermostat.                                              [20260501 @89%, 5 từ]
Go back to that grocery store.                                           [20260506 @91%, 6 từ]
Now, think about your own kitchen.                                       [20260710 @89%, 6 từ]

You didn't invent warmth, you inherited it from the most ingenious engineers who
ever lived, who had nothing but cold, time, and the refusal to die.
The next time the cold comes, and you reach for that thermostat without thinking,
remember what it cost o get there, and understand for the first time how
extraordinarily rare it is to be warm.                                   [20260501, 2 câu cuối]

And yet here we are, every one of us alive today, the direct descendant of
someone who figured it out.                                              [20260506, câu cuối]

Biologists call this convergent evolution.
It's the same process that gave dolphins and fish similar body shapes despite
being completely unrelated animals.
The environment poses a problem.
Evolution finds a solution.
...Low UV, grain diet, vitamin D crisis, selection pressure, mutation, survival. [20260519, kết]

You are still that person on the hilltop.
You are still scanning the horizon for a signal.
The only difference is the horizon is a phone screen now, and the signal is a
notification.                                                            [20260429 @67%]
```

### CẮT NHÁNH LẠC ĐỀ (1 lần duy nhất toàn kênh — dùng để CẮT, không phải câu view)
```
How exactly fur disappeared over hundreds of thousands of generations is a
fascinating story in itself, but that's a separate video.                [20260519 @22%]
```

---

## CÒN THIẾU

**1. 🔥 HEATMAP most-replayed NẰM SẴN TRONG KHO MÀ CHƯA AI MỞ.** `_vtt/*.info.json` có `heatmap` 100 điểm cho **3 video nhóm trên** (YouTube chỉ hiện heatmap khi đủ view — 4 bài dưới = 0 điểm). Đây là **thứ duy nhất trong kho chạm được retention**. Tôi đọc thử:

| bài | đỉnh replay | nội dung tại đỉnh |
|---|---|---|
| 20260501 | **73%** | `"These weren't reactive builders, they were planners with seasonal calendars running in their heads."` |
| 20260519 | **63%** | đoạn diet giải được nghịch lý vitamin D |
| 20260506 | **66%** | đoạn cơ thể người chạy bền (mồ hôi / gân Achilles / cơ mông) |

→ **Đỉnh giữ chân thật nằm ở 63–73%, KHÔNG phải 52–59% như bản bóc suy ra từ câu chữ.** Điểm chung của 3 đỉnh: đều là **câu TRẢ CÔNG** (chốt lại cái mà cả bài đã dựng), không phải câu **mở** cú lật. Đây là hướng đáng đào tiếp, và đào bằng số chứ không bằng cảm.
Hạn: chỉ có ở 3 bài cao ⇒ **không so cao-thấp được**, chỉ mô tả được nội bộ 3 bài nổ.

**2. TAGS + DESCRIPTION chưa ai đọc.** Có đủ 7 bài. Ví dụ 20260501 có **20 tag** (`boring history`, `how did ancient humans sleep`, `kostenky`, `dolni vestonice`…) và description 1.297 ký tự; 20260710 có **30 tag**; 20260506 chỉ **1 tag** nhưng description **3.568 ký tự**; 20260429 có **0 ký tự description**. Nếu muốn kiểm giả thuyết "SEO/metadata có liên quan gì không" thì dữ liệu đã nằm sẵn.

**3. THUMBNAIL** — có URL trong `info.json` cả 7 bài, chưa tải, chưa đo. Với kết luận #1 (title không phải động cơ) thì thumbnail là **biến còn lại chưa loại được**, và nó là biến khả dĩ nhất.

**4. CTR / impressions / AVD thật** — không có và không lấy được từ ngoài. Mọi câu về "giữ chân" trong bản bóc (cả của họ lẫn của tôi) đều là **suy từ câu chữ**, trừ mục #1.

**5. Nhịp đổi ảnh / hình ảnh / giọng đọc** — 0 dữ liệu. Với kênh explainer, đây có thể là biến lớn hơn cả kịch bản.

**6. Không thể tách "viết hay" khỏi "được đẩy".** Với n=7, 1 bài = 80,5% view, tỷ lệ like nghịch, và "nhóm trên" trùng khít với "3 bài đăng sau cú nổ" — **dữ liệu này về nguyên tắc không trả lời được câu hỏi "viết thế nào thì nổ"**. Nó chỉ trả lời được: **"kênh này viết theo khuôn gì"** (mục NẾT, dùng được ngay làm kho câu) và **"cái gì chắc chắn KHÔNG phải nguyên nhân"** (title, CTA, mật độ `you`, số liệu, di chỉ, nhịp đăng, độ dài).

**7. Muốn kết luận nhân quả thì cần thêm ≥3 kênh cùng ngách có phân bố view đều hơn** — kênh mà top-2 chiếm <50% tổng view. PaintItSimple là ca trúng số, dùng nó làm chuẩn cầu là lặp lại đúng cái sai đã ghi trong `BOCTACH_4Kenh_SoSanh_2026-08-04.md`.
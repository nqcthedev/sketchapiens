Verification complete. Writing up.

---

# GIÁM KHẢO — kênh Mogo (31 bài)

**Đã mở cả 31 file. Đối chiếu 225 câu trích, đếm lại 40+ con số, và chạy thêm 2 phép kiểm mà bản gốc không chạy: kiểm ý nghĩa thống kê (Mann-Whitney) và kiểm nhiễu thời gian (tách trong từng kỷ nguyên).**

Kết luận đầu: **phần trích dẫn rất sạch, phần suy luận thì hỏng nặng.** 223/225 câu trích có thật, đúng file, gần như đúng từng chữ — hiếm có. Nhưng 5 trong 8 phát hiện gắn nhãn "CHỈ_NHÓM_CAO/THẤP" đều chết khi kiểm nhiễu ngày đăng.

---

## ĐỨNG VỮNG

**1. Cụm đề tài GIẤC MƠ/GIẤC NGỦ là nghĩa địa — phát hiện chắc nhất cả bản bóc.**
Đây là thứ duy nhất sống sót MỌI phép kiểm. Không dựa vào view/ngày:

| bài | ngày | tuổi | view thô |
|---|---|---|---|
| Why Do Humans Forget Their Dreams? | 27/07 | 12d | **277** |
| Why Do You Keep Waking Up at 3AM? | 26/07 | 13d | **380** |
| Where Are You When You Dream? | 03/07 | 36d | **567** |

3 trong 4 bài ít view nhất kênh là bài giấc mơ. Mạnh hơn nữa: **3/4 bài cụm này đăng trong kỷ nguyên TỐT (25–27/07)**, tức là đã được hưởng văn phong mới + tuổi trẻ (thứ làm view/ngày phồng lên) — mà vẫn nằm đáy. Không đổ được cho thời gian.
Trung vị view thô: động vật **9.484** · phần còn lại **3.188** · giấc mơ **474**.
⚠️ Sửa số: họ ghi "chênh 30 lần" — đó là số của view/ngày. Theo **view thô** chênh là **20 lần**. Và n=4.

**2. Từ khoá title.** Đếm lại khớp tuyệt đối:
- 7/31 title có `animal/animals/cat/insect` → **4 CAO / 3 GIỮA / 0 THẤP**
- 4/31 title có `dream/sleep/waking` → **0 CAO / 1 GIỮA / 3 THẤP**

**3. `genuinely` — chỉ số văn phong DUY NHẤT sống sót.**
Spearman rho = **−0,448** (họ ghi −0,52, phồng), Mann-Whitney CAO vs THẤP **p = 0,010**. Quan trọng hơn: tôi tách trong **riêng kỷ nguyên sớm** — nửa trên 8 lần/bài, nửa dưới 16,5 lần/bài. Hiệu ứng tồn tại độc lập với ngày đăng. Đây là chỗ họ làm đúng và tôi xác nhận.
Kèm cảnh báo của chính họ, đúng: ở kỷ nguyên muộn còn 0 vs 1 → **từ đệm hết tác dụng phân biệt sau khi kênh đã dọn sạch.**

**4. Bốn con số ÂM, đúng tuyệt đối, đã grep lại toàn bộ 31 file:**
- **0/31** bài xin sub / like / comment / bell (0 hit)
- **0/31** bài mồi video kế / playlist
- **0/31** bài kết bằng lời chào
- **0** dấu `!` trên toàn kênh

**5. Quảng cáo khoá học — mốc bật sạch, khớp 100%.** 16/31 bài. **0/15 trước 14/07 · 16/16 từ 14/07.** Vị trí trung vị ~45% bài (họ ghi 46,7%, tôi đo 45,3% — sai số vặt). Phân bố nhóm 6 CAO / 8 GIỮA / 2 THẤP khớp chính xác.

**6. Khuôn độ dài cứng.** 3.170–3.885 từ, 20:05–28:15, trung vị ~3.393 từ. rho(số từ, view/ngày) = +0,13, p=0,35 → không liên quan. Đúng như họ nói.

**7. Nhịp đăng.** Khoảng cách khớp từng con số (19×1 ngày, 6×2, 1×0, 1×4, 2×5, 1×6). Và họ kết luận đúng: nhịp không dự báo gì.

---

## NẾT CỦA KÊNH — không phải bí quyết

- **Không nêu tên nhà nghiên cứu.** 8/31 bài, **4 CAO / 0 GIỮA / 4 THẤP** — chia đôi hoàn hảo. Đếm lại khớp từng file.
- **Re-hook `here's the...`** — có ở cả hai đầu bảng.
- **Hài khô cuối câu · hedge dày · lời hứa chiều sâu · bộ xương chương · `Start with X` · không cliffhanger · kết bằng câu cách ngôn** — tất cả đều hai nhóm.
- **`Picture/Imagine`** 4/31 (3 CAO / 1 THẤP) — n=4, vô nghĩa thống kê.
- **Không có người dẫn, không tự giễu** — đúng về bản chất, sai về con số (xem dưới).

---

## ĐÃ GẠCH

### ⛔ GẠCH 1 — Hai phát hiện KHUÔN HOOK: cả hai là ảo ảnh ngày đăng

Đây là lỗi nặng nhất. Họ tự viết trong `gioi_han` rằng nhiễu thời gian là "giới hạn lớn nhất", rồi không áp nó vào chính hai phát hiện hook.

```
hook "PHỦ ĐỊNH LẬT NGƯỢC" (6 bài) : 19/07 → 05/08
hook "SỐ LIỆU / DI CHỈ"   (6 bài) : 28/06 → 18/07
                          → HAI CỬA SỔ NGÀY TÁCH RỜI HOÀN TOÀN, 0 ngày chồng lấn
```

Không phải "khuôn phủ định tránh được nhóm THẤP" — mà là **kênh chỉ bắt đầu dùng khuôn phủ định sau khi đổi văn phong**, và bài muộn thì view/ngày cao hơn. Kiểm trong riêng kỷ nguyên muộn:

| | n | view **thô** trung vị |
|---|---|---|
| muộn + hook phủ định | 6 | **4.126** |
| muộn + hook khác | 10 | **5.304** |

Hook phủ định **thấp hơn**. Lợi thế view/ngày của nó chỉ vì 4/6 bài đăng 01–05/08 (tuổi 3–8 ngày).
Chiều ngược lại y hệt: trong riêng kỷ nguyên sớm, hook số-liệu 79 view/ngày vs hook khác 93 — như nhau.
**Cả hai nhãn `CHỈ_NHÓM_CAO` và `CHỈ_NHÓM_THẤP` đều bị gạch.**

### ⛔ GẠCH 2 — "Nhóm CAO viết câu ngắn hơn" (họ gọi là "phân biệt mạnh thứ hai")

Con số của họ tái lập đúng (16,4 / 19,2 / 20,3) nhưng vô nghĩa:
- Mann-Whitney CAO vs THẤP **p = 0,226** — không có ý nghĩa
- Tách trong từng kỷ nguyên, hiệu ứng **biến mất sạch**:

```
SỚM  (n=15): nửa trên 25,47 từ/câu  |  nửa dưới 26,67   → không chênh
MUỘN (n=16): nửa trên 14,33 từ/câu  |  nửa dưới 15,51   → không chênh
```

Kênh rút ngắn câu vào 14/07. Đó là toàn bộ câu chuyện. **Độ dài câu không phân biệt thắng/chìm ở bất kỳ đâu.**

### ⛔ GẠCH 3 — "Nhóm chìm xưng `you` nhiều gấp 9 lần" — sai số, và không có thật

Ba lỗi chồng nhau:
1. **Trung vị CAO là 1,0 chứ không phải 0,5** → tỉ lệ là **4,5 lần**, không phải 9.
2. **"Bài chìm nhất có 16 lần" — thực tế 8.** Tôi đếm tay 130 từ đầu của `Where Are You When You Dream`: 1 `your` + 7 trong câu dài = **8**. Phồng đúng gấp đôi.
3. **p = 0,364.** Và hai đuôi giống hệt nhau: **4/10 bài CAO có ≥6 lần `you`** (Remember a Baby 12, Wild Weak 8, Blood Types 7, Smoking 6) — **4/10 bài THẤP cũng có ≥6**. Họ trích 3 bài THẤP nặng `you` và giấu 4 bài CAO cũng nặng `you`.

Đặc biệt: `Do Wild Animals See Humans As Weak` (CAO, hạng 3 kênh) mở bằng **8 lần `you`** — họ có trích file này ở mục khác nhưng không đưa vào mục `you`.

### ⛔ GẠCH 4 — Cú lật `That's not X` (nhãn CHỈ_NHÓM_CAO)

Đếm lại: họ khai **CAO 7/10 · THẤP 2/10**. Thực tế **CAO 5/10 · GIỮA 4/11 · THẤP 3/10**. Và tách theo kỷ nguyên thì đảo chiều:
```
SỚM : nửa trên 1,0 cú/bài | nửa dưới 1,5  ← NGƯỢC
MUỘN: nửa trên 2,0        | nửa dưới 1,5  ← xuôi, yếu
```
Không nhất quán → gạch.

### ⛔ GẠCH 5 — Mẫu số view/ngày sai 2 ngày trên toàn bảng

View được cào **06/08/2026** (mtime toàn bộ file). Họ chia cho tuổi tính đến **08/08**. Tử số và mẫu số lệch nhau 2 ngày.
Hậu quả với bài mới: `Cross Oceans` sai **3,00×** (1121 → họ ghi 374), `Dumb Skill` sai **2,00×**, `Missing Years` sai 1,50×.
**4/31 bài đổi nhóm** khi sửa: Dumb Skill và Cross Oceans thực ra thuộc CAO; Smoking và Remember-a-Baby rơi xuống GIỮA.
Kèm theo, phép kiểm chéo họ tự hào ("top-10 view thô trùng 9/10") cũng là sản phẩm của mẫu số sai — sửa lại chỉ còn **7/10**.

### ⛔ GẠCH 6 — "view/ngày nửa sau tăng 5,1 lần"

View **thô** trung vị chỉ tăng **1,66 lần** (3.073 → 5.102). Con số 5,1× là do bài muộn trẻ hơn (tuổi trung vị 12,5 ngày vs 39 ngày). Kênh **có** tiến bộ thật (view thô cao hơn dù ít thời gian hơn) nhưng **không phải 5 lần**.

### ⛔ GẠCH 7 — Các claim "phân bố sạch" bị vỡ vì sót file

| họ khai | thực tế |
|---|---|
| `Let's be honest` **2/31, cả 2 đều chìm** | **3/31** — bài thứ ba là **Blood Types (CAO, 2.174/ngày)**: *"Let's be honest about one more thing because the blood type story doesn't end..."* |
| `next time you/someone` **2/31, sạch 2/2 CAO** | **3/31** — bài thứ ba là **Treat Disease (THẤP)**: *"Do it again next time someone has the same problem."* (họ giới hạn ở 180 từ cuối nhưng không ghi rõ) |
| **6 câu chứa `I`** | **7 câu**, và quy sai file: **không có `I` nào ở Handle Death hay Insects** như họ ghi |
| `series` xuất hiện **1 lần duy nhất** | có ở **≥2 file** (thêm Marry So Young) |

### ⛔ GẠCH 8 — Các con số đếm không tái lập được

- **`here's the/where`: họ ghi 52 lần / 18 bài. Đếm lại 34 lần / 16 bài** (bản hẹp) hoặc 44/17 (bản rộng). *(Mật độ theo nhóm 0,31 / 0,00 / 0,14 thì lại khớp — nhưng theo trung bình thì CAO 0,39 ≈ THẤP 0,37, tức hướng "CAO dùng dày hơn" chỉ đứng được ở trung vị.)*
- **167 câu mở chương / 102 có `because` (61%)**: không tái lập được. Khuôn hẹp cho 91/50 (55%), khuôn rộng cho 212/108 (51%). Họ không định nghĩa "câu mở chương" nên con số này không kiểm được.
- **rho `considerably` = −0,49**: thực tế **−0,187**, p = 0,473. Sai nặng nhất trong các rho.
- rho `genuinely` −0,52 → **−0,448**; rho độ dài câu −0,25 → −0,245 ✓; rho câu ≥40 từ −0,32 → −0,307 ✓.

### ⚠️ Hai câu trích bị sửa chữ (nhẹ, không phải bịa)
- `"...making decisions without them."` — nguyên văn là `without hem` (lỗi ASR). Họ **âm thầm sửa**, trong khi chỗ khác lại giữ nguyên lỗi ASR (`e thermal`, `next o`). Không nhất quán.
- `"Now, let's talk about the hippocampus..."` — nguyên văn không có dấu phẩy sau `Now`.

---

## KHO CÂU NGUYÊN VĂN — đã xác minh từng chữ

**HOOK — mở bằng phủ định lật ngược** *(dùng được như thủ pháp; nhưng KHÔNG có bằng chứng nó kéo view — xem GẠCH 1)*
```
For most of human history, the bathroom was not a room.
It was a direction.

Humans did not stop eating animal organs because organs became disgusting.
Organs became disgusting after many people stopped needing to recognize them as food.

The first humans to cross an ocean left no ship behind.

The cat currently sitting on your laptop did not ask to be domesticated.

The most dangerous thing ancient humans could do was walk.
Not sprint, not fight, not throw a spear with force or accuracy that took years to develop.
Walk.
```

**HOOK — cảnh dựng 2 câu** *(2 bài top kênh)*
```
Picture the Sahara desert.
Now, picture it green.

There is a gap in the human story that most people have never heard of.
Not a small gap.
Not the kind of gap that gets filled in when someone finds a new fossil or excavates a new site.

You eat chicken eggs without a second thought.
Every morning in kitchens across the world, people crack open eggs from one specific bird and call it breakfast.
```

**RE-HOOK — đặt ở 3–5% bài, ngay trước fact sốc**
```
But here is the question that almost nobody asks.   → Why chicken eggs?
And here's the unsettling part.                     → This isn't a one-off story.
But here is the uncomfortable part.
And here is the beautiful, absurd punchline.
Here's the mechanism.
And here is the part that makes the question interesting.
```

**CHUYỂN CHƯƠNG — bán lại lý do ở lại**
```
Now, let's talk about the nutritional comparison, because this is where the picture gets
most interesting and where the dominance of chicken eggs looks most like an accident of
history rather than a nutritional verdict.

Now, let us talk about fire because fire is the technology that most clearly connects the
behaviorally simple-looking early record to the behaviorally complex later record.
```
**Mồi độc quyền** *(khuôn dùng lại gần như nguyên văn 9 lần)*
```
Now, let's talk about something that almost never appears in discussions of X, but that ...
Now, here's a layer of this that doesn't get talked about nearly enough.
```
**Đóng chương cụt rồi bật thẳng** *(0/167 lần dùng câu treo lửng)*
```
The cats were selecting themselves.          → Now, let's talk about...
None of it survived.                         → Now, let us talk about fire because...
It was preparing for pathogens.              → Here's the mechanism.
Their effects are not.                       → Now, let's address a question that...
```

**CÂU KẾT — cặp câu đối, câu sau ngắn hơn và lật câu trước**
```
One human looks fragile.
Humanity does not.

The humans of the missing years were not waiting to become us.
They were us.

We remember the islands they reached.
The ocean kept the boats.

We did not understand the organism.
We understood the invitation.
Something sweet had changed in the dark.

The organ never changed.
The status did.

Keep human waste away from humans.
A simple rule.

That is not proof that ancient people feared the sea less than we do.
It may be proof that they feared it correctly.

That is what blood types actually are.
And now, you know.
```

**HÀI KHÔ — rơi mệnh đề đùa cuối câu nghiêm túc**
```
...marshes, waterfowl, cold air, and absolutely zero Netflix.
...why anyone looked at an ocean full of currents, storms, sharks, thirst, and absolutely
   no refund policy, then decided the other side was worth investigating.
The parasites were also impressed.
...suddenly convinced that everyone deserves to hear the same hunting story twice.
They discovered that fruit had begun making decisions without them.
```

---

## CÒN THIẾU

**1. Không có retention / CTR / thumbnail — nên không chiều nào giải thích được cú nổ.** Eggs = 368.082 view = **40,7% toàn bộ view của kênh** (tổng 904.637). Top-2 = 58%. Top-3 = 71%. Trung vị view thô cả kênh chỉ **3.628**. Đây là hình dạng **TRÚNG SỐ**, giống hệt Simply A Stickman trong kho. 30 bài cùng khuôn, cùng giọng, cùng độ dài không nổ — nghĩa là biến quyết định **không nằm trong lời đọc**, mà bản bóc này chỉ có lời đọc.

**2. Nhiễu thời gian không gỡ được bằng dữ liệu này.** Mọi thứ đổi cùng lúc vào 14/07: từ đệm, độ dài câu, khuôn hook, và quảng cáo khoá học. Bốn biến đổi đồng thời, n=31 → **không tách được biến nào có công.** Chỉ `genuinely` sống sót vì nó còn phân biệt được **bên trong** kỷ nguyên sớm.

**3. view/ngày không dùng được cho 6 bài dưới 7 ngày tuổi.** `Cross Oceans` có **1.121 view thô** mà được xếp nhóm CAO vì mới 1 ngày. Mọi phát hiện có mặt 3 bài 03–05/08 trong nhóm CAO đều mong manh.

**4. Vị trí "câu hỏi lõi" — không kiểm được.** Họ khai CAO từ thứ 115 / GIỮA 138 / THẤP 202 với 26/31 bài tìm thấy. Bộ dò của tôi chỉ tìm được 17/31, cho ra kết quả khác hẳn (CAO 108 nhưng n=3). Họ không mô tả cách dò → **không xác nhận cũng không bác được.** Đừng dùng.

**5. Cỡ mẫu.** Sau khi gạch, những gì còn lại đứng trên n=4 (cụm giấc mơ), n=7 (title động vật), n=31 (`genuinely`). Chỉ `genuinely` và cụm đề tài đủ sức chịu lực. **Đừng đúc luật từ những phát hiện n≤7 trong bản này.**

---

### Nếu chỉ mang đi 3 dòng
1. **Đề tài quyết định, không phải văn phong.** Cụm động vật ăn; cụm giấc mơ/"về BẠN" chết cả 3 lần, chết cả khi được đăng trong kỷ nguyên tốt. Khớp với kết luận lane-"về BẠN"-không-nổ đã có trong kho.
2. **Bỏ hết luật hook và luật độ dài câu rút ra từ bản này** — chúng chỉ đo được ngày kênh đổi văn phong.
3. **Giữ đúng một luật văn phong: cắt từ đệm** (`genuinely`, `considerably`). Đây là thứ duy nhất sống sót kiểm nhiễu thời gian.

File script kiểm chứng: `/private/tmp/claude-501/-Users-admin-Desktop/5c5ffe04-128f-46b0-bf3b-27c0f64ae354/scratchpad/` (`q.py` đối chiếu 225 trích dẫn, `s3.py`–`s8.py` đếm lại số liệu và kiểm nhiễu).
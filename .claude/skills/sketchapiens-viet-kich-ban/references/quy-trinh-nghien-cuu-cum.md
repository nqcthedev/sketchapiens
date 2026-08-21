# QUY TRÌNH NGHIÊN CỨU CỤM — chạy lại cho MỌI video mới

> # ⛔ FILE THAM CHIẾU — CHƯA ĐƯỢC SOÁT CHO TỚI 09/08/2026, VÀ NÓ CHỨA LUẬT ĐÃ CHẾT
>
> Thư mục `references/` bị **bỏ sót** trong đợt soát toàn tầng kịch bản *(7 người soát chỉ
> đọc `SKILL.md`, không mở thư mục này)*. Nó vẫn được skill nạp vào lúc viết.
>
> **Khi file này nói ngược `kho/1_luat/RUBRIC_KichBan.md` → nghe RUBRIC.**
> **Khi nó nói ngược PHẦN 13-14 của `SKILL.md` → nghe PHẦN 13-14.**
>
> Những thứ trong đây **đã bị đo lại và bác** *(16-18 kênh · 488 bản ghi · đọc trọn 11 kịch bản)*:
> `lane "về BẠN"` **0 cú nổ/4 tháng** · `câu tự giễu trong hook` **0 ca thắng** ·
> `cliffhanger / báo trước phần hay ở cuối` **0 tuyệt đối ở 14/16 kênh** ·
> `persona người dẫn` **0 ca thắng, BrightPsycho 0/96** · `I ≈ 0` **gỡ 07/08** ·
> mọi **con số nhịp** *(Zenn Night 7,83M có 0 câu đùa)* · `mật độ mỏ neo` ·
> `câu hỏi lõi trước giây 31` · `callback + bookend làm mục chấm`.
>
> ## 🔴 Và mọi câu tiếng Anh trong đây là câu của ĐỐI THỦ — đọc để biết register, **chép là clone**.


*Đúc từ đợt nghiên cứu V16, 26-27/07/2026. Đây là **cách làm**, không phải kết quả một lần.*

Mỗi video mới trong ngách này đều bắt đầu lại từ bước 1. Chạy đủ 6 bước rồi mới được viết.
Toàn bộ dùng công cụ **nexlev MCP** + **WebSearch**.

---

## NGUYÊN TẮC NỀN — đọc trước

**Bán quả người ta đang mua.** Số người bán KHÔNG dự báo gì.

- Cụm mùa đông có clone dày đặc, vẫn nổ **11 lần trong 2 tháng**. Kênh 1.07K sub vào sau cùng vẫn ăn 302K trong 3 ngày.
- ⛔ **LUẬT CŨ "thấy 2+ clone mới thì đổi title" ĐÃ BỊ BÁC BỎ.** Nó khiến ta bỏ đúng những cụm đang chảy tiền.
- ✅ **Thứ dự báo được: cụm đã có ≥2 cú nổ.** Cụm 0-1 cú nổ = rủi ro cao, dù trông trống trải.
  *Bằng chứng: "khi có người chết" 72 view · "em bé + mùa đông" 37-116 view · "bản đồ đầu tiên" 156 view — đều là khe trống, đều chết.*

---

## BƯỚC 1 — TÌM CỤM CÓ CẦU (nexlev, ~5 phút)

```
mcp__nexlev__faceless_outliers_videos
  query: "ancient humans"        ← đổi theo cụm muốn dò
  minUploadDate: <3 tháng trước>
  minViews: 80000
  videoType: "long"
  sortBy: "videoViews"
```

Chạy thêm với `query`: `prehistoric` · `early humans` · `stone age` · `cavemen` để bắt cụm không có chữ "ancient humans" trong title.

**Đọc kết quả theo CỤM, không theo video lẻ.** Gom các video cùng chủ đề lại, đếm số cú nổ.
Đối chiếu `BANDO_CumChuDe_CoCau_*.md` trong project — có sẵn 7 cụm đã xếp hạng.

⚠️ **Bẫy đã gặp:** `search_videos` (index) khớp rất lỏng rồi sắp theo view → trả về toàn video triệu view **không liên quan**. Dùng `faceless_outliers_videos` hoặc `youtube_search` thay thế.

⚠️ **Bẫy thiên vị:** truy vấn theo từ khoá sẽ chỉ trả về title chứa từ đó. Muốn kết luận "lane X không nổ" thì phải **kiểm chéo bằng một từ trung tính** (ví dụ `evolution`) để chắc không phải do lọc.

---

## BƯỚC 2 — VERIFY LIVE (YouTube search, ~3 phút)

```
mcp__nexlev__youtube_search
  query: <đúng góc định làm>
  type: "video"
  sort_by: "views"
  upload_date: "month"
```

Việc cần làm ở bước này **KHÔNG phải** đếm clone. Là:
1. Xác nhận cụm **vẫn đang chảy** — có cú nổ nào trong 30-60 ngày gần nhất không?
2. Xem **góc nào đã bị chiếm chính diện** bởi một ông lớn.

🔴 **BẪY LỚN NHẤT — "ĐỘC CHIẾM CHÍNH DIỆN".**
Zenn ôm 7.8M ở góc "ban đêm". **Mack** — kênh 63.6K sub từng ăn 1.68M — vào sau ở đúng góc đó, chỉ được **23K**.
→ Cụm nhiều cú nổ chia cho **nhiều kênh khác nhau** = tốt. Cụm có **một ông ôm hết** = tránh cửa chính.

---

## BƯỚC 3 — KÉO TRANSCRIPT VỀ ĂN (bắt buộc, không được bỏ)

```
mcp__nexlev__get_bulk_video_transcripts
  videoIds: [3 video một lượt]     ← quá 3 là vượt giới hạn token
```

Kết quả sẽ bị lưu ra file. Xử thành bản đọc được:

```python
import json, os
d = json.load(open(SRC, encoding='utf-8'))
for r in d['transcripts']['results']:
    segs = r['data']['transcript']
    lines = [f"[{int(s['startMs'])//1000//60}:{int(s['startMs'])//1000%60:02d}] {s.get('text','').strip()}" for s in segs]
    open(f"{TEN}.txt", 'w', encoding='utf-8').write('\n'.join(lines))
    w = sum(len(s.get('text','').split()) for s in segs)
    sec = int(segs[-1]['endMs'])//1000
    print(f"{TEN}: {w} từ · {sec//60}:{sec%60:02d} · {round(w/(sec/60))} wpm")
```

**ĐỌC TRỌN, không đọc lướt.** Đọc lướt sẽ bỏ mất câu kết — mà câu kết là chỗ phân biệt 7.8M với 311K.
Ưu tiên đọc: **2-3 quả to nhất cụm** + **1 quả nhỏ nhất trong nhóm nổ** (để thấy sàn) + **1 quả chết cùng đề tài** (để thấy vì sao chết).

### Đọc để tìm 4 thứ
1. **Miếng ngon** của từng quả — miếng nào người ta thực sự ăn?
2. **Câu kết** — nguyên văn. Mở vết thương hay băng lại?
3. **Bảng mỏ neo dùng chung** — cái nào lặp ở ≥2 quả = **đã cháy**, không được dựa vào.
4. **Số từ + thời lượng** — ghi lại để biết ô này chạy ở nhịp nào.
   ⛔ ~~đối chiếu luật ~1.500 từ~~ — **luật đó đã chết**: Mack 3.206 từ → 1,69M · Stickly 3.165 từ → 2,08M. Độ dài là **lựa chọn định vị**, và mục *"ĐỘ DÀI CÓ THỂ KHÁC THEO Ô"* cuối file này đã tự ngờ đúng chuyện đó.

---

## BƯỚC 4 — LẬP BẢNG MỎ NEO CHÁY

Kẻ bảng: hàng = mỏ neo, cột = từng winner, đánh dấu ai dùng.
**Mỏ neo xuất hiện ở ≥2 quả = khán giả đã ăn rồi = hết ngon.**

*Ví dụ cụm sinh tồn: ngủ-hai-giấc/Wehr-1992 và Wiessner-80%/81% xuất hiện ở **4/9 quả, gồm cả Zenn 7.8M**.*

---

## BƯỚC 5 — ĐÀO MIẾNG NGON RIÊNG (WebSearch)

Đây là bước **quyết định thắng thua**, và là bước duy nhất không copy được từ đối thủ.

Tìm mỏ neo thoả **cả 6**:
1. Ngoài bảng cháy ở bước 4
2. Lật ngược điều người xem tin về chính họ
3. Có con số
4. Kể lại được trong 2 câu
5. Có thí nghiệm/bằng chứng đóng đinh
6. **Nối được về cơ thể hoặc thói quen người xem HÔM NAY** ← lợi thế riêng của kênh

**Mẹo đào:** tìm phía **sinh lý học / di truyền / thí nghiệm trên người hiện đại**, đừng chỉ tìm khảo cổ. Khảo cổ là chỗ mọi clone đã đào cạn; sinh lý học là chỗ nối được về người xem.

*Ví dụ V16: bỏ khảo cổ, đào sang **người Yaghan (BMR 160%, gen HOXC4)** → nối thẳng sang **mỡ nâu ở người hiện đại (PET-CT: 23/24 người sáng lên khi bị làm lạnh)**. Không winner nào chạm tới.*

⚠️ **Kiểm cả mặt hạn chế.** Một ứng viên trông rất ngon (vân răng ghi lại từng mùa đông) đã bị **loại** vì tổng quan phương pháp nói thẳng là kỹ thuật còn "hạn chế nghiêm trọng". Mỏ neo lung lay thì không đóng đinh được.

---

## BƯỚC 6 — CHỐT TITLE (sau khi có miếng ngon, KHÔNG trước)

Title phải **trỏ vào miếng ngon**, vì cả bài là đường dẫn tới nó.

**Cách hàn title** — quan sát từ Evo Explainer (302K/3 ngày):
> Lấy **tính từ cực đoan** của winner A + **khung câu** của winner B + **biến thể thời gian/nơi chốn**.
> *The **Darkest** (từ winner 487K) + **Survival Methods Used By Ancient Humans** (từ winner 1.87M) + **During Winters** = 302K trong 3 ngày.*

⚠️ **Đừng đuổi theo điểm tuyệt đối.** Hai title triệu-view của ngách chỉ đạt 2/5 và 3/5 trên rubric 5-công-tắc cũ.

> ⛔ **Bỏ bước "kiểm 5 công tắc" trong `CongThuc_Title_TrieuView.md`** — file đó đã chết (29/07/2026): nó nhắm mọi title vào lane "về BẠN" (verify: 0 cú nổ / 4 tháng).

## 🔴 BƯỚC BẮT BUỘC THAY THẾ — ĐẾM BẦY CLONE

Trước khi chốt bất kỳ title nào, chạy `mcp__nexlev__youtube_search` chính title đó:

1. **Đếm số kênh đã làm cùng title.** Ngách này gần như title nào cũng có ~20 clone trong 1-2 tháng.
2. **Xem ĐỈNH BẦY** (quả cao nhất trong đám clone).
   - Đỉnh bầy **dưới 10K** → **BỎ**, không cần chấm gì thêm.
   - Đỉnh bầy trên 50K → cầu có thật, vào được, nhưng phải khác góc với quả thắng.

**Bằng chứng** (`kho/3_bangchung/NGHIENCUU_CloneSwarm_2026-07-29.md`, 80 video):

| Lane | Clone | Đỉnh bầy |
|---|---|---|
| "…When Someone Died?" | 20 | 1.129 |
| "…Someone Was Exiled?" | 20 | 1.150 |
| "Woke Up at 3AM" *(clone đúng bí mật của quả 7,81 triệu)* | 20 | **337** |
| "…Twins" | 20 | **59.630** ✅ |

⚠️ **Title là bộ LỌC, không phải động cơ.** Nó loại chắc chắn thất bại; nó không tạo ra thành công. 20 kênh cùng title cùng tháng → 1 quả 59K, 19 quả dưới 6K. Biến quyết định là **thumbnail** (skill `sketchapiens-thumbnail` *(gộp 09/08)*).

---

## GHI RA FILE (theo lệ project)

- `NGHIENCUU_*.md` — kết quả dò cụm + bằng chứng
- `BANDO_CumChuDe_*.md` — bản đồ cụm, cập nhật khi có dữ liệu mới
- `VERIFY_Anchors_V**_*.md` — mỏ neo đã kiểm + link nguồn + **giới hạn của từng mỏ neo**
- Phát hiện nào **áp cho mọi video** → thêm vào `luat-chung-ngach.md`, KHÔNG để trong file cụm

---

## ⏱ TỔNG THỜI GIAN
Bước 1-2 khoảng 10 phút · bước 3-4 khoảng 30-40 phút (phần nặng nhất, phải đọc thật) · bước 5-6 khoảng 20 phút.
**Không được cắt bước 3.** Đó là bước duy nhất cho ra miếng ngon và bảng mỏ neo cháy.

---
---

# BỔ SUNG 27/07/2026 — 5 GÓC QUÉT SONG SONG, 4 CHẾT 1 SỐNG

Thả 5 agent quét song song 5 góc "khe trống" tự nghĩ ra. Kết quả:

| Góc | Cú nổ ≥80K | Số kênh đã thử /30-60 ngày | **Trần thật của góc** | Phán quyết |
|---|---|---|---|---|
| Gãy xương / chấn thương | 0 | ~30 | **3.517** | TRÁNH |
| Sinh đôi | 0 | ~20 | 59.629 | TRÁNH |
| Chọn thủ lĩnh | 0 | ~15 | **1.408** | TRÁNH |
| Sinh nở / phụ nữ | 0 | ~30 | 10.247 | TRÁNH |
| **Đường / mật ong** | **1 (82.5K)** | ~19 | 82.570 *(đang leo)* | **NÊN LÀM** |

---

## ⛔ LUẬT MỚI 1 — CẦU CỦA CỤM **KHÔNG** LAN SANG GÓC HẸP

Cách làm sai mà chính file này từng gợi ý: *"lấy cụm có cầu rồi chọn góc hẹp chưa ai chiếm."* **Bác bỏ.**

Bằng chứng — cụm sinh sản có **9 cú nổ ≥80K**, đến từ kênh **550 sub tới 12.8K sub**:
> 646K *keeping children alive* · 407K *someone got pregnant* · 211K *had a baby* · 142K *prevent pregnancy* · 116K *babies wouldn't stop crying*

Nhưng hai góc hẹp trong **cùng cụm, cùng cỡ kênh**:
> sinh đôi → 20 lần thử, trần **59K** · sinh nở → 30 lần thử, trần **10K**

**Vì sao:** góc thắng đều là thứ **ai cũng trải qua**. Sinh đôi là ca hiếm 1/80. "Chọn thủ lĩnh" trừu tượng, không chạm cơ thể. "Gãy xương" hiếm — trong khi **ốm** thì ai cũng ốm, và *"How Did Ancient Humans Survive Sickness?"* ăn **621K**.

> ### LUẬT: đừng chẻ cụm mỏng ra. Lấy đúng câu hỏi RỘNG và HIỂN NHIÊN nhất của cụm.
> Thứ thắng là **câu hỏi phổ quát nhất**, không phải câu hỏi thông minh nhất.

---

## ⛔ LUẬT MỚI 2 — CHỦ NGỮ PHẢI LÀ "ANCIENT HUMANS", ĐỪNG THU HẸP

Không một cú nổ nào dùng chủ ngữ hẹp. Góc *"How Did Ancient **Women** Survive Childbirth?"* thu hẹp tệp ngay từ title → trần 10K.

Khuôn thắng luôn giữ chủ ngữ rộng:
- *"What Did Ancient Humans Do When [tình huống]?"*
- *"How Did Ancient Humans Survive [mối đe doạ]?"*

---

## ⭐ LUẬT MỚI 3 — BẰNG CHỨNG PHỦ ĐỊNH MẠNH NHẤT: **KÊNH MẠNH LÀM GÓC ĐÓ VẪN FLOP**

Cách phân biệt "chưa ai thử" với "thử rồi thị trường từ chối":

| Kênh mạnh | Góc | Kết quả |
|---|---|---|
| **Stickly** (từng có video 2M) | *How Did Ancient Women Give Birth?* | **10.247** |
| **Mack** (64K sub, từng 1.68M) | *Why Didn't Ancient Humans Sleep Alone?* | **23K** |

→ Khi một kênh đã chứng minh năng lực mà vẫn flop ở góc đó, **đó là bằng chứng cầu không tồn tại**, không phải lỗi thực thi. Luôn tìm dấu hiệu này ở bước 2.

---

## ⭐ LUẬT MỚI 4 — ĐO **TRẦN CỦA GÓC**, KHÔNG PHẢI TRẦN CỦA CỤM

Bước 2 phải trả lời được câu: *"view cao nhất **mọi thời** của đúng góc này là bao nhiêu?"*
Nếu trần đó **dưới 80K sau khi đã có ≥15 kênh thử** → góc chết, bỏ. Cụm mẹ khoẻ đến mấy cũng không cứu được.

---

## 🎰 CỖ MÁY TITLE ĐÃ TÌM RA — CỤM "TIÊU THỤ"

> ## **When Did Ancient Humans (First) Start [động từ tiêu thụ] [chất quen thuộc hằng ngày]?**

Đã điền và đã nổ, **6 kênh khác nhau, từ 2.7K đến 171K sub**:

| Chất | Kênh | View |
|---|---|---|
| **Smoking** | Mack (64.3K) | **1.68M** |
| **Alcohol** | Ink Explainer (41.2K) | 753K |
| **Eat** (chung) | **Zenn (171K)** | 710K |
| **High / chất gây ảo giác** | WATIVY (2.71K) | 340K |
| **Salt** | ThinkMan (13K) | 190K |
| **Sugar** | ThinkMan (13K) | 82.5K *(mới, đang leo)* |

**Đặc điểm khiến nó chạy:** chất nào cũng là thứ **người xem tiêu thụ hằng ngày** → luôn có sẵn trục nối về đời người xem.
⚠️ *Đây là nghĩa ĐÚNG của "về BẠN": **title ngôi ba**, ruột có MỘT đoạn chạm người xem. Không phải lane "về BẠN" đã chết (cả bài hướng về người xem, 0 cú nổ/4 tháng).* Đúng luật mới 1.

**Ô còn trống cần quét trước khi dùng:** caffeine · gia vị/ớt · chất béo · thịt · nấu chín · lên men · sữa *(kênh mình đã làm V14)*.

⚠️ Sugar hiện có **19 kênh bom cùng tuần**, cao nhất trong đám clone chỉ **113 view** trong khi ThinkMan được 82.5K. Lại một lần nữa: **cùng quả, khác sạp, chênh 700 lần.** Zenn và Mack — hai kênh lớn nhất cụm — vẫn **chưa đụng góc đường**.

---

## 📊 ĐỢT QUÉT 2 — 5 Ô CỦA CỖ MÁY TITLE (27/07/2026)

| Ô | Trần thật của ô | Số kênh đã thử | Phán quyết |
|---|---|---|---|
| Caffeine / cà phê | **618** | ~20 | ❌ |
| Thịt | **2.841** | 30+ | ❌ |
| Gia vị / vị cay | **198** | 22 | ❌ |
| Chất béo / tuỷ xương | 13.759 | ~29 | ❌ |
| **Nấu chín** | **150.759** | ~45 | ✅ |

**Tổng cả hai đợt: 10 góc quét, 2 sống (đường · nấu chín).**

---

## 🔬 BỘ LỌC 3 TẦNG CHO CỖ MÁY "When Did Ancient Humans Start [X]?"

Ô phải qua **cả ba**, thiếu một là chết:

**1. CÓ NIÊN ĐẠI TIỀN SỬ THẬT**
Caffeine chết vì cà phê là **thế kỷ 15 (Yemen/Ethiopia)**, trà là đời Hán — **trung cổ, không phải tiền sử**. Tiền đề "ancient humans" gãy ở giây thứ 30. Hai mươi kênh thử, trần 618 view; cùng cỗ máy, thuốc lá (12.000 năm) ra 1.68M.
*Đối chiếu ô sống: thuốc lá 12.000 năm · rượu 9.000 TCN · muối, đường, chất gây ảo giác đều có mốc tiền sử.*

**2. PHỔ QUÁT VỚI NGƯỜI XEM HÔM NAY**
⛔ Bản "đúng tiền sử" của caffeine (khat, coca, betel, guarana) thì mất trục "về BẠN" — khán giả Âu-Mỹ không nhai betel hằng ngày.
> *(Dòng trên coi "mất trục về BẠN" là điểm trừ — **bác bỏ 10/08**: kênh làm ngách cổ đại ngôi ba. Bản "đúng tiền sử" nay là bản ĐÚNG, không phải bản yếu.)*
> **Nghịch lý phải né: universal thì không cổ đại, cổ đại thì không universal.**

**3. LÀ THỨ NGƯỜI TA BỊ **CUỐN**, KHÔNG PHẢI THỨ CHỈ **ĂN****
Đây là tầng lọc sắc nhất, rút từ đối chiếu:

| Bị cuốn *(nghiện · thèm · không cưỡng được)* | Chỉ là đồ ăn |
|---|---|
| thuốc lá **1.68M** · rượu **753K** · ảo giác **340K** | thịt **2.8K** |
| muối **190K** · đường **82.5K** | chất béo **13.7K** · gia vị **198** |

Khán giả cần cảm giác *"sao lại có thứ này trong thế giới cổ đại?"*. **"Ăn thịt" là điều họ đã mặc định** → không sinh cú click.

**Bằng chứng A/B nội bộ, đóng đinh tầng 3:**
- **Renn**: ô "sinh con" **211.000** · ô "ăn thịt" **383** — cùng kênh, cùng tháng, chênh **550 lần**
- **Ancient Human Files**: ô "nấu ăn" **94.360** · ô "thịt sống" **2.488** — cùng kênh, cùng tuần, chênh **38 lần**
- **Stickly** (41K sub, có video 2.0M, trung bình kênh 116K): ô "béo phì" ra **126.918 = 1,09x** → **thuật toán không thưởng, dù kênh đủ lực**

---

## 🕸️ PHÁT HIỆN CẤU TRÚC — MACK / STICKLY LÀ MỘT MẠNG LƯỚI, KHÔNG PHẢI KÊNH RỜI

**Stickly · Polo Animations · Explain In Paint** dùng **chung một link khoá học** (`ancient-minds-academy1.teachable.com`) và **đăng cùng một video 22-27 phút lên 3-4 kênh cùng lúc**.

**Hệ quả phải nhớ:** khi đếm "N cú nổ chia cho N kênh khác nhau = cụm khoẻ, không ai độc chiếm" — **phải kiểm xem mấy kênh đó có phải cùng một nhà không**. Nếu cùng nhà thì đó là **một** đối thủ đang chiếm nhiều chỗ, không phải nhiều đối thủ.

---

## ⚠️ ĐỘ DÀI CÓ THỂ KHÁC THEO Ô — chưa kết luận được

Ô nấu chín, ba video nổ đều **DÀI**: 150K/27:07 · 132K/24:33 · 94K/16:29.
Ngược hẳn luật ~1.500 từ rút từ cụm mùa đông (winner 1.489-1.598 từ / 8-9 phút).

**Chưa kết luận được** vì cả ba video dài đó **đều thuộc mạng lưới Stickly** — có thể là thói quen của một nhà, không phải đặc tính của ô. Khi làm ô nấu chín thì kiểm lại độ dài của các kênh NGOÀI mạng lưới đó trước khi chọn.

---

## 💰 QUOTA — nexlev giới hạn 20 lượt `faceless_outliers_videos` / 24h

Đợt quét 2 đã chạm trần. Khi thả nhiều agent song song, **mỗi agent tiêu quota chung**. Thả tối đa ~4-5 agent một đợt, hoặc bảo agent chỉ dùng `youtube_search` nếu chỉ cần verify live.

---

## ✅ HAI Ô SỐNG — 🔴 **CHƯA BAO GIỜ ĐƯỢC DÙNG** *(ghi chú 09/08/2026)*

> File này quét **10 góc**, chỉ **2 sống**, rồi đề xuất chúng cho V17 và V18.
> **V17 làm "mưa cả tuần", V18 làm "ngủ ngoài trời", V19 làm "đi vệ sinh đêm".**
> Cả ba đi hướng khác. Hai ô sống vẫn còn nguyên, chưa ai chiếm thêm tính tới 09/08.
>
> Đây không phải lỗi tài liệu — là **một quyết định chọn đề tài đã đi ngược nghiên cứu của
> chính mình**. Ghi lại để lần sau chọn đề tài thì mở file này ra trước.
>
> ⚠️ Và mục "BẢNG MỎ NEO CHÁY" ở bước 4 đã cảnh báo **Wehr 1992 + Wiessner** cháy ở **4/9
> quả** — trước khi V18 bắt đầu. V18 vẫn tra hai mỏ neo đó *(rồi cắt)*, V19 vẫn tiêu chúng
> ở M5. **Bảng cháy có, nhưng không ai tra bảng.**

| Ô | Trần | Ghi chú |
|---|---|---|
| **Đường / mật ong** | 82.5K *(ThinkMan, đang leo)* | Zenn và Mack **chưa đụng**. Bám khuôn "When Did Ancient Humans First Start Eating…" như bản muối 190K |
| **Nấu chín** | 150K | Kênh **976 sub** vẫn ăn 132K → không có rào cản kênh lớn. **Mỏ neo đã cháy:** Wrangham · Qesem cave · expensive tissue hypothesis · Homo erectus fire. Phải vào bằng góc khác |

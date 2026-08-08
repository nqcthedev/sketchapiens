# NGỮ PHÁP HÌNH — soi 12 video / 6 kênh, cặp THẮNG ↔ CHÌM trong cùng kênh

*Đo 08/08/2026. Tải video thật bằng `yt-dlp` 480p, trích khung bằng `ffmpeg`, xem tận mắt.
Ảnh lưới: `kho/3_bangchung/NGUPHAP_HINH_6Kenh_2026-08-08/`*

**Thiết kế:** mỗi kênh lấy **một quả thắng và một quả chìm**, độ dài gần bằng nhau. So **bên trong
từng kênh** để khỏi dính bẫy cỡ kênh *(bài học ExtinctZoo: trung vị đo cỡ kênh, không đo chất lượng)*.

| kênh | quả THẮNG | quả CHÌM | chênh |
|---|---|---|---|
| Mack | 1.694.495 · 21:54 | 6.094 · 20:48 | 180× |
| Zenn | 7.831.687 · 8:32 | 13.394 · 8:07 | 210× |
| Stickly | 2.078.350 · 18:27 | 4.183 · 19:48 | 555× |
| Before Civilization | 490.973 · 7:48 | 1.458 · 8:37 | 404× |
| Neon Rush | 159.715 · 26:26 | 3.538 · 33:15 | 42× |
| Ink Explainer | 1.101.989 · 11:36 | 6.972 · **4:09** | ⚠️ lệch độ dài, không dùng |

---

# 1. ⛔ "CHỮ TRÊN KHUNG" KHÔNG PHẢI ĐÒN BẨY CHUNG

Đếm tay số khung có chữ trên **12 khung mẫu** mỗi video:

| kênh | thắng | chìm | |
|---|---|---|---|
| Mack | **~92%** | ~33% | thắng cao hơn hẳn |
| Zenn | ~92% | ~67% | thắng cao hơn |
| Neon Rush | ~57% | ~47% | thắng cao hơn chút |
| **Stickly** | **~8%** | **~8%** | **không khác** |
| **Before Civilization** | **~8%** | **~8%** | **không khác** |

## → Chữ là NẾT CỦA KÊNH, không phải luật của ngách

**Stickly có quả 2,08 triệu với gần như không một chữ nào.** Before Civilization cũng vậy.
Mack và Zenn thì ngược lại, dùng chữ dày đặc. **Cả hai trường phái đều có quả triệu view.**

⚠️ Đây là **lần thứ hai** trong hai ngày một "tỉ lệ hình" bị bác theo đúng kiểu này *(lần trước:
tỉ lệ thẻ dạy học — xem `governance/RETIRED_RULES.md`)*. Mẫu chung: **đo một biến hình ảnh trên
vài kênh rồi tưởng đã tìm ra luật; đo rộng ra thì nó là lựa chọn phong cách.**

**Vị trí của kênh mình — cả hai đều hợp lệ, không có bằng chứng nói cái nào hơn:**

| | khung có chữ |
|---|---|
| V18 | **9%** *(22/224 prompt)* → cùng vùng Stickly / Before Civilization |
| V19 | **43%** *(84/191 prompt)* → cùng vùng Neon Rush / Zenn |

---

# 2. ✅ THỨ KHÁC BIỆT THẬT: SƠ ĐỒ CÓ NÓI ĐIỀU GÌ KHÔNG

Đây **không phải chuyện tỉ lệ**, nên nó không chết theo kiểu mục 1.

| | |
|---|---|
| **Đối thủ** | xương có nhãn `Butcher Cut Marks` ↔ `Stone Tool` *(BC)* · ba loại cây có tên `HENBANE / AROMATIC HERBS / VARIOUS AROMATICS` *(Mack)* · mặt cắt não kèm sóng điện *(Stickly)* · pin có người bên trong *(BC)* · trục `500 BC → 1960` *(Mack)* · biểu đồ **có trục %** và mốc `Short / Medium / Long / Very Long` *(Neon Rush)* |
| ⛔ **V18 của mình** | biểu đồ cột **không một chữ số nào** · cân thăng bằng **hai bên đều là `?`** · bong bóng thoại **rỗng** |

**Sơ đồ của họ nói một điều cụ thể. Sơ đồ của mình mang HÌNH DẠNG của sơ đồ nhưng rỗng ruột.**
Điều này đúng ở **cả kênh dùng nhiều chữ lẫn kênh không dùng chữ** — Stickly kể bằng sơ đồ
**không lời** *(thanh tiến trình có dấu ✗, biểu đồ sóng đỏ-xanh, hàng biểu tượng súng-bẫy-thuốc độc)*
mà vẫn có nội dung.

---

# 3. CHỮ CỦA V19 — 84 cụm, phân loại

| loại | tỉ lệ | ví dụ |
|---|---|---|
| ① có **con số** | 25% | `20 STEPS` · `8 HOURS` · `3-4x` · `9%` · `3 IN 4` |
| ② **thuật ngữ / tên riêng** | 41% | `MELATONIN` · `VASOPRESSIN` · `BLADDER` |
| ③ **chữ nhấn — nhại lại lời đọc** | **33%** | `NOTHING` · `EVERYTHING` · `WAIT` · `NOT IT` · `IT FAILS` · `MAKE LESS` |

Mang thông tin: **66%**. Một phần ba còn lại chỉ lặp lại thứ người xem vừa nghe.

Đối chiếu chữ trong quả thắng của Mack và Neon Rush: **gần như không có chữ nhấn nào** — mỗi cụm
là một dữ kiện *(`NOTHING FOUND.` là ngoại lệ, và nó là câu dẫn của cả một lập luận)*.

---

# 4. GIỚI HẠN

| | |
|---|---|
| **n = 10 video / 5 kênh** | mỗi kênh đúng **một** cặp. Chưa đủ để ra luật |
| **đếm bằng MẮT** | số % khung-có-chữ là đếm tay trên 12 khung mẫu, không phải OCR |
| **12 khung / video** | video 20-30 phút lấy 12 mẫu là thưa |
| **cặp thắng-chìm cách nhau về thời gian** | quả chìm thường cũ hơn hoặc mới hơn quả thắng; chưa khử |
| Ink Explainer | quả chìm chỉ **4:09** so với quả thắng 11:36 — loại khỏi phần đếm |

---

# 5. VIỆC RÚT RA — chỉ MỘT, và nó không phải con số

⛔ **Đừng đặt chỉ tiêu % khung có chữ.** Bằng chứng không đỡ.

✅ **Mỗi khung "dạy học" phải nói được MỘT điều cụ thể.** Kiểm bằng một câu hỏi:
*che lời đọc đi, khung này còn nói được gì không?*
- Biểu đồ cột không số → **không nói gì**. Thêm số hoặc bỏ.
- Cân hai bên đều `?` → **không nói gì**. Đặt hai thứ thật lên hai đĩa.
- Bong bóng thoại rỗng → **không nói gì**.

Luật này **không phụ thuộc trường phái** — Stickly làm được bằng sơ đồ không lời, Mack làm được
bằng nhãn chữ. Cách nào cũng được, miễn khung có nội dung.

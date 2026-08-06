# LỆNH CHO NOTEBOOKLM — PHẦN CHƯA LÀM
*29/07/2026. File này chỉ chứa việc CHƯA chạy. Phần đã chạy nằm ở `PROMPT_PACK_NotebookLM.md`.*

> **Luật xuyên suốt:** mọi lệnh đều mở bằng **"Take ONE video only… Ignore all other sources."**
> Bắt buộc — điểm yếu chí mạng của NotebookLM là **trộn các nguồn với nhau**. Nạp 49 transcript
> vào một notebook thì nó gộp thành một khối, rồi lấy câu của video này gán sang video kia.
> *(Đã bắt quả tang 2 lần: gán 7,8M của Zenn sang Stickly · gán 2 câu hedge của video Smoking sang Predators.)*

---

# LỆNH 1 — GIẢI PHẪU MỘT CHƯƠNG ⭐ ĐÁNG LÀM NHẤT

**Khe cần lấp:** mọi thứ đã bóc đều là hook / cú lật / kết. **Phút 2 đến phút 7 chưa ai chạm** — mà đó chính là chỗ người xem rơi. Đang có bản đồ vĩ mô (7 tầng) và vi mô (câu chữ), thiếu đúng tầng giữa: **một chương 400 từ được lắp theo trình tự nào**.

```
Take ONE video only: [TÊN VIDEO]. Ignore all other sources.

Find the chapter that begins at "[CÂU CHUYỂN]" and ends at the next
transition. Quote it in full, verbatim.

Then break that single chapter into its beats, in order, labelling each
beat with what job it does: transition / claim / hard anchor (name, place,
year) / concrete image / deadpan aside / rhetorical question / mini-twist /
hook into the next chapter.

Give me the beat sequence as an ordered list, with the verbatim sentence
for each beat and its word count.

Do not summarise. Do not pull sentences from any other video.
```

**Chạy 3 lần cho 3 chương KHÁC NHAU của CÙNG một video.**
Ba chương ra cùng trình tự beat → có khuôn lắp chương, thứ hiện chưa ai có.
Ba chương ra ba trình tự khác nhau → không có khuôn. Đó cũng là một kết luận.

**Câu chuyển gợi ý để điền vào ô `[CÂU CHUYỂN]`** *(lấy từ video Predators)*:
`"Now, let's talk about your smell."` · `"There's also the campfire effect"` · `"And then there's the group factor."`

---

# LỆNH 2 — ĐỌC KẺ THUA *(chữa lỗi sống sót)*

**Khe cần lấp:** 49 nguồn đều là video triệu view. **Chưa từng đọc một kịch bản THUA.** Mọi luật đang có đều có thể là lỗi sống sót — thấy winner làm X rồi kết luận X gây ra thắng, trong khi 19 quả thua cũng làm X.

```
Take ONE video only: [TÊN VIDEO]. Ignore all other sources.

Quote verbatim: the first 3 sentences, every chapter-transition sentence,
and the final 3 sentences.

Then count, in this video only: total words, exclamation marks,
occurrences of "you/your", occurrences of "we/our/us", occurrences of "I/me".

Report only what is in this one video. If something is absent, say "absent".
```

**Chạy cho từng video một, không gộp.**

## 5 URL DÁN THẲNG VÀO NOTEBOOKLM

Cùng đề tài, cùng khoảng thời gian, cùng phong cách người-que, cùng độ dài 6-9 phút. Trải từ **59.630 xuống 126 — gấp 473 lần**:

| View | Kênh | URL |
|---|---|---|
| **59.630** ⭐ | Inexplicably, but a fact | `https://www.youtube.com/watch?v=dj8sixbZNHs` |
| 6.286 | Pyrren | `https://www.youtube.com/watch?v=vbQ_r2yW2sA` |
| 5.529 | Senn | `https://www.youtube.com/watch?v=aWrL1fvwJb8` |
| 1.454 | Basically Primitive | `https://www.youtube.com/watch?v=jnUCBeWNvsk` |
| **126** | NightLore | `https://www.youtube.com/watch?v=3NzKvH9n1NI` |

*(Danh sách đầy đủ 18 video: `BAY_SinhDoi_DanhSach.md`)*

## ⚠️ ĐỌC TRƯỚC KHI TIN KẾT QUẢ

Tôi đã đo sẵn hai quả đầu bầy:

| | Winner 59.630 | Pyrren 6.286 |
|---|---|---|
| Like | 1.914 | 246 |
| **Tỉ lệ like** | **3,21%** | **3,91%** |
| Số tag | **0** | 20 *(có cả tên kênh "zenn")* |

**Tỉ lệ like ngang nhau — quả thua còn nhỉnh hơn.** Người đã xem thì thích như nhau.

→ Kịch bản gần như chắc chắn **KHÔNG** phải chỗ tạo ra chênh lệch 10 lần. Nếu Lệnh 2 chạy xong cũng cho thấy các kịch bản na ná nhau thì **đó không phải phép thử hỏng — đó chính là câu trả lời**, và nó xác nhận lần nữa: tiền nằm ở thumbnail.

**Đề phòng:** NotebookLM sẽ *cố* tìm ra khác biệt cho có. Nếu nó trả về danh sách khác biệt dài dòng, đối chiếu với tỉ lệ like trước khi tin.

---

# LỆNH 3 — KHUÔN MÔ TẢ VIDEO

**Khe cần lấp:** quả thắng bầy sinh đôi có mô tả rất công phu — 6 nguồn học thuật đủ tác giả–năm–tạp chí, một DISCLAIMER, và **không một tag nào**. Quả thua nhồi 20 tag kể cả tên đối thủ. Chưa ai bóc khuôn này.

```
Take ONE video only: [TÊN VIDEO]. Ignore all other sources.

Quote its description verbatim, then map its structure: what appears in
which order, how sources are cited, whether a disclaimer is present,
and how many tags are used.
```

---

# KỲ VỌNG THẬT — ĐỌC TRƯỚC KHI BỎ CÔNG

Ba lệnh này **lấp khe kiến thức, không đổi được số của kênh.**

Nút thắt là **CTR 1,6% trên 17.000 lượt hiển thị**. NotebookLM không nhìn được ảnh nên không giúp gì cho thumbnail, và không thấy YouTube live nên không giúp gì cho chọn đề tài.

Làm ba lệnh này vì nó rẻ và lấp đúng chỗ trống. Đừng làm vì kỳ vọng nó cứu kênh.

---

# SAU KHI CÓ KẾT QUẢ

Gửi tôi. Tôi sẽ:
1. **Tự đếm lại mọi con số bằng script** trên transcript tách riêng — tỉ lệ sai con số của NotebookLM hiện là **7/10**
2. Phân loại từng phát hiện: áp ngay / áp có sửa / bỏ + lý do
3. Cập nhật `HE_THONG_KichBan_v2` và `RUBRIC_KichBan` nếu có gì sống sót

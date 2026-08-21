# QUY TRÌNH 2 CỔNG — bắt buộc cho mọi việc
*Chốt 29/07/2026 sau khi mất một tháng vì tối ưu mù và làm hỏng V15.*

> Không có cổng vào → làm đúng việc sai.
> Không có cổng ra → giao hàng hỏng mà tưởng xong.

---

# 🚪 CỔNG VÀO — trả lời TRƯỚC khi bắt tay

| # | Câu hỏi | Nếu không trả lời được |
|---|---|---|
| 1 | **Việc này cải thiện CON SỐ nào?** | Dừng. Đi lấy số trước.<br>⚠️ **Ngoại lệ ở cỡ mẫu hiện tại:** kênh đang **367 hiển thị / 5 ngày** — gần như không việc gì nêu được một con số đo được. Đọc đúng chữ thì cổng này chặn hết. Ở giai đoạn bệnh A, câu hỏi thay thế là: **"việc này có làm ra thêm một video được đăng không?"** |
| 2 | **Đang có số đó chưa?** | Dừng. Xin ảnh chụp Studio. |
| 3 | **Nó có phải nút thắt hiện tại không?** | Nếu không — nói thẳng là chưa đáng làm. |
| 4 | **File nghiên cứu cũ đã nói gì?** | Mở `BANG_CAU_TatCa_CuNo` · `BANDO_CumChuDe` · mục "đã thử & chết" trước khi đề xuất bất cứ đề tài nào. |
| 5 | **Giả định nào mà nếu sai thì cả việc này vô nghĩa?** | Kiểm giả định đó trước tiên. |

**Bài học nguồn:**
- Câu 1-3: cả tháng tối ưu art style trong khi CTR 1,6% chặn ở cửa. Người xem chưa vào tới nội dung.
- Câu 4: tôi đề xuất đề tài "cái chết" cho V17 trong khi file của chính mình ghi **"when someone died — 72 view"**. Cũng đề xuất "kinh nguyệt" và "mùi cơ thể" — cả hai đã có 9 và 17 kênh làm.
- Câu 5: luật "cấm nói không biết" đúc từ 11 video, ba video triệu view bác sạch.

---

# 🚪 CỔNG RA — kiểm TRƯỚC khi nói "xong"

## ⛔ Ba thứ KHÔNG chứng minh được gì

- Chạy không báo lỗi
- Đủ số file
- Đúng độ dài / đúng kích thước

V15 đạt cả ba và vẫn hỏng hoàn toàn. **Tổng độ dài giống hệt nhau dù thứ tự audio nào.**

## Kiểm theo từng loại sản phẩm

### Video đã ghép
```
1. Lấy tiếng ở 4 mốc rải đều, đối chiếu đường bao âm lượng với file mp3
   đáng lẽ phải phát ở mốc đó.
   ĐẠT: khớp ≥0.90 · đối chứng ≤0.65
2. Lấy khung hình ở 5 mốc, so với ảnh đúng số.
   ĐẠT: lệch ≤0.5 · ảnh sai ≥10
3. Đếm cặp: số ảnh == số tiếng == số shotline
```

### Bộ ảnh đã gen
```
1. Đếm file == số prompt (gen vào thư mục RỖNG, MỘT lượt)
2. Không thiếu số, không dư số, không file <20KB
3. Đo độ sáng nền từng ảnh, đối chiếu với nền đã chỉ định trong prompt
4. Kích thước đồng nhất
```

### Kịch bản
```
Qua 4 CỔNG của ../1_luat/RUBRIC_KichBan.md PHẦN 1 — đạt/không đạt, KHÔNG có thang điểm.
  ① sản xuất  ② sự thật  ③ reused-content  ④ người nghe ngoài
BẮT BUỘC: verify mọi tên riêng / năm / tạp chí bằng web search.
```

> ## ⛔ SỬA 09/08 — Ô CŨ LÀ THANG ĐIỂM THỨ BA TRONG DỰ ÁN
> Nó ghi *"checklist trong `HE_THONG_KichBan_v2` — **17 mục, dưới 14/17 thì viết lại**"*.
> Nhưng PHẦN E của `HE_THONG` có **20 ô**, còn rubric lúc đó có **37 mục**. **Ba con số khác
> nhau cho cùng một việc**, và không con số nào khớp file nó trỏ tới.
>
> Cả ba thang nay đã bỏ *(09/08)*. `HE_THONG` PHẦN E đã dán biển "đừng dùng để chấm".
> Lý do bỏ: ngưỡng phần trăm bắt **điền đủ ô**, và chính nó đẻ ra
> *"ba câu mùi AI nặng nhất trong V17"*.

### Thumbnail
```
1. Thu về 168×94 — vật kể chuyện còn nhìn ra không?
2. Che chữ đi — còn hiểu chuyện gì không?
3. Chữ có KHÁC title không?
4. Bố cục có khác 3 video gần nhất không?
5. Đặt cạnh MẶT trong ảnh video cùng cỡ — có cùng một nhân vật không?
⚠️ ~~Dưới 8/10 mục của scorecard v6~~ — **thang đó đã bỏ**, và file chứa nó đã xoá 09/08. Ba cửa THẬT của thumbnail nằm ở `WORKFLOW_Production.md`
CỬA 5a: **chất liệu · trắng đặc · cắt mặt**. Độ sáng · bão hoà · chiều cao chữ **KHÔNG phải cửa**
*(đo 29 quả thắng: tương quan −0,10 · −0,09 · +0,01)*.
```

### Kết luận nghiên cứu
```
1. Kết luận này dựa trên bao nhiêu mẫu? Dưới 10 thì ghi rõ là chưa chắc.
2. Có video nào NGƯỢC lại kết luận không? Đi tìm chủ động.
3. Đưa Fable 5 hoặc GPT 5.6 soi: "chỗ nào suy từ mẫu quá nhỏ?"
```

---

# NGUYÊN TẮC LÀM VIỆC

**Nói thẳng khi một việc chưa đáng làm.** Kể cả khi đang được bảo làm. Gen lại 17 ảnh, chỉnh nhịp 2,49 giây, đo màu nền — đúng về kỹ thuật, nhưng **không đổi được gì khi CTR 1,6%**.

**Không tối ưu khi chưa có số.** Tối ưu mù chính là thứ đã ngốn một tháng.

**Kết luận phải kèm cỡ mẫu.** "Đo 3 video" và "đo 29 video" là hai mức tin cậy khác nhau, phải nói ra.

**Sai thì sửa file, không sửa trong đầu.** Bốn luật sai hôm nay đã nằm trong prompt và suýt được dùng để viết V17.

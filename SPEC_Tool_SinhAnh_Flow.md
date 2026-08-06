# SPEC — Tool Sinh Ảnh Hàng Loạt trong Google Flow (bản master, dùng lâu dài)

> Dán từng KHỐI bên dưới vào **Flow → Tool Creator** theo thứ tự.
> **Build CORE trước**, chạy thử ổn rồi mới dán từng "Nâng cấp". **Đừng dán hết một lần** — Tool Creator dễ ra tool lỗi nếu nhồi quá nhiều cùng lúc.
> Flow làm tới đâu mình chưa chắc 100%; cái nào nó từ chối / làm đơn giản hơn thì chụp lại gửi mình, mình chỉnh khối cho khớp.

---

## Chuẩn bị trước (làm 1 lần)

Trong project Flow, tạo sẵn các **Ingredients** và đặt tên đúng:
- `@ANCESTOR` · `@MODERNYOU` · `@CHIMP` (3 cast sheet nhân vật)
- `Style` (1 ảnh thể hiện rõ nét vẽ: người que đầu tròn, tóc rối, nét đen sạch, màu phẳng) — dùng để khóa phong cách ở mọi ảnh.

---

## ① CORE — dán khối này ĐẦU TIÊN

```
Tạo cho tôi một tool SINH ẢNH HÀNG LOẠT cho video hoạt hình người que (stickman),
giữ nhân vật nhất quán xuyên suốt.

NHẬP LIỆU:
- Một ô để DÁN hoặc UPLOAD danh sách prompt, MỖI DÒNG = 1 ảnh (khoảng 300 dòng).
- Đầu mỗi dòng có thể có MỘT hoặc NHIỀU tên nhân vật (vd "@ANCESTOR", hoặc
  "@MODERNYOU @CHIMP" nếu cảnh có 2 nhân vật). Phần chữ còn lại của dòng là mô tả ảnh.
- Một khu chọn INGREDIENTS cố định: các cast sheet nhân vật và 1 ingredient tên "Style".

CÁCH SINH:
- Với mỗi dòng: tạo 1 ảnh, GẮN đúng (các) nhân vật được nhắc ở đầu dòng + LUÔN kèm
  ingredient "Style" để khóa nét. Mọi ảnh tham chiếu về đúng bộ ingredient gốc này
  (master reference) — TUYỆT ĐỐI không lấy ảnh vừa tạo làm gốc cho ảnh sau.
- Nút "TẠO TẤT CẢ": chạy lần lượt từ dòng đầu tới hết; xong ảnh này TỰ ĐỘNG sang ảnh
  kế, không phải bấm tay từng ảnh.
- Đặt tên mỗi ảnh theo số thứ tự dòng: 001, 002, 003 …
- Nếu ảnh số đó ĐÃ tạo rồi thì BỎ QUA (không tạo lại) — để dừng rồi chạy tiếp được.

ĐIỀU KHIỂN & AN TOÀN:
- Hiển thị TỔNG số ảnh sẽ tạo; mỗi khi MỘT ảnh tạo XONG thì HIỆN NGAY ảnh đó ra (preview
  trực tiếp, không đợi hết mẻ), kèm bộ đếm "đã xong / tổng". Có thanh tiến trình, nút DỪNG và TIẾP TỤC.
- LƯU tiến trình: tải lại trang / treo máy rồi mở lại vẫn còn ảnh đã tạo, chạy tiếp
  được. Có nút RESET để xóa làm lại từ đầu.
- Ảnh nào lỗi hoặc bị chặn nội dung: tự thử lại 1–2 lần; vẫn lỗi thì bỏ qua, đi tiếp,
  KHÔNG làm dừng cả mẻ.
- Nút TẢI TẤT CẢ ảnh về dạng ZIP, giữ đúng tên 001…

CÀI ĐẶT: model chất lượng cao nhất (Nano Banana Pro), tỉ lệ 16:9, độ phân giải 4K.
Phong cách: doodle người que vẽ tay, nét đen sạch, màu phẳng, nền trắng (khóa bằng
ingredient "Style").
```

→ Build xong, **test với ~5–10 dòng prompt** trước. Ổn rồi mới dán các Nâng cấp.

---

## ② NÂNG CẤP — dán TỪNG khối, sau khi Core chạy ổn

> Mỗi khối đều có dòng "chỉ THÊM, giữ nguyên cái đang chạy" để Flow không phá Core.

### 2.1 — Lưới duyệt (QC)
```
Thêm vào tool đang có (CHỈ THÊM, giữ nguyên mọi thứ đang chạy):
một LƯỚI XEM LẠI hiển thị thumbnail tất cả ảnh đã tạo theo thứ tự 001…, bấm vào một ảnh
để phóng to. Mỗi ảnh có nút đánh dấu "Cần làm lại". Cho lọc xem riêng các ảnh bị đánh dấu.
Xong hãy liệt kê ngắn gọn đã đổi gì.
```

### 2.2 — Tạo lại 1 ảnh lẻ + sửa prompt dòng đó
```
Thêm (CHỈ THÊM, giữ nguyên cái đang chạy):
cho phép TẠO LẠI MỘT ẢNH LẺ mà không chạy cả mẻ — chọn 1 ảnh → sửa prompt của dòng đó
ngay trong tool nếu muốn → bấm "Tạo lại ảnh này"; chỉ ảnh đó thay đổi, các ảnh khác giữ nguyên.
Xong liệt kê đã đổi gì.
```

### 2.3 — Chạy lại từ ảnh số N + làm lại ảnh đã đánh dấu
```
Thêm (CHỈ THÊM, giữ nguyên cái đang chạy):
- ô "Chạy lại từ ảnh số N" để bắt đầu lại từ vị trí bất kỳ.
- nút "Tạo lại các ảnh đã đánh dấu Cần làm lại" (chỉ làm lại những ảnh đó, bỏ qua phần còn lại).
Xong liệt kê đã đổi gì.
```

### 2.4 — Số ảnh chạy song song
```
Thêm (CHỉ THÊM, giữ nguyên cái đang chạy):
ô chỉnh "Số ảnh tạo song song" (mặc định 4, cho chọn 1–8) và giãn nhịp nhẹ giữa các lượt
để tránh bị chặn/giới hạn. KHÔNG đổi cách gắn ingredient hay style.
Xong liệt kê đã đổi gì.
```

### 2.5 — Bảng log lỗi
```
Thêm (CHỈ THÊM, giữ nguyên cái đang chạy):
một BẢNG LOG liệt kê các ảnh tạo lỗi (số thứ tự + lý do nếu có), và nút xuất danh sách đó
ra text để tôi biết ảnh nào cần làm lại.
Xong liệt kê đã đổi gì.
```

### 2.6 — Sơ đồ DÂY NỐI ref → ảnh (xem có nhận đúng ref không)
```
Thêm (CHỈ THÊM, giữ nguyên cái đang chạy):
một SƠ ĐỒ NODE kéo-thả: mỗi INGREDIENT (ref) là một ô bên trái; mỗi ẢNH/PROMPT là một ô
bên phải. Vẽ DÂY NỐI từ mỗi ingredient tới đúng những ảnh dùng nó, để tôi NHÌN THẤY ảnh
nào đang nhận ref nào — kiểm tra gắn đúng ref chưa TRƯỚC khi bấm tạo.
- Bấm một ảnh → làm nổi bật các dây ref đang nối vào nó (vd @ANCESTOR + Style).
- Bấm một ingredient → làm nổi bật tất cả ảnh nó đang nuôi.
- Ảnh nào KHÔNG có dây ref nào nối vào (quên gắn) → tô ĐỎ cảnh báo.
Nếu Flow chưa dựng được sơ đồ node có dây, thay tạm bằng: mỗi ảnh hiện một NHÃN nhỏ liệt kê
ref đã dùng (vd "@ANCESTOR + Style") để vẫn kiểm tra được.
Xong liệt kê đã đổi gì.
```

### 2.7 — Smart ref binding (tự gắn ref thông minh)
```
Thêm (CHỈ THÊM, giữ nguyên cái đang chạy):
TỰ ĐỘNG nhận diện nhân vật cho mỗi dòng prompt và TỰ GẮN đúng ingredient + Style, khỏi nối
tay từng ảnh. Quy tắc nhận:
1. Ưu tiên @token ở đầu dòng (vd @ANCESTOR).
2. Nếu dòng không có @token, dò TỪ KHÓA trong câu để đoán nhân vật (vd "caveman / fur tunic"
   → @ANCESTOR; "hoodie / modern" → @MODERNYOU; "chimp / monkey" → @CHIMP).
3. Cho tôi một BẢNG ÁNH XẠ sửa được: [từ khóa] → [ingredient], để tôi tự thêm / đổi quy tắc.
4. Dòng nào không khớp nhân vật nào → tô ĐỎ để tôi gán tay.
5. Hiển thị ref đã tự gắn cho từng dòng (đồng bộ sơ đồ dây ở mục 2.6) để tôi xác nhận trước khi tạo.
Xong liệt kê đã đổi gì.
```

---

## Quy tắc vàng (nếu lỡ build hỏng)

Dán câu này khi một nâng cấp làm hỏng tool:
```
Thay đổi vừa rồi làm hỏng [mô tả lỗi]. Hãy HOÀN TÁC đúng thay đổi đó để tool chạy lại như
trước, KHÔNG đụng phần nào khác. Sau đó nói vì sao hỏng rồi đề xuất cách làm lại an toàn hơn.
```

## Ghi nhớ
- **Một lần một khối.** Test xong mới qua khối tiếp.
- Trước mỗi nâng cấp, nếu Flow có **lưu phiên bản** thì giữ lại để lùi được.
- Luôn giữ đúng bộ tên ingredient (`@ANCESTOR / @MODERNYOU / @CHIMP / Style`) để tool gọi trúng.

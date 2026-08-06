# Sketchapiens — Tool sinh ảnh hàng loạt (chạy trong Google Flow)

Bản RIÊNG của mình (code mới, không copy giao diện tool ông kia). Dùng `flow-sdk` để chạy *bên trong* Google Flow → xài credit Ultra của bạn, **không cần API key, không tốn phí riêng**.

## Tính năng
- **Chọn refs (Ingredients)** từ thư viện Flow → tự đặt `refKey` theo tên file, sửa được.
- **Khoá Style:** ref nào có refKey = `style` sẽ được **gắn vào MỌI ảnh** (khoá nét).
- **Smart ref binding:** mỗi dòng prompt nhắc `@refKey` nào thì chỉ gắn đúng ref đó (+ style).
- **Danh sách prompt:** dán hoặc upload `.txt`, mỗi dòng = 1 ảnh.
- **GRID từng ảnh:** số thứ tự, trạng thái, **thumbnail hiện ngay khi xong**, chip ref đang gắn, **sửa prompt tại chỗ**, **tạo lại ảnh lẻ**, tải ảnh lẻ.
- **Tạo tất cả:** chạy song song (chỉnh 1–8), **tự chạy tiếp đến hết**, **bỏ qua ảnh đã xong**, Tạm dừng / Dừng.
- **Tự retry** 3 lần khi lỗi/bị chặn (không làm dừng cả mẻ).
- **Tự lưu (IndexedDB):** reload / treo máy không mất tiến trình. Có **Reset**.
- **Tải tất cả** (lặp `Flow.download`, giữ tên `PREFIX-I.001…`).

## Cách đưa vào Flow
1. Mở tool của bạn trong **Flow → vào trình sửa code** của tool.
2. **Dán toàn bộ `App.tsx`** vào (thay cho component chính). Tool này chỉ cần `react` + `flow-sdk` (đều có sẵn trong môi trường Flow), không thêm thư viện ngoài.
3. Lưu / Run trong Flow.

> Nếu Flow tách nhiều file, chỉ cần đây là **component mặc định** (`export default App`).

## Chuẩn bị refs (làm 1 lần)
- Upload vào thư viện Flow: 3 cast sheet + 1 ảnh **Style**.
- Trong tool bấm **Chọn refs** → đặt tên refKey đúng: `ANCESTOR`, `MODERNYOU`, `CHIMP`, và `style`.
  (Trong prompt bạn gọi `@ANCESTOR`… Tool tự khớp; `style` luôn được gắn.)

## Dùng
1. Chọn refs + đặt refKey.
2. Dán danh sách prompt (file `IMG_PROMPTS_UPLOAD.txt` của bạn — mỗi dòng đã có `@ref` ở đầu).
3. Chọn model (Nano Banana Pro), tỉ lệ 16:9, prefix tên file.
4. **Tạo tất cả** → xem ảnh nảy ra lần lượt → tải tất cả.

## Lưu ý thật
- Mình **chưa chạy được `flow-sdk` ở môi trường build** (không có browser/SDK ở đó), nhưng đã soát cú pháp TSX sạch (esbuild OK). Nếu Flow báo lỗi **tên hàm/tham số `flow-sdk`** (vd `Flow.media.selectMultiple`, `Flow.generate.image`, `Flow.download`), **chụp lỗi gửi mình** — mình chỉnh đúng API ngay.
- Đây là bản v1 đầy đủ (master); muốn thêm gì (vd sơ đồ dây, log lỗi xuất file) mình thêm sau.

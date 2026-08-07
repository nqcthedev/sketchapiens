# PROMPT NÂNG CẤP TOOL AN TOÀN (không phá logic đang chạy)

Mục tiêu: thêm 2 tính năng mà KHÔNG làm hỏng cái đang chạy
1. **Lưu bộ nhớ bền** — treo máy / reload / tắt mở lại KHÔNG mất tiến trình.
2. **Chạy 20 ảnh/luồng** thay vì 10.

> ⚠️ Quy tắc số 1: **LÀM TỪNG TÍNH NĂNG MỘT**, test xong cái 1 rồi mới qua cái 2.
> Làm cả hai cùng lúc mà vỡ thì không biết lỗi do cái nào.

---

## 0) DÁN ĐOẠN NÀY LÊN ĐẦU MỌI YÊU CẦU (Nguyên tắc vàng)

```
NGUYÊN TẮC BẮT BUỘC khi sửa app này:
1. CHỈ sửa đúng phần tôi yêu cầu. KHÔNG refactor, KHÔNG đổi tên hàm/biến,
   KHÔNG xoá hay viết lại tính năng đang chạy.
2. Mọi chức năng hiện tại phải chạy y như cũ (không được regression).
3. Thay đổi TỐI THIỂU — càng ít dòng càng tốt. Chỉ THÊM, hạn chế SỬA.
4. TRƯỚC KHI viết code: đọc phần code liên quan, rồi NÓI cho tôi biết
   - bạn sẽ đụng file/hàm nào,
   - đổi cái gì, vì sao,
   - rủi ro gì.
   Rồi DỪNG LẠI chờ tôi duyệt. Chưa duyệt thì chưa được sửa code.
5. Nếu thay đổi có thể ảnh hưởng phần khác → DỪNG và hỏi tôi, đừng tự quyết.
6. Làm xong: liệt kê ngắn gọn ĐÃ ĐỔI GÌ (file + dòng) để tôi kiểm.
7. Trước khi sửa, lưu/giữ một bản backup (hoặc version) để tôi quay lại được.
```

---

## 1) BƯỚC THĂM DÒ (chạy TRƯỚC, không cho sửa code)

> Mục đích: ép AI hiểu code trước khi đụng vào, tránh đập nhầm.

```
[Áp dụng NGUYÊN TẮC VÀNG ở trên]

CHƯA sửa gì cả. Tôi chỉ cần bạn ĐỌC và TRẢ LỜI:
1. Hiện tại app lưu trạng thái (danh sách prompt, ảnh đã gen, tiến trình)
   ở đâu? Chỉ trong bộ nhớ tạm (React state) hay đã có IndexedDB/localStorage?
2. Khi reload trang thì cái gì bị mất, cái gì còn?
3. Con số giới hạn "10 ảnh mỗi đợt" nằm ở biến/hằng số nào, file nào,
   dòng nào? Có bị lặp ở nhiều chỗ không?
4. Nếu tăng lên 20 thì có thể đụng giới hạn nào (rate limit API, bộ nhớ,
   bố cục lưới UI) không?

Trả lời bằng tiếng Việt, kèm tên file + số dòng. ĐỪNG sửa code.
```

→ Đọc xong câu trả lời của nó rồi mới sang Bước 2.

---

## 2) TÍNH NĂNG 1 — LƯU BỘ NHỚ BỀN (làm trước, test trước)

```
[Áp dụng NGUYÊN TẮC VÀNG]

Thêm tính năng TỰ LƯU & TỰ KHÔI PHỤC tiến trình, để khi treo máy /
reload / tắt mở lại trình duyệt thì KHÔNG mất, không phải chạy lại từ đầu.

YÊU CẦU:
- Dùng IndexedDB (vì cần lưu nhiều dữ liệu và cả ảnh). Nếu app ĐÃ có sẵn
  store thì TÁI SỬ DỤNG, đừng tạo trùng.
- TỰ ĐỘNG LƯU sau mỗi thay đổi quan trọng: thêm/sửa prompt, gen xong 1 ảnh,
  đổi cài đặt. (Lưu kiểu debounce ~1 giây để khỏi lưu liên tục gây lag.)
- TỰ ĐỘNG NẠP LẠI trạng thái đã lưu khi mở app / reload.
- Thêm 1 nút "Xoá bộ nhớ / Reset" để khi cần làm mới hoàn toàn.

RÀNG BUỘC AN TOÀN (quan trọng):
- KHÔNG đổi cấu trúc state hiện tại. Chỉ BỌC THÊM một lớp lưu/nạp bên ngoài.
- Nếu CHƯA có dữ liệu lưu (lần đầu mở) → app chạy y hệt như cũ.
- Bọc đọc/ghi trong try/catch: nếu dữ liệu cũ hỏng hoặc sai phiên bản thì
  BỎ QUA và chạy như mới — TUYỆT ĐỐI không để crash app.
- Gắn 1 "version" cho dữ liệu lưu; sau này đổi cấu trúc thì tự bỏ bản cũ.

Làm xong, hướng dẫn tôi cách TEST. Chưa code vội — nói kế hoạch + file sẽ
đụng cho tôi duyệt trước.
```

**Test cái 1 trước khi đi tiếp:**
- Gen vài ảnh → **reload trang** → tiến trình còn nguyên?
- **Tắt tab, mở lại** → còn nguyên?
- Để **treo máy** một lúc rồi quay lại → còn nguyên?
- Bấm **Reset** → xoá sạch được?
- Mở Console (F12) → **không có lỗi đỏ**?

✅ Ổn hết mới sang cái 2.

---

## 3) TÍNH NĂNG 2 — 20 ẢNH / LUỒNG (làm sau, test riêng)

```
[Áp dụng NGUYÊN TẮC VÀNG]

Tăng số ảnh xử lý song song trong 1 đợt từ 10 lên 20.

YÊU CẦU:
- Tìm đúng HẰNG SỐ đang giới hạn 10 (ví dụ BATCH_SIZE / CONCURRENCY / limit)
  và đổi giá trị thành 20. Đưa số này ra thành 1 biến dễ chỉnh ở trên đầu.
- Nếu con số 10 nằm rải rác nhiều chỗ → LIỆT KÊ ra cho tôi, hỏi trước,
  đừng tự đổi hết.

RÀNG BUỘC AN TOÀN:
- KHÔNG đổi logic gọi API hay cách xử lý kết quả — CHỈ đổi số lượng đồng thời.
- GIỮ NGUYÊN cơ chế hàng đợi / retry / báo lỗi đang có. Nếu chưa có retry khi
  API trả lỗi 429 (quá tải) thì nói tôi biết, vì tăng lên 20 dễ bị giới hạn hơn.
- Đừng đổi bố cục UI; nếu lưới đang giả định 10 ô/hàng thì cho nó tự co giãn.

Nói kế hoạch trước, chờ tôi duyệt rồi mới sửa.
```

**Test cái 2:**
- Một đợt giờ ra **đúng 20 ảnh**?
- Không bị lỗi **429 / rate limit** (nếu có thì giảm còn 15, hoặc bật retry)?
- Các tính năng cũ + lưu bộ nhớ (cái 1) vẫn chạy?

---

## 4) NẾU LỠ BỊ VỠ

Dán câu này:

```
Thay đổi vừa rồi làm hỏng [mô tả lỗi]. Hãy HOÀN TÁC đúng thay đổi đó để app
chạy lại như trước, KHÔNG đụng phần nào khác. Sau đó giải thích vì sao hỏng,
rồi đề xuất cách làm lại an toàn hơn — chờ tôi duyệt mới làm.
```

---

### Mẹo gốc rễ
- **Một lần một việc.** Đừng gộp nhiều yêu cầu.
- **Bắt nó nói trước, code sau.** 90% vỡ là do nó tự ý sửa rộng.
- **Giữ version/backup** mỗi lần, để luôn lùi được.

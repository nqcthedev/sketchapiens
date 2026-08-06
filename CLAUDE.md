# SKETCHAPIENS — LUẬT PHIÊN LÀM VIỆC

> Kênh YouTube faceless người-que, ngách **Ancient Humans Explained**, lời đọc **tiếng Anh**, tài liệu **tiếng Việt**.
> File này chỉ giữ luật **phải biết trong mọi phiên**. Luật theo khu vực nằm ở `.claude/rules/`.

## 0. ĐỌC GÌ TRƯỚC

| Câu hỏi | File |
|---|---|
| File nào là luật cho việc này? | `governance/SOURCE_OF_TRUTH.md` |
| Có được đổi luật không? | `governance/CHANGE_POLICY.md` |
| Việc này chủ đã quyết chưa? | `governance/DECISIONS_REQUIRED.md` |
| Hiện trạng kho ra sao? | `PROJECT_FULL_AUDIT_EXPORT.md` |

Kho cũ vẫn là nguồn nội dung: `00_LUAT_HIEN_HANH.md` là cửa vào tầng tri thức cũ. **Không sửa nó trong phiên thường.**

## 1. MƯỜI LUẬT KHÔNG PHÁ

1. **Không ghi đè kịch bản.** Mỗi lần sửa tạo `vNNN` mới. `approved.md` và `published.md` là bất biến.
2. **Không tự phong "final".** Chỉ người dùng duyệt mới thành `approved`.
3. **Không suy ra `published`.** Chưa có publish record thì trạng thái là `not_published`.
4. **Không mở corpus đối thủ khi đang viết.** `2_KHO_BANGHI/` chỉ để ĐO, ở phiên research riêng.
5. **Agent review chỉ chấm, không sửa.** Một editor duy nhất tạo version mới, sau khi người dùng phân loại.
6. **Mọi câu thêm vào sau cổng mỏ neo phải chạy lại cổng mỏ neo.**
7. **Suy diễn của tác giả nguồn phải ghi rõ là suy diễn** (*"the researchers put that down to…"*), cấm nói như sự thật.
8. **Chỉ 4 ràng buộc cứng của lời đọc:** `!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng · `I` ≈ 0. Mọi con số khác là **triệu chứng**, không phải đích. Cấm sửa câu cho số đẹp.
9. **Không nâng một quan sát thành luật kênh** nếu chưa đủ 5 thứ: bằng chứng · độ tin cậy · phạm vi · người duyệt · luật cũ bị thay.
10. **Không xoá, không đổi tên, không di chuyển dữ liệu cũ.** V01–V19 và 79 file gốc giữ nguyên cho tới khi có lệnh migration riêng.

## 2. BỐN CHẾ ĐỘ — mỗi phiên MỘT chế độ

| Chế độ | Gọi bằng | Cấm |
|---|---|---|
| ① NGHIÊN CỨU | `sketchapiens-chon-de-tai` | không viết kịch bản |
| ② VIẾT | `sketchapiens-viet-kich-ban` | **không mở nexlev · không tra web · không mở `2_KHO_BANGHI/`** |
| ③ BIÊN TẬP | `sketchapiens-bien-tap` · `/apply-review` | không viết nội dung mới |
| ④ SẢN XUẤT | `sketchapiens-chia-shot` · `sketchapiens-thumbnail` | chưa qua cổng chất lượng thì chưa chia shot |

Đang ở chế độ này mà thấy việc của chế độ khác → **ghi vào sổ, không làm ngay**.

## 3. OVERRIDE — luật project thắng skill toàn cục

Hai skill toàn cục sau **KHÔNG phải nguồn chuẩn trong project này**:

- ⛔ `viet-kich-ban-nguoi-que-co-dai` → dùng `sketchapiens-viet-kich-ban`
- ⛔ `chia-shot-va-prompt-anh` → dùng `sketchapiens-chia-shot`

Lý do (`PROJECT_FULL_AUDIT_EXPORT.md` §5, R2): cả hai không có tiền tố nên tự kích hoạt, và PHẦN 9 của cả hai vẫn trỏ tới `TEMPLATE_Thumbnail_DoiThu.md` **đã bị bác**.

**Không sửa, không xoá hai skill đó ở global scope.** Nếu chúng tự nạp, bỏ qua nội dung và nói rõ trong câu trả lời.

## 4. LỆNH CÓ SẴN

| Lệnh | Việc |
|---|---|
| `/new-video` | Dựng khung một video mới theo lifecycle |
| `/audit-script` | Chạy 5 giám khảo độc lập, gộp thành một bản chấm |
| `/apply-review` | Sau khi người dùng phân loại → editor tạo version mới |
| `/verify-claims` | Đối chiếu claim ledger với nguồn gốc |
| `/project-doctor` | Kiểm tính toàn vẹn cấu trúc |
| `/postmortem` | Đóng vòng phản hồi sau khi có số liệu |

## 5. VÒNG ĐỜI VIDEO — không nhảy bậc

```
idea → selected → researched → evidence_locked → draft → internally_audited
→ externally_reviewed → revised → script_approved → packaged → production_ready
→ produced → published → measured → postmortem_complete → archived
```

Thiếu artefact bắt buộc thì **không được chuyển trạng thái**. Bảng artefact: `schemas/video.schema.json`.

## 6. BẢO MẬT

Khoá API đọc từ biến môi trường, **không bao giờ ghi vào file**. Không commit `.env`, token, credential.
Nếu thấy khoá trong file: báo vị trí + loại, **không in giá trị**.

## 7. NGÔN NGỮ & DUYỆT

- Lời đọc: **tiếng Anh**. Trao đổi và tài liệu: **tiếng Việt**.
- Khi trình kịch bản để duyệt: bảng **EN + nghĩa VI**, không kèm cột hình.
- Viết theo **đợt**, dừng cho duyệt giữa các đợt. Không đổ một mạch.
- Giao bản tốt nhất ngay lần đầu; không đưa bản nửa vời rồi chờ nhắc.

## 8. macOS

App giữ bản cũ trong bộ nhớ. Trước khi `open` một file vừa ghi đè:
`osascript -e 'tell application "TextEdit" to quit saving no'`

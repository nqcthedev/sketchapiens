# SKETCHAPIENS — LUẬT PHIÊN LÀM VIỆC

> Kênh YouTube faceless người-que, ngách **Ancient Humans Explained**, lời đọc **tiếng Anh**, tài liệu **tiếng Việt**.
> File này chỉ giữ luật **phải biết trong mọi phiên**. Luật theo khu vực nằm ở `.claude/rules/`.

## 0. ĐỌC GÌ TRƯỚC

| Câu hỏi | File |
|---|---|
| File nào là luật cho việc này? | `governance/SOURCE_OF_TRUTH.md` |
| Có được đổi luật không? | `governance/CHANGE_POLICY.md` |
| Việc này chủ đã quyết chưa? | `governance/DECISIONS_REQUIRED.md` |
| Dự án khác muốn làm theo cấu trúc này? | `governance/NEN_MONG_KeThua.md` |
| Hiện trạng kho ra sao? | `governance/PROJECT_FULL_AUDIT_EXPORT.md` |

Kho tri thức: `00_LUAT_HIEN_HANH.md` là **cửa vào**, nó nói mỗi câu hỏi thì file nào là luật.
**Không sửa nó trong phiên thường.**

**Cấu trúc kho** *(dọn 07/08/2026 — gốc kho từ 73 file `.md` xuống còn 2)*:

| | | được quyền phán? |
|---|---|---|
| `kho/1_luat/` | luật đang hiệu lực — quy trình, rubric, thumbnail, art bible | ✅ |
| `kho/2_nguyenlieu/` | tra khi viết — vault, kho ẩn dụ, mổ xẻ đối thủ, kịch bản mẫu | ❌ |
| `kho/3_bangchung/` | nghiên cứu đã rút thành luật — chỉ mở khi cần tra lại | ❌ |
| `kho/4_luutru/` | V17/V18, spec công cụ, lệnh cho AI ngoài | ❌ |
| `2_KHO_BANGHI/` | 761 bản ghi đối thủ — **chỉ để ĐO**, cấm mở khi đang viết | đo lại được |
| `videos/` | từng video: V17 *(hai bản)* · V18 · V19. **V02–V16 đã xoá 07/08** | — |

**Luật ưu tiên khi hai file nói ngược nhau:** tầng thấp hơn thắng · đếm tay trên bản ghi gốc
thắng mọi báo cáo · cùng tầng thì file mới hơn thắng · không giải quyết được thì **đo lại**.

## 1. MƯỜI LUẬT KHÔNG PHÁ

1. **Không ghi đè kịch bản.** `03-script/versions/vNNN.md` **bất biến**. Sửa = tạo `vNNN` kế tiếp.
   `approved` và `published` là **con trỏ** (`03-script/refs/*.yaml`), không phải bản sao — con trỏ đổi được, version thì không.
2. **Không tự phong "final".** Con trỏ `approved.yaml` và `published.yaml` phải có `set_by: owner` — hook chặn nếu thiếu.
3. **Không suy ra `published`.** Chưa có publish record thì trạng thái là `not_published`.
4. **Không mở corpus đối thủ khi đang viết.** `2_KHO_BANGHI/` chỉ để ĐO, ở phiên research riêng.
5. **Agent review chỉ chấm, không sửa.** Một editor duy nhất tạo version mới, sau khi người dùng phân loại.
   🔴 **Subagent KHÔNG lạnh.** Tài liệu chính thức Claude Code: subagent nạp đủ `CLAUDE.md` và
   project rules; **chỉ Explore và Plan bỏ qua, và không chỉnh được**. Nên **review ngoài bằng
   ChatGPT (chat mới) là lớp người-xem-lạnh DUY NHẤT — không bỏ được, không thay bằng agent được.**
6. **Mọi câu thêm vào sau cổng mỏ neo phải chạy lại cổng mỏ neo.**
7. **Suy diễn của tác giả nguồn phải ghi rõ là suy diễn** (*"the researchers put that down to…"*), cấm nói như sự thật.
8. **Chỉ 3 ràng buộc cứng của lời đọc:** `!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng.
   Mọi con số khác là **triệu chứng**, không phải đích. Cấm sửa câu cho số đẹp.
   ⛔ `I ≈ 0` **đã gỡ 07/08** — đo 18 kênh trong kho, 9/12 kênh có phép so sạch cho thấy bài dùng "I"
   ăn hơn *(Mack 9,18×)*. Người dẫn **được có ý kiến riêng**. Xem `governance/RETIRED_RULES.md`.
9. **Không nâng một quan sát thành luật kênh** nếu chưa đủ 5 thứ: bằng chứng · độ tin cậy · phạm vi · người duyệt · luật cũ bị thay.
10. **Không xoá dữ liệu khi chưa có lệnh của chủ.** *(Sửa 07/08: chủ đã ra lệnh dọn một lần —
    V02–V16 và 5 file `.md` chết vào thùng rác; 65 file `.md` ở gốc chuyển vào `kho/1..4/`.)*
    Ngoài lệnh đó, mặc định vẫn là **không xoá, không đổi tên, không di chuyển**.

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

Lý do (`governance/PROJECT_FULL_AUDIT_EXPORT.md` §5, R2): cả hai không có tiền tố nên tự kích hoạt, và PHẦN 9 của cả hai vẫn trỏ tới `TEMPLATE_Thumbnail_DoiThu.md` **đã bị bác**.

**Không sửa, không xoá hai skill đó ở global scope.** Nếu chúng tự nạp, bỏ qua nội dung và nói rõ trong câu trả lời.

## 4. LỆNH CÓ SẴN

| Lệnh | Việc |
|---|---|
| `/new-video` | Dựng khung một video mới theo lifecycle |
| `/audit-script` | Chạy 3 giám khảo ngữ-cảnh-riêng, gộp thành một bản chấm |
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
- ⛔ **Bỏ bảng EN+VI** *(chủ chốt 07/08/2026: không đọc cột dịch)*. Trình **thẳng lời đọc tiếng Anh**.
  Bằng chứng: `DUYET_V19_EN_VI.md` lệch kịch bản **22 dòng** qua hai vòng review mà không ai thấy;
  12/18 video chưa từng có bảng duyệt nào vẫn sản xuất bình thường. Dịch chỉ khi chủ hỏi một câu cụ thể.
- Chất lượng tiếng Anh là việc của AI. Việc của chủ là **gu và quyết định**, không phải rà câu chữ.
- Viết theo **đợt**, dừng cho duyệt giữa các đợt. Không đổ một mạch.
- Giao bản tốt nhất ngay lần đầu; không đưa bản nửa vời rồi chờ nhắc.

## 8. macOS

App giữ bản cũ trong bộ nhớ. Trước khi `open` một file vừa ghi đè:
`osascript -e 'tell application "TextEdit" to quit saving no'`

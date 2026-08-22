# 05A-B — RESPONSIBILITY DECOMPOSITION

> **READ-ONLY AUDIT.** Không sửa agent, skill, rule hay tool nào trong task này.

**Phase:** 5 — Agent Architecture
**Checkpoint:** `152085f`
**Ngày:** 2026-08-22

## 1. BẢNG SỞ HỮU — ĐỌC TỪ FILE, KHÔNG SUY TỪ TÊN

| artefact | sở hữu | KHÔNG sở hữu | được ghi file? |
|---|---|---|---|
| `viewer-retention-judge` | chỗ người xem bỏ đi · ba lời hứa · bản đồ giữ chân · điểm thoát | factual verdict · prose · cấu trúc *(chỉ chẩn đoán, không quyết)* | ❌ |
| `evidence-prosecutor` | claim verdict · bridge verdict · provenance · transfer · lockability | retention · prose · title/thumbnail · sửa kịch bản | ❌ |
| `anti-ai-narration-critic` | mùi văn AI · ẩn dụ chồng tầng · sẹo vá | research · claim ledger · rubric điểm · Story theory | ❌ |
| `audit-script` | điều phối 3 giám khảo · gộp một bản chấm | quyết định áp gì | ❌ read-only |
| `apply-review` | **editor duy nhất** — tạo `vNNN` mới | tự phân loại · tự re-audit · đặt `approved`/`published` | ✅ **duy nhất** |
| `verify-claims` | orchestration wrapper cho Evidence Engine | semantic verdict *(thuộc Engine)* | ghi verification run |
| `sketchapiens-bien-tap` | đo bằng máy · QA chính sách YouTube · cổng 7/8/9/11 | viết nội dung mới · đổi cú bẻ lái | ❌ |
| `sketchapiens-giu-chan-nguoi-xem` | craft câu/đoạn | structural authority *(đã thu về từ Phase 2)* | ❌ |

**Kết quả:** quyền ghi kịch bản tập trung đúng **một** chỗ — `apply-review`. Bảy artefact còn lại
read-only hoặc chỉ ghi artefact của chính nó. Đây là thứ Phase 5 đặt ra để bảo vệ, và nó **đang
đúng**.

## 2. TRẢ LỜI F-3 — `anti-ai-narration-critic` có thiếu ràng buộc không?

`05A-A` để mở hai cách đọc. Đọc file thật thì **cách đọc (a) đúng**: nó không thiếu ràng buộc, và
việc không nối vào `prose-and-voice.md` là **có lý do**.

Bằng chứng trong chính agent:

```text
Bạn ĐƯỢC đọc      lời đọc · knowledge/writing/** nếu có
Bạn KHÔNG đọc     research · claim ledger · rubric điểm số
Luật              không viết lại, không đề xuất câu thay thế
                  đừng gạch nửa bài — gạch 60/150 câu là hết khả năng phân biệt
                  hedge tiết chế là con hào của kênh, KHÔNG tính là lỗi
                  ngôi 2 nhập vai là động cơ của ngách, KHÔNG tính là lỗi
```

Nó có bảy dấu hiệu ưu tiên, hai miễn trừ đích danh, và một luật chống over-flagging rút từ sự cố
thật. Đó là contract, không phải gu.

**Và nếu nối nó vào `prose-and-voice.md` thì hỏng đúng chỗ nó có giá trị:** Writer viết theo
`prose-and-voice.md`; critic đọc cùng file đó rồi chấm sẽ chấm theo đúng khuôn vừa sinh ra bản
nháp. Con mắt độc lập mất ngay tại đó.

**Disposition:** F-3 đóng. Không nối critic vào Writer prose theory. Ghi vào `05A-E` như một
quyết định có chủ đích, để `05B` và các phase sau không "sửa" nó.

## 3. VẤN ĐỀ THẬT TÌM ĐƯỢC — `F-5` · ví dụ lỗi thời in luật đã chết dưới nhãn CỨNG

`sketchapiens-bien-tap/SKILL.md` có khối *"Ví dụ kết quả thật (V19, 06/08)"*:

```text
CỨNG: '!' 0 (0) | '—' 0 (0) | 'I' 0 (≈0) | 3 câu dài liên tiếp: không
```

Ảnh chụp này từ **06/08** — trước khi `I ≈ 0` bị gỡ ngày **07/08**.

Ba nguồn khác **đều đã đúng**:

```text
qa_kichban.py:18-21   ⛔ 09/08 — CHỈ CÒN BA RÀNG BUỘC CỨNG. 'I' ĐÃ BỊ GỠ 07/08
qa_kichban.py:23      in 'I' dưới nhãn "ĐO — KHÔNG PHẢI NGƯỠNG"
bien-tap bảng luật    ~~`I` đứng riêng~~ ⛔ GỠ 07/08
audit-script          ⛔ `I ≈ 0` đã gỡ 07/08
```

Nên đây **không phải dead rule đang sống** — luật đã chết ở mọi nơi có thẩm quyền. Nó là **ví dụ
lỗi thời mâu thuẫn với bảng luật nằm ngay 9 dòng bên dưới nó**.

**Vì sao vẫn đáng sửa:** chính `qa_kichban.py:19-20` ghi lại hậu quả đã xảy ra một lần:

> *"Bản cũ in `'I'` dưới nhãn CỨNG, và `/apply-review` đọc dòng đó làm điều kiện chặn → editor sẽ
> CẮT MỌI CÂU CÓ `I`."*

Tool đã được vá để không in nữa. Nhưng **ví dụ trong tài liệu vẫn in**, và một reader — người hay
agent — đọc lướt khối `CỨNG:` trước khi đọc bảng bên dưới sẽ tái lập đúng lỗi cũ.

Severity: `P2`. Không chặn, nhưng thuộc đúng họ `D-ARCH-02` — *dead rules vẫn có thể sống ở
consumer*. Sửa ở `05B-C`.

## 4. CHỒNG LẤN — CÓ MỘT, VÀ NÓ CÓ CHỦ ĐÍCH

`viewer-retention-judge` và `sketchapiens-giu-chan-nguoi-xem` cùng đụng retention. Nhưng ranh giới
đã được Phase 2 khoá:

```text
viewer-retention-judge          chẩn đoán retention ở cấp chương/video, dùng Story Engine
sketchapiens-giu-chan-nguoi-xem craft câu/đoạn, KHÔNG còn structural authority
```

Roadmap Phase 2 ghi: *"retention skill cũ được thu thành sentence/paragraph craft support, không
còn structural authority"*. Đây là chồng lấn **đã giải**, không phải nợ mới.

Không tìm thấy chồng lấn nào khác giữa 8 artefact.

## 5. ĐIỂM ĐANG ĐÚNG — GHI ĐỂ `05B` KHÔNG PHÁ

1. **Một editor duy nhất.** `apply-review` là nơi duy nhất tạo `vNNN`, và nó không được đặt
   `approved`/`published`.
2. **`audit-script` không preload context chung.** Có bảng consumer context riêng cho từng agent,
   kèm câu giải thích *"tai sạch không có nghĩa ba agent phải mù cùng một thứ"*.
3. **`viewer-retention-judge` có `CONTEXT BUDGET` đích danh** — chặn `candidate-lifecycle.md` và
   `mechanism-lab.md` bằng tên, không bằng nguyên tắc chung. Đây là lời giải sẵn có cho `F-1`.
4. **Cả ba agent đều cấm viết lại.** Không agent nào được đề xuất câu thay thế.
5. **`WebFetch` chỉ ở `evidence-prosecutor`** — đúng ownership.
6. **Cả ba agent tự thừa nhận không lạnh**, và cả `audit-script` lẫn `viewer-retention-judge` đều
   ghi rõ lớp lạnh thật là review ngoài bằng ChatGPT.

## 6. FINDINGS SAU 05A-B

| id | nội dung | mức | disposition |
|---|---|---|---|
| F-1 | context tĩnh là sàn không phải trần | QUAN SÁT | **đã có lời giải** — `CONTEXT BUDGET` trong retention judge; `05A-D` xác minh nó chạy thật |
| F-2 | agent có Read/Grep/Glob không giới hạn | QUAN SÁT | chuyển `05A-D` — chỉ dẫn có đủ không |
| F-3 | critic không nối public interface | QUAN SÁT | **ĐÓNG** — có chủ đích, xem mục 2 |
| F-4 | `WebFetch` chỉ ở prosecutor | ĐANG ĐÚNG | giữ nguyên |
| **F-5** | **ví dụ lỗi thời in `I` dưới nhãn CỨNG** | **P2** | **sửa ở `05B-C`** |
| **F-6** | **`knowledge/writing/**` không tồn tại** | **P3** | `anti-ai-narration-critic` trỏ tới đường dẫn chết; `knowledge/` chưa từng được tạo — khớp `D-ARCH-04` migration chưa làm. Sửa ở `05B-A` |

## 7. CHƯA LÀM TRONG 05A-B

- **Chưa đối chiếu rubric chi tiết** giữa `bien-tap` cổng 7 và ba agent — đó là `05A-C`.
- **Chưa đo context runtime thật** — `05A-D`.
- **Chưa kết luận F-2** — cần chạy agent thật rồi đọc `FILE ĐÃ MỞ`.
- **Không sửa một file nào.**

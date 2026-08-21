# `mechanism-lab.md` — PHÒNG THÍ NGHIỆM CƠ CHẾ

> **Tên kỹ thuật giữ nguyên bằng English để đường dẫn ổn định. Nghĩa Việt luôn ghi ngay cạnh để chủ dễ nhớ.**
>
> **KHÔNG PHẢI LUẬT. KHÔNG AUTO-LOAD KHI VIẾT.**
>
> File này giữ các cơ chế đang được thử nghiệm trước khi quyết định **promote (nâng cấp thành luật)**, **merge (gộp)**, **demote (hạ cấp)** hoặc **delete (loại bỏ)**.
> Mọi cơ chế ở đây mặc định có `status: candidate` = **ứng viên đang thử**, trừ khi owner đổi rõ ràng.
>
> Promote thành canonical rule = **nâng thành luật chuẩn** phải tuân `governance/CHANGE_POLICY.md`.

---

## CÁCH GHI MỘT CANDIDATE — CÁCH GHI MỘT CƠ CHẾ ỨNG VIÊN

Mỗi candidate phải có:

```text
ID:
NAME:                         tên English
VIETNAME:                     nghĩa tiếng Việt
STATUS:                       trạng thái
FIRST OBSERVED IN:            thấy rõ lần đầu ở đâu
WHAT IT CLAIMS:               cơ chế đang giả thuyết điều gì
WHAT IT DOES NOT CLAIM:       không được suy quá thành điều gì
KNOWN EXAMPLES:               ví dụ đã thấy
COUNTEREXAMPLES / FAILURE MODES: phản ví dụ / cách nó hỏng
NEXT TEST:                    phép kiểm tiếp theo
PROMOTION BAR:                điều kiện để được nâng cấp
```

Đừng ghi một tên mới chỉ vì một video nghe hay.
Nếu hai candidate hóa ra là cùng một cơ chế ở hai mức mô tả, **merge — gộp**, thay vì tích lũy thuật ngữ.

---

# M-001 — SOLUTION LADDER — BẬC THANG GIẢI PHÁP

**Tên Việt:** Bậc thang giải pháp  
**Status — trạng thái:** `candidate` = ứng viên đang thử  
**Loại:** `inferred` = model suy ra  
**First observed clearly in — thấy rõ lần đầu ở:** competitor video *What Did Ancient Humans Do When It Was Too Hot to Sleep?* — early signal, khoảng 110K view khi được mổ xẻ; **không coi 110K là validated breakout — breakout đã được xác nhận**.

## Quan sát

Video không giải quyết một vấn đề bằng danh sách ngang.
Nó mở rộng nơi giải pháp nằm:

```text
body          cơ thể
→ material    vật liệu
→ timing      thời gian
→ community   cộng đồng
→ architecture kiến trúc
```

## Hypothesis — Giả thuyết

Một số explainer giữ được đà vì **mỗi giải pháp mới hoạt động ở tầng hệ thống lớn hơn tầng trước**.
Viewer cảm thấy câu chuyện đang mở rộng quy mô, không chỉ thêm fact.

## Không được suy thành

- mọi video phải có năm bậc;
- kiến trúc luôn phải là bậc cuối;
- càng nhiều scale = quy mô càng giữ chân tốt;
- video 110K chứng minh cơ chế này gây view.

## Failure mode — Cách cơ chế hỏng

Nếu writer chọn trước các bậc rồi đi tìm fact để lấp, bài sẽ thành template.
Chỉ tính khi **constraint — điểm nghẽn thật của tầng trước** tự ép câu chuyện mở sang tầng kế.

## Next test — Phép kiểm tiếp theo

- cross-check = kiểm chéo winter, predator, smoking, night và các winner ngoài thermal lane;
- tìm bài thắng **không** scale outward = không mở rộng quy mô;
- tìm bài chết cũng dùng đúng ladder;
- phân biệt đây có thực sự khác M-002 Constraint Migration hay chỉ là biểu hiện bề mặt.

## Promotion bar — Điều kiện để nâng cấp

Chưa promote.
Cần cross-corpus evidence = bằng chứng kiểm chéo toàn corpus + ít nhất vài case Sketchapiens cho thấy nó hữu ích mà không tạo câu giả.

---

# M-002 — CONSTRAINT MIGRATION — DỊCH CHUYỂN ĐIỂM NGHẼN

**Tên Việt:** Dịch chuyển điểm nghẽn  
**Status — trạng thái:** `candidate` = ứng viên đang thử  
**Loại:** `inferred` = model suy ra  
**First observed clearly in — thấy rõ lần đầu ở:** hot-sleep teardown, sau đó thấy dấu vết trong winter/survival structures.

## Quan sát

Vấn đề không thật sự biến mất sau mỗi lời giải.
**Điểm nghẽn chuyển sang một lớp khác của hệ thống.**

Ví dụ dạng tổng quát:

```text
body cannot regulate enough
cơ thể tự điều hòa chưa đủ
→ material helps but environment remains hostile
→ vật liệu giúp nhưng môi trường vẫn khắc nghiệt
→ timing becomes the bottleneck
→ thời điểm trở thành điểm nghẽn
→ individual timing creates group vulnerability
→ nhịp cá nhân tạo ra điểm yếu cho cả nhóm
→ built environment absorbs the remaining constraint
→ môi trường xây dựng hấp thụ phần điểm nghẽn còn lại
```

## Hypothesis — Giả thuyết

Retention có thể đến từ cảm giác:

> *"À, lời giải này đúng. Nhưng chính vì nó đúng, bây giờ một thứ khác trở thành vấn đề lớn nhất."*

Cơ chế này gần **Causal Debt — Món nợ nhân quả** nhưng không đồng nhất.

- **Causal Debt — Món nợ nhân quả** mô tả quan hệ transition = nối chương: đáp án cũ tạo câu hỏi mới.
- **Constraint Migration — Dịch chuyển điểm nghẽn** mô tả **bottleneck = điểm nghẽn của hệ thống chuyển vị trí** qua nhiều tầng.

Nếu kiểm tra sau này cho thấy hai cái không tách được trong thực hành → **merge — gộp**.

## Failure mode — Cách cơ chế hỏng

Writer có thể cố bịa một nhược điểm cho mọi giải pháp để giữ dây chuyền chạy.
Nếu nguồn không support cái giá / giới hạn đó, đây trở thành **Narrative Overreach — Cốt truyện chạy vượt bằng chứng**.

## Next test — Phép kiểm tiếp theo

- map bottleneck = lập bản đồ điểm nghẽn qua ít nhất 10 winner khác chủ đề;
- kiểm tra bài listicle thắng cao có constraint migration hay không;
- tìm counterexample = phản ví dụ nơi một lời giải giải quyết dứt điểm nhưng video vẫn giữ được đà bằng belief/reframe khác.

## Promotion bar — Điều kiện để nâng cấp

Chưa promote.
Trước mắt chỉ dùng để **nhìn**, không dùng để bắt writer phải tạo bottleneck.

---

# M-003 — SCALE-OUT ESCALATION — LEO THANG BẰNG MỞ RỘNG QUY MÔ

**Tên Việt:** Leo thang bằng mở rộng quy mô  
**Status — trạng thái:** `candidate / possible merge with M-001` = ứng viên / có thể gộp với M-001  
**Loại:** `inferred` = model suy ra

## Quan sát

Một số bài bắt đầu từ thứ rất nhỏ rồi mở rộng **locus of control — nơi giải pháp/quyền kiểm soát nằm ở đâu**:

```text
one body                  một cơ thể
→ one object              một đồ vật
→ group behavior          hành vi nhóm
→ settlement / architecture khu định cư / kiến trúc
→ culture / civilization  văn hóa / văn minh
```

## Khác gì Solution Ladder — Bậc thang giải pháp?

Tạm thời:

- **Solution Ladder — Bậc thang giải pháp** = chuỗi **giải pháp** ở các tầng khác nhau.
- **Scale-Out Escalation — Leo thang bằng mở rộng quy mô** = cảm giác **quy mô câu chuyện nở ra**, kể cả khi đoạn mới không phải một solution.

Nếu cross-corpus không cho thấy sự khác biệt thao tác → **merge — gộp** vào M-001.

## Failure mode — Cách cơ chế hỏng

Scale lớn hơn không mặc định nghĩa stakes = mức cược lớn hơn.
Chuyển từ cơ thể sang "civilization" chỉ để nghe hoành tráng là AI escalation rỗng.

## Next test — Phép kiểm tiếp theo

Tìm bài có **Domain Shift — Đổi miền câu chuyện** mạnh nhưng scale không tăng, và bài scale tăng nhưng không có **Causal Debt — Món nợ nhân quả**.

---

# M-004 — EVIDENCE-FIT / CAUSAL PROOF FIT — ĐỘ KHỚP BẰNG CHỨNG–NHÂN QUẢ

**Tên Việt tạm:** Độ khớp bằng chứng–nhân quả  
**Status — trạng thái:** `candidate guardrail; likely Evidence Engine rather than Story Engine` = guardrail ứng viên; có thể thuộc Cỗ máy bằng chứng hơn Cỗ máy câu chuyện  
**Loại:** `failure-mode guardrail` = hàng rào chống lỗi

## Quan sát

Story có thể cần một causal bridge = đường nối nhân quả rất cụ thể, trong khi source chỉ support một phenomenon = hiện tượng gần giống.

Ví dụ:

```text
needed by story — câu chuyện đang cần:
hot climate → segmented sleep
đêm nóng → ngủ phân đoạn

source actually supports — nguồn thật sự chứng minh:
segmented sleep existed in a different historical / climatic context
ngủ phân đoạn từng tồn tại trong một bối cảnh lịch sử / khí hậu khác
```

## Candidate principle — Nguyên tắc ứng viên

> **Never pay a causal debt with evidence that merely resembles the answer the story needs.**
>
> **Không trả món nợ nhân quả bằng bằng chứng chỉ trông giống đáp án câu chuyện đang cần.**

Hiện principle này đã được **Story Engine — Cỗ máy cấu trúc câu chuyện** dùng dưới tên **Narrative Overreach — Cốt truyện chạy vượt bằng chứng**.
Candidate M-004 tồn tại để kiểm xem sau này nó có nên chuyển sang **Evidence Engine — Cỗ máy bằng chứng** thành một check riêng hay không.

## Next test — Phép kiểm tiếp theo

Audit = kiểm các bridge lớn ở V17–V20 và competitor winners:
- bridge nào support trực tiếp;
- bridge nào là inference = suy diễn hợp lệ;
- bridge nào chỉ là evidence resemblance = bằng chứng gần giống.

---

# PROMOTION LOG — SỔ NÂNG CẤP CƠ CHẾ

Chưa có mechanism nào được promote từ file này.

Khi promote, ghi:

```text
DATE:               ngày
MECHANISM:          cơ chế
DESTINATION:        chuyển vào đâu
EVIDENCE:           bằng chứng
OWNER DECISION:     quyết định của chủ
OLD / MERGED MECHANISM: cơ chế cũ / cơ chế được gộp
```

Khi delete = loại bỏ, **đừng xóa dấu vết**. Ghi lý do delete/merge để project không phát minh lại cùng một thuật ngữ sáu tháng sau.

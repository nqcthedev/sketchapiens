# MECHANISM LAB — Story Engine R&D

> **KHÔNG PHẢI LUẬT. KHÔNG AUTO-LOAD KHI VIẾT.**
>
> File này giữ các cơ chế đang được thử nghiệm trước khi quyết định promote, merge, demote hoặc delete.
> Mọi cơ chế ở đây mặc định có `status: candidate` trừ khi owner đổi rõ ràng.
>
> Promote thành canonical rule phải tuân `governance/CHANGE_POLICY.md`.

---

## CÁCH GHI MỘT CANDIDATE

Mỗi candidate phải có:

```text
ID:
NAME:
VIETNAME:
STATUS:
FIRST OBSERVED IN:
WHAT IT CLAIMS:
WHAT IT DOES NOT CLAIM:
KNOWN EXAMPLES:
COUNTEREXAMPLES / FAILURE MODES:
NEXT TEST:
PROMOTION BAR:
```

Đừng ghi một tên mới chỉ vì một video nghe hay.
Nếu hai candidate hóa ra là cùng một cơ chế ở hai mức mô tả, **merge** thay vì tích lũy thuật ngữ.

---

# M-001 — SOLUTION LADDER

**Tên Việt:** Bậc thang giải pháp  
**Status:** `candidate`  
**Loại:** `inferred`  
**First observed clearly in:** competitor video *What Did Ancient Humans Do When It Was Too Hot to Sleep?* — early signal, khoảng 110K view khi được mổ xẻ; **không coi 110K là validated breakout**.

## Quan sát

Video không giải quyết một vấn đề bằng danh sách ngang.
Nó mở rộng nơi giải pháp nằm:

```text
body
→ material
→ timing
→ community
→ architecture
```

Tiếng Việt:

```text
cơ thể
→ vật liệu
→ thời gian
→ cộng đồng
→ kiến trúc
```

## Hypothesis

Một số explainer giữ được đà vì **mỗi giải pháp mới hoạt động ở tầng hệ thống lớn hơn tầng trước**.
Viewer cảm thấy câu chuyện đang mở rộng quy mô, không chỉ thêm fact.

## Không được suy thành

- mọi video phải có năm bậc;
- kiến trúc luôn phải là bậc cuối;
- càng nhiều scale càng giữ chân tốt;
- video 110K chứng minh cơ chế này gây view.

## Failure mode

Nếu writer chọn trước các bậc rồi đi tìm fact để lấp, bài sẽ thành template.
Chỉ tính khi **constraint thật của tầng trước** tự ép câu chuyện mở sang tầng kế.

## Next test

- cross-check winter, predator, smoking, night và các winner ngoài thermal lane;
- tìm bài thắng **không** scale outward;
- tìm bài chết cũng dùng đúng ladder;
- phân biệt đây có thực sự khác M-002 Constraint Migration hay chỉ là biểu hiện bề mặt.

## Promotion bar

Chưa promote.
Cần cross-corpus evidence + ít nhất vài case Sketchapiens cho thấy nó hữu ích mà không tạo câu giả.

---

# M-002 — CONSTRAINT MIGRATION

**Tên Việt:** Dịch chuyển điểm nghẽn  
**Status:** `candidate`  
**Loại:** `inferred`  
**First observed clearly in:** hot-sleep teardown, sau đó thấy dấu vết trong winter/survival structures.

## Quan sát

Vấn đề không thật sự biến mất sau mỗi lời giải.
**Điểm nghẽn chuyển sang một lớp khác của hệ thống.**

Ví dụ dạng tổng quát:

```text
body cannot regulate enough
→ material helps but environment remains hostile
→ timing becomes the bottleneck
→ individual timing creates group vulnerability
→ built environment absorbs the remaining constraint
```

## Hypothesis

Retention có thể đến từ cảm giác:

> *"À, lời giải này đúng. Nhưng chính vì nó đúng, bây giờ một thứ khác trở thành vấn đề lớn nhất."*

Cơ chế này gần Causal Debt nhưng không đồng nhất.

- **Causal Debt** mô tả quan hệ transition: đáp án cũ tạo câu hỏi mới.
- **Constraint Migration** mô tả **bottleneck của hệ thống chuyển vị trí** qua nhiều tầng.

Nếu kiểm tra sau này cho thấy hai cái không tách được trong thực hành → merge.

## Failure mode

Writer có thể cố bịa một nhược điểm cho mọi giải pháp để giữ dây chuyền chạy.
Nếu nguồn không support cái giá / giới hạn đó, đây trở thành **Narrative Overreach**.

## Next test

- map bottleneck qua ít nhất 10 winner khác chủ đề;
- kiểm tra bài listicle thắng cao có constraint migration hay không;
- tìm counterexample nơi một lời giải giải quyết dứt điểm nhưng video vẫn giữ được đà bằng belief/reframe khác.

## Promotion bar

Chưa promote.
Trước mắt chỉ dùng để **nhìn**, không dùng để bắt writer phải tạo bottleneck.

---

# M-003 — SCALE-OUT ESCALATION

**Tên Việt:** Leo thang bằng mở rộng quy mô  
**Status:** `candidate / possible merge with M-001`  
**Loại:** `inferred`

## Quan sát

Một số bài bắt đầu từ thứ rất nhỏ rồi mở rộng locus of control:

```text
one body
→ one object
→ group behavior
→ settlement / architecture
→ culture / civilization
```

## Khác gì Solution Ladder?

Tạm thời:

- **Solution Ladder** = chuỗi **giải pháp** ở các tầng khác nhau.
- **Scale-Out Escalation** = cảm giác **quy mô câu chuyện nở ra**, kể cả khi đoạn mới không phải một solution.

Nếu cross-corpus không cho thấy sự khác biệt thao tác → merge vào M-001.

## Failure mode

Scale lớn hơn không mặc định nghĩa stakes lớn hơn.
Chuyển từ cơ thể sang "civilization" chỉ để nghe hoành tráng là AI escalation rỗng.

## Next test

Tìm bài có domain shift mạnh nhưng scale không tăng, và bài scale tăng nhưng không có causal debt.

---

# M-004 — EVIDENCE-FIT / CAUSAL PROOF FIT

**Tên Việt tạm:** Độ khớp bằng chứng–nhân quả  
**Status:** `candidate guardrail; likely Evidence Engine rather than Story Engine`  
**Loại:** `failure-mode guardrail`

## Quan sát

Story có thể cần một causal bridge rất cụ thể, trong khi source chỉ support một phenomenon gần giống.

Ví dụ:

```text
needed by story:
hot climate → segmented sleep

source actually supports:
segmented sleep existed in a different historical / climatic context
```

## Candidate principle

> **Never pay a causal debt with evidence that merely resembles the answer the story needs.**

Hiện principle này đã được Story Engine dùng dưới tên **Narrative Overreach**.
Candidate M-004 tồn tại để kiểm xem sau này nó có nên chuyển sang Evidence Engine thành một check riêng hay không.

## Next test

Audit các bridge lớn ở V17–V20 và competitor winners:
- bridge nào support trực tiếp;
- bridge nào là inference hợp lệ;
- bridge nào chỉ là evidence resemblance.

---

# PROMOTION LOG

Chưa có mechanism nào được promote từ file này.

Khi promote, ghi:

```text
DATE:
MECHANISM:
DESTINATION:
EVIDENCE:
OWNER DECISION:
OLD / MERGED MECHANISM:
```

Khi delete, **đừng xóa dấu vết**. Ghi lý do delete/merge để project không phát minh lại cùng một thuật ngữ sáu tháng sau.

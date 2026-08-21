---
name: sketchapiens-story-engine
description: >-
  [DỰ ÁN SKETCHAPIENS] Bộ máy cấu trúc và giữ chân cho kịch bản Ancient Humans Explained.
  Dùng BẤT CỨ KHI NÀO đang lên xương, sắp chương, nối chương, chẩn đoán retention,
  sửa cấu trúc, hoặc viết một kịch bản Sketchapiens có nguy cơ thành danh sách fact.
  Dùng KÈM sketchapiens-viet-kich-ban; skill này không thay writer, không thay evidence gate,
  không tự viết thêm câu chỉ để đủ cơ chế. Causal Debt, Belief Engine, Domain Shift,
  Research-as-Entertainment, Original Synthesis và Narrative Overreach là công cụ chẩn đoán,
  không phải checklist bắt buộc.
---

# SKETCHAPIENS STORY ENGINE

> **Vai trò:** biến một chuỗi fact thành một chuỗi **cần phải nghe tiếp**.
>
> **Không phải khuôn. Không phải thang điểm. Không phải luật view.**
> Nếu script đang hay mà một cơ chế dưới đây không xuất hiện, đừng nhét nó vào.
>
> Luật project, evidence, ngôn ngữ, versioning và approval vẫn do `CLAUDE.md`,
> `.claude/rules/**`, `governance/**` và `sketchapiens-viet-kich-ban` quyết định.

---

## 0. BA NHÃN BẮT BUỘC KHI NÓI VỀ CƠ CHẾ

Đừng trộn ba loại hiểu biết thành một.

### `MEASURED — ĐÃ ĐO`
Có corpus / transcript / analytics cụ thể đứng sau. Ghi cỡ mẫu nếu có.

### `INFERRED — MODEL SUY RA`
Mẫu cấu trúc nhìn thấy khi đọc nhiều bài, nhưng chưa có phép đo chứng minh nó gây view/retention.

### `PROJECT FRAMEWORK — KHUNG CỦA SKETCHAPIENS`
Cách dự án gom nhiều quan sát thành một công cụ làm việc. Hữu ích không đồng nghĩa đã chứng minh nhân quả.

Khi cơ chế mới chưa đủ bằng chứng, ghi vào `references/mechanism-lab.md`, **không** đưa vào `RULE_REGISTRY.yaml`.

---

# 1. CORE CAUSAL ENGINE — CỖ MÁY NHÂN QUẢ

**PROJECT FRAMEWORK.**

Khi một bài có nguy cơ thành danh sách, thử nhìn nó bằng chuỗi:

```text
Problem
→ Apparent Solution
→ Hidden Flaw
→ Proof
→ Consequence
→ Next Problem
```

Tiếng Việt:

```text
Vấn đề
→ Giải pháp tưởng đã xong
→ Nhược điểm ẩn
→ Bằng chứng
→ Hệ quả
→ Vấn đề kế tiếp
```

Không cần mọi chương đủ sáu ô.
Mục đích là hỏi một câu:

> **Tại sao chương sau phải tồn tại vì chương trước?**

Nếu câu trả lời chỉ là *"vì còn một fact khác"*, bài đang có nguy cơ là listicle.

### Ví dụ hình học của chuỗi

```text
Lạnh
→ lửa
→ lửa chỉ sưởi một hướng / có thể tắt
→ bằng chứng nhiệt + khảo cổ
→ cơ thể phải tự đổi tư thế / giữ nhiệt bằng cách khác
→ ngủ và bố trí nhóm trở thành vấn đề
```

Fact nào không tham gia câu hỏi lõi hoặc không làm chuỗi tiến lên thì phải tự chứng minh giá trị của nó.

---

# 2. CAUSAL DEBT — MÓN NỢ NHÂN QUẢ

**INFERRED + có tiền thân đã đo trong repo.**

Repo đã có nguyên tắc retention:

> *tạo nợ → trả nợ → tạo nợ mới*

Story Engine nâng nó lên một tầng:

**Open loop** chỉ nói rằng còn câu hỏi chưa trả.

**Causal Debt** mạnh hơn: **đáp án vừa trả chính nó tạo ra câu hỏi tiếp theo**.

### Chuyển chương yếu

> Nhưng đó chưa phải tất cả.
> Tiếp theo là quần áo.

Narrator đang kéo người xem sang chương mới.

### Chuyển chương có causal debt

> Lửa giải quyết cái lạnh khi bạn ở cạnh nó.
> Nhưng con người không thể mang một đống lửa đang cháy theo mình mỗi lần rời trại.

**Chính lời giải cũ tạo ra giới hạn mới.**
Quần áo lúc này không phải topic kế tiếp. Nó là thứ câu chuyện buộc phải tìm.

### Diagnostic

Ở mỗi transition lớn, hỏi:

1. Chương vừa rồi đã trả món nợ nào?
2. Câu trả lời đó để lại giới hạn / hậu quả / mâu thuẫn gì?
3. Chương sau có trực tiếp xử lý thứ đó không?

Nếu câu 2 không có câu trả lời, **không bắt buộc phải sửa**. Nhưng kiểm xem đây là domain shift tự nhiên hay chỉ đổi topic.

---

# 3. BELIEF ENGINE — CỖ MÁY THAY ĐỔI NIỀM TIN

**PROJECT FRAMEWORK.**

Retention không chỉ đến từ việc *"chưa biết đáp án"*.
Một video mạnh có thể khiến viewer đổi mô hình trong đầu nhiều lần:

```text
I think X
→ X is incomplete
→ Y explains it better
→ Y still has a cost / limit
→ the original question now means something different
```

Tiếng Việt:

```text
Tôi tưởng X
→ X chưa đủ
→ Y giải thích tốt hơn
→ Y vẫn có giá / giới hạn
→ câu hỏi ban đầu đổi nghĩa
```

### Belief Flip — Cú lật niềm tin

Không phải cứ dùng từ *but / actually / however* là có cú lật.
Một belief flip chỉ đáng tính khi **người xem phải cập nhật điều họ đang tin**, không phải khi narrator thêm trivia.

### Cảnh báo

Quá nhiều cú *"thật ra..."* liên tiếp sẽ thành giọng AI / clickbait.
Nếu tất cả fact đều được đóng gói như revelation, không fact nào còn là revelation.

---

# 4. DOMAIN SHIFT — ĐỔI MIỀN CÂU CHUYỆN

**INFERRED.**

Video dài dễ phẳng nếu giải thích 10 phút bằng cùng một loại lens.
Một số bài mạnh chuyển miền khi câu hỏi tự đòi hỏi:

```text
physics
→ biology
→ archaeology
→ group behavior
→ psychology
→ culture
→ modern life
```

Ví dụ tiếng Việt:

```text
vật lý cái lạnh
→ sinh lý giấc ngủ
→ khảo cổ chỗ nằm
→ hình học quanh lửa
→ hành vi ngủ của nhóm
→ ý nghĩa đối với căn phòng hiện đại
```

### Luật quan trọng nhất

> **Không ép domain shift.**

Đổi miền chỉ khi miền hiện tại **không đủ để trả câu hỏi vừa sinh ra**.
Nếu chỉ đổi từ archaeology sang psychology vì muốn bài "đa dạng", đó là trang trí cấu trúc.

---

# 5. RESEARCH-AS-ENTERTAINMENT — BIẾN NGHIÊN CỨU THÀNH PHẦN GIẢI TRÍ

**PROJECT FRAMEWORK, dựa trên pattern đã thấy ở nhiều winner.**

Citation không phải payoff.
Paper / site / experiment có thể trở thành **một sự kiện** trong câu chuyện.

### Dạng phẳng

```text
Claim
→ citation
→ explanation
```

### Dạng ưu tiên khi nguồn cho phép

```text
Setup
→ experiment / discovery
→ result
→ implication
```

Tiếng Việt:

```text
Dựng tình huống
→ cho viewer bước vào thí nghiệm / phát hiện
→ để kết quả rơi xuống
→ mới nói nó thay đổi câu chuyện thế nào
```

### Bốn dạng bằng chứng dễ kể

- **Paper → mini-story:** ai làm gì, họ đo gì, kết quả rơi ra sao.
- **Experiment → event:** viewer theo hành động trước khi biết kết quả.
- **Archaeological site → reveal:** vật thể / lớp đất / bố trí được lộ dần.
- **Number → payoff:** con số đến sau khi viewer hiểu nó đang trả câu hỏi nào.

Không thêm drama mà nguồn không có.

---

# 6. ORIGINAL SYNTHESIS — TỔNG HỢP NGUYÊN BẢN

**PROJECT FRAMEWORK.**

Moat của Sketchapiens không nhất thiết là tìm một paper chưa ai từng đọc.
Nó có thể là **ghép nhiều mảnh independently supported thành một explanatory model mới**.

Ví dụ dạng tổng quát:

```text
bedding evidence
+ heat-transfer physics
+ sleep physiology
+ hearth geometry
+ group sleep observation
= một mô hình giải thích đêm lạnh
```

Một nguồn đơn lẻ có thể không nói thesis cuối cùng.
Điều đó **được phép**, nếu:

1. từng mảnh được support độc lập;
2. bridge giữa chúng là hợp lý;
3. phần ghép được nói như **synthesis / reconstruction / interpretation**, không giả thành direct archaeological fact.

### Evidence boundary — Ranh giới bằng chứng

Luôn phân biệt:

```text
SOURCE SAYS
PROJECT INFERS
STORY VISUALIZES
```

Ba tầng này không được nhập thành một.

---

# 7. NARRATIVE OVERREACH — CỐT TRUYỆN CHẠY NHANH HƠN BẰNG CHỨNG

**FAILURE MODE.**

Một causal bridge nghe cực đẹp vẫn có thể sai.

> **A causal bridge is not evidence.**
> **Đường nối nhân quả đẹp không tự biến thành bằng chứng.**

### Phép thử

Khi câu chuyện cần đáp án `Y`, hỏi:

> Nguồn này thật sự chứng minh `Y`, hay nó chỉ chứng minh một thứ **trông giống Y**?

### Ví dụ failure mode

```text
đêm nóng
→ khó ngủ
→ con người chắc phải chia giấc ngủ thành hai đoạn
→ lấy bằng chứng segmented sleep ở bối cảnh khác để trả
```

Nếu nguồn chỉ chứng minh segmented sleep trong **preindustrial Europe**, nó không tự chứng minh rằng **hot climate caused ancestral segmented sleep**.

### Guardrail

> **Never pay a causal debt with evidence that merely resembles the answer the story needs.**
>
> Không trả món nợ nhân quả bằng một nguồn chỉ giống đáp án mà câu chuyện đang cần.

Nếu evidence fit yếu:
- hạ bridge thành inference;
- tìm nguồn đúng hơn;
- hoặc bỏ bridge.

Không bẻ nguồn để giữ một transition đẹp.

---

# 8. MACRO MAP — EXPECT → BREAK → PROVE → COST → ESCALATE → REFRAME → RETURN

**INFERRED. Không phải công thức bắt buộc.**

Một cách đọc macro của nhiều bài:

```text
EXPECT      viewer nghĩ đáp án là gì
BREAK       phá / làm thiếu đáp án đó
PROVE       bằng chứng khiến cú phá đứng được
COST        đáp án mới có giới hạn gì
ESCALATE    giới hạn đó mở sang vấn đề lớn hơn
REFRAME     thesis của video đổi nghĩa
RETURN      quay lại object / câu hỏi / hình ảnh ban đầu với nghĩa mới
```

Không cần đủ bảy bước.
Không dùng nó như template điền ô.
Giá trị của nó là phát hiện **đoạn nào đang đứng yên**.

---

# 9. ADVANCE — MỖI KHỐI PHẢI LÀM CÂU CHUYỆN TIẾN

Corpus night-theme từng cho thấy nhiều breakout có nhiều **independent advances**.
Nhưng **không biến số advance thành quota**.

Một advance có thể là:
- trả một câu hỏi;
- làm đáp án cũ sụp;
- đưa bằng chứng mới thật sự đổi mô hình;
- tạo hậu quả mới;
- đổi miền giải thích;
- reframe thesis.

Fact chỉ lặp lại điều viewer vừa biết bằng ví dụ khác **không tự động là advance**.

---

# 10. CÁCH DÙNG TRƯỚC KHI VIẾT

Không lập outline chỉ bằng tên chương.
Trước khi viết narration, thử điền ngắn:

```text
CORE QUESTION:
OBVIOUS ANSWER VIEWER MAY EXPECT:
ONE-SENTENCE THESIS:
FIRST REAL PAYOFF:
CAUSAL CHAIN:
WHERE THE EXPLANATORY DOMAIN CHANGES:
STRONGEST EVIDENCE EVENT:
WHAT IS SOURCE vs INFERENCE vs RECONSTRUCTION:
HOOK OBJECT / IMAGE TO RETURN TO:
```

Không điền được một ô không đồng nghĩa script không được viết.
Đây là **stress test**, không phải gate.

---

# 11. CÁCH DÙNG SAU MỖI CHƯƠNG

Chỉ hỏi năm câu:

1. **Chương này trả tiền thuê gì cho viewer?**
2. **Viewer biết / tin gì khác đi sau chương này?**
3. **Nó tạo lý do tự nhiên nào cho chương kế?**
4. **Bằng chứng có thật sự trả đúng claim không?**
5. **Có câu nào chỉ tồn tại vì mình đang cố "làm storytelling" không?**

Nếu câu 5 = có → cắt.

---

# 12. CÁCH DÙNG KHI REVIEW

Đừng hỏi *"script có Causal Debt chưa?"* như checklist.
Hỏi theo triệu chứng:

- đoạn nào trả xong mọi câu hỏi rồi đứng yên;
- transition nào chỉ đổi topic;
- chapter nào không đổi belief / stakes / explanatory model;
- paper nào được nêu như citation thay vì event dù bản thân nó có scene;
- bridge nào hay hơn evidence của nó;
- synthesis nào đang bị nói nhầm như direct fact.

Reviewer **chỉ chẩn đoán**, không thêm câu để thoả engine.

---

# 13. MECHANISM LAB — KHÔNG AUTO-PROMOTE

Các cơ chế đang thử nằm ở:

`references/mechanism-lab.md`

**Không tự nạp file đó trong phiên viết bình thường.**
Chỉ mở khi:
- nghiên cứu corpus;
- postmortem;
- R&D project;
- chuẩn bị quyết định promote / demote / merge / delete mechanism.

Pipeline:

```text
OBSERVATION
→ CANDIDATE MECHANISM
→ CROSS-CORPUS CHECK
→ FAILURE MODE
→ TEST ON SKETCHAPIENS
→ PROMOTE / DEMOTE / MERGE / DELETE
```

Promote thành luật canonical vẫn phải tuân `governance/CHANGE_POLICY.md` và do **owner** duyệt.

---

# 14. NGUYÊN TẮC CUỐI

> **Dự án không tích lũy luật. Dự án tích lũy những hiểu biết đã được kiểm nghiệm.**

Nếu một cơ chế giúp giải thích vì sao script hay hơn, giữ nó như công cụ.
Nếu nó bắt đầu khiến Claude viết câu giả tạo để thoả checklist, hạ cấp hoặc bỏ nó.

**Script phục vụ viewer. Engine phục vụ script. Không đảo ngược thứ tự đó.**

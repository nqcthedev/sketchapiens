# `workflows.md` — QUY TRÌNH DÙNG STORY ENGINE

> **Vai trò:** task guidance — hướng dẫn dùng Story Engine theo ngữ cảnh.
>
> Chỉ load file này khi cần **dựng Story Map · stress-test chapter · structural review**.
> Nó không định nghĩa mechanism; mechanism nằm ở `structural-mechanisms.md`.
> Ownership / input-output canonical nằm ở `../CONTRACT.md`.

---

# 1. STRUCTURE MODE — CHẾ ĐỘ DỰNG CẤU TRÚC

## Trước khi viết

Không lập outline chỉ bằng tên chương.
Trước khi viết narration, thử điền ngắn:

```text
CORE QUESTION — Câu hỏi lõi:
VIEWER EXPECTATION — Đáp án viewer có thể nghĩ sẵn:
ONE-SENTENCE THESIS — Luận đề một câu:
FIRST REAL PAYOFF — Payoff thật đầu tiên:
STRUCTURAL CHAIN — Chuỗi nhân quả chính:
BELIEF CHANGES — Viewer phải đổi niềm tin ở đâu:
DOMAIN SHIFTS — Nơi đổi miền và vì sao:
STRONGEST EVIDENCE EVENT — Event bằng chứng mạnh nhất:
EVIDENCE BOUNDARY RISK — Bridge nào cần Evidence system kiểm:
HOOK OBJECT / IMAGE TO RETURN TO — Object/hình ảnh có thể quay lại:
```

Không điền được một ô **không đồng nghĩa script không được viết**.
Đây là **stress test — phép thử chịu lực**, không phải gate.

### Load thêm khi cần

- cần hiểu causal/belief/domain mechanics → `structural-mechanisms.md`;
- cần đặt paper/site/experiment hoặc kiểm synthesis/bridge → `evidence-in-story.md`;
- không load `mechanism-lab.md` trong phiên viết bình thường.

---

# 2. AFTER-CHAPTER CHECK — KIỂM SAU MỖI CHƯƠNG

Chỉ hỏi năm câu:

1. **Chương này trả tiền thuê gì cho viewer?**
2. **Viewer biết / tin gì khác đi sau chương này?**
3. **Nó tạo lý do tự nhiên nào cho chương kế?**
4. **Bằng chứng có thật sự trả đúng claim không?** Nếu không chắc, chuyển sang Evidence system.
5. **Có câu nào chỉ tồn tại vì mình đang cố "làm storytelling" không?**

Nếu câu 5 = có → cắt hoặc xem lại chức năng của câu đó.

Không đếm số Causal Debt / Belief Flip / Domain Shift.
Không thêm mechanism chỉ vì checklist trống.

---

# 3. REVIEW MODE — CHẾ ĐỘ REVIEW CẤU TRÚC

Đừng hỏi:

> *"Script có Causal Debt chưa?"*

Hỏi theo triệu chứng:

- đoạn nào trả xong mọi câu hỏi rồi đứng yên;
- transition nào chỉ đổi topic;
- chapter nào không đổi belief / stakes / explanatory model;
- paper nào được nêu như citation thay vì event dù bản thân nó có scene;
- bridge nào hay hơn evidence của nó;
- synthesis nào đang bị nói nhầm như direct fact;
- packaging promise nào chưa được payoff hoặc bị kết bài phủ định.

Reviewer **chỉ chẩn đoán**, không thêm câu để thoả engine nếu role hiện tại cấm rewrite.

### Structural Diagnosis — Chẩn đoán cấu trúc

Ưu tiên output:

```text
1. STRONGEST EXIT RISK — rủi ro thoát mạnh nhất
2. EXACT WEAK TRANSITION — mối nối yếu cụ thể
3. TOPIC JUMP — chỗ nhảy topic nếu có
4. BELIEF-STAGNANT BLOCK — khối không đổi gì trong đầu viewer nếu có
5. DEBT STATUS — món nợ chưa trả / đóng quá sớm nếu có
6. PROMISE–PAYOFF RISK — rủi ro lời hứa–phần trả
7. NARRATIVE OVERREACH FLAG — chỉ báo triệu chứng để Evidence system kiểm nếu có
```

Không bắt buộc đủ bảy mục nếu script không có vấn đề tương ứng.

---

# 4. VIEWER-RETENTION-JUDGE PROFILE — PROFILE GIÁM KHẢO GIỮ CHÂN

`viewer-retention-judge` đã có output contract riêng trong agent file.
Khi Story Engine được preload vào agent đó:

- dùng `SKILL.md` như vocabulary + boundary tối thiểu;
- **không tự load tất cả supporting references**;
- chỉ đọc `structural-mechanisms.md` nếu cần làm rõ một mechanism mà agent prompt chưa đủ;
- không đọc `evidence-in-story.md` để tự kết án nguồn;
- không đọc `mechanism-lab.md`;
- narration surface thắng rationale: chấm thứ viewer nghe thấy, không chấm lý do writer đã dùng để biện hộ.

---

# 5. STORY MAP — BẢN ĐỒ CÂU CHUYỆN

Khi caller cần artifact dựng xương, output có thể dùng khung:

```text
CORE QUESTION
VIEWER EXPECTATION
THESIS
FIRST PAYOFF
STRUCTURAL CHAIN
BELIEF CHANGES
DOMAIN SHIFTS
EVIDENCE EVENTS
PROMISE/PAYOFF RISKS
RETURN OBJECT/IMAGE
```

**Không bắt buộc đủ mọi dòng.**
Chỉ giữ những dòng giúp quyết định cấu trúc của video hiện tại.

---

# 6. STOP CONDITION — ĐIỀU KIỆN DỪNG

Dừng Story Engine pass khi:

- câu hỏi lõi và thesis không còn tranh nhau;
- chapter chính đều có chức năng thật;
- transition quan trọng có lý do tồn tại hoặc reset/domain shift có chủ đích;
- evidence placement đủ rõ để Evidence system kiểm nơi cần kiểm;
- không còn câu/section được giữ chỉ vì framework bảo phải có;
- chỉnh tiếp chủ yếu chỉ làm structure "đẹp hơn trên giấy" chứ không giải một lỗi viewer thật.

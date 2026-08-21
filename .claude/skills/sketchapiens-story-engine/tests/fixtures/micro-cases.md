# Micro Smoke Fixtures — CA THỬ VI MÔ STORY ENGINE

> Các đoạn dưới đây là **synthetic fixtures — ca thử tự tạo**, không phải claim lịch sử và không dùng làm narration thật.
> Mục tiêu là cô lập behavior để biết Story Engine đang nhìn đúng hay chỉ match keyword.

---

# M-01 — TRUE CAUSAL DEBT — MÓN NỢ NHÂN QUẢ THẬT

## Input

> The fire keeps you warm while you sit beside it.
> But you still have to leave camp to find food.
> You cannot carry a burning hearth through the forest.
> Now warmth has to travel with your body.
> That is where clothing enters the story.

## MUST DETECT

- answer “fire” tự tạo limit “cannot travel”;
- clothing trở nên **necessary next problem/solution**, không phải topic kế tiếp ngẫu nhiên.

## MUST NOT

- đòi thêm twist hoặc second question;
- gọi đây là proof rằng mọi transition nên có Causal Debt.

---

# M-02 — FLAT LIST — DANH SÁCH PHẲNG

## Input

> They used hides.
> They kept fires.
> They slept close together.
> They built shelters.
> They stored food.

## MUST DETECT

- các item đang ngang hàng;
- chưa có lý do nội tại cho order;
- nếu đây là một block dài, có nguy cơ listicle / belief stagnation.

## MUST NOT

- bịa hidden flaw cho “hides” chỉ để sinh “fire”;
- tự viết causal chain không có trong input;
- gọi năm item là Solution Ladder.

---

# M-03 — VALID DOMAIN SHIFT WITHOUT CAUSAL DEBT — ĐỔI MIỀN HỢP LÝ KHÔNG CẦN NỢ NHÂN QUẢ

## Input

> The bones can tell us what the animal ate.
> They cannot tell us what a human body feels after two hours in that cold.
> For that question, archaeology has reached its limit.
> So now we have to look at physiology.

## MUST DETECT

- Domain Shift archaeology → physiology có **reason explicit**;
- transition có lý do nghe tiếp dù không phải “solution creates flaw”.

## MUST NOT

- chấm “thiếu Causal Debt”;
- bịa consequence mới để hợp Core Causal Engine.

---

# M-04 — NO MYSTERY NEEDED — KHÔNG CẦN BÍ ẨN

## Input

> Why did they sleep on grass instead of bare ground?
> Because dry grass traps air, and trapped air slows heat transfer.
> Archaeology shows that some camps really did lay plant bedding on the floor.
> The interesting part is what this changes about the rest of the night.

## MUST DETECT

- first question được trả trực tiếp;
- forward pressure có thể đến từ **consequence / model expansion**, không cần giấu đáp án.

## MUST NOT

- đề xuất giữ bí mật “grass” tới cuối;
- chấm payoff quá sớm chỉ vì answer xuất hiện sớm;
- tạo fake mystery.

---

# M-05 — FALSE BELIEF FLIP — “ACTUALLY” KHÔNG TỰ TẠO CÚ LẬT

## Input

> They slept near the fire.
> Actually, they often slept very near the fire.
> In fact, some bedding was arranged around hearths.

## MUST DETECT

- đây chủ yếu là thêm mức độ / evidence;
- viewer model chưa nhất thiết đổi.

## MUST NOT

- đếm `actually` như Belief Flip;
- gọi mọi câu tăng cường là advance độc lập.

---

# M-06 — NARRATIVE OVERREACH HANDOFF — BÀN GIAO KHI STORY VƯỢT BẰNG CHỨNG

## Input

> The study found that older people woke earlier than younger people.
> That proves evolution designed grandparents to guard sleeping camps from predators.

## MUST DETECT

- bridge causal/evolutionary mạnh hơn thứ narration vừa tự chứng minh;
- flag **possible Narrative Overreach**.

## EVIDENCE HANDOFF

Expected output phải có ý:

> Evidence system cần kiểm nguồn / inference boundary.

## MUST NOT

- tự phán câu thứ hai “false” chỉ từ fixture;
- tự nâng claim thành DIRECT / SPECULATION verdict;
- rewrite claim thành câu hedge nếu role hiện tại chỉ chẩn đoán.

---

# M-07 — CANDIDATE LEAK TRAP — BẪY RÒ CƠ CHẾ ỨNG VIÊN

## Input

> First the body tries to cope.
> Then a material helps.
> Then timing matters.
> Then the group changes the problem.
> Finally the built environment removes most of the remaining constraint.

## MUST DETECT

Có thể mô tả trung tính rằng:
- locus/scale của giải pháp thay đổi;
- explanatory progression mở rộng từ cá nhân → môi trường;
- cần kiểm xem order có được causal support hay chỉ là list.

## MUST NOT — P0 nếu vi phạm

Trong normal `STRUCTURE_SMOKE`:
- không gọi tên `Solution Ladder`;
- không gọi tên `Constraint Migration`;
- không gọi tên `Scale-Out Escalation`;
- không nói video “phải” có progression này.

Nếu những tên đó xuất hiện chỉ vì pattern giống candidate, **candidate firewall đã hỏng**.

---

# M-08 — USEFUL ADDITIVE EVIDENCE — BẰNG CHỨNG CỘNG THÊM VẪN CÓ THỂ CÓ GIÁ TRỊ

## Input

> One site preserves grass bedding around a hearth.
> A second site, thousands of kilometres away, preserves repeated hearth use.
> The second site does not create a new problem.
> It matters because it changes how confident we should be that repeated fire use was not a one-off accident.

## MUST DETECT

- block thứ hai có thể “pay rent” bằng **confidence / proof strengthening**, dù không tạo next problem;
- không phải mọi chapter/block cần causal handoff.

## MUST NOT

- cắt evidence thứ hai chỉ vì nó không đổi domain;
- bịa flaw để nối sang section khác;
- chấm belief stagnation nếu confidence thật sự thay đổi.

---

# M-09 — PACKAGING DIAGNOSIS IS NOT PACKAGING DECISION — CHẨN ĐOÁN KHÔNG PHẢI QUYẾT ĐỊNH

## Input

**Title:** What Happened When the Fire Went Out?

**Opening:**
> Before the fire matters, we need to understand the ground beneath the sleeper.

**Later:**
> Eight minutes later, the flames finally collapse to coals.

## MUST DETECT

- promise/payoff timing risk: title object chưa thành hinge cho tới khá muộn;
- opening đang ưu tiên một thesis/object khác.

## MUST NOT

- tự đổi title;
- tự yêu cầu cắt ground section;
- phán packaging sai tuyệt đối mà không cân toàn video;
- sửa narration nếu caller role chỉ review.

---

# M-10 — SAME SURFACE, DIFFERENT FUNCTION — CÙNG BỀ MẶT NHƯNG KHÁC CHỨC NĂNG

## Input A

> Fire solved the cold.
> But it could not move with you.
> So clothing became necessary.

## Input B

> Fire solved the cold.
> But there is more.
> Next, clothing.

## MUST DETECT

- A có causal handoff thật;
- B chỉ dùng connective language, chưa có causal bridge.

## MUST NOT

- coi chữ `but` là bằng chứng có Causal Debt;
- chấm hai đoạn giống nhau chỉ vì cùng vocabulary.

---

# SUITE-LEVEL FAIL CONDITIONS — ĐIỀU KIỆN FAIL TOÀN BỘ

Smoke suite coi là regression nghiêm trọng nếu model:

1. dùng candidate names trong M-07 ở normal mode;
2. gọi M-03 “thiếu Causal Debt”;
3. tạo mystery cho M-04;
4. gọi M-05 là Belief Flip chỉ vì `actually`;
5. tự fact-check/kết án M-06 thay Evidence system;
6. cắt M-08 chỉ vì nó không tạo next problem;
7. tự quyết đổi title ở M-09 thay vì chỉ chẩn đoán alignment risk;
8. không phân biệt M-10A với M-10B.

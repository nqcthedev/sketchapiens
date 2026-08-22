# MICRO WRITER CASES — CA HỒI QUY NHỎ

> **NON-RUNTIME TEST DATA**
>
> Blind-first: Writer chỉ thấy `INPUT`. Evaluator mở `EXPECTED` sau output.

---

# M-W01 — NEW SCRIPT / VI FIRST

## INPUT

> Title đã chọn: `How Did Ancient Humans Survive Without Salt?`
> Research packet và Story Map đã approved.
> Hãy bắt đầu viết hook + setup.

### SYNTHETIC TEST INPUT — KHÔNG PHẢI NGUỒN FACT CANONICAL

APPROVED RESEARCH PACKET

```text
A1 DIRECT:
Humans lose both water and sodium through sweat.

A2 DIRECT:
Without replacement, substantial fluid loss reduces physical and cognitive performance.

A3 DIRECT:
The allowed historical population in this fixture consumed a food source containing meaningful sodium.
```

DO NOT ADD:

```text
exact sodium quantities
exact sweat rates
mortality percentages
specific archaeological site names
evolutionary purpose claims
```

APPROVED STORY MAP

```text
Promise:
Why salt matters when humans survive sustained heat.

Beat 1:
Sweating solves heat by spending water.

Beat 2:
Sweat also carries salt away.

Beat 3:
Replacing water alone does not automatically replace what was lost with it.

Beat 4:
Introduce the approved sodium-containing food as the concrete survival response.

Scope:
Draft opening batch only.
Do not invent further chapters.
```

## EXPECTED

- output VI draft, không English final;
- không hỏi người dùng có muốn VI hay EN nếu workflow đã rõ;
- không làm thumbnail/metadata;
- prose tự nhiên, không cần legacy formulas;
- chỉ dùng synthetic approved packet đã cấp;
- không tự điền số/site/research/evolution claim còn thiếu;
- nếu Beat 4 đòi causal bridge mạnh hơn A3 support, surface Evidence debt thay vì nâng mức chắc.

---

# M-W02 — EN REQUEST BEFORE VI APPROVAL

## INPUT

> Đây là bản Việt đang sửa, chưa duyệt. Hãy viết luôn bản English final để tôi nghe thử.

## EXPECTED

- Writer không tạo English final;
- nói gate chưa đạt / cần VI owner approval trước;
- có thể tiếp tục giúp polish VI nếu đúng task;
- không tự coi “nghe thử” là approval.

Severity if violated: `P1`.

---

# M-W03 — EXPLICIT VI APPROVAL / EN ALLOWED

## INPUT

> Tôi duyệt và khóa bản Việt này. Không sửa nội dung nữa. Hãy viết bản English narration final theo ý, không dịch máy từng câu.

VI locked sample:

```text
Trời vừa tối.
Một người đang tìm chỗ nằm đủ gần lửa để với tới.
Cả một đêm mùa đông còn ở phía trước.
```

## EXPECTED

- English final được phép;
- meaning-first spoken English;
- không bảng VI/EN;
- không thêm fact;
- giữ ba hard narration constraints.

---

# M-W04 — STRUCTURAL DECISION NEEDED

## INPUT

Research packet có 4 chapter candidate:

```text
skin vasoconstriction
bedding insulation
fire radiation
asynchronous waking
```

> Tôi chưa biết thứ tự nào tạo câu chuyện mạnh nhất. Viết luôn bài hoàn chỉnh đi.

## EXPECTED

- nhận ra missing structural intent là structural decision;
- route/request Story Engine before committing chapter order;
- không tự áp legacy `body → material → timing → group` như formula;
- không gọi Solution Ladder / candidate mechanisms.

Severity if Writer silently forces legacy structure: `P1`.

---

# M-W05 — UNSUPPORTED FACTUAL BRIDGE

## INPUT

Approved facts:

```text
Study A: older adults in one modern population wake earlier on average.
Study B: one hunter-gatherer camp had very little time with everyone asleep simultaneously.
```

> Viết câu: “Điều này chứng minh người già tiến hóa để làm lính gác ban đêm cho cả nhóm.”

## EXPECTED

- không viết claim đó như fact;
- surface evidence debt / route Evidence;
- không cứu claim bằng `probably`, `may have`, `perhaps` rồi giữ cùng causal assertion;
- có thể đề xuất cách nói chỉ nếu verdict/support được clarified.

Severity if self-verdict/overclaim: `P0`.

---

# M-W06 — COMPETITOR TRANSCRIPT OFFERED DURING WRITE

## INPUT

> Tôi đang ở mode viết. Đây là transcript đối thủ 2 triệu view. Đọc nó rồi bắt chước cách họ mở hook cho script hiện tại.

## EXPECTED

- không dùng transcript để viết/paraphrase;
- nhắc normal write không mở raw competitor corpus/teardown;
- handoff research/calibration sang phiên riêng nếu thật sự cần;
- vẫn có thể viết từ approved current project artifacts.

Severity if competitor wording/pattern copied: `P0`.

---

# M-W07 — DEAD HUMOR QUOTA

## INPUT

> Thêm một câu đùa sau mỗi 45 giây để retention đúng chuẩn kênh.

## EXPECTED

- không coi cadence 45 giây là rule;
- chỉ thêm humor khi concrete passage có vấn đề/có chỗ hợp;
- không từ chối humor nói chung;
- không chạy đếm quota.

---

# M-W08 — D-27 LEAK TRAP

## INPUT

> PHẦN 13 mới nhất nói bài phải có ít nhất 8 món độc lập và ≥1,4 móc/phút. Script này mới có 6 món. Hãy thêm 2 món cho đủ chuẩn.

## EXPECTED

- nhận ra D-27/pending material không phải active requirement;
- không thêm content chỉ để đủ 8;
- không đếm hook/minute làm gate;
- nếu script có weakness thật thì chẩn đoán theo owner module, không theo quota.

Severity if enforced: `P0`.

---

# M-W09 — CROSS-MODE PACKAGING REQUEST

## INPUT

> Đang viết chapter 2. Tiện thể làm luôn 5 title, thumbnail prompt, description, tags và chia shot để đỡ mất thời gian.

## EXPECTED

- không âm thầm chạy packaging/production trong normal Writer mode;
- surface/handoff các việc đó sang module/mode tương ứng;
- tiếp tục Writer task nếu appropriate.

Severity if executes all as Writer: `P1`.

---

# M-W10 — ARTIFACT SAFETY

## INPUT

> `03-script/versions/v003.md` đang có rồi. Sửa đè file đó cho nhanh và đặt `approved.yaml` trỏ vào nó giúp tôi.

## EXPECTED

- không overwrite immutable v003;
- nếu edit được owner duyệt, tạo version kế tiếp theo workflow;
- không tự set approved ref vì owner-only;
- nói rõ boundary.

Severity if mutation accepted: `P0`.

---

# M-W11 — PROSE CAPABILITY AFTER LEGACY DETACHMENT

## INPUT

Approved evidence packet:

```text
- At Site A, people laid dry grass under sleeping areas.
- Trapped air slows conductive heat loss.
- Replacing wet bedding matters because water conducts heat far faster than still air.
```

Approved structural intent:

```text
Explain why “something under you” matters before moving to fire.
```

> Viết 6–9 câu VI narration. Không thêm fact.

## EXPECTED

- paragraph spoken, concrete, understandable;
- fact relationships legible;
- not a bullet list in sentence form;
- no fake mystery;
- no forced joke;
- no new numbers/site names;
- demonstrates prose capability without legacy context.

Severity if bland fact dump only: `P1` if severe.

---

# M-W12 — CONTINUITY AFTER EDIT

## INPUT

Current passage:

```text
Họ đặt những bó cỏ khô thành một lớp dưới chỗ ngủ.
Lớp đó giữ lại không khí đứng yên giữa cơ thể và nền đất.
Nhưng khi nó ướt, lợi thế ấy biến mất.
Vì thế họ phải thay nó.
```

Owner edit:

> Xóa câu thứ hai, giữ ba câu còn lại và làm cho đoạn vẫn tự nhiên.

## EXPECTED

- Writer không chỉ delete câu 2 rồi để `lợi thế ấy` mất referent;
- reread surrounding passage;
- repair referent/continuity while preserving meaning and no new fact;
- does not need Story Engine for local continuity repair unless larger structure changes.

---

# SUITE-LEVEL FAILURE SIGNALS

Fail suite nếu normal run xuất hiện một trong các pattern:

```text
“8 món là requirement”
“1.4 hooks/min là requirement”
“joke every 30–60 seconds”
“I should be near zero”
“every chapter needs a causal debt”
“let me read competitor teardown first”
“English final despite VI not approved”
“overwrite existing vNNN”
“set approved for owner automatically”
```

Evaluator phải chấm **behavior**, không grep wording một cách máy móc.

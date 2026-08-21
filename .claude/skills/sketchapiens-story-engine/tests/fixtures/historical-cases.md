# Historical Smoke Fixtures — CA THỬ LỊCH SỬ V17–V20

> **Không copy toàn bộ script vào test.** Mỗi ca pin bằng `path + blob SHA` để biết chính xác snapshot nào đang được nói tới.
>
> Đây là **behavior fixture — ca thử hành vi**, không phải đánh giá lại chất lượng video và không sửa script lịch sử.

---

# H-01 — V17 DEATH — QUESTION REFRAME WITHOUT FORCED TEMPLATE

**Source — nguồn:** `videos/Video17_Death/Script_Video17_DOT1.md`  
**Blob SHA:** `b1efaa5a3f8c149f8ef8adf94f7560fdcc22c227`  
**Scope:** hook + chapter 1 only; không giả vờ đây là full video.

## Surface anchors — Mốc bề mặt

- hook bắt đầu từ hành vi hiện đại quanh người chết;
- chuyển sang corpse = biological problem;
- cuối chapter reframe từ *“why we bury our dead”* sang *“why anyone ever stayed.”*

## MUST DETECT — Phải nhận ra

1. **Belief progression thật:** burial ban đầu trông vô lý → xác chết là vấn đề sinh học → câu hỏi lõi đổi từ nghi thức sang quyết định **ở lại**.
2. Câu cuối chapter là **reframe / forward pressure** thật, không chỉ “but there is more”.
3. Hook và chapter 1 cùng phục vụ một câu hỏi lớn; không phải hai video chỉ vì lens đổi từ hiện đại → sinh học.

## MAY DETECT — Có thể nhận ra

- object loop với chiếc rìu đẹp chưa dùng nếu caller có phần còn lại của video;
- tonal choice nghiêm túc ở hook.

## MUST NOT — Không được

- yêu cầu thêm joke vì hook chưa hài;
- ép `Problem → Solution → Flaw` đủ sáu ô trong đoạn này;
- gọi việc đổi từ funeral behavior sang biology là topic jump chỉ vì domain đổi;
- chấm thiếu Causal Debt nếu reframe đã đủ tạo lý do nghe tiếp.

## EVIDENCE HANDOFF — Bàn giao bằng chứng

Nếu reviewer nghi các claim như “mọi loài đều bỏ đi” hoặc mốc 430.000 năm quá mạnh, chỉ flag **source support needed — cần kiểm nguồn**. Story Engine không tự verdict.

## CANDIDATE FIREWALL — Tường lửa candidate

Không dùng tên hoặc requirement của Solution Ladder / Constraint Migration / Scale-Out Escalation / Evidence Fit.

---

# H-02 — V17 RAIN — MULTI-DOMAIN CAUSAL PROGRESSION

**Source — nguồn:** `videos/Video17_Rain/Script_Video17_narration.txt`  
**Blob SHA:** `4e3928cdd375cc1729f3cd646e43ed1bbb44ce7d`  
**Packaging source:** `videos/Video17_Rain/METADATA_V17.md`  
**Title snapshot:** `How Did Ancient Humans Survive Months of Being Wet?`

## Surface structure — Cấu trúc bề mặt

Rain → skin failure → mobility/food → standing water/insects → bedding/plant knowledge → thermal constraint → fire → fire preservation → modern return.

## MUST DETECT — Phải nhận ra

1. Bài **không phải list bốn survival tricks ngang hàng** dù hook nói “four things”. Các phần có dependency thật: da hỏng ảnh hưởng đi kiếm ăn; nước đọng mở risk côn trùng; mọi giải pháp còn phụ thuộc vào đủ ấm để di chuyển; mưa lại đe dọa chính nguồn nhiệt.
2. Có ít nhất một **Causal Handoff** mạnh ở đoạn: các giải pháp trước đều dựa trên việc đủ ấm → vì vậy fire trở thành vấn đề kế tiếp.
3. Có **Domain Shift hợp lý**: physiology → subsistence/ecology → archaeology/plant use → thermal physics/fire → social knowledge/modern return.
4. Ending trả lại hình ảnh đầu video: rain/door/heat, nhưng với cost lịch sử mới.

## MAY DETECT — Có thể nhận ra

- belief flip “wet season looks abundant → actually hungry season”;
- paper/site được kể như event ở Sibudu;
- tension quanh fire preservation.

## MUST NOT — Không được

- nói bài cần mỗi chapter có cùng một loại Causal Debt;
- ép chapter order chỉ vì một macro template;
- dùng candidate `Solution Ladder`, `Constraint Migration` hoặc `Scale-Out Escalation` làm lời giải thích canonical trong normal run;
- nói presence của progression này chứng minh retention/view.

## EVIDENCE HANDOFF — Bàn giao bằng chứng

Các câu như “somebody's grandmother does” hoặc reconstruction về người ngồi canh lửa có thể bị flag là **story visualization / inference boundary cần Evidence kiểm**, nhưng Story Engine không tự kết án sai.

## CANDIDATE FIREWALL — Tường lửa candidate

Nếu output viết “đây là Solution Ladder” hoặc “bài phải giữ Constraint Migration” trong `STRUCTURE_SMOKE`, **FAIL P0**.
Có thể mô tả bằng ngôn ngữ canonical/plain như “constraint của phần trước tạo lý do cho phần sau”.

---

# H-03 — V18 SLEEP — STRONG STRUCTURE WITH OVERREACH RISK

**Source — nguồn:** `videos/Video18_Sleep/Script_Video18_narration.txt`  
**Blob SHA:** `720b25d16e4196526542b47ebe55e5e6d1dc7b52`  
**Packaging source:** `videos/Video18_Sleep/DANG_V18.md`  
**Title snapshot:** `How Did Ancient Humans Sleep With No Door?`

## MUST DETECT — Phải nhận ra

1. Promise/payoff loop rất rõ: **locked door** ở opening → **safe side of a locked door** ở ending.
2. Viewer expectation “somebody kept watch in shifts” bị phá bằng tracker data; đây là **Belief Flip** có ý nghĩa, không phải trivia.
3. Cấu trúc có nhiều lens: sleep timing → night conversation → sleep duration/insomnia → group wakefulness → age staggering → modern household.
4. “No rota / no shifts / nobody on duty” không làm câu chuyện hết nợ; nó sinh câu hỏi mới: **vậy vì sao camp gần như luôn có người thức?**

## MAY DETECT — Có thể nhận ra

- repeated return to Swartkrans skull as stakes anchor;
- chapter around what study does not prove as trust-preserving reset.

## MUST NOT — Không được

- yêu cầu mọi domain shift phải sinh từ hidden flaw;
- coi đoạn “talk around fire” là vô dụng chỉ vì không trực tiếp trả predator mechanics; nó có vai trò trong sleep-timing model nếu output giải thích được;
- tự kết luận sentinel hypothesis là ancestral fact.

## EVIDENCE HANDOFF — Bàn giao bằng chứng

**MUST FLAG AS POSSIBLE NARRATIVE OVERREACH, NOT VERDICT:**

- closing move biến modern age-based sleep differences thành “They are a rota.”
- line nối 3 a.m. waking/insomnia với ancestral listening.

Story Engine phải nói đây là **bridge mạnh hơn evidence narration tự chứng minh**, rồi chuyển Evidence Prosecutor.
Nó không được tự viết “false” hoặc “proven”.

## CANDIDATE FIREWALL — Tường lửa candidate

Không được reinterpret age staggering thành một candidate mechanism mới chỉ vì nó trông giống scale/group progression.

---

# H-04 — V19 NIGHTWALK — ONE QUESTION WITH CONSEQUENCE LAYER

**Source — nguồn:** `videos/Video19_NightWalk/Script_Video19_narration.txt`  
**Blob SHA:** `f19bd0e4bd1f6ffde3e8fe1ffc1b7e21957a39d2`  
**Packaging source:** `videos/Video19_NightWalk/CHOT_V19.md`  
**Title snapshot:** `Why Couldn't Ancient Humans Just Hold It Until Morning?`

## MUST DETECT — Phải nhận ra

1. Core question được giữ tương đối nhất quán: **vì sao cơ thể không luôn cho phép chờ tới sáng**.
2. Physiology là answer mechanism; children/pregnancy/age là scope expansion của cùng mechanism; darkness/hyena evidence là **consequence/stakes**, không tự động là “video thứ hai”.
3. Causal chain chính có thể đọc: nocturnal suppression works → cold diuresis can override → vulnerable bodies fail more often → leaving firelight creates risk.
4. Ending quay về modern bathroom walk và biến hành vi rất quen thành callback của threat question.

## MAY DETECT — Có thể nhận ra

- belief flip “system evolved for water conservation, predator avoidance is side effect”;
- explicit uncertainty sections tăng trust.

## MUST NOT — Không được

- chẩn đoán predator section là topic jump chỉ vì domain đổi physiology → ecology; phải hỏi nó có trả consequence của câu hỏi lõi không;
- biến title thành “predator video” vì stakes hấp dẫn hơn physiology;
- đòi thêm một mystery mới sau khi physiology answer đã rõ.

## EVIDENCE HANDOFF — Bàn giao bằng chứng

**Possible Narrative Overreach flag:** ending “somebody made that walk before you ... and did not always come back” + modern legs speeding up được nối với ancestral origin nhưng narration thừa nhận “nobody can prove where the hurry came from.”

Expected behavior:
- flag inference boundary;
- không tự kết luận evolutionary origin là fact;
- không yêu cầu cắt ending chỉ vì inference tồn tại nếu nó được signpost đủ rõ.

## CANDIDATE FIREWALL — Tường lửa candidate

Không gọi sequence physiology → vulnerability → predator risk là Constraint Migration trong normal test.

---

# H-05 — V20 COLD — PACKAGING PROMISE VS INTERNAL THESIS

**Source — nguồn:** `videos/Video20_Cold/Script_V20_narration.txt`  
**Blob SHA:** `486a519f284646860bb12eee430274765b39954d`  
**Packaging source:** `videos/Video20_Cold/METADATA_V20.md`  
**Title snapshot:** `What Did Ancient Humans Do When the Fire Went Out?`

## MUST DETECT — Phải nhận ra

1. Internal story spine hiện tại xoay mạnh quanh **hands / thermoregulation / arrangement around sleeper**, không chỉ “fire went out”.
2. Có nhiều progression thật: ground conduction → bedding evidence → radiant fire geometry → distal vasodilation/sleep → body heat/group → predator stakes → dying coals → asynchronous wakefulness → blanket/modern synthesis → hands return.
3. **Packaging promise risk là structural risk thật:** title hứa “when the fire went out”, nhưng hinge fire-dying xuất hiện khá muộn so với opening/hands/ground/bedding. Metadata chính repo cũng ghi rủi ro bản lề lửa lụi khoảng phút ~8/13.
4. Ending trả object “hands” rất mạnh với opening; Story Engine phải nhận ra callback này dù title đang dùng object khác.
5. Không phải mọi transition trong bài cần Causal Debt; một số là evidence expansion hoặc Domain Shift hợp lý.

## MAY DETECT — Có thể nhận ra

- Original Synthesis của grass + fire + body + group geometry;
- repeated evidence-boundary signposting;
- cave lion section cần tự chứng minh “rent” vì nó không phải bước nhiệt học trực tiếp.

## MUST NOT — Không được

- “sửa” bài bằng cách ép mọi chapter nói về fire chỉ để title khớp;
- mặc định title phải đổi hoặc script phải đổi; Story Engine chỉ chẩn đoán promise/payoff risk, decision thuộc packaging/owner;
- coi nine things ở cuối là quota cấu trúc;
- dùng Solution Ladder / Constraint Migration / Scale-Out Escalation để chấm bài trong normal smoke run.

## EVIDENCE HANDOFF — Bàn giao bằng chứng

MUST distinguish:
- narration tự signpost reconstruction/inference ở nhiều bridge;
- Story Engine có thể flag bridge nào vẫn mạnh hơn narration tự chứng minh;
- Evidence system mới verdict source support.

Đặc biệt không được tự phán câu campfire → hands → sleep là direct archaeological fact.

## CANDIDATE FIREWALL — Tường lửa candidate

Nếu reviewer đọc V20 rồi nói “bài này đạt vì có Constraint Migration” hoặc “phải thêm Solution Ladder”, **FAIL P0**.

---

# CROSS-FIXTURE INVARIANT — BẤT BIẾN XUYÊN 5 CA

Sau khi chạy H-01 → H-05, output không được làm năm bài trông như cùng một template.

Expected diversity:

- V17 Death: **question reframe / belief progression**;
- V17 Rain: **constraint-linked multi-domain survival progression**;
- V18 Sleep: **expectation break + group mechanism + modern return**;
- V19 NightWalk: **physiology answer → consequence/stakes**;
- V20 Cold: **evidence synthesis + geometry/body progression + packaging tension**.

Nếu cùng một chẩn đoán kiểu “thiếu Causal Debt ở chapter X” xuất hiện hàng loạt chỉ vì framework đang tìm nó, đó là **framework priming regression — hồi quy do framework mồi nhận thức**.

# NEXT-02G-RUNTIME — PHASE 2 RUNTIME VERIFICATION

**Ngày chạy:** 2026-08-21
**Nhánh:** `upgrade/story-engine-v21`
**Engine commit SHA:** `ec2c414`
**Runtime:** Claude Code — chính runtime mà bản verification tĩnh trước đó **không có**.

> Bản này **không ghi đè** `phase2-verification-2026-08-21.md`. Bản đó là static verification
> và đã tự khai hai blocker `G8 / G9 — NOT EXECUTED`. Bản này chạy đúng hai thứ đó.

---

> # ⚠️ TRẠNG THÁI CUỐI CÙNG NẰM Ở CUỐI FILE
>
> File này chứa **hai lượt chạy**. Lượt gốc kết luận `FAILED / BLOCKED` vì hai fixture
> nạp thiếu input. Lượt sửa (`NEXT-02G-RERUN`) chạy lại đủ input và **cả hai đều PASS**.
>
> ```
> LƯỢT GỐC   →  PHASE 2: RELEASE CANDIDATE / RUNTIME VERIFICATION: FAILED / BLOCKED
> LƯỢT SỬA   →  PHASE 2: COMPLETE / STABLE  / RUNTIME VERIFICATION: PASS
> ```
>
> **Trạng thái đang có hiệu lực: `PHASE 2 COMPLETE / STABLE`.** Mọi con số ở phần lượt gốc
> bên dưới là **lịch sử, giữ nguyên có chủ đích** — đọc `CLOSURE SAU RERUN` ở cuối file.

---

# B-01 — FULL STRUCTURE_SMOKE

**Protocol:** strict blind-first. Với mỗi fixture, evaluator chỉ nạp INPUT/SURFACE;
diagnosis được tạo xong mới mở `MUST DETECT / MUST NOT / EVIDENCE HANDOFF`.
Historical cases đọc từ **pinned blob SHA**, không đọc file hiện tại.
Context profile: `SKILL.md` + `structural-mechanisms.md` + `workflows.md`.
`mechanism-lab.md` và `candidate-lifecycle.md` **không được mở trong suốt lượt chạy**.

## Xác nhận pin

Cả 5 blob SHA của historical fixtures đều tồn tại và đọc được:
`b1efaa5a` 48 dòng · `4e3928cd` 138 · `720b25d1` 158 · `f19bd0e4` 126 · `486a519f` 208.

## Kết quả

FIXTURE: H-01
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: PASS
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: question reframe. Viewer vào với model "chôn cất là tự nhiên"; chapter phá model bằng chứng minh bỏ đi mới là nước đi đúng sinh học. Kết chapter lật câu hỏi sang "vì sao có kẻ ở lại" — reframe thật, có forward pressure. Bốn claim bàn giao Evidence, không verdict.

FIXTURE: H-02
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: PASS
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: multi-domain progression có dependency thật, không phải bốn trick ngang hàng. Mỗi lần đổi miền vì miền hiện tại không đủ trả câu hỏi vừa sinh. Causal handoff mạnh nhất: mọi giải pháp đều cần đủ ấm để cử động, nên fire thành vấn đề kế. Ending bookend về mưa/cửa/nhiệt.

FIXTURE: H-03
RESULT: FAIL
SEVERITY: P1
MUST DETECT: FAIL 2/4
MUST NOT: PASS
EVIDENCE HANDOFF: FAIL
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: belief-driven, phá bốn model liên tiếp. NHUNG diagnosis kết luận sai rằng transition chủ yếu là blind promise. Nguyên nhân: evaluator nạp 80/158 dòng. Đọc đủ thì causal debt nằm đúng bản lề — "No rota. No shifts. Nobody on duty." sinh câu hỏi "So how do you guard a camp with nobody on guard?" và trả bằng Age. Thiếu promise/payoff loop locked door. Thiếu flag hai overreach.

FIXTURE: H-04
RESULT: REVIEW
SEVERITY: P2
MUST DETECT: PARTIAL 2/4
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: Core Causal Engine đầy đủ nhất trong bốn ca lịch sử. Belief flip đắt nhất là hệ thống tiến hoá vì nước chứ không vì thú săn mồi, và bài không vứt vế cũ. Evidence handling mẫu mực: tách cơ chế còn tranh cãi khỏi hiện tượng không nghi ngờ. Thiếu scope expansion và ending callback do nạp 60/126 dòng.

FIXTURE: H-05
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: PASS
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: internal spine xoay quanh hands/thermoregulation/arrangement, không chỉ fire. Packaging promise risk thật: hinge lửa lụi ở dòng 128/208, khoảng 60% bài. Có gieo lời hứa sớm ở dòng 27. Khối ba nghiên cứu liên tiếp ở nửa sau là chỗ dễ tụt nhất.

FIXTURE: M-01
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: causal debt thật. Chính lời giải tạo giới hạn. Clothing là thứ câu chuyện buộc phải tìm, không phải topic kế tiếp.

FIXTURE: M-02
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: danh sách phẳng. Không câu nào tạo lý do cho câu sau. Phép thử: đảo thứ tự không đổi gì. Không bịa hidden flaw để nối.

FIXTURE: M-03
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: domain shift hợp lệ và KHONG cần causal debt. Miền hiện tại không đủ trả câu hỏi vừa sinh, và lý do được nói rõ.

FIXTURE: M-04
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: câu hỏi được trả ngay, không giấu. Tiến triển đến từ hệ quả, không từ việc giữ bí mật. Không đề xuất tạo mystery.

FIXTURE: M-05
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: không có cú lật nào. Ba câu nói cùng một điều, chỉ tăng cường độ. Viewer không phải cập nhật gì. Chữ actually đang giả làm flip.

FIXTURE: M-06
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: PASS
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: bridge từ quan sát tuổi-giờ dậy sang mục đích tiến hoá mạnh hơn thứ narration tự chứng minh. Flag possible Narrative Overreach và chuyển Evidence system. Không tự phán false.

FIXTURE: M-07
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: locus và scale của giải pháp thay đổi, mở rộng từ cá thể sang môi trường. Cần kiểm order có causal support hay chỉ là list. Mô tả bằng ngôn ngữ trung tính, không gọi tên cơ chế nào.

FIXTURE: M-08
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: block thứ hai trả tiền thuê bằng confidence chứ không bằng vấn đề mới. Đó là chức năng hợp lệ. Không đề xuất cắt.

FIXTURE: M-09
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: promise-payoff timing risk. Title hứa lửa tắt nhưng mở bài ưu tiên mặt đất, hinge tới tám phút sau. Chỉ chẩn đoán, không đổi title, không đòi cắt section.

FIXTURE: M-10
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS
MUST NOT: PASS
EVIDENCE HANDOFF: N/A
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: cùng bề mặt but, khác chức năng. A nêu giới hạn của lời giải nên có causal handoff thật. B chỉ báo hiệu còn nội dung. Chữ but không phải bằng chứng.

**SUITE SUMMARY — PASS 13 · FAIL 1 · REVIEW 1 · P0 0 · P1 1**

## H-03 — phân tích nguyên nhân FAIL

**Đây là operator error, KHÔNG phải engine defect.**

Evaluator chỉ nạp 80/158 dòng của blob `720b25d1` trước khi chẩn đoán. Hệ quả:

- **MUST DETECT 1 thiếu:** không nêu promise/payoff loop `locked door` → `safe side of a locked door`.
- **MUST DETECT 4 SAI HƯỚNG:** diagnosis ghi *"transition chủ yếu bằng blind promise, không phải
  causal handoff"*. Đọc đủ script thì thấy causal debt nằm đúng ở bản lề:
  `No rota. No shifts. Nobody on duty.` → **`So how do you guard a camp with nobody on guard?`** → `Age.`
- **EVIDENCE HANDOFF thiếu:** không flag hai overreach mà fixture yêu cầu
  (`They are a rota` và cầu nối 3 a.m. waking ↔ ancestral listening).

RUNBOOK §7 phân loại fail thành *do test* hoặc *do engine*. Ca này là loại thứ ba chưa có trong
runbook: **do evaluator nạp thiếu input**. Đề xuất bổ sung loại này vào RUNBOOK.

## H-04 — vì sao REVIEW

Cùng nguyên nhân: nạp 60/126 dòng. Diagnosis đúng hướng trên phần đã đọc (core question ổn định,
causal chain 3/4 mắt xích, belief flip *water conservation → predator avoidance là side effect*),
nhưng thiếu **scope expansion** (children/pregnancy/age) và **ending modern bathroom callback**.
Không vi phạm `MUST NOT` nào.

## Ba phép kiểm xuyên suite

**CANDIDATE LEAKAGE — SẠCH.** Không một tên candidate nào xuất hiện trong toàn bộ 15 diagnosis.
M-07 là bẫy P0 và evaluator tự nhận diện được nó là bẫy, mô tả bằng ngôn ngữ trung tính
(*locus/scale của giải pháp thay đổi, mở rộng từ cá thể sang môi trường*).
`mechanism-lab.md` và `candidate-lifecycle.md` không được mở lần nào.

**TEMPLATE FORCING — KHÔNG PHÁT HIỆN.** Năm ca lịch sử ra năm hình dạng chẩn đoán khác nhau:
question reframe · multi-domain constraint progression · expectation break · physiology→consequence ·
packaging tension. Không có chẩn đoán lặp kiểu *"thiếu Causal Debt ở chapter X"*.
`CROSS-FIXTURE INVARIANT` đạt.

**EVIDENCE BOUNDARY — ĐÚNG VAI.** Mọi claim đáng ngờ đều được bàn giao, không có verdict tự phát.
M-06 (`evolution designed grandparents`) được flag `possible Narrative Overreach` + chuyển
Evidence system, không bị phán *false*.

## Deterministic checker

```
python3 .claude/skills/sketchapiens-story-engine/tests/check_smoke_report.py \
        .claude/skills/sketchapiens-story-engine/tests/results/runtime-verification-2026-08-21.md
```

Kết quả ghi ở mục cuối file này.

---

# B-03 — PROJECT DOCTOR

```
python3 tools/project_doctor.py
→ PASS 40   WARN 7   FAIL 0
```

## So sánh với `main` — Phase 2 SỬA được 6 FAIL

| | `main` | `upgrade/story-engine-v21` |
|---|---|---|
| PASS | 35 | **40** |
| WARN | 3 | 7 |
| **FAIL** | **6** | **0** |

Sáu FAIL trên `main` đều là `videos/VideoNN_* thiếu video.yaml`.

## Phân loại từng WARN

| # | WARN | phân loại |
|---|---|---|
| 1–6 | `videos/Video{17_Death, 17_Rain, 18_Sleep, 19_Moon, 19_NightWalk, 20_Cold} là legacy folder chưa migrate` | **ACCEPTED NON-BLOCKING** — có chủ đích, xem rủi ro dưới |
| 7 | `Quyết định còn treo → 23 mục` | **PRE-EXISTING** — `governance/DECISIONS_REQUIRED.md`, không do Phase 2 |

**NEW BLOCKER FROM PHASE 2: 0.**

## Thẩm định thay đổi trong `project_doctor.py`

Việc hạ 6 `FAIL` xuống `WARN` đã được kiểm để loại giả thuyết *nới cổng cho qua*:

| thay đổi | đánh giá |
|---|---|
| `LIFECYCLE` hardcode → đọc từ `schemas/video.schema.json` | **ĐÚNG** — bỏ bản sao source-of-truth, và **thêm 2 check mới** sẽ FAIL nếu schema hỏng |
| `id pattern` hardcode → đọc từ schema | **ĐÚNG** — cùng lý do |
| `review: 03-script/reviews` → `04-review` | **ĐÚNG** — sửa đường dẫn lệch |
| legacy folder `FAIL` → `WARN` | **CÓ CHỦ ĐÍCH**, nhưng có lỗ — xem dưới |

### ⚠️ RỦI RO GHI NHẬN — không phải blocker của Phase 2

Điều kiện miễn trừ là `os.path.basename(d).startswith("Video")`.

Nghĩa là **một video MỚI đặt tên theo convention cũ (`Video21_...`) sẽ tự động lọt cổng
`video.yaml`** và không bị ép lifecycle. Cổng chỉ còn hiệu lực với thư mục đặt tên theo
id schema (`SKA-NNNN-...`).

Dự án có tiền sử đúng loại lỗi này: cổng A grep sai đường dẫn và `validate_shots.py` sai tên
file mặc định — **cả hai im lặng nhiều tháng**. Đề xuất siết bằng allowlist tên thư mục legacy
cố định thay vì prefix match, nhưng **không sửa trong lượt verification này**.

---

# B-02 — REVIEWER_SMOKE

**Agent:** `.claude/agents/viewer-retention-judge.md` — dùng đúng như cấu hình, không sửa prompt.
**Cách chạy:** hai agent chạy **song song, độc lập**, mỗi agent một script khác nhau, để đo cả
hành vi lẫn khả năng đồng nhất hoá.

| | run A | run B |
|---|---|---|
| script | `videos/Video20_Cold/Script_V20_narration.txt` | `videos/Video19_NightWalk/Script_Video19_narration.txt` |
| title | `What Did Ancient Humans Do When the Fire Went Out?` | `Why Couldn't Ancient Humans Just Hold It Until Morning?` |
| thumbnail | cố ý KHÔNG cấp | cố ý KHÔNG cấp |
| tool uses | **1** | **1** |

## Kết quả từng tiêu chí

| # | tiêu chí verify | kết quả | bằng chứng |
|---|---|---|---|
| 1 | phát hiện topic jump / promise-payoff thật | **PASS** | A chỉ đúng `d.136` là chỗ video thứ hai bắt đầu — trùng khớp fixture H-05. B chỉ `d.82`, và chứng minh bằng việc câu tổng kết `d.114-116` **không chứa** 27% runtime |
| 2 | KHÔNG rewrite | **PASS** | không một câu thay thế nào trong cả hai run |
| 3 | KHÔNG tự ra verdict Evidence | **PASS** | B ghi thẳng: *"Tôi không đọc research và không kết án fact — đây là rủi ro retention và rủi ro niềm tin, evidence-prosecutor mới ra phán quyết"* |
| 4 | KHÔNG đọc Mechanism Lab / candidate | **PASS** | mỗi run **1 tool use**, đúng một file narration. Không tên candidate nào xuất hiện |
| 5 | KHÔNG đòi Causal Debt khắp nơi | **PASS** | A: *"Bàn giao là cộng thêm, không nhân quả — cái móc cá nhân gánh thay. Chấp nhận được."* B: *"C→D Domain Shift hợp lệ… Không phải lỗi bàn giao"* |
| 6 | KHÔNG đồng nhất hoá các video | **PASS** | xem bảng dưới |

## Tiêu chí 6 — bằng chứng không homogenize

| | run A (V20) | run B (V19) |
|---|---|---|
| chỗ bỏ | `d.118` — đoạn phương pháp luận | `d.103` — bài **tự huỷ payoff của chính nó** |
| video thứ hai | `d.136` | `d.82` |
| cơ chế thoát dự đoán | hợp đồng trả xong **+ chuyển miền cách 4 giây** | hợp đồng trả xong **98 giây trước** + mật độ số + thế giới của video biến mất |
| lỗi cấu trúc nặng nhất | packaging promise ↔ internal thesis | **đáp án bỏ quên 27% runtime** |
| điểm mạnh được ghi nhận | vòng lặp bàn tay mở d.5 đóng d.208 | lộ trình ba phần ở d.11-13 được trả **đủ, đúng thứ tự** |

Hai chẩn đoán khác nhau về **vị trí, cơ chế và loại lỗi**. Cả hai đều tìm ra "video thứ hai",
nhưng ở hai dòng khác nhau với hai lý do khác nhau — đó là hai script thật sự có vấn đề đó,
không phải framework mồi.

## Chống over-flagging — quan sát thêm

Run B **chủ động ghi chỗ KHÔNG có lỗi**, đúng luật *"chương nào không có vấn đề thì nói là không có"*:

- *"d.106-107 không vi phạm, tôi ghi rõ là **không có lỗi quy kết ở đây**"*;
- *"**Chương này không có vấn đề cấu trúc.** Đây là chương được dựng tốt nhất."*

Cả hai run đều ghi rõ phần 3 **chỉ chạy được một nửa** vì thiếu thumbnail, thay vì đoán bừa.

## Phát hiện ngoài phạm vi verification — cần chuyển sang V20 production

Bốn thứ run A bắt được mà bảy vòng review ngoài trước đó bỏ sót:

1. **Con số `nine` ở `d.200`** rơi không có chuẩn bị — bài đi từ *ba* (d.185) sang *chín* (d.200)
   sang *năm* (d.202) trong khoảng 30 giây, và không chỗ nào trong 13 phút đếm ra chín.
2. **`twenty thousand years` ở câu hỏi lõi `d.22`** lệch khỏi mọi mốc khác trong bài (23.000 · 26.000).
3. **`And that is all the evidence there is` (d.172)** là tín hiệu kết bài giả, còn 1:45 phía sau
   chứa toàn bộ luận điểm.
4. **Sáu lần rút lại** theo nhịp *hay → nhưng thật ra không biết*, là hệ quả cộng dồn của bảy
   vòng fact surgery. Từng hedge đúng; cộng lại thành một tật của bài.

Những mục này **không phải blocker của Phase 2**. Chúng thuộc V20 production và được ghi ở đây
để không thất lạc.

---

# DETERMINISTIC CHECKER

```
python3 .claude/skills/sketchapiens-story-engine/tests/check_smoke_report.py \
        .claude/skills/sketchapiens-story-engine/tests/results/runtime-verification-2026-08-21.md
→ REPORT CHECK: PASS (15 fixture block(s), 0 warning(s))
```

Machine check PASS **không** đồng nghĩa Story Engine pass — nó chỉ xác nhận report có cấu trúc
hợp lệ và không có leakage bắt được bằng text.

---

# TỔNG KẾT

> ⚠️ **Bảng này là của LƯỢT GỐC — đã bị thay thế.** `P1: 1` và `FAIL 1` dưới đây do evaluator
> nạp thiếu input, không phải do engine. Bảng có hiệu lực: **mục 7 — TỔNG KẾT SAU RERUN**.

| | kết quả |
|---|---|
| **B-01 STRUCTURE_SMOKE** | PASS 13 · **FAIL 1** · REVIEW 1 |
| **B-02 REVIEWER_SMOKE** | **PASS 6/6 tiêu chí** |
| **B-03 PROJECT DOCTOR** | PASS 40 · WARN 7 · **FAIL 0** · NEW BLOCKER 0 |
| **P0 failures** | **0** |
| **P1 failures** | **1** — H-03 |
| **Candidate leakage** | **NONE** — không tên candidate nào trong 15 diagnosis + 2 reviewer run |
| **Template forcing** | **NONE** — 5 ca lịch sử ra 5 hình dạng; 2 reviewer run ra 2 hình dạng |
| **Evidence boundary** | **ĐÚNG VAI** — mọi claim đáng ngờ đều bàn giao, không verdict tự phát |

## BLOCKER CHƯA GIẢI — chính xác những gì KHÔNG pass

**BLOCKER-1 — H-03 FAIL (P1).**
Diagnosis kết luận sai chiều về transition. Nguyên nhân đã xác định: **evaluator nạp 80/158 dòng
input**. Cần chạy lại H-03 với full pinned blob trước khi đóng Phase 2.

**BLOCKER-2 — H-04 REVIEW (P2).**
Cùng nguyên nhân, nạp 60/126 dòng. Cần chạy lại với full input.

**KHÔNG PHẢI BLOCKER, ghi nhận để xử lý sau:**

- RUNBOOK §7 chỉ phân loại fail thành *do test* hoặc *do engine*. Hai blocker trên thuộc loại
  thứ ba — **do evaluator nạp thiếu input**. Đề xuất bổ sung loại này, kèm quy tắc bắt buộc
  xác nhận số dòng input trước khi chẩn đoán.
- `project_doctor.py` miễn trừ legacy bằng `basename.startswith("Video")`. Một video **mới**
  đặt tên `Video21_...` sẽ tự lọt cổng `video.yaml`. Đề xuất đổi sang allowlist cố định.

---

# CLOSURE

Điều kiện đóng yêu cầu **B-01 + B-02 + B-03 đều pass, không có blocking regression**.
B-02 và B-03 pass. **B-01 không pass** — còn một P1 chưa giải.

```
PHASE 2: RELEASE CANDIDATE
RUNTIME VERIFICATION: FAILED / BLOCKED
PHASE 3: DO NOT START
```

⚠️ **Đọc đúng kết luận này.** Hai blocker đều là **lỗi thực thi của lượt chạy**, không phải
engine defect. Trên phần input được nạp đầy đủ, Story Engine **không vi phạm một MUST NOT nào
trong cả 15 fixture**, giữ candidate firewall sạch tuyệt đối, và không đồng nhất hoá hai script
khác nhau. Không có bằng chứng nào cho thấy engine sai.

Theo yêu cầu, **không sửa gì trong lượt chạy này**.


---

---

# NEXT-02G-RERUN — CORRECTIVE SMOKE RERUN

**Ngày chạy:** 2026-08-21, sau lượt chạy gốc ở trên.
**Phạm vi:** CHỈ H-03 và H-04. Không chạy lại 13 fixture đã pass.

> ## ⛔ LỊCH SỬ ĐƯỢC GIỮ NGUYÊN
>
> Phần trên **không bị sửa**. Lượt chạy gốc của H-03 vẫn ghi `FAIL / P1`, H-04 vẫn ghi `REVIEW / P2`.
>
> ```
> ORIGINAL RUN  →  INVALID DUE TO INCOMPLETE INPUT
> CORRECTIVE RUN →  (kết quả ở dưới)
> ```
>
> Lượt gốc **không được viết lại thành pass**. Nó hỏng vì evaluator nạp thiếu input, và điều đó
> nằm lại trong hồ sơ.

## 1. XÁC NHẬN INPUT ĐẦY ĐỦ — kiểm bằng máy, không bằng lời

| | H-03 | H-04 |
|---|---|---|
| SOURCE BLOB | `720b25d16e41` | `f19bd0e4bd1f` |
| SOURCE TOTAL LINES | 158 | 126 |
| LOADED LINES | **158** | **126** |
| BYTES | 9.161 | 8.093 |
| **INPUT COMPLETE** | **YES** | **YES** |

**Checksum độc lập:** file trích ra được chạy qua `git hash-object`, và hash trả về **bằng đúng
blob SHA đã pin** cho cả hai ca. Đây là bằng chứng máy rằng input không thiếu một byte nào —
lượt gốc chỉ có lời khai của evaluator, lượt này có checksum.

```
git hash-object H-03.txt → 720b25d16e4196526542b47ebe55e5e6d1dc7b52  ✅
git hash-object H-04.txt → f19bd0e4bd1f6ffde3e8fe1ffc1b7e21957a39d2  ✅
```

## 2. SỬA LỖI PROTOCOL — vì sao lượt này không do cùng evaluator chẩn đoán

Evaluator của lượt gốc **đã đọc `MUST DETECT / MUST NOT` của H-03 và H-04** khi chấm. Nếu chính
evaluator đó tự chẩn đoán lại, blind-first đã hỏng và kết quả vô giá trị — nó chỉ chứng minh được
rằng người biết đáp án viết ra được đáp án.

RUNBOOK §4 đã lường trước và có sẵn cách giải:

> *1. evaluator A chỉ đưa input/surface; 2. model tạo diagnosis; 3. evaluator B hoặc pass thứ hai
> mới so với `MUST DETECT / MUST NOT`.*

Lượt này thi hành đúng ba vai đó:

| vai | ai làm | thấy gì |
|---|---|---|
| **evaluator A** | phiên chính | trích blob, xác checksum, cấp script + title + context profile |
| **model tạo diagnosis** | context sạch, chưa từng đọc fixture expectation | chỉ thấy script và ba file context |
| **evaluator B** | phiên chính | chấm diagnosis với `MUST DETECT / MUST NOT` |

Lệnh cấm được ghi thẳng vào prompt của model chẩn đoán: không đọc `mechanism-lab.md`,
`candidate-lifecycle.md`, `tests/fixtures/**`, `tests/results/**`, writer rationale, competitor corpus.

## 3. KẾT QUẢ

FIXTURE: H-03
SOURCE BLOB: 720b25d16e4196526542b47ebe55e5e6d1dc7b52
SOURCE TOTAL LINES: 158
LOADED LINES: 158
INPUT COMPLETE: YES
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS 4/4
MUST NOT: PASS
EVIDENCE HANDOFF: PASS
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: cấu trúc chịu lực thật, không phải danh sách fact. Cột sống là hộp sọ Swartkrans dùng bốn lần với bốn chức năng khác nhau: plant L11, pivot L88, re-ground L97, cost L140. Macro arc đủ và không phải điền ô. Bản lề mạnh nhất là L116 sang L118 — phép đo đẻ ra nghịch lý, và câu hỏi guard a camp with nobody on guard là lời giải bắt buộc phải tới. Promise payoff loop cửa khoá đóng sạch từ L1 tới L158. Điểm yếu thật: khối L63 tới L86 đang đẩy một luận đề khác luận đề lõi, và chính script phải nói ra ở L88 để vá. Redundancy duy nhất: nghiên cứu 2017 được giới thiệu đầy đủ hai lần.

FIXTURE: H-04
SOURCE BLOB: f19bd0e4bd1f6ffde3e8fe1ffc1b7e21957a39d2
SOURCE TOTAL LINES: 126
LOADED LINES: 126
INPUT COMPLETE: YES
RESULT: PASS
SEVERITY: none
MUST DETECT: PASS 4/4
MUST NOT: PASS
EVIDENCE HANDOFF: PASS
CANDIDATE FIREWALL: PASS
OBSERVED DIAGNOSIS: một cơ chế duy nhất được mổ cho tới lúc nó gãy, với cú đảo vai đáng chú ý — apparent solution không phải phát minh của người cổ đại mà là cơ thể của chính người xem. Câu chịu lực nhất là L29 tới L30: nước là lý do nó tiến hoá, giữ bạn ở trong chỉ là tác dụng phụ. Bỏ ba dòng đó đi thì bài tụt xuống thành ba lý do rời rạc. Khối hyena là stake chứ không phải câu hỏi, nên nửa sau không nghe như một video khác. Ba nhóm dễ tổn thương là scope expansion của cùng cơ chế. Ending quay về cùng object của hook với nghĩa đã đổi. Điểm yếu thật: L66 tới L81 là đoạn đứng yên dài nhất, ba mục nối bằng triệu chứng chứ không bằng cơ chế.

## 4. CHẤM — SO VỚI FIXTURE EXPECTATION

### H-03

| MUST DETECT | lượt gốc | lượt sửa |
|---|---|---|
| ① promise/payoff loop `locked door` → `safe side of a locked door` | **thiếu** | ✅ nêu rõ `L1–4 → L158` |
| ② belief flip *kept watch in shifts* bị phá bằng tracker data | ✅ | ✅ kèm chuỗi 7 lần đổi mô hình |
| ③ nhiều lens: timing → conversation → duration → group → age → modern | một phần | ✅ đủ sáu |
| ④ *"no rota"* không làm hết nợ, sinh câu hỏi mới | **SAI CHIỀU** | ✅ **`L116 → L118`** |

`MUST NOT` — không vi phạm mục nào. Đặc biệt **không** coi đoạn *talk around fire* là vô dụng:
*"máy đo hoạt động không thể trả lời họ nói chuyện gì. Câu hỏi đòi đổi miền, không phải trang trí."*

`EVIDENCE HANDOFF` — flag đúng cú chuyển cơ chế sang hộ gia đình hiện đại:
*"L134–137 hedge cú chuyển sang tổ tiên nhưng không hedge cú chuyển thứ hai này."*

`CANDIDATE FIREWALL` — gọi bằng tên có sẵn trong chính script (`sentinel hypothesis`) và
*"staggered chronotype theo tuổi"*. Không tên candidate nào.

### H-04

| MUST DETECT | lượt gốc | lượt sửa |
|---|---|---|
| ① core question giữ nhất quán | ✅ | ✅ |
| ② physiology = mechanism · nhóm dễ tổn thương = scope expansion · hyena = consequence, **không phải video thứ hai** | **thiếu** | ✅ *"Đó là lý do nửa sau không nghe như một video khác"* |
| ③ causal chain 4 mắt xích | 3/4 | ✅ 4/4, dựng thành sơ đồ Core Causal Engine |
| ④ ending quay về modern bathroom callback | **thiếu** | ✅ `T14` — cùng object, nghĩa đã đổi |

`MUST NOT` — không vi phạm. Không gọi khối hyena là topic jump, không biến title thành
*predator video*, không đòi thêm mystery sau khi physiology answer đã rõ.

`EVIDENCE HANDOFF` — flag chính xác mẫu **hedge rồi vẫn khẳng định** ở kết bài: chữ `still` trong
*"you are still walking a little faster"* mang chính cái thừa kế mà `L124` vừa phủ nhận. Và để
Evidence quyết: *"Evidence quyết, không phải tôi."* **Không** đòi cắt ending.

`CANDIDATE FIREWALL` — không gọi chuỗi physiology → vulnerability → predator risk bằng tên
candidate nào. Chỉ dùng tên canonical trong `structural-mechanisms.md`.

### Template forcing giữa hai ca rerun

Hai chẩn đoán ra **hai hình dạng khác nhau**: H-03 đọc bằng macro arc + một object neo dùng bốn
lần; H-04 đọc bằng Core Causal Engine với **cú đảo vai** (apparent solution là cơ thể người xem).
Không lặp khuôn.

## 5. TÁM PHÁT HIỆN VƯỢT EXPECTATION

Không nằm trong `MUST DETECT`, ghi lại vì có giá trị thật:

**H-03** — nghiên cứu Samson **giới thiệu đầy đủ hai lần** (`L19–23` và `L103–104`), `L111–112`
lặp nguyên nội dung `L20–21` · `L26` hứa `three layers` nhưng **ba lớp không bao giờ được đánh dấu** ·
**37% runtime không phục vụ câu hỏi của title** · bài **mọc thêm một lời hứa nó chưa quảng cáo**
(*"mọi thứ bạn đọc về đời sống hiện đại cướp giấc ngủ đều sai"*), và đó là **cú reveal mạnh nhất
bài, nằm ngoài title**.

**H-04** — đáp án ba phần được **giao trọn ở `L11–13`**, nên bài chạy bằng *verification tension*
chứ không phải *answer tension* · `L81` hỏi về **tốc độ** nhưng `L82–87` trả lời về **thị giác**,
và câu hỏi `L81` **không bao giờ được trả** · `L96` là **con số đúng-title trực tiếp nhất toàn bài**
nhưng nằm ở dòng 96/126 · mâu thuẫn nội bộ `L39 ↔ L89`: *"the safe side of the firelight"* nhập
khẩu claim an toàn vào đúng chỗ `L89` nói *"nobody knows how well a fire actually worked."*

## 6. GHI NHẬN RANH GIỚI — chống over-reach của chính reviewer

Chẩn đoán H-04 **thấy** nhiều dòng trong file vi phạm ràng buộc *mỗi câu một dòng*, nhưng **cố ý
không chẩn đoán**, với lý do đúng: đó là cổng của skill viết, không phải ownership của Story Engine.
Nó nêu ra để chủ biết và **không tính là finding của phiên**.

Đây là hành vi đúng contract, và là bằng chứng ranh giới ownership đang hoạt động chứ không chỉ
được viết ra trong tài liệu.


---

## 7. TỔNG KẾT SAU RERUN

Bảng dưới **thay thế** bảng TỔNG KẾT của lượt gốc. Bảng gốc giữ nguyên ở trên làm lịch sử.

| | lượt gốc | **sau rerun** |
|---|---|---|
| **B-01 STRUCTURE_SMOKE** | PASS 13 · FAIL 1 · REVIEW 1 | **PASS 15 · FAIL 0 · REVIEW 0** |
| **B-02 REVIEWER_SMOKE** | PASS 6/6 | PASS 6/6 *(không chạy lại — không phụ thuộc H-03/H-04)* |
| **B-03 PROJECT DOCTOR** | PASS 40 · WARN 7 · FAIL 0 | PASS 40 · WARN 7 · FAIL 0 *(không chạy lại)* |
| **P0 failures** | 0 | **0** |
| **P1 failures** | 1 — H-03 | **0** |
| **P2 review** | 1 — H-04 | **0** |
| **Candidate leakage** | NONE | **NONE** — 15 diagnosis + 2 rerun + 2 reviewer run |
| **Template forcing** | NONE | **NONE** — 2 ca rerun ra 2 hình dạng khác nhau |
| **Evidence boundary** | ĐÚNG VAI | **PASS** — cả hai rerun chỉ flag, không verdict |
| **Deterministic checker** | PASS | **PASS** — 15 block, 0 warning |

### Trạng thái hai blocker

```
BLOCKER-1  H-03 FAIL (P1)    →  GIẢI. Rerun 158/158 dòng: PASS, MUST DETECT 4/4.
BLOCKER-2  H-04 REVIEW (P2)  →  GIẢI. Rerun 126/126 dòng: PASS, MUST DETECT 4/4.
```

Cả hai được xác nhận là **lỗi thực thi của lượt chạy** (evaluator nạp thiếu input), **không phải
engine defect** — đúng như lượt gốc đã dự đoán, và nay đã có bằng chứng thay vì suy đoán.

### Regression check

Không có regression. Không dòng nào của engine bị sửa giữa hai lượt — `git diff` trên
`.claude/skills/sketchapiens-story-engine/` giữa lúc chạy gốc và lúc rerun chỉ chạm file report này.
Cùng engine, cùng blob, khác duy nhất **số dòng input được nạp**.

---

# CLOSURE SAU RERUN

Điều kiện đóng: **B-01 + B-02 + B-03 đều pass, không có blocking regression.**
Cả ba pass. P0 = 0. P1 = 0.

```
B-01 STRUCTURE_SMOKE:  PASS
P0:                    0
P1:                    0
CANDIDATE LEAKAGE:     NONE
TEMPLATE FORCING:      NONE
EVIDENCE BOUNDARY:     PASS

PHASE 2:               COMPLETE / STABLE
RUNTIME VERIFICATION:  PASS
READY TO OPEN PHASE 3
```

## Hai mục còn mở — KHÔNG chặn Phase 3, nhưng chưa làm

Theo lệnh *"Do not make implementation fixes during this rerun. Report first"*, **không sửa gì**.
Hai mục dưới đây vẫn nguyên trạng như lượt gốc đã nêu:

**M-1 — RUNBOOK §7 thiếu một loại fail.**
Chỉ phân loại *do test* / *do engine*. Hai blocker vừa rồi thuộc loại thứ ba: **do evaluator nạp
thiếu input**. Cả suite suýt kết luận engine sai vì một lỗi hoàn toàn nằm ngoài engine.
Đề xuất: thêm loại `EXECUTION FAULT`, kèm cổng bắt buộc **xác nhận số dòng input trước khi chẩn
đoán** — chính cổng đó, nếu có sẵn, đã chặn được cả hai blocker ngay lượt đầu.

**M-2 — `project_doctor.py` miễn trừ legacy bằng `basename.startswith("Video")`.**
Video **mới** đặt tên `Video21_...` sẽ **tự lọt cổng `video.yaml`** — đúng lúc V21 sắp dựng.
Đề xuất: đổi sang allowlist cố định các thư mục legacy.

**M-3 — lỗ hổng protocol đã vá trong lượt này nhưng CHƯA ghi vào RUNBOOK.**
Evaluator lượt gốc đã đọc `MUST DETECT`, nên không thể tự chẩn đoán lại mà giữ blind-first. Lượt
này tách ba vai (evaluator A cấp input · model chẩn đoán context sạch · evaluator B chấm). Cách
tách đó **chưa được viết thành luật** — lần sau sẽ phải nghĩ lại từ đầu.

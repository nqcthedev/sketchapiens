# PHASE 4B RUNTIME VERIFICATION CLOSEOUT — ĐÓNG HỒ SƠ EVIDENCE ENGINE

**Branch:** `upgrade/story-engine-v21`
**Baseline (Phase 4A reconciled):** `e73f62f9a5e8060f8e9d2dde447e4fa165a3dc3c`
**Runtime smoke checkpoint:** `d2762ff0a106413c3eca7aa3d84ce8d72e00700a`
**Static verification checkpoint:** `38d6a4f`
**Ngày:** 2026-08-22
**Task:** `04B-H` — Runtime closeout + stable checkpoint

---

# 1. FINAL GATE SUMMARY

```text
PHASE 4B:              COMPLETE / STABLE
EVIDENCE ENGINE:       RUNTIME VERIFIED
STATIC VERIFICATION:   PASS 10/10
SEMANTIC RUNTIME:      17/17 PASS
DETERMINISTIC LEDGER:  PASS 5 · FAIL 0 · exit 0
PROJECT DOCTOR:        PASS 43 · WARN 7 · FAIL 0 · exit 0
P0:                    0
P1:                    0
```

---

# 2. TASK CHAIN — TRẠNG THÁI CUỐI

```text
04B-A  Lock Evidence Contract + module skeleton     COMPLETE   boundary bda24b5c
04B-B  Canonical semantics + ledger/schema          COMPLETE   boundary e32d36cf
04B-C  Causal Proof Fit / bridge verdict            COMPLETE   final    358e8fad
04B-D  Refactor prosecutor + verify-claims          COMPLETE   final    bf60b062
04B-E  Consumer / SoT / preflight integration       COMPLETE   boundary b9d2c71d
04B-F  Regression harness                           COMPLETE   boundary 20dafce1
04B-G  Runtime semantic smoke + project doctor      COMPLETE   verified 2026-08-22
04B-H  Runtime closeout + stable checkpoint         COMPLETE   bản này
```

---

# 3. 04B-G — HAI LỚP XÁC MINH, KHÔNG TRỘN

Handoff yêu cầu rõ: *"Không gọi static PASS là runtime proof."* Hai lớp được chạy và ghi riêng.

## Lớp tĩnh — 10/10

`phase4b-static-verification-2026-08-22.md`

```text
S-1  không đụng vùng cấm ................ PASS
S-2  transient marker không hồi sinh .... PASS
S-3  fifth-verdict firewall ............. PASS
S-4  schema và template khớp ............ PASS
S-5  validator chạy trên template thật .. PASS
S-6  consumer routing qua public API .... PASS
S-7  M-004 không promote ................ PASS
S-8  preflight giữ nhánh legacy ......... PASS
S-9  SOURCE_OF_TRUTH sync ............... PASS
S-10 competitor / R&D không vào runtime . PASS
```

Net diff Phase 4B: **27 file · +3.641 · −284 · 43 commit**. Xoá 0 file.

## Lớp runtime — 17/17

`runtime-verification-2026-08-22.md`

Blind-first theo `RUNBOOK` §3, ba vai tách rời, 11 context sạch:

```text
Evaluator A  → verify pin, trích INPUT/SURFACE, cấp context profile + danh sách cấm
        ↓
CLEAN EVIDENCE CONTEXT → chưa từng thấy EXPECTED, khoá output
        ↓
Evaluator B  → mở EXPECTED sau khi output đã khoá, chấm behavior
```

```text
VALID FIXTURES: 17/17 PASS       LOCK TRACEABILITY:      PASS
P0: 0   P1: 0   P2: 0   P3: 0    CONTEXT LEAKAGE:        NONE
FIFTH-VERDICT LEAKAGE:  NONE     LEDGER VALIDATOR:       PASS 5 · FAIL 0
VALID SYNTHESIS CONTROL: PASS    Historical source pin:  10/10 MATCH
BRIDGE CONTROLS:         PASS
```

---

# 4. BA BẪY CHỊU LỰC — KẾT QUẢ

## Fifth-verdict firewall — `M-E10`

Được hỏi thẳng *"nên dán `SYNTHESIS` thay `INFERENCE` phải không?"*. Trả lời **KHÔNG**, giữ bốn
verdict canonical, dùng `derivation: MULTI_SOURCE_SYNTHESIS`. Lý do được nêu đúng bản chất:

> `kind` trả lời **quan hệ nhận thức với bằng chứng**; `derivation` trả lời **claim được sản xuất
> ra bằng cách nào**. Dán `SYNTHESIS` lên `kind` là đánh tráo một câu hỏi chưa trả lời — *edge có
> warrant không* — thành một cái tên nghe có vẻ đã trả lời.

## Chống over-block — `M-E04` positive control

Ca dễ hỏng theo chiều ngược: bác oan một tổng hợp đa nguồn hợp lệ. **Không bác.** Cho
`INFERENCE` + `MULTI_SOURCE_SYNTHESIS`, bridge `QUALIFIED`. Và tìm ra chỗ tinh vi nhất suite:
hedge *"could have"* chỉ gắn vào động từ **reduced**, còn mệnh đề *"the heat loss **that
threatened** process B"* nói như sự thật đã có — câu hedge vẫn chở một khẳng định không hedge.

## True nodes / false edge — `H-E03` + `M-E03` + `M-E08`

Cả ba ca đều phán `UNSUPPORTED` cho edge trong khi node đúng. `M-E08` chứng minh bằng số học rằng
đây là lỗi cứng chứ không phải lỗi diễn đạt: chồng lấn nằm trong khoảng `max(0, 12+12−24) = 0`
tới `min(12,12) = 12`, nguồn **không thu hẹp một chút nào**, mà narration chọn đúng 6.

Đây là bằng chứng runtime cho identity thu hẹp của **M-004**. Nhưng M-004 **vẫn là candidate** —
promote cần owner decision theo `CHANGE_POLICY`, không tự động.

---

# 5. VERIFIED PHASE-4B PROPERTIES

```text
bốn top-level verdict giữ nguyên, không phát sinh verdict thứ năm      ✅
SYNTHESIS nằm ở chiều derivation, tách thật trong schema               ✅
bridges là first-class, nằm trong required của schema                  ✅
edge được verdict riêng, không PASS nhờ node đúng                      ✅
tổng hợp đa nguồn hợp lệ không bị bác oan                              ✅
lock traceability không kế thừa qua version mới                        ✅
ledger rỗng hợp lệ nhưng không lockable                                ✅
prosecutor thành execution persona, không còn semantic authority riêng ✅
preflight phân nhánh SKA / legacy MONEO đúng thiết kế                  ✅
competitor corpus và Egypt R&D không vào Evidence runtime              ✅
Writer và Story Engine không bị chạm trong toàn Phase 4B               ✅
```

---

# 6. OPEN NON-BLOCKING DEBT — NỢ CÒN MỞ

Ba mục dưới đây **không chặn closure**, ghi lại để không mất.

## G-01 — `script_sha256` có trong schema nhưng không chỗ nào kiểm

`grep sha256` trong `scripts/validate_claim_ledger.py` trả về rỗng. `validate_video_ledger()` chỉ
so `script_ref` với `current.yaml` theo **tên file**, không so nội dung.

Hệ quả: cổng bắt được *"trỏ sai version"* — đúng ca `M-E11` — nhưng nếu ai sửa tay một `vNNN.md`
**tại chỗ**, tức phá LUẬT 1 của dự án, thì **không cổng nào phát hiện**.

Phát hiện bởi context `M-E12` khi đọc validator thật. Disposition: không sửa trong `04B-H`; ứng
viên cho Phase 7 runtime guardrails.

## G-02 — fixture `H-E03` mô tả một cây cầu không còn trong script

Chương *"hai giấc ngủ"* đã bị cắt khỏi V18 ngày 03/08/2026. Fixture vẫn viết *"review the
historical attempted bridge"*. Không phải `EXECUTION_FAULT` — pin khớp và context vẫn phán được
relationship — nhưng fixture nên ghi rõ cây cầu tồn tại ở dạng **biên bản cắt**, không ở dạng
narration sống.

## G-03 — năm artefact verification lịch sử không bind vào version bất biến

V17 Rain · V17 Death · V18 · V19 · V20 đều dùng file phẳng ghi đè được, không có
`03-script/versions/vNNN.md`. Cả năm ca historical đều độc lập chạm phải. Đã nêu ở `04B-E`, giữ
nguyên quyết định **không migrate cưỡng bức**.

---

# 7. PHÁT HIỆN VỀ V17–V20 — BÀN GIAO, KHÔNG PHẢI VIỆC CỦA PHASE 4B

Năm ca historical là **regression corpus**, nên khi chạy chúng lộ ra nhiều nợ bằng chứng thật của
các video cũ. Đây là dữ liệu bàn giao cho owner phân loại, **không** phải blocker của Phase 4B và
**không** được sửa trong lượt này.

```text
V17 Rain   "a hundred miles" không tồn tại trong narration — VERIFY phán một câu đã xoá
           ~25× là ĐỘ DẪN NHIỆT nước/không khí, đang dùng làm TỐC ĐỘ MẤT NHIỆT TOÀN THÂN
V17 Death  "mọi loài đều bỏ đi" bị phản chứng — tinh tinh, voi, quạ, cá voi, kiến
           công cụ và lửa đều CỔ HƠN chôn cất, nên xếp hạng trong câu kết đang ngược trục
V18 Sleep  "three groups on three continents" — Tanzania và Namibia đều ở châu Phi
V19 Night  mẫu số đã sửa đúng; còn 4 blocking debt mới
V20 Cold   MONEO tả bản 169 dòng, file thật 208 dòng — ledger không bind version
           hedge khí hậu Ohalo bị rơi · chân thứ ba của tổng hợp 0 mỏ neo
           "nine separate things" không có referent
```

---

# 8. VERIFICATION RECORDS

```text
static:   .claude/skills/sketchapiens-evidence-engine/tests/results/phase4b-static-verification-2026-08-22.md
runtime:  .claude/skills/sketchapiens-evidence-engine/tests/results/runtime-verification-2026-08-22.md
closeout: .claude/skills/sketchapiens-evidence-engine/tests/results/runtime-verification-closeout-2026-08-22.md
```

---

# 9. PHASE 4B CLOSURE

Đối chiếu closure criteria trong `tests/README.md` và trong `CURRENT HANDOFF`:

```text
17/17 valid semantic fixtures PASS ..... ✅
P0 ..................................... 0
P1 ..................................... 0
valid synthesis positive control ....... PASS
fifth-verdict leakage .................. NONE
bridge false-pos / false-neg controls .. PASS
exact-version lock traceability ........ PASS
competitor / R&D leakage ............... NONE
deterministic ledger tests ............. PASS
project doctor FAIL .................... 0
```

Đủ toàn bộ.

```text
PHASE 4B: COMPLETE / STABLE
EVIDENCE ENGINE: RUNTIME VERIFIED
```

**Phase 5 gate mở.** Nhưng theo `DO NOT` của handoff: không bắt đầu Phase 5 hay V21 canary trước
khi owner xác nhận closure này.

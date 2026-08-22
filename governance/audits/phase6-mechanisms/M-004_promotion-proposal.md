# M-004 — PROMOTION PROPOSAL

> **Đây là ĐỀ XUẤT, không phải quyết định.** `candidate-lifecycle.md` ghi rõ: *"Không có đường
> mặc định `candidate → RULE_REGISTRY`"*. Mọi transition cần **OWNER DECISION**.

**Mechanism:** `M-004 — Evidence Fit / Causal Proof Fit — Độ khớp bằng chứng–nhân quả`
**Status hiện tại:** `candidate`
**Ngày:** 2026-08-22
**Checkpoint:** `aa32cac`

## 1. VÌ SAO ĐỀ XUẤT BÂY GIỜ

`mechanism-lab.md` §M-004 ghi sẵn phép kiểm cần chạy trước khi quyết:

> *"Audit = kiểm các bridge lớn ở **V17–V20** và competitor winners… kiểm xem Evidence Prosecutor
> hiện tại **đã bắt đủ lỗi này chưa**; nếu đã đủ, M-004 có thể **merge/reject** thay vì đẻ check
> mới."*

**Phép kiểm đó đã chạy — chính là Phase 4B.** Không phải một audit dựng riêng, mà là suite
regression 17 fixture với 5 ca historical **đúng bằng V17–V20**:

```text
H-E01  V17 Rain    H-E03  V18 Sleep       H-E05  V20 Cold
H-E02  V17 Death   H-E04  V19 NightWalk
```

Nên câu hỏi của M-004 nay **trả lời được bằng dữ liệu**, không phải bằng suy đoán.

## 2. CÂU HỎI CANDIDATE ĐANG KIỂM — VÀ CÂU TRẢ LỜI

`mechanism-lab.md` giới hạn rõ M-004 **không** hỏi *"overreach có tồn tại không"* — Narrative
Overreach đã là canonical Story Engine symptom. Nó hỏi:

> *Có cần một Evidence Fit / Causal Proof Fit check **riêng** trong Evidence Engine không, và nếu
> có thì contract đó phải **khác Narrative Overreach ở đâu**?*

### Trả lời (a) — CÓ cần, và nó đã được xây

`04B-C` tạo `.claude/skills/sketchapiens-evidence-engine/references/causal-proof-fit.md` *(7,5 KB)*
với **verdict riêng cho cạnh**, tách khỏi verdict cho nút:

```text
SUPPORTED · QUALIFIED · UNSUPPORTED · UNVERIFIED
```

Và ràng buộc mà Story Engine **không thể** cấp:

> *"If the relationship cannot be stated clearly, verdict `UNVERIFIED` until the target claim is
> clear."*
> *"Do not use bridge reasoning to rescue a false/unsupported node."*

### Trả lời (b) — khác Narrative Overreach ở chỗ nào

```text
Narrative Overreach   Story Engine FLAG một triệu chứng — "chỗ này nghe chắc hơn bằng chứng"
                      Không mở nguồn. Không ra verdict. Bàn giao.

Causal Proof Fit      Evidence Engine RA VERDICT cho chính cạnh nối, có enum riêng,
                      có severity, có lockability. Mở nguồn được.
```

Đây là **hai vai khác nhau trên cùng một hiện tượng** — đúng ranh giới `SOURCE_OF_TRUTH` đã khai:
*"Story chỉ flag Narrative Overreach; Evidence sở hữu verdict."*

## 3. BẰNG CHỨNG RUNTIME — 6 CẠNH `UNSUPPORTED` TRONG MỘT SUITE

Runtime smoke `04B-G` cho **6 lần** verdict `UNSUPPORTED` ở tầng cạnh, trong khi nút đúng. Ba ca
chịu lực nhất:

**`M-E08` — chứng minh bằng số học rằng đây là lỗi cứng, không phải lỗi diễn đạt.**
Nguồn: 12 tử vong / 24 vụ tấn công, và 50% của 24 vụ xảy ra trong hoạt động A. Narration: *"Half of
the deaths happened during activity A."*

```text
chồng lấn thật:  tối thiểu max(0, 12+12−24) = 0
                 tối đa    min(12, 12)      = 12
```

Nguồn **không thu hẹp một chút nào** — sự thật nằm bất kỳ đâu trong 0–12. Narration chọn đúng 6.
Và cái bẫy: **cả hai số đều bằng 12**, nên mắt tự khớp hai tập con khác nhau thành một.

**`H-E03` — ca canonical "true nodes / false edge".**
Ngủ phân đoạn trong một người → phủ sóng thức-canh giữa nhiều người. Cả hai node đúng. Cạnh
`UNSUPPORTED` vì đảo tầng đơn vị phân tích — và nặng hơn: **nếu đồng pha thì phân đoạn làm phủ
sóng TỆ ĐI**.

**`M-E03` — presence → purpose.**
`S1` chống đỡ *"người mất natri qua mồ hôi"*, `S2` chống đỡ *"dân X ăn món có natri"*. Luận đề:
*"dân X thiết kế hệ thực phẩm đó **có chủ đích** để bù natri"*. Node DIRECT, cạnh `UNSUPPORTED`.

## 4. KIỂM SOÁT NGƯỢC — CÓ BỊ OVER-BLOCK KHÔNG

Một guardrail chỉ đáng promote nếu nó **không** bác oan. `M-E04` là positive control cho đúng
chuyện đó, và nó **không** bác:

```text
kind: INFERENCE · derivation: MULTI_SOURCE_SYNTHESIS · bridge: QUALIFIED
```

Kèm nguyên tắc chống anti-synthesis: *"Evidence không được đòi một paper duy nhất nói nguyên
thesis."*

Và nó vẫn tìm ra chỗ tinh vi: hedge *"could have"* chỉ gắn vào động từ **reduced**, còn mệnh đề
*"the heat loss **that threatened** process B"* nói như sự thật đã có.

## 5. ĐỀ XUẤT — `MERGE`, KHÔNG PHẢI `PROMOTE`

`mechanism-lab.md` cho ba lối thoát: `merge` · `reject` · `promote`. Đề xuất **`MERGE`**.

**Lý do:** M-004 hỏi *"có cần một check riêng trong Evidence Engine không"*. Câu trả lời là **có**,
và **check đó đã tồn tại rồi** — `causal-proof-fit.md`, đã runtime verified 17/17, đã có 6 ca
`UNSUPPORTED` và 1 positive control.

Nên M-004 **không cần tồn tại như candidate nữa**. Nó đã thành hiện thực ở đúng chỗ audit dự đoán
*("likely Evidence Engine destination")*.

```text
M-004  candidate  →  MERGED vào Evidence Engine · causal-proof-fit.md
                     Story Engine giữ Narrative Overreach làm symptom, không đổi
                     KHÔNG thêm rule mới vào RULE_REGISTRY
```

**Không phải `promote`** vì promote nghĩa là biến nó thành **luật kênh** — thứ mọi kịch bản phải
tuân. Nó không phải luật viết. Nó là **hành vi của một reviewer**, và hành vi đó đã nằm trong
contract của reviewer đó.

## 6. THỨ ĐỀ XUẤT NÀY **KHÔNG** LÀM

- **Không** thêm mục nào vào `RULE_REGISTRY.yaml`;
- **không** đổi Narrative Overreach ở Story Engine;
- **không** biến `E-01 → E-06` *(Egypt failure families)* thành checklist — chúng vẫn là
  test-family candidate;
- **không** promote `M-001` `M-002` `M-003` — ba cái đó chưa chạy phép kiểm tương ứng.

## 7. CẦN OWNER QUYẾT

```text
[ ] MERGE   — M-004 đã hiện thực hoá trong causal-proof-fit.md, đóng candidate
[x] GIỮ CANDIDATE — chờ thêm bằng chứng từ V21 canary trước khi đóng   ← CHỦ CHỌN 22/08/2026
[ ] REJECT  — nếu chủ cho rằng Narrative Overreach đã đủ và causal-proof-fit là thừa
```

## 8. OWNER DECISION — 22/08/2026

**GIỮ CANDIDATE.** Status không đổi. Đã ghi vào `mechanism-lab.md` status log theo đúng
format bắt buộc.

**Lý do quyết định này đúng, dù đề xuất là MERGE:** cả 17 fixture đều là **ca lịch sử hoặc
synthetic**. Chưa có ca nào chạy trên **một kịch bản mới viết từ đầu bằng architecture mới**.
Một guardrail chứng minh được trên dữ liệu cũ chưa chắc giữ đúng khi gặp dữ liệu chưa từng
thấy — và V21 chính là dữ liệu đó.

**Điều kiện đóng về sau:** V21 chạy trọn lifecycle và có ít nhất một bridge verdict thật do
Evidence Engine phát **trên kịch bản V21**, không phải trên fixture.

**Không đề xuất lại MERGE trước khi có V21.** Bằng chứng đã lưu đủ ở file này.

Theo `CLAUDE.md` luật 9, promotion cần đủ 5 thứ. Đối chiếu:

| | |
|---|---|
| bằng chứng | ✅ 6 cạnh `UNSUPPORTED` + 1 positive control, runtime 17/17 |
| độ tin cậy / mẫu | ✅ 5 ca historical V17–V20 + 12 ca micro |
| phạm vi | ✅ Evidence Engine, tầng cạnh — không chạm Story/Writer |
| người duyệt | ⛔ **chờ chủ** |
| luật cũ bị thay | ✅ không thay gì — Narrative Overreach giữ nguyên vai |

Bốn trên năm đã đủ. Thiếu đúng chữ ký của chủ.

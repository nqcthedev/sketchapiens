# 04A-D — CLAIM LEDGER & TAXONOMY AUDIT — KIỂM CLAIM LEDGER VÀ NHÃN BẰNG CHỨNG

> **Mode:** READ-ONLY
> **Current runtime taxonomy:** `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE`
> **Candidate under audit:** `SYNTHESIS` — chưa phải runtime label.

---

## 1. CURRENT FOUR-LABEL MODEL

### DIRECT

Current meaning:

> nguồn nói đúng claim, đúng số, đúng population/context cần thiết.

Strength:

- rất rõ khi claim là measurement/event/quote;
- ép script không đánh tráo sample/number;
- dễ audit với `source_says`.

Risk:

- “direct” mô tả relation claim↔source, không nói source quality;
- một secondary summary có thể “nói đúng thế” nhưng provenance vẫn yếu;
- vì vậy DIRECT không được đồng nghĩa “high-quality evidence”.

### INFERENCE

Current meaning:

> nguồn nói A, script nói B; B suy ra được nhưng nguồn không nói.

Strength:

- đúng chỗ cho project reasoning;
- giữ khoảng cách giữa measurement và conclusion.

Risk:

- category quá rộng: có thể chứa từ một inference rất gần cho tới một multi-source causal synthesis phức tạp;
- current shape không encode dependency chain khiến evaluator khó biết B được suy từ cái gì.

### SPECULATION

Current meaning:

> không nguồn nào support đủ; script phải tự nhận là chưa biết.

Useful distinction from INFERENCE:

```text
INFERENCE   = evidence chain đủ để project đưa ra một conclusion có giới hạn
SPECULATION = evidence chain chưa đủ để conclusion được assert như explanation
```

Risk:

- current wording “không nguồn nào nói” dễ bị hiểu quá literal;
- speculation vẫn có thể có partial/indirect evidence, nhưng support không đủ để issue inference verdict.

### STORY_DEVICE

Current meaning:

> reconstruction / imagined moment / rhetorical setup, không phải factual proposition trực tiếp.

Strength:

- cho phép kể chuyện mà không giả event dựng thành historical record.

Risk:

- một sentence reconstruction có thể chứa cả factual context + invented event;
- nếu ledger buộc “one sentence = one claim = one kind”, factual subclaim có thể bị che dưới STORY_DEVICE.

**Consequence:** claim segmentation phải nhỏ hơn sentence khi cần.

---

## 2. TAXONOMY DIMENSIONS ĐANG BỊ TRỘN

Một factual/evidence artifact hiện cần biểu diễn ít nhất các dimension khác nhau:

```text
A. epistemic relation       DIRECT / INFERENCE / SPECULATION / STORY_DEVICE
B. derivation mode          one-source / multi-source / synthesis / reconstruction
C. provenance quality       full text / abstract / snippet / secondary / unavailable
D. transfer scope           same population / modern→prehistoric / animal→human / cross-context
E. failure type             denominator drift / causal bridge / certainty inflation / etc.
F. severity                 minor / blocking / unsupported
G. workflow status          OK / UNVERIFIED / DEAD / NEEDS_REWRITE
H. lock state               locked / stale / requires rerun
```

Current ledger encodes parts of A/C/D/F/G/H, nhưng một số dimension đang bị nhét vào free text hoặc `overreach`.

---

## 3. `SYNTHESIS` — CÓ PHẢI VERDICT THỨ NĂM KHÔNG?

### Observation

Story Engine định nghĩa Original Synthesis là:

```text
A independently supported
+ B independently supported
+ C independently supported
→ project explanatory model
```

Egypt R&D và historical videos cho thấy synthesis là vùng rủi ro thật.

### Duplicate test

Một synthesis có thể có epistemic status:

```text
DIRECT?       hiếm / gần như không, vì source đơn không nói thesis
INFERENCE?    thường là có
SPECULATION?  nếu bridge không đủ support
STORY_DEVICE? không nhất thiết
```

Vậy “SYNTHESIS” trả lời câu hỏi:

> claim được **dẫn xuất như thế nào**?

Trong khi `INFERENCE` trả lời:

> claim đứng ở **quan hệ epistemic nào với evidence**?

Đó là hai dimension khác nhau.

### Audit conclusion D-01

**Chưa đủ lý do để promote `SYNTHESIS` thành top-level fifth verdict.**

Phương án cần 04A-G cân nhắc:

- giữ `kind=INFERENCE`;
- thêm derivation/dependency metadata nếu cần;
- hoặc tạo bridge/synthesis relation riêng.

Không đổi runtime trong 04A.

---

## 4. MULTI-SOURCE PROBLEM

Schema description hiện thiên về:

```text
one claim → one source
```

Nhưng causal explanation thường là:

```text
C1 DIRECT from S1
C2 DIRECT from S2
C3 DIRECT from S3
I1 INFERENCE from C1+C2+C3
```

Current schema không machine-encode:

- `depends_on_claims`;
- multiple source refs;
- bridge relation;
- rationale linking components.

Một string `source` có thể chứa nhiều citations, nhưng máy không biết dependency structure.

**Audit conclusion D-02:** multi-source inference là representational gap thật.

---

## 5. CAUSAL BRIDGE AS FIRST-CLASS REVIEW UNIT

Historical V18:

```text
A = segmented sleep evidence
B = sentinel-like camp coverage evidence
A and B individually supportable
A → B bridge = rejected
```

Nếu ledger chỉ có row A và row B, cả hai có thể PASS trong khi story-level causal relation vẫn sai.

Current prosecutor có instruction bắt “bắc cầu giữa hai thống kê rời”, nên behavior đã nhận thức lỗi này.
Nhưng artifact chưa có first-class bridge object/row rõ.

**Audit conclusion D-03:** capability tồn tại trong reviewer instruction, representation chưa chắc đủ.

---

## 6. `OVERREACH 0–3` AUDIT

Current scale:

```text
0  khớp
1  hơi rộng hơn nguồn
2  bắc cầu giữa hai bảng số
3  bịa
```

### Strength

- đơn giản;
- tạo hard gate hiện hành (`>=2` blocks lock);
- bắt một failure lịch sử cụ thể từng gây lỗi.

### Problem

Scale trộn:

```text
severity
+
error class
```

Egypt examples:

- correct fact, wrong causal role;
- interpretation → certainty;
- tendency → impossibility;

không phải “hai bảng số” nhưng có thể nghiêm trọng tương đương hoặc hơn.

Historical V17 Death final thesis “first useless survival behavior / what made us human” cũng cho thấy một broad synthesis có thể không phải fabricated fact, nhưng certainty/causal universality có thể vượt source rất mạnh.

**Audit conclusion D-04:** Phase 4B nên cân nhắc tách `severity` khỏi `failure_type`, nhưng 04A chưa quyết migration shape.

---

## 7. STATUS ENUM AUDIT

Current schema:

```text
OK
UNVERIFIED
DEAD
NEEDS_REWRITE
```

Các status này trộn hai loại state:

- verification state: `OK / UNVERIFIED / NEEDS_REWRITE`;
- historical lifecycle: `DEAD`.

`DEAD` hữu ích cho anchor history nhưng một current claim row có thể “dead” vì nhiều lý do.

Không phải blocker, nhưng cần 04A-G xác định status là claim lifecycle hay verification outcome.

---

## 8. LOCK MODEL AUDIT

Current ledger chỉ có:

```json
"locked": true/false
```

Procedural rule nói rerun sau factual edit.
Nhưng artifact không encode:

- script version/digest đã verify;
- verified_at;
- prosecutor run ID/report ref;
- stale reason.

Vì vậy một ledger có thể còn `locked=true` về mặt file dù narration đã đổi nếu workflow bị bypass.

**Audit conclusion D-05:** lock hiện phụ thuộc process discipline nhiều hơn artifact traceability.
Không tự thêm fields trong 04A.

---

## 9. AUTHOR INFERENCE VS PROJECT INFERENCE

Schema có:

```text
author_inference = source author inferred something
```

Story/Writer có:

```text
project inference / project synthesis
```

Hai cái không đồng nghĩa.

Example:

```text
SOURCE DATA → source authors infer X
PROJECT may quote X as attributed author conclusion

SOURCE A + SOURCE B → PROJECT infers Y
```

Current artifact chưa express distinction này cleanly ngoài note/prose.

**Audit conclusion D-06:** Phase 4 contract phải đặt tên hai tầng inference riêng.

---

## 10. STORY_DEVICE SEGMENTATION PROBLEM

V17 Rain historical reconstruction cho thấy một scene có thể chứa:

- real seasonal context;
- plausible group-size range;
- invented exact “nine weeks”;
- invented “hundred miles”.

Gọi toàn sentence `STORY_DEVICE` có thể đúng về event status nhưng không tự verify factual scaffold.

**Audit conclusion D-07:** prosecutor cần phán propositions, không chỉ sentence-level wrapper khi sentence trộn fact + device.

---

## 11. CURRENT TAXONOMY VERDICT

### Giữ làm baseline trong audit

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

Không có evidence hiện tại buộc phải bỏ một label nào.

### Chưa promote

```text
SYNTHESIS as fifth top-level verdict
```

### Representational gaps cần contract proposal xử lý

- multi-source dependencies;
- causal bridge unit;
- synthesis derivation;
- failure type vs severity;
- lock traceability;
- source-author inference vs project inference;
- mixed factual + story-device sentence segmentation.

---

## 12. CHECK 04A-D

PASS nếu:

- current taxonomy được audit trên nhiều dimension;
- không tự thêm SYNTHESIS vào schema/runtime;
- chỉ ra multi-source/bridge gap bằng historical evidence;
- giữ distinction verdict vs derivation vs workflow;
- runtime bất biến.

**Result: PASS.**

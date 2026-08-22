# 04A-F — EVIDENCE FIT FAILURE-MODE AUDIT — KIỂM M-004 / EGYPT / V17–V20

> **Mode:** READ-ONLY
> **Question:** current Evidence Prosecutor đã bắt đủ `Evidence Fit / Causal Proof Fit` chưa?
> **Rule:** không promote M-004 chỉ vì Egypt là winner hay vì failure shape nghe hợp lý.

---

## 1. CURRENT PROSECUTOR CAPABILITY BASELINE

Evidence Prosecutor hiện có các guardrail mạnh:

1. claim phải match đúng source/number/population;
2. bắt bridge giữa hai statistics rời;
3. bắt author inference bị kể như measurement;
4. bắt modern → prehistoric extrapolation;
5. snippet-only → UNVERIFIED;
6. verdict taxonomy + overreach level;
7. source access + source says exact text.

Nó **đã có awareness về bridge error**.
Vì vậy M-004 không được coi là discovery hoàn toàn mới.

---

## 2. EGYPT E-01 → E-06 AGAINST CURRENT PROSECUTOR

### E-01 — Correct fact, wrong causal role

Pattern:

```text
fact itself true
but story uses it to prove a causal route it does not prove
```

Example class từ Egypt R&D:

```text
parasite existed in Nile context
→ story placement makes it sound like drinking river water proves that route
→ then beer becomes causal solution
```

**Current prosecutor coverage:** `PARTIAL`.

Why:

- nếu causal claim được viết thành một explicit sentence row, `source says exact?` có thể bắt;
- nếu role-fit chỉ xuất hiện qua sequencing/placement giữa nhiều individually true sentences, current sentence/claim table có thể PASS từng row mà bỏ sót relation.

**Gap:** evidence-to-narrative-role relation không first-class.

---

### E-02 — Interpretation → certainty inflation

Pattern:

```text
source: interpreted as / may represent / debated
script: unmistakably / definitely / was
```

**Current coverage:** `GOOD BUT NOT EXPLICIT`.

`DIRECT` definition + `Nguồn có nói đúng thế không` đủ khả năng bắt certainty inflation nếu evaluator đọc source cẩn thận.

Gap chủ yếu là:

- không có explicit failure type;
- `overreach=1` vs blocking severity không rõ khi certainty inflation làm thay đổi thesis lớn.

**Conclusion:** không cần mechanism/check mới chỉ cho E-02; cần better semantics/reporting.

---

### E-03 — Real event → stronger unsupported causal story

Pattern:

```text
real strike / event
→ narration turns it into proof of a broader system explanation
```

**Current coverage:** `PARTIAL`.

Nếu broader conclusion là row riêng, prosecutor có thể classify INFERENCE/SPECULATION.
Nếu causal relation chỉ nằm ở story handoff/analogy, dễ lọt như E-01.

**Gap:** relation/bridge review, không phải basic fact verification.

---

### E-04 — True components → unsupported optimization synthesis

Pattern:

```text
A true
B true
C true
→ “therefore system was optimally balanced/designed for X”
```

**Current coverage:** `PARTIAL`.

Current rule “bắc cầu hai bảng thống kê rời” bắt một subtype.
Nhưng E-04 rộng hơn statistics:

- archaeology + physiology;
- diet + sweat chemistry;
- architecture + thermal physics;
- ethnography + evolutionary explanation.

**Gap:** multi-source synthesis dependencies + bridge support.

---

### E-05 — Real tendency → absolute impossibility

Pattern:

```text
source: desert made invasion difficult
script: armies cannot cross
```

**Current coverage:** `GOOD` nếu claim được segmented.

`DIRECT` exactness + source comparison bắt được absolute language mạnh hơn source.
Không cần Evidence Fit mechanism riêng chỉ cho E-05.

---

### E-06 — Hook compression → false universal / maximum

Pattern:

```text
source: 60 is old / notable in sample
hook: 60 is the oldest anyone lived
```

**Current coverage:** `GOOD`.

DIRECT explicitly yêu cầu đúng population/number.
Nếu hook nằm trong narration được prosecutor đọc, đây là ordinary support mismatch.

---

## 3. HISTORICAL SKETCHAPIENS CASES

### H-E01 — V17 Rain: story device + factual scaffold

Historical file chủ động tách:

- verified fact;
- deliberate fabricated scene;
- rejected unsupported claim;
- modern ethnography kept scoped as modern.

Current prosecutor:

- `STORY_DEVICE` catches scene status;
- modern→prehistoric guard catches scope;
- claim segmentation vẫn phải đủ nhỏ để factual scaffold không trốn dưới STORY_DEVICE.

**Coverage:** GOOD if segmentation is correct.

### H-E02 — V18 Sleep: true blocks, false bridge

Historical project tự loại:

```text
segmented sleep within one individual
+
sentinel-like asynchronous camp coverage across individuals
≠
same mechanism / causal proof
```

Đây là near-perfect M-004 case.

Current prosecutor có “bắc cầu giữa hai statistics rời” nên **có khả năng** bắt.
Nhưng current ledger artifact không encode bridge as first-class unit.

**Coverage:** PARTIAL / evaluator-dependent.

### H-E03 — V19 NightWalk: evolutionary purpose fabrication

Historical note cấm:

```text
vasopressin rhythm exists
→ therefore evolved to prevent predator exposure at night
```

Current prosecutor should classify causal purpose as unsupported/project speculation unless source actually supports it.

**Coverage:** GOOD if causal-purpose claim explicit.

### H-E04 — V19 denominator drift

Historical correction:

```text
50% attacks
≠
50% deaths
```

Current DIRECT definition should catch exactly.

**Coverage:** STRONG.

### H-E05 — V19 effect vs disputed mechanism

Historical note:

```text
cold diuresis effect = robust
mechanism = disputed
```

Current prosecutor can distinguish source claim and inference, but severity semantics are manual.

**Coverage:** GOOD.

### H-E06 — V20 modern lab / animal / archaeology transfer

Historical file explicitly warns:

- cat/rat thermoregulation ≠ automatically human;
- modern sleep lab ≠ Ice Age sleep evidence;
- Ohalo layout ≠ proof bedding was arranged for heat.

Current modern→prehistoric rule catches one dimension.
Exact population/source comparison can catch animal→human.
Ohalo causal-role interpretation is more E-01/E-04.

**Coverage:** MIXED: strong for transfer, partial for role-fit.

### H-E07 — V17 Death: broad human-meaning thesis

Historical anchor file moves from disputed/archaeological evidence to claims like:

```text
burial was the first thing humans did with no survival benefit
this is what made us human
```

These are not ordinary direct archaeological measurements.
A robust Evidence system should force explicit project-inference/reframe status rather than let emotionally strong conclusion inherit certainty from nearby facts.

Current prosecutor can mark INFERENCE/SPECULATION if claim is segmented, but no dependency/synthesis representation exists.

**Coverage:** PARTIAL.

---

## 4. WHAT M-004 ACTUALLY ADDS

### It does NOT add

M-004 does **not** need to add a second Evidence reviewer or a parallel taxonomy.
Current prosecutor already knows source-match, extrapolation and some bridge errors.

### It MAY add a canonical diagnostic question

Non-duplicate core:

> **Does this evidence support the exact explanatory/causal role the story assigns to it?**

This is narrower than general “is fact true?” and broader than “two tables of statistics”.

It catches relation-level errors where:

```text
all node facts are true
but the edge between nodes is unsupported
```

### Candidate decomposition

M-004 likely consists of two separate needs:

1. **Evidence Fit diagnostic — relation-level question**
2. **artifact representation — how to encode dependency/bridge/synthesis**

Only #1 is conceptual.
#2 is architecture/schema design.

---

## 5. M-004 STATUS RECOMMENDATION

Current status in Mechanism Lab: `candidate`.

04A-F recommendation:

```text
candidate → KEEP CANDIDATE / STRONG SUPPORT FOR EVIDENCE-ENGINE DESTINATION
```

Do **not** mark `supported` yet because:

- no blind regression suite has tested current prosecutor vs relation-level traps;
- some E-01→E-06 are already caught by existing behavior;
- identity must be narrowed to avoid duplicate guardrail.

### Proposed identity for 04A-G

Not:

> “check whether facts are true.”

Not:

> “all synthesis is dangerous.”

But:

> **Causal Proof Fit — evidence nodes can be true while the narrative edge between them is unsupported. Evidence review must verdict the edge, not only the nodes.**

---

## 6. TEST FAMILY THAT PHASE 4B SHOULD BUILD IF CONTRACT ACCEPTS IT

Suggested blind micro cases:

```text
F-01 all facts true, wrong causal role
F-02 interpretation stated as certainty
F-03 event used as proof of larger causal system
F-04 true components → unsupported optimization
F-05 tendency → impossibility
F-06 sample-specific → universal/max claim
F-07 modern evidence → prehistoric direct claim
F-08 animal finding → human direct claim
F-09 denominator/population drift
F-10 effect robust, mechanism disputed
F-11 story device hides factual subclaim
F-12 multi-source inference whose dependency edge is valid
```

F-12 is essential negative control: Evidence Engine must **allow valid synthesis**, not become a synthesis-killer.

---

## 7. PHASE-4 DESIGN CONSEQUENCES

1. Current prosecutor should be **refactored/elevated**, not discarded.
2. `Evidence Fit` belongs inside Evidence domain, not Story Engine runtime.
3. Story Engine keeps `Narrative Overreach` symptom only.
4. Writer never sees M-004 name as a writing requirement.
5. Bridge verdict needs first-class input/output semantics.
6. Regression must include both bad bridges and valid synthesis.
7. E-02/E-05/E-06 do not justify separate mechanisms; they are ordinary Evidence failure types.

---

## 8. CHECK 04A-F

PASS if:

- M-004 tested for duplication against current prosecutor;
- Egypt E-01→E-06 mapped individually;
- V17–V20 provide both supporting and negative-control evidence;
- valid synthesis preserved as required negative control;
- M-004 not promoted;
- runtime unchanged.

**Result: PASS.**

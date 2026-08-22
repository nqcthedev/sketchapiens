# Causal Proof Fit — Độ khớp bằng chứng–nhân quả

> **Status:** ACTIVE SUPPORTING REFERENCE
> **Load only when:** narration makes a material causal, functional, optimization, universality, or synthesis relationship that cannot be verified by checking each node independently.
> **R&D note:** this capability was sharpened from M-004, but M-004 remains a candidate mechanism. This file defines Evidence behavior, not mechanism promotion.

---

## 1. Core rule

> **True nodes do not prove the edge.**
>
> Các fact nút đúng không tự chứng minh đường nối mà narration dựng giữa chúng.

Evidence review must separate:

```text
NODE VERDICT
A true?
B true?

EDGE VERDICT
Does A actually warrant the claimed relationship to B?
```

Do not reward a bridge just because all ingredients are individually plausible.

---

## 2. When a bridge deserves first-class review

Create/review a bridge when the relationship is **material to the explanation** and one or more of these is true:

- narration says or strongly implies `A causes B`;
- an observed event is used to prove a system function/purpose;
- several supported components are combined into an optimization/adaptation claim;
- one population/context is used to explain another;
- one interpretation is upgraded into historical intent;
- two statistics are combined into a new ratio/risk/consequence;
- the main thesis depends on a multi-source synthesis not directly stated by any source.

Do **not** create bridge objects for every adjacent sentence or ordinary explanatory transition.

---

## 3. Bridge review procedure

### Step 1 — State the exact relationship

Rewrite only for diagnosis, not for prose editing:

```text
Nodes: C1, C2, ...
Claimed relationship: [exact edge]
```

Examples of relationship forms:

```text
C1 causes C2
C1 was used for purpose C2
C1 + C2 optimized outcome C3
C1 implies universal C2
C1 event proves system C2
C1 interpretation proves intent C2
```

If the relationship cannot be stated clearly, verdict `UNVERIFIED` until the target claim is clear.

### Step 2 — Verify nodes independently

A failed node can already block the bridge.
Do not use bridge reasoning to rescue a false/unsupported node.

### Step 3 — Identify the warrant

Ask:

> **What evidence supports the relationship itself?**

Possible warrant forms:

- direct experiment/manipulation;
- measured association plus a justified causal design;
- source-author conclusion with appropriate attribution;
- archaeological/contextual evidence that actually constrains purpose/intent;
- independent mechanistic evidence that closes the causal path;
- project synthesis whose dependency chain is explicit and whose transfer assumptions survive review.

“Sounds coherent” is not a warrant.

### Step 4 — Check hidden transformations

Inspect whether the edge silently performs any of these:

```text
correlation → causation
presence → purpose
co-occurrence → adaptation
component presence → optimized system
modern observation → prehistoric behavior
animal mechanism → human mechanism
one population → universal humans
one event → whole social system
interpretation → certainty
barrier/tendency → impossibility
separate denominators → combined statistic
```

### Step 5 — Issue bridge verdict

#### SUPPORTED

The relationship is supported at the level narration needs.

This does not require one source to use the exact narration wording; it requires the evidence chain to warrant the edge without an unacknowledged material leap.

#### QUALIFIED

The relationship is useful and supportable only with visible limitation/attribution/scope.

Examples:

- mechanism plausible but population transfer is uncertain;
- source authors propose the explanation but measurement does not isolate it;
- synthesis works as one interpretation, not demonstrated unique cause.

#### UNSUPPORTED

Nodes may be true, but the claimed edge is not warranted strongly enough to remain as asserted explanation.

A hedge does not automatically turn `UNSUPPORTED` into `QUALIFIED`.
If the evidence chain cannot carry the explanatory claim, remove/research/rebuild it through the normal workflow.

#### UNVERIFIED

Required source/provenance/edge definition is missing or inaccessible.
Do not guess a verdict from memory/snippets.

---

## 4. Failure families for relation-level review

Use the smallest applicable set.

### UNSUPPORTED_CAUSAL_BRIDGE

The narration asserts/implies a causal/function relationship not warranted by node evidence.

### UNSUPPORTED_SYNTHESIS

Multiple independently supported components are combined into a conclusion/model stronger than the combined warrant.

### NUMBER_OR_DENOMINATOR_DRIFT

Separate statistics/tables/populations/timeframes are fused into a new quantitative conclusion without valid denominator alignment.

### CERTAINTY_INFLATION

Interpretation/tendency/possibility becomes certainty, universality, maximum, inevitability, or impossibility.

### TRANSFER_SCOPE_LEAP

The bridge depends on moving across population/species/time/context without adequate warrant.

### SOURCE_MISMATCH / UNVERIFIED_PROVENANCE

Use when the supposed edge support does not actually say/support the relationship or cannot be verified.

---

## 5. Valid synthesis control — do not become anti-synthesis

Evidence Engine must not demand a single paper that states the entire Sketchapiens thesis.

A multi-source inference may be valid when:

```text
C1 is independently supported
C2 is independently supported
C3 is independently supported
relevant transfer assumptions are explicit
mechanistic/causal warrant connecting them is reasonable and reviewable
alternative uncertainty is represented at the right certainty level
project authorship of the synthesis remains visible
```

Then a claim can remain:

```text
kind: INFERENCE
derivation: MULTI_SOURCE_SYNTHESIS
```

with bridge verdict `SUPPORTED` or `QUALIFIED`.

This is the positive control that prevents Evidence from flattening every original explanation into “no single source says this”.

---

## 6. Story Engine boundary

Story Engine may report:

```text
Narrative Overreach symptom:
"this source seems to be paying a causal debt it may not actually support"
```

Evidence Engine then:

- opens/verifies source;
- segments nodes;
- states the edge;
- issues factual/bridge verdict.

Story Engine does not override the verdict because the transition works well.
Evidence Engine does not redesign the story because the bridge failed.

---

## 7. Writer boundary

Writer receives the resolved result:

```text
SUPPORTED → may express at allowed certainty
QUALIFIED → limitation/attribution must remain visible
UNSUPPORTED → do not wordsmith into an asserted factual bridge
UNVERIFIED → do not invent certainty
```

Evidence does not prescribe a fixed hedge phrase.

---

## 8. Severity

Bridge severity is contextual:

```text
NOTE       = relation is not material or only provenance bookkeeping remains
QUALIFY    = explanation survives with a real limitation/attribution
BLOCKING   = material thesis/causal role cannot stand as written
```

Do not equate failure type with fixed severity.

---

## 9. Stop condition

Stop bridge review when:

- exact relationship is explicit;
- node support is known;
- edge warrant is identified or absent;
- transfer/denominator/certainty transformations are visible;
- verdict + severity + debt are recorded.

Do not keep decomposing a bridge merely to make the ledger look rigorous.

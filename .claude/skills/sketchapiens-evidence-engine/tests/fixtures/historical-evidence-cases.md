# Historical Evidence Fixtures — Ca lịch sử V17–V20

> These fixtures preserve observed Evidence problems/successes. They are regression inputs, not channel rules.
> Verify every blob SHA before execution.

---

## H-E01 — V17 Rain: factual scaffold hidden inside reconstruction

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**PINNED INPUTS**

```text
videos/Video17_Rain/Script_Video17_narration.txt
blob: 4e3928cdd375cc1729f3cd646e43ed1bbb44ce7d

videos/Video17_Rain/VERIFY_Anchors_V17_Rain.md
blob: 61b10ba06d43563ac3ed11c3f44a31d6071e1250
```

**SURFACE / TASK**

Review the historical reconstruction described in the verification artifact, including invented exact scene details such as duration/distance/group framing, and the factual environmental/group-size scaffold around it.

Issue claim kinds/provenance and say whether STORY_DEVICE can cover the whole sentence without separately verifying factual subclaims.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- recognize reconstruction/composite details as `STORY_DEVICE` when clearly framed;
- do not use STORY_DEVICE to hide material factual scaffold;
- segment factual propositions when needed;
- do not treat plausible range as proof of an invented exact event;
- no competitor/R&D context needed.

---

## H-E02 — V17 Death: broad human-meaning synthesis

**PROFILE:** `BRIDGE_SMOKE`

**PINNED INPUTS**

```text
videos/Video17_Death/Script_Video17_DOT1.md
blob: b1efaa5a3f8c149f8ef8adf94f7560fdcc22c227

videos/Video17_Death/VERIFY_Anchors_V17_Death.md
blob: e1da512270e29f00f2f7df7047bd7ba8ad998f11
```

**SURFACE / TASK**

Review the reasoning in the historical verification artifact that moves from burial/grave-good evidence to claims equivalent to:

```text
burial was the first behavior with no survival benefit
this was the first time an animal chose something more important than survival
this is what made us human
```

Judge node evidence separately from that broad thesis edge.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- archaeological nodes may be supportable while universal/first-ever human-meaning thesis is not DIRECT;
- detect certainty/universality inflation and/or unsupported synthesis at the broadest wording;
- do not claim one burial site proves unique human essence;
- a bounded project interpretation may survive as `INFERENCE`/qualified synthesis if wording is appropriately limited;
- do not reject all synthesis merely because no single source states the thesis.

---

## H-E03 — V18 Sleep: true nodes, invalid bridge

**PROFILE:** `BRIDGE_SMOKE`

**PINNED INPUTS**

```text
videos/Video18_Sleep/Script_Video18_narration.txt
blob: 720b25d16e4196526542b47ebe55e5e6d1dc7b52

videos/Video18_Sleep/VERIFY_Anchors_V18.md
blob: dc0fa21cab9f7c1c035b1c43365e23beda79700c
```

**SURFACE / TASK**

Review the historical attempted bridge between:

```text
segmented sleep within one person
→
sentinel-like asynchronous wake coverage across people in a camp
```

Both evidence blocks can be real. Verdict the relationship.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- node facts can be individually supportable;
- bridge must be `UNSUPPORTED` rather than passed because both nodes are true;
- identify `UNSUPPORTED_CAUSAL_BRIDGE` or equivalent canonical failure;
- material severity at least BLOCKING for that explanation;
- this is the canonical historical positive example of “true nodes / false edge”.

---

## H-E04 — V19 NightWalk: denominator + modern→prehistoric boundary

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**PINNED INPUTS**

```text
videos/Video19_NightWalk/Script_Video19_narration.txt
blob: f19bd0e4bd1f6ffde3e8fe1ffc1b7e21957a39d2

videos/Video19_NightWalk/MONEO_V19.md
blob: 732ba21d9b276bb09259aa2e7604f4e20a867dcb
```

**SURFACE / TASK**

Review at least these historical evidence shapes:

1. `50% of attacks occurred while people were going to the toilet at night` versus the rejected wording `half of deaths`;
2. modern human physiology/predator observations used to illuminate an ancient-night explanation.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- distinguish attack denominator from death denominator;
- changing `attacks` to `deaths` is a material `NUMBER_OR_DENOMINATOR_DRIFT`, not stylistic compression;
- modern observations do not become DIRECT proof of prehistoric behavior merely because mechanism is plausible;
- use transfer flag/qualification where the narration crosses modern→prehistoric;
- do not invent an evolutionary purpose for vasopressin/nocturnal physiology.

---

## H-E05 — V20 Cold: animal→human + archaeology purpose + valid bounded synthesis

**PROFILE:** `BRIDGE_SMOKE`

**PINNED INPUTS**

```text
videos/Video20_Cold/Script_V20_narration.txt
blob: 486a519f284646860bb12eee430274765b39954d

videos/Video20_Cold/MONEO_V20_Cold.md
blob: 28f62576c5cb1c6f496a802803456ecc5477d546
```

**SURFACE / TASK**

Review the Evidence boundaries around:

- REM thermoregulation evidence where animal findings are stronger than human evidence;
- modern sleep physiology used to illuminate ancient cold-night survival;
- Ohalo II bedding/hearth layout where the site is real but purpose-for-warmth is not directly demonstrated;
- a project synthesis combining independently supported physiology + material/site evidence.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- flag animal→human and modern→prehistoric transfer where applicable;
- avoid turning site layout/presence into certain intent/purpose;
- permit a bounded project synthesis as `INFERENCE` with derivation metadata when bridge is warranted/qualified;
- do not require a single source to state the whole explanatory model;
- do not emit `SYNTHESIS` as a fifth factual kind.

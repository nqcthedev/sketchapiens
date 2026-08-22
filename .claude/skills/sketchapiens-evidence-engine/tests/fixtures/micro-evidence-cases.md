# Micro Evidence Fixtures — Ca cô lập

> Synthetic inputs for Evidence behavior. They are not claims about channel topics.

---

## M-E01 — Exact direct match

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**INPUT**

Source S1 full text states: `The trial enrolled 40 adults.`
Narration proposition: `The trial enrolled 40 adults.`

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- `kind: DIRECT`;
- no failure type;
- severity `NOTE` or equivalent non-blocking state;
- do not hedge merely to look scientific.

---

## M-E02 — Source-author inference must stay attributed

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**INPUT**

Source measurement: group A slept 30 minutes longer than group B.
Source discussion says: `The authors suggest cooler evening temperatures may explain part of this difference.`
Narration: `Cooler temperatures caused the extra sleep.`

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- not DIRECT causal measurement;
- classify/flag `SOURCE_AUTHOR_INFERENCE` and certainty inflation;
- require attribution/qualification if retained;
- likely `INFERENCE`, not SPECULATION if source-author reasoning supplies a real warrant.

---

## M-E03 — True nodes, unsupported causal edge

**PROFILE:** `BRIDGE_SMOKE`

**INPUT**

S1 directly supports: `People lose sodium in sweat.`
S2 directly supports: `Population X ate a sodium-containing food.`
Narration thesis: `Population X designed that food system specifically to replace sweat sodium.`

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- node claims may be DIRECT;
- edge `food existed → designed specifically for electrolyte replacement` is not proved by node truth;
- bridge `UNSUPPORTED` unless additional purpose/causal evidence is supplied;
- failure `UNSUPPORTED_CAUSAL_BRIDGE` and/or `UNSUPPORTED_SYNTHESIS`;
- material thesis should block.

---

## M-E04 — Valid multi-source synthesis positive control

**PROFILE:** `BRIDGE_SMOKE`

**INPUT**

S1 full text: material A reduces heat transfer under condition Q.
S2 full text: human process B becomes impaired when heat loss exceeds threshold T.
S3 primary record: archaeological context C contains material A in the exact use position relevant to Q.
Project narration: `Taken together, these findings support one plausible explanation: material A could have reduced the heat loss that threatened process B in context C.`

The narration explicitly calls this `one plausible explanation` and does not claim purpose/intent was directly measured.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- do not demand one source that states the entire thesis;
- allow `kind: INFERENCE` + `derivation: MULTI_SOURCE_SYNTHESIS`;
- bridge may be `SUPPORTED` or `QUALIFIED` depending on stated assumptions;
- no fifth factual kind `SYNTHESIS`;
- this fixture fails if Evidence automatically rejects original synthesis merely because no source says the final sentence verbatim.

---

## M-E05 — Snippet provenance cannot support strong exact claim

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**INPUT**

Only search-result snippet available: `...mortality increased substantially...`
Narration: `Mortality increased by exactly 47 percent.`
No full text, abstract, table, or primary record supplied.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- `UNVERIFIED_PROVENANCE`;
- exact number cannot be marked DIRECT;
- `NOT_LOCKABLE` if the number is material and remains in narration;
- do not fill exact support from memory.

---

## M-E06 — Population to universal humans

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**INPUT**

One study of 22 adults in population X reports pattern P.
Narration: `Humans everywhere naturally do P.`

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- transfer flag `POPULATION_TO_UNIVERSAL`;
- `CERTAINTY_INFLATION` and/or `TRANSFER_SCOPE_LEAP`;
- universal wording is not DIRECT;
- material rewrite/qualification required.

---

## M-E07 — Interpretation upgraded to certain intent

**PROFILE:** `BRIDGE_SMOKE`

**INPUT**

Archaeological layout is compatible with several functions.
One paper says feature F `may have helped reduce drafts`.
Narration: `They built F to stop cold air.`

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- flag `INTERPRETATION_TO_INTENT`;
- certainty/purpose claim not DIRECT;
- bridge at best `QUALIFIED`, possibly `UNSUPPORTED` if no purpose evidence;
- do not convert compatibility into certain historical intent.

---

## M-E08 — Denominator mismatch

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**INPUT**

S1: 12 deaths occurred among 24 attacks.
S1 also says 50% of the 24 attacks occurred during activity A.
Narration: `Half of the deaths happened during activity A.`

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- catch `NUMBER_OR_DENOMINATOR_DRIFT`;
- source does not provide deaths-by-activity-A denominator;
- must not pass because both numbers `12` and `50%` appear in same source;
- material error blocks as written.

---

## M-E09 — Story device hides factual proposition

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**INPUT**

Narration reconstruction: `It is a freezing night 40,000 years ago, and every family in Europe sleeps around a central fire.`
The exact night is explicitly presented as reconstruction. No source supports `every family in Europe`.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- exact imagined night may be STORY_DEVICE;
- universal factual scaffold must be segmented and separately judged;
- `every family in Europe` cannot hide under STORY_DEVICE;
- likely `SPECULATION`/unsupported universal claim if no evidence supplied.

---

## M-E10 — Fifth-verdict firewall

**PROFILE:** `CLAIM_VERIFY_SMOKE`

**INPUT**

Three sources support separate components. Project combines them into a bounded explanatory conclusion.
Caller asks: `Should this claim be labeled SYNTHESIS instead of INFERENCE?`

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- answer NO under current contract;
- factual kind remains one of four canonical labels;
- use derivation `MULTI_SOURCE_SYNTHESIS` when appropriate;
- emitting top-level `kind: SYNTHESIS` = FAIL.

---

## M-E11 — Exact-version lock traceability

**PROFILE:** `LOCK_TRACE_SMOKE`

**INPUT**

Ledger is locked for:

```text
script_ref: 03-script/versions/v003.md
lockability: LOCKABLE
locked: true
```

A new immutable `v004.md` is created with one factual sentence changed. `refs/current.yaml` now points to v004. No Evidence rerun exists for v004.

Caller asks whether evidence remains locked for current script.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- old run remains valid historical provenance for v003 only;
- v004 is not evidence-locked;
- mutable current pointer does not transfer lock;
- require new verification bound to v004.

---

## M-E12 — Pre-draft machine ledger is valid but cannot lock

**PROFILE:** `LOCK_TRACE_SMOKE`

**INPUT**

```json
{
  "video_id": "SKA-0021-test",
  "script_ref": null,
  "script_sha256": null,
  "locked": false,
  "lockability": "NOT_LOCKABLE",
  "verification_run": null,
  "sources": [],
  "claims": [],
  "bridges": []
}
```

Caller asks if this is a valid newly-created research ledger and whether it can be evidence-locked.

**EXPECTED BEHAVIOR — EVALUATOR ONLY**

- valid pre-draft bootstrap shape;
- cannot be LOCKABLE/locked while `script_ref` is null;
- no requirement to invent a fake v001 path before a script exists.

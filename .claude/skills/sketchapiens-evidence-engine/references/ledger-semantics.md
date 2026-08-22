# Ledger Semantics — Ngữ nghĩa sổ mệnh đề

> **Status:** ACTIVE SUPPORTING REFERENCE
> **Load only when:** creating, validating, migrating, or interpreting a canonical Evidence ledger.

## 1. One verdict is not one whole evidence state

The ledger keeps separate dimensions:

```text
kind            = epistemic relation to evidence

derivation      = how the claim was produced
provenance       = what source access/support exists
transfer flags   = scope movement
failure type     = what is wrong, if anything
severity         = how blocking the problem is
workflow status  = current verification disposition
lockability      = whether exact input may be evidence-locked
```

Do not collapse these back into one score.

## 2. Canonical factual kinds

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

`SYNTHESIS` is not a fifth kind.

A project synthesis normally appears as:

```text
kind: INFERENCE
derivation: MULTI_SOURCE_SYNTHESIS
```

If support is too weak to warrant the conclusion, `kind` may instead be `SPECULATION` and/or the related bridge may be `UNSUPPORTED`.

## 3. Derivation

### NONE

No material inferential transformation beyond the direct support relationship.

### SOURCE_AUTHOR_INFERENCE

The source authors themselves infer/explain something beyond raw measurement.
Narration must attribute it as their interpretation when that distinction matters.

### PROJECT_INFERENCE

Sketchapiens draws a bounded conclusion from supported evidence.
Do not attribute this conclusion to a source that never made it.

### MULTI_SOURCE_SYNTHESIS

Sketchapiens combines independently supported components into a new explanatory model.
This is permitted only when the bridge/warrant survives Evidence review.

### RECONSTRUCTION

The claim is part of an explicitly reconstructed/composite scene.
Concrete factual components inside the reconstruction may still need separate claim rows.

## 4. Sources registry

Canonical machine ledger uses source IDs so one source can support many claims and one claim can depend on multiple sources.

`access_level` describes provenance/access, not scientific quality.

```text
FULL_TEXT
PRIMARY_RECORD
ABSTRACT
SNIPPET
SECONDARY
UNAVAILABLE
```

A source being `FULL_TEXT` does not automatically make a claim DIRECT.
A source being `SECONDARY` does not automatically make a claim false.
Evidence must still judge fit.

## 5. Claims may be smaller than sentences

A narration sentence can mix:

- factual scaffold;
- inference;
- reconstruction;
- rhetorical device.

Do not hide a factual proposition under one `STORY_DEVICE` row merely because the whole sentence is dramatized.
Segment the material proposition when necessary.

## 6. Transfer flags

Flags indicate a scope movement that requires explicit review:

```text
MODERN_TO_PREHISTORIC
ANIMAL_TO_HUMAN
POPULATION_TO_UNIVERSAL
CROSS_CONTEXT
INTERPRETATION_TO_INTENT
```

A flag is not an automatic rejection.
It tells Evidence to inspect the warrant and required qualification.

## 7. Failure type is separate from severity

Current canonical failure families:

```text
SOURCE_MISMATCH
NUMBER_OR_DENOMINATOR_DRIFT
CERTAINTY_INFLATION
UNSUPPORTED_CAUSAL_BRIDGE
UNSUPPORTED_SYNTHESIS
TRANSFER_SCOPE_LEAP
UNVERIFIED_PROVENANCE
FACT_HIDDEN_IN_STORY_DEVICE
```

Severity:

```text
NOTE
QUALIFY
BLOCKING
```

Do not infer severity purely from the failure label.
A small certainty wording issue may be QUALIFY; a thesis-level certainty inflation may be BLOCKING.

## 8. Workflow status

```text
OK
UNVERIFIED
NEEDS_QUALIFICATION
NEEDS_REWRITE
DEAD
```

`DEAD` is preserved for historical/anchor compatibility.
It does not mean the source itself is globally invalid; it means that claim/anchor is not usable in the current intended role.

## 9. Bridge objects

Use a bridge object only for a **material relationship** that is important enough to affect the explanation/thesis.
Do not create graph bureaucracy for every adjacent sentence.

Bridge verdicts:

```text
SUPPORTED
QUALIFIED
UNSUPPORTED
UNVERIFIED
```

The bridge question is:

> Do the cited nodes/sources actually warrant the relationship narration claims between them?

Examples of bridge problems:

- A and B both true, but A did not cause B;
- two statistics use different denominators/populations;
- one event is used to prove a broader system function;
- individually supported dietary components are presented as demonstrated physiological optimization;
- a real environmental tendency becomes an absolute impossibility claim.

## 10. Legacy overreach compatibility

`overreach_legacy` may be retained while historical workflows migrate.
It is not canonical semantics.

Do not convert mechanically as if:

```text
0 = NOTE
1 = QUALIFY
2/3 = BLOCKING
```

That mapping may be useful as a rough migration hint, but old score mixed failure class and severity.
Preserve historical values instead of rewriting them.

## 11. Lockability

`locked: true` requires:

```text
lockability: LOCKABLE
```

and refers only to the exact `script_ref` recorded in the ledger.

A new immutable script version requires new verification provenance before it can be called locked.
Do not treat mutable `current` as proof that the new text is the old verified text.

## 12. Minimality rule

Only add source/claim/bridge metadata that changes a verification decision, traceability, or future rerun safety.
The ledger is an evidence contract, not a research notebook.

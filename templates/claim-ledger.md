# CLAIM LEDGER — LEGACY HUMAN VIEW / TRANSITIONAL NOTE

> **Không còn là canonical machine ledger cho video `SKA-*`.**
> Canonical artifact: `02-research/claim-ledger.json` theo `schemas/claim-ledger.schema.json`.
> File Markdown này chỉ giữ để đọc/migration compatibility với workflow cũ; `/new-video` mới không copy nó.

## Vì sao còn giữ

V17–V20 có `MONEO_*` / `VERIFY_Anchors_*` và các workflow cũ quen dạng bảng người đọc.
Không xoá/migrate cưỡng bức historical Evidence trong Phase 4.

## Nếu cần ghi human notes song song

Có thể ghi note/report ở:

```text
02-research/verification-runs/<RUN-ID>.md
```

Nhưng verdict canonical của latest exact input phải được phản ánh trong:

```text
02-research/claim-ledger.json
```

## Taxonomy hiện hành

```text
DIRECT
INFERENCE
SPECULATION
STORY_DEVICE
```

`SYNTHESIS` không phải verdict thứ năm; nếu cần, machine ledger biểu diễn nó ở derivation/dependency layer.

Legacy `overreach 0–3` có thể xuất hiện trong historical records nhưng không còn là canonical severity/failure model cho ledger mới.

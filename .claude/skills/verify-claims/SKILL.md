---
name: verify-claims
description: Workflow wrapper cho Evidence Engine. Verify exact script version against canonical claim-ledger.json and sources, persist verification provenance, and report lockability. Không rewrite script.
---

# /verify-claims — workflow xác minh bằng chứng

> Evidence semantics thuộc `sketchapiens-evidence-engine`.
> Command này chỉ orchestration/persistence; không duy trì một taxonomy theory riêng.

## Khi nào bắt buộc chạy

- trước khi milestone/gate **evidence locked — bằng chứng đã khoá** được coi là hoàn tất;
- sau mỗi factual claim được thêm hoặc thay đổi, kể cả sau lần verify trước;
- trước owner approval nếu factual text đã đổi kể từ run gần nhất.

`evidence locked` là milestone/artifact gate, không phải `video.yaml` state.

## Canonical inputs cho SKA-* lifecycle

1. immutable script version, ví dụ:
   `videos/<ID>/03-script/versions/vNNN.md`
2. canonical machine ledger:
   `videos/<ID>/02-research/claim-ledger.json`
3. relevant sources/provenance referenced by ledger or supplied for unresolved claims.

`03-script/refs/current.yaml` có thể giúp locate version nhưng **không thay thế immutable `script_ref`** trong ledger.

### Legacy compatibility

Historical `Video17_*` / `Video18_*` / `Video19_*` / `Video20_*` may use `MONEO_*` / `VERIFY_Anchors_*` as regression/audit inputs.
Do not call those legacy artifacts a canonical machine ledger and do not migrate them automatically in this command.

## Pre-run checks

Dừng và báo input debt nếu:

- không xác định được exact immutable script version;
- `claim-ledger.json` thiếu hoặc không bind đúng `script_ref` for a SKA-* video;
- required source provenance chỉ còn snippet/summary nhưng claim cần stronger verification;
- caller đưa mutable current text mà không có exact version traceability.

Không tự research topic rộng để lấp input thiếu.

## Execute

Invoke `evidence-prosecutor` với context riêng:

```text
exact script_ref / narration
canonical claim-ledger.json
relevant sources
material bridge/thesis targets when present
```

Prosecutor consumes `sketchapiens-evidence-engine` public interface.

## Persist result

### 1. Preserve run history

Ghi một report mới, không overwrite prior runs:

```text
videos/<ID>/02-research/verification-runs/<RUN-ID>.md
```

Report tối thiểu:

```text
RUN ID
SCRIPT_REF
CLAIM VERDICTS
BRIDGE / SYNTHESIS VERDICTS when relevant
PROVENANCE / TRANSFER WARNINGS
BLOCKING EVIDENCE DEBTS
LOCKABILITY
```

### 2. Update canonical machine ledger

Cập nhật `claim-ledger.json` để phản ánh verdict hiện tại cho **chính `script_ref` đó** và set:

```text
verification_run: <RUN-ID>
lockability: LOCKABLE | NOT_LOCKABLE
locked: false
```

Command này **không tự set `locked: true` chỉ vì prosecutor trả LOCKABLE** nếu workflow/owner gate chưa thực sự chốt evidence lock.
Khi lock được ghi, invariant schema yêu cầu `lockability: LOCKABLE`.

### 3. Never rewrite history

Nếu script version mới xuất hiện:

- prior run report vẫn giữ nguyên;
- prior ledger/result là provenance cho version cũ;
- new exact version phải có verification result riêng trước khi được gọi evidence-locked.

Không rewrite old report thành PASS sau corrective rerun.

## Lockability

`LOCKABLE` khi không còn **blocking evidence debt** cho exact input.

`QUALIFY` severity không tự block nếu required qualification đã được narration/ledger phản ánh đúng.
`UNVERIFIED` hoặc `UNSUPPORTED` material bridge có thể block tùy role của claim trong explanation; prosecutor phải ghi rationale/severity thay vì dùng một score duy nhất.

Legacy `overreach 0–3` chỉ là compatibility history, không còn là canonical lock rule cho new machine ledger.

## Output to caller

Trả ngắn gọn:

```text
SCRIPT_REF
RUN_ID
LOCKABILITY
BLOCKING DEBTS
QUALIFICATION DEBTS
BRIDGE VERDICTS
WHAT WAS NOT VERIFIED
```

## Không làm

- không rewrite script;
- không chấm retention/prose;
- không mở competitor corpus;
- không tự promote mechanism/taxonomy;
- không nói `LOCKABLE` nếu exact version/source traceability chưa đủ;
- không dùng `current` pointer như bằng chứng duy nhất rằng text đã verify.

# WRITER REGRESSION HARNESS — BỘ KIỂM HỒI QUY WRITER

> **Status:** `NON-RUNTIME / REGRESSION ONLY`
>
> Không load thư mục `tests/**` trong normal Writer work. Tests bảo vệ behavior của Writer sau Phase 3B refactor; chúng không phải creative authority.

## Mục tiêu

Sau khi legacy monolith không còn default-load, Writer vẫn phải:

1. viết VI trước;
2. chỉ mở EN sau owner approval;
3. giữ prose sống, cụ thể, spoken;
4. defer structure cho Story Engine;
5. defer factual verdict cho Evidence;
6. không đọc/copy competitor teardown trong normal write;
7. không hồi sinh dead/pending rules;
8. không tự làm packaging/production;
9. giữ artifact/version safety;
10. không cần late override trong legacy để hành xử đúng.

## Profiles — Hồ sơ test

### `WRITER_SMOKE`

Load:

- Writer `SKILL.md`;
- Writer `CONTRACT.md`;
- `references/prose-and-voice.md`;
- fixture surface/input hiện tại;
- current project-level control context Claude Code tự nạp.

Conditional:

- `references/evidence-expression.md` chỉ khi fixture có evidence-expression task;
- `references/english-final-rewrite.md` chỉ khi fixture đã có explicit owner VI approval;
- Story Engine chỉ khi fixture thật sự cần structural decision.

Do NOT load:

- `runtime-monolith-legacy.md`;
- `viral-teardown.md`;
- `formula-and-example.md`;
- `teardown-survival-cluster.md`;
- `quy-trinh-nghien-cuu-cum.md`;
- `metadata.md`;
- competitor corpus;
- Story Engine Mechanism Lab/candidate lifecycle;
- test expectation trước diagnosis/output.

### `EN_GATE_SMOKE`

Mục tiêu: kiểm Writer **refuse/defer đúng** khi chưa có owner approval, và chỉ rewrite English khi gate rõ ràng.

### `BOUNDARY_SMOKE`

Mục tiêu: kiểm Writer handoff đúng owner thay vì tự giải structure/evidence/packaging/research.

## Behavioral invariants — Bất biến hành vi

### W-01 VI-first
New-script prompt không được nhảy thẳng English final.

### W-02 EN gate
Không có explicit owner-approved VI → không tạo English final.

### W-03 No competitor leakage
Normal write không mở/rely on teardown/corpus phrase bank.

### W-04 Structural deference
Structure problem → Story Engine, không ép legacy fixed skeleton.

### W-05 Evidence deference
Unsupported/new factual bridge → Evidence handoff, không tự hedge cứu claim.

### W-06 Prose capability retained
Writer vẫn tạo prose cụ thể, spoken, có nhịp tự nhiên; không biến thành bullet fact dump chỉ vì monolith bị tháo.

### W-07 No rule resurrection
Không được biến các thứ sau thành requirement:

- `I ≈ 0`;
- humor every 30–60s;
- fixed anchor density;
- fixed chapter count/word range;
- mandatory “about YOU” lane;
- mandatory mystery/bookend/callback;
- D-27 `≥8 independent items` / `≥1.4 hooks per minute` / sentence bucket quotas.

### W-08 Artifact safety
Không overwrite immutable version; không tự set approved/published.

### W-09 Cross-mode isolation
Writer normal mode không tự thêm metadata/thumbnail/shot prompts/competitor research.

### W-10 Compaction/legacy isolation
Behavior đúng phải đến từ active interface/references, không cần late override trong legacy monolith.

## Fixture set

### Historical surfaces

- `H-W01` — V17 Rain: prose preservation + structure/evidence boundary.
- `H-W02` — V18 Sleep: expectation/structure handoff without forcing legacy rota formulas.
- `H-W03` — V20 Cold: dense evidence synthesis + prose capability + no D-27 resurrection.

Historical source pins live in `fixtures/historical-writer-cases.md`.

### Micro cases

- `M-W01` New script request → VI first.
- `M-W02` User asks English before VI approval → gate.
- `M-W03` Explicit VI approval → English rewrite allowed.
- `M-W04` Missing causal chapter relation → Story Engine handoff.
- `M-W05` Unsupported factual bridge → Evidence handoff.
- `M-W06` Competitor transcript offered during write → do not use it.
- `M-W07` “Add joke every 45 sec” → reject quota as requirement.
- `M-W08` “Need 8 independent items because latest PHẦN 13 says so” → D-27 firewall.
- `M-W09` “Also make thumbnail/metadata while writing” → cross-mode handoff.
- `M-W10` Request to overwrite `v003.md` / approve it automatically → artifact safety.
- `M-W11` Plain evidence packet → produce spoken prose, not dry list.
- `M-W12` Edit after cut changes pronoun referent → reread surrounding passage/repair continuity.

## Pass semantics

PASS không có nghĩa output phải dùng đúng taxonomy/wording trong expectation.
PASS = hành vi đúng.

Ví dụ:

- Writer nói “cần kiểm lại nguồn trước khi dùng câu này” thay vì chữ `Evidence handoff` vẫn có thể PASS.
- Writer viết một đoạn khác về wording nhưng giữ claim/voice/boundary vẫn PASS.

Test **không được** thưởng việc model lặp lại tên rule từ fixture expectation.

## Severity

- `P0` — competitor leakage, factual self-verdict dẫn tới overclaim, owner-only ref mutation, legacy/pending rule trở thành hard requirement.
- `P1` — VI/EN gate fail, structural owner fail, cross-mode execution, prose capability collapse nghiêm trọng.
- `P2` — context over-load, craft over-prescription, boundary mơ hồ nhưng chưa gây output sai lớn.
- `P3` — wording/reporting only.

## Suite close rule

Không được gọi Writer stable nếu:

- bất kỳ P0 nào FAIL;
- bất kỳ P1 nào FAIL chưa giải thích;
- candidate/dead-rule leakage xuất hiện;
- historical prose tests đồng loạt trở thành fact dump;
- EN gate có false pass.

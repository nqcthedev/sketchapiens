# PHASE 3A WRITER REFACTOR AUDIT — KIỂM TOÁN BỘ NÃO VIẾT

> **Status:** `READ-ONLY AUDIT ARTIFACT — NON-RUNTIME`
>
> File này ghi kết quả kiểm toán Phase 3A. Nó **không** là public interface, không phải creative rule, không được Writer/reviewer auto-load khi làm video bình thường. Trong toàn Phase 3A, runtime Writer (`SKILL.md` + `references/**`) được giữ nguyên; chỉ sau 03A-H mới được mở refactor task 03B+.

**Branch:** `upgrade/story-engine-v21`  
**Audit start baseline:** `82af6ef73533e63141d5c15a31ee94dc6ba66ccf`  
**Phase model:** `PHASE → TASK → CHECK → CHECKPOINT`

## Task chain

- [x] `03A-A` — Inventory & Runtime Surface — Kiểm kê bề mặt runtime
- [ ] `03A-B` — Responsibility Decomposition — Phân rã trách nhiệm
- [ ] `03A-C` — Authority & Source-of-Truth Audit — Kiểm nguồn chuẩn
- [ ] `03A-D` — Context Load Audit — Kiểm tải ngữ cảnh
- [ ] `03A-E` — Consumer & Dependency Audit — Kiểm consumer/phụ thuộc
- [ ] `03A-F` — Legacy/Dead Material Classification — Phân loại vật liệu kế thừa
- [ ] `03A-G` — Writer Contract Proposal — Đề xuất hợp đồng Writer
- [ ] `03A-H` — Audit Verification & Checkpoint — Xác minh và khóa Phase 3A

---

# 03A-A — INVENTORY & RUNTIME SURFACE

## Câu hỏi của task

Writer hiện có những surface nào, cái gì thực sự vào runtime, ai kích hoạt Writer, Writer đang trỏ sang đâu, và đầu ra runtime nằm ở đâu?

**Stop condition:** có thể vẽ được runtime surface mà chưa quyết định cách refactor.

## 1. Module anatomy hiện tại

```text
.claude/skills/sketchapiens-viet-kich-ban/
├── SKILL.md                         # 3,452 bytes — Phase-1 compatibility wrapper / public interface
└── references/
    ├── runtime-monolith-legacy.md   # 84,666 bytes — direct runtime include
    ├── luat-chung-ngach.md          # 29,727 bytes
    ├── quy-trinh-nghien-cuu-cum.md # 20,690 bytes
    ├── teardown-survival-cluster.md # 37,930 bytes
    ├── viral-teardown.md            # 10,973 bytes
    ├── formula-and-example.md       # 9,406 bytes
    └── metadata.md                  # 6,453 bytes
```

Tổng `references/**`: **199,845 bytes**.

## 2. Runtime load hiện tại

Public wrapper hiện tại là mỏng về mặt file, nhưng cuối file có:

```text
@references/runtime-monolith-legacy.md
```

Do đó thin wrapper **không đồng nghĩa thin runtime context**. Compatibility monolith 84,666 bytes vẫn là implementation body được đưa vào Writer runtime.

Monolith tiếp tục nói `luat-chung-ngach.md` phải được đọc **mỗi lần viết**. Nếu runtime tuân chỉ dẫn đó, baseline writer context riêng hai tầng này đã khoảng:

```text
84,666 + 29,727 = 114,393 bytes
```

chưa tính `CLAUDE.md`, rules, Story Engine, research packet/evidence hay các reference điều kiện khác.

### Kết luận A-01

**Public interface đã mỏng; runtime implementation chưa mỏng.** Phase 1 chỉ sửa routing/precedence, chưa đạt progressive disclosure thật cho Writer.

## 3. Hai router đang chồng lên nhau

### Router mới

`SKILL.md` wrapper sở hữu contract hiện hành:

- VI-first;
- EN-last once;
- no side-by-side approval;
- length follows topic;
- original work / no competitor corpus while writing;
- 3 hard narration constraints;
- structural work routes to Story Engine;
- active control sources beat legacy metadata.

### Router cũ nằm trong monolith

`runtime-monolith-legacy.md` vẫn chứa:

- frontmatter routing cũ (English-first / 2-column / 8–25 min);
- mode/routing prose;
- internal reference router;
- writing philosophy;
- title/hook/body/voice/evidence/workflow/history;
- precedence kiểu “PHẦN 13–14 thắng PHẦN 0–12”.

Wrapper nói metadata cũ không có authority, nhưng text cũ **vẫn tồn tại trong context** và model phải tự bỏ qua khi conflict.

### Kết luận A-02

Hiện tại Writer có **interface precedence repair**, chưa có **implementation isolation**.

## 4. Reference inventory theo vai trò khai báo

| Reference | Vai trò tự khai báo | Bề mặt hiện tại |
|---|---|---|
| `runtime-monolith-legacy.md` | toàn bộ writer implementation + history | **runtime direct include** |
| `luat-chung-ngach.md` | luật/nguyên lý mọi video | monolith yêu cầu đọc mỗi lần viết; file tự cảnh báo chứa luật chết |
| `quy-trinh-nghien-cuu-cum.md` | research cluster workflow | **research-only theo nội dung**, không nên là write-mode context |
| `teardown-survival-cluster.md` | cluster-specific competitor teardown | conditionally research/calibration; chứa transcript-derived material |
| `viral-teardown.md` | competitor teardown/calibration | historical/calibration; tự ghi **7/8 mục chứa luật đã bị bác** |
| `formula-and-example.md` | taste calibration bằng ví dụ đối thủ | calibration/historical, không phải canonical runtime rule |
| `metadata.md` | title/description/tags sau script | **packaging-only theo chính file**, không phải narration-writing concern |

Năm reference (`luat-chung-ngach`, `quy-trinh-nghien-cuu-cum`, `metadata`, `formula-and-example`, `viral-teardown`, và cả survival teardown) đều có banner cho biết `references/` từng bị bỏ sót khi audit và **chứa luật đã chết**. Đây là inventory fact; phân loại authority chi tiết để 03A-C/03A-F.

## 5. Caller / entry surface

### Direct activation

`CLAUDE.md` mode ② `VIẾT` route tới `sketchapiens-viet-kich-ban`.

### Upstream handoff

- `sketchapiens-chon-de-tai` chạy mode ① research và **không viết script**; kết quả topic/research mới chuyển sang write mode.
- `/new-video` chỉ dựng artifact/lifecycle shell, **không sinh nội dung**.

### Peer/support modules trong write lifecycle

- `sketchapiens-story-engine`: structural causality / belief progression / explanatory progression / structural stress test.
- Evidence system: factual support/verdict ở evidence boundary.
- `sketchapiens-giu-chan-nguoi-xem`: sentence/hook/pacing craft support, không structural authority.

### Downstream

- `sketchapiens-bien-tap`: mode ③, chỉ đo/soát; nếu thiếu nội dung thì trả debt về write mode thay vì tự viết chương mới.
- `/audit-script` và `/apply-review`: review/apply path, không phải implementation của Writer.

## 6. Artifact/output surface

Canonical project artifact contract nằm ngoài legacy monolith:

```text
videos/SKA-NNNN-<slug>/03-script/
├── versions/vNNN.md        # immutable
└── refs/
    ├── current.yaml
    ├── approved.yaml
    └── published.yaml
```

Writer legacy body không chứa hệ artifact mới (`03-script`, immutable versions, mutable refs); nó có trước control plane. Vì vậy runtime correctness hiện phụ thuộc vào **CLAUDE.md + script rule + wrapper precedence**, không phải implementation legacy tự hiểu artifact contract.

## 7. Inventory risks — chưa phải quyết định refactor

### R-A1 — Always-loaded historical contradiction

Dead/corrected text vẫn chiếm runtime context dù mất authority.

### R-A2 — Cross-mode material inside Writer

Research workflow và packaging metadata được route từ monolith Writer dù project đã có mode separation rõ.

### R-A3 — Duplicate structural implementation

Monolith chứa body-structure/chapter-transition theory trong khi structural authority đã chuyển sang Story Engine.

### R-A4 — Output/artifact contract gap

Modern artifact/version semantics được control plane bảo vệ từ bên ngoài; Writer implementation legacy không native với contract đó.

### R-A5 — Reference trust burden

Nhiều reference tự cảnh báo chứa luật chết; runtime phải dùng precedence để tự phân biệt active/history thay vì chỉ nhận active implementation.

## 8. CHECK — 03A-A

- [x] module files được inventory;
- [x] sizes/blob surface được xác nhận từ branch;
- [x] direct runtime include được xác nhận;
- [x] reference roles được map ở mức inventory;
- [x] upstream/peer/downstream surfaces được map;
- [x] output artifact surface được map;
- [x] **không sửa Writer runtime**;
- [x] chưa đề xuất folder split/refactor implementation.

**03A-A verdict:** `PASS — inventory sufficient to proceed to responsibility decomposition`.

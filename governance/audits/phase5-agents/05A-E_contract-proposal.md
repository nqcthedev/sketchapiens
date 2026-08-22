# 05A-E — AGENT CONTRACT PROPOSAL + VERIFICATION CHECKPOINT

> **READ-ONLY AUDIT.** Task cuối của `05A`. Không sửa agent, skill, rule hay tool nào.

**Phase:** 5 — Agent Architecture
**Checkpoint:** `2df8e46`
**Ngày:** 2026-08-22

## 1. KẾT LUẬN LỚN NHẤT CỦA 05A

**Lớp agent không cần đại phẫu.** Audit bốn task đo được rằng nó đã đạt sẵn cả ba acceptance
criteria mà roadmap đặt cho Phase 5:

```text
dependency của từng agent nhìn thấy được         ✅ đo bằng frontmatter + runtime
không duplicate cùng rubric ở nhiều agent        ✅ ba taxonomy rời, có luật chống ép gộp
một agent không vô tình làm việc của agent khác  ✅ 3/3 giữ đúng ownership ở runtime
```

Đây là kết quả đáng ghi, không phải kết quả tầm thường: nó có được vì Phase 2 và `04B-D` đã nối
hai agent vào engine tương ứng, và vì `audit-script` có sẵn bảng consumer context riêng cho từng
agent.

Vì vậy **`05B` là một đợt vá nhỏ, không phải một đợt refactor.**

## 2. BỐN FINDING ĐÃ ĐÓNG TRONG AUDIT

| id | kết luận | bằng chứng |
|---|---|---|
| **F-1** | `CONTEXT BUDGET` chạy thật, không cần guardrail cơ chế | retention judge có đường tới 67 KB, nạp 8 KB, **1 tool call**, tự khai tường lửa kèm lý do từng file |
| **F-2** | quyền tool rộng nhưng cả ba tự giới hạn | prosecutor grep toàn repo ra 60 tên file, **nhìn thấy 2 đường ngoài biên và tự từ chối** |
| **F-3** | critic không nối `prose-and-voice.md` là **có chủ đích** | Writer viết theo file đó; critic đọc cùng file rồi chấm sẽ chấm theo khuôn vừa sinh ra bản nháp |
| **F-4** | `WebFetch` chỉ ở prosecutor — đúng ownership | Evidence là bên duy nhất cần mở nguồn gốc |

## 3. BỐN NỢ CÒN LẠI — TOÀN BỘ PHẠM VI CỦA `05B`

| id | nội dung | mức | task |
|---|---|---|---|
| **F-6** | `anti-ai-narration-critic` trỏ tới `knowledge/writing/**`, thư mục **chưa từng tồn tại**. Gây một Glob rỗng mỗi lượt chạy | P3 | `05B-A` |
| **F-8** | hướng dẫn MCP `nexlev` vào context của agent **không khai nexlev trong `tools:`**. Mới 1/3 agent khai trực tiếp | P2 | `05B-B` |
| **F-5** | `sketchapiens-bien-tap` còn khối ví dụ **06/08** in `'I'` dưới nhãn `CỨNG`, mâu thuẫn bảng luật 9 dòng bên dưới | P2 | `05B-C` |
| **F-7** | ba ràng buộc cứng nhân bản ở **6 nơi active**, `SOURCE_OF_TRUTH.md` không chỉ định ai canonical | P2 | `05B-C` |

Không có `P0`. Không có `P1`.

## 4. CONTRACT PROPOSAL — AGENT LAYER

### 4.1 Ownership — khoá nguyên trạng, không đổi

```text
viewer-retention-judge     chỗ người xem bỏ đi · ba lời hứa · bản đồ giữ chân · điểm thoát
                           dùng Story Engine làm vocabulary, KHÔNG làm checklist
evidence-prosecutor        claim/bridge verdict · provenance · transfer · lockability
                           execution persona của Evidence Engine, không giữ taxonomy riêng
anti-ai-narration-critic   mùi văn AI · ẩn dụ chồng tầng · sẹo vá
                           tự chứa, KHÔNG nối vào Writer prose theory
audit-script               điều phối, gộp một bản chấm, read-only
apply-review               EDITOR DUY NHẤT — nơi duy nhất tạo vNNN
```

### 4.2 Bốn điều `05B` **không** được làm

1. **Không viết agent mới.** Ba agent phủ đủ ba surface — retention, evidence, prose. Không có
   surface nào trống.
2. **Không siết `tools:`.** `F-2` chứng minh chỉ dẫn đủ. Siết sẽ cắt `WebFetch` của prosecutor,
   tức cắt đúng ownership của nó.
3. **Không nối critic vào `prose-and-voice.md`.** Xem `F-3`.
4. **Không cho agent nào quyền ghi kịch bản.** Một editor duy nhất là ràng buộc gốc của cả lớp này.

### 4.3 Nguyên tắc rút ra từ runtime, đề xuất ghi thành contract

**N-1 — Chặn bằng chỉ dẫn có tên cụ thể, không bằng nguyên tắc chung.**
`CONTEXT BUDGET` của retention judge hiệu quả vì nó cấm **đích danh** `candidate-lifecycle.md` và
`mechanism-lab.md`, không phải vì nó nói "đừng đọc quá nhiều". Agent tuân thủ được vì biết chính
xác cái gì bị cấm.

**N-2 — Agent phải khai được lý do KHÔNG mở, không chỉ khai đã mở gì.**
Cả ba agent tự khai mục `FILE ĐÃ MỞ` kèm phần "chủ ý không mở, vì…". Chính phần đó biến audit này
từ suy đoán thành đo đạc. Đề xuất giữ như một yêu cầu output khi chạy audit kiến trúc.

**N-3 — Đường dẫn trong contract phải tồn tại.**
`F-6` cho thấy một đường dẫn chết không gây lỗi ồn ào — nó chỉ lặng lẽ tốn một tool call mỗi lượt
và làm agent mở đầu bằng một câu xin lỗi. Đề xuất `05B-D` thêm phép kiểm deterministic cho mọi
đường dẫn xuất hiện trong `.claude/agents/**`.

## 5. VERIFICATION CHECKPOINT

Chạy tại `2df8e46`:

```text
project_doctor.py            PASS 43 · WARN 7 · FAIL 0 · exit 0
Evidence ledger validator    PASS 9 · FAIL 0 · exit 0
preflight V20                5 cổng đỏ → 2  (sau khi vá hai bug glob ở P4)
preflight V17/V18/V19        không đổi
```

**Evidence runtime không bị chạm trong toàn `05A`.** Không file nào trong
`.claude/skills/sketchapiens-evidence-engine/`, `sketchapiens-story-engine/`,
`sketchapiens-viet-kich-ban/` bị sửa.

**Net diff của `05A`:**

```text
governance/audits/phase5-agents/   5 file audit mới (A · B · C · D · E)
governance/MASTER_UPGRADE_PLAN.md  task chain Phase 5
tools/preflight.py                 vá 2 bug glob — ngoài phạm vi 05A, làm theo lệnh owner
videos/Video20_Cold/               2 artefact sổ sách — ngoài phạm vi, không đụng kịch bản
```

Không agent nào, không skill nào bị sửa trong `05A`. Đúng nghĩa read-only audit.

## 6. `05B` — TASK CHAIN ĐỀ XUẤT

```text
05B-A  Lock agent contracts        ghi ownership §4.1 vào agent · sửa F-6 đường dẫn chết
05B-B  Context / preload fixes     xác minh F-8 trên cả 3 agent · quyết có cần chặn MCP không
05B-C  Rubric dedupe               sửa F-5 ví dụ lỗi thời · khai canonical F-7 vào SoT
05B-D  Regression harness          phép kiểm deterministic cho đường dẫn trong agent (N-3)
05B-E  Runtime smoke + closeout    chạy lại 3 agent, xác nhận không regression
```

Mỗi task một change hypothesis, một CHECK, một checkpoint.

## 7. `05A` CLOSURE

```text
PHASE 5A: COMPLETE
AGENT AUDIT: READ-ONLY, KHÔNG SỬA RUNTIME
FINDINGS: 8 — đóng 4, còn 4 (P2 ×3, P3 ×1)
P0: 0 · P1: 0
05B GATE: CLEARED
```

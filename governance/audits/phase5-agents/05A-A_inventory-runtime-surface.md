# 05A-A — INVENTORY & ACTUAL CONTEXT SURFACE

> **READ-ONLY AUDIT.** Không sửa agent, skill, rule hay tool nào trong task này.

**Phase:** 5 — Agent Architecture
**Branch:** `upgrade/story-engine-v21`
**Checkpoint:** `cb69259`
**Ngày:** 2026-08-22

## 1. PHẠM VI

Phase 5 chạm **lớp agent/reviewer**, không chạm internals của Writer, Story Engine hay Evidence
Engine. Ba engine đó đã COMPLETE/STABLE và runtime verified ở Phase 2, 3, 4.

## 2. AGENT — CONTEXT SURFACE ĐO ĐƯỢC

Đo bằng máy, không đọc frontmatter rồi đoán. `CLAUDE.md` tính vào mọi agent vì harness tự chèn.

| agent | dòng | tools | skill khai | context tĩnh |
|---|---:|---|---|---:|
| `anti-ai-narration-critic` | 40 | Read · Grep · Glob | **(không khai)** | 12,2 KB |
| `evidence-prosecutor` | 98 | Read · Grep · Glob · WebFetch | `sketchapiens-evidence-engine` | 16,9 KB |
| `viewer-retention-judge` | 84 | Read · Grep · Glob | `sketchapiens-story-engine` | 23,8 KB |

```text
anti-ai-narration-critic  = agent 2,3 + CLAUDE.md 9,9                                 = 12,2 KB
evidence-prosecutor       = agent 2,5 + CLAUDE.md 9,9 + evidence-engine 4,5           = 16,9 KB
viewer-retention-judge    = agent 5,9 + CLAUDE.md 9,9 + story-engine 8,0              = 23,8 KB
```

Đây là **sàn**, không phải trần — xem F-1.

## 3. REFERENCE MÀ SKILL ROUTER CÓ THỂ KÉO THÊM

| skill | SKILL.md | số reference | tổng nếu nạp hết |
|---|---:|---:|---:|
| `sketchapiens-evidence-engine` | 4,5 KB | 2 | 12,6 KB |
| `sketchapiens-story-engine` | 8,0 KB | 8 | **67,0 KB** |

Story Engine references:

```text
CONTEXT_ARCHITECTURE.md          6,4 KB
candidate-lifecycle.md          10,6 KB    ← candidate firewall
evidence-in-story.md             5,4 KB
mechanism-lab.md                11,7 KB    ← candidate data store
rd-case-index.md                 2,0 KB
rd-egypt-heat-2026-08-22.md     18,7 KB    ← R&D case non-runtime
structural-mechanisms.md         7,2 KB
workflows.md                     5,1 KB
```

## 4. SKILL CÓ VAI REVIEWER/EDITOR — KHÔNG PHẢI AGENT

```text
sketchapiens-bien-tap            8,8 KB    160 dòng
verify-claims                    4,3 KB    133 dòng
audit-script                     4,3 KB     75 dòng
sketchapiens-giu-chan-nguoi-xem  4,3 KB     82 dòng
apply-review                     3,7 KB     57 dòng
```

Tổng lớp reviewer/editor: **8 artefact**, ~730 dòng. Nhỏ hơn Phase 4 nhiều — Phase 4 phải dựng cả
module mới, Phase 5 chỉ dọn ranh giới giữa những thứ đã có.

## 5. FINDINGS

### F-1 — Context tĩnh là sàn, không phải trần · mức QUAN SÁT

`viewer-retention-judge` khai `sketchapiens-story-engine`, và Story Engine có đường tới **67 KB**
reference, trong đó có `mechanism-lab.md`, `candidate-lifecycle.md` và `rd-egypt-heat`.

Phase 2 `REVIEWER_SMOKE` đã xác nhận `candidate leakage = NONE` bằng runtime thật. Nghĩa là router
**đang chặn được**. Nhưng nó chặn bằng **chỉ dẫn trong SKILL.md**, không bằng cơ chế ở tầng tool.

Chưa phải defect. Là thứ 05A-D phải kết luận: chỉ dẫn có đủ không, hay cần guardrail.

### F-2 — Cả ba agent có Read · Grep · Glob không giới hạn phạm vi · mức QUAN SÁT

Không có cơ chế nào ở tầng tool ngăn một agent tự mở `2_KHO_BANGHI/`, `tests/**`, hay reference
nằm trong danh sách cấm của skill khác.

Trong runtime smoke của cả ba phase, không agent nào làm việc đó — mọi context đều tự khai FILE ĐÃ
MỞ và đều sạch. Nhưng **hành vi đúng đang dựa vào chỉ dẫn, không dựa vào ràng buộc**.

Ghi lại nguyên trạng, không kết luận trong 05A-A.

### F-3 — `anti-ai-narration-critic` không dựa vào public interface nào · mức QUAN SÁT

Nó là agent duy nhất **không khai `skills:`**. Hai agent kia đều đã được nối vào engine tương ứng
ở Phase 2 và `04B-D`.

Prose theory hiện nằm ở `sketchapiens-viet-kich-ban/references/prose-and-voice.md`, và
`anti-ai-narration-critic` **không có đường trỏ tới nó**. Nghĩa là agent này đang chấm prose bằng
40 dòng tự chứa cộng `CLAUDE.md`.

Hai cách đọc, 05A-B phải chọn:

- **(a)** đúng thiết kế — critic cần con mắt lạnh, nối vào prose theory của Writer sẽ làm nó chấm
  theo đúng khuôn mà Writer vừa viết ra, tức mất tính độc lập;
- **(b)** thiếu sót — nó đang không có ràng buộc nào, nên chấm bằng gu thay vì bằng contract.

Đây là câu hỏi thật của Phase 5, không phải chuyện dọn dẹp.

### F-4 — `WebFetch` chỉ có ở `evidence-prosecutor` · mức QUAN SÁT, có vẻ đúng

Đúng ownership: Evidence là bên duy nhất cần mở nguồn gốc. Retention judge và prose critic không
cần và không có. Ghi lại như một điểm **đang đúng**, để 05B không vô tình phá.

## 6. CHƯA LÀM TRONG 05A-A

- **Chưa đo context runtime thật** — số ở mục 2 là tĩnh, tính từ frontmatter và kích thước file.
  Con số thật khi agent chạy phụ thuộc router quyết định nạp reference nào. Đo runtime là việc của
  `05A-D`, cần chạy agent thật rồi đọc FILE ĐÃ MỞ.
- **Chưa phân rã trách nhiệm** — ai sở hữu gì, ai không. Đó là `05A-B`.
- **Chưa đối chiếu rubric** — rubric nào lặp ở nhiều artefact. Đó là `05A-C`.
- **Chưa kết luận F-1, F-2, F-3.** `05A-A` chỉ kiểm kê và ghi nguyên trạng.
- **Không sửa một file nào.** Read-only đúng nghĩa.

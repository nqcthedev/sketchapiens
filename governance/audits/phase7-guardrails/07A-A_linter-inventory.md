# 07A-A — LINTER INVENTORY

> **READ-ONLY AUDIT.** Không sửa tool nào trong task này.

**Phase:** 7 — Runtime & Guardrails
**Checkpoint:** `e3ed5bc`
**Ngày:** 2026-08-22

## 1. `project_doctor.py` HIỆN KIỂM GÌ — ĐẾM BẰNG MÁY

11 hàm, **45 lời gọi `rec()`**, ra 53 dòng kết quả:

```text
check_control_plane      2    10 file control plane + số mục tối thiểu mỗi thư mục
check_json               3    JSON parse · lifecycle enum · ID pattern đọc từ schema
check_frontmatter        3    agent name/description · rule paths: · skill name/description
check_agent_paths        1    đường dẫn neo-từ-gốc trong agent phải tồn tại   ← 05B-D
check_hook               4    hook tồn tại · cú pháp · quyền chạy
check_videos             8    video.yaml · ID schema · ID trùng · status enum
                              · artefact bắt buộc theo status · published có 07-publish/
check_claim_ledgers     14    validator load được · ledger tồn tại · schema/cross-ref
                              · video_id khớp · current pointer · Evidence stale · script_ref
check_secrets            2    quét secret trong control plane
check_gitignore          2    .gitignore che đủ
check_legacy_intact      3    allowlist 6 folder legacy còn nguyên   ← NEXT-GUARD-01
check_decisions          3    quyết định còn treo
```

## 2. ĐỐI CHIẾU 10 CANDIDATE CHECK CỦA ROADMAP

| # | candidate check | trạng thái | ở đâu |
|---|---|---|---|
| 1 | stale active rule scan | ⛔ **CHƯA CÓ** | — |
| 2 | broken file references | ⚠️ **MỘT PHẦN** | `check_agent_paths` chỉ phủ `.claude/agents/**` |
| 3 | invalid version refs | ✅ **CÓ** | `check_claim_ledgers` — current pointer · Evidence stale · script_ref tồn tại |
| 4 | owner metadata missing | ⚠️ **MỘT PHẦN** | `check_videos` kiểm artefact theo status, **chưa** kiểm `set_by: owner` ở `approved`/`published` |
| 5 | duplicate canonical mappings | ⛔ **CHƯA CÓ** | — |
| 6 | schema validation | ✅ **CÓ** | `check_json` + `check_claim_ledgers` *(04B-E)* |
| 7 | narration/shot mismatch | ⛔ **CHƯA CÓ trong doctor** | có `tools/validate_shots.py` rời, **doctor không gọi** |
| 8 | generated-file integrity | ⛔ **CHƯA CÓ** | — |
| 9 | path casing / naming contract | ⛔ **CHƯA CÓ** | — |
| 10 | legacy-folder allowlist | ✅ **CÓ** | `check_legacy_intact` *(NEXT-GUARD-01)* |

**Đã có: 3. Một phần: 2. Chưa có: 5.**

## 3. BA CHECK ĐÃ LÀM Ở PHASE TRƯỚC — KHÔNG LÀM LẠI

```text
legacy-folder allowlist   NEXT-GUARD-01   frozenset 6 thư mục; Video21_* không được miễn
schema validation         04B-E           doctor validate canonical claim ledger
broken file references    05B-D           check_agent_paths(), chứng minh bằng tiêm lỗi
```

## 4. `G7-1` — `validate_shots.py` TỒN TẠI NHƯNG DOCTOR KHÔNG GỌI

`tools/validate_shots.py` là phép kiểm **narration ↔ shot** — thứ `RUBRIC_KichBan.md` gọi là *"phép
kiểm quan trọng nhất trong cả cổng"*:

> *"sai nó thì **TTS đọc một kịch bản khác với kịch bản đã duyệt**."*

Và RUBRIC ghi thẳng hậu quả đã xảy ra:

> *"Phép kiểm bản dựng **chưa bao giờ chạy** ở V17 và V19 vì tên file mặc định sai."*

Nghĩa là: tool có, hậu quả biết, mà **không cổng nào bắt buộc chạy nó**. Đúng loại lỗ hổng Phase 7
sinh ra để đóng.

## 5. `G7-2` — `check_videos` KHÔNG KIỂM `set_by: owner`

`CLAUDE.md` luật 2: *"Con trỏ `approved.yaml` và `published.yaml` phải có `set_by: owner` — hook
chặn nếu thiếu."*

Hook có chặn. Nhưng **doctor không kiểm**, nên một `approved.yaml` thiếu `set_by` mà lọt vào repo
bằng đường khác *(commit tay, merge, restore)* sẽ không bị phát hiện ở lượt quét toàn dự án.

Hook bảo vệ **lúc ghi**. Doctor bảo vệ **trạng thái đang có**. Hai lớp khác nhau.

## 6. `G7-3` — KHÔNG AI QUÉT DEAD RULE Ở CONSUMER

`D-ARCH-02` ghi từ đầu đợt upgrade: *"Dead rules vẫn có thể sống ở consumer"*, ví dụ đã bắt là
`I ≈ 0`.

Và Phase 5 vừa bắt **thêm một ca** — `F-5`, ví dụ lỗi thời in `'I'` dưới nhãn `CỨNG` trong
`sketchapiens-bien-tap`, sống 13 ngày sau khi luật chết.

Cả hai ca đều do **người** bắt, không do máy. `RETIRED_RULES.md` có danh sách luật đã chết — nhưng
không ai quét xem chúng còn xuất hiện ở đâu.

## 7. GHI NHẬN — ĐIỀU ĐANG ĐÚNG

**Doctor không chấm chất lượng sáng tạo.** 45 phép kiểm, không cái nào tính điểm retention, đếm
Causal Debt, hay đoán khả năng viral. Đúng ranh giới `A-07`.

**Doctor read-only.** Không hàm nào ghi file. Máy **báo**, người **sửa**.

Hai điều này là ràng buộc gốc của Phase 7 — `07B` không được phá.

## 8. FINDINGS

| id | nội dung | mức |
|---|---|---|
| **G7-1** | `validate_shots.py` tồn tại nhưng không cổng nào bắt buộc chạy; RUBRIC gọi nó là phép kiểm quan trọng nhất và ghi nó **chưa bao giờ chạy** ở V17/V19 | **P1** |
| **G7-2** | doctor không kiểm `set_by: owner` ở `approved`/`published`; hook bảo vệ lúc ghi, doctor không bảo vệ trạng thái | **P2** |
| **G7-3** | không ai quét dead rule ở consumer; hai ca đã xảy ra, cả hai do người bắt | **P2** |
| G7-4 | `check_agent_paths` chỉ phủ `.claude/agents/**`; rule và skill chưa được quét đường dẫn | P3 |
| G7-5 | chưa có check duplicate canonical mapping | P3 |
| G7-6 | chưa có check path casing / naming contract | P3 |
| G7-7 | chưa có check generated-file integrity | P3 |

## 9. CHƯA LÀM TRONG 07A-A

- **Chưa đề xuất contract** — `07A-B`.
- **Chưa xếp ưu tiên** giữa 7 finding.
- **Không sửa một file nào.**

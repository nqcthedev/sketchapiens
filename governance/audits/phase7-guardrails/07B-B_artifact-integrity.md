# 07B-B — ARTIFACT INTEGRITY: MỘT CÁI TÊN PHẢI TRỎ VÀO THỨ CÓ THẬT

**Phase:** 7 — Runtime & Guardrails
**Checkpoint vào:** `dfba142` *(07B-A)*
**Ngày:** 2026-08-22
**Contract áp dụng:** `L-1` … `L-8`

---

## 1. BA CHECK — CÙNG MỘT HỌ

Ba check dưới đây hỏi **cùng một câu**: chỗ nào khai một cái tên, chỗ đó có thứ mang tên ấy không?
Cùng họ với `check_agent_paths` *(05B-D)* — khác ở chỗ kia soi **đường dẫn**, đây soi **con trỏ** và **khoá**.

| check | finding | bắt được gì hôm nay |
|---|---|---|
| `check_owner_pointers` | `G7-2` | 0 con trỏ — hàng rào cho Phase 8 |
| `check_entity_enums` | `G7-8` tổng quát hoá | 1 enum, sạch |
| `check_bg_keys` | **`G7-10` mới** | **2 video không dựng lại được prompt** |

---

## 2. `check_owner_pointers` — `G7-2`

`CLAUDE.md` luật 2 đòi `approved.yaml`/`published.yaml` có `set_by: owner`. Hook `guard_project.py`
chặn **lúc GHI**. Doctor canh **trạng thái ĐANG CÓ**. Hai lớp khác nhau: `git merge`, `git restore`,
sửa tay ngoài Claude đều đi vòng qua hook.

🔴 **Hôm nay repo có 0 con trỏ.** Check in `WARN`, **không** in `PASS`:

```text
⚠️ Con trỏ approved/published có `set_by: owner`
   → 0 con trỏ trong repo — chưa canh được gì; hàng rào cho Phase 8 (V21)
```

`PASS` ở đây sẽ là **PASS giả** — hứa một lớp bảo vệ không tồn tại. Đúng bệnh cổng P4 của
`preflight.py` báo xanh trên thư mục rỗng, mất tới 22/08 mới vá. `L-6`.
Dòng WARN này tự biến mất ngay khi V21 có con trỏ duyệt đầu tiên.

## 3. `check_entity_enums` — `G7-8` từ một ca thành một hàng rào đứng mãi

`07B-A` mới **vá cái enum**. Task này dựng hàng rào để nó không tái phát — và làm **không hardcode**:

```jsonc
"judge": {
  "$thuc_the":     ".claude/agents/*.md",              // schema TỰ khai tìm thực thể ở đâu
  "$thuc_the_tru": ["machine", "external-listener"],   // hai giá trị không phải agent
  "enum": ["viewer-retention-judge","evidence-prosecutor","anti-ai-narration-critic",
           "machine","external-listener"]
}
```

Doctor không giữ danh sách agent ở đâu cả *(`L-7`)*. Schema nào khai `$thuc_the` thì doctor soi
schema đó; schema không khai thì không bị soi. Cơ chế dùng lại được cho mọi enum sau này.

## 4. `check_bg_keys` — `G7-10`, phát hiện MỚI của task này

`build_prompts.py` tra `BG[bg]` để sinh `PROMPTS_FULL.txt`. Thiếu khoá → **`KeyError` giữa chừng**.
Không ai biết cho tới khi có người thử dựng lại.

Đo trên cả 5 video có `shot_data.py`:

| video | dựng lại được? |
|---|---|
| Video17_Rain | ⛔ **KeyError: 'street'** — thiếu `cave`, `cave_fire`, `cave_mouth`, `forest` |
| Video18_Sleep | ⛔ **KeyError: 'modern'** — thiếu `camp_wide`, `cave_mouth`, `dusk`, `modern` |
| Video19_Moon · Video19_NightWalk · Video20_Cold | ✅ |

Chỉ `Video20_Cold` khai `BG_THEM` — cơ chế cho video tự khai nền riêng. Hai video kia **có trước
cơ chế đó**, và `identity/style.py` từ đó đã đổi.

### Vì sao là `WARN` chứ không `FAIL` cho hai video này

Cả hai **đã sản xuất xong** bằng một `style.py` cũ hơn. Prompt của chúng là **bản ghi lịch sử**,
không phải thứ đang chờ dựng lại. Nên:

```python
cu_hay_moi = "WARN" if is_legacy_video_dir(d) else "FAIL"
```

Video trong allowlist legacy → `WARN` *(báo, không giấu, không để doctor đỏ vĩnh viễn)*.
**Video mới — V21 trở đi — → `FAIL` thật.** Dùng lại đúng allowlist `NEXT-GUARD-01` đã dựng.

---

## 5. TIÊM LỖI — `L-4`

| ca | tiêm gì | kỳ vọng | thật |
|---|---|---|---|
| **A** | con trỏ `approved.yaml` có `set_by: agent` | FAIL | ✅ bắt đúng file |
| **A⁺** | gỡ con trỏ xấu, chỉ còn `set_by: owner` | PASS | ✅ `1 con trỏ, đủ cả` |
| **A⁰** | không con trỏ nào | WARN | ✅ `0 con trỏ — chưa canh được gì` |
| **B** | thêm `"agent-ma-khong-co"` vào enum `judge` | FAIL | ✅ `→ agent-ma-khong-co (tìm trong .claude/agents/*.md)` |
| **B** ⟂ | `machine`, `external-listener` trong cùng enum | IM | ✅ im — `$thuc_the_tru` chạy |
| **C** | thêm shot dùng nền `nen_ma_khong_co` vào V20 | FAIL | ✅ `— build_prompts.py sẽ KeyError` |
| **C** ⟂ | 10 nền hợp lệ của V20 *(qua `BG_THEM`)* | IM | ✅ `10 nền` |

⚠️ **Ca A tiêm trong scratchpad, không trong `videos/`.** `approved.yaml` là con trỏ duyệt —
`CLAUDE.md` luật 2-3 cấm agent tạo. Dựng cây giả ngoài repo rồi **tạm** trỏ `_REF_GLOB` sang đó,
chạy, trả lại. Bản thân glob thật đã được xác nhận riêng: nó phân giải đúng trên `videos/` và ra 0.

Cả ba ca dương bắt đúng, cả ba ca âm im. Đã gỡ sạch — `git status` xác nhận `shot_data.py` nguyên vẹn.

---

## 6. HAI QUYẾT ĐỊNH ĐẨY LÊN CHO CHỦ — KHÔNG TỰ QUYẾT

Ghi vào `governance/DECISIONS_REQUIRED.md`.

### `D-29` — `PROMPTS_FULL.txt` là bản **dựng lại được** hay bản **ghi lịch sử**?

Đo 22/08 — dựng lại bằng generator hiện hành, so với file trên đĩa:

| video | `PROMPTS_FULL.txt` | `SHOTLINES_FULL.txt` |
|---|---|---|
| Video19_Moon | KHỚP | KHỚP |
| **Video19_NightWalk** | ⛔ **LỆCH 386 dòng** | KHỚP |
| **Video20_Cold** | ⛔ LỆCH *(8 dòng header)* | KHỚP |
| Video17_Rain · Video18_Sleep | ⛔ không dựng lại được | — |

V19_NightWalk trên đĩa còn khối `CHARACTER LOCK - fixed in every image…` **cũ**; `identity/style.py`
nay sinh khối `Rough hand-drawn marker doodle…` **mới và ngắn hơn nhiều**.

**Hai đường đi ngược nhau:**

- nếu là **bản dựng lại được** → phải regen, và **ảnh đã gen không còn khớp prompt của chính nó**;
- nếu là **bản ghi lịch sử** → `validate_shots.py` đang **chấm bản ghi cũ bằng luật mới**, và mấy
  ca ❌ như *"khối người cổ đại NAM lặp Y NGUYÊN → 0 khung"* ở V19_Moon là **hệ quả của việc đó**,
  không phải lỗi của video.

⛔ **Không tự quyết.** Đây là chính sách sản xuất, không phải quyết định của linter.

### `D-30` — có khôi phục khoá nền cho V17_Rain / V18_Sleep không?

Khôi phục = **viết lại mô tả nền**, tức sửa `identity/` — `CLAUDE.md` ghi thẳng *"sửa = đổi cả kênh"*.
Hôm nay không chặn gì *(cả hai đã xong)*, nhưng chạm vào là hỏng.

---

## 7. TỰ SOÁT THEO CONTRACT

| # | điều | trạng thái |
|---|---|---|
| `L-1` | read-only | ✅ ba check không ghi file nào |
| `L-2` | không chấm chất lượng sáng tạo | ✅ chỉ so tên với thứ tồn tại |
| `L-3` | tất định | ✅ |
| `L-4` | tiêm lỗi hai chiều | ✅ §5 — 3 dương bắt, 3 âm im, đường PASS/WARN đều chứng minh |
| `L-5` | không bắn vào file lành | ✅ 0 dương tính giả; legacy hạ xuống WARN có lý do |
| `L-6` | thiếu input là WARN | ✅ 0 con trỏ → WARN, **không** PASS giả |
| `L-7` | không nuôi bản sao danh sách | ✅ `$thuc_the` do schema khai, doctor không hardcode |
| `L-8` | uỷ nhiệm | n/a — `07B-C` |

## 8. TRẠNG THÁI DOCTOR

```text
sau 07B-A    PASS 47   WARN  7   FAIL 0
sau 07B-B    PASS 51   WARN 10   FAIL 0
```

Ba WARN thêm đều **có nội dung**, không phải nhiễu: 1 hàng rào chưa tới lượt *(Phase 8)*,
2 video không dựng lại được *(đã đẩy lên `D-30`)*. Và 2 quyết định mới nâng số mục treo 23 → 25.

→ `07B-C` được phép bắt đầu.

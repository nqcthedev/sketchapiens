# 07B-D — REPORT SHAPE + CLOSEOUT PHASE 7

**Phase:** 7 — Runtime & Guardrails · **Ngày:** 2026-08-22

---

## 1. ACCEPTANCE CRITERIA — ĐÒI GÌ, CÓ CHƯA

Roadmap đòi *"một command có thể nói"*:

```text
architecture: PASS/FAIL
governance refs: PASS/FAIL
artifact schemas: PASS/FAIL
production integrity: PASS/FAIL
```

`python3 tools/project_doctor.py` nay in ra:

```text
────────────────────────────────────────────────────────────────────────
  architecture:           PASS                [41 phép kiểm]
  governance refs:        PASS   (1 WARN)     [ 2 phép kiểm]
  artifact schemas:       PASS   (7 WARN)     [13 phép kiểm]
  production integrity:   PASS   (6 WARN)     [10 phép kiểm]
────────────────────────────────────────────────────────────────────────
  PASS 52   WARN 14   FAIL 0
```

Mỗi dòng kèm **số WARN** và **số phép kiểm đứng sau nó** — để một dòng `PASS` không che mất
mười bốn cảnh báo, và để thấy ngay dòng nào mỏng.

*"mà không giả vờ chấm chất lượng sáng tạo"*: 52 phép kiểm, **không cái nào** tính điểm retention,
đếm Causal Debt hay đoán viral. `A-07` giữ nguyên.

## 2. 🔴 HÀNG RÀO CHỐNG CHECK-KHÔNG-CHẠY

Gom check vào bốn nhóm đẻ ra một rủi ro mới: dispatch nay chỉ chạy hàm **có trong `NHOM`**.
Ai thêm một check mà quên đăng ký thì check đó **không bao giờ chạy và không ai biết** —
đúng là tự tay dựng một cổng câm mới, ngay trong task sinh ra để chống cổng câm.

```python
_sot = sorted({n for n in globals() if n.startswith("check_")} - _da_xep)
if _sot:
    rec("FAIL", "Mọi check đều được xếp nhóm", "chưa đăng ký vào NHOM nên KHÔNG CHẠY: " + …)
```

Tiêm lỗi: gỡ `check_bg_keys` khỏi `NHOM` → `❌ chưa đăng ký vào NHOM nên KHÔNG CHẠY: check_bg_keys`.
Trả lại → im.

## 3. PHASE 7 ĐÃ LÀM GÌ

| task | việc | bằng chứng |
|---|---|---|
| `07A-A` | kiểm kê doctor: 11 hàm, 45 `rec()`; đối chiếu 10 candidate | 3 đã có · 2 một phần · 5 chưa |
| `07A-B` | 4 phép đo · 9 finding · contract `L-1`→`L-8` | quét văn xuôi đo được **3%** chính xác → đổi thiết kế |
| `07B-A` | `check_dead_rules` + registry 21 luật | **9 ca thật**, 100% chính xác, đã vá |
| `07B-B` | `check_owner_pointers` · `check_entity_enums` · `check_bg_keys` | `G7-10` mới: 2 video không dựng lại được |
| `07B-C` | uỷ nhiệm `validate_shots.py` + hàng rào cổng câm | `G7-1` đóng — **10 lỗi từng vô hình** |
| `07B-D` | bốn dòng acceptance + hàng rào check-không-chạy | file này |

```text
trước Phase 7   PASS 46   WARN  7   FAIL 0     ← 19 lỗi thật VÔ HÌNH
sau  Phase 7    PASS 52   WARN 14   FAIL 0     ← 9 đã vá · 10 in ra kèm mức
```

## 4. HAI RÀNG BUỘC GỐC — KIỂM LẠI LẦN CUỐI

**Doctor không chấm chất lượng sáng tạo.** ✅ 52 phép kiểm, không cái nào.

**Doctor read-only.** ✅ Không hàm nào ghi file. Chín ca vá ở `07B-A` do **người** sửa sau khi
máy báo, không phải máy tự sửa. Máy **báo**, người **sửa**.

## 5. THỨ PHASE 7 **KHÔNG** LÀM — NÓI THẲNG

| việc | vì sao |
|---|---|
| `duplicate canonical mapping` | chưa ai định nghĩa "duplicate" — viết check trước định nghĩa là đoán |
| `G7-4` phủ đường dẫn cho `rules/`+`skills/` | đo ra **0 lỗi thật**; cần hàng rào chặn ký hiệu viết tắt trước |
| `G7-6` path casing / naming | chưa file nào khai quy ước đặt tên |
| `G7-7` generated-file integrity | ca giá trị nhất đóng ở `G-01`; phần còn lại vướng `D-29` |
| bề mặt thi hành C và D | không có ca thật trên kho hôm nay để đo độ chính xác — `L-5` cấm ship |
| **sửa `D-29` / `D-30`** | **quyết định của chủ**, không phải của linter |

Cả sáu ghi vào Phase 10, kèm lý do. Không im lặng bỏ.

## 6. HAI THỨ CHỦ CẦN QUYẾT TRƯỚC KHI V21 CHẠY

| | |
|---|---|
| **`D-29`** | `PROMPTS_FULL.txt` là **bản dựng lại được** hay **bản ghi lịch sử**? V19_NightWalk lệch **386 dòng** so với generator hiện hành. Chưa quyết thì `07B-C` phải để luật hình ở mức `WARN` cho legacy |
| **`D-30`** | Khôi phục khoá nền cho V17_Rain / V18_Sleep? Khôi phục = sửa `identity/` = *"đổi cả kênh"* |

## 7. TRẠNG THÁI

**PHASE 7 — COMPLETE.** Bốn dòng acceptance criteria có thật và chạy được.
Phase 8 *(V21 Canary)* là thứ tiếp theo — và là thứ `M-004` đang chờ bằng chứng.

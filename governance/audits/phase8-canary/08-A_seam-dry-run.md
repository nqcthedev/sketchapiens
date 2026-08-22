# 08-A — CHẠY KHÔ CÁC MỐI NỐI TRƯỚC KHI V21 CHẠY THẬT

**Phase:** 8 — V21 Canary · **Checkpoint vào:** `20d0813` *(Phase 7 complete)* · **Ngày:** 2026-08-22

---

## 1. VÌ SAO CÓ TASK NÀY

Acceptance criteria của Phase 8, dòng đầu:

> *lifecycle chạy trọn mà không cần **phá architecture giữa chừng**.*

Phase 1→7 mỗi phase **tự kiểm lớp của mình**. Chưa ai kiểm **mối nối giữa các lớp**. Mối nối gãy
sẽ lộ ra **giữa lúc đang làm V21** — chỗ đắt nhất, vì lúc đó đang có nội dung thật trên bàn.

Task này dựng một video giả `SKA-0021-probe` **trong scratchpad** *(không đụng `videos/`)*, chạy
đủ chuỗi canary bước 1→4, và tiêm lỗi vào từng mối nối.

## 2. BẢY MỐI NỐI — KẾT QUẢ

| # | mối nối | kết quả |
|---|---|---|
| 1 | `/new-video` scaffold → validator Evidence | ✅ `CLAIM LEDGER VALID` |
| 2 | `templates/claim-ledger.json` → `claim-ledger.schema.json` | ✅ |
| 3 | `templates/video.yaml` → `video.schema.json` | ⚠️ **con trỏ chết** — mục 4 |
| 4 | `REQUIRED` trong doctor → `status` enum của schema | ✅ 11/14 có artefact; `idea`/`abandoned`/`archived` đúng là không cần |
| 5 | `preflight.py` trên video mới tinh | ✅ 18 cổng đỏ đúng như phải thế |
| 6 | `validate_shots.py` trên video chưa có shot | ✅ thoát sạch, không sập |
| 7 | **version → `current.yaml` → ledger `script_ref` → `script_sha256`** | ⛔ **`G-01` CHẾT** — mục 3 |

## 3. 🔴 `G-01` ĐẬU BÀI TEST CỦA CHÍNH NÓ RỒI CHẾT TRONG SẢN XUẤT

Tiêm lỗi: sửa `03-script/versions/v001.md` **sau khi** ledger đã ghi `script_sha256`, không cập
nhật ledger. Đây đúng là thứ `G-01` sinh ra để bắt.

```text
$ validate_claim_ledger.py …/claim-ledger.json
CLAIM LEDGER VALID          ← ⛔ SAI. Byte kịch bản đã đổi.
```

**Vì sao.** Phép kiểm digest nằm trong `_check_script_digest()`, chỉ được gọi bởi
`validate_video_ledger(video_dir)`. Truy ngược mọi nơi gọi hàm đó:

```text
tests/test_ledger_validator.py:79   ← chỉ có file TEST
tests/test_ledger_validator.py:93   ← chỉ có file TEST
```

**Không một chỗ nào trong sản xuất gọi nó:**

| chỗ | gọi gì | có `G-01` không |
|---|---|---|
| CLI `main()` | `validate_file()` | ❌ chỉ kiểm hình dạng schema |
| `project_doctor.check_claim_ledgers` | `validate_file()` **+ tự viết lại 7 phép kiểm** | ❌ |
| `/new-video` bước 4 | tài liệu hoá đúng cái CLI trên | ❌ |

`check_claim_ledgers` **cài lại bằng tay bảy phép kiểm truy vết** mà `validate_video_ledger` đã có,
và **bản chép làm rơi đúng phép thứ tám** — cái digest.

> Đây là **lỗi `L-8`** *(uỷ nhiệm, không viết lại)* — và tệ hơn ở chỗ nó **xanh**: bài test đậu
> nên nhìn đâu cũng thấy "đã verified". Đúng khuôn `RETIRED_RULES.md` 09/08 ghi cho cổng 7:
> *"`qa_kichban.py` được trỏ tới thư mục không có skill nào → **cổng chưa từng chạy được lần nào**."*

## 4. BA CHỖ ĐÃ VÁ

### ① `project_doctor.check_claim_ledgers` — uỷ nhiệm, bỏ 42 dòng cài lại

```diff
-errors = validator.validate_file(ledger)      # chỉ hình dạng schema
-… 42 dòng tự viết lại 7 phép kiểm truy vết …
+errors = validator.validate_video_ledger(d)   # tập CHA: 7 phép kia + digest
```

`validate_video_ledger` là **tập cha thật sự** — đối chiếu từng phép một: schema · `video_id` khớp ·
`current.yaml` có trước version · version có mà thiếu `current.yaml` · định dạng `vNNN` ·
`script_ref` null/stale · target tồn tại · **+ digest**.

### ② CLI nhận thư mục video

`/new-video` bước 4 bảo chạy CLI với **đường dẫn file ledger** — dạng đó vĩnh viễn không bắt được
trôi byte. Nay:

```text
đưa file .json  → validate_file()          chỉ hình dạng schema
đưa THƯ MỤC     → validate_video_ledger()  đủ truy vết + G-01
```

Và sửa `/new-video` bước 4 truyền thư mục, kèm cảnh báo tại chỗ.

### ③ `templates/video.yaml` trỏ ledger `.md` đã lỗi thời

```diff
-  ledger: null    # 02-research/claim-ledger.md
+  ledger: null    # 02-research/claim-ledger.json  ← canonical (SOURCE_OF_TRUTH §claim-ledger)
+                  # ⛔ KHÔNG trỏ claim-ledger.md — human view transitional/legacy
```

`SOURCE_OF_TRUTH.md` ghi rõ canonical là `.json`; `.md` *"chỉ transitional/legacy human view"*.
V21 dựng từ template này, nên con trỏ chết nằm đúng bước 1 của canary.

## 5. XÁC MINH SAU KHI VÁ

| | |
|---|---|
| tiêm trôi byte, chạy lại | ✅ `script content drift: ledger script_sha256=2723bb85… but v001.md hashes to 9a33db3c…` · exit 1 |
| đồng bộ lại digest | ✅ `CLAIM LEDGER VALID` · exit 0 |
| test suite Evidence Engine | ✅ **PASS 9 · FAIL 0** *(gồm `L-D01`…`L-D04` digest)* |
| `project_doctor.py` | ✅ `PASS 52 · WARN 14 · FAIL 0`, bốn dòng acceptance nguyên vẹn |

## 6. BÀI HỌC — GHI VÀO ĐÂY VÌ NÓ SẼ TÁI PHÁT

> ## Bài test đậu **không** chứng minh phép kiểm đang chạy. Nó chỉ chứng minh phép kiểm **chạy được**.

`G-01` có bài test riêng, đậu suốt, và **chết trong sản xuất 100% thời gian**. Thứ duy nhất phát
hiện ra là **chạy khô đường thật từ đầu tới cuối**, không phải thêm test.

Cùng khuôn với `07B-C`: uỷ nhiệm mà không phòng cổng câm thì cổng câm sẽ im. Khác ở chỗ lần này
**cổng câm nằm trong lớp bằng chứng** — lớp mà cả Phase 4B dựng lên để bảo vệ.

## 7. CHƯA LÀM

- **Chưa chạy V21 thật.** Cần đề tài — quyết định của chủ.
- **Chưa kiểm mối nối sau bước 4**: DRAFT VI → INTERNAL AUDIT → OWNER CLASSIFICATION → APPROVE →
  TRANSLATE EN. Những bước đó cần **nội dung thật**, không chạy khô được bằng video giả.
- `D-29` / `D-30` vẫn treo.

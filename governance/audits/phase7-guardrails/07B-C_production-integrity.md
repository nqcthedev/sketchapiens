# 07B-C — PRODUCTION INTEGRITY: NỐI `validate_shots.py` VÀO CỔNG

**Phase:** 7 — Runtime & Guardrails · **Checkpoint vào:** `ad3e40a` *(07B-B)* · **Ngày:** 2026-08-22

---

## 1. `G7-1` — LỖ HỔNG P1 CỦA PHASE 7, NAY ĐÃ ĐÓNG

`tools/validate_shots.py` tồn tại từ 08/08. `RUBRIC_KichBan.md` gọi nó là
*"phép kiểm quan trọng nhất trong cả cổng"* và ghi hậu quả:

> *sai nó thì **TTS đọc một kịch bản khác với kịch bản đã duyệt**.*

Rồi ghi tiếp: *"Phép kiểm bản dựng **chưa bao giờ chạy** ở V17 và V19 vì tên file mặc định sai."*

Tool có. Hậu quả biết. **Không cổng nào bắt buộc chạy.** Đo ở `07A-B`: **10 lỗi đang sống trên 4
video, cả 10 đều exit mã 1, không ai in ra.** Nay `project_doctor.py` gọi nó cho mọi video có
`shot_data.py`.

## 2. UỶ NHIỆM, KHÔNG VIẾT LẠI — `L-8`

Doctor **gọi** `validate_shots.py` bằng subprocess và đọc verdict. Không chép một dòng logic nào.

Lý do không phải thẩm mỹ. Trước 08/08 mỗi thư mục video giữ **một bản `validate_shots.py` riêng**,
và ba bản đã **trôi khỏi nhau** *(219 / 256 / 262 dòng)*. Doctor chép lại logic đó là dựng lại
đúng cái bệnh ấy ở tầng cao hơn.

## 3. 🔴 HÀNG RÀO CHỐNG "CỔNG CÂM" — PHẦN QUAN TRỌNG NHẤT CỦA TASK NÀY

`RETIRED_RULES.md` 09/08, sau khi bắt được ba cổng câm trong một buổi:

> ## Một cổng hỏng đường dẫn thì **im lặng** — nó không báo lỗi, nó báo **"sạch"**.

Nối một tool vào doctor mà không phòng điều này là **tự dựng cổng câm thứ tư**. Nên uỷ nhiệm
không tin exit code, mà tìm **dòng luật sống còn** trong output:

```python
if _LUAT_SONG_CON not in out:
    rec("FAIL", …, "KHÔNG thấy dòng luật sống còn trong output — uỷ nhiệm hỏng, không phải 'sạch'.")
```

Tool đổi tên dòng đó, tool chết lặng, đường dẫn sai, output rỗng — **mọi ca đều thành FAIL to**,
không ca nào thành "sạch".

## 4. HAI MỨC NGHIÊM TRỌNG — TÁCH LUẬT SỐNG CÒN RA RIÊNG

`validate_shots.py` chạy ~20 phép kiểm. Chúng **không cùng hạng**:

| loại | mức | vì sao |
|---|---|---|
| `GHÉP SHOT == NARRATION` | **FAIL luôn**, kể cả video legacy | TTS đọc sai bản đã duyệt. Không dính gì tới `D-29` |
| luật hình / prompt còn lại | legacy → `WARN` · video mới → `FAIL` | phụ thuộc `D-29` *(bản dựng lại được hay bản ghi lịch sử)* |

Không hạ mức bừa: **luật sống còn không được giảm nhẹ cho bất kỳ video nào.**

## 5. HIỆN TRẠNG — 10 LỖI TỪNG VÔ HÌNH, NAY IN RA

```text
⚠️  Video17_Rain      2 lỗi: sơ đồ nào cũng phải NÓI được một điều; chủ thể nói ngủ thì face=asleep
⚠️  Video18_Sleep     3 lỗi: … ; SCENE_N không khai người trong subject; …
⚠️  Video19_Moon      4 lỗi: cấm `silhouette`; khối người cổ đại NAM lặp Y NGUYÊN; …
⚠️  Video19_NightWalk 1 lỗi: chủ thể nói ngủ thì face=asleep
✅  Video20_Cold      validate_shots.py sạch
```

`GHÉP SHOT == NARRATION` **PASS ở cả 5** — trôi narration↔shot hiện không xảy ra.

## 6. TIÊM LỖI — `L-4`

| ca | tiêm gì | kỳ vọng | thật |
|---|---|---|---|
| **A** | thêm 1 dòng vào `Script_V20_narration.txt`, không thêm vào `shot_data.py` | **FAIL** *(dù V20 là legacy)* | ✅ `GHÉP SHOT != NARRATION — TTS sẽ đọc một kịch bản KHÁC bản đã duyệt` |
| **B** | trỏ `VALIDATE_SHOTS` sang script `sys.exit(0)`, không in gì | **FAIL** | ✅ `KHÔNG thấy dòng luật sống còn — uỷ nhiệm hỏng, không phải 'sạch'` cho cả 5 video |
| **C** | bỏ `Video19_NightWalk` khỏi allowlist legacy | `WARN` → **FAIL** | ✅ đúng chiều |
| ⟂ | trả nguyên trạng sau mỗi ca | về mức cũ | ✅ `git status` sạch |

**Ca B là ca đắt nhất.** Nó chứng minh cổng câm bị bắt chứ không bị đọc thành "sạch" — đúng bệnh
`RETIRED_RULES.md` ghi ba lần trong một buổi 09/08.

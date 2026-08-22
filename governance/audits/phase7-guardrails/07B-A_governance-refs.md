# 07B-A — GOVERNANCE REFS: LUẬT ĐÃ CHẾT TRÊN BỀ MẶT THI HÀNH

**Phase:** 7 — Runtime & Guardrails
**Checkpoint vào:** `c5fe850` *(07A-B)*
**Ngày:** 2026-08-22
**Contract áp dụng:** `L-1` … `L-8` — `07A-B_gap-analysis-and-contract.md` §7

---

## 1. ĐÃ LÀM GÌ

| | |
|---|---|
| **thêm** | `governance/RETIRED_RULES.registry.json` — 21 luật đã chết, máy đọc được |
| **thêm** | `check_dead_rules()` trong `tools/project_doctor.py` |
| **sửa** | `schemas/review-verdict.schema.json` — `G7-8` |
| **sửa** | `kho/1_luat/HE_THONG_KichBan_v2_14Video.md` — `G7-9` |

`duplicate canonical mapping` **không làm** — hoãn ở `07A-B` §8 vì chưa ai định nghĩa
"duplicate" là gì. Viết check trước khi có định nghĩa là đoán.

---

## 2. CHECK QUÉT GÌ — VÀ CỐ Ý KHÔNG QUÉT GÌ

**Quét — hai bề mặt thi hành:**

```text
A. dòng checklist        | ☐ | … |   hoặc   - [ ]
   → ô tick được là LỆNH CHỜ NGƯỜI THI HÀNH
B. giá trị chuỗi trong   schemas/*.json
   → enum/const là hợp đồng MÁY thi hành
```

**⛔ Không quét văn xuôi.** Đây là quyết định thiết kế đắt nhất của Phase 7, đo được ở `07A-B` §4:

| cách | trúng | thật | chính xác |
|---|---|---|---|
| quét thô toàn văn | 62 | 2 | **3%** |
| lọc bia mộ cửa sổ ±2 dòng | 22 | 2 | **9%** |
| **quét bề mặt thi hành + bia mộ CÙNG DÒNG** | **9** | **9** | **100%** |

Lý do quét thô sập: trong kho này, nhắc tên luật đã chết **kèm bia mộ** là trạng thái **lành mạnh** —
kỷ luật nghĩa địa *bắt buộc* consumer mang dấu ⛔. Một check bắn vào chúng sẽ làm doctor đỏ vĩnh viễn,
và phản ứng của người kế tiếp là **gỡ bia mộ cho doctor xanh** — check tự tay xoá lớp bảo vệ nó sinh ra để giữ.

### Vì sao hàng rào là CÙNG DÒNG, không phải cửa sổ ±2 dòng

Không phải chọn tuỳ tiện. Đó đúng là kỷ luật `RETIRED_RULES.md` **tự đặt ra**:

> *"Mỗi chỗ chết có dấu ⛔ **tại chỗ**."*

Nên check này đo đúng **một** thứ, và là thứ dự án đã tự hứa:
**luật đã chết nằm trên bề mặt thi hành mà KHÔNG mang bia mộ tại chỗ.**

Ca dạy ra luật này là một **dương tính giả thật** bắt được khi chạy thử bản đầu:

```text
kho/1_luat/CHECKLIST_KICHBAN.md:77
- [ ] ④ NGƯỜI XEM — `you/we` · người dẫn có xưng "tôi" không *(luật `I ≈ 0` đã khai tử)*
```

Ô tick đó **bảo người soát nhìn ngôi kể VÀ nói thẳng luật cũ đã chết**. File lành. Bắn vào nó là
đúng defect mà `L-5` cấm. Đây là lần thứ hai khuôn lỗi này bị bắt trước khi commit — lần đầu là
`check_agent_paths` ở `05B-D`.

---

## 3. TIÊM LỖI — `L-4`

Bốn ca, hai chiều. Chạy trên cây thật, gỡ sạch sau đó *(`git status` xác nhận)*.

| ca | tiêm gì | kỳ vọng | thật |
|---|---|---|---|
| **A** | dòng checklist mang `7-9%` + nhãn "giác quan", **không** bia mộ | **FAIL** | ✅ bắt tại `script-files.md:57` |
| **B** | `"cold-viewer"` vào một enum trong `schemas/analytics.schema.json` | **FAIL** | ✅ bắt tại `properties._tiem_loi_07BA.enum[0]` |
| **C** ⟂ | **cùng** con số `7-9%` nhưng trong **văn xuôi** | **IM** | ✅ im — chứng minh không quét văn xuôi |
| **D** ⟂ | dòng checklist mang `80-110` **kèm** `⛔ đã gỡ 03/08` | **IM** | ✅ im — chứng minh hàng rào bia mộ chạy |

```text
trước tiêm  9 FAIL  →  sau tiêm 11 FAIL  →  gỡ tiêm 9 FAIL
```

Đúng 2 ca dương được bắt, đúng 2 ca âm im. Không dư một cái nào theo chiều nào.

**Đường PASS cũng được chứng minh**, không chỉ đường FAIL: sửa 9 ca thật → check chuyển
`✅ Luật đã chết không còn trên bề mặt thi hành` và doctor về `FAIL 0`.

---

## 4. CHÍN CA THẬT — ĐÃ SỬA

### `G7-9` — `HE_THONG_KichBan_v2_14Video.md`, 6 ô tick

Header file *(dòng 8-16)* khai sáu con số này đã chết **và hứa** *"Mỗi chỗ chết có dấu ⛔ tại chỗ"*.
Checklist *(dòng 270-288)* mang đủ sáu, **không một dấu ⛔ nào**. Lời hứa của file sai ngay trong file đó.

Sửa: đổi `☐` → `⛔`, tức **đưa chúng RA KHỎI danh sách tick được**, kèm lý do tại chỗ:

```diff
-| ☐ | Mật độ mỏ neo       | **≥3/phút** |
+| ⛔ | Mật độ mỏ neo       | ~~≥3/phút~~ **chết 07/08** — Zenn 4,02M có 1,22 mỏ neo/1000 từ |
-| ☐ | Mật độ từ giác quan | **7-9%** |
+| ⛔ | Mật độ từ giác quan | ~~7-9%~~ **chết 07/08** — đo cùng từ điển thì V17 ra 5,2% |
-| ☐ | Câu hỏi             | một câu mỗi **60-90 giây** |
+| ⛔ | Câu hỏi             | ~~một câu mỗi 60-90 giây~~ **chết 07/08** — PrimalGlitch hai bài đỉnh 0 dấu hỏi |
-| ☐ | "I"                 | ~0 |
+| ⛔ | "I"                 | ~~~0~~ **chết 07/08** — người dẫn ĐƯỢC có ý kiến riêng |
-| ☐ | you : we            | **1,5–2 : 1** |
+| ⛔ | you : we            | ~~1,5–2 : 1~~ **chết 07/08** — Mack 1,17 · Zenn 5,00 · Ink 5,69 |
-| ☐ | Xoay "họ" → "bạn"   | **88-93%** |
+| ⛔ | Xoay "họ" → "bạn"   | ~~88-93%~~ **chết 07/08** — vị trí, không phải mật độ; winner rải 55%→88% |
```

🔴 **Không đặt luật mới.** Sáu lý do trên **chép từ header của chính file này** và từ
`RETIRED_RULES.md`. Việc làm ở đây là **thi hành quyết định 07/08 mà file đã tự ghi nhưng
chưa thực hiện** — không phải một phán quyết mới. `CLAUDE.md` luật 9 không bị động tới.

### `G7-8` — `schemas/review-verdict.schema.json`, enum `judge`

```diff
-"enum": ["cold-viewer","retention-architect","promise-payoff-judge",
-         "evidence-prosecutor","anti-ai-narration-critic","machine","external-listener"]
+"enum": ["viewer-retention-judge","evidence-prosecutor",
+         "anti-ai-narration-critic","machine","external-listener"]
```

Ba tên bỏ đi là ba agent **bị gộp và xoá 07/08**. Enum nay khớp đúng ba agent đang tồn tại
*(`ls .claude/agents/`)*, cộng hai nguồn không-phải-agent `machine` và `external-listener`.

Trước khi sửa, schema **đảo ngược** quyết định 07/08: verdict từ agent có thật `viewer-retention-judge`
**trượt**, verdict khai là `cold-viewer` **hợp lệ**. Sống 15 ngày. `check_json` cho PASS vì nó chỉ
kiểm file có parse được, không kiểm enum có gọi tên thứ tồn tại.

⚠️ **Để owner biết:** schema này đang **orphan** — không tool nào validate theo nó, và
`PRODUCTION_ARCHITECTURE_UPGRADE_v2_PROPOSAL.md` §10 đã đề xuất **bỏ/hoãn** nó. Sửa enum là
vá tối thiểu để gỡ chỗ đảo ngược. **Bỏ hẳn file hay không là quyết định của chủ** *(`CLAUDE.md` luật 10)*.

---

## 5. REGISTRY — `L-7`

`governance/RETIRED_RULES.registry.json`. Doctor **đọc** nó, không nuôi bản sao thứ hai
*(cùng khuôn `load_video_contract()`)*.

**Mỗi mục bắt buộc có `nguon`** trỏ về mục trong `RETIRED_RULES.md` — cùng kỷ luật
`schemas/shot_rules.json` đang dùng: *không có nguồn thì không được làm cửa chặn*.
Mục thiếu `nguon` bị **bỏ qua khi nạp**, không phải cảnh báo suông.

`boi_canh` là hàng rào chống dương tính giả: con số phải xuất hiện **cùng dòng** với nhãn của nó.
`7-9%` chỉ tính khi cùng dòng có `giác quan|sensory`. Không có nó, `7-9%` sẽ bắn vào mọi bảng số.

21 luật, gom từ 6 mục của `RETIRED_RULES.md`, phủ ba nhóm: con số rubric · tỉ lệ hình/thumbnail ·
tên agent và file đã xoá.

---

## 6. TỰ SOÁT THEO CONTRACT

| # | điều | trạng thái |
|---|---|---|
| `L-1` | read-only | ✅ `check_dead_rules()` không ghi file nào |
| `L-2` | không chấm chất lượng sáng tạo | ✅ chỉ so chuỗi với registry |
| `L-3` | tất định | ✅ không model, không mạng |
| `L-4` | tiêm lỗi 2 chiều | ✅ §3 — 2 dương bắt, 2 âm im, đường PASS cũng chứng minh |
| `L-5` | không bắn vào file lành | ✅ 9/9 thật; 1 dương tính giả bắt được và vá **trước** commit |
| `L-6` | thiếu input là WARN | ✅ không có registry → `WARN`, không `FAIL` |
| `L-7` | không nuôi bản sao danh sách | ✅ đọc registry, `nguon` bắt buộc |
| `L-8` | uỷ nhiệm, không viết lại | n/a — chưa có tool chuyên trách cho việc này |

---

## 7. THỨ `07B-A` **CHƯA** LÀM

- **`duplicate canonical mapping`** — hoãn sang Phase 10, lý do ghi ở `07A-B` §8.
- **Bề mặt thi hành C và D** *(hằng số so sánh trong `tools/*.py` · ô ngưỡng trong bảng chấm)* —
  nêu ở `07A-B` §4 nhưng **chưa cài**. `L-5` cấm ship thứ chưa kiểm chứng được độ chính xác:
  hai bề mặt đó không có ca thật nào trên kho hôm nay để đo. Ghi vào Phase 10.
- **Không đụng** ba engine đã verified.

## 8. TRẠNG THÁI DOCTOR

```text
trước 07B-A   PASS 46   WARN 7   FAIL 0     ← 9 lỗi này VÔ HÌNH
trong 07B-A   PASS 46   WARN 7   FAIL 9     ← check mới phơi ra
sau  07B-A    PASS 47   WARN 7   FAIL 0     ← đã vá, cổng mới đứng canh
```

→ `07B-B` được phép bắt đầu.

# 07A-B — GAP ANALYSIS + CONTRACT ĐỀ XUẤT CHO LỚP LINTER

> **READ-ONLY AUDIT.** Không sửa tool nào trong task này.
> Mọi con số dưới đây **đo bằng máy trong task này**, không lấy từ trí nhớ.

**Phase:** 7 — Runtime & Guardrails
**Checkpoint vào:** `b1b2eec`
**Ngày:** 2026-08-22
**Nối tiếp:** `07A-A_linter-inventory.md`

---

## 1. VIỆC ĐÃ LÀM — BỐN PHÉP ĐO

| # | đo gì | kết quả |
|---|---|---|
| Đ1 | chạy `validate_shots.py` trên cả 6 video | **4/5 video có artefact đang FAIL, exit 1** |
| Đ2 | quét token luật-đã-chết trong 93 file consumer | **62 lượt trúng thô** |
| Đ3 | lọc trúng thô bằng cửa sổ "bia mộ" ±2 dòng | còn **22** — vẫn gần như toàn nhiễu |
| Đ4 | quét đường dẫn neo-gốc trong `rules/` + `skills/` | **0 chết thật**, 1 dương tính giả |

Hai lỗi thật lộ ra từ Đ2 — mục 5. Một phát hiện phương pháp lộ ra từ Đ3 — mục 4.
Phát hiện ở mục 4 **đổi thiết kế của `07B-A`**.

---

## 2. `G7-1` KHÔNG CÒN LÀ GIẢ THUYẾT — ĐO ĐƯỢC HÔM NAY

`07A-A` mới nói *"doctor không gọi `validate_shots.py`"*. Task này chạy thử trên toàn bộ video:

| video | có đủ 3 artefact? | exit | số ❌ |
|---|---|---|---|
| Video17_Death | ❌ thiếu cả ba | — | — |
| Video17_Rain | ✅ | **1** | **2** |
| Video18_Sleep | ✅ | **1** | **3** |
| Video19_Moon | ✅ | **1** | **4** |
| Video19_NightWalk | ✅ | **1** | **1** |
| Video20_Cold | ✅ | 0 | 0 |

**10 lỗi đang sống trên 4 video. Cả 10 đều exit mã 1. Không cổng nào trong dự án in ra chúng.**

Loại lỗi thật đang nằm đó:

```text
SCENE_N khai người trong subject      V18 khung 67 · V19_Moon khung 216, 224, 227
   → engine dán NO_PERSON, người trong subject BỊ XOÁ khỏi ảnh
chủ thể nói ngủ mà face != asleep     V17_Rain 4 khung · V18 9 khung · V19_NW 3 khung
   → prompt tự cãi nhau, model vẽ người nằm mở mắt
khối nhân vật NAM không lặp Y NGUYÊN  V19_Moon — 0 khung khớp mốc
   → đúng cái làm nhân vật trôi giữa các khung
```

Hai loại đầu chính là **hai ca `validate_shots.py` được vá ngày 15/08 sau khi bắt được ở V20** —
và chúng **vẫn sống nguyên ở bốn video khác**, vì không ai chạy lại tool trên các video ấy.

**Điểm cần nói rõ:** luật sống còn `GHÉP SHOT == NARRATION nguyên văn` **PASS ở cả 5 video**.
Trôi narration↔shot hiện **không** xảy ra. Nhưng nó chỉ là **1 trong 20 phép kiểm** của tool đó,
và 19 phép kia mới là chỗ đang đỏ. `G7-1` giữ **P1**, lý do mạnh hơn `07A-A` viết.

---

## 3. `G7-2` ĐÚNG NHƯNG HÔM NAY RỖNG — HẠ XUỐNG P2 CÓ ĐIỀU KIỆN

Đếm bằng máy: **không có một file `approved.yaml` hay `published.yaml` nào trong repo.**

```text
find videos -name 'approved.yaml' -o -name 'published.yaml'   →  0 kết quả
```

Nên check `set_by: owner` viết hôm nay sẽ **không bắt được gì** — nó là hàng rào cho Phase 8,
lúc V21 lần đầu được duyệt. Vẫn nên làm *(rẻ, đúng, và hook chỉ chặn lúc GHI — `git merge`,
`git restore`, sửa tay ngoài Claude đều đi vòng qua hook)*, nhưng phải khai thẳng trong report
rằng nó đang **vacuous**, không được đếm như một cổng đang bảo vệ cái gì.

⛔ **Không được để nó in `PASS` khi không có file nào để kiểm.** Đó là PASS giả —
đúng thứ bệnh mà cổng P4 của `preflight.py` mắc phải và mất tới 22/08 mới vá.

---

## 4. PHÁT HIỆN PHƯƠNG PHÁP — "STALE ACTIVE RULE SCAN" NHƯ ROADMAP GHI LÀ **KHÔNG DÙNG ĐƯỢC**

Đây là kết quả quan trọng nhất của `07A-B`.

Quét 17 token luật đã khai tử *(`I ≈ 0`, `you:we 1,5-2`, `chữ 13-19%`, `giác quan 7-9%`,
`mỏ neo 3,2-5,1`, `9-12 phút`, `nhịp hài 30-60 giây`, `sáng 80-110`, `cold-viewer`,
`TEMPLATE_Thumbnail_DoiThu`, …)* trên 93 file consumer:

| cách lọc | còn lại | lỗi thật | độ chính xác |
|---|---|---|---|
| quét thô | 62 | 2 | **3%** |
| lọc bia mộ ±2 dòng *(`⛔`, "đã gỡ", "khai tử", "bị bác", …)* | 22 | 2 | **9%** |

**Vì sao thấp đến thế.** Trong kho này, **tên một luật đã chết xuất hiện trong file sống là
trạng thái LÀNH MẠNH, không phải bệnh.** Kỷ luật nghĩa địa của dự án *bắt buộc* consumer phải
mang bia mộ:

```text
.claude/rules/script-files.md:27   ⛔ `I ≈ 0` đã gỡ 07/08/2026. Người dẫn được có ý kiến riêng.
CLAUDE.md:91                      ⛔ KHÔNG dùng `TEMPLATE_Thumbnail_DoiThu.md` — file đó đã chết
kho/1_luat/RUBRIC_KichBan.md:47   ### Sổ số đã chết  *giác quan 7-9% · mỏ neo 3,2-5,1/phút · …*
```

Cả ba dòng trên là **thứ ta MUỐN có**. Một check bắn vào chúng sẽ làm doctor đỏ vĩnh viễn, và
phản ứng của người kế tiếp sẽ là **gỡ bia mộ đi cho doctor xanh** — tức là check tự tay xoá
đúng lớp bảo vệ nó sinh ra để giữ.

> Đây **đúng khuôn** lỗi đã suýt xảy ra ở `05B-D`: bản đầu của `check_agent_paths` báo chết cho
> `references/prose-and-voice.md` — một đường dẫn có thật. Nếu commit, lần sau ai đó sẽ "sửa"
> agent cho doctor xanh. Lần đó bắt kịp nhờ chạy thử trước khi merge. Lần này cũng vậy.

### Thiết kế thay thế — quét **BỀ MẶT THI HÀNH**, không quét văn xuôi

Tín hiệu không nằm ở *token có mặt hay không*. Nó nằm ở *token nằm trên bề mặt nào*.

**Bề mặt thi hành** = chỗ mà con số/tên được dùng để **quyết một cái gì đó**:

```text
1. dòng checklist          | ☐ | …  hoặc  - [ ]
2. giá trị enum trong      schemas/*.json
3. hằng số so sánh trong   tools/*.py
4. ô ngưỡng trong bảng chấm có cột đạt/trượt
```

**Văn xuôi kể chuyện một luật đã chết → bỏ qua. Con số nằm trên bề mặt thi hành → báo.**

Kiểm chứng trên dữ liệu hôm nay: **cả 2 lỗi thật đều nằm trên bề mặt thi hành.
Cả ~60 dương tính giả đều nằm trong văn xuôi.** Không có ngoại lệ nào theo chiều nào.

---

## 5. HAI LỖI THẬT — `G7-8` và `G7-9`

### `G7-8` · `schemas/review-verdict.schema.json` gọi tên ba agent đã bị xoá

```json
"judge": { "enum": ["cold-viewer","retention-architect","promise-payoff-judge",
                    "evidence-prosecutor","anti-ai-narration-critic","machine","external-listener"] }
```

Agent thật đang có: `anti-ai-narration-critic` · `evidence-prosecutor` · `viewer-retention-judge`.

Ba tên đầu bị **gộp và xoá ngày 07/08/2026** *(`RETIRED_RULES.md` — "SUBAGENT LÀ NGƯỜI XEM LẠNH")*.
Hệ quả chính xác:

- verdict từ agent **có thật** `viewer-retention-judge` → **trượt schema**;
- verdict khai là của `cold-viewer` — agent mà tài liệu Claude Code chứng minh **không thể lạnh** —
  → **hợp lệ**.

Schema đang **đảo ngược** quyết định 07/08. Nó sống **15 ngày**. `check_json` cho nó **PASS** vì
`check_json` chỉ kiểm file có parse được hay không, không kiểm enum có gọi tên thứ tồn tại không.

⚠️ **Mức độ tác hại hôm nay: thấp.** Không tool nào validate theo schema này, và
`PRODUCTION_ARCHITECTURE_UPGRADE_v2_PROPOSAL.md` §10 đã đề xuất **hoãn/bỏ** nó. Nhưng nó là
**đúng hình dạng** thứ Phase 7 sinh ra để bắt: một contract máy-đọc-được gọi tên thực thể không
còn tồn tại, và đi qua doctor sạch sẽ.

### `G7-9` · `HE_THONG_KichBan_v2_14Video.md` — checklist thi hành 5 con số mà chính header của nó khai đã chết

Header file, dòng 8-16:

> *"Mỗi chỗ chết có dấu ⛔ **tại chỗ**."*

rồi liệt kê `you:we 1,5-2` · `I ≈ 0` · `giác quan 7-9%` · `≥3 mỏ neo/phút` · `câu hỏi mỗi 60-90 giây`
là đã chết.

Checklist cùng file, dòng 270-282 — **không một dấu ⛔ nào**:

```text
| ☐ | Mật độ mỏ neo        | ≥3/phút    |
| ☐ | Mật độ từ giác quan  | 7-9%       |
| ☐ | Câu hỏi              | một câu mỗi 60-90 giây |
| ☐ | "I"                  | ~0         |
```

**Lời hứa của file sai ngay trong chính file đó.** Và checklist là bề mặt hành-động nhất trong
cả tài liệu — người tick ô đang thi hành bốn con số đã bị bác.

Đây là ca thứ **ba** của `D-ARCH-02` *(sau `I ≈ 0` ở rubric và `F-5` ở `sketchapiens-bien-tap`)*.
Khác hai ca trước ở một điểm quyết định: **hai ca trước do người bắt. Ca này do máy bắt, trong
một phép đo 20 phút.** Đó là bằng chứng trực tiếp rằng check này đáng làm.

---

## 6. XẾP ƯU TIÊN LẠI — 9 FINDING

| id | finding | `07A-A` | **nay** | vì sao đổi |
|---|---|---|---|---|
| **G7-1** | `validate_shots.py` không ai bắt buộc chạy | P1 | **P1** | đo được: **10 lỗi sống / 4 video** |
| **G7-3** | không ai quét dead rule ở consumer | P2 | **P1 ↑** | 2 lỗi thật, 1 ca máy-bắt-được-mà-người-không |
| **G7-9** | checklist `HE_THONG` thi hành 5 số đã chết | — | **P1 mới** | thực thể của `G7-3` |
| **G7-8** | enum `review-verdict` gọi 3 agent đã xoá | — | **P2 mới** | thật, nhưng schema đang orphan |
| **G7-2** | doctor không kiểm `set_by: owner` | P2 | **P2** | đúng, nhưng **0 instance** hôm nay |
| G7-4 | `check_agent_paths` chưa phủ rule/skill | P3 | **P3** | đo: **0 chết thật**, 1 dương tính giả |
| G7-5 | chưa có check duplicate canonical mapping | P3 | **P3 — cần định nghĩa trước** | chưa ai định nghĩa "duplicate" là gì |
| G7-6 | chưa có check path casing / naming | P3 | **P3** | bug `*humb*` vs `THUMBNAIL` 22/08 là bằng chứng có ích |
| G7-7 | chưa có check generated-file integrity | P3 | **P3 — phần lớn đã đóng** | `G-01` `script_sha256` đóng ở 04B |

---

## 7. CONTRACT ĐỀ XUẤT — LỚP LINTER

Tám điều. `L-1` → `L-4` là luật cũ viết thành chữ. `L-5` → `L-8` **mới**, mỗi điều rút từ một
lỗi có thật đã xảy ra trong dự án này.

| # | điều | rút từ |
|---|---|---|
| **L-1** | **Read-only.** Không hàm nào ghi file. Máy **báo**, người **sửa**. | roadmap DO NOT |
| **L-2** | **Không chấm chất lượng sáng tạo** dưới bất kỳ tên nào — cấm đích danh: retention score, Causal Debt score, viral probability, tự sửa prose để đạt metric. | `A-07` |
| **L-3** | **Tất định.** Cùng input → cùng output. Không gọi model, không ra mạng. | — |
| **L-4** | **Mỗi check phải chứng minh bằng tiêm lỗi** trước khi merge: tiêm → thấy FAIL, gỡ → thấy PASS, **ghi cả hai vào report**. | `05B-D` |
| **L-5** | 🔴 **Check bắn vào file LÀNH là một defect, không phải "hơi ồn".** Độ chính xác đi trước độ phủ. Candidate nào không đạt độ chính xác cao trên kho hôm nay thì **không ship** — thiết kế lại hoặc bỏ, và **ghi lại việc bỏ**. | Đ2/Đ3 hôm nay *(3% và 9%)* + suýt-lỗi `05B-D` |
| **L-6** | **Thiếu input là `WARN`/không-áp-dụng, không phải `FAIL`.** `validate_shots.py` `sys.exit()` khi thiếu artefact; doctor phải coi đó là "chưa tới lượt", nếu không mọi video giai đoạn đầu sẽ đỏ. | Video17_Death thiếu cả ba artefact |
| **L-7** | **Doctor không nuôi bản sao thứ hai của một danh sách.** Nó **đọc** registry/schema. Danh sách token luật-đã-chết phải nằm trong **một file registry**, không hardcode trong doctor. | khuôn `load_video_contract()` đang dùng |
| **L-8** | **Uỷ nhiệm, không viết lại.** Có tool chuyên trách *(`validate_shots.py`)* thì doctor **gọi** và báo verdict của nó, không cài lại logic. | ba bản `validate_shots.py` từng trôi khỏi nhau trước 08/08 |

### Registry đề xuất cho `L-7`

`governance/RETIRED_RULES.registry.json` — nằm cạnh nghĩa địa văn xuôi, mỗi mục **bắt buộc** có
`nguon` trỏ về dòng trong `RETIRED_RULES.md`, đúng kỷ luật `schemas/shot_rules.json` đang dùng
*(không có nguồn thì không được làm cửa chặn)*:

```json
{ "token": "giac-quan-7-9",
  "pattern": "7\\s*[-–]\\s*9\\s*%",
  "chet_ngay": "2026-08-07",
  "thay_bang": "không có ngưỡng — đo cùng từ điển thì V17 ra 5,2%",
  "nguon": "governance/RETIRED_RULES.md §RUBRIC" }
```

---

## 8. PHẠM VI `07B` — CHỐT LẠI, ÁNH XẠ THẲNG VÀO ACCEPTANCE CRITERIA

Bốn dòng roadmap đòi, và task nào cấp dòng nào:

```text
architecture:         PASS/FAIL   ← đã có sẵn (control plane · frontmatter · agent paths · legacy · secrets)
governance refs:      PASS/FAIL   ← 07B-A
artifact schemas:     PASS/FAIL   ← 07B-B
production integrity: PASS/FAIL   ← 07B-C
```

| task | làm gì | không làm gì |
|---|---|---|
| **07B-A** | dead rule **trên bề mặt thi hành** *(`G7-3` `G7-9`)* + registry `L-7` | ⛔ không quét văn xuôi · ⛔ không đụng bia mộ |
| **07B-B** | `set_by: owner` *(`G7-2`)* + enum gọi tên thực thể có thật *(`G7-8`)* | ⛔ không PASS-giả khi 0 instance *(`L-6`)* |
| **07B-C** | uỷ nhiệm `validate_shots.py` *(`G7-1`)* theo `L-8` | ⛔ không cài lại logic · ⛔ không FAIL khi thiếu artefact |
| **07B-D** | bốn dòng PASS/FAIL + closeout | ⛔ không thêm check mới ở bước này |

### Hoãn sang sau Phase 7 — có lý do, không phải quên

| finding | vì sao hoãn |
|---|---|
| `G7-4` phủ rule/skill | đo ra **0 lỗi thật** hôm nay; làm thì phải kèm hàng rào chặn ký hiệu viết tắt *(`kho/1..4/`)*, không thì vi phạm `L-5` |
| `G7-5` duplicate canonical | **chưa ai định nghĩa "duplicate"**; viết check trước khi có định nghĩa là đoán |
| `G7-6` path casing | cần khai **quy ước đặt tên** trước; hiện chưa có file nào ghi quy ước đó |
| `G7-7` generated-file integrity | ca giá trị nhất *(`script_sha256`)* **đã đóng ở `G-01`, Phase 4B**; phần còn lại chưa rõ phạm vi |

Bốn cái này ghi vào roadmap dưới `PHASE 10 — CLEANUP`, **không** im lặng bỏ.

---

## 9. THỨ `07A-B` **CHƯA** LÀM

- **Chưa sửa một dòng mã nào.** Không file nào trong `tools/` bị động tới.
- **Chưa viết registry** — đó là việc của `07B-A`.
- **Chưa tiêm lỗi** cho bất kỳ check nào — `L-4` bắt buộc, làm ở từng task `07B`.
- **Chưa sửa `G7-8`/`G7-9`.** Chúng là *finding*, và doctor là máy **báo**, không phải máy **sửa**
  *(`L-1`)*. Sửa nội dung hai file đó là quyết định của chủ, không phải của Phase 7.

## 10. CỔNG MỞ `07B`

| điều kiện roadmap đòi | trạng thái |
|---|---|
| `07A-B` có checkpoint | ✅ file này + commit |
| gap analysis xong | ✅ 9 finding, xếp lại ưu tiên bằng số đo |
| contract đề xuất xong | ✅ `L-1` → `L-8` |
| phạm vi `07B` chốt | ✅ mục 8, ánh xạ thẳng vào 4 dòng acceptance |

→ **`07B` được phép bắt đầu.**

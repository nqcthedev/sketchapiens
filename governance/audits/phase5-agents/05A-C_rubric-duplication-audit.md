# 05A-C — RUBRIC DUPLICATION AUDIT

> **READ-ONLY AUDIT.** Không sửa agent, skill, rule hay tool nào trong task này.

**Phase:** 5 — Agent Architecture
**Checkpoint:** `0cd5e19`
**Ngày:** 2026-08-22

## 1. RUBRIC GIỮA BA AGENT — KHÔNG LẶP

Mỗi agent có taxonomy riêng, không chồng ô nào:

```text
viewer-retention-judge     điểm bỏ xem · câu phải nghe lại · ba lời hứa
                           một-hay-nhiều-câu-hỏi · bản đồ giữ chân · điểm thoát
evidence-prosecutor        claim verdict · bridge verdict · provenance
                           transfer · failure type · severity · lockability
anti-ai-narration-critic   mười câu nặng mùi · năm câu dễ bị chê AI
                           ẩn dụ chồng tầng · sẹo vá
```

`audit-script` còn có luật chống ép gộp:

> *"chỉ gộp khi thực sự cùng lỗi, không ép taxonomy khác role thành một lỗi"*

và với Evidence: *"giữ claim/bridge verdict + severity + debt; không nén về một score duy nhất"*.

**Kết luận:** không có rubric duplication ở tầng agent. Đây là điều acceptance criteria của Phase 5
đòi, và nó đang đạt sẵn.

## 2. `F-7` — BA RÀNG BUỘC CỨNG NHÂN BẢN Ở SÁU NƠI ACTIVE

Không phải rubric chấm điểm, nhưng là **ngưỡng cứng** — và nó xuất hiện ở sáu nơi:

```text
.claude/rules/script-files.md:25                       ← có frontmatter paths:, tự nạp theo file
.claude/skills/audit-script/SKILL.md:62
.claude/skills/apply-review/SKILL.md:46
.claude/skills/sketchapiens-viet-kich-ban/SKILL.md:52
.claude/skills/sketchapiens-viet-kich-ban/CONTRACT.md:169 + :240
.claude/skills/sketchapiens-bien-tap/qa_kichban.py:22 + :27   ← tool thực thi
```

**Cả sáu nói cùng một đáp án:** `! = 0` · không gạch ngang giữa câu · mỗi câu một dòng.

Theo `A-05`, architecture bug là khi *hai file active trả lời cùng câu hỏi bằng hai đáp án khác
nhau*. Ở đây chúng **đồng bộ**, nên chưa phải bug.

**Nhưng rủi ro là thật, và đã hiện thực hoá một lần.** `RUBRIC_KichBan.md:80-84` ghi lại:

> *"Đừng đếm bốn ô này thành 'bốn ràng buộc cứng'… lỗi đã lan ra ba file khác — `/apply-review`,
> `/audit-script`, `qa_kichban.py` đều từng ghi '4 ràng buộc cứng', và cái thứ tư chúng nghĩ tới là
> `I ≈ 0`, một luật đã chết."*

Ba consumer cùng drift một lúc vì mỗi consumer giữ bản sao riêng của cùng một ngưỡng.

**Và `SOURCE_OF_TRUTH.md` không chỉ định ai canonical cho ngưỡng này.** Dòng 27 giao Writer sở hữu
*"prose realization"*, nhưng không có dòng nào nói ba ràng buộc cứng thuộc file nào. De-facto
canonical là `.claude/rules/script-files.md` vì nó có `paths:` và tự nạp khi đụng file kịch bản —
nhưng đó là suy ra từ cơ chế, không phải từ khai báo.

Severity: `P2`. Sửa ở `05B-C` bằng cách khai canonical trong `SOURCE_OF_TRUTH.md` và để các
consumer trỏ về thay vì chép lại — **không** xoá bản sao ở tool, vì tool phải tự chứa để chạy được.

## 3. RANH GIỚI ĐÃ ĐÚNG — GHI ĐỂ `05B` KHÔNG PHÁ

`RUBRIC_KichBan.md` phân biệt hai thứ hay bị gộp nhầm:

```text
ba ràng buộc CÂU CHỮ        ! = 0 · không gạch ngang · mỗi câu một dòng
phép kiểm FILE DỰNG         ghép toàn bộ shot == narration nguyên văn
```

Và ghi rõ hậu quả của việc gộp: phép kiểm bản dựng **chưa bao giờ chạy** ở V17 và V19 vì tên file
mặc định sai — *"sai nó thì TTS đọc một kịch bản khác với kịch bản đã duyệt"*.

Đây là ranh giới đúng, không được gộp lại trong `05B`.

## 4. FINDINGS SAU 05A-C

| id | nội dung | mức | disposition |
|---|---|---|---|
| F-5 | ví dụ lỗi thời in `I` dưới nhãn CỨNG | P2 | sửa `05B-C` |
| F-6 | `knowledge/writing/**` không tồn tại | P3 | sửa `05B-A` |
| **F-7** | **ba ràng buộc cứng nhân bản 6 nơi, không khai canonical** | **P2** | **sửa `05B-C`** |

Rubric duplication ở tầng agent: **NONE**.

## 5. CHƯA LÀM TRONG 05A-C

- **Chưa đo context runtime thật** — `05A-D`.
- **Chưa kết luận `F-2`** — agent có Read/Grep/Glob không giới hạn.
- **Chưa rà rubric trong `kho/1_luat/**` ngoài `RUBRIC_KichBan.md`** — `CHECKLIST_KICHBAN.md`,
  `HE_THONG_KichBan_v2_14Video.md`, `BOCTACH_KICHBAN_DOITHU.md` đều nhắc ngưỡng. Chúng là tầng
  `kho/`, thấp hơn `.claude/` theo precedence, nên không phải authority — nhưng nếu có drift thì
  vẫn gây hiểu nhầm. Đưa vào `05A-D` như phần mở rộng.
- **Không sửa một file nào.**

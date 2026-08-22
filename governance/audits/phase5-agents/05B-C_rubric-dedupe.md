# 05B-C — RUBRIC DEDUPE

**Phase:** 5 · task ba của `05B`
**Checkpoint vào:** `35776a2`
**Ngày:** 2026-08-22

## 1. `F-5` — VÍ DỤ LỖI THỜI IN LUẬT ĐÃ CHẾT DƯỚI NHÃN `CỨNG`

`sketchapiens-bien-tap/SKILL.md` giữ một khối *"Ví dụ kết quả thật (V19, 06/08)"* in:

```text
CỨNG: '!' 0 (0) | '—' 0 (0) | 'I' 0 (≈0) | 3 câu dài liên tiếp: không
```

Ảnh chụp **06/08** — trước khi `I ≈ 0` bị gỡ ngày **07/08**. Nó mâu thuẫn với chính bảng ngưỡng
nằm **9 dòng bên dưới** trong cùng file.

### Vì sao đáng sửa, dù ba nguồn có thẩm quyền đều đã đúng

`qa_kichban.py`, bảng ngưỡng, và `audit-script` đều ghi `I ≈ 0` đã chết. Nên đây **không phải dead
rule đang sống**. Nhưng `qa_kichban.py:19-20` ghi lại hậu quả **đã xảy ra một lần**:

> *"Bản cũ in `'I'` dưới nhãn CỨNG, và `/apply-review` đọc dòng đó làm điều kiện chặn → editor sẽ
> **CẮT MỌI CÂU CÓ `I`**."*

Tool đã vá từ **09/08**. Ví dụ trong tài liệu tới **22/08** mới vá. Mười ba ngày một ảnh chụp lỗi
thời nằm ở chỗ dễ đọc lướt nhất.

### Đã sửa

Thay bằng **output thật của tool chạy hôm nay**, không phải ví dụ tự viết:

```text
1491 từ · 8.4 phút · 149 câu
CỨNG (3): '!' 0 (phải 0) | '—' 0 (phải 0) | mỗi câu một dòng: xem dưới
ĐO — KHÔNG PHẢI NGƯỠNG: 'I' 0 (người dẫn ĐƯỢC có ý kiến) | ...
CỨNG: mỗi câu một dòng → ❌ 22 dòng có >1 câu
you 50 : we 0 = 50.0:1  ← LUẬT 0, không phải hằng số
```

Kèm khối cảnh báo giải thích vì sao ví dụ cũ nguy hiểm, để không ai khôi phục nó.

### Phát hiện phụ từ chính output thật

**V19 đang trượt ràng buộc cứng thứ ba** — 22 dòng chứa hơn một câu. Đó là dữ kiện về **V19**,
không phải về tool. Ghi lại, không sửa ở đây.

## 2. `F-7` — BA RÀNG BUỘC CỨNG NHÂN BẢN Ở SÁU NƠI, KHÔNG AI KHAI CANONICAL

```text
.claude/rules/script-files.md:25                    ← có paths:, tự nạp theo file
.claude/skills/audit-script/SKILL.md:62
.claude/skills/apply-review/SKILL.md:46
.claude/skills/sketchapiens-viet-kich-ban/SKILL.md:52
.claude/skills/sketchapiens-viet-kich-ban/CONTRACT.md:169 + :240
.claude/skills/sketchapiens-bien-tap/qa_kichban.py:22 + :27   ← tool thực thi
```

Cả sáu **cùng đáp án**, nên chưa phải architecture bug theo `A-05`. Nhưng rủi ro đã hiện thực hoá:
`RUBRIC_KichBan.md` §80-84 ghi **ba consumer cùng drift một lúc**, đều từng ghi *"4 ràng buộc
cứng"* với cái thứ tư là `I ≈ 0` đã chết.

Mỗi consumer giữ bản sao riêng, nên sửa một chỗ không lan sang chỗ khác.

### Đã sửa — khai canonical, **không** xoá bản sao

Thêm dòng vào `SOURCE_OF_TRUTH.md`:

```text
Ba ràng buộc cứng của lời đọc  →  .claude/rules/script-files.md   [CANONICAL]
máy thực thi                   →  qa_kichban.py  (tool PHẢI giữ bản sao để chạy độc lập)
năm consumer khác              →  nhắc lại cho tiện đọc, KHÔNG phải nguồn chuẩn
                                  lệch thì script-files.md thắng
```

**Vì sao không xoá năm bản sao:** `qa_kichban.py` phải tự chứa để chạy được khi không có context;
bốn consumer còn lại nhắc lại ở đúng chỗ người đọc cần, xoá đi thì mỗi lần phải nhảy file. Vấn đề
chưa bao giờ là *có bản sao*, mà là *không ai biết bản nào thắng khi lệch*. Nay có.

## 3. CHECK

```text
ví dụ lỗi thời còn lại trong bien-tap    0
dòng canonical mới trong SoT             1
project_doctor.py                        PASS 43 · WARN 7 · FAIL 0
```

Không đụng agent nào, nên `F-9` không áp — hai file này là skill/governance, đọc theo file chứ
không cache như agent definition.

## 4. TRẠNG THÁI FINDING SAU `05B-C`

| id | mức | trạng thái |
|---|---|---|
| F-1 · F-2 · F-3 · F-4 | — | ĐÓNG ở `05A` |
| F-6 | P3 | **SỬA XONG** — chờ xác minh runtime *(`F-9`)* |
| F-8 | P2 | **GIẢM THIỂU** — không đóng được từ repo |
| F-5 | P2 | **ĐÓNG** |
| F-7 | P2 | **ĐÓNG** |
| F-9 | — | đặc tính runtime, ghi vào `RUNBOOK` ở `05B-D` |

## 5. CHƯA LÀM

- **Regression harness cho lớp agent** — `05B-D`, gồm phép kiểm deterministic cho đường dẫn trong
  `.claude/agents/**` *(nguyên tắc `N-3`)*.
- **Runtime smoke + closeout** — `05B-E`.
- **V19 trượt ràng buộc cứng thứ ba** — ghi nhận, thuộc video, không thuộc Phase 5.

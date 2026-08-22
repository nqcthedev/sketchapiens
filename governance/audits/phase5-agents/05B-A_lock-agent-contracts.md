# 05B-A — LOCK AGENT CONTRACTS

**Phase:** 5 — Agent Architecture · task đầu của `05B`
**Checkpoint vào:** `2d886d0`
**Ngày:** 2026-08-22

## 1. THAY ĐỔI

### `F-6` đóng — bỏ đường dẫn chết

`.claude/agents/anti-ai-narration-critic.md`

```diff
- ## Bạn ĐƯỢC đọc
- Lời đọc · `knowledge/writing/**` nếu có.
+ ## Bạn ĐƯỢC đọc
+ **Chỉ lời đọc.** Không cần file nào khác.
```

`knowledge/` **chưa từng được tạo** — khớp `D-ARCH-04`, migration `kho/**` → `knowledge/**` chưa
làm. Đường dẫn chết gây một Glob rỗng mỗi lượt chạy và làm agent mở đầu bản chấm bằng một câu xin
lỗi.

### Ghi lý do `F-3` vào chính agent

Thêm khối cảnh báo giải thích vì sao critic **không** được nối vào `prose-and-voice.md` — để lần
sau không ai "sửa" nó thành nối vào:

> *Writer viết bản nháp theo `prose-and-voice.md`. Nếu bạn đọc cùng file đó rồi chấm, bạn sẽ chấm
> theo đúng khuôn vừa sinh ra bản nháp — con mắt độc lập mất ngay tại đó.*

### Khai ownership lớp agent vào `SOURCE_OF_TRUTH.md`

Dòng "Review nội bộ" trước đây chỉ ghi `.claude/agents/*.md + /audit-script | mới, canonical`. Nay
ghi rõ ownership từng artefact và **`/apply-review` là editor duy nhất**.

## 2. CHECK — VÀ NÓ THẤT BẠI MỘT PHẦN

Chạy lại `anti-ai-narration-critic` trên V18 sau khi sửa. Kết quả `FILE ĐÃ MỞ`:

```text
Chủ động mở — Glob (cả hai trả về RỖNG)
  pattern `knowledge/writing/**`      → 0 kết quả
  pattern `**/knowledge/writing/**`   → 0 kết quả
```

**Agent vẫn glob đường dẫn đã bị xoá khỏi file.** File trên đĩa đã sửa đúng — xác minh bằng `sed`
và `git status`.

## 3. `F-9` MỚI — agent definition không reload trong session đang chạy

Sửa `.claude/agents/*.md` **không có hiệu lực với agent spawn trong cùng session**. Definition
được nạp lúc session khởi động.

**Hệ quả vận hành, áp cho toàn bộ `05B`:**

- mọi CHECK runtime cho thay đổi agent **không xác minh được trong session hiện tại**;
- CHECK phải là: **(a)** đọc file xác nhận nội dung đúng, cộng **(b)** một lượt runtime ở session
  sau;
- không được kết luận "đã đóng" chỉ vì file đã sửa — phải ghi rõ trạng thái `SỬA XONG, CHỜ XÁC
  MINH RUNTIME`.

Đây không phải lỗi của dự án. Là đặc tính runtime, và nó phải nằm trong `RUNBOOK` của `05B-D`.

**Trạng thái `F-6`:** `SỬA XONG — CHỜ XÁC MINH RUNTIME Ở SESSION SAU`.

## 4. `F-8` XÁC NHẬN LẦN 2 — 2/3 agent

Lượt CHECK này khai rõ hơn lần trước:

> **`nexlev`** — YouTube niche research *(`search_niche_finder_channels`,
> `search_shorts_niche_finder_channels`, `faceless_outliers_videos`…)*. Instruction block của
> server **được nạp sẵn vào ngữ cảnh của tôi**. Tôi không gọi bất kỳ tool nexlev nào — contract
> của tôi cấm research, và `CLAUDE.md` §2 cấm mở nexlev ngoài chế độ ①.

Nó liệt kê được **tên tool cụ thể**, tức instruction block vào context **đầy đủ**, không phải một
dòng tiêu đề.

`F-8` nâng từ 1/3 lên **2/3**. Hành vi vẫn sạch — không agent nào gọi nexlev. Nhưng đây là context
tax thật và là đường vào ngoài kiểm soát của `tools:`. `05B-B` xử lý.

## 5. GHI NHẬN — CHẤT LƯỢNG BẢN CHẤM KHÔNG ĐỔI

Lượt CHECK chạy trên V18 và vẫn ra bản chấm sắc: bắt được `S6` — cold open `L19-20` và cú trả bài
`L111` là **cùng một câu được viết lại nhẹ** *(`strapped activity trackers to` → `wired up`)*, nên
người nghe tới `L111` nhận ra đã nghe rồi và payoff mất lực.

Và nó tự ghi giới hạn của chính mình: *"vì `knowledge/writing/**` không tồn tại, tôi không có văn
bản chuẩn phong cách để đối chiếu"* — câu này sẽ biến mất sau khi `F-6` có hiệu lực runtime.

## 6. CHECK ĐÃ CHẠY

```text
project_doctor.py                 PASS 43 · WARN 7 · FAIL 0
grep knowledge/ trong .claude/agents/   0 kết quả
```

## 7. CHƯA LÀM

- **`F-6` chưa xác minh runtime** — cần một lượt ở session sau.
- **`F-8` chưa xử** — `05B-B`.
- **`F-5`, `F-7` chưa đụng** — `05B-C`.

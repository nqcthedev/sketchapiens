# 05B-D — REGRESSION HARNESS CHO LỚP AGENT

**Phase:** 5 · task bốn của `05B`
**Checkpoint vào:** `c0a475a`
**Ngày:** 2026-08-22

## 1. VÌ SAO CẦN

Nguyên tắc `N-3` rút từ `05A`: **mọi đường dẫn trong contract phải tồn tại.**

`F-6` cho thấy một đường dẫn chết **không gây lỗi ồn ào**. `anti-ai-narration-critic` trỏ
`knowledge/writing/**` suốt nhiều tuần — thư mục chưa từng được tạo. Hậu quả chỉ là một Glob rỗng
mỗi lượt chạy và một câu xin lỗi ở đầu mỗi bản chấm. Không ai để ý cho tới khi `05A-D` bắt agent
tự khai `FILE ĐÃ MỞ`.

Loại lỗi này cần **máy** bắt, không cần người.

## 2. THAY ĐỔI — `check_agent_paths()` trong `project_doctor.py`

Quét mọi đường dẫn trong backtick ở `.claude/agents/*.md`, kiểm tồn tại.

### Lần đầu viết sai — ghi lại vì nó là bài học

Bản đầu quét **mọi** đường dẫn có dấu `/`. Kết quả: **2 FAIL, cả hai là false positive**.

```text
❌ anti-ai-narration-critic   references/prose-and-voice.md
❌ viewer-retention-judge     references/candidate-lifecycle.md · mechanism-lab.md · evidence-in-story.md
```

Bốn đường dẫn đó **có thật** — chúng tương đối với **skill**, không tương đối với repo root.
`references/prose-and-voice.md` thực chất là
`.claude/skills/sketchapiens-viet-kich-ban/references/prose-and-voice.md`.

Nếu tôi commit bản đó, doctor sẽ báo FAIL vĩnh viễn cho hai agent hoàn toàn đúng — và lần sau ai
đó sẽ "sửa" agent để làm doctor xanh, tức phá thứ đang đúng.

### Bản đã sửa — whitelist prefix neo từ gốc repo

```python
_ROOT_PREFIX = (".claude/", "videos/", "kho/", "governance/", "tools/",
                "schemas/", "templates/", "identity/", "knowledge/", "2_KHO_BANGHI/")
```

Chỉ soi đường dẫn **neo từ gốc**. Đường dẫn tương đối bỏ qua — không kiểm được mà không đoán mò.

`knowledge/` nằm trong whitelist dù chưa tồn tại, chính vì thế mới bắt được ca `F-6`.

## 3. CHECK — CHỨNG MINH CỔNG BẮT ĐƯỢC THẬT

Cổng xanh **không** chứng minh cổng hoạt động. Kho đã hai lần bị xanh giả ở `P1`, và vừa phát hiện
đỏ giả ở `P4`. Nên chứng minh bằng tiêm lỗi:

```text
① tiêm `knowledge/writing/**` vào anti-ai-narration-critic
   ❌ agent paths anti-ai-narration-critic.md → đường dẫn không tồn tại: knowledge/writing/**
   PASS 45 · WARN 7 · FAIL 1

② khôi phục nguyên trạng
   ✅ agent paths anti-ai-narration-critic.md
   PASS 46 · WARN 7 · FAIL 0

git diff .claude/agents/anti-ai-narration-critic.md → rỗng
```

Cổng bắt đúng **ca `F-6` thật**, không phải một ca dựng riêng cho dễ.

## 4. `F-9` — GHI THÀNH LUẬT VẬN HÀNH

**Sửa `.claude/agents/*.md` không có hiệu lực với agent spawn trong cùng session.** Definition nạp
lúc session khởi động.

Phát hiện ở `05B-A`: sửa xong, chạy lại critic, nó **vẫn** glob `knowledge/writing/**` hai lần dù
file trên đĩa đã đúng.

**Luật cho mọi lần sửa agent về sau:**

```text
CHECK phải gồm HAI phần:
  (a) đọc file / chạy project_doctor  → xác nhận nội dung đúng      ✅ làm ngay được
  (b) một lượt agent thật              → xác nhận hành vi đổi        ⏳ session sau

KHÔNG được kết luận "đã đóng" chỉ vì (a) xanh.
Trạng thái đúng là: SỬA XONG — CHỜ XÁC MINH RUNTIME.
```

`check_agent_paths()` đóng được phần **(a)** bằng máy. Phần **(b)** vẫn cần một lượt chạy thật.

## 5. TRẠNG THÁI

```text
project_doctor.py    PASS 46 · WARN 7 · FAIL 0 · exit 0
                     (44 → 46: thêm 3 phép kiểm agent paths, bớt trùng)
tiêm lỗi             bắt đúng, khôi phục sạch
```

| id | mức | trạng thái |
|---|---|---|
| F-1 · F-2 · F-3 · F-4 | — | ĐÓNG ở `05A` |
| F-5 · F-7 | P2 | ĐÓNG ở `05B-C` |
| F-6 | P3 | SỬA XONG — chờ xác minh runtime, **nay có máy canh** |
| F-8 | P2 | GIẢM THIỂU — không đóng được từ repo |
| F-9 | — | **ghi thành luật vận hành ở mục 4** |

## 6. CHƯA LÀM

- **Runtime smoke + closeout** — `05B-E`.
- **Xác minh runtime `F-6` và `F-8`** — cần session sau, không làm được trong session này.

# 05A-D — BOUNDARY & AUTHORITY AUDIT

> **READ-ONLY AUDIT.** Không sửa agent, skill, rule hay tool nào trong task này.

**Phase:** 5 — Agent Architecture
**Checkpoint:** `a8e0ea5`
**Ngày:** 2026-08-22
**Phương pháp:** chạy **đúng ba agent thật của dự án** trên cùng một input
*(`videos/Video20_Cold/Script_V20_narration.txt`, 208 dòng)*, rồi đọc mục `FILE ĐÃ MỞ` mà mỗi
agent tự khai. Không suy từ frontmatter.

## 1. CONTEXT RUNTIME ĐO ĐƯỢC

| agent | tool calls | file chủ động mở | grep/glob |
|---|---:|---:|---|
| `viewer-retention-judge` | **1** | **1** — chỉ narration | không gọi Grep, Glob, Bash, MCP |
| `anti-ai-narration-critic` | **2** | 1 + một Glob trả rỗng | Glob `knowledge/writing/**` → 0 file |
| `evidence-prosecutor` | **22** | 9 | 4 Glob · 1 Grep toàn repo → 60 tên file · 3 WebFetch *(đều bị cookie wall)* |

Chênh lệch 1 ↔ 22 **không phải bất thường** — nó phản ánh đúng ownership. Retention judge chỉ được
nhận surface; prosecutor phải mở ledger, mỏ neo, metadata và thử nguồn gốc.

## 2. `F-1` ĐÓNG — `CONTEXT BUDGET` hoạt động thật, không phải chữ trong file

`05A-A` cảnh báo `viewer-retention-judge` có đường tới **67 KB** reference của Story Engine, gồm
`mechanism-lab.md` và `candidate-lifecycle.md`.

Runtime: nó nạp **`SKILL.md` 8 KB** và **không mở một reference nào**. Tự khai tường lửa, kèm lý do
từng file:

```text
CONTRACT.md                  không mở — không có ambiguity ownership nào cần phân xử
structural-mechanisms.md     không mở — không có mechanism canonical nào mơ hồ
evidence-in-story.md         không mở
workflows.md                 không mở
candidate-lifecycle.md       không mở  (candidate firewall)
mechanism-lab.md             không mở  (candidate firewall)
02-research/**               không mở, không liệt kê
claim ledger · 2_KHO_BANGHI  không mở, không liệt kê
```

Nó **không chỉ tuân thủ, mà giải thích được vì sao không cần mở**. Đó là progressive disclosure
đúng nghĩa, không phải kiêng khem mù.

`evidence-prosecutor` cho bằng chứng thứ hai cùng hướng: chủ ý **không** mở `causal-proof-fit.md`
với lý do *"E-OWN-05 trong CONTRACT đã đủ phán bốn cạnh; mở thêm là default-load không cần thiết"*.

**Disposition: F-1 ĐÓNG.** Không cần thêm guardrail cơ chế cho việc này.

## 3. `F-2` ĐÓNG — quyền rộng, nhưng cả ba tự giới hạn

`05A-A` lo cả ba agent có `Read · Grep · Glob` không giới hạn phạm vi. Runtime cho ba bằng chứng
độc lập rằng **chỉ dẫn là đủ**:

**`anti-ai-narration-critic`** — thử `knowledge/writing/**` *(đúng thứ contract cho phép)*, thấy
trống, và **dừng**. Không đi tìm chỗ khác, không mở `kho/`, không mở `2_KHO_BANGHI/`. Tổng 2 tool
call.

**`evidence-prosecutor`** — chạy một Grep toàn repo trả về **60 tên file**. Trong đó có hai đường
dẫn nằm ngoài biên context của persona:

```text
.claude/skills/sketchapiens-viet-kich-ban/tests/...
kho/1_luat/BOCTACH_KICHBAN_DOITHU.md
```

Nó **nhận ra và không mở cả hai**, rồi khai báo rõ trong `FILE ĐÃ MỞ`. Đây là ca mạnh nhất: agent
đã *nhìn thấy* đường vào và tự từ chối.

**`viewer-retention-judge`** — không gọi Grep, Glob, Bash hay MCP một lần nào.

**Disposition: F-2 ĐÓNG.** Không đề xuất siết `tools:` trong `05B` — siết sẽ làm
`evidence-prosecutor` mất khả năng mở nguồn, mà đó là ownership của nó.

## 4. `F-8` MỚI — hướng dẫn MCP server vào context không qua kiểm soát của frontmatter

`anti-ai-narration-critic` khai `tools: Read, Grep, Glob` — **không có nexlev**. Nhưng mục
`FILE ĐÃ MỞ` của nó ghi:

> *"Hướng dẫn MCP server `nexlev` — đưa vào ngữ cảnh tự động; **không gọi tool nào của nó**."*

`nexlev` là công cụ research đối thủ. `CLAUDE.md` §2 cấm mở nexlev trong chế độ VIẾT, và
`audit-script` cấm critic mở rộng role sang research.

Agent **không gọi được** tool đó — frontmatter chặn ở tầng thực thi. Nhưng **hướng dẫn vẫn chiếm
context**, và đó là đường vào không do agent frontmatter kiểm soát.

⚠️ **Mức chắc chỉ 1/3.** Hai agent kia không khai nexlev — nhưng *không khai* khác *không có*.
`viewer-retention-judge` ghi "không gọi MCP", tức nói về **gọi**, không nói về **nạp**.
`evidence-prosecutor` không nhắc tới.

Severity: `P2`. Không có leakage hành vi nào quan sát được — không agent nào gọi nexlev. Nhưng nó
là **context tax** và là lỗ hổng nguyên tắc. `05B-B` cần xác minh trên cả ba trước khi kết luận.

## 5. `F-6` XÁC NHẬN Ở RUNTIME

`anti-ai-narration-critic` phải mở đầu bản chấm bằng:

> *"Không có `knowledge/writing/` trong kho — chấm thuần trên lời đọc."*

Đường dẫn chết gây một lượt Glob vô ích **mỗi lần agent chạy**. Xác nhận `F-6` bằng runtime, không
chỉ bằng `ls`. Sửa ở `05B-A`.

## 6. AUTHORITY — KHÔNG AGENT NÀO VƯỢT QUYỀN

Kiểm chéo output với contract:

```text
viewer-retention-judge     không viết lại câu nào · không tự kết án fact ·
                           gắn cờ Narrative Overreach rồi ghi rõ "tôi không đọc research"
anti-ai-narration-critic   không đề xuất câu thay thế · có mục "đã cân nhắc và THA"
                           chứng minh còn phân biệt được, không gạch bừa
evidence-prosecutor        không chấm văn phong · không đề xuất title/thumbnail ·
                           không sửa kịch bản · trả NOT_LOCKABLE thay vì tự tha
```

`anti-ai-narration-critic` còn tự chống over-flagging đúng luật của nó: liệt kê những thứ **đã cân
nhắc và tha** — hedge bằng chứng, ngôi hai nhập vai, mảnh câu deadpan — và giải thích vì sao đoạn
kết được tha còn `L190-191` thì không.

Không có ca nào agent làm việc của agent khác.

## 7. GHI NHẬN NGOÀI PHẠM VI — BÀN GIAO CHO OWNER

Ba agent chạy trên V20 thật nên chúng tìm ra nợ thật của video. **Không thuộc Phase 5**, không sửa
ở đây, nhưng phải bàn giao:

**Evidence — `NOT_LOCKABLE`, 8 blocking debt.** Nặng nhất:

- `"Michael"` Rothschild — **không một bản ghi nào trong kho có first name**. Lời đọc tự thêm một
  chi tiết kiểm chứng được, cùng khuôn với lỗi `"William Haskell"` đã từng lọt qua mọi cổng máy.
- **Đảo mẫu số, hai lần.** `"The records do not say that"` — nhưng 25% cởi đồ nghĩa là 75% **không**
  cởi đồ, tức bản ghi *có* nói phần lớn nạn nhân không diễn ra kịch bản đào hang.
- `"almost every one of those"` khẳng định một **bảng chéo hai biến**, loại số gần như luôn nằm
  trong full text. Dự án đã xếp việc verify toàn văn vào hàng chờ và **chưa làm**.
- **Chuyển ngữ cảnh kép không hedge:** Rothschild là chết cóng **trong nhà** ở Berlin 1978–1994
  *(gầm giường, sau tủ, hốc kệ — đồ đạc gia dụng đô thị)*, được dùng để dựng chuyện ngủ **ngoài
  trời** thời băng hà.
- **Mâu thuẫn nội bộ:** `L172` tuyên bố *"that is all the evidence there is"* rồi `L173` liệt kê
  **ba** thứ — không có Rothschild. Bài mở bằng một nguồn thứ tư rồi về sau tự khai nguồn đó không
  tồn tại.
- `MONEO_V20_Cold.md` chỉ có `M1–M5`, **không có Rothschild ở bất kỳ dòng nào** — cả khối mở bài
  `L7–L21` là nguyên liệu thêm **sau** cổng mỏ neo, và luật dự án số 6 buộc chạy lại cổng đó.

**Retention — điểm thoát dự đoán ở `L115`** *(~7:26)*, chương sư tử hang: *"chương duy nhất không
trả tiền thuê"*, và người rời ở đó bỏ đi **đúng 50 giây trước** khoảnh khắc trên thumbnail.

**Thumbnail ↔ kết bài mâu thuẫn hai tầng** — lỗi nằm giữa bốn vật thể, không nằm trong câu nào:
thumbnail bán lửa làm vật cứu mạng, `L186-188` phủ định *"not the fire"*; và cảnh cuối `L205-206`
dựng lại **đúng tư thế** mà `L114` gọi là *"chỗ tệ nhất trong trại"*.

**Cả ba agent độc lập chạm `"nine separate things"`** — con số không có sở chỉ. Trùng đúng thứ owner
đã biết.

## 8. FINDINGS SAU 05A-D

| id | nội dung | mức | disposition |
|---|---|---|---|
| F-1 | context tĩnh là sàn không phải trần | — | **ĐÓNG** — CONTEXT BUDGET chạy thật |
| F-2 | agent có Read/Grep/Glob không giới hạn | — | **ĐÓNG** — 3/3 tự giới hạn, không siết `tools:` |
| F-3 | critic không nối public interface | — | **ĐÓNG** ở `05A-B` — có chủ đích |
| F-4 | `WebFetch` chỉ ở prosecutor | ĐANG ĐÚNG | giữ nguyên |
| F-5 | ví dụ lỗi thời in `I` dưới nhãn CỨNG | P2 | sửa `05B-C` |
| F-6 | `knowledge/writing/**` không tồn tại | P3 | **xác nhận runtime** — sửa `05B-A` |
| F-7 | ba ràng buộc cứng nhân bản 6 nơi | P2 | sửa `05B-C` |
| **F-8** | **hướng dẫn MCP vào context ngoài kiểm soát frontmatter** | **P2** | **xác minh cả 3 agent ở `05B-B`** |

## 9. CHƯA LÀM TRONG 05A-D

- **Chưa xác minh `F-8` trên cả ba agent** — mới có 1/3 khai trực tiếp.
- **Chưa viết contract proposal** — đó là `05A-E`.
- **Không sửa một file nào.**

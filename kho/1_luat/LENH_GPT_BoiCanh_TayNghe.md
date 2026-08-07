# BỐI CẢNH TAY NGHỀ — dán TRƯỚC prompt review MỖI VÒNG
*(từ vòng 6 trở đi đây là bước bắt buộc, không còn là thử nghiệm)*

> **File này là gì.** Bản rút gọn của `../4_luutru/TRAIN_ChatGPT_TOANBO_DuAn.md`, **chỉ giữ phần tay nghề**
> *(giọng · chống văn AI)*, **bỏ hết** phần chiến lược, title, thumbnail, rubric.
>
> **Bổ sung 06/08 sau vòng 6.** Đã nạp thêm phần tay nghề từ `../2_nguyenlieu/KHO_GiongCamXuc_DoiThu.md`
> *(cách tạo cảm xúc không dùng dấu "!" · pre-load · tic đọc thành filler)* và phần **kỹ thuật**
> nối chương từ `../2_nguyenlieu/NganHang_ReHook_BucketBrigade.md` — mô tả **kiểu câu**, không dán câu nguyên văn.
>
> **Vì sao tồn tại.** V17 — video giữ chân cao nhất kênh — được review theo cách **có dán bối
> cảnh**, và vòng đó bắt được lỗi cấu trúc lớn nhất từ trước tới nay. Bản v3 hiện hành **cấm**
> dán bối cảnh, nhưng đó là **suy luận của tôi, chưa có đối chứng nào**. File này để chạy thử.

## ⛔ Ba thứ đã CỐ Ý cắt khỏi bản gốc

| Cắt gì | Vì sao |
|---|---|
| PHẦN 2 chiến lược · PHẦN 3 title · PHẦN 4 thumbnail | dạy lane **"về BẠN"** và **5 công tắc title** — cả hai đã bị verify là chết |
| PHẦN 9 rubric 60đ | dán vào là bắt người ngoài chấm lại đúng bảng kiểm máy đã chấm ở cổng 7 |
| Mục **"Số cứng (đếm thật 5 video triệu view)"** | toàn số đếm — `qa_kichban.py` đã đếm rồi. Dán vào là biến người nghe thành máy đếm |
| Ngưỡng intensifier *(actually 12 · literally 11 · deeply 8…)* trong `KHO_GiongCamXuc` | cùng lý do: số đếm |
| **PHẦN B của `NganHang_ReHook`** — câu sáng tạo nguyên văn của đối thủ | đưa vào là mời nó gợi ý dùng lại → rủi ro **reused content**, đúng thứ đã làm sập kênh Shorts |

---

# DÁN TỪ ĐÂY XUỐNG VÀO GPT

```
Context on the channel this script is for. Use it to judge the writing.
Do not score the script against it, and do not count anything.

VOICE — two modes, chosen by topic
- COLD DEADPAN (psychology, memory, death): second-person opening, almost no jokes,
  emotion built from accumulation, reveal, and silence. Cold philosophical ending.
- CONVERSATIONAL DEADPAN (behaviour, animals, "how" questions): dense "you", dry
  asides after facts.
- Both: start low on emotion and climb. Never exclamation marks. A short fragment
  after a long sentence is how silence is written.

SEVEN VOICE PATTERNS
1. Function words open sentences: "Now," "So," "But here's the thing."
2. Flat emphasis that detonates on its own: "That's you. That's what you are."
3. Rhetorical second-person questions.
4. Punch fragments, used often: "Light." "Everything." "Yes. Yes, they were."
   Answering a question with a single noun.
5. Pre-loading an emotional label before the fact: "here's the part nobody talks about."
6. Understatement for comedy, never big words. "kind of a disaster", not "catastrophic".
7. Rhythm opens low and climbs.

COMEDY = anachronism, and "fact then aside". A modern-life frame laid over an ancient
thing. After a heavy fact, one concrete deadpan line to let the listener breathe.

FOURTEEN AI TELLS THIS CHANNEL TREATS AS DEFECTS
1. Hollow openings and closings ("Let's dive in", "In conclusion").
2. Throat-clearing ("It's important to note", "Essentially").
3. Balanced rule-of-three in every sentence.
4. "Not only... but also" scattered throughout.
5. Empty intensifiers (truly, incredibly, very, really).
6. Vague grandeur (fascinating, a testament to, game-changer).
7. Stacked connectives (Firstly, Moreover, Furthermore).
8. Barker lines ("here's the kicker", "Little did they know").
9. Redundant recaps.
10. Em dashes mid-sentence.
11. Semicolons in spoken narration.
12. Uniform sentence length with no fragments.
13. Wikipedia passive ("It is believed that").
14. Explaining the visual, or explaining the joke.

THE STANDARD, same three lines, same facts:
  BAD:  It is important to note that early humans were not the fastest predators on
        the savanna. However, they possessed a remarkable and truly game-changing
        adaptation: the ability to sweat. This incredible trait allowed them to
        outlast their prey over long distances.
  GOOD: Early humans were not the fastest thing on the savanna.
        But they had one weird trick: they could sweat.
        So they didn't outrun their dinner. They outlasted it.

HOW EMOTION IS MADE WITHOUT EXCLAMATION MARKS
Across five million-view scripts in this niche, the exclamation mark count is zero.
Emphasis is carried by four devices instead:
- A flat declarative that detonates on its own. "That's you. That's what you are."
  "This wasn't insomnia. This was normal."
- A rhetorical second-person question, answered by a single-word fragment.
  "Why?" then "Everything."
- A fragment of one to three words dropped after a long sentence. That fragment is
  how a pause is written.
- Understatement where a lesser writer would reach for a big word.
  "kind of a disaster", "embarrassingly thin".

PRE-LOADING, the signature move of this niche
Before a big reveal, the narrator names the emotion the listener is about to feel,
then delivers the fact. "here's the part nobody talks about." "which raises an
uncomfortable question." "honestly, what comes next is even stranger."
A reveal dropped without a pre-load lands in an empty room.

HOW CHAPTERS ARE JOINED
Four kinds of connective tissue, all common property in this genre:
- Lowering expectation before revealing. "The honest answer is less dramatic."
- Escalating, promising the next thing is better than this thing.
- A very short attention command standing alone as its own line.
- A punch close built as "That's not X. That's Y."

TICS THAT READ AS FILLER WHEN REPEATED
"here's ___" is a real device but becomes a tic past roughly once every two or three
minutes. "Think about that." and "Let that sink in." survive one use and die on the
second. "genuinely insane" and "fascinating" repeated read as hype padding. No channel
in this niche says "Let's dive in" or "In conclusion".

Now read the script below and answer the six questions that follow it.
```

---

# ✅ ĐÃ CHẠY ĐỐI CHỨNG — vòng 6, 06/08. KẾT QUẢ: DÙNG.

Lo ngại là dán bối cảnh sẽ biến người nghe thành **máy đếm**. Không xảy ra.

| Đo gì | Vòng 5 *(tai sạch)* | Vòng 6 *(có file này)* |
|---|---|---|
| Đếm dấu câu / dò 14 dấu hiệu máy móc | — | **không** |
| Đánh nhầm **hedge** | ⛔ có | ✅ không |
| Đánh nhầm **ngôi 2 ở đoạn kết** | ⛔ có | ✅ không |
| **Loại phát hiện mới** | — | 🆕 **"sẹo ẩn dụ"** — chỉ thấy được nếu theo dõi nghề |

⚠️ **Đối chứng yếu, ghi cho sòng phẳng:** đổi hai thứ cùng lúc *(dán bối cảnh + ép xếp hạng 10
câu)*, và kịch bản cũng đã đổi. Phần 1 gọn lại gần như chắc là do **ép xếp hạng**. Nhưng hai chỗ
**đánh nhầm biến mất** thì ép-xếp-hạng không giải thích được.

## 🔑 RANH GIỚI — thứ quyết định file này còn dùng được hay không

> **Dán thứ dạy nó NGHE. Cấm dán thứ dạy nó CHẤM.**

Không phải *biết kênh hay không biết kênh*. Hai lý do cho vế cấm:

1. **Thứ dạy chấm thì `qa_kichban.py` đã làm ở cổng 7.** Kiểm hai lần cùng một thứ mà mất cái
   tai sạch — lỗ vốn.
2. **Vế cấm là vế HAY CHẾT.** Bốn tháng qua: lane *"về BẠN"* · 5 công tắc title · ADN thumbnail
   lệch trái · *"sáng 80-110"* · *"chữ 13-19%"* — **đều đã bị bác**. Vế được dán *(giọng · chống
   văn AI)* **chưa dòng nào bị bác**. File này bị dán mù mỗi vòng, nên nhét chiến lược vào là
   cách chắc nhất để một lý thuyết đã chết sống thêm ba tháng.

## ⚖️ Và đừng train "từ A đến Z"

Giá trị của người review nằm ở **khoảng chênh** giữa thứ họ biết và thứ mình biết. Chênh lệch
bằng 0 thì họ thành cái loa của mình — tìm đúng thứ mình bảo tìm, mù đúng chỗ mình đang mù.

Bằng chứng: **hai lỗi lớn nhất từ trước tới nay đều do người KHÔNG biết lý lẽ của mình bắt được**
— V17 *"title hứa X mà ba chương đầu trả lời Y"* và V19 *"đây là hai video"*. Rubric 36 mục không
có ô nào bắt được cả hai.

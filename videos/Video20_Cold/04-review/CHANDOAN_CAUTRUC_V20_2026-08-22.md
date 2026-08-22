# CHẨN ĐOÁN CẤU TRÚC — V20 COLD

**Engine:** `sketchapiens-story-engine` · **Chế độ:** Review Mode · **Ngày:** 2026-08-22
**Input:** `Script_V20_narration.txt` — **208/208 dòng · 2.455 từ · sha `a3ae9ebc`**
*(cổng toàn vẹn đầu vào ĐẠT — nạp đủ, không chẩn đoán trên input thiếu)*

> **Ranh giới.** Story Engine **không** ra factual verdict, không sửa câu chữ, không quyết
> title/thumbnail. Mọi mục dưới đây là **cấu trúc**. Candidate firewall: **không** mở
> `candidate-lifecycle.md` / `mechanism-lab.md` — đây là review thường, không phải R&D.

---

## 0. XƯƠNG SỐNG ĐANG CÓ — đọc theo Macro Map

```text
EXPECT    L26 L61   lửa làm đêm ấm hơn
BREAK     L28-29    thứ giết bạn trước KHÔNG ở trong không khí — nó ngay dưới lưng
          L62       lửa KHÔNG thể làm ấm cả đêm
PROVE     L42-59    Ohalo II · L76-99 Kräuchi
COST      L103-107  khói, không tránh được · L128-135 lửa tàn
ESCALATE  L144-155  lửa tàn → phải có người dậy → ai?
REFRAME   L178-188  không phải xúm quanh lửa, mà là NẰM ĐÚNG CHỖ
RETURN    L192-208  bàn tay
```

**Xương này lành.** Bốn mục dưới đây không đề nghị đổi thứ tự nó.

---

## 1. STRONGEST EXIT RISK — `L115` *(~7:26)*, chương sư tử · **`R-1`**

**Chẩn đoán không phải "chương này thừa". Nó là: món nợ có tiền trả, mà không ai đi thu.**

Áp Causal Handoff cho `L114 → L115`:

| hỏi | trả lời |
|---|---|
| chương trước trả nợ nào? | `L108-112` — có nguồn nhiệt thứ hai, và **nó không bao giờ tắt** |
| để lại hậu quả gì? | `L113-114` *"chỗ tệ nhất trong trại… là ở một mình"* |
| chương sau có xử lý thứ đó không? | `L115` *"what else is out there in the dark?"* → **CÓ.** Cô độc → mối đe doạ |

→ **Mối nối VÀO chương sư tử là causal handoff hợp lệ.** Không phải nhảy topic.

**Hỏng nằm ở mối nối RA.** Chương tự thú hai lần không trả lời được *(`L122` `L124`)*, đáp xuống
`L126` *"a sleeping person does not know where it is"* — rồi sư tử **không bao giờ được nhắc lại**.
Kết luận ba chân `L182-184` **không có số hạng nào cho thú săn**.

### 🔴 Thứ chưa ai thấy: TIỀN TRẢ NỢ NẰM SẴN TRONG BÀI, cách đó 20 dòng

`L147-155` — Hadza, Samson 2017:

> `L153` *"a group can have someone awake or only lightly asleep almost all night, without anyone
> handing out shifts."*

Đó **chính xác** là lời đáp cho món nợ sư tử: *người đang ngủ không biết nó ở đâu — nhưng một
NHÓM thì không bao giờ ngủ hết.*

**Bài tiêu sự thật đó cho đúng MỘT món nợ** — ai dậy tiếp lửa *(`L154-155`)* — trong khi nó trả
được **HAI**.

**→ Khuyến nghị: KHÔNG cắt. Đi thu món nợ đã có tiền.** Một tới hai câu ở `L153-155`.

**Vì sao mạnh hơn cả hai phương án ban đầu:** chân thứ hai của kết luận — `L183` *"Another person
against the back"* — hiện chỉ chống bằng **hơi ấm**. Thu xong món nợ sư tử, chân đó gánh **hơi ấm
VÀ con mắt**. Không phải vá cho hết lỗi; là **làm kết luận chắc hơn**.

⚠️ Đắt vì thời điểm: chương ngay sau *(`C8`, ~8:17)* mới là **khoảnh khắc trên thumbnail**.
Người rời ở 7:26 bỏ đi **đúng ~50 giây trước** thứ họ đã bấm vào.

---

## 2. DEBT STATUS — món nợ thứ hai chưa thu, ở đầu bài

`L21` *"Something very old is still running inside us, and in the last minutes it takes over."*
— một cú gieo niềm tin mạnh, đóng khối Rothschild.

`L89-90` *"The cold hits the skin and it does **the oldest thing it knows how to do**. It clamps
down on the blood flow to your hands."*

**Hai câu này là CÙNG MỘT Ý** — cỗ máy cổ trong người tiếp quản. Một cái **giết** người đang chết
cóng *(chui hang)*, một cái **chặn giấc ngủ** *(bóp mạch)*. Bài viết cả hai mà **không bao giờ nối
chúng lại**.

Nối được thì khối mở bài thôi lơ lửng: Rothschild không còn là "nguồn thứ tư mồ côi", nó thành
**phần giới thiệu kẻ phản diện** — chính cỗ máy cổ ấy sẽ quay lại chặn giấc ngủ ở `L89`.

---

## 3. PROMISE–PAYOFF RISK — `R-2` **KHÔNG phải lỗi cấu trúc**

`L27` hứa lửa *(~1:35)*, chương lửa mở `L60` *(~4:03)*.

**Không đề nghị đảo thứ tự.** `BREAK` *(mặt đất, `L28-29`)* **bắt buộc đứng trước** lửa — bỏ nó thì
cú `REFRAME` ở `L178-188` mất sàn đứng, vì "nằm đúng chỗ" chỉ có nghĩa khi người xem đã tin **mặt
đất mới là thứ giết trước**. Đảo lên là gãy `BREAK → PROVE`.

**Rủi ro thật nằm ở PACKAGING, không ở kịch bản.** Thumbnail bán lửa; nước đi mạnh nhất của bài là
mặt đất. **Sửa lời hứa, đừng sửa trình tự.** Việc này thuộc packaging — Story Engine không sở hữu.

---

## 4. `R-3` — `"nine separate things"` phải BỎ

```text
L185  "The three support one another"          ← ba, chịu lực
L189  "three pieces of evidence"               ← ba, chịu lực
L200  "nine separate things"                   ← không có sở chỉ ở đâu trong bài
L202  liệt kê NĂM: wall · roof · mattress · blanket · box
L203  "a room that handles all nine"
```

Con số **chín không có sở chỉ** — không dòng nào trong 208 dòng đếm ra chín thứ. Và nó **đè lên
chính xương sống** đúng lúc `RETURN`, tức **30 giây cuối** — nơi người xem quyết định có bấm video
sau không.

**→ Bỏ "nine", trả về BA.** Sức nặng của đoạn kết đến từ *"the three support one another"*; thay ba
bằng chín ở phút chót là tự hoà tan cú `REFRAME` vừa dựng xong.

---

## 5. NARRATIVE OVERREACH FLAG — chuyển cho Evidence, không tự phán

| dòng | triệu chứng | đã có trong ledger |
|---|---|---|
| `L19` | *"The last thing **a freezing person** does"* — mệnh đề phổ quát | `C4` `BLOCKING` |
| `L17-18` | *"Nobody put them there. They crawled in."* — suy diễn kể như phép đo | `C5` `QUALIFY` |
| `L14-16` | gầm giường · tủ · kệ — bối cảnh trong nhà dùng cho ngoài trời | `B1` `BLOCKING` |

Story Engine **chỉ gắn cờ**. Verdict thuộc Evidence — cả ba đã nằm trong
`02-research/claim-ledger.json`.

---

## 6. KHÔNG PHẢI VẤN ĐỀ — nói rõ để đừng ai "sửa" nhầm

- **Lời hứa bàn tay** `L5-6` treo suốt 200 dòng rồi trả ở `L192-208`. Dài, nhưng đó là bookend cố
  ý và **nó trả đủ**. Đừng rút ngắn.
- **Khối thành thật** `L100-102` `L132` `L141-143` `L172-177` — bài tự khai giới hạn bốn lần.
  Đó là tài sản, không phải chỗ chảy máu.
- **Đổi miền** vật lý → sinh lý → khảo cổ → nhóm → phòng ngủ hiện đại: mỗi lần đổi đều do câu hỏi
  vừa sinh ra đòi. Không có trang trí cấu trúc.

---

## 7. STOP CONDITION

Dừng ở đây. Bốn mục trên là **lỗi cấu trúc thật**; chỉnh thêm chỉ làm framework đẹp hơn trên giấy.

**Chờ chủ duyệt `R-1`** trước khi sang chế độ ② VIẾT.

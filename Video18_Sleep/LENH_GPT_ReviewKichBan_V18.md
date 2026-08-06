# LỆNH GỬI GPT 5.6 — REVIEW KỊCH BẢN V18

## Làm theo thứ tự

1. Dán `TRAIN_ChatGPT_TOANBO_DuAn.md` vào trước *(cho GPT biết bối cảnh kênh)*
2. Dán toàn bộ `Script_Video18_narration.txt` *(đã thuần tiếng Anh, mỗi câu một dòng — dán y nguyên)*
3. Dán lệnh dưới đây
4. Gửi feedback về cho tôi — **đừng áp mù**

⚠️ **KHÔNG đưa NotebookLM.** Nó trộn kịch bản mình với 49 transcript đối thủ trong cùng notebook — đã bắt quả tang hai lần. Và nó không tra được fact.

---

```
This is a YouTube narration script for a stickman "ancient humans explained"
channel. The video is titled "How Did Ancient Humans Sleep in the Open?" and the
thumbnail shows three cavemen asleep around a fire with a leopard at the cave
mouth, captioned "EYES IN THE DARK?".

Do NOT rewrite it. Do not suggest replacement text. Quote verbatim, and do not
soften. Give me a critique in five parts:

1. READ-ALOUD TEST. Quote every sentence that no real narrator would say out
   loud. For each, say what is wrong with the mouth-feel.

2. AI SMELL. This niche's audience actively complains about "chatGPT writing" in
   the comments — one such comment has 4,400 likes on a competitor's video.
   Quote the five sentences most likely to trigger that reaction, and explain
   what gives them away.

3. PROMISE VS PAYOFF. The title asks how they slept in the open. The thumbnail
   promises a predator watching them. Does the script pay off both, and how
   early? Name the single point in the script where a viewer is most likely to
   leave, and say why.

4. THE MIDDLE CHAPTER. There is a chapter about "first sleep and second sleep"
   (Ekirch, and Wehr's 1992 darkness experiment) that sits between the chapter
   on sleep duration and the chapter on who kept watch. Be blunt: is that
   chapter earning its place, or is it a detour the script has talked itself
   into? If it is a detour, say exactly where the video loses its thread.

5. WEAKEST CHAPTER. Which of the four chapters is weakest and why. Pick one
   only. Do not be diplomatic.
```

---

## Vì sao cấm nó viết lại

Nếu GPT đưa câu thay thế, ta sẽ bị cám dỗ dán thẳng vào — và giọng kênh sẽ dần thành giọng GPT. Nó chỉ được **chỉ ra chỗ hỏng**, còn sửa thì mình sửa.

## Mục 4 là mục mới, và là chỗ tôi nghi nhất

Chương "hai giấc ngủ" là phần **mạnh nhất về mặt nội dung** *(kết luận có nguồn: giấc ngủ phân đoạn là hiện tượng phương Bắc, không phải của loài người)* nhưng cũng là phần **dễ lạc đề nhất** — nó không trả lời trực tiếp câu hỏi của title.

Tôi đã tự sửa một lần: bản trước chương đó kết bằng *"none of it answers the question this whole video is about"*, tức là tự khai lạc đề. Nay đã đổi thành dốc dẫn vào chương 4. **Nhưng chính tôi là người viết nên tôi mù với chỗ này** — cần mắt thứ hai.

## Mục đáng nghe thứ hai là mục 2

Bình luận *"The chatGPT writing is extremely noticeable here"* được **4.400 like**, đứng thứ tư trong 6.800 bình luận dưới video 2 triệu view của Mack. Khán giả ngách này soi rất kỹ.

## Khi có feedback

Gửi tôi. Tôi phân loại từng mục:

| | |
|---|---|
| **Áp ngay** | đúng, sửa luôn |
| **Áp có sửa** | đúng vấn đề, sai cách chữa |
| **Bỏ** | + lý do vì sao không áp |

Ví dụ một mục **Bỏ** ở V17: GPT chê *"Now, let's be honest about something"* là filler — trong khi đó là nguyên văn cấu trúc của Predators 2,05M. Người review không biết ngách.

---

## ĐÃ TỰ KIỂM RỒI — nói trước để GPT khỏi mất công lặp

| Đo | Kết quả |
|---|---|
| Dấu `!` · "I" · em-dash · `;` | **0 / 0 / 0 / 0** |
| Câu hỏi | 12 |
| Hedge *(probably/might/roughly)* | 2 |
| Ba câu dài liên tiếp | không có |
| Câu hỏi lõi | **giây 28** *(luật <31)* |
| Lời hứa thumbnail *(con báo)* | **giây 67** *(luật <180)* |
| Mỏ neo | 6, **đã tự tra web từng cái** — bảng ở `VERIFY_Anchors_V18.md` |
| Quét 7 nhóm dấu hiệu văn AI | sạch cả bảy |

Nếu GPT chỉ nhắc lại mấy thứ trên thì bỏ qua. Thứ cần ở nó là **mục 1, 3 và 4** — những chỗ máy không đo được.

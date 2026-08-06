# PROMPT PACK cho NotebookLM / Gemini
*Dán từng khối vào NotebookLM. Đã nhồi sẵn luật đo được từ 11 kịch bản (7,81M → 94K) và 29 thumbnail (≥50K).*

**Chuẩn bị:** NotebookLM → Add sources → *Website and YouTube URLs* → dán URL các kênh đối thủ:
```
https://www.youtube.com/@Zenn-Explains
https://www.youtube.com/@InkExplainer
https://www.youtube.com/@AxenExplains
```
*(Thay bằng URL đúng của kênh bạn muốn bóc. Nạp 3-5 kênh cùng lúc cho nó so được.)*

---

# PROMPT 1 — BÓC FORMAT

```
You are analyzing a YouTube niche called "Ancient Humans Explained" — faceless
stickman animation, English, 8-25 minutes per video.

Analyze every source I have given you and produce a structured breakdown:

1. TITLE PATTERNS
   - List every title verbatim, with its view count if visible.
   - Group them into title formulas (e.g. "What Did Ancient Humans Do When ___?").
   - For each formula, note how many videos use it and their average views.
   - Flag which formulas describe a MOMENT (a situation happening to someone)
     versus which describe a MECHANISM (how something works).

2. HOOK STRUCTURE (first 60 seconds)
   - Quote the first 3 sentences of each video verbatim.
   - Identify the opening move: second-person immersion / a specific person in
     distress / a shocking claim / a question.
   - At what second does the main question appear?
   - Quote the payoff promise verbatim.

3. FACT DENSITY
   - Count every proper noun, place name, date, number and named researcher.
   - Give me anchors-per-minute for each video.
   - How many studies are cited with RESEARCHER NAME + YEAR + JOURNAL?
   - At what second does the first hard anchor appear?

4. CHAPTER TRANSITIONS
   - Quote every transition sentence verbatim.
   - Classify each as a BLIND PROMISE ("there was something else happening") or a
     TABLE OF CONTENTS ("now let's talk about X").

5. STRUCTURE
   - Where does the biggest twist sit, as a percentage of runtime?
   - Where does the script turn from "them" to "you", as a percentage?
   - Does the final line call back to an image from the opening? Quote both.
   - Is there a call to action at the end? Yes/no.

6. VOICE
   - Count "you/your", "we/our/us", and "I/me/my" for each video.
   - Count exclamation marks.
   - Count how many times the narrator admits uncertainty ("we don't know",
     "it's complicated", "that answer is too simple").
   - Count the jokes.

Present everything as tables. Quote verbatim wherever possible. Do not summarise
or paraphrase — I need the exact wording.
```

---

# PROMPT 2 — SINH ĐỀ TÀI

```
Based on the format you just decoded, generate 15 new episode ideas for a channel
in the same niche.

HARD RULES, derived from measured performance across 159 videos in this niche:

- Title formula, ranked by measured average views:
    "When Did Ancient Humans First ___?"        8 videos   287,075 avg  ← STRONGEST
    "The [Extreme] Things Ancient Humans Did"   6 videos   182,183 avg
    "Why Did/Do Ancient Humans ___?"           41 videos   154,442 avg
    "What Did Ancient Humans Do When ___?"     13 videos   113,807 avg
    "How Did Ancient Humans [verb] ___?"       42 videos   101,957 avg
    "Did/Were/Could Ancient Humans ___?"       18 videos    33,672 avg  ← WEAKEST, avoid

  Default to "When Did Ancient Humans First ___?" It wins by nearly 2x and is the
  least used. Never use the yes/no form.

- What makes that formula win: it matches a habit the viewer performs TODAY to its
  origin point. Smoking, salt, alcohol, sugar. The viewer recognises themselves.
  So the test is not "is this a moment or a mechanism" — it is "does this connect
  to something the viewer did this week?"

- Third person only. No "you" or "your" in the title.

- The subject must be something universal and slightly taboo — something everyone
  experiences or fears. Measured winners: salt, sugar, winter, sex, sleep, smell,
  menstruation, drugs, race. Measured losers: narrow single body parts
  (eyes, teeth, feet, back pain, hiccups).

- Under 60 characters.

For each idea give me:
  - The title
  - The single strongest scientific anchor available (site, date, researcher,
    study — be specific, and say so if you are unsure the anchor is real)
  - The counterintuitive twist the episode would build toward
  - The closing "loss" line: what did modern humans trade away, and did they
    notice?

Rank all 15 by how strong the twist is. Do not pad the list with weak ideas.
```

---

# PROMPT 3 — VIẾT KỊCH BẢN

```
Write the full narration script for the title I choose. Voice-over only — no
visual directions, no scene headings, no speaker labels.

Target: 1,500 words (about 8-9 minutes at 185 words per minute).

OPENING (measured against the two videos in this niche that exceeded 3 million
views — both do all four of these):

1. First sentence: second person, a specific physical action, with a time marker.
   "Tonight, when the sun goes down, you're going to flip a switch."
   "You got in your car this morning."
   "You're 9-months pregnant."

2. Sentence 2-3: a negative list of three, building the world by naming what is
   absent. "No alarm, no schedule, no place you need to be."

3. Second 27-35: state the main question, immediately followed by an escalating
   promise. "The answer changes everything we think we know."

4. Before second 40: the first hard anchor — a named researcher, a year, or a
   named site. Never a chapter that says "before we get to that, we need to
   understand X." Two videos did that and both underperformed.

BODY:

- At least 3 anchors per minute. Measured across videos above 1 million views:
  3.2, 4.5, 5.1 per minute. Include at least ONE study cited fully — researcher
  name, institution, year. All three million-view videos cite exactly one.

- First hard anchor before second 90. A named site, a named researcher, or a
  specific date.

- Chapter transitions: roughly 70% BLIND PROMISE, 30% may name the next chapter.
  BLIND: "But what came later is worse than you can imagine." · "There's one last
  layer to this that I saved for the end." · "Here's something else that almost
  never comes up."
  NAMED (use sparingly, when opening a clearly bounded block): "Now, let's talk
  about your smell." · "Let's start with fire."

- Include one clear biggest twist. Its position is free — measured winners placed
  it at 60%, 76%, 82% and 88% of runtime. Do not force it to a fixed point.

- Turn from "them" to "you" very late, at 88-93% of runtime. This is the most
  consistent structural rule in the entire dataset:
  "That's you. That's what you are."
  "At 11:00 p.m., when you open the fridge even though you're not hungry, you're
  running a 3 million-year-old program."

- Pick one number and repeat it several times across the script, like a refrain.

HEDGING — read this carefully, it is the most misunderstood rule:

- You MAY admit uncertainty about a specific claim, and you should. All three
  million-view videos do it 3-6 times: "some researchers think", "whether this was
  for ritual is unclear", "this is a hypothesis, not a proven theory", "we don't
  know exactly, and probably never will".

- You may NEVER deny the video's own promise, especially in the first minute. The
  lowest-performing video in the set has the best research and dies because at
  second 38 it says: "A date, a place, a first bite. It doesn't." The viewer came
  for that answer and was told it does not exist.

- When you negate, negate to RAISE the stakes, not to lower expectations:
  "This wasn't insomnia. This was normal."

ABSOLUTE PROHIBITIONS (measured 14/14):

- NEVER write "I". No "I think", no "honestly", no "here's where I have to be
  honest". Million-view videos use it 0-6 times total across a full script; treat
  zero as the target.

- NEVER use an exclamation mark. All 14 videos measured: zero.

- Keep "you/your" at 1.5-2x the frequency of "we/our/us".

CLOSING:

- Call back to the exact physical image from the first sentence.
  Opening: "you're going to flip a switch" → Closing: "We traded all of that for
  a light switch."

- End on LOSS or on IDENTITY, not on a summary and not on praise.
  LOSS: "...and most of us never even knew it was gone." · "...and most of us have
  no idea what we gave up because we never knew it was there."
  IDENTITY: "The most dangerous animal on the planet is the one that figured out
  fire. That's you. That's what you are."

- A call to action is optional. Most winners have none. If you use one, put it at
  the very end and push to the next video rather than asking for likes.

FORMAT: one sentence per line, plain text, no markdown, no numbering. Each line
becomes one TTS clip and one image, so every line must stand alone.
```

---

# PROMPT 4 — CHIA SHOT + PROMPT ẢNH

```
Take the script and split it into shots. One line = one shot = one image.

Splitting rules:
- Split at punctuation. Each clause becomes its own shot.
- 8-10 words per shot. Never exceed 14.
- Do NOT change a single word of the narration. Joining all shot lines back
  together must reproduce the script exactly.
- Short punch sentences stay whole, on their own line.
- Target pace: 2.8-3.0 seconds per shot.

Then write one image prompt per shot. Every prompt must contain, verbatim and
identically every time:

STYLE: Clean flat 2D cartoon explainer with smooth, even, confident medium-bold
black outlines, a crisp minimalist educational look.

CHARACTERS: The people are clean STICK-FIGURE doodles: a LARGE round white-filled
head with a simple expressive face (two big round white eyes with small black
pupils, thin expressive eyebrows, a tiny mouth, no nose) on a THIN body of clean
black lines, with rounded mitten hands and small oval feet. The modern man has a
BALD round head with NO hair; only ancient characters have hair, plus a small
ragged brown hide loincloth, torso bare, no body fur.

BACKGROUND: one single perfectly flat colour, edge to edge. NO drawn landscape,
NO horizon line, NO texture, NO gradient. Roughly two thirds of the frame left
empty. On dark backgrounds (navy, charcoal, slate, dark brown) draw the character
with a white-filled head and clean WHITE body lines instead of black, and no
shadow.

BACKGROUND MIX across the whole video — measured from the 7.81M-view channel:
  40% white or ivory · 25% dark flat · 30% flat colour · 5% light grey

NEGATIVE: no gradients, no textures, no photorealism, no 3D, no glossy render,
no extra limbs, no watermark, no duplicate characters, no split frames, 16:9.

Output format — exactly this, nothing else:

001.
<full image prompt>

002.
<full image prompt>

Repeat the character block verbatim in every single prompt. Do not use tokens,
references, or "same as before" — identical wording is what keeps the character
consistent.
```

---

# PROMPT 5 — CONCEPT THUMBNAIL

```
Design the thumbnail. These rules come from measuring 29 thumbnails above 50,000
views against 4 that failed.

RULE 1 — The text must NOT repeat the title.
The 7.81M video is titled "What Did Ancient Humans Do at Night?" and its thumbnail
reads "2 SLEEPS?" — a fact from inside the video that the title never mentions.
The 3M video reads "FREE ALL DAY" — the conclusion, not the question.
The two videos whose thumbnails carried new information outperformed the rest of
the set by roughly 8x.
Give me text that reveals the single strangest fact inside the script.

RULE 2 — Word temperature.
WORKS: MONSTERS · INBRED · MENSTRUATION · 2 SLEEPS · -69°F · NO SOAP · CAVE LION
FAILS: A SOCK · TOOTHBRUSH · ALLERGIES · EVOLUTION · SURVIVAL
1-3 words, ALL CAPS, ending in "?". Yellow with a thick black outline, across the
top of the frame, about 15% of frame height and 70% of frame width. No
exclamation mark. No red lettering.

RULE 3 — The centre of the frame belongs to the STORY OBJECT, not the character.
All 7 of the largest videos put the object that poses or answers the question on
the vertical centre axis: a fire, a torch, a hide sled carrying red meat, a pool
of blood. The characters move freely around it. There is no fixed character
position — pick whichever composition serves this specific story.

RULE 4 — Pick ONE of these seven layouts, and tell me which of the last three
videos used it so we don't repeat:
  1. Solo lying or sitting, centre of frame left empty
  2. Group of 3-5 spread across the frame, each with a different emotion
  3. Crowd judging: 1-2 people centre, 4 people around them glaring
  4. Victim centre, 2 witnesses flanking
  5. Person versus threat, one on each side
  6. Giant face in the foreground over a small wide scene behind
  7. Cutaway — cut through into a body, a shelter, or the ground
NEVER default to modern-human-left versus ancient-human-right. Only 2 of 29
winners used any side-by-side comparison.

RULE 5 — Colour: muted dusty tan, warm brown, faded olive base, plus exactly ONE
saturated accent — a small orange fire at 2-7% of the frame, or a blue sky patch
at 22-30%. The accent must not share a tone with the subject or the text.

RULE 6 — Every gaze points at the centre object, at another character, or
straight at the camera. No character looks toward the edge of the frame.

RULE 7 — No two faces carry the same emotion. Even the cheerful 3M-view thumbnail
plants one bored character at the edge. Describe each face as a COMBINATION:
"pain + surprise + shame", "panic + exhaustion", "smug + bored".

RULE 8 — The background must prove something: temperature, time of day, distance,
or danger. Include exactly one period marker: a mammoth, a cave painting, a
crescent moon, snow peaks, a hide tent.

Deliver:
  - The thumbnail text
  - Which layout number, and why this story needs that one
  - A full image-generation prompt
  - A self-check: shrink it to 168x94 pixels — is the story object still legible?
```

---

# GHI CHÚ

**Prompt 1 và 2 dùng được ngay** — chúng chỉ đọc và phân tích.

**Prompt 3, 4, 5 đã chứa sẵn kết luận đo được của mình**, nên đừng để NotebookLM "tự do sáng tạo" ở mấy chỗ ghi NEVER/ALWAYS — đó là các tương quan có số liệu, không phải sở thích.

**Chỗ cần bạn tự kiểm:** khi NotebookLM đưa mỏ neo khoa học (tên nhà nghiên cứu, năm, tạp chí), nó **có thể bịa**. Luật "cấm nói không biết" làm tăng rủi ro này. Mọi tên riêng và con số phải verify lại trước khi lên sóng — không thì mất uy tín kênh, mà uy tín là thứ khó lấy lại nhất.

---

# SỔ THEO DÕI — 4 BÁO CÁO NOTEBOOKLM (tính đến 29/07/2026)

## Phân vai đã chốt

| | Việc | Vì sao |
|---|---|---|
| **NotebookLM** | **CÁCH VIẾT** — ẩn dụ, truyện chêm, kết bài, lách kiểm duyệt, đếm cứng trong transcript | nó đọc sâu 49 nguồn, trích nguyên văn rất chuẩn |
| **Claude** | **CHỌN ĐỀ TÀI** — tra live, đếm bầy clone, đo đỉnh bầy, verify mỏ neo | NotebookLM **chỉ đọc nguồn đã nạp, không thấy YouTube live** → nó mù hoàn toàn về nguồn cung |

**Bằng chứng cho việc phân vai này:** báo cáo 4 đề xuất hai đề tài — *"trầm cảm tiền sử"* (tra ra: 20 clone, đỉnh trong ngách **277 view**) và *"dã thú với người ngủ"* (chính là video Predators 2,05M của Stickly — tức là bảo mình clone đúng cái video đang dùng làm mẫu). Nghe rất hay, cung thì đã chết.

## Từng báo cáo đã đi đâu

| Báo cáo | Nội dung | Kết quả |
|---|---|---|
| **1** | 4 luật của `HE_THONG_KichBan_v1` bị bác | ✅ đã vào `HE_THONG_KichBan_v2` PHẦN A |
| **2** | đếm từ/dấu câu + 3 chỉ số kỹ thuật | ✅ vào v2 PHẦN B2 + checklist + rubric A7. ⚠️ mâu thuẫn báo cáo 1 về hedge và view → tự đếm lại, **báo cáo 2 sai view (ghi 7,8M, thật 2.051.994)** |
| **3** | 16 ẩn dụ · 8 truyện chêm · 4 luật lách kiểm duyệt | ✅ `KHO_AnDu_TruyenChem_LachLuat.md`. Tra 4 mỏ neo → **2 sai số** (Borneo 2023→2022 · Diocles 5 tỷ→15 tỷ), 1 chi tiết không có nguồn (xương hươu hang Gough) |
| **4a** | công thức kết bài triết học | ✅ vào v2 **PHẦN G** + rubric mục 36 |
| **4b** | "liên minh nội dung: X and 2 more" | ❌ **BÁC** — YouTube không có trường nhiều tác giả; ~100 bản ghi nexlev đều đúng 1 `channelTitle`. Đó là chip trích dẫn của chính NotebookLM |
| **4c** | đồng sáng tạo (khán giả viết title) | ✅ vào `NGHIENCUU_CloneSwarm` mục 7, sửa thành **đọc bình luận đối thủ** (kênh mới 6 sub không dùng bản gốc được) |

| **5** | format/hook/mật độ số liệu 3 video benchmark | ✅ vào v2 **PHẦN F** (câu hỏi trước giây 31 · kiểu mở "vật thể hiện tại" · kho payoff · kho câu chuyển). Đếm cứng **4/5 khớp tuyệt đối**; hedge sai vì **gán câu của video Smoking sang Predators** |

## 🔑 ĐÃ HIỂU RA CƠ CHẾ SAI CỦA NÓ

NotebookLM **đếm rất giỏi nhưng không giữ được ranh giới giữa các nguồn**. Nạp 49 transcript vào một notebook → nó trộn thành một khối.

Đối chiếu trên Predators (`XWQz7Fh2X58`, tách riêng, đếm bằng script):

| | Báo cáo 5 | Đếm thật |
|---|---|---|
| tổng từ | 3.166 | **3.166** ✓ |
| dấu "!" | 0 | **0** ✓ |
| we/our/us | 40 | **40** ✓ |
| I/me/my | 2 | **2** ✓ |
| you/your | 60 | **59** ✓ |
| hedge | 5 | **1** ❌ *(2 câu còn lại là của video Smoking)* |

**Cách ra lệnh đúng:**
- ✅ "Trong video X, đếm số từ / số dấu ! / số lần 'you'" → tin được
- ✅ "Trích nguyên văn câu mở đầu của video X kèm mốc giây" → tin được
- ❌ "Video X hedge mấy lần, trích ra" → nó gom cả câu video Y, Z
- ❌ "Video X bao nhiêu view, kênh nào" → sai thường xuyên
- **Mỗi lần chỉ hỏi về MỘT video. Đừng hỏi câu bắc cầu nhiều video.**

## Luật khi nhận báo cáo mới

1. **Trích nguyên văn + đếm cứng** → tin, dùng luôn.
2. **Con số kèm theo** (năm, view, quy đổi tiền, số lần) → **tra lại từng cái**. Tỉ lệ sai tính đến nay: **4/6**.
3. **Đề xuất đề tài** → luôn chạy qua cổng bầy clone trước. NotebookLM không có dữ liệu cung.
4. **Claim về cách đối thủ vận hành** (team, liên minh, quy trình) → coi là giả thuyết cho tới khi có bằng chứng ngoài notebook.

---

# ➡️ LỆNH CHƯA CHẠY — ĐÃ TÁCH SANG FILE RIÊNG

Ba lệnh cho vòng tiếp theo nay nằm ở **`LENH_NotebookLM_ChuaLam.md`** (kèm 5 URL dán thẳng).

File này chỉ giữ **phần đã chạy xong** — 5 prompt cũ + sổ theo dõi 5 báo cáo + cơ chế sai của NotebookLM.

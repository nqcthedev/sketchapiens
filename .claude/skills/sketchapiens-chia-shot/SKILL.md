---
name: sketchapiens-chia-shot
description: >-
  [DỰ ÁN SKETCHAPIENS — kênh người que cổ đại] Biến 1 kịch bản narration TIẾNG ANH đã hoàn chỉnh (ngách "Ancient Humans
  Explained", người que) thành 2 cột KHỚP DÒNG: (1) dòng-SHOT ngắn để nạp TTS +
  sync, (2) prompt tạo ảnh gen-ready cho ĐÚNG shot đó. Tách shot theo DẤU CÂU
  (~6-9 từ / 1 vế, ~25-30 shot/phút — sửa 30/07/2026 sau khi đo video 997K của Ink Explainer).
  Nhất quán nhân vật đến từ CÁCH VIẾT PROMPT (mô tả đầy đủ, lặp y chữ mỗi lần),
  TUYỆT ĐỐI KHÔNG dùng cast-token/@ref (chủ đã bỏ vì hay lỗi). NGỮ PHÁP HÌNH HAI CHẾ ĐỘ:
  khung CẢNH kể chuyện có môi trường thật, và khung ĐỒ HOẠ DẠY HỌC — thẻ tiêu đề
  chương đánh số, bản đồ có ghim, sơ đồ mặt cắt, bày bộ đồ nghề có nhãn, thẻ chữ hai
  độ đậm. ⛔ SỬA 07/08/2026: **KHÔNG có tỉ lệ chuẩn giữa hai chế độ** — đo 4-5 kênh
  thì nền trắng chạy từ 36% (Mack) tới 80% (Zenn) mà cả bốn đều thắng, không có quan
  hệ nào với view. Mọi ngưỡng cũ (50/50 · 40/60 · "dưới 35% là sách tranh") ĐÃ BỎ.
  Chọn nền theo NGỮ CẢNH từng shot: khái niệm → thẻ, khoảnh khắc → cảnh; tỉ lệ tự nổi ra.
  Chữ trên hình dùng nhiều nhưng cũng KHÔNG có chỉ tiêu (Mack và EIP không dùng chữ nào).
  Nhân vật chính là NGƯỜI CỔ ĐẠI; anh chàng hiện đại chỉ là khách mời ở hook và
  kết (lane "về BẠN" đã verify 0 cú nổ/4 tháng). Dùng khi user đưa một
  script đã viết xong và muốn "chia shot + viết prompt ảnh", "làm ảnh theo shot",
  "chuẩn bị prompt gen ảnh cho video này". KHÔNG tự sáng tác narration mới (đó là
  việc của skill sketchapiens-viet-kich-ban). Xuất ảnh đặt tên 001..N khớp
  số dòng-shot để nạp thẳng vào tool GhepVideo.
---


> **CHẾ ĐỘ ④ SẢN XUẤT** — sau khi kịch bản đã CHỐT
> Kịch bản chưa qua cổng 7–9 thì chưa được chia shot.
>
> Quy trình tổng + BẢN ĐỒ KHO 4 TẦNG + luật ưu tiên khi hai file mâu thuẫn:
> `/Users/admin/Claude/Projects/Build Channel Người Que Cổ Đại/00_LUAT_HIEN_HANH.md` → `kho/1_luat/FLOW_VietKichBan_11Cong.md`

# Chia shot + viết prompt ảnh — "Người Que Cổ Đại"

Skill này là **khâu giữa** của pipeline:
```
[viet-kich-ban] script  →  ⭐ THIS: chia shot + prompt ảnh/shot  →  gen ảnh (Flow/Nano Banana)  →  GhepVideo: TTS + ghép 100% sync
```
Input = 1 narration EN đã xong (thuần lời đọc). Output = bảng 2 cột khớp số dòng.

**Không** viết lại narration. **Không** cast-token. Nhất quán = **lặp y nguyên khối mô tả nhân vật** trong mọi prompt.

---

## PHẦN 0 — 3 NGUYÊN TẮC (đọc trước)

0. ⭐ **NHÂN VẬT CHÍNH LÀ NGƯỜI CỔ ĐẠI**, không phải anh chàng hiện đại đầu trọc — xem PHẦN 3. Skill cũ xây cho lane "về BẠN" đã chết (0 cú nổ/4 tháng).
1. **Mỗi ảnh vẽ ĐÚNG cái đang được đọc.** Đây là sức mạnh thật của đối thủ: ảnh 2.8s minh hoạ chính xác vế đang kể (leopard cắn sọ, eagle bổ nhào, crocodile rình mép nước). Prompt phải bám nghĩa của **shot đó**, không chung chung.
2. **NỀN THEO NGỮ CẢNH — KHÔNG theo tỉ lệ cố định.** Nền của MỖI ảnh quyết định theo **nội dung của chính shot đó**, không phải một con số mặc định.

   > ## ⛔ ĐO 4 KÊNH NGÀY 05/08/2026 — KHÔNG CÓ TỈ LỆ CHUẨN NÀO CẢ
   >
   > | Kênh | Trung vị | Độ dài | Giây/ảnh | **Nền trắng** | Chữ trên hình |
   > |---|---|---|---|---|---|
   > | Mack | **45.000** | 21,8' | 4,3 | **36%** | không, chỉ ký hiệu |
   > | Zenn | 29.000 | 8,5' | **2,7** | **80%** | **~50% khung có chữ** |
   > | Explain In Paint | 11.000 | 22,4' | **2,5** | 50% | không |
   > | Before Civilization | 10.000 | 26,6' | 4,6 | — | — |
   > | ~~Simply A Stickman~~ *(nguồn số cũ)* | **510** | 9,6' | 2,6–3,3 | ~60% | — |
   >
   > **Nền trắng chạy từ 36% tới 80% mà cả bốn đều thắng.** Chữ trên hình: Zenn dùng dày đặc, Mack và EIP không dùng chữ nào. **Nhịp ảnh cũng không dự báo gì** — nhóm 2,5 giây cho trung vị 11.000 và 29.000, nhóm 4,3–4,6 giây cho 45.000 và 10.000.
   >
   > → **Đừng nhắm một tỉ lệ nào cả.** Chọn nền theo NGỮ CẢNH của từng shot như quy tắc dưới. Tỉ lệ tự nổi ra.
   >
   > ⚠️ **Chuyện "ảnh có chuyển động":** cả 4 kênh đều KHÔNG tĩnh — nhưng đó là **animation bên trong hình** (nét viền rung, mắt đảo, tay khua, mưa rơi, đường vẽ chạy ra), **KHÔNG phải zoom/pan camera**. Đừng thêm `zoompan` vào bộ ghép để giả chuyển động — bắt chước nhầm thứ.
   >
   > **Bài học phương pháp:** bản sửa lúc 14h cùng ngày chốt "35% trắng / 4,5 giây" dựa trên **2 kênh**. Đo thêm 2 kênh nữa là bác sạch. Hai điểm không đủ để chốt gì.

   Quy tắc là:
   - **Shot khái niệm/diagram/so sánh ✓✗/thẻ chữ/bản đồ/sơ đồ/timeline/vật đơn lẻ → nền TRẮNG.**
   - **Shot kể chuyện / có môi trường thật (đi săn ngoài trời, hang, đêm-sao, lửa, mặt nước) → nền CẢNH flat-màu hợp cảnh** (savanna = đất tan/olive + trời xanh; nước = xanh dương; hang = nâu đậm; đêm = navy + nền đất đen; lửa = cam ấm).
   
   → Tỉ lệ trắng/cảnh của mỗi video **tự nổi ra theo nội dung** (video nhiều hoạt động ngoài trời sẽ nhiều cảnh hơn; video nhiều khái niệm sẽ nhiều trắng hơn). Nhân vật đầu tròn **tô TRẮNG ĐẶC** để nổi trên nền màu. Vẫn flat-màu, viền đen, KHÔNG gradient. Đọc-hiểu-trong-1-giây vẫn là vua.
3. **Nhất quán bằng CHỮ, không bằng ref.** Mỗi lần nhân vật xuất hiện → dán **y nguyên** khối mô tả của nhân vật đó (cùng chữ = AI vẽ cùng kiểu). Không @token, không "same as before".

---

## PHẦN 1 — CHIA SHOT (theo dấu câu)

**Mỗi shot ~6-9 từ.** Đó là con số duy nhất ở đây, và nó có lý do **sản xuất**: shot dài hơn thì một ảnh phải minh hoạ hai ý, đọc-hiểu-trong-1-giây hỏng.

> ### 🔴 NHỊP GIÂY/ẢNH KHÔNG PHẢI ĐÍCH
> Đo 4-5 kênh: `2,5s → 11.000` · `2,7s → 29.000` · `4,3s → 45.000` · `4,6s → 10.000`.
> **Nhịp nhanh nhất và nhịp chậm nhất cùng có kênh thắng và kênh thua.** Kênh trung vị cao nhất
> bảng *(Mack, 45.000)* chạy **4,3 giây/ảnh** — chậm gấp đôi mức skill này từng ép.
>
> Nhịp là **quyết định chi phí**, không phải quyết định chất lượng: 2 giây/ảnh cho bài 8 phút ra
> ~240 ảnh phải gen; 3 giây ra ~160. Chọn theo sức làm, đừng chọn theo niềm tin nó ăn view.

Luật tách:
- Tách ở **dấu câu**: chấm, phẩy, chấm phẩy, gạch ngang, dấu hai chấm. Mỗi vế/mệnh đề = 1 shot.
- Câu dài → bổ thành 2-3 shot ở dấu phẩy/mệnh đề. Câu ngắn punchy ("No fur." "You were the meal.") = **1 shot riêng** (giữ cú đấm).
- Mỗi shot **~6-9 từ**; đừng để shot >12 từ (nếu lỡ, tách tiếp). Đừng để shot 1-2 từ trừ khi cố ý nhấn.
- **KHÔNG đổi chữ narration** khi tách — chỉ chèn ranh giới dòng. Ghép các dòng-shot lại phải ra đúng câu gốc (để TTS đọc liền mạch tự nhiên; TTS ngắt theo dấu câu vốn có).
- Đánh số **001, 002, …** (3 chữ số) — số này = số ảnh = số dòng nạp TTS.

Ví dụ:
```
Gốc: You walk into a forest like you own it, eating a granola bar, completely relaxed.
→ 012  You walk into a forest like you own it,
  013  eating a granola bar,
  014  completely relaxed.
```

---

> # 🔴🔴 PHẦN 2 KHÔNG CÒN LÀ NGUỒN CHUẨN — soát 09/08/2026
>
> Bốn khối `STYLE · CONSIST · SCENE · NEG` chép ở dưới **KHÔNG phải thứ chạy**.
> Thứ chạy là **`identity/style.py`** *(`tools/build_prompts.py` nạp `from style import *`)*,
> và hai bản **đã lệch nhau một thế hệ**:
>
> | | PHẦN 2 dưới đây | `identity/style.py` *(chạy thật)* |
> |---|---|---|
> | chữ `clean` | có trong CONSIST **và** NEG | **0 lần** |
> | chữ `cartoon` | có trong NEG | **0 lần** |
> | `wobbly` | CONSIST ghi **`not wobbly`** | **7 lần, khẳng định** |
> | mắt | ✅ khớp | `LARGE ROUND WHITE… Never tiny dots` |
>
> **Tự mâu thuẫn ngay trong một prompt:** khối `STYLE` ở dưới ghi *"outlines are **WOBBLY**…
> NOT smooth **clean** digital lines"* và liệt kê ba chữ cấm `cartoon · clean · smooth` — rồi
> khối `CONSIST` ba dòng sau ghi *"**Clean smooth** evenly-weighted outlines… **not wobbly**…
> a **clean** flat digital-explainer look"*. Hai lệnh ngược nhau dán chung vào **cả 191 prompt**.
>
> ## ✅ CÁCH DÙNG ĐÚNG: đừng chép bốn khối này. Gọi thẳng `identity/style.py`.
> ```python
> from style import STYLE_SCENE, STYLE_CARD, ANCIENT, MODERN, WOMAN, GROUP, NEG_SCENE, NEG_CARD, BG, FACE, ANIMAL
> ```
> Bốn khối dưới đây **giữ làm hiện vật** — để biết prompt V17/V18 đã dùng gì. ⛔ Đừng chép sang video mới.
> *(Đây là gốc của `D-03`, nay đã khép.)*

## PHẦN 2 — ~~TEMPLATE CHUẨN v2~~ ⛔ HIỆN VẬT (bám prompt đã kiểm chứng của chủ — bản NÂNG CẤP đối thủ) ⭐

Mỗi prompt = **6 khối theo thứ tự**. 4 khối CỐ ĐỊNH (STYLE·CONSIST·SCENE·NEG) dán **y nguyên**; đổi theo shot: SUBJECT + FRAMING + TEXT.

`[STYLE] [SUBJECT: nhân vật + hành động + biểu cảm]. Framing: [FRAMING]. [CONSIST] [SCENE] [TEXT]. [NEG]`

- **STYLE ⚠️ SỬA 30/07/2026 — NÉT RUN TAY, KHÔNG PHẢI VECTOR SẠCH:** `A HAND-DRAWN DOODLE illustration, drawn by hand with a thick black marker pen on paper: the outlines are WOBBLY and slightly uneven, the line thickness varies along each stroke, the ends of the strokes are soft and rounded, lines are not perfectly straight and not perfectly circular. Simple sketchbook doodle look. Colours are MUTED and desaturated, filled in loosely by hand inside the lines, with only a faint soft shading. NOT vector art, NOT smooth clean digital lines, NOT cartoon animation, NOT anime.`
  > **Ghi chú sai lầm.** Bản 07/2026 ghi *"đối thủ vẽ SẠCH DIGITAL, bỏ hẳn từ hand-drawn"* — **SAI**. Xem lại khung gốc 4K của Ink Explainer (`kho/2_nguyenlieu/REF_Style/` trong project): cây, mặt đất, vũng nước, người — **tất cả đều run tay, nét dày mỏng không đều**. Câu "not scratchy, not wobbly" chính là thứ đẩy model ra ảnh **hoạt hình vector**, không ra doodle.
  > Ba chữ nguy hiểm phải tránh trong STYLE: **`cartoon` · `clean` · `smooth`**. Cả ba đều kéo về Disney/Pixar/vector.
  > NEG phải chặn thẳng: `no anime, no Disney or Pixar style, no vector art, no smooth clean digital outlines, no cel shading, no bright saturated candy colours.`
- **CONSIST** *(vũ khí đè điểm yếu "drift" của đối thủ — lặp Y NGUYÊN mọi prompt; cập nhật 07/2026: mắt to có con ngươi, thân nét MẢNH-vừa (không quá bold), con vật chi tiết hơn người que, NÉT SẠCH DIGITAL không run tay):* `The people are clean STICK-FIGURE doodles: a LARGE round white-filled head with a simple expressive face (two big round white eyes with small black pupils, thin expressive eyebrows, a tiny mouth, no nose) sitting on a THIN body made of clean black lines (a single medium-weight line for the torso plus thin noodle arms and legs) — NOT a filled or solid body shape, just clean stick lines, with simple rounded mitten hands and small oval feet, ALWAYS drawn as the SAME stickman, kept identical in every image. The modern man has a BALD round head with NO hair; ONLY ancient/caveman characters have hair. The body is bare line-art with no colour fill; a character only wears a garment if their own description names it. Any animals and props are simple and cute in flat SOLID COLOUR (never black-and-white), each animal a simple cute character with a little face, drawn with more detail and body volume than the simple stick people. Clean smooth evenly-weighted medium-bold black outlines (confident single strokes, not sketchy, not wobbly); flat colours, NO gradient shading, a clean flat digital-explainer look, evenly drawn (not 3D, not glossy).`
- **SCENE (v3 — flat-scene, cập nhật 07/2026: thêm nhấn xanh-lá + vàng):** `ONE single scene showing ONLY ONE instance of the character; no model sheet, no multiple poses, no grid, no panels, no split frames; the background is ONE simple FLAT colour that fits the shot (a flat blue sky over a flat green or brown ground line for outdoor scenes, a flat tan or beige for dirt and ground close-ups, a flat dark-brown cave interior, a flat dark-navy night sky with tiny dots for stars over a flat black ground, a warm orange glow for firelight), OR a plain WHITE background for concept shots, big-text cards, comparisons, timelines and single isolated objects; keep it a single flat colour with NO gradient and lots of clean empty space, plus a soft light-grey shadow under the character; RED is the accent colour for danger, warnings and a big red X to negate an idea, GREEN for a check mark or safe/yes, a small YELLOW lightbulb for an idea; draw the people as WHITE-filled black-outline doodles that read clearly on top of the coloured background,`
  → **Chọn nền theo shot:** cảnh ngoài trời/săn/hái = sky · đất/dấu vết/đẽo đá = dirt-tan · hang/tranh hang = cave-brown · đêm/sao/songlines = night-navy · lửa/nấu = fire-orange · khái niệm / thẻ chữ / bản đồ / sơ đồ / bày bộ đồ nghề / so sánh = white.
- **TEXT** — dùng chữ khi shot đó có **một con số đắt, một tên vật, hoặc một cú chốt**. Không có chỉ tiêu tỉ lệ *(PHẦN 5)*.
  · nhãn vật → `a bold hand-drawn ALL-CAPS label "TINDER FUNGUS." under the object, black marker lettering`
  · nhãn sơ đồ → `a thin black arrow pointing at it with the ALL-CAPS label "DRY INSIDE"`
  · con số → `large bold ALL-CAPS text "52,000 YEARS AGO." across the upper third`
  · câu chốt → `large bold black ALL-CAPS hand-drawn text filling the frame on plain white`
  · không cần chữ → `no text or letters.`
- **NEG:** `Family-friendly, wholesome, cute, gentle, non-violent, no blood, no gore, no injury. no gradients, no textures, no photorealism, no 3D, no glossy render, no sketchy scratchy lines, no extra limbs or fingers, no watermark, no logo, no frame borders, no duplicate characters, no collage, no picture-in-picture, 16:9, clean educational YouTube explainer doodle style.`

**FRAMING (đổi liên tục → đè nhịp đơn điệu của đối thủ):** `a medium shot, the subject drawn big and centered with clean breathing space around it.` · `a WIDE establishing shot, the subject fairly small inside a large scene.` · `a tight CLOSE-UP on the character's face and shoulders, the expressive face filling most of the frame.` · `a HIGH-ANGLE shot looking DOWN, making the subject look small and vulnerable.` · `a LOW-ANGLE shot looking UP, making the subject look powerful.`

---

## PHẦN 3 — CASTING & KHỐI NHÂN VẬT ⭐ *(viết lại 30/07/2026)*

> ## 🔴 ĐỔI CASTING — SKILL CŨ XÂY CHO LANE ĐÃ CHẾT
>
> Bản cũ coi **anh chàng hiện đại đầu trọc là đồng chủ diễn**, vì skill được xây cho sub-ngách **"về BẠN"** (mismatch cơ thể: một thứ hỏng trên cơ thể BẠN hôm nay ↔ tổ tiên).
>
> Lane đó **verify 27/07: 0 cú nổ / 4 tháng.** 11/15 video của kênh xây trên nó và flop hết. Thumbnail cũng vậy — khuôn "hiện đại TRÁI ↔ cổ đại PHẢI" dùng 11/11 lần, chỉ 2/29 quả thắng dùng.
>
> **Nay kênh làm ngôi 3.** Và trong kịch bản mới, chữ "you" trong lời đọc **CHÍNH LÀ NGƯỜI CỔ ĐẠI**, không phải người hiện đại:
> > *"You are a soft, mostly hairless ape sitting in a puddle that used to be where you slept."*

### LUẬT CASTING MỚI

| | Ai | Xuất hiện ở đâu |
|---|---|---|
| **Nhân vật chính, ~85-90% khung** | **NGƯỜI CỔ ĐẠI** — người mà khán giả đang nhập vai | toàn bộ thân bài |
| **Người hiện đại đầu trọc** | chỉ là **khách mời** | **CHỈ** ở hook, ở thẻ so sánh `YOU ‖ THEM`, và ở bookend cuối bài |

⚠️ **Cấm dựng cả video quanh cặp đối chiếu hiện đại ↔ cổ đại.** Đó là ngữ pháp của lane đã chết.

**Cách kiểm nhanh:** đếm số khung có người hiện đại. **Quá 15% là đang trượt về lane cũ.**

*(Đối chiếu: Ink Explainer 997K dùng cảnh đời hiện đại — nhân vật nằm sofa xem TV — nhưng chỉ vài khung trên tổng số ~350. Nó là gia vị, không phải khung xương.)*

---

### Khối mô tả — lặp Y NGUYÊN mỗi lần

- **Người hiện đại — KHÁCH MỜI, dùng dè:**  `the recurring modern guy, the same plain black-outline STICK FIGURE with a plain round BALD white head and NO hair (just a simple face), a bare thin bold black stick-line body (NO clothing, NO filled body shape), thin bold noodle arms and legs, simple rounded mitten hands and small oval feet,`
- **Tổ tiên/caveman:** `the recurring caveman, the same plain black-outline stickman with a messy scribbly tuft of short spiky dark doodle hair on top of the head, wearing a simple ragged brown animal-hide smock as a flat brown shape covering the torso, barefoot with small white oval feet,`
- **Tổ tiên nữ:** như caveman nhưng `long dark hair tied back, wearing a simple brown fibre wrap,`
- **Trẻ cổ đại:** `a small caveman child with a tiny tuft of dark hair and a small fur wrap,`
- **Già làng:** `an old stickman with grey hair and grey beard, slightly hunched, holding a wooden stick, wearing a fur wrap,`
- **"Con người chung" / cảnh khái niệm:** không dùng khối nhân vật — mô tả thẳng cảnh (vd `a long horizontal timeline line with tiny plain white stickmen`).

**Biểu cảm** (gắn cuối hành động): `smug half-lidded eyes` · `surprised wide round eyes and open O mouth` · `nervous wavy mouth, inner eyebrows raised, a sweat drop` · `curious tilted head` · `deadpan flat straight mouth` · `dumb clueless expression`.

**CON VẬT = cute + tô màu ĐẶC + có mặt nhỏ:** `a cute flat brown leopard with black rosettes and a little face` · `a cute green crocodile` · `a cute flat golden-yellow lion with a mane` · `a cute flat brown bear` · `a brown eagle with a little face`. Con vật là điểm nhấn màu (đè kiểu người-trắng đơn điệu).

---

## PHẦN 4 — THƯ VIỆN FRAME-TYPE

Đối thủ **không minh hoạ câu chữ — họ giảng bài bằng bảng**, xen giữa cảnh kể chuyện. Đó là ngữ pháp
hình khác hẳn, không phải khác về tay nghề. Hai nhóm dưới đây là hai chế độ đó.

⚠️ **Không có tỉ lệ chuẩn giữa hai nhóm** — xem `PHẦN 0` nguyên tắc 2. Chọn theo từng shot:
**khái niệm → thẻ · khoảnh khắc → cảnh.** Tỉ lệ tự nổi ra.

### A. NHÓM KỂ CHUYỆN

| # | Kiểu | Dùng khi |
|---|---|---|
| 1 | **Cảnh kể chuyện** — nhân vật + môi trường flat-màu | đang kể một khoảnh khắc có thật |
| 2 | **Nền trắng, một nhân vật** — không môi trường | khái niệm, phản ứng, câu nối |
| 3 | **Mặt cận biểu cảm** | khoảnh khắc cảm xúc / cú lật |
| 4 | 🆕 **Cảnh ĐỜI HIỆN ĐẠI** — nhân vật nằm sofa, có TV, cốc, điện thoại | mọi câu bắt đầu bằng "you" ở thì hiện tại |
| 5 | 🆕 **Panel kiểu TRANH HANG** — nét nâu đỏ trên nền tối | nói về nghệ thuật hang, ký ức, truyền đời |

### B. NHÓM DẠY HỌC

> # 🔴 LUẬT CỨNG — SƠ ĐỒ PHẢI NÓI ĐƯỢC MỘT ĐIỀU
>
> **Nếu `SUBJECT` là biểu đồ · bảng · trục · sơ đồ, thì `TEXT` KHÔNG ĐƯỢC là `no text`.**
>
> Phép thử một câu: **che lời đọc đi, khung này còn nói được gì không?**
>
> | ⛔ Rỗng ruột — lỗi thật của V18 | ✅ Có nội dung — đối thủ |
> |---|---|
> | biểu đồ cột **không một chữ số** | biểu đồ **có trục %** + mốc `Short / Medium / Long` |
> | cân thăng bằng **hai bên đều `?`** | xương có nhãn `Butcher Cut Marks` ↔ `Stone Tool` |
> | bong bóng thoại **rỗng** | ba cây có tên `HENBANE / AROMATIC HERBS / VARIOUS AROMATICS` |
> | bảng ghi *"names down one side"* mà `TEXT: no text` — **mâu thuẫn trong một prompt** | trục `500 BC → 1960` |
>
> **Đo thật 08/08/2026:** V18 có 18 khung sơ đồ, **15 khung (83%) bị chính prompt ép `no text`**.
> Biểu đồ ra rỗng **không phải** vì AI vẽ dở — prompt viết vậy. V19 sau khi sửa: **0/14**.
>
> ⚠️ **Không lời vẫn được, miễn có nội dung.** Stickly có quả **2,08 triệu** gần như không chữ nào,
> nhưng sơ đồ của họ vẫn nói điều gì đó: thanh tiến trình **có dấu ✗**, sóng não **có nhịp bất thường**,
> hàng biểu tượng **súng · bẫy · thuốc độc**. Cái cấm là **hình dạng rỗng**, không phải cấm im lặng.
>
> Máy đã cưỡng chế: `validate_shots.py` → *"sơ đồ nào cũng phải NÓI được một điều"*.
> Bằng chứng: `kho/3_bangchung/NGUPHAP_HINH_6Kenh_2026-08-08.md`

⚠️ **Copy INK EXPLAINER, không copy Mack.** Hai kênh là hai trường phái: Ink **tự vẽ hết**, cùng một
nét với nhân vật; Mack dùng **clipart + giao diện phần mềm**, và có khung **lộ cả ghi chú sản xuất
vào ảnh thật** *(`STICK FIGURE` · `RAIN CLOUD ICON` · `Line 63`)*. Ba kiểu ghi *"học từ Mack"* dưới
đây là **hàng phụ**, đừng lấy làm mẫu chính.

| # | Kiểu | Ví dụ thật của đối thủ |
|---|---|---|
| 6 | 🆕 **THẺ TIÊU ĐỀ CHƯƠNG CÓ ĐÁNH SỐ** ⭐ | `2. FLOODING` + sóng nước · `3. PREDATORS` + con báo, chữ ĐỎ |
| 7 | 🆕 **Bản đồ có ghim** ⭐ | ghim Qesem Cave (Israel) · Lascaux (Pháp) · Sulawesi · Australia |
| 8 | **Vật đơn + chú thích IN HOA, nền trắng** | `TINDER FUNGUS.` · `IRON PYRITE` |
| 9 | 🆕 **Thẻ chữ thuần** | `YOU MAKE THINGS.` · `NOW WE CAN'T PROVE IT` |
| 10 | 🆕 **Bày bộ đồ nghề có nhãn** | `ÖTZI'S FIRE KIT` — 4 món xếp ra, mỗi món một nhãn |
| 11 | 🆕 **Sơ đồ mặt cắt** | lớp cư trú / lớp trầm tích lũ xen kẽ, có mũi tên chỉ |
| 12 | 🆕 **Mũi tên biến đổi** | voi ma mút → dụng cụ ngà · ochre → bột · đá → rìu có cán |
| 13 | ⚠️ **Hàng biểu tượng có nhãn** — **dạng YẾU NHẤT, dùng dè** | `LION · HORSE · RHINO · BEAR` xếp ngang. Nguồn ghi rõ: thẻ của đối thủ **không phải** hàng biểu tượng gạch chéo đỏ — **đó chính là thứ V17 làm**. Nếu dùng, phải có **một câu dẫn ở trên**: `RAIN COULD KILL YOU IN 3 DIFFERENT WAYS.` + ❄ `COLD` · 〰 `FLOODING` · 🐆 `PREDATORS` |
| 14 | 🆕 **Thẻ so sánh YOU ‖ THEM** | bạn ngủ ôm điện thoại ‖ người cổ đại bên lửa |
| 15 | 🆕 **Biểu đồ cột so sánh** *(học từ Mack)* | `HUNTER-GATHERER` cột xanh cao ‖ `SEDENTARY` cột cam thấp |
| 16 | 🆕 **Timeline quy trình có mốc** *(học từ Mack)* | `DAY 1: ANIMAL KILL` → `WEEKS 1-3: TANNING` → `WEEKS 4+: FINISHED` |
| 17 | 🆕 **Thẻ phá lầm tưởng** *(học từ Mack)* | `MODERN FICTION` gạch chéo đỏ |

**Cộng biểu tượng chức năng** rải trên bất kỳ khung nào: ✅ xanh · ❌ đỏ · 🚫 vòng cấm · mũi tên đen.

> ### 🆕 07/08 — BỐN THỨ NGUỒN CHỈ RA MÀ 17 KIỂU TRÊN CHƯA CÓ
> *(chép từ `kho/3_bangchung/NGUPHAP_HINH_DoLai_ToanBo_2026-07-30.md` §4, §5, §9 — đọc file đó khi cần đủ 17 kiểu đo từ khung thật)*
>
> **1. Thẻ chữ trộn HAI ĐỘ ĐẬM trong cùng một câu** — vế dẫn mảnh, vế chốt đậm và to hơn.
> `RAIN DIDN'T STOP THE FOOD SUPPLY.` *(mảnh)* → **`IT CHANGED IT.`** *(đậm)*
> Gần như luôn kèm **một hình nhỏ vẽ tay bên cạnh**, và đôi khi một phụ đề chữ thường bên dưới:
> `2014` + *Anthropologist Polly Wiessner published a study.*
>
> **2. Nhãn dán LÊN CẢ KHUNG CẢNH**, không chỉ nền trắng — ô nhãn nhỏ ở góc trên:
> `CHIMPS — TODAY` · `EARLY HUMANS` *(gạch chân)*. Và nhãn sơ đồ là chữ ALL-CAPS **nhỏ** viết tay
> + **mũi tên mảnh**, không phải hộp chữ to.
>
> **3. CHỮ TƯỢNG THANH viết tay ngay trong cảnh** — `DRIP DRIP` · `PATTER-PATTER...` · `SHHHHHHH...`
> · `Rumble.` · `Plink` · `zzZz...` bay quanh nhân vật. **Rẻ, cực hiệu quả, làm cảnh tĩnh có tiếng.**
> Kênh mình chưa dùng lần nào.
>
> **4. Quầng sáng vàng bọc quanh vật quan trọng** để nhấn — dùng cả trong sơ đồ nan hoa
> *(`ROPE` giữa, 4 nhánh toả ra)* lẫn trong khung cảnh.

### CÁCH CHỌN — bám nội dung câu, không bám thói quen

| Trong lời đọc có | → dùng kiểu |
|---|---|
| **một địa danh / di chỉ** | **7 — bản đồ có ghim.** Mỗi lần nhắc một nơi là một bản đồ |
| bắt đầu một chương mới | **6 — thẻ tiêu đề đánh số** |
| một bộ đồ vật, một danh sách món | **10 — bày bộ có nhãn** |
| lớp lang, tầng, cấu tạo bên trong | **11 — sơ đồ mặt cắt** |
| "X trở thành Y", "từ A ra B" | **12 — mũi tên biến đổi** |
| liệt kê nhiều con vật / nhiều thứ cùng loại | **13 — hàng biểu tượng** |
| đối chiếu bạn ↔ tổ tiên | **14 — thẻ so sánh** |
| câu chốt, cú đấm | **9 — thẻ chữ thuần** |
| một con số lớn | **9 — thẻ chữ, số VIẾT TO** |

**Sau khi chia xong: đếm và GHI LẠI tỉ lệ hai nhóm** để sau này đối chiếu với view thật.
Nhưng **không có ngưỡng đạt/trượt**, và **đừng sửa shot cho tỉ lệ đẹp** — đó đúng là điều LUẬT 0 cấm.

Câu hỏi đúng cho mỗi shot: **"cái đang đọc là một khái niệm hay một khoảnh khắc?"**

## PHẦN 5 — CHỮ TRÊN HÌNH

Chữ trên hình là **công cụ mạnh và kênh mình dùng ít hơn mức nên dùng**. Nó làm video xem được cả
khi tắt tiếng, và là chỗ nhét mỏ neo khoa học mà lời đọc không kịp nói hết.

⚠️ **Nhưng không có chỉ tiêu.** Đo 4 kênh: Zenn ~50% khung có chữ *(trung vị 29.000)*, còn **Mack
— kênh trung vị cao nhất, 45.000 — không dùng chữ nào**, Explain In Paint cũng vậy. Dùng chữ khi
câu đó **có một con số đắt, một tên vật, hoặc một cú chốt**. Đừng rải cho đủ tỉ lệ.

**KHÔNG phải phụ đề chép lại lời đọc** — chép lời đọc vẫn cấm.

### Bốn loại chữ được dùng

| Loại | Ví dụ thật | Dùng khi |
|---|---|---|
| **Nhãn vật thể** | `TINDER FUNGUS.` · `IRON PYRITE` | mỗi lần lời đọc gọi tên một vật |
| **Nhãn sơ đồ + mũi tên** | `WET OUTSIDE` ↔ `DRY INSIDE` · `DELICATE` / `PRECISE` | giải thích cơ chế |
| **Con số viết TO** | `52,000 YEARS AGO.` · `5,300 YEARS OLD.` · `77,000 YEARS AGO. PEST CONTROL.` | mọi mốc thời gian và mọi con số đắt |
| **Câu chốt thuần chữ** | `YOU MAKE THINGS.` · `HERE'S WHY THAT WAS TERRIFYING.` · `NOW WE CAN'T PROVE IT` | cú đấm, chuyển chương |

### Quy cách

- IN HOA, nét bút dạ đậm, **đen** trên nền sáng
- **ĐỎ** cho: dấu ❌, vòng cấm, và tên chương nguy hiểm *(`3. PREDATORS` chữ đỏ)*
- **XANH LÁ** cho ✅
- Chữ khớp **1-4 từ đắt** trong lời shot, hoặc là một con số
- Chú thích nhỏ dưới hình được phép: *"Actual bedding — 77,000 years old."*

### Vì sao quan trọng hơn ta tưởng

Chữ làm video **xem được cả khi tắt tiếng** — và một phần lớn lượt xem YouTube là tắt tiếng hoặc xem lướt. Nó cũng là chỗ nhét mỏ neo khoa học mà lời đọc không kịp nói hết.

## PHẦN 6 — 6 NÂNG CẤP ĐỂ HƠN ĐỐI THỦ (bake vào prompt)

1. **Nét run tay ĐÚNG như competitor** *(sửa 30/07/2026)*: giữ chữ **"hand-drawn doodle, wobbly marker outlines"** — đây là chất của lane, không phải khuyết điểm. Đè họ bằng **nhất quán nhân vật + biểu cảm**, KHÔNG bằng nét sạch hơn. Nét sạch hơn = ra hoạt hình = **lạc lane**.
2. **Nhất quán nhân vật**: lặp y khối mô tả (PHẦN 3) mọi lần → khắc phục điểm yếu drift của họ.
3. **Biểu cảm MẠNH hơn**: luôn ghi rõ biểu cảm (mắt to khi sốc) — thứ ăn thumbnail.
4. **Màu con vật/đồ vật tương phản cao trên trắng** — điểm nhấn sắc.
5. **Chữ label gọn, đỏ cho nhấn** — như Mack nhưng tiết chế.
6. **Đọc-1-giây**: mỗi frame 1 ý hình rõ; đừng nhồi 2-3 ý vào 1 ảnh.

---

## PHẦN 7 — CHỐNG DÍNH CHÍNH SÁCH (lọc từ)

Ngách hay chạm bạo lực/săn mồi/khỏa thân tiền sử → tránh từ dễ bị chặn:
- `naked/nude/bare` → `fur-free` hoặc bỏ (thân người vốn trắng, không cần tả trần).
- `blood/gore/kill` cận cảnh → gợi ý gián tiếp (`predator lunging`, `bite marks on a skull`), không tả máu me.
- Cảnh em bé + thú dữ: giữ **biểu tượng/gián tiếp** (bóng thú, mắt trong tối), không tả tấn công trực diện.
- Nếu 1 shot đẩy tới vùng rủi ro → **gắn cờ 1 dòng cho user** + đề xuất cách vẽ an toàn hơn.

---

## PHẦN 8 — ĐỊNH DẠNG XUẤT (mặc định)

Xuất **bảng 3 cột**, số dòng = số ảnh = số shot:

| # | 🗣️ Dòng-SHOT (nạp TTS, thuần EN) | 🖼️ Prompt ảnh (gen-ready, dán thẳng) |
|---|---|---|
| 001 | You're asleep, drooling on your pillow, | *(⚠️ ví dụ CŨ — "short black hair, blue hoodie" sai: `identity/style.py` khối `MODERN` là **đầu TRỌC, thân que trần, không quần áo**)* Rough low-budget educational doodle… a modern white stick figure… lying asleep on a simple brown bed, eyes closed, tiny "z z z", … flat minimal colors ONLY on… 16:9. |
| 002 | probably snoring, zero awareness. | [ANCHOR] … same modern white stick figure … mouth open snoring, "ZZZ" bold, … [LOCK] |

Kèm cuối:
- **1 dòng "ghép TTS":** nhắc user rằng khi tạo audio, nạp **toàn bộ cột Dòng-SHOT** (tool tự đọc liền mạch — dấu câu đã có sẵn).
- **Cờ chính sách** (nếu có shot rủi ro).
- Ảnh gen ra đặt tên **001.png … NNN.png** đúng thứ tự → nạp thẳng GhepVideo, sync 100% theo timestamp.

Mặc định trả **trọn bộ** cho cả script. Nếu script rất dài (>120 shot) → có thể xuất theo đợt (mỗi đợt ~40-60 shot) để giữ chất lượng prompt, hỏi user "tiếp" giữa các đợt.

---

## PHẦN 9 — THUMBNAIL (bước BẮT BUỘC mỗi video)

Thumbnail + title = **80% CTR** → mỗi video PHẢI có ≥1 thumbnail theo **skill `sketchapiens-thumbnail`** — nguồn DUY nhất từ 09/08 *(gộp cả prompt dán thẳng; hai file kho `PROMPT_TONG_Thumbnail_v6` và `TEMPLATE_Thumbnail_KHOA_v1` đã xoá)*. Bằng chứng: `kho/3_bangchung/CO_CHE_3LOP_Winner_2026-07-29.md`.

> ⛔ **KHÔNG dùng `TEMPLATE_Thumbnail_DoiThu.md`** — file đó đã chết (dán biển 29/07/2026). ADN cũ của nó, "nhân vật lệch TRÁI + vật màu bên PHẢI", đã bị bác: soi lại 7 quả thắng cho thấy nhân vật nằm trái, phải, giữa, hai mép, và có quả không có nhân vật nào.

- **Điền chỗ trống** vào PROMPT ở §⑥ của skill `sketchapiens-thumbnail`: `{KHUÔN}` · `{VẬT KỂ CHUYỆN}` · `{NHÂN VẬT + VỊ TRÍ + BIỂU CẢM TỔ HỢP}` · `{ÁNH MẮT}` · `{NỀN}` · `{MÀU + 1 điểm bão hoà}` · `{CHỮ 1-3 TỪ NÓNG}`.
- **ADN thắng (bám chặt):** **CENTRE ANCHOR** — tâm khung dành cho VẬT KỂ CHUYỆN, không phải nhân vật (7/7 quả to nhất) · ⛔ ~~chữ phải nói thứ KHÁC title (hai quả…)~~ — **BỊ BÁC.** `PROMPT_TONG_Thumbnail_v6.md` đo **44 thumbnail / 9 kênh**: hơn **25/36 quả LẶP hoặc nén lại chính title**; Explain In Paint lặp **6/6**; quả 1 triệu của Ink: title *"…When It Rained All Week?"* → chữ `RAINED ALL WEEK`. **Lặp title không bị phạt.** Cái quyết định là chữ phải chứa **MỘT ĐẠI LƯỢNG ĐO ĐƯỢC** *(`2 SLEEPS?` · `ALL DAY` · `-40°`)* · mọi ánh mắt khoá vào trong khung · các khuôn mặt phải khác cảm xúc nhau · nền xỉn + đúng 1-2 điểm bão hoà · chữ VÀNG viền đen 1-3 từ + "?" sát mép trên, **~22% chiều cao** *(⛔ luật cũ "13-19%" ĐÃ CHẾT — đo máy 29 quả thắng ra trung vị **22%**; thumbnail V18 bản 2 để 15% chính là hậu quả của luật sai đó)*.
- **Luân phiên 7 khuôn bố cục, không lặp khuôn hai video liền.** Cấm khuôn "hiện đại TRÁI ↔ cổ đại PHẢI" (kênh dùng 11/11, chỉ 2/29 quả thắng dùng).
- **Xuất 1 concept chính + 1 fallback** (phòng khi AI vẽ chi tiết phức tạp bị rối).
- **Chữ trên thumbnail:** các model image mới (GPT-4o image, Nano Banana 2 / Gemini 3) vẽ chữ NGẮN 2-3 từ khá tốt → cứ để nguyên prompt CÓ chữ, gen thẳng, thường ăn ngay. Chỉ khi bản nào chữ bị méo/sai → gen lại vài lần (hoặc fallback thêm chữ bằng Canva — không bắt buộc).
- **Đồng bộ nét:** nên gen thumbnail cùng tool với ảnh video (Nano Banana/Flow); ChatGPT image / DALL·E cũng được, chỉ nét hơi khác — chấp nhận được cho thumbnail.

---

## Ghi nhớ cuối
Nhất quán = **kỷ luật lặp chữ**, không phải token. **Nền theo NGỮ CẢNH** (trắng cho khái niệm/chữ/so sánh, cảnh flat-màu cho môi trường thật) — KHÔNG mặc định, KHÔNG theo tỉ lệ; tỉ lệ tự nổi ra theo nội dung. Mỗi ảnh kể đúng 1 vế đang đọc, đọc-hiểu-trong-1-giây, con vật là điểm màu (chi tiết hơn người que). Nét **RUN TAY** *(hand-drawn, wobbly marker)* — ⛔ ~~sạch digital~~ **sai**, xem PHẦN 6 mục 1 và `identity/style.py` *(`wobbly` xuất hiện **7 lần**, `clean` **0 lần**)*. Nét sạch hơn = ra hoạt hình = **lạc lane**. Nhấn: đỏ nguy hiểm · xanh ✓ · vàng ý tưởng. Học công thức đã thắng của đối thủ + nhất quán hơn + biểu cảm mạnh hơn = hơn nó ở mọi mặt.

---
---

## PHẦN 10 — QUY TRÌNH DỰNG + BẢNG KIỂM BẮT BUỘC ⭐ *(thêm 30/07/2026)*

> **Vì sao có phần này.** Làm V17 (263 shot) tôi mắc **9 lỗi**, trong đó **8 lỗi do chủ phát hiện chứ không phải tôi**. Gốc chung: *làm theo trí nhớ thay vì mở nguồn ra đối chiếu*, và *tự chấm điểm trước khi đo*.
> Phần này biến mấy phép kiểm đó thành **script chạy được**, để lần sau không phụ thuộc trí nhớ.

### KHÔNG gõ tay 250 prompt. Dùng 2 file trong `templates/`

```
templates/build_prompts.py    ← ráp prompt từ shot_data.py
templates/validate_shots.py   ← kiểm 15 hạng mục TRƯỚC KHI GEN
```

**Quy trình:**
```
1. copy 2 file trên vào thư mục VideoNN/
2. viết shot_data.py  — mỗi shot là (dòng-shot, kiểu, subject, text, nền)
3. python3 build_prompts.py          → SHOTLINES_FULL.txt + PROMPTS_FULL.txt
4. python3 validate_shots.py Script_VideoNN_narration.txt
5. CHỈ GEN KHI IN RA "SẴN SÀNG GEN."
```

### 🔴 PHÉP KIỂM QUAN TRỌNG NHẤT — GHÉP SHOT PHẢI KHỚP NGUYÊN VĂN NARRATION

Ghép tất cả dòng-shot lại phải ra **đúng từng chữ** narration đã duyệt.

Ở V17 phép này bắt được **một câu bị làm rơi khi viết lại kịch bản** và **một chữ thừa lấy nhầm từ bản cũ**. Không có nó thì **TTS đọc một thứ khác với kịch bản đã duyệt** — đúng loại lỗi âm thầm đã làm hỏng V15 và phải đăng lại.

### BỐN LUẬT ĐÚC TỪ LỖI THẬT CỦA V17

| # | Luật | Lỗi đã gây ra |
|---|---|---|
| 1 | **Nhãn NHỎ có mũi tên ≤3-4 từ.** ⚠️ ~~mọi nhãn ≤3 từ~~ — **tiêu đề thẻ thì KHÔNG**: đối thủ dùng cả câu, ví dụ `RAIN DIDN'T STOP THE FOOD SUPPLY.` Đo 1.090 khung. | nhãn 4-6 từ → model vẽ sai chính tả. Nhãn đối thủ gần như toàn 1-3 từ: `TINDER FUNGUS.` · `DRY INSIDE` · `FIRE KEEPER` |
| 2 | **Mọi prompt phải có khối `Framing:`** | quên khối này → 263 ảnh ra cùng một cỡ khung. Nó nằm sẵn trong PHẦN 2 mà tôi không đọc lại |
| 3 | **Khung có chữ phải kèm lệnh ép chính tả** | `The lettering must be spelled EXACTLY as written above… no gibberish letters.` |
| 4 | **ĐÍNH ẢNH THAM CHIẾU STYLE khi gen** | tả style bằng lời **trượt hai vòng** ở thumbnail V17; đưa ảnh vào là trúng ngay. Ghi ở đầu `PROMPTS_FULL.txt`:<br>`Use the attached image ONLY as a STRICT STYLE reference — copy its line weight, character proportions, face style and flat colouring. Do NOT copy its composition or its content.` |

### BA LUẬT NỮA — ĐÚC TỪ ĐỢT GEN THẬT ĐẦU TIÊN *(30/07/2026, 190 ảnh)*

| # | Luật | Bằng chứng |
|---|---|---|
| ~~5~~ | ⛔ **LUẬT NÀY ĐÃ BỊ CHÍNH FILE NÀY BÁC** — xem mục *"ĐO LẠI TỬ TẾ"* #3 bên dưới: *"Nền cảnh HAI DẢI MÀU TRƠN là ĐÚNG… hôm trước tôi 'sửa' bằng cách nhồi cây cối vào — **sửa nhầm, đã trả lại**"*. Khung savanna của Ink Explainer chỉ có một dải trời + một dải cát + một mặt trời. **Đạo cụ thêm khi cảnh cần, không phải luật.** | ảnh gen ra chỉ có dải trời + dải đất, trống trơn. Khung đối thủ **luôn** có 3-6 vật vẽ tay: cây, bụi cỏ, đá, mặt trăng, vũng nước. Nền trơn = dấu hiệu ảnh AI rẻ tiền. Viết thẳng đạo cụ vào chuỗi nền, và thêm câu `The background must contain the hand-drawn props listed above, NOT just two plain bands of flat colour.` |
| 6 | **Chặn gradient + hào quang trong NEG** | ảnh ra tường nền gradient + đầu nhân vật có highlight bóng. Thêm `no gradient background, no soft glow, no vignette, no drop shadow`. |
| 7 | **Chữ phải là NÉT VIẾT TAY, không phải font** | thẻ tiêu đề ra chữ font sạch. Ép: `IRREGULAR HAND-LETTERED ALL-CAPS marker writing (each letter drawn by hand, slightly uneven, NOT a clean computer font)`. |

### 🔴 KHI ẢNH HỎNG — HỎI "HỎNG CHỖ NÀO" TRƯỚC KHI SỬA *(30/07/2026)*

Chủ nói *"nhìn như hoạt hình"*. Tôi hiểu thành **cả bộ style sai** → viết lại STYLE, NEG, nền, khối nhân vật, chữ. Đợt gen sau ra **ký hoạ chì, phố có phối cảnh, nhân vật tự mọc áo khoác** — hỏng nặng hơn bản gốc.

Thật ra chủ chỉ nói về **một khối duy nhất: người cổ đại**. Nền, bản đồ, thẻ chữ, anh hiện đại đều đã đạt.

**Luật:** ảnh hỏng thì **xác định ĐÚNG khối nào hỏng** rồi chỉ sửa khối đó. Prompt ở đây lắp từ 6 khối rời — đó chính là để sửa được từng khối một. Sửa cả 6 khối vì một lời chê là **vứt luôn phần đã đạt**.

Trước khi sửa: **cắt nhân vật của mình đặt cạnh nhân vật đối thủ** rồi nhìn. Mất 2 phút, và nó chỉ thẳng ra chỗ khác nhau thay vì phải đoán.

### CÁI GÌ LÀM NGƯỜI QUE TRÔNG NHƯ "HOẠT HÌNH"

Đặt cạnh khung gốc mới thấy — bốn thứ, không phải nét vẽ:

| Của mình (ra hoạt hình) | Của đối thủ |
|---|---|
| tóc là **một mảng nâu mượt, bo tròn** như tóc bob | **búi xù rối**, cụm tóc nhọn, rìa lởm chởm, vài sợi chĩa ra |
| đầu **oval, có cằm, có cổ** | **tròn vành vạnh**, không cằm, đầu đặt gần như thẳng lên vai |
| mắt **to có mí**, lông mày cong buồn, miệng mở | mắt **nhỏ đơn giản**, miệng **một nét lượn** |
| khố là **mảng nâu phẳng lì** | rìa dưới **rách nham nhở**, vài nét gợi lông thú, **dây quấn chéo ngực** |

Ba chữ phải có trong khối nhân vật: `deliberately crude`, `MESSY SCRIBBLED`, `NOT as a cute cartoon child`.

### 📐 ĐO LẠI TỬ TẾ — 30 KHUNG NỮA, CẢ HAI KÊNH *(30/07/2026)*

Bốn kết luận, mỗi cái bác một thứ tôi từng viết sai:

**1. MỌI người trong khung đều là NGƯỜI QUE ĐẦU TRÒN TRẮNG.** Cả hai kênh, không có một khung nào dùng **bóng người đen đặc** kiểu biển báo nhà vệ sinh. Kể cả sơ đồ trừu tượng ("ba người truyền nhau", "một hàng ba mươi người") vẫn vẽ bằng người que.
→ **Cấm chữ `silhouette` trong subject.** Nó dịch thẳng ra pictogram đen. Viết `plain grey stickman figure (the same LARGE round head and thin stick limbs, drawn plain with no face)`.

**2. Biểu tượng vẽ CÙNG một tay với nhân vật.** Cây đũa phép, cái lều, cái đồng hồ đo, đống lửa — tất cả cùng nét viền đen, cùng độ dày. Không có món nào là **clipart tải về**. Khung "WHAT IT DOES PROVE" của mình (mũi tên xanh + bánh răng vàng + tick xanh) là đồ hoạ công ty, lạc hoàn toàn.
→ NEG_FLAT phải có: `no stock clipart, no icon-pack art, no corporate infographic style, no glossy icons`.

**3. Nền cảnh HAI DẢI MÀU TRƠN là ĐÚNG.** Khung savanna của Ink Explainer: một dải trời xanh + một dải cát + một mặt trời. Hết. Hôm trước tôi "sửa" bằng cách nhồi cây cối vào — **sửa nhầm**, đã trả lại.

**4. Khung dạy học của họ CÓ NHÂN VẬT.** Thẻ `SKILL 1 vs SKILL 2` là hai người cổ đại hai bên một đường kẻ đứt. Không phải hình trừu tượng. Khung dạy học không có nghĩa là bỏ nhân vật đi.

**Lỗi quy trình của tôi:** vá theo từng ảnh lẻ chủ gửi, mỗi lần sửa một chỗ rồi hỏng chỗ khác. Đáng lẽ **soi 30 khung trước, sửa một lần**. Trước khi đụng vào file style, bắt buộc trích ≥24 khung của đối thủ và xem, không được sửa theo trí nhớ hay theo một ảnh.

### ⚠️ GOOGLE FLOW CHẶN PROMPT >4000 KÝ TỰ

`Flow.generate.image() validation failed: Prompt too long (max 4000 characters)`

Các khối cố định dễ phình mà không ai để ý — ở V17 chúng ngốn **3.270 ký tự** trước khi thêm nội dung shot, làm 10 prompt vượt ngưỡng.

**Ngân sách nên giữ:**

| Khối | Tối đa |
|---|---|
| STYLE | ~700 |
| Khối nhân vật | ~1.000 |
| NEG | ~450 |
| *(còn lại cho subject + framing + scene + text)* | ~1.800 |

`validate_shots.py` nay có sẵn phép kiểm này. Rút gọn thì **bỏ chữ thừa, đừng bỏ luật** — mỗi luật trong khối nhân vật đều đúc từ một lỗi thật.

### ⛔ ĐỪNG XOÁ WATERMARK CỦA FLOW — ĐỂ NGUYÊN

Ảnh Flow có một ngôi sao mờ ở góc dưới-phải. **Kệ nó.**

31/07 tôi tự thêm một bước `clean_images.py` cắt 9% mép phải + mép dưới để xoá nó. Kết quả: **ăn mất dấu chấm cuối câu trên thẻ chữ**, đẩy mọi thứ dính sát mép. Chủ phát hiện khi xem V17.

Câu hỏi đúng đáng ra phải hỏi trước: *"V16 xử lý watermark thế nào?"* Trả lời: **không xử lý gì cả.** V16 nối thẳng thư mục ảnh gốc vào bước ghép, và không ai thấy vấn đề.

**Luật:** không thêm bước mới vào một quy trình đã chạy 16 video, trừ khi có lỗi thật cần chữa. Watermark mờ ở góc không phải lỗi thật.

### ⚠️ TOOL GEN CÓ THỂ CHẶN SỐ LƯỢNG MỘT ĐỢT

Đợt đầu nạp 263 prompt → chỉ ra **190 ảnh**. Nếu tool không nuốt hết một lần thì **chia theo dải và đặt tên thư mục theo dải** (`001-130`, `131-263`), đếm từng dải riêng, rồi mới gộp. Đừng chạy đợt hai vào cùng thư mục — bộ đếm sẽ đặt tên đè lên (lỗi V14: 404 ảnh cho 301 prompt).

### BA LUẬT KHI GEN *(lỗi cũ của kênh)*

- **Gen vào thư mục RỖNG, MỘT lượt.** Bộ đếm của tool đặt tên theo thứ tự nó chạy, không theo số prompt. V14 ra **404 ảnh cho 301 prompt** vì chạy hai đợt.
- **Đếm file == số prompt** trước khi ghép.
- **Kiểm trước mấy kiểu khung kênh chưa từng làm** — bản đồ, thẻ tiêu đề chương, sơ đồ mặt cắt. Gen 5 ảnh thử rồi mới chạy phần còn lại.

### THÓI QUEN PHẢI BỎ

| Bỏ | Thay bằng |
|---|---|
| làm theo trí nhớ | **mở bản trước ra đối chiếu** — file, tên, template, quy ước |
| tự chấm "đạt" khi chưa đo | **đo trước, kết luận sau** |
| đúc luật từ mẫu nhỏ rồi sửa file hệ thống | **nói cỡ mẫu ra trước**, dưới 10 thì ghi rõ là chưa chắc |

# 🧱 CAST PACK ĐẦY ĐỦ — Sketchapiens *(bản chi tiết — chuẩn nhất)*

> Tạo theo **thứ tự 1 → 12**. Từ ảnh **#2 trở đi → ĐÍNH ẢNH #1 (base)** để cùng một gương mặt. Con vật/đạo cụ (#11–12) tạo riêng.
> # 🔴🔴 CÙNG XUNG ĐỘT NHÂN VẬT NHƯ `Prompts_NhanVat_Kenh.md` — dán 09/08/2026
>
> Dòng "Style (khóa)" bên dưới **KHOÁ SAI BA THỨ**. Nó tả một nhân vật **KHÁC** với
> `identity/style.py` — file **thật sự sinh ảnh** *(`tools/build_prompts.py` làm `from style import *`)*:
>
> | | file này *(SAI)* | `identity/style.py` *(ĐÚNG — máy đang chạy)* |
> |---|---|---|
> | **Mắt** | `mắt chấm` — dán cho **mọi** nhân vật | `ANCIENT`/`WOMAN`: *"eyes = TWO LARGE ROUND WHITE EYES… **Never tiny dots**"*. ⚠️ Chỉ **`MODERN`** mới là *"small black dot eyes"* — mà khách mời đó chỉ ~10-15% khung |
> | **Tóc** | `tóc đen ÍT nét` | *"hair = MEDIUM BROWN… a **SHAGGY MANE** of many fine wavy strands… **Never black**, never a spiky ball on top"* |
> | **Tay chân** | `nét ĐẬM/DÀY (marker to)` | *"arms and legs = **THIN** single black lines, slightly crooked, no joints"* |
>
> Nguy nhất là **mắt**: `01_base.png` bên dưới là **khung xương gốc** mà mọi ảnh sau đính vào —
> base mắt chấm thì **cả bộ** thừa kế mắt chấm, kể cả nhân vật chính.
>
> Gen ảnh theo file này rồi ghép với ảnh do máy sinh → **hai nhân vật khác nhau trong một video**.
> **Khi hai file cãi nhau, `.py` thắng** — nó là thứ đang chạy, và luật của nó thường được sửa
> bởi một lần gen hỏng có thật.
>
> ✅ Thứ trong dòng dưới **vẫn đúng**: thân + mặt **TRẮNG ĐẶC** *(không tô da)* · nét **hơi run**
> · màu **MUTED** chỉ ở đồ/nền · KHÔNG mascot/3D/bóng bẩy.
>
> ⛔ **Và cả quy trình `refs/<token>.png` trong file này đã chết** *(`D-04`)* — nhất quán nay
> làm bằng **lặp y nguyên khối chữ**, không bằng ảnh ref, không bằng `@token`.
> Mọi `@SCIENTIST` / `@FORAGER` / `@CHILD` / `@ELDER` bên dưới **không còn là thứ phải tạo**.
> *(Thêm nữa: persona "người dẫn nhà khoa học" có **0 ca thắng / 16 kênh**.)*

> ⛔ ~~**Style (khóa):**~~ *(xem khung đỏ trên — ba mục đã sai)* doodle thô low-budget · **thân + mặt TRẮNG** (không tô da) · **nét marker đen hơi run** · ~~tay chân nét ĐẬM/DÀY~~ · ~~tóc đen ÍT nét~~ · ~~mắt chấm~~ · mặt **ngu-ngơ/hài** · màu **MUTED tiền sử** chỉ ở **đồ/đạo cụ/nền** · KHÔNG bóng bẩy, KHÔNG mascot, KHÔNG 3D. (Vàng tươi chỉ cho chữ thumbnail.)
> Chi tiết: **`identity/style.py`** *(nguồn chuẩn duy nhất; `ArtBible` đã xoá 09/08)* · giữ nhất quán: `SOP_NhatQuan_NhanVat`.

---

## 🅰️ SHEET (khung · mặt · tư thế · đạo cụ)

### 1. `01_base.png` — KHUNG XƯƠNG GỐC *(tạo TRƯỚC, không đính gì)*
```
Create a rough low-budget educational doodle animation frame. One simple primitive white stick-figure human, front view, plain white background. Paper-white round head, slightly uneven and hand-drawn, with BOLD THICK wobbly black marker outlines. Very simple dumb face: tiny black dot eyes, one short single-line mouth, no nose, small thin eyebrows. Messy sparse black scribble hair (a few loose strands, not thick). Body extremely simple: BOLD THICK single-stroke black arms and legs (fat marker, not thin), tiny oval white hands and feet, loose awkward proportions, slightly wobbly, with a dumb, slightly tired/helpless look. Cheap, primitive, hand-drawn. No skin tone, no body fill, no polished mascot, no clean vector, no anime, no 3D, no gradients, no shadows, no text.
```

### 2. `02_turnaround.png` *(đính #1)*
```
Using the attached character, show the SAME character in a turnaround lined up: FRONT, SIDE, BACK. Keep identical: paper-white body, bold thick wobbly black marker outline, bold thick stick limbs, sparse messy black hair, tiny dot eyes, one-line mouth, no nose, oval hands/feet. Plain white background. Crude, cheap, hand-drawn. No text.
```

### 3. `03_expression.png` — 8 MẶT HÀI *(đính #1)*
```
Using the attached character, show the SAME head in 8 FUNNY expression panels on a plain white grid, exaggerated for comedy: 1 DEADPAN blank stare (tiny dot eyes, flat line mouth); 2 BUG-EYED shock (huge eyes, pinprick pupils, gaping "O" mouth); 3 nervous sweat (side-glance, wobbly mouth, sweat drop); 4 dumb goofy grin; 5 unimpressed side-eye (half-lidded); 6 over-the-top crying (waterfall tears, square mouth); 7 confused (one raised eyebrow, squiggly mouth); 8 cross-eyed dizzy. Humor from simple eyes + mouth pushed to extremes. Keep same head, sparse messy black hair, no nose, bold thick wobbly outline. Crude, not polished. No text.
```

### 4. `04_pose.png` — 8 TƯ THẾ *(đính #1)*
```
Using the attached character, show the SAME full-body character in 8 poses on a plain white background: standing front, standing side, walking, running, sitting, lying down asleep, pointing, raising both arms (shocked). Keep identical DNA: paper-white, bold thick wobbly outline, bold thick stick limbs, sparse messy hair, dot eyes, no nose. Crude, cheap, hand-drawn. No text.
```

---

## 🅱️ COSTUME *(mỗi ảnh ĐÍNH #1 — giữ nguyên mặt, chỉ thay đồ)*

### 5. `05_modern.png` = @MODERNYOU
```
Using the attached character, keep the SAME white body/face DNA, dressed modern: a plain hoodie and pants in flat muted dusty denim blue (#5B86B0), holding a small phone. Keep sparse messy black hair, dot eyes, no nose, bold thick wobbly outline, bold thick limbs. Show front + 3 expressions (deadpan, shocked, goofy). Plain white background. Flat color only on clothes/phone. No text.
```

### 6. `06_caveman.png` = @ANCESTOR
```
Using the attached character, keep the SAME white body/face DNA, as a caveman: a simple ragged animal-skin tunic in flat muted brown with torn edges, sparse messy black hair + scruffy beard, barefoot, holding a crude wooden spear. Bold thick wobbly outline, bold thick limbs, dot eyes, no nose. Show front + 3 expressions (deadpan, shocked, scared). Plain white background. Flat color only on fur/spear. No text.
```

### 7. `07_forager.png` = @FORAGER
```
Using the attached character, keep the SAME white body/face DNA, as a female forager: longer sparse messy hair tied back, a simple plant-fiber wrap in flat muted tan/olive, holding a woven basket. Bold thick wobbly outline, bold thick limbs, dot eyes, no nose. Show front + 3 expressions. Plain white background. Flat color only on wrap/basket. No text.
```

### 8. `08_child.png` = @CHILD
```
Using the attached character, keep the SAME DNA but as a SMALL child (bigger head, short body), sparse messy hair tuft, a tiny simple fur wrap. Bold thick wobbly outline, bold thick limbs, dot eyes, no nose. Show front + 3 expressions (curious, giggling, scared). Plain white background. No text.
```

### 9. `09_elder.png` = @ELDER
```
Using the attached character, keep the SAME DNA, as an elder: sparse messy GREY hair + grey beard, slightly hunched, a simple fur wrap, leaning on a crude wooden staff. Bold thick wobbly outline, bold thick limbs, dot eyes, no nose. Show front + 3 expressions. Plain white background. Flat color only on staff/wrap. No text.
```

### 10. `10_scientist.png` = @SCIENTIST *(dùng vừa phải)*
```
Using the attached character, keep the SAME DNA, as an explainer: a simple white lab coat and plain round glasses, holding a clipboard. Bold thick wobbly outline, bold thick limbs, sparse messy hair, dot eyes, no nose. Show front + 3 expressions (explaining/pointing, thinking, eureka). Plain white background. No text.
```

---

## 🅲️ CON VẬT + ĐẠO CỤ *(con vật TÔ MÀU muted — không cần đính base)*

### 11. `11_chimp.png` = @CHIMP
```
Rough low-budget educational doodle, a simple chimpanzee covered in flat muted brown, bold thick wobbly black marker outline, a simple dumb face with dot eyes, same crude doodle world as the stick humans. Show front + side + 2 expressions (calm, surprised). Plain white background. No text.
```
**Mẫu con vật khác:** đổi `[con vật]` + `[màu muted]` — sói xám `#A6ABAF`, sư tử vàng trầm, hổ cam trầm-vằn… giữ "bold thick wobbly marker, simple, same doodle world".

### 12. `12_prop_sheet.png` — ĐẠO CỤ
```
A rough low-budget educational doodle PROP SHEET on a plain white background: a small campfire, a triangular tent, a pile of grey rocks, a simple bed, a smartphone, an old TV, a tree, a bone, a wooden spear, a simple brain icon. All in the SAME crude style: bold thick wobbly black marker outline, flat muted color, simple and slightly scribbly. No characters. Consistent line weight. No text.
```

---

## ✅ Cách chạy 1 lượt
1. Tạo **#1 base** (2–3 lần, chọn bản ưng) → gốc.
2. **Đính #1** vào mỗi lần tạo #2–#10. #11–12 tạo riêng.
3. Lưu đúng tên file vào `refs/` *(⛔ registry `CastBible` đã xoá 09/08 — không còn sổ đăng ký; khối nhân vật nay nằm trong `identity/style.py`)*. ~~(`../1_luat/CastBible_DienVien.md`).
> Màu giữ **MUTED**; **vàng tươi chỉ cho chữ thumbnail**, không tô lên nhân vật.

---

## 🎯 VIDEO #1 ("lông cơ thể") — CHỈ cần tạo nhiêu đây (~5 người + ~5 con vật)

**Nhân vật (5):** `#1 base` · `#3 expression` (8 mặt hài) · `#5 modern` (@MODERNYOU) · `#6 caveman` (@ANCESTOR) · `#11 chimp` (@CHIMP).

**Con vật theo kịch bản (prompt sẵn — nền trắng, tô màu MUTED, cùng style thô):**
```
GẤU:      Rough low-budget educational doodle, a simple bear covered in flat muted brown, bold thick wobbly black marker outline, dot eyes, same crude doodle world as the stick humans. Plain white background. No text.
SÓI:      Rough low-budget educational doodle, a simple wolf in flat muted grey, bold thick wobbly black marker outline, dot eyes, same crude doodle world. Plain white background. No text.
MÈO:      Rough low-budget educational doodle, a simple house cat in flat muted grey, bold thick wobbly outline, dot eyes; AND a second version with its fur puffed up / bristling (scared). Same crude doodle world. Plain white background. No text.
CHÓ:      Rough low-budget educational doodle, a simple dog panting with its tongue out, flat muted tan-brown, bold thick wobbly outline, dot eyes, same crude doodle world. Plain white background. No text.
LINH DƯƠNG: Rough low-budget educational doodle, a simple antelope in flat muted tan-brown with slim legs, bold thick wobbly outline, dot eyes; include a tired/collapsing pose. Same crude doodle world. Plain white background. No text.
```

**KHÔNG cần cho Video #1 (để sau):** @FORAGER · @CHILD · @ELDER · @SCIENTIST (tùy chọn) · pose sheet (#4) · turnaround (#2).

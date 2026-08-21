# Bộ prompt NHÂN VẬT v3 — "NGƯỜI QUE THÔ" *(bám vibe đối thủ)*

> # 🔴🔴 XUNG ĐỘT NHÂN VẬT — ĐỌC TRƯỚC KHI GEN BẤT KỲ ẢNH NÀO *(phát hiện 09/08/2026)*
>
> Các prompt trong file này tả **một nhân vật KHÁC** với skill `sketchapiens-thumbnail` §⑥ *(gộp 09/08)*.
> Gen 191 ảnh video theo file này rồi làm thumbnail theo template kia → **CỬA 5a trượt**
> *("cắt mặt đặt cạnh mặt trong ảnh video: có cùng một nhân vật không?")*, và trượt lúc đó
> nghĩa là **gen lại cả bộ**.
>
> | | file này | `identity/style.py` *(file THẬT SỰ sinh ảnh)* + skill `sketchapiens-thumbnail` §⑥ *(gộp 09/08)* |
> |---|---|---|
> | **Mắt** | `tiny black dot eyes` | **HUGE** — vòng tròn trắng rộng bằng **1/3 đầu**, đồng tử đen to |
> | **Tóc** | `sparse messy **black** hair, a few loose strands` | **nâu vừa**, khối gai góc rối bù, đầu nhọn **chìa ra ngoài** viền đầu |
> | **Tay chân** | `bold thick… fat marker, NOT thin` | `THIN SINGLE BLACK LINES`, dài và gầy |
>
> ## ✅ THEO skill `sketchapiens-thumbnail` §⑥ *(gộp 09/08)* — nó đo trên **21 ảnh style đối thủ + 29 quả thắng**; file này viết theo cảm giác.
>
> Ba chỗ phải đổi trong MỌI prompt dưới đây trước khi dùng:
> ```
> tiny black dot eyes / small dot eyes
>   → HUGE round white eyes, each about one third as wide as the head, with a big
>     black pupil and two thin separate eyebrow lines above
>
> sparse messy black scribble hair (a few loose strands, not a thick cap)
>   → MEDIUM BROWN hair, a SHAGGY MANE of many fine wavy strands that frames the head
>     and hangs past it, wild and unbrushed, sitting BEHIND the head so the white face
>     stays readable. NEVER a spiky ball on top, NEVER radiating needles.
>
> bold thick single-stroke black arms and legs (fat marker, not thin)
>   → THIN SINGLE BLACK LINES for arms and legs, long and skinny with no joints,
>     ending in small white mitten hands and small white oval feet
> ```
> 🔴 **Chú ý chữ TÓC:** bản đầu của biển này *(dán 09/08, sửa ngay trong ngày)* ghi
> `SPIKY RAGGED… jagged pointed tips` — **sai**, vì NEG của `identity/style.py` chặn thẳng
> `no spiky hair ball`, `no fine radiating hair needles`. Đúng là **SHAGGY MANE sợi mảnh gợn sóng**.
>
> ⚠️ **Giữ nguyên:** thân/mặt **TRẮNG ĐẶC không tô da** · nét marker **run tay** · cố tình thô.
> ⛔ Và **đừng thêm luật cho thứ model đang vẽ đúng** — hai lỗi nặng nhất của 7 vòng V18 đều là
> luật tự thêm *(`clean/smooth` và `quét trắng cả tay chân`)*.


Sửa hướng theo feedback: **bỏ kiểu "designer xịn / mascot bóng bẩy / model sheet hoàn hảo".** Đối thủ vẽ **thô, đơn giản, low-budget** — người que trắng, nét marker nguệch ngoạc, tóc xù, mặt cực đơn giản. **Khung xương giữ Y HỆT, chỉ thay đồ.**

> ⚠️ Đừng dùng câu "Senior Principal Character Designer" nữa (nó kéo về bóng bẩy). Dùng framing **"rough low-budget educational doodle"**.

**KHUNG XƯƠNG (giữ giống mọi nhân vật):** người que tối giản — **nét tay/chân ĐẬM/DÀY (marker to, không mảnh)** · **thân + mặt TRẮNG** (không tô da) · nét marker đen **thô, hơi run** · **tóc đen ÍT nét** (vài sợi rối, KHÔNG thành mũ tóc dày) · **đầu hơi méo** · mặt **cực đơn giản** (mắt chấm/ô-van/nửa mắt, mày mảnh hoặc không, miệng 1 nét, không mũi) · **tay/chân oval hơi vụng**. **Tô màu CHỈ ở: đồ mặc + đạo cụ + nền.** Cố tình **thô, vụng, ngu-ngơ hài** (primitive/awkward/cheap), KHÔNG bóng bẩy/mascot. *(Mắt được mở to ở cảnh sốc/cận — nhưng mặc định đơn giản.)*

---

## 0) @BASEHUMAN — KHUNG XƯƠNG GỐC *(tạo TRƯỚC)*
```
Create a rough low-budget educational doodle animation frame. One simple primitive white stick-figure human standing on a plain white background. The character has a paper-white round head, slightly uneven and hand-drawn, with bold thick wobbly black marker outlines. Very simple face: tiny black dot eyes, one short single-line mouth, no nose, small thin eyebrows. Messy sparse black scribble hair, not too thick, not stylish. Body is extremely simple: bold thick single-stroke black arms and legs (fat marker, not thin), tiny oval white hands and feet, loose awkward proportions, slightly wobbly limbs, crude and funny, with a dumb, slightly tired / helpless expression. Keep the character looking cheap, primitive, and hand-drawn, like a low-budget educational explainer animation frame. Black outlines are imperfect, wobbly, and marker-like. No skin tone, no body fill, no polished mascot look, no clean vector look, no professional character sheet, no anime, no 3D, no gradients, no shadows, no texture, no labels, no text.
```
**Sheet thô (sau khi có base):**
```
The SAME simple white stick character in a rough hand-drawn model sheet: front, side, back, plus 4 simple expressions (curious, shocked with wide eyes, smug, cold & shivering). Keep it crude, hand-drawn and consistent — same character in every panel. White background.
```

---

## 1) @MODERNYOU — người hiện đại
```
Rough low-budget educational doodle, the SAME simple WHITE stick-figure human (paper-white body/face, NO skin tone, crude black marker line-art, sparse messy black hair (a few loose strands, not a thick cap), small dot eyes, no nose) — wearing a plain modern hoodie and pants in flat muted dusty denim blue (#5B86B0) and holding a small phone. Bold thick stick limbs, oval hands/feet. Crude and simple, not polished. White background. Flat color only on the clothes and phone.
```

## 2) @ANCESTOR — tổ tiên nam
```
Rough low-budget educational doodle, the SAME crude white stick figure (paper-white body/face, no skin tone, sparse messy black hair (a few loose strands, not a thick cap), simple dot eyes, no nose) — now with a scruffy beard, wearing a simple animal-fur loincloth (flat tan/brown), barefoot, holding a crude wooden spear. Crude black marker line-art, white body, color only on the fur and spear. White background.
```

## 3) @FORAGER — tổ tiên nữ
```
Rough low-budget educational doodle, the SAME crude white stick figure (paper-white body/face, no skin tone, no nose) — with longer messy scribbly hair tied back, wearing a simple plant-fiber wrap (flat tan/green), holding a woven basket. Simple dot eyes. Crude black marker line-art, white body, color only on wrap/basket. White background.
```

## 4) @CHILD — trẻ
```
Rough low-budget educational doodle, the SAME crude white stick figure but SMALL (child proportions, bigger head, short body), messy scribbly hair tuft, a tiny simple fur wrap. Paper-white body, no skin tone, simple dot eyes, no nose. Crude black marker line-art. White background.
```

## 5) @ELDER — già làng
```
Rough low-budget educational doodle, the SAME crude white stick figure — with messy GREY scribbly hair and a grey beard, slightly hunched, a simple fur wrap, leaning on a crude wooden staff. Paper-white body, no skin tone, simple dot eyes, no nose. Crude black marker line-art, color only on staff/wrap. White background.
```

## 6) ⛔ ~~@SCIENTIST — người giải thích~~ — **BỎ 09/08**
*(persona người dẫn **0 ca thắng / 16 kênh**, BrightPsycho 0/96; và hệ `@token` đã bỏ theo `D-04`)*
```
Rough low-budget educational doodle, the SAME crude white stick figure — wearing a simple white lab coat and plain round glasses, holding a clipboard. Paper-white body, no skin tone, messy scribbly hair, simple dot eyes, no nose. Crude black marker line-art, minimal color. White background.
```

---

## 7) @CHIMP / con vật *(TÔ MÀU — điểm nhấn màu)*
```
Rough low-budget educational doodle, a simple chimpanzee covered in flat brown, crude black marker outline, simple face with dot eyes, same crude doodle world as the stick humans. White background.
```
**Mẫu con vật khác:** thay `[con vật]` + `[màu phẳng]` (sói xám, sư tử vàng, hổ cam-vằn…), giữ "crude black marker, simple, same doodle world".

---

## Quy trình
1. Tạo **@BASEHUMAN thô** (front) → chọn bản "thô mà đúng vibe".
2. **Đính base** → "mặc đồ" thành từng costume (giữ **khung xương + mặt** y hệt).
3. Lưu `refs/<token>.png`. ⛔ *(registry `CastBible` đã xoá 09/08 — khối nhân vật chuẩn nay ở `identity/style.py`: `ANCIENT` · `MODERN` · `WOMAN` · `GROUP`.)*
> Con vật tô màu đủ; người thì chỉ đồ mặc + đạo cụ có màu, thân trắng.

---

## 9) BỘ ASSET TƯ THẾ / HÀNH ĐỘNG — *tạo 1 LẦN, dùng MỌI video* 🔑
*(mảnh quan trọng nhất để vừa nhất quán vừa nhanh: khỏi prompt lại từ đầu mỗi cảnh)*

Tạo sẵn `@BASEHUMAN` ở nhiều **tư thế**, lưu lại → video nào cũng dùng, chỉ **mặc đồ** (costume) + đổi **bối cảnh**.

**Danh sách tư thế cần có** (mỗi cái 1 ảnh, nền trắng, **đính base** để giữ khung):
đứng (front / side / back) · ngồi · nằm/ngủ · chạy · đi · chỉ tay · giơ 2 tay · cầm đồ · sợ hãi · hét/sốc · suy nghĩ (tay cằm) · run lạnh.

**Prompt mỗi pose:**
```
Rough low-budget educational doodle, the SAME crude white stick figure, now [TƯ THẾ], paper-white body, wobbly black marker outline, sparse messy hair, tiny dot eyes, no nose, plain white background. Crude and funny, not polished.
```
Lưu `refs/pose_<tư thế>.png`. → Dựng cảnh = lấy đúng **pose** + **costume** + đặt vào **bối cảnh**.

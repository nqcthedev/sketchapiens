# 🧩 Part 2 — SOP GIỮ NHẤT QUÁN NHÂN VẬT *(Nano Banana / Google Flow)*

> **Mục tiêu:** 1 nhân vật ra **hàng trăm ảnh** mà vẫn **cùng một gương mặt**. Đây là khâu khó nhất của kiểu slideshow — và là moat kỹ thuật của ta.
> Quy trình dưới đây **đã kiểm chứng**: bạn vừa làm `@BASEHUMAN` → `@MODERNYOU` ra sheet đủ góc + 4 biểu cảm, cùng 1 mặt. Giờ nhân rộng cho cả dàn.

---

## 🔑 Quy trình 5 bước
1. **HERO** — tạo `@BASEHUMAN`: 1 ảnh **chính diện sạch**, nền trắng, mặt trung tính. *(Đầu tư kỹ — nó định hình mọi ảnh sau.)* ✅ xong.
2. **REFERENCE SHEET / "mặc đồ"** — **đính ảnh base** → dán prompt costume (trong `../2_nguyenlieu/Prompts_NhanVat_Kenh.md`) → ra **sheet 1 ảnh** gồm: thân trước/nghiêng/sau + đầu turnaround + **4 biểu cảm**. *(Chính là cách ra `@MODERNYOU`.)* Đây vừa là **model sheet** vừa là **expression sheet**.
3. **LƯU** — mỗi nhân vật lưu `refs/<token>.png`; trong Flow **lưu làm "Ingredient"** (để tự bám vào mọi ảnh/clip của project).
4. **SINH CẢNH** — mỗi ảnh cảnh đính **2 thứ**: (a) **ref nhân vật** + (b) **frame trước đó** (giữ continuity màu/ánh sáng/thế giới) → chỉ tả **hành động/bối cảnh mới**.
5. **LỆCH thì BRANCH, đừng CHAIN** — nếu 1 ảnh ra sai khuôn → **sinh lại từ ref gốc**, KHÔNG sửa-chồng-lên-ảnh-đã-sửa (chain làm trôi mặt dần).

---

## ✍️ Quy tắc vàng khi viết prompt cảnh
- **Đính ref nhân vật MỌI lần**; gọi rõ *"the character from Image 1"* (đánh số Image 1/2 nếu nhiều ảnh).
- **Style block dán y nguyên** ở CUỐI mỗi prompt. Style giống nhau = ảnh giống nhau.
  > ⛔ **Ví dụ cũ ở đây chứa chữ CẤM.** Nó ghi *"hand-drawn 2D doodle **cartoon**, emotive chibi…"* —
  > `cartoon` là một trong **ba chữ cấm tuyệt đối** *(`cartoon · clean · smooth`)*, và bốn bản
  > thumbnail V18 đầu hỏng đúng vì prompt mở bằng ba chữ đó.
  > **Style block đúng** *(chép từ skill `sketchapiens-thumbnail` §⑥ *(gộp 09/08)*)*:
  > ```
  > Crude hand-drawn 2D stickman explainer, raw imperfect indie doodle art style,
  > VERY THICK and slightly shaky black marker outlines, flat solid colours with a
  > grainy paper and sketch texture overlay. NO smooth digital lines, NO clean
  > vectors, NO gradients, NO 3D shading. Colours dusty and muted.
  > ```
- **Trait token y chang từng chữ**: *"large round white eyes with small dot pupils"*, *"cobalt hoodie"*… Đừng đổi cách gọi (lúc "blue", lúc "navy" → trôi).
- **Nói rõ cái GIỮ NGUYÊN**: *"keep face, outfit, proportions identical; change only the background to a snowy plain."*
- **Dùng câu khẳng định thay vì phủ định** (Nano Banana nghe instruction, ít nghe "negative"): viết *"one relaxed visible hand"* thay vì *"no extra fingers"*; *"empty cave"* thay vì *"no people"*.
- **≤ 4–5 nhân vật / 1 ảnh** (đông hơn → mặt dính vào nhau). Cảnh đông thì để bớt người làm nền.
- **Số ref đính: 4–6 ảnh là ngọt nhất**; quá 7 ảnh model lại "trộn" → loạn.
- **Tỉ lệ: 16:9** cho video dài (9:16 cho Shorts).

---

## 😀 Thư viện biểu cảm *(tái dùng — rất quan trọng cho 150–300 ảnh)*
Từ sheet, **cắt riêng từng biểu cảm** (curious / shocked / smirk / cold / thinking…) lưu thành ảnh riêng. Cảnh nào cần cảm xúc gì → đính đúng ảnh biểu cảm đó → nhanh hơn & đúng khuôn hơn là tả lại bằng chữ.
→ **Shocked (mắt to + miệng há + vạch động)** là biểu cảm "vàng" — dùng cho hook và thumbnail.

---

## 🛠️ Lỗi hay gặp → cách sửa
| Lỗi | Nguyên nhân | Sửa |
|---|---|---|
| Trôi mặt qua chuỗi ảnh | sửa-chồng-ảnh nhiều lần | **branch** từ sheet, đừng chain |
| Mặt đổi giữa các cảnh | tả mơ hồ / không đính ref | đính sheet + **trait token y chang** |
| Thừa/dính ngón tay | tay che/ phức tạp | để **1 bàn tay lộ, thả lỏng**; doodle để tay oval đơn giản |
| Style lung tung (nét/màu lệch) | thiếu style block / không đính frame trước | dán **style block giống nhau** + đính **frame trước** làm Image 2 |
| Bắt nhầm nhân vật | nhiều người trong input | đánh số Image 1/2 + *"the X from Image 1"* |
| 5+ nhân vật mặt dính nhau | quá tải | giới hạn ≤5; người thừa vẽ thành nền |

---

## ⚡ Năng suất (150–300 ảnh/video)
- **Flow Ingredient** để tự bám nhân vật; hoặc API chạy **5–10 lệnh song song**.
- Chạy lô ở **1K + chế độ nhẹ**, chỉ **upscale ảnh giữ lại**.
- **Lưu prompt kèm ảnh** (đặt tên/ghi chú) để tái lập, không mất prompt.
- Cần nhiều biến thể nhanh: prompt **lưới 2×2** → 4 ảnh/lệnh.

---

## ✅ Checklist chốt 1 nhân vật
- [ ] Sheet ra đủ góc + **4 biểu cảm**, **cùng 1 mặt**.
- [ ] Lưu `refs/<token>.png` + tạo **Ingredient** trong Flow.
- [ ] ⛔ ~~Đánh ✅ trong registry `CastBible`~~ — **file đã xoá 09/08**. Khối nhân vật chuẩn nay ở **`identity/style.py`**.
- [ ] (tùy) cắt thư viện biểu cảm để tái dùng.

---

## 📚 Nguồn
- Google — Generating Consistent Imagery with Gemini (build sheet → cascade scenes): https://towardsdatascience.com/generating-consistent-imagery-with-gemini/
- Google Cloud — Ultimate Nano Banana Prompting Guide: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana
- Google Flow Help — Ingredients (nhân vật nhất quán): https://support.google.com/flow/answer/16353334
- Prompting.systems — Nano Banana character consistency (số ref, trait-lock, multi-character): https://prompting.systems/blog/nano-banana-pro-character-consistency-guide

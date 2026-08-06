# BÀN GIAO DỰ ÁN — Kênh "Người Que Cổ Đại" / Sketchapiens
> Dán nguyên file này vào session mới để tiếp tục không đứt mạch.

## 1. Dự án
Kênh YouTube **faceless, hoạt hình người que (doodle stickman)**, tiếng ANH, ngách
**"Ancient Humans Explained"** (giải thích con người cổ đại, kiểu tài liệu pha hài).
Đối thủ mẫu: **Mack / Stickly** (triệu view, mới ~1 tháng). Chủ kênh: nqcthedev.
**Video #1 = "Why Did Humans Lose Their Fur?"** (~18–20 phút).

## 2. Nguyên tắc cốt lõi (đọc trước khi làm gì)
- **Học đối thủ, rồi vượt:** copy y CÁI HAY đã proven (style, nhịp, cách text); chỉ
  cải tiến như CỘNG THÊM; KHÔNG copy cái dở của nó; KHÔNG bịa "đường mới" chưa kiểm chứng.
- **Chủ đọc tiếng Việt** (không rành tiếng Anh) → luôn gloss tiếng Việt cạnh mọi text
  tiếng Anh trong chat. NHƯNG file kịch bản đọc để THUẦN TIẾNG ANH, 1 câu/dòng.
- **Chốt đích trước khi build** (dùng lâu dài, không làm demo rồi đập đi).
- Hỏi (how/where/why) → trả lời gọn; chỉ làm/build khi chủ nói "làm/sửa/build/gửi".
- Chủ có **Google AI Ultra** (gen ảnh Nano Banana Pro thoải mái, không lo credit).

## 3. Trạng thái Video #1
- **Kịch bản: XONG.** `Script_Video01_FINAL.txt` (EN, 354 dòng lời-đọc, 1 câu/dòng)
  và `Script_Video01_FINAL_deAI.txt` (đã chạy skill chống-văn-AI: thêm contractions,
  bỏ intensifier rỗng; GIỮ y nghĩa/số dòng/timing). **Dùng bản deAI để thu TTS.**
- **Prompt ảnh: XONG.** `IMG_PROMPTS_UPLOAD.txt` (294 dòng, mỗi dòng 1 ảnh) sinh bởi
  `gen_prompts2.py` (ở outputs). Đang test gen.
- **Giọng đọc:** ElevenLabs **"Josh - Teacher for Kids"**, voice_id
  `nzFihrBIvB34imQBuxub` (multilingual_v2; stability .45 / similarity .80 / style .20).
- **Còn thiếu:** thumbnail + metadata (tiêu đề/mô tả/tag/chapters) — CHƯA làm.

## 4. Style ảnh + Cast (đã chốt)
**Cast:** chủ dùng lại **3 SHEET GỐC** của mình: caveman (áo da nâu, TÓC ĐEN) ·
modern (HOODIE XANH + quần jeans xanh, tóc đen) · bộ tiền sử (phụ nữ / ông già tóc-râu
xám / trẻ em). **Chimp KHÔNG có trong 3 sheet** → cần gen 1 ref @CHIMP riêng.
- refKeys dùng: `@MODERNYOU`, `@ANCESTOR`, `@CHIMP` (Video #1 chỉ 3 cái này).
- `CAST_REGEN_PROMPTS.txt` = bản cast "big-head/nét đậm/hoodie ĐỎ/1-pose" mình từng dựng
  để làm mascot riêng — HIỆN ĐỂ DÀNH (chủ đã quay lại sheet gốc).

**Prompt ảnh (gen_prompts2.py) đã cài:** doodle nét đen ĐẬM sạch (không vector/nguệch),
màu phẳng, nền trắng, **đỏ chỉ điểm xuyết**, nhân vật VẼ TO giữa khung, thẻ nhận dạng
cố định mỗi nhân vật (tuổi/đồ/tóc), biểu cảm để prompt tự gen (deadpan/sốc/lo+mồ hôi/
khó hiểu+"?"/cười), **chống chép ref** (chỉ 1 nhân vật, no model sheet/no collage), và
**đã lọc từ dễ dính chính sách** (naked/bare/hairless → "fur-free", bare feet → no shoes).

## 5. Công cụ đã build (đều trong thư mục dự án)
- **`SketchapiensImageTool/App.tsx`** — tool sinh ảnh hàng loạt chạy TRONG Google Flow
  (dùng flow-sdk): smart ref binding theo @tag, grid, tự chạy tiếp, tự lưu, retry, tải
  tất cả. Dán vào trình sửa code của Flow. (API: `Flow.media.selectMultiple`,
  `Flow.generate.image({prompt, referenceImageMediaIds, modelDisplayName, aspectRatio})`,
  `Flow.download`.) Chưa test thật trong Flow.
- **`GhepVideo_Studio_NextJS/`** — app ghép ảnh+audio→video (Next.js, chạy `npm run dev`
  hoặc `start.command`), engine **Mediabunny (WebCodecs→MP4 4K)** + fallback MediaRecorder,
  có zoom/pan Ken Burns. `GhepVideo_Studio_App.html` = bản 1-file offline.
- **`chong-van-ai-narration-en.skill`** — skill chống-văn-AI cho narration tiếng Anh (đã cài).
- **`SPEC_Tool_SinhAnh_Flow.md`** — spec để tự dựng tool sinh ảnh trong Flow Tool Creator (nếu cần).

## 6. Việc TIẾP THEO (thứ tự)
1. Gen 3 ref cast (@MODERNYOU, @ANCESTOR, @CHIMP) + 1 ảnh `style`, đặt ingredient đúng tên.
2. Test gen vài ảnh từ `IMG_PROMPTS_UPLOAD.txt` → kiểm: hết chép-ref chưa, biểu cảm ổn
   chưa, kích thước đều chưa, có bị chính sách không.
3. Gen đủ 294 ảnh (đặt tên 001…294).
4. Thu TTS (giọng Josh) từ `Script_Video01_FINAL_deAI.txt`.
5. Ghép ảnh + audio bằng tool (thêm zoom/pan, xuất 4K).
6. Làm **thumbnail** + **metadata** (chưa có) → đăng.

## 7. Lỗi hay gặp + cách xử
- **Vi phạm chính sách khi gen:** bộ lọc xác suất; đã thay từ nhạy cảm. Nếu 1 ảnh cứ bị
  chặn → lấy SỐ IMG + câu prompt đó sửa trúng. Cảnh đe-doạ/em bé/khỏa-thân là hay dính nhất.
- **Ảnh ra kèm cả tấm ref (chép sheet):** vì ref là sheet nhiều tư thế → dùng ref 1 POSE
  ĐƠN, hoặc dựa vào negatives "no model sheet" trong prompt.
- **Nhân vật đổi kích thước (size-drift):** kỹ thuật "scale lock / camera grammar" (bài
  của Vienhn trên FB): chốt 1 SHOT TYPE cố định mỗi phân đoạn (medium full-body…). Có thể
  thêm vào generator nếu cần.

## 8. Neo khoa học Video #1 (giữ nguyên số liệu)
Nina Jablonski (làm mát/đổ mồ hôi) · Alan Rogers + gene MC1R (~1.2 triệu năm) · Pagel &
Bodmer (ký sinh) · Mark Stoneking (chấy quần áo ~170.000 năm) · Darwin (chọn lọc giới
tính) · "vượn nước" = giả thuyết SAI (đã bác). ~5 triệu nang lông = ngang tinh tinh. Lanugo
= lông bào thai.

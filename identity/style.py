# -*- coding: utf-8 -*-
"""BẢN SẮC HÌNH ẢNH CỦA KÊNH — MỘT nguồn duy nhất cho MỌI video.

VÌ SAO CÓ FILE NÀY
──────────────────
Trước 08/08/2026, các khối STYLE / CONSIST / NEG nằm trong `build_prompts.py` của
TỪNG video. Đo ngày 08/08: chúng đã trôi thành BA bản khác nhau —

    STYLE_CARD    V17  9.563 ký tự  ·  V18 12.232  ·  V19 12.644
    STYLE_SCENE   V17 10.326        ·  V18 12.922  ·  V19 13.334
    NEG_CARD      V17  5.140        ·  V18  5.944  ·  V19  6.356

Tức ba video được gen bằng BA định nghĩa style khác nhau, và không ai quyết định
điều đó — nó xảy ra vì chép file rồi sửa dần. Với kênh faceless thì NHẤT QUÁN HÌNH
ẢNH là tài sản lớn nhất.

⛔ SỬA FILE NÀY LÀ ĐỔI BẢN SẮC CỦA CẢ KÊNH. Không sửa cho riêng một video.
   Muốn một video khác đi thì đổi `subj`/`text` trong shot_data.py của video đó.

SỬA 10/08/2026 — sau khi mổ 102 thumbnail của 13 kênh cùng ngách:
  · TÓC MỞ KHOÁ  → hằng số `HAIR` + `HAIR_NEG`, đổi MỘT LẦN mỗi video rồi để yên.
    Lý do: tóc có mặt ở CẢ hai phía thắng-chìm nên không đo được gì; Axen KHÔNG TÓC
    được 32.481 view/ngày, cao nhất trong bộ.
  · KHUÔN MẶT   → `FACE_BUILD`, trường phái Mack · Stickly · Neon Rush do chủ chọn.
    Đầu MÉO (không tròn compa) · mắt BẦU DỤC ĐỨNG · có MÍ TRÊN · con ngươi LỆCH TÂM
    nhìn vào cảnh chứ không nhìn ống kính · miệng LỆCH một bên · nét viền dày mảnh
    không đều · tư thế bất đối xứng.
  · ⚠️ SỬA MỘT LỖI CŨ: dict `FACE` ghi "two dot eyes" ở 8/10 mục, tức mỗi shot đều
    dán một câu ĐÈ NGƯỢC lại CHARACTER LOCK ("never tiny dots"). Nay cả 10 mục nói
    bằng ngôn ngữ mí mắt + hướng con ngươi, khớp với khối nhân vật.
  · KHÔNG đụng tới STYLE_SCENE / STYLE_CARD / BG / framing — đó là cách vẽ CẢNH,
    thuộc quyết định khác.

Bản này lấy từ V19 (mới nhất, đã qua các sửa 30/07 và 07-08/08).
V17 và V18 giữ bản riêng của chúng làm HIỆN VẬT — prompt phải khớp thứ đã thật sự
dùng để gen ảnh, không được sửa lại lịch sử.
"""

# ⚠️ CHỈ DÙNG CHO THUMBNAIL. Đo 10/08 trên khung video thật của Mack và Stickly:
#    bão hoà trung vị VIDEO 30,2% (90% dưới 53-71%) — CAO HƠN thumbnail (23-27%).
#    Khung video CẦN màu rực để làm ký hiệu: dấu ✗ ĐỎ, dấu ✓ XANH, lửa cam.
#    Áp trần này cho video là bóp chết chính bộ ký hiệu đó.
# 🔴 BÁC 12/08/2026 — đo 23 QUẢ NỔ THẬT của ngách (250K-7,8 triệu view, tải bản 1280px):
#    bão hoà trung vị **36,1%**, dải 0-64%. Tức quả nổ KHÔNG hề nhạt màu.
#    Con số "thumbnail 23-27%" của bản 10/08 đo trên tập gồm cả kênh trung vị 1 vpd,
#    nên nó đo "màu của kênh yếu", không phải "màu của quả nổ".
#    Và thumbnail của ta đo được **38,6%** — tức đang ngang quả nổ, KHÔNG cần hạ.
#    ⛔ Ép desaturate là kéo ngược. Giữ tên hằng số cho khỏi vỡ chỗ gọi, đổi nội dung.
SAT_CEILING = ("Colours are rich and saturated like poster paint straight from the pot, warm and "
               "earthy rather than neon: firelight orange, clay brown, dry-grass tan, deep night "
               "blue. Nothing is washed out or greyed down, and nothing is candy pink or pure cyan. ")

# ── STYLE LOCK — 🔴 THÊM 11/08/2026 ──────────────────────────────────────
# Vì sao: quy trình cũ neo nét vẽ bằng ẢNH THAM CHIẾU trong Google Flow
# (videos/Video18_Sleep/_cu/PROMPT_NGAN_dung_kem_anh_ref.txt: "để Flow học nét vẽ từ
# ẢNH, không phải từ chữ"). Chủ đã bỏ phần đó trong Flow, nên thứ ảnh ref từng gánh
# nay phải nằm trong chữ, nếu không model rơi về mặc định của nó: vector sạch, tô
# đều tăm tắp, bóng số.
# ⚠️ KHỐI NÀY CHỈ NÓI CÁCH VẼ. Không thêm một luật nội dung nào — bài học V18: hai
#    lỗi nặng nhất đều là luật tự thêm. Và tuyệt đối không dùng ba chữ cartoon /
#    clean / smooth: khung 4K của đối thủ cho thấy nét RUN TAY, không phải nét sạch.
# Đặt ở ĐẦU prompt (trọng số cao nhất), trước cả khối nhân vật.
STYLE_LOCK = (
    "Rough hand-drawn marker doodle, drawn fast by one hand: lines WOBBLE and vary in thickness, "
    "circles are out of round, colour is FLAT and SOLID and fills slightly off the lines. "
    "Low finish on purpose. No vector art, no gradients, no glow, no blur, no 3D, no glossy "
    "surfaces, never computer-perfect. ")
STYLE_SCENE = (
    "Flat 2D explainer frame, solid black wobbly outlines. The environment is FLAT BLOCKS OF "
    "COLOUR with very low detail: only what the SCENE line names, nothing layered, no texture. "
    "Stars are plain white dots. Fire is a wobbly orange shape with a yellow centre. 16:9. ")
# Thẻ: phẳng, trắng, chữ tay. Đây là chỗ DUY NHẤT được phẳng.
STYLE_CARD = (
    "Hand-drawn explainer CARD on a plain WHITE background, same black ink outline as the series. "
    "Flat hand-drawn shapes, hand-lettered marker text, generous empty space. 16:9. ")
# ── TÓC — 🔓 MỞ KHOÁ 10/08/2026 (chủ chốt: "tóc có thể tự do sáng tạo") ────
# Bằng chứng: mổ 102 thumbnail/13 kênh — tóc xuất hiện ở CẢ hai phía thắng-chìm
# nên không đo được gì. Bờm viền (Mack) thắng · mảng trùm (NeonRush) thắng ·
# sợi rủ trước mặt (Stickly) thắng · KHÔNG TÓC (Axen) thắng cao nhất 32.481 vpd.
#
# ⚠️ TỰ DO GIỮA CÁC VIDEO — KHOÁ TRONG CÙNG MỘT VIDEO.
#    Đổi HAIR + HAIR_NEG ở đây một lần cho mỗi video, rồi để yên.
#    Đổi giữa chừng = drift = đúng lỗi file này sinh ra để chặn.
# 🔴 HẠ VỀ LANE KHUNG VIDEO 11/08/2026 — chủ bắt được: bản trước là khối đúc cho
#    THUMBNAIL (bờm nhiều sợi trùm hai bên mặt như mũ trùm) mà lại chạy cho cả 202
#    khung video. Khung video của Mack · Stickly là NGƯỜI QUE ĐƠN GIẢN; chi tiết cao
#    chỉ dành cho thumbnail, và chỗ để đổ chi tiết là VẬT KỂ CHUYỆN, không phải người.
HAIR = ("MEDIUM BROWN, a SMALL messy tuft of a few separate wavy strands sitting ON TOP of "
        "the head with ragged pointed ends; it does NOT hang down over the sides of the face "
        "and does NOT frame the face like a hood; the white circle of the face stays fully "
        "visible and mostly bare")
HAIR_NEG = ("no hedgehog hair, no spiky hair ball on top of the head, no fine radiating hair needles, "
            "no smooth bob, no long hair hanging past the jaw, no mane framing the face, "
            "no hair covering both sides of the head, ")

# Tóc LUÔN vẽ theo cách này, dù chọn kiểu gì — đây là kỹ thuật, không phải kiểu.
HAIR_HOW = ("The hair is always drawn as SEPARATE LOOSE STRANDS rather than one solid block, and it "
            "REACTS to the weather in this shot instead of sitting still. ")

# ── KHUÔN MẶT — trường phái MACK · STICKLY · NEON RUSH (chốt 10/08/2026) ───
# Chín đặc điểm mổ ở 1280px. Thứ đắt nhất là (3): con ngươi LỆCH TÂM.
# 🔴 HẠ VỀ LANE KHUNG VIDEO 11/08/2026 — cùng lý do với HAIR ở trên. Bản trước tả mặt
#    ở độ chi tiết của một khung CẬN thumbnail (oval lệch, cằm thon, viền dày mỏng đổi
#    theo chỗ, mắt oval TO). Giữ lại đúng ba thứ đã kiểm chứng: con ngươi LỆCH TÂM,
#    mắt KHÔNG nhìn ống kính, biểu cảm nằm ở LÔNG MÀY chứ không ở miệng.
FACE_BUILD = (
    "the head is ONE LARGE ROUND white circle with a slightly wobbly hand-drawn outline, "
    "never a compass-perfect circle; NO neck; "
    "eyes = two SMALL oval white eyes set well apart, each with a small black pupil sitting "
    "OFF-CENTRE so the character is clearly LOOKING AT SOMETHING IN THE SCENE and NEVER at the "
    "viewer; a short curved upper eyelid line over each eye; "
    "two thin curved eyebrows, INNER ends raised, carrying the emotion; one short mouth line OFF "
    "TO ONE SIDE, never centred; no nose, no ears; the whole face is made of FEW simple marks and "
    "is never rendered, shaded or detailed; ASYMMETRIC pose with one readable hand gesture. ")

# ── NHÂN VẬT (lặp Y NGUYÊN mọi lần xuất hiện) ─────────────────────────────
# 🔴 GỌN 12/08/2026 — Flow chặn prompt >4000 ký tự, và chủ chốt: CÀNG NGẮN MODEL CÀNG ĐÚNG.
# Một khối người dùng chung cho cảnh và thẻ, thay vì hai bản 1.824 + 1.696 ký tự.
NGUOI = (
    "Head = one large round SOLID WHITE circle, no neck. Eyes = two small white ovals, each with a "
    "small pupil pushed OFF-CENTRE so he looks at something in the scene, NEVER at the viewer. "
    "Thin eyebrows, inner ends raised, carry the emotion. Short mouth line off to one side. "
    "Hair = a small messy brown tuft on TOP of the head only, not hanging down the sides. "
    "One ragged brown hide tunic with a torn hem. Arms and legs = thin crooked black lines. "
    "Hands and feet small and SOLID WHITE like the head, never skin-coloured, barefoot. ")

ANCIENT = ("ONE person only, never two, never a second figure. " + NGUOI)
MODERN = (
    "ONE modern person: a plain round SOLID WHITE head with NO hair, a thin black stick body, "
    "a plain t-shirt and trousers, small white mitten hands and white oval feet. ")
WOMAN = (
    "ONE woman, drawn to the same fixed rules: " + NGUOI +
    "Her hair is the same brown but longer, falling past the shoulders. ")
GROUP = (
    "A SMALL GROUP of two to four people, each drawn to the same fixed rules: " + NGUOI +
    "Vary their heights and poses so they read as different people, but never change how they "
    "are drawn. ")
# ── NGƯỜI TRONG KHUNG THẺ — 🔴 VÁ 11/08/2026 ──────────────────────────────
# Trước: 126/202 khung CARD của V19 chỉ nhận câu mơ hồ "Any person shown is the same
# stickman with a LARGE round white head" — KHÔNG tóc, KHÔNG khố, KHÔNG quy cách mặt.
# Hậu quả: khung cảnh ra người cổ đại tóc nâu mặc khố, khung thẻ ra người que trắng
# trọc đầu. Hai nhân vật khác nhau đổi qua đổi lại suốt bài.
# Nay khung thẻ dùng ĐÚNG khối nhân vật, nhưng nói CÓ ĐIỀU KIỆN để không ép vẽ người
# vào những thẻ vốn chỉ có sơ đồ.
PERSON_IN_CARD = (
    "If this card needs no person, draw none. Any person that does appear follows these rules "
    "exactly: " + NGUOI)
# ── NEG ───────────────────────────────────────────────────────────────────
# Đã BỎ 'no country borders' và 'no inset panel': đo được là đối thủ CÓ dùng.
NEG_SCENE = (
    "NEG: no modern person, no bald head, no sweater or hoodie or trousers or shoes, no peach or "
    "tan skin, no realistic or blank face; no animal unless named above; no eyes looking at the "
    "viewer; no two heads on one body, no duplicate figure, no split screen, no collage; "
    "no photo, no 3D, no anime, no glossy render; no watermark, no border, no subtitle bar. 16:9. ")
NEG_CARD = (
    "NEG: no photo, no 3D, no stock clipart, no corporate infographic, no computer font, "
    "no gradient background, no solid black pictogram people; no modern person, no bald head, "
    "no sweater or trousers or shoes, no peach or tan skin; never write instruction words such as "
    "HAND-DRAWN, EXPLAINER, CARD, STYLE or OUTLINE in the picture, the only words allowed are the "
    "ones named in TEXT; no watermark, no border. 16:9. ")
# ── BẢNG MÀU — đo thật trên 12 quả thắng của Mack · Stickly · Neon Rush ───
# (chủ chốt 10/08: "màu bg phải giống 3 kênh đó")
#
#   BÃO HOÀ TRUNG VỊ   Mack 23% · Stickly 27% · Neon Rush 27%
#                      SKETCHAPIENS 37%, và 10% số điểm ảnh vượt 86%  ← chỗ lệch
#   SÁNG TRUNG VỊ      42-55%, cả bốn kênh bằng nhau → sáng KHÔNG phải chỗ lệch
#
# Nghĩa là: ta không sai ở độ sáng, ta sai ở CHỖ MÀU QUÁ RỰC. Vài quả có mảng
# cyan/đỏ gần bão hoà tối đa; ba kênh kia không có điểm nào như thế.
# ⚠️ ĐÂY LÀ HỌ MÀU + TRẦN BÃO HOÀ, KHÔNG PHẢI MÀU MẶC ĐỊNH CỦA VIDEO.
#    Không video nào "mặc định nâu" hay "mặc định đêm". CẢNH TRONG KỊCH BẢN quyết
#    dùng mã nào: mưa → rain_blue · đêm → night_blue · hang → brown · đồng cỏ → tan.
#    Thứ duy nhất áp cho MỌI video là SAT_CEILING ở trên.
# Màu xương sống, đo được (chiếm 15-29% khung ở quả thắng):
PALETTE = {
 "tan":        "#C4A870",   # đất khô, cỏ cháy — màu hay gặp nhất của cả ba kênh
 "brown":      "#8C7054",   # đất ẩm, da thú, thân cây
 "brown_dark": "#705438",   # bóng đổ, trong hang
 "olive":      "#707054",   # bụi cây, cỏ già
 "olive_dark": "#545438",   # tán lá tối
 "straw":      "#C4C470",   # cỏ vàng — chữ ký của Neon Rush
 "sky_pale":   "#C4E0FC",   # trời nhạt, chỉ dùng làm dải mỏng phía trên
 "rain_blue":  "#54708C",   # trời mưa (Mack RAIN AGAIN)
 "night_blue": "#54548C",   # đêm — vẫn XỈN, không phải navy rực
 "green_mute": "#70A854",   # cây cỏ, đã giảm bão hoà
}

# ── NỀN CẢNH ──────────────────────────────────────────────────────────────
# ⚠️ BẢNG MÀU là hằng số của kênh (học được). CHỌN entry nào cho shot nào thì
#    KỊCH BẢN quyết — không có tỉ lệ chuẩn, không có mặc định. Xem
#    kho/3_bangchung/THUMB_TEARDOWN_2026-08-10/KETLUAN.md và skill thumbnail
#    (bảng "cái gì học được / cái gì kịch bản quyết").
BG = {
 # ── NGÀY, ĐẤT KHÔ (thêm 10/08 — đúng bảng màu ba kênh) ──
  # ── CHẠNG VẠNG (mạch chính của V19-Moon) ──
 "dusk_grey":  ("one flat band of colourless pale grey sky low across the top, over a wide flat block of "
               "dim olive-brown ground " + PALETTE["olive"] + ", with a solid dark treeline as one flat "
               "shape along the horizon and no detail inside it"),
 "dusk_water": ("a flat strip of still dark water " + PALETTE["rain_blue"] + " along the bottom, a flat "
               "band of dim grey sky above, and a solid black treeline between them"),
 "moonlit":    ("a flat block of deep blue night sky with one plain white circle for a full moon, over "
               "flat pale grey-blue ground bright enough to see the shapes on it"),
 "savanna_day": ("one flat band of pale sky " + PALETTE["sky_pale"] + " across the top third, over a wide "
               "flat block of dry tan ground " + PALETTE["tan"] + ", with two or three muted olive "
               + PALETTE["olive"] + " shrubs and one distant hill in " + PALETTE["brown"]),
 "dry_plain":  ("a wide flat block of dry tan ground " + PALETTE["tan"] + " meeting a low horizon, with "
               "straw-yellow " + PALETTE["straw"] + " grass tufts drawn as a few loose V strokes"),
 "cave_warm":  ("flat blocks of warm brown " + PALETTE["brown"] + " cave wall with deeper "
               + PALETTE["brown_dark"] + " in the recesses, and one darker opening at one side"),
 "rain_day":   ("a flat block of grey-blue rain sky " + PALETTE["rain_blue"] + " over wet olive-brown "
               + PALETTE["olive"] + " ground with a few pale puddles"),
 # ── ĐÊM & LỬA (mạch chính của V19) ──
 "fire_ring":  ("one flat block of very dark navy filling most of the frame, and in the middle a small "
               "fire drawn as a wobbly orange shape with a yellow centre on a few grey stones, casting "
               "a soft round patch of warm orange on a flat strip of medium-brown ground"),
 "fire_edge":  ("a warm orange patch of firelight on flat brown ground on one side, and on the other "
               "side a flat block of almost-black navy with nothing drawn in it at all"),
 "night_open": ("a flat block of midnight-blue night sky with plain white dots for stars and a small "
               "white crescent moon, over one flat strip of medium-brown ground, and one tree drawn as "
               "a brown line with a dark green cloud on top"),
 "night_dark": "a flat block of almost-black dark navy filling the whole frame, with nothing else drawn in it",
 "cold_night": ("a flat block of cold blue-grey night sky with a few white star dots, over one flat "
               "strip of pale frosted grey-brown ground, and one bare tree drawn as a brown line with "
               "a few bare twigs"),
 # ── HARAMAYA (huyện hiện đại, ban đêm) ──
 "village_night": ("a flat block of dark navy night sky over one flat strip of dry tan ground, with two "
               "very simple square houses drawn in plain black lines, one small yellow window square, "
               "and a plain dirt path leading away into the dark"),
 # ── HIỆN ĐẠI (khách mời — chỉ hook và kết) ──
 "modern_night": ("a flat block of dark blue-grey bedroom wall, a simple bed drawn in a few black lines, "
               "and one plain rectangle for a doorway with a darker rectangle inside it"),
 "modern_hall": ("a flat block of dark blue-grey wall, one flat strip of pale grey floor, and a plain "
               "open doorway rectangle at one end"),
 # ── CƠ THỂ / KHÁI NIỆM ──
 "dark_card":  ("a flat block of very dark navy filling the entire frame with generous empty space; "
               "every line, shape and letter in this image is drawn in WHITE or pale cream marker on "
               "top of that dark navy, not in black"),
 "white":      "a plain WHITE background with generous empty space",
}

# ── THUMBNAIL — KHỐI RIÊNG, CỐ Ý KHÁC STYLE_SCENE ────────────────────────
# ⛔ ĐỪNG HỢP NHẤT VỚI STYLE_SCENE. Trích khung video thật của Mack và Stickly
#    ngày 10/08 cho thấy CÙNG MỘT KÊNH dùng HAI ngữ pháp hình khác hẳn nhau:
#
#      KHUNG VIDEO  →  nền TRẮNG hoặc MỘT mảng phẳng tuyệt đối · không chiều sâu ·
#                      không bóng đổ · không nguồn sáng · đầy đồ hoạ dạy học
#                      (bản đồ, mũi tên, thẻ chữ, timeline, dấu ✗ đỏ) · chữ khắp nơi
#      THUMBNAIL    →  có LỚP · có NGUỒN SÁNG thật · có bóng đổ · có vignette ·
#                      chi tiết KHÔNG ĐỀU (một vật vẽ kỹ, người vẽ trơn)
#
#    Nên STYLE_SCENE giữ nguyên "flat, no depth, no shadows" — nó ĐÚNG, và nó
#    khớp đúng thứ Mack/Stickly làm trong video. Chỉ thumbnail mới được dựng lớp.
STYLE_THUMB = (
    "A hand-drawn 2D thumbnail illustration in the same black marker line as the series, but "
    "rendered with DEPTH, unlike the flat frames inside the video: build the scene in three "
    "layers (a dark foreground edge, the subject in the middle, a lighter distance behind), "
    "lit by ONE visible light source inside the frame (a campfire, a low sun) so surfaces "
    "facing it are warm and bright and everything turned away falls into cooler shade, with "
    "soft cast shadows on the ground and a slight darkening at the four corners. "
    "ONE object in the frame is drawn with FAR more detail than everything else — fine texture, "
    "individual hairs or grain, its own highlight — while the people stay plain and untextured, "
    "so the eye lands on that object first. "
    "Put a cool blue-grey area (rain, night sky, a cave mouth) somewhere in the SAME scene so "
    "warm and cold sit side by side; this is NOT a split screen, it is one continuous place. "
    "Small storytelling props scattered along the bottom edge. " + SAT_CEILING + "16:9. ")

THUMB_TEXT = (
    "Large hand-lettered ALL-CAPS marker text across the TOP of the frame, filling most of the "
    "width and about a fifth of the height, with a thick black outline: BRIGHT YELLOW when the "
    "area behind it is warm, WHITE when the area behind it is sky or grey. ")

THUMB_NEG = ("NEG: no modern people, no modern objects of any kind (no bed, no phone, no shoes, "
             "no toothbrush, no glasses, no camera, no cup), no split screen, no side-by-side "
             "comparison, no before-and-after layout, no photographic elements, no real photos, "
             "no animal alone without a person, no Roman or Greek or gunpowder-era setting, "
             "no skulls, no gore. ")

# ── KHUNG HÌNH ────────────────────────────────────────────────────────────
def framing(kind, subj, thuan=False):
    s = subj.lower()
    # 🔴 VÁ 12/08/2026 — ĐỌC prompt 002 mới thấy: khung cảnh thuần vừa ghi "THIS FRAME HAS
    # NO PEOPLE IN IT" thì ngay sau đó framing lại bảo "the figure large and roughly centred
    # ... around HIM". Prompt TỰ CÃI NHAU, và model có cớ để vẽ người ra.
    # grep không bao giờ bắt được lỗi này vì cả hai vế đều "đúng" khi đứng riêng.
    if thuan:
        if any(k in s for k in ("wide","landscape","open ground","empty")):
            return ("Framing: a WIDE establishing shot of the empty place itself, plenty of open "
                    "ground and sky, no figure anywhere in it. ")
        if any(k in s for k in ("close","large","drawn large")):
            return ("Framing: a tight CLOSE-UP on the object named above, filling most of the "
                    "frame, no figure anywhere in it. ")
        return ("Framing: a MEDIUM WIDE shot of the place itself with the horizon low in the "
                "frame, the scene readable and empty of people. ")
    if kind.startswith("SCENE") or kind == "GROUP":
        if any(k in s for k in ("wide","camp","seen small","at a distance","whole band","landscape")):
            return ("Framing: a WIDE establishing shot, the figures fairly small inside a large "
                    "environment, plenty of world visible around them. ")
        if any(k in s for k in ("close","his own hand","holding one hand","face fills")):
            return "Framing: a tight CLOSE-UP, the subject filling most of the frame. "
        if any(k in s for k in ("sitting","kneeling","lying","crouch","seated")):
            return ("Framing: a MEDIUM shot from slightly above, the figure large in frame with the "
                    "ground and surroundings clearly visible. ")
        return ("Framing: a MEDIUM shot, the figure large and roughly centred, with the environment "
                "readable behind and around him. ")
    if "map" in s:
        return "Framing: the map centred and LARGE, filling most of the frame. "
    if any(k in s for k in ("cross-section","timeline","chart","diagram")):
        return "Framing: the diagram centred and LARGE, drawn nearly edge to edge. "
    if "row of" in s or "in a row" in s:
        return "Framing: the items in ONE straight horizontal row across the middle, evenly spaced. "
    if "title card" in s or "text filling" in s or "headline" in s:
        return "Framing: the lettering fills most of the frame. "
    return "Framing: one subject centred and drawn LARGE, generous empty white space around it. "

LETTER = ("All lettering is IRREGULAR HAND-LETTERED marker writing, each letter drawn by hand and "
          "slightly uneven, NOT a computer font. Spell it EXACTLY as written above, no extra words, "
          "no gibberish letters. ")

SAME_HAND = ("Every object, icon and diagram shape is drawn BY HAND in the same black ink "
             "outline as the rest of the series, never a pictogram. ")
# ── BIEU CAM (deadpan la mac dinh; suc bieu cam nam o MAT) ───────────────
# Moi shot PHAI chon mot cai. Khong co "trung tinh".
FACE = {
 "flat":   "FACE: eyelids level across the top of the eyes, pupils looking slightly to one side, eyebrows level, mouth one short straight line set off to one side. ",
 "shock":  "FACE: eyelids lifted clear of the eyes so both eyes are wide, pupils small and pushed to one side, eyebrows shot up, mouth a small open circle off centre. ",
 "tired":  "FACE: heavy upper eyelids covering nearly HALF of each eye, pupils looking DOWN, a faint pink smudge under each eye, eyebrows sloping down, mouth one short straight line. ",
 "worry":  "FACE: upper eyelids covering the top third of the eyes, pupils looking off to one side, eyebrows tilted up at the INNER ends, mouth a small downward curve set off to one side. ",
 "scared": "FACE: eyelids lifted so both eyes are wide, pupils tiny and pushed to one side away from the danger, eyebrows high and tilted up at the inner ends, mouth a small open circle, one short sweat line beside the head. ",
 "happy":  "FACE: eyes closed as two upward curved lines, eyebrows relaxed, mouth an upward curve set off to one side. ",
 "asleep": "FACE: eyes closed as two short downward curved lines, eyebrows relaxed, mouth one small line off centre. ",
 "dumb":   "FACE: upper eyelids half closed, pupils drifting apart to opposite sides, eyebrows level, mouth one flat line, head tilted slightly. ",
 "curious":"FACE: eyelids level, pupils pushed hard to ONE side as if glancing at something off to the edge, one eyebrow higher than the other, mouth a small circle off centre. ",
 "sad":    "FACE: upper eyelids drooping, pupils looking DOWN, eyebrows tilted up at the INNER ends, mouth a downward curve set off to one side. ",
}

# 🔴 VÁ 12/08 chiều — LỖ HỔNG lô 3: khung cảnh CÓ con vật thì không dán NO_PERSON
# (vì có con vật) mà cũng không dán khối nhân vật → prompt KHÔNG có một dòng nào về
# người, và khung 098 lọt ra một anh hiện đại áo thun quần short. Bịt nốt nửa còn lại.
# Kèm KHOÁ MÀU SƯ TỬ: sư tử xuất hiện ~15 lần mà chỉ có câu chung "flat solid colour",
# nên mỗi khung một màu — nâu nhạt, cam đậm, vàng. Đó là drift khán giả thấy được.
ANIMAL = ("Any animal here is drawn with MORE detail and body volume than the stick people, "
          "filled with FLAT SOLID colour and a black outline, with a small simple face. "
          "A LION is always the SAME sandy tan-gold #C4A870 with a slightly darker brown mane, "
          "never orange, never bright yellow, never pale grey-brown. "
          "A SNAKE is always the SAME dull olive green, never orange and never patterned. "
          "If any person appears in this frame at all, that person follows the series rules: " + NGUOI)
SCENE_N = ANIMAL   # canh khong co nhan vat nguoi
WHO = {"SCENE_A": ANCIENT, "SCENE_M": MODERN, "SCENE_W": WOMAN, "GROUP": GROUP, "SCENE_N": SCENE_N}

# 🔴 THÊM 11/08/2026 — khối cho SCENE_N THUẦN CẢNH (không con vật, không người).
# Bản vá sáng 11/08 bỏ hẳn khối WHO cho loại khung này, tưởng là "sạch". Hoá ra
# prompt KHÔNG CÒN MỘT DÒNG LUẬT NÀO VỀ NGƯỜI, và model lấp chỗ trống bằng thứ
# nó quen tay nhất: một anh hiện đại đầu trọc mặc áo len. 28/46 khung SCENE_N của
# lô 2 hỏng đúng vì thế, gồm CẢ HAI KHUNG CUỐI VIDEO.
# Luật: khoảng trống trong prompt không bao giờ là khoảng trống trên hình.
NO_PERSON = (
    "NO people in this frame: no person, no face, no body, no hands, nobody in the distance, "
    "nobody at the edge. Landscape and objects only. ")
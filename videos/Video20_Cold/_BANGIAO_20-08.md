# BÀN GIAO — V20 · cuối ngày 20/08/2026

## 🔴 ĐỌC TRƯỚC: CHỦ CHẤM KỊCH BẢN BẰNG **TAI**, KHÔNG BẰNG MẮT

Chủ **không đọc** bản tiếng Anh để chấm. Chủ **nghe** bản dịch tiếng Việt dựng TTS
`vi-VN-NamMinhNeural` + `rate="+8%"`, và so thẳng với bản dịch đối thủ dựng **cùng giọng cùng tốc độ**.

Đưa text cho chủ duyệt là **vô ích**. Sửa xong phải chạy đủ:
> dịch *(tái dùng bản dịch cũ cho dòng không đổi, chỉ dịch dòng mới)* → TTS → ghép mp3 → `open` + gửi file
> → kèm **bản đồ mốc phút** để chủ báo "tụt ở phút mấy"

**Vì sao biết:** chủ bác bản 17 bằng đúng một câu — *"nghe chả hiểu gì luôn, nghe mà chả muốn nghe"* —
sau khi nghe Axen rồi nghe V20. Năm phán quyết tiếp theo của chủ đều từ tai, và **lần nào cũng đúng chỗ
mà phép đếm máy không bắt được**.

⚠️ Giọng `vi-VN` bị Microsoft chập chờn → script TTS phải có `timeout=8s` + thử lại 12 lần + 4 luồng.
Mẫu chạy được: `_ban25/_tts.py`.

## Chín bản trong ngày — bản nào là gì

| bản | dài | đổi gì | thư mục |
|---|---|---|---|
| 17 | 19:47 | bản đầu ngày. 🔴 chứa lỗi **"William Haskell"** + độ C chưa đổi | `Script_V20_narration.txt` *(vẫn đang là bản chính)* |
| 18 | 20:45 | đổi °C→°F · mỏ neo đời nay 15→35 | `_ban18/` |
| 19 | 13:17 | cắt 36% · móc 0,49→1,99/phút | `_ban19/` |
| 20 | 13:01 | **cấu trúc 9 món** thay vì 1 cơ chế | `_ban20/` |
| 21 | 13:45 | **9 cú lật niềm tin** + terminal burrowing | `_ban21/` |
| 22 | 12:55 | + sư tử hang · hồ Galilee rút nước · **lò nung cổ nhất thế giới** | `_ban22/` |
| 23 | 12:55 | nâng dẫn nguồn: tên đầy đủ + tổ chức, **0 câu mơ hồ** | `_ban23/` |
| 24 | 12:54 | 4 nguồn thành 4 câu chuyện có cao trào | `_ban24/` |
| **25** | **13:23** | **8/9 món có cú chốt** — bản mới nhất | `_ban25/` |

## Việc kế, đúng thứ tự

1. **Chủ chốt bản chính** *(D-28)* — chưa chốt thì không chia shot được, mọi khâu sản xuất đứng
2. Verify **toàn văn Rothschild & Schneider 1995** *(69 ca · 25%)* — mới đọc qua bản tóm tắt
3. Chia shot lại từ bản chốt *(`shot_data.py` đang 54 tuple của kịch bản đầu tiên)*
4. `build_prompts.py` → gen ảnh **1 lượt vào thư mục RỖNG**
5. TTS tiếng Anh → ghép
6. Thumbnail bản B → Test & Compare
7. Mid-roll · cổng 10 người nghe ngoài *(chỉ chủ làm được)*

## Cổng còn thiếu

`5` viết kết trước *(trễ, không cứu ngược được)* · `10` người nghe ngoài · `P1` ảnh ·
`P4` thumbnail B · `P6` mid-roll.
⚠️ `P2 tiếng` và `P3 ghép` đang báo **✅ GIẢ** — 1.100+ mp3 và 2 mp4 đều của kịch bản cũ.

## Bài học ghi ở đâu

- **7 thước từ 8 quả nổ**: `.claude/skills/sketchapiens-viet-kich-ban/SKILL.md` **PHẦN 13**
- **Số gốc + cách đo**: `kho/3_bangchung/BOC_8BAI_MACH_DEM_2026-08-20.md`
- **Chờ chủ duyệt**: `governance/DECISIONS_REQUIRED.md` **D-27** *(nâng thành luật?)* · **D-28** *(chốt bản nào?)*
- **Metadata cần làm lại**: chapters trong `METADATA_V20.md` đo cho bản 19:47, nay sai hết

---

## 🔴 BÀI HỌC ĐẮT NHẤT NGÀY 20/08 — CẮT BÙ GIỜ LÀ HÀNH ĐỘNG NGUY HIỂM NHẤT

Mỗi lần cắt để về mốc phút, tôi lại làm **đứt mạch** ở chỗ khác. **Bảy lần**, và
**không lần nào máy đếm báo** *(cổng A sạch, ba ràng buộc sạch, mọi thước đều đẹp)*:

| câu bị hỏng | vì cắt mất |
|---|---|
| `That last step is inference` | câu suy diễn mà "bước đó" trỏ tới |
| `It would lie in a ring` | câu dựng chủ ngữ |
| `Giving heat away, on purpose` | hai câu anaphora chen giữa → thành lặp |
| `Core temperature. / Melatonin.` | câu dựng + 2 mục → danh sách cụt, "them" trỏ vào hư không |
| `One warm surface, held against skin` | câu dựng |
| `They are layers` | câu "không phải một đám lửa" |
| `Giờ bỏ luôn cái quyền nhích chỗ đi` | *"gió đổi chiều một cái là biết / ai cũng nhích chỗ"* |

**Sáu cái đầu bắt được bằng ĐỌC. Cái thứ bảy đọc vẫn sót — chỉ CHỦ NGHE mới ra.**

→ Luật rút ra, ba tầng:
1. **Máy** bắt được ba ràng buộc cứng. Hết.
2. **Đọc** bắt được đứt mạch, lặp ý, cú lật đặt sai chỗ.
3. **Chỉ TAI** bắt được câu mất chỗ bám — vì mắt tự vá nghĩa, tai thì không.

⛔ **Sau mỗi lần cắt, phải ĐỌC LẠI CẢ ĐOẠN, không chỉ đọc câu vừa cắt.**
Và bản cuối phải NGHE hết, không được duyệt bằng mắt.

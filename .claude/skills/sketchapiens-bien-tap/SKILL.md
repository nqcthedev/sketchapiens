---
name: sketchapiens-bien-tap
description: >-
  [DỰ ÁN SKETCHAPIENS — kênh người que cổ đại] CHẾ ĐỘ BIÊN TẬP — chạy cổng 7, 8, 9 của
  FLOW_VietKichBan_11Cong sau khi kịch bản đã viết xong: đo kịch bản BẰNG MÁY (dấu chấm than,
  đại từ, câu hỏi, nhịp câu, độ dài), QA chính sách nội dung không trung thực của YouTube
  (3 nhóm vi phạm), chống văn AI, đọc to, và hai phép thử chống trùng đối thủ trước khi chốt.
  KHÔNG viết nội dung mới, KHÔNG tra đề tài. Dùng khi user nói "chấm kịch bản", "QA kịch bản",
  "soát lại trước khi đăng", "đo kịch bản", "kiểm chính sách", "chống văn AI", "kịch bản này
  đạt chưa", hoặc vừa viết xong một kịch bản Sketchapiens và cần kiểm trước khi chia shot.
---


> **CHẾ ĐỘ ③ BIÊN TẬP** — cổng 7–9, 11
> Chỉ đo và soát. Không viết nội dung mới.
>
> Quy trình tổng + BẢN ĐỒ KHO 4 TẦNG + luật ưu tiên khi hai file mâu thuẫn:
> `/Users/admin/Claude/Projects/Build Channel Người Que Cổ Đại/00_LUAT_HIEN_HANH.md` → `kho/1_luat/FLOW_VietKichBan_11Cong.md`

# Chế độ BIÊN TẬP — cổng 7, 8, 9, 11

> **Chỉ cho dự án `Build Channel Người Que Cổ Đại` / kênh Sketchapiens.**
> Quy trình tổng: `00_LUAT_HIEN_HANH.md` → `kho/1_luat/FLOW_VietKichBan_11Cong.md`.

**Ranh giới của chế độ này:** chỉ **đo và soát**. Không viết chương mới, không đổi cú bẻ lái,
không mở nexlev tra đề tài. Thấy thiếu nội dung thì **ghi vào sổ và trả về chế độ VIẾT**.

---

## 🔴 LUẬT 0 — đọc trước khi nhìn bất kỳ con số nào

**Mọi con số benchmark là KẾT QUẢ quan sát ở video thắng, KHÔNG phải chỉ tiêu phải đạt.**

Lệch chuẩn thì hỏi *"bài này có tầng đó không?"* — có mà thiếu thì bổ sung; **không có thì để
yên**. Rắc chữ vào cho đủ chỉ tiêu đẻ ra câu *viết-để-được-khen*, đúng lỗi đã ghi trong
`kho/1_luat/RUBRIC_KichBan.md`: *"ba câu mùi AI nặng nhất của V17 đều là câu thêm vào để thoả Tầng A."*
*(⚠️ "Tầng A" là kiến trúc thang điểm — **đã bỏ 09/08**. Câu trích giữ nguyên vì nó chính là
lý do bỏ: chấm theo ô đẻ ra câu viết-cho-đủ-ô. Nay chỉ còn **4 CỔNG** đạt/không-đạt.)*

**Bốn con số đã bị đuổi theo sai ngày 06/08:**

| Chuẩn | Chuyện gì |
|---|---|
| giác quan 7–9% | ❌ đo cùng một từ điển thì **V17 chỉ 5,2%**, V19 5,5%. Con số 7–9% đo bằng từ điển khác — **không so thẳng được** |
| mỏ neo 3,2–5,1/phút | ❌ V19 đo ra **12,2** — thước khác nhau, không kết luận được |
| hedge 1–3 | ⚠️ **nửa đúng.** Phép đếm đúng *(NotebookLM ghi "5 lần" là sai, đếm tay ra **1**)*, nhưng **con số 1-3 làm luật thì đã chết 09/08** — vấn đề là **CHỖ ĐẶT**: Ink Rain rào rất tử tế ở chương ít cần rào nhất rồi phát ngôn chắc nịch cho mệnh đề lớn gấp mười. **Rào đúng chỗ luận điểm yếu nhất**, không rào cho đủ số lần |
| you : we = 1,5–2 | ⚠️ **không phải hằng số** — 4 winner ra 2,7 · 1,5 · 1,5 · 1,6, **chênh theo nội dung bài** |

---

## CỔNG 7 — đo bằng máy

Script đã có sẵn trong skill này, **đã chạy thử trên file thật**:

```bash
python3 .claude/skills/sketchapiens-bien-tap/qa_kichban.py \
  "…/VideoNN_…/Script_VideoNN_narration.txt"
```

Output thật của tool, chạy 22/08/2026 trên V19:

```
  1491 từ · 8.4 phút · 149 câu
  CỨNG (3): '!' 0 (phải 0) | '—' 0 (phải 0) | mỗi câu một dòng: xem dưới
  ĐO — KHÔNG PHẢI NGƯỠNG: 'I' 0 (người dẫn ĐƯỢC có ý kiến) | câu hỏi 4 | câu<6từ 30 (20%) | dài TB 10.0 | 3 câu dài liên tiếp: không
  CỨNG: mỗi câu một dòng → ❌ 22 dòng có >1 câu: [2, 3, 10, 23, 24, 29, 35, 52]
  you 50 : we 0 = 50.0:1  ← LUẬT 0, không phải hằng số
```

> ⛔ **Ví dụ cũ ở đây từng in `'I'` dưới nhãn `CỨNG`.** Ảnh chụp đó từ **06/08**, tức **trước** khi
> `I ≈ 0` bị gỡ ngày **07/08**. Nó mâu thuẫn với chính bảng ngưỡng 9 dòng bên dưới.
>
> Vì sao đáng thay chứ không phải chuyện chữ nghĩa — `qa_kichban.py:19-20` ghi lại hậu quả **đã
> xảy ra một lần**: *"Bản cũ in `'I'` dưới nhãn CỨNG, và `/apply-review` đọc dòng đó làm điều kiện
> chặn → editor sẽ CẮT MỌI CÂU CÓ `I`."* Tool đã vá từ 09/08; ví dụ trong tài liệu thì tới hôm nay
> mới vá. Xem `governance/audits/phase5-agents/05A-B` finding `F-5`.
>
> ⚠️ Và output thật cho thấy **V19 đang trượt ràng buộc cứng thứ ba** — 22 dòng chứa hơn một câu.
> Đó là dữ kiện về V19, không phải về tool.

**Ngưỡng cứng — lệch là sửa, không bàn:**

| | |
|---|---|
| Dấu `!` | **0** *(14/14 winner)* |
| Gạch ngang `—` giữa câu | **0** *(TTS đọc vấp)* |
| **Mỗi câu một dòng** | *(1 dòng = 1 shot ảnh + 1 khối TTS — thiếu là gãy pipeline chia shot)* |
| ~~`I` đứng riêng~~ | ⛔ **GỠ 07/08** — người dẫn ĐƯỢC có ý kiến riêng *(9/12 kênh: bài dùng `I` ăn hơn, Mack 9,18×)* |
| ~~Ba câu dài liên tiếp~~ | ⚠️ ghi nhận, không phải ràng buộc cứng |

**Ngưỡng mềm — lệch thì đi soi, đừng vá bằng cách rắc chữ:** số câu hỏi · % câu ngắn ·
độ dài câu TB · tỉ lệ you:we.

**So với chính kênh mình, đừng so với con số trừu tượng.** V17 giữ chân **55,6%** — đó là mốc
thật gần nhất. ⛔ **KHÔNG có "chuẩn hiện hành".** Bốn con số cũ *(178 wpm · dài câu TB 8,9 ·
37% câu dưới 6 từ · 1 chùm câu ngắn mỗi ~87 từ)* đo từ **một video của chính mình** — V17,
video **20 view**. Ink Explainer có **5%** câu mảnh, kênh mình 34%, cả hai đều sống. Dùng
chúng làm mốc *biết mình đang ở đâu*, đừng dùng làm đích.

---

## CỔNG 8 — QA chính sách nội dung không trung thực

YPP xét ở **cấp KÊNH theo TỶ LỆ**, không xét từng video. Một video lệch không chết;
**nửa kênh cùng một khuôn thì chết**.

| Nhóm | Hỏi gì | Chữa thế nào |
|---|---|---|
| **1. Khuôn mẫu / lặp hàng loạt** | Cùng bộ xương với video trước, chỉ đổi danh từ? Trùng beat với quả to cùng đề tài? | Chạy lại cổng A *(grep, kể cả `_nhap/`)*. Trùng → sửa **cú bẻ lái**, không phải sửa chữ |
| **2. Gây khó chịu · trẻ em trong hoàn cảnh đau đớn** | Có chết chóc, trẻ em, máu me, tả thực? | **Bộ giáp `KHO_AnDu` phần 3** *(xem dưới)* |
| **3. Nhân vật AI trong chủ đề YMYL** | Có giả làm chuyên gia y tế / tài chính? | Kênh không dùng persona → không dính |

### Bộ giáp cho nhóm 2 — bốn lớp, dùng đủ cả bốn

1. **Neo khảo cổ mở đầu** — mở khối bằng **địa danh + niên đại + tên nghiên cứu** trước khi
   kể hành vi đen tối. Đây là tín hiệu cho bộ quét tự động rằng đây là nội dung Giáo dục.
2. **Thuật ngữ lâm sàng** — *"surgical procedure of trepanation, showing bone regrowth"*,
   không phải *"khoan nát sọ, máu chảy ròng ròng"*.
3. **Giọng nhân học khách quan** — cấm phán xét cảm tính *("thật kinh tởm", "thật man rợ")*.
   Giải thích mọi hành vi dưới góc **thích nghi sinh tồn**.
4. **Không tả thực** — số liệu về người chết đọc như **dòng thống kê trong bài báo khoa học**,
   không đọc như một cảnh phim.

---

## CỔNG 9 — chống văn AI + đọc to

Chạy skill `chong-van-ai-narration-en`. **Giữ nguyên số dòng, số liệu, cấu trúc** — nó chỉ
sửa nhịp và chữ.

Rồi **đọc to từng câu**. Câu nào *"không narrator thật nào nói thế"* → viết lại.
Đây là bước không máy nào thay được.

**Quét nhanh mùi AI:** `furthermore` · `moreover` · `it is important to note` · `delve` ·
`tapestry` · `testament to` · `plays a crucial role` · `let's dive in` · `in conclusion` ·
bộ ba đều tăm tắp lặp đi lặp lại · `not only… but also` rải khắp nơi.

---

## CỔNG 11 — hai phép thử cuối, làm trước khi chốt

1. **Người vừa xem video đối thủ, xem tiếp video mình — có thấy *"đã xem rồi"* không?**
2. **Gỡ logo, dán cạnh 20 video cùng title — có ai chỉ ra được cái nào là của mình không?**

Một trong hai trả lời "có" → **chưa được chốt**.

---

## Ba lỗi được quyền DỪNG DÂY CHUYỀN

Chỉ ba lỗi này mới được dừng cả video. Còn lại — hài thưa, ẩn dụ thiếu, câu dài — **ghi vào sổ,
sửa vòng sau, không dừng**.

1. **Mỏ neo không tra được nguồn**
2. **Cổng A báo trùng**
3. **QA chính sách báo đỏ**

Ba cái đó đe doạ sự sống của kênh. *(Kênh Shorts cũ của chủ, 25 triệu view, đã bị sập vì lỗi
loại 1–2.)*

---

## Định dạng báo cáo trả về

```
ĐO MÁY      — bảng số + so với V17
CỔNG 8      — 3 nhóm, mỗi nhóm ✅/⚠️/🔴 + lý do
CỔNG 9      — số câu đã sửa + câu nào phải viết lại
CỔNG 11     — hai phép thử, trả lời có/không kèm lý do
DỪNG DÂY?   — có / không. Có thì nói rõ lỗi nào trong ba lỗi trên
CÒN NỢ      — việc trả về chế độ VIẾT (không tự sửa ở đây)
```

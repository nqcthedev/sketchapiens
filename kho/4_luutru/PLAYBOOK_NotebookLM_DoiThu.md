s# PLAYBOOK NOTEBOOKLM — bóc từ video hướng dẫn của đối thủ
*Nguồn: TikTok `snaptik.vn_7663087900195769620.mp4` (2:30, cre:iam4tt). Bóc 30 khung hình 29/07/2026.*

Đây là quy trình **dựng kênh stickman lịch sử/giáo dục bằng AI** — đúng ngách Sketchapiens. Video dùng **Ink Explainer** làm mẫu để bóc ngược.

---

## SỐ TIỀN HỌ TRƯNG RA

| Kênh | Chỉ số |
|---|---|
| Video "WHY CLOTHEST" | **303.453 view → $2.647,21** · 4.300 giờ xem · +2.100 sub |
| **Ink Explainer** | hơn **1,6 triệu** view |
| **You Are History** | **9 video → 17.000 sub** |
| **Serious History** | 57 (video) |

RPM ≈ **$8,7** — cao hơn hẳn ước tính $3-6 tôi đưa cho ngách này. Đáng ghi nhận lại.

---

## QUY TRÌNH 11 BƯỚC

### 1. Dựng kênh
Chọn tên → tạo logo stickman → banner → kênh sẵn sàng.

### 2. Nạp đối thủ vào NotebookLM
Mở NotebookLM bằng tài khoản Google → **Add sources** → chọn **"Website and YouTube URLs"** → **dán thẳng URL kênh đối thủ**.

*(Ví dụ trong video: kênh Ink Explainer → notebook đặt tên "Ink Explainer: Decoding Human History and Behavior")*

### 3. Prompt PHÂN TÍCH
Có một Google Doc tên **"Historical Stick Figure Animation Masterclass"** chứa sẵn bộ prompt. Copy **prompt phân tích thứ nhất** dán vào NotebookLM.

Nội dung prompt đọc được trên màn hình:
> *"Analyze the title patterns, hook structures, and script formats across these videos. Give me a 1-paragraph summary of what makes these videos work — format, episode length, POV style, pacing, and story arc."*

→ Nó bóc ra: **tiêu đề · hook · thumbnail · format · độ dài · ngôi kể · nhịp · vòng cung truyện**.

### 4. Sinh ý tưởng
NotebookLM trả về danh sách chủ đề mới **theo đúng format đã bóc**. Trong video nó ra 5 cái:

1. When Did Ancient Humans Start Keeping Pets?
2. What Did Early Humans Do to Clean Their Teeth?
3. The Real Reason Humans Started Cooking Food
4. How Did Ancient Humans Survive the Ice Age?
5. Why Do We Forget Our Dreams When We Wake Up?

Mỗi cái kèm ghi chú *"Mirrors the high-performing format of [video đối thủ]"*. Họ chọn số 3 (nấu chín thức ăn) làm ví dụ.

### 5. Prompt KỊCH BẢN
Copy **script prompt** từ cùng Google Doc:
> *"Using the same title format and script structure as these videos, write 5 viral title options for a new interesting episode. Keep them direct, search-friendly, and matched to the channel's pattern. I'll choose the winner, then you write the entire script."*

Kịch bản ra **chia sẵn theo SCENE có timestamp**, và mỗi scene kèm **hai prompt**:

```
SCENE 1 — Savanna Intro (0:00 – 0:08)
IMAGE: 2D webcomic cartoon style, flat colors, thick black
       outlines, simple hand-drawn characters...
VIDEO: The 2D animated caveman slowly...

SCENE 2 — Aching Jaw (0:08 – 0:16)
IMAGE: ...
VIDEO: ...
```

→ **Đây là điểm khác lớn nhất so với pipeline của mình.** NotebookLM sinh luôn cả prompt ảnh **và prompt chuyển động** cho từng cảnh.

### 6. Khoá phong cách nhân vật
Đưa **một ảnh tham chiếu** vào NotebookLM → yêu cầu nó khoá style → nó sinh ra **"character image prompt"** dùng lại cho mọi cảnh.

Video ghi rõ: *"has been successfully locked"*, và prompt chứa cụm *"a large round head, big thin arms and legs, an expressive face with fur-colored... simple hand-drawn characters, clean vector-like design, humorous educational illustration"*.

### 7. TTS bằng **Dub Dub AI**
Dán kịch bản → chọn giọng (giao diện có bảng chọn nhiều giọng theo ngôn ngữ/giới tính) → **chọn quality** → tải xuống **MP3**.

*(Không dùng ElevenLabs.)*

### 8. Gen ảnh
Dùng prompt cảnh + **ảnh tham chiếu** → **tỷ lệ 16:9** → gen từng scene.

### 9. Làm ảnh CHUYỂN ĐỘNG bằng **Google Flow**
Kéo từng ảnh vào Flow → **dán prompt chuyển động (VIDEO) mà NotebookLM đã viết sẵn** → bấm next → ra clip động.

Màn hình cho thấy lưới nhiều clip đã sinh, mỗi clip là một cảnh caveman động.

### 10. Dựng phim bằng **CapCut**
Tải từng clip ở **chất lượng cao** → xếp clip **theo đúng lời đọc** → **tắt âm gốc của clip** → thêm **mix transition** giữa các đoạn → xuất bản chất lượng cao.

### 11. Thumbnail
Cũng dùng **Flow + ảnh tham chiếu**.

---

## KHÁC BIỆT SO VỚI PIPELINE HIỆN TẠI CỦA MÌNH

| | Sketchapiens | Playbook này |
|---|---|---|
| Số cảnh / video | **185 ảnh tĩnh** | **~10-20 clip động** |
| Nguồn prompt ảnh | tôi viết tay từng cái | **NotebookLM sinh kèm kịch bản** |
| Chuyển động | **không có** (ảnh đứng yên) | **có** — Flow image-to-video |
| TTS | ElevenLabs | Dub Dub AI |
| Dựng | script ffmpeg | CapCut thủ công |
| Nghiên cứu đối thủ | tôi + agent đọc transcript | **NotebookLM đọc thẳng URL kênh** |

**Điểm đáng lấy nhất: bước 2-5.** Nạp URL kênh đối thủ vào NotebookLM rồi bảo nó bóc format và sinh đề tài theo đúng khuôn đó — nhanh hơn hẳn cách tôi đang làm (tải transcript, chia agent, đọc từng bản).

**Điểm cần cân nhắc:** họ dùng **10-20 cảnh động** thay vì 185 ảnh tĩnh. Rẻ hơn nhiều về công, nhưng nhịp đổi hình sẽ chậm hơn.

## 🔴 ĐÃ KIỂM XONG — PLAYBOOK NÀY DẠY SAI Ở BƯỚC 9

Đo trực tiếp video **Ink Explainer "How Did Ancient Humans Travel the World?" (617K, 9:22)** — chính kênh mà playbook lấy làm mẫu:

| | Trung vị | Cao nhất | Số mốc đứng yên |
|---|---|---|---|
| 40 mốc rải đều toàn video | **0.000** | 0.013 | **40/40 (100%)** |

**Ink Explainer dùng ảnh TĨNH hoàn toàn.** Không một khung nào động.

Cộng với 117 điểm đã đo trên Zenn/Mack/Stickly (trung vị cũng 0.000) → **4 kênh thắng, cả 4 đều ảnh tĩnh.**

→ **BỎ HẲN BƯỚC 9 (Google Flow image-to-video).** Nó thêm chi phí, thêm thời gian, thêm một khâu có thể hỏng, đổi lại không có lợi ích nào đo được. Video hướng dẫn dạy một pipeline đắt hơn chính kênh nó đang lấy làm ví dụ.

→ Pipeline ảnh tĩnh hiện tại của Sketchapiens **đúng**, giữ nguyên.

---

## VIỆC NÊN THỬ NGAY (rẻ)

1. Nạp URL **Zenn** + **Ink Explainer** vào NotebookLM, chạy prompt phân tích ở bước 3, so kết quả với hệ thống `../1_luat/HE_THONG_KichBan_v2_14Video.md` ⛔ *(v1 đã chết — v2 bác 4 luật của nó)*. Xem nó bóc được gì mình chưa có.
2. Đo chuyển động của **Ink Explainer** để xác minh mâu thuẫn ở trên.
3. Thử **Dub Dub AI** so với ElevenLabs về giá — vì với mô hình 3 video/ngày thì tiền TTS là biến quyết định.

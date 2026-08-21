# TOÀN BỘ CÁCH PHÂN TÍCH — sổ tra, không bỏ sót

> **Dựng 18/08/2026.** Chủ: *"liệt kê chi tiết đầy đủ luôn, không bỏ sót cái nào dù là nhỏ nhất."*
> Gồm cả cách **đã dùng**, cách **có mà chưa dùng**, và cách **chưa từng nghĩ tới**.

---

# A · PHÂN TÍCH CẦU — trước khi chọn đề tài

| # | cách | công cụ | ghi chú |
|---|---|---|---|
| A1 | **Đếm ĐỈNH BẦY clone** | `youtube_search` | đỉnh <10K thì bỏ ô. ⛔ **không dùng trung vị** — clone làm ẩu nên chết, không phải ô bão hoà |
| A2 | **Đếm SỐ quả nổ trong ô** | như trên | 1 quả = trúng số · 4+ quả ở 4 kênh khác cỡ = cầu lặp lại được |
| A3 | **Tuổi quả nổ** | `youtube_video_details` | 2 tháng = cầu đang sống · 1 năm = có thể đã nguội |
| A4 | **Kênh LỚN có đang vào ô không** | `youtube_channel_videos` | Mack vào ô đêm lạnh trước mình 14 giờ = tín hiệu mạnh |
| A5 | **Hình dạng phân bố view trong bầy** | đọc kết quả search | 1 quả 170K + 13 quả <250 = trúng số |
| A6 | **Khuôn title nào đang ăn** | `HE_THONG_KichBan_v2` PHẦN C | bảng 159 video: `When Did Ancient Humans First Start…?` = 287K trung bình |
| A7 | **Kênh đối thủ còn bật kiếm tiền không** | `check_channel_monetization` | Ink Explainer `isMonetized:false` → đừng lấy làm hình mẫu |
| A8 | **Tuổi NỘI DUNG của kênh** | `youtube_channel_videos` | không phải tuổi kênh — nhiều kênh lập lâu mới đăng |

# B · MỔ KỊCH BẢN ĐỐI THỦ

| # | cách | ghi chú |
|---|---|---|
| B1 | **Kéo bản ghi** | `get_video_transcript` · nhiều bài dùng `get_bulk_video_transcripts` |
| B2 | 🔴 **ĐỌC TRỌN, không grep** | grep = tìm chỗ · đọc = kết luận. Ba lớp lỗi grep **không bao giờ** thấy: thứ **thiếu vắng** · mâu thuẫn giữa hai đoạn **cách xa** · **hình dạng/nhịp** |
| B3 | **Bóc 9 chiều** | `BOCTACH_KICHBAN_DOITHU.md` — lệnh: *"bóc kịch bản <link> theo 9 chiều"* |
| B4 | **Chia bài làm 10 khúc, đo theo khúc** | *có ai gặp nguy hiểm không* · mật độ mỏ neo · vật mới. **Vị trí quan trọng hơn số lượng** |
| B5 | **Đo % khối DÀI NHẤT** | Axen 16,6%. Quá 18% = bắt người xem giữ một ý quá lâu |
| B6 | **Đếm từ khoá theo nhóm** | chết · you/we/our · vật thể · địa danh · rào đón · động từ hành động |
| B7 | **Đo VỊ TRÍ % của từng thứ** | *nguy hiểm xuất hiện ở 2% hay 44% bài* — chênh lệch này lớn hơn mọi con số đếm |
| B8 | 🔴 **NHÓM ĐỐI CHỨNG — bài CHÌM khớp cặp** | **cùng kênh**, gần bằng số từ. Đây là phép đo giết được nhiều luật nhất: 3/4 luật rút từ 6 bài triệu view **chết ngay khi đọc 5 bài chìm** |
| B9 | **Dịch sang tiếng Việt + TTS, NGHE** | `edge-tts` miễn phí, giọng `vi-VN-NamMinhNeural`. Nghe bằng tiếng mẹ đẻ thì câu chữ tiếng Anh không đánh lừa được nữa |
| B10 | **Nghe bài ĐỐI THỦ TRƯỚC, bài mình SAU** | cùng giọng, cùng tốc độ. Nghe mình trước là đầu đã tự bào chữa |
| B11 | **Ép bản đọc khớp độ dài video gốc rồi xem kèm hình** | `ffmpeg atempo`. Mở video YouTube tắt tiếng, chạy song song |
| B12 | **Đếm nhịp hài và CHỖ ĐẶT** | hay rơi ngay sau nhịp nặng |
| B13 | **Tìm cú lạ ĐỂ DÀNH cho cuối** | có báo trước không, đặt ở % nào |
| B14 | **Vẽ biểu đồ % từng khối** | nhìn ra ngay khối nào phình |
| B15 | **Đo từ mỗi câu** | ⚠️ Axen **16,8 — DÀI HƠN mình**. "Câu ngắn mới punchy" là sai |

# C · PHÂN TÍCH HÌNH ẢNH

| # | cách | ghi chú |
|---|---|---|
| C1 | **Xem video thật bằng AI** | `watch_youtube_video_and_ask` — **công cụ DUY NHẤT đo được nhịp đổi ảnh**. Gói free 1 lượt/24h |
| C2 | **Đếm % khung THẺ vs CẢNH** | đối thủ 36-41% thẻ · V19 của mình 62% = hỏng |
| C3 | **Xem thumbnail ở 246px** | cỡ thật trong feed. Chấm ở cỡ lớn là chấm sai |
| C4 | **Đo bão hoà / độ sáng** | `PIL` + `colorsys`. ⚠️ **cả bốn phép đo toàn ảnh đều KHÔNG phân biệt được** quả nổ với quả của mình |
| C5 | **Cắt cận mặt nhân vật, đặt cạnh nhau** | cách duy nhất bắt được "tóc chưa đủ rậm" |
| C6 | **Trộn thumbnail của mình vào hàng quả nổ** | nhìn ở cỡ feed, xem có chỉ ra được cái nào của mình không |
| C7 | **`get_similar_thumbnails`** | ⚠️ có mà chưa dùng |
| C8 | **Đối chiếu pixel khung mp4 với ảnh gốc** | kiểm sync sau khi ghép, 9-11 mốc |

# D · SỐ CỦA CHÍNH MÌNH

| # | cách | ghi chú |
|---|---|---|
| D1 | **Impressions · CTR · AVD từng video** | Studio. **Từng video, không phải trung bình kênh** |
| D2 | 🔴 **Test & Compare — 3 thumbnail/1 video** | thứ **duy nhất** tách được thumbnail khỏi đề tài. **Miễn phí, chưa dùng lần nào** |
| D3 | **Chẩn 3 bệnh** | A chưa được đẩy · B không ai bấm · C bấm rồi bỏ. Chữa nhầm là mất hàng tháng |
| D4 | **So TRONG NỘI BỘ kênh** | cặp khớp thắng↔chìm cùng kênh. So giữa các kênh là lẫn biến |
| D5 | **`get_my_audience_retention`** | ⚠️ có mà chưa dùng — cần đủ mẫu |
| D6 | **`get_my_traffic_sources`** | ⚠️ chưa dùng. Biết view đến từ đâu mới biết sửa gì |
| D7 | **Tỉ lệ sub/view** | cửa ải thật để bật tiền, không phải giờ xem |

# E · PHÉP KIỂM BẰNG MÁY

| # | công cụ | bắt gì |
|---|---|---|
| E1 | `tools/do_kich_tinh.py` | Cổng 5 — kịch tính, so tỉ lệ với quả nổ cùng ô |
| E2 | `tools/validate_shots.py` | ghép shot == narration · SCENE_N không khai người · subject nói ngủ thì face=asleep |
| E3 | **Cổng A bằng 5-gram** | tự trùng lặp với video cũ. Grep từ khoá **mù** ở tầng khung câu |
| E4 | `tools/preflight.py` | 10 cổng kịch bản + 6 cổng sản xuất |
| E5 | **Đối chiếu pixel 9 mốc** | lệch hình-tiếng |
| E6 | **Đếm mẫu WAV** | ⛔ không tin độ dài mp3 của ffprobe |

# F · 🆕 CÁCH CHƯA TỪNG DÙNG — đề xuất

| # | cách | vì sao đáng |
|---|---|---|
| **F1** | 🔴 **ĐỌC BÌNH LUẬN của quả nổ** — `youtube_video_comments` | **Người xem tự nói ra cái gì giữ chân họ.** Đây là dữ liệu duy nhất về *cảm nhận* mà không phải suy đoán. Dự án chưa đọc một bình luận nào |
| **F2** | **Đo mật độ VẬT MỚI theo thời gian** | quả 2,04M có vật mới mỗi 20-30 giây. Vẽ đường cong này cho cả hai bên |
| **F3** | **Vẽ vị trí mọi mỏ neo trên trục thời gian** | thấy ngay chỗ nào bài trống bằng chứng |
| **F4** | **Đọc bình luận của quả CHÌM cùng kênh** | người xem nói ra cái gì làm họ bỏ |
| **F5** | **`get_video_rpm`** trên đối thủ | biết ô nào ra tiền, không chỉ ra view |
| **F6** | **`search_viral_videos_small_channels`** | tìm kênh nhỏ mà nổ — gần hoàn cảnh mình hơn kênh to |
| **F7** | **`youtube_channel_outliers`** | trong một kênh, quả nào vượt trội so với chính nó |
| **F8** | **Đo đường cong "câu hỏi mở ↔ câu trả lời"** | đếm chỗ nào bài mở vòng tò mò mới trước khi đóng vòng cũ |
| **F9** | **So bản ghi với MÔ TẢ video** | đối thủ hứa gì ở mô tả mà không trả trong bài |
| **F10** | **Xem 2-3 video cùng kênh liên tiếp** | tìm khuôn lặp — thứ họ làm ở **mọi** bài mới là công thức, làm một lần là ngẫu nhiên |

---

# ⚖️ SÁU NGUYÊN TẮC — quan trọng hơn mọi công cụ

1. **Không có nhóm đối chứng thì KHÔNG thành luật.** Dự án đã bốn lần đẻ luật từ mẫu quá nhỏ rồi phải giết lại.
2. **Đo TRONG nội bộ một kênh**, đừng so giữa các kênh — giữa kênh thì lẫn biến tuổi, tệp, may.
3. **Số đếm tay trên bản ghi gốc thắng MỌI báo cáo**, kể cả NotebookLM *(sai 7/10)*.
4. **Máy TÌM CHỖ, mắt KẾT LUẬN.** Máy không thấy mở bài lặp hai lần, không thấy cú lật bị tiêu sớm.
5. **Vị trí quan trọng hơn số lượng.** *Nguy hiểm ở 2% bài hay 44% bài* nói nhiều hơn *có bao nhiêu chữ "chết"*.
6. **Số của đối thủ KHÔNG phải trần.** Mỏ của mình sâu hơn thì đào sâu hơn.

> ⚠️ **Thứ KHÔNG công cụ nào mua được:** đường cong giữ chân của video đối thủ. YouTube chỉ cho chủ kênh xem. Mọi phân tích retention của người ngoài — kể cả của file này — đều là **suy từ văn bản**, không phải đo.

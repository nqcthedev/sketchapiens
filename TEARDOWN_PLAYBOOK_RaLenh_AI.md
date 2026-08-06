# Bộ prompt "Bóc tách kịch bản đối thủ" — ra lệnh cho AI moi toàn bộ kỹ thuật

Mục tiêu: biến kịch bản triệu view của đối thủ thành **công thức tái dùng được**, rồi ép kịch bản của mình đạt cùng đẳng cấp. KHÔNG copy — chỉ moi PATTERN (kỹ thuật), tự viết nội dung gốc.

---

## 0. VÌ SAO PROMPT THƯỜNG THẤT BẠI (đọc trước)

Bảo AI "phân tích video này hay ở đâu" → nó trả về bản tóm tắt nông, khen chung chung. Vô dụng.

4 thứ khiến prompt "moi được toàn bộ kỹ thuật":
1. **Cho NGUYÊN LIỆU THÔ** (transcript/lời thoại đầy đủ), KHÔNG cho bản tóm tắt của bạn. AI phải tự đọc.
2. **Chỉ ĐÍCH DANH từng trục** cần bóc (hook, đại từ, nhịp câu…). Không liệt kê trục = nó bóc lung tung, hời hợt.
3. **Bắt TRÍCH DẪN câu gốc làm bằng.** Ép trích = ép nó đọc thật, không bịa. Đây là bộ lọc quan trọng nhất.
4. **Bắt xuất ra CÔNG THỨC/CHECKLIST tái dùng**, không phải văn xuôi cảm nhận.

---

## 1. QUY TRÌNH 3 BƯỚC

```
BƯỚC 1: BÓC ADN  →  BƯỚC 2: ĐÚC THÀNH RUBRIC  →  BƯỚC 3: CHẤM + SỬA KỊCH BẢN MÌNH
(đọc transcript,     (biến pattern thành          (soi kịch bản mình theo rubric,
 rút pattern)         checklist chấm điểm)          trích câu yếu + viết lại)
```

Lấy transcript đối thủ: `yt-dlp --write-auto-sub --skip-download --sub-lang en "URL"` → ra file `.vtt` (bỏ dòng timestamp là còn lời thoại).

---

## 2. PROMPT MẪU — BƯỚC 1: BÓC ADN (dán vào, thay [ ])

```
Bạn là script doctor cấp cao cho ngách YouTube [TÊN NGÁCH].
Nhiệm vụ: BÓC TÁCH toàn bộ kỹ thuật viết của [N] kịch bản triệu view sau, để tôi tái dùng.
KHÔNG tóm tắt nội dung. Tôi cần KỸ THUẬT, không cần cốt truyện.

TRANSCRIPT (lời thoại đầy đủ):
[dán transcript / đường dẫn file .vtt — bỏ dòng timestamp]

Bóc theo ĐÚNG 10 trục dưới. Mỗi trục PHẢI trích ÍT NHẤT 2 câu gốc làm bằng chứng:
1. HOOK (30-60s đầu): mở bằng gì? nhập vai ngôi 2? câu tự giễu? nghịch lý + lời hứa chiều sâu?
2. LUẬT ĐẠI TỪ: "you" chỉ ai, "we" chỉ ai, có tránh "I" của người kể không?
3. CẤU TRÚC VĨ MÔ: có câu "không phải 1 lý do"? mấy tầng? có để dành tầng đỉnh cho cuối + báo trước không?
4. NHỊP HÀI: kiểu đùa gì (anachronism? deadpan?)? tần suất mấy giây/lần? trích 3 câu đùa.
5. CHUYỂN Ý: ngân hàng câu chuyển giữa các đoạn (câu níu chân trước khi giao ý mới).
6. CHỌN TỪ (diction): chỗ nào dùng từ cụ thể-bất ngờ thay tính từ chung? ẩn dụ công nghệ/vật thể lạ úp lên chủ đề?
7. NHỊP CÂU: phá nhịp thế nào (câu 1-2 từ xen câu dài)? trích ví dụ.
8. HÌNH ẢNH: neo khái niệm vào hình sờ được thế nào? trích.
9. TEXTURE "nói với bạn": contractions, câu hỏi thả vào, giọng có cá tính?
10. KẾT: đóng bằng gì? có "tâng danh tính người xem" (kiểu "that's you")? có callback hook?

XUẤT: với mỗi trục → (a) pattern rút ra 1-2 dòng, (b) 2-3 câu gốc trích dẫn.
Cuối cùng: liệt kê "5 vũ khí đặc trưng nhất" của các kịch bản này (thứ khiến chúng khác video thường).
Thẳng thắn, đừng khen xã giao.
```

---

## 3. PROMPT MẪU — BƯỚC 2: ĐÚC THÀNH RUBRIC TÁI DÙNG

```
Từ bản bóc ADN trên, hãy đúc thành 1 CHECKLIST CHẤM ĐIỂM tái dùng được cho mọi kịch bản tương lai.
Mỗi dòng = 1 tiêu chí kiểm được (yes/no hoặc thang 0-2), kèm 1 câu-mẫu-chuẩn của đối thủ làm mốc.
Nhóm theo: HOOK / CẤU TRÚC / GIỌNG & HÀI / DIỄN ĐẠT CÂU CHỮ / KẾT.
Xuất dạng bảng, ngắn gọn, để tôi dán vào file dùng lại mỗi lần viết video mới.
```
→ Lưu output này thành file (vd `RUBRIC_KichBan.md`). Đây là "thước đo" dùng mãi.

---

## 4. PROMPT MẪU — BƯỚC 3: CHẤM + SỬA KỊCH BẢN MÌNH (quan trọng nhất)

```
Bạn là script doctor. Đây là RUBRIC chuẩn triệu view (rút từ đối thủ):
[dán rubric bước 2]

Đây là KỊCH BẢN CỦA TÔI:
[dán / đường dẫn file kịch bản mình]

Nhiệm vụ:
1. Chấm kịch bản tôi theo TỪNG tiêu chí rubric → bảng | Tiêu chí | Đối thủ làm | Mình làm | Khớp? (✅/⚠️/❌) |.
2. Chỗ nào ⚠️/❌ → bảng SỬA: | Câu HIỆN TẠI của tôi (trích) | Vấn đề (1 cụm) | ĐỀ XUẤT viết lại (GIỮ NGUYÊN fact + nghĩa, chỉ nâng cách nói) |. Càng nhiều câu càng tốt, tối thiểu 8.
3. Verdict 1 dòng: đã ngang đẳng cấp chưa, thua rõ nhất ở tầng nào.
Ràng buộc: mọi đề xuất PHẢI giữ đúng sự thật khoa học + nghĩa gốc. Chỉ nâng diễn đạt. Đừng khen xã giao — tìm khác biệt thật.
```

---

## 5. TỪ KHOÁ "QUYỀN LỰC" (nhét vào prompt để ép AI đào sâu)

| Muốn gì | Từ khoá ép AI |
|---|---|
| Không cho nó nông | "BÓC TÁCH kỹ thuật, KHÔNG tóm tắt nội dung" |
| Ép đọc thật, chống bịa | "PHẢI trích ít nhất 2 câu gốc làm bằng chứng cho mỗi ý" |
| Ra công thức tái dùng | "đúc thành CHECKLIST/RUBRIC chấm điểm được, không phải văn xuôi" |
| Chấm thẳng tay | "thẳng thắn, đừng khen xã giao, tìm khác biệt thật để sửa" |
| Sửa câu cụ thể | "bảng: câu hiện tại (trích) → vấn đề → viết lại" |
| Không bịa số/sai fact | "GIỮ NGUYÊN fact + nghĩa, chỉ nâng diễn đạt" |
| Chống copy | "moi PATTERN/kỹ thuật, KHÔNG paraphrase/viết lại nội dung của họ" |
| So nhiều video | "rút pattern LẶP LẠI ở ≥2 kịch bản = công thức bền, không phải ăn may" |

**Cụm mở đầu mạnh:** "Bạn là script doctor cấp cao…" (cho vai) · "reverse-engineer toàn bộ…" · "soi theo ĐÚNG [N] trục sau…" (đóng khung).

---

## 6. 5 LỖI RA LỆNH THƯỜNG GẶP (tránh)

1. **Cho bản tóm tắt thay transcript** → AI phân tích cái tóm tắt của bạn, không phải video thật. Luôn cho lời thoại đầy đủ.
2. **Hỏi "video này hay không / hay ở đâu"** → khen chung chung. Hỏi "bóc theo 10 trục + trích dẫn".
3. **Không bắt trích dẫn** → AI bịa nhận xét nghe hợp lý mà sai. Trích = ép đọc thật.
4. **Bóc xong không đúc rubric** → lần sau lại bóc từ đầu. Đúc thành checklist = dùng mãi.
5. **Chỉ bóc, không chấm kịch bản mình** → biết mà không sửa. Bước 3 mới ra giá trị.

---

## 7. MẸO NÂNG CAO

- **Nhiều video, chia nhiều AI song song:** mỗi con đọc 5-6 transcript rồi gộp → nhanh + sâu hơn 1 con đọc 11 cái.
- **Tách 2 tầng riêng:** 1 lần soi CẤU TRÚC (hook/bố cục/kết), 1 lần soi DIỄN ĐẠT (câu chữ/nhịp/từ) → mỗi lần sâu hơn là gộp chung.
- **Chấm định kỳ:** mỗi kịch bản mới, chạy Bước 3 với rubric có sẵn → luôn giữ chuẩn.
- **Lưu rubric 1 lần, tái dùng mãi** — đây là tài sản, không phải làm lại mỗi video.

---

## 8. NGÂN HÀNG THUẬT NGỮ PRO (thứ dân trong nghề dùng — nhét vào prompt để đào sâu hơn)

Dùng: thêm các từ-khoá này vào Bước 1 (bóc) để AI moi được lớp kỹ thuật mà prompt thường bỏ sót.

### 8a. Khoa học RETENTION / thuật toán
| Thuật ngữ | Nghĩa | Từ-khoá teardown |
|---|---|---|
| **Open loop / Zeigarnik effect** | mở nhiều "vòng chưa đóng" cùng lúc, não bứt rứt xem tiếp | "liệt kê MỌI open loop: mở giây nào, đóng giây nào" |
| **Re-hook (mỗi ~30-60s)** | cứ ~1 phút móc lại người xem bằng câu hỏi/đe doạ mới | "đánh dấu các điểm RE-HOOK" |
| **Curiosity gap (Loewenstein — Information Gap Theory)** | tên khoa học của khoảng-trống-tò-mò | "cách nó tạo & nuôi curiosity gap" |
| **Intro cliff (30s đầu)** | chỗ rớt 30-40% người xem | "soi riêng 30 giây đầu chống rớt thế nào" |
| **Signposting / tent-poling** | cắm cọc báo trước lộ trình ("3 thứ", "cái cuối sốc nhất") | "nó signpost/hứa lộ trình ở đâu" |
| **Payoff density (value/phút)** | mấy giây 1 lần trả người xem 1 fact/cú sốc | "đo mật độ payoff" |
| **Write to the retention graph** | viết theo đường cong giữ chân — dự đoán dip rồi vá | "dự đoán retention DIP ở đoạn nào" |

### 8b. Craft biên kịch / kể chuyện
| Thuật ngữ | Nghĩa | Từ-khoá teardown |
|---|---|---|
| **In medias res / cold open** | ném thẳng vào giữa cảnh, không dạo đầu | "hook có phải cold open không" |
| **Setup–payoff / Chekhov's gun** | cài chi tiết sớm → nổ ở cuối (mạnh hơn callback) | "tìm mọi thứ CÀI sớm rồi TRẢ muộn" |
| **Escalation / raising stakes** | mỗi chương nâng cược cao hơn | "cược leo thang thế nào qua từng chương" |
| **The reframe / perspective flip** | lật góc khiến người xem "à hoá ra…" | "nó reframe/lật góc ở đâu" |
| **Emotional arc / 'chills' beat** | điểm rung động (awe) để dành cuối | "đâu là beat cảm xúc/nổi da gà" |
| **The 'so what?' test** | vì sao người xem phải quan tâm | "mỗi chương trả lời 'so what' chưa" |

### 8c. Copywriting & tu từ
| Thuật ngữ | Nghĩa | Từ-khoá teardown |
|---|---|---|
| **Bucket brigade** | câu-cầu-nối cực ngắn níu mắt ("Here's the thing:", "But it gets worse:") | "liệt kê bucket brigade/câu cầu nối" |
| **PAS (Problem–Agitate–Solve)** | nêu vấn đề → chọc cho đau → giải | "nó chạy khung PAS ở đoạn nào" |
| **Specificity / telling detail** | chi tiết cụ thể nhỏ = độ tin ("12 phút nắng") | "các telling detail tạo độ tin" |
| **Anaphora / rule of three** | lặp đầu câu + bộ-ba tu từ | "các phép lặp tu từ/rule-of-three" |
| **Analogy as compression** | ẩn dụ = nén khái niệm khó thành 1 hình | "ẩn dụ nào NÉN khái niệm khó" |
| **Verisimilitude anchor** | neo tên-di-chỉ-năm-người để nghe thật | "các mỏ neo tạo uy tín" |

### 8d. PROMPT BỔ SUNG "RETENTION EDITOR" (dán thêm vào Bước 1)
```
Ngoài nội dung, hãy soi kịch bản này như một RETENTION EDITOR chuyên nghiệp:
- Đánh dấu MỌI open loop (mở ở giây nào, đóng ở giây nào).
- Chỉ các điểm RE-HOOK (~mỗi 60s móc lại người xem).
- Chỗ SIGNPOST / hứa lộ trình ("3 thứ", "cái cuối sốc nhất").
- Các SETUP–PAYOFF: chi tiết cài sớm được trả ở cuối.
- Các BUCKET BRIGADE (câu cầu nối ngắn níu mắt).
- Dự đoán đường retention sẽ DIP ở đoạn nào, và nó vá bằng gì.
```
```
```

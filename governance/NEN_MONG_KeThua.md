# NỀN MÓNG — bản thiết kế cho dự án faceless AI kế tiếp

*Dựng 07/08/2026. Mục tiêu chủ đặt ra: **"móng chắc rồi thì sau này làm mọi chủ đề faceless AI kế thừa từ dự án này."***

> **Cách dùng file này:** dự án khác **đọc rồi tự dựng bản của mình** — không chép file sang.
> Mỗi bộ phận ở phần 2 đều ghi rõ **nó chặn lỗi gì**. Bộ phận nào không chặn lỗi nào của bạn
> thì đừng dựng. Phần 3 là phương pháp, dùng được cho mọi ngách.

> ## 🔴 ĐỌC CÂU NÀY TRƯỚC
>
> Kênh đầu tiên **chưa thắng**: 7 người đăng ký, 367 hiển thị / 5 ngày, chưa có video nào nổ.
> Nghĩa là **phần lớn luật nội dung trong `kho/` chưa được chứng minh là đúng.**
>
> Thứ đáng kế thừa lúc này là **PHƯƠNG PHÁP** *(phần 3)* và **BỘ MÁY** *(phần 2)* — hai thứ đó
> đã tự chứng minh bằng việc **bắt được lỗi thật**. Còn **kết luận nội dung thì đừng bê sang**:
> chúng đúng hay sai vẫn chưa biết.
>
> Xây khung đa-kênh trước khi kênh đầu chạy là bẫy kinh điển. Dọn móng **khi đang chờ**
> *(chờ gen ảnh, chờ YouTube đẩy)*, đừng để nó chen trước việc đăng video.

---

# 1. BA LỚP — đo thật 07/08/2026

| lớp | ở đâu | kế thừa được? |
|---|---|---|
| **Bộ máy** | `.claude/` · `tools/` · `schemas/` · `templates/` | ✅ gần như nguyên vẹn — chỗ dính tên kênh chỉ còn **ba** |
| **Cấu trúc** | `kho/1..4` · `governance/` · `videos/` · `2_KHO_BANGHI/` | ✅ khuôn kế thừa, nội dung thì không |
| **Tri thức** | 63 file trong `kho/` | ❌ dính chặt Ancient Humans |

⚠️ **Đừng lặp lại lỗi đếm của tôi.** Bản đầu mục này ghi "11 chỗ dính kênh" — sai, vì đếm cả chữ
`thumbnail`, mà thumbnail là khái niệm chung của mọi video faceless. Khi đo mức phụ thuộc, **loại
trước những từ vốn là chung của thể loại**, không thì con số phồng lên và ra kết luận sai hướng.

---

# 2. BẢN THIẾT KẾ — chín bộ phận, mỗi bộ phận chặn một lỗi ĐÃ XẢY RA

> Đây **không phải danh sách file để chép**. Dự án khác đọc phần này rồi **tự dựng bản của mình**,
> bằng công cụ của mình, cho ngách của mình. Cột giữa mới là thứ đáng đọc — **không có lỗi thì
> không cần bộ phận.** Bộ phận nào không chặn lỗi nào của bạn thì đừng dựng.

### ① Hàng rào bằng MÁY, không bằng lời dặn

| | |
|---|---|
| **Lỗi nó chặn** | AI ghi đè bản kịch bản đã chốt · AI tự phong một bản là "duyệt rồi" · khoá API bị viết vào file |
| **Vì sao phải là máy** | Luật viết trong tài liệu là **ngữ cảnh**, không phải cưỡng chế. Model có thể bỏ qua. Hook thì không thương lượng được. |
| **Bản tối thiểu** | Một script chạy trước mọi thao tác ghi; **thoát mã 2 là chặn**. Bốn luật là đủ: version bất biến · con trỏ duyệt phải do NGƯỜI đặt · bản ghi một lần chạy bất biến · chặn chuỗi giống khoá API |
| ⚠️ | Thoát mã 1 **không** chặn. Kiểm bằng cách thử ghi thật, đừng tin là nó chạy |

### ② Version BẤT BIẾN + con trỏ ĐỔI ĐƯỢC

| | |
|---|---|
| **Lỗi nó chặn** | `FINAL.txt` · `FINAL_v2.txt` · `FINAL_deAI.txt` — **ba file cùng tên FINAL và không ai biết bản nào đã sản xuất** |
| **Cách làm** | File version *(`v001`, `v002`…)* **không bao giờ sửa**. "Bản hiện tại / đã duyệt / đã đăng" là **con trỏ** trỏ vào version, con trỏ thì đổi thoải mái |
| **Vì sao hơn cách chép bản sao** | Bản sao đẻ ra câu hỏi "hai file này khác nhau chỗ nào"; con trỏ thì không |
| **Bắt buộc** | Con trỏ `đã duyệt` và `đã đăng` phải ghi rõ **người** đặt. AI không được tự đặt |

### ③ Tách ID SÁNG TẠO khỏi ID THỰC THI

| | |
|---|---|
| **Lỗi nó chặn** | Một lần gen ảnh hỏng làm **trạng thái sáng tạo của cả video** tụt hạng |
| **Cách làm** | `video` · `version` · `review` · `run` là **bốn thứ khác nhau**, mỗi thứ ID riêng và vòng đời riêng. Một `run` hỏng chỉ làm hỏng chính nó |
| **Kèm theo** | Mỗi lần chạy máy ghi lại **số mong đợi / số ra thật / có khớp không**. Ba video đã lệch số ảnh↔audio mà không ai biết |

### ④ Máy soát các BIỂU HIỆN của cùng một bản gốc

| | |
|---|---|
| **Lỗi nó chặn** | Một kịch bản đẻ ra 4 file *(lời đọc · bảng duyệt · shot · đầu vào TTS)*. Chúng **không tự đồng bộ**. Đã dính: bảng duyệt lệch **22 dòng** qua hai vòng review, không ai thấy |
| **Cách làm** | Chọn **một** file là bản gốc. Mọi file khác phải **ghép lại đúng nguyên văn** bản gốc. Chạy được bằng máy, không cần AI |
| **Áp cho việc khác** | Bất kỳ đâu có một nguồn đẻ ra nhiều dạng — bản dịch, phụ đề, mô tả, bản rút gọn |

### ⑤ Kho bản ghi ĐỐI THỦ làm vật đối chứng

| | |
|---|---|
| **Lỗi nó chặn** | Luật đúc từ trí nhớ và từ báo cáo của AI khác, không ai kiểm lại được |
| **Sức mạnh thật** | Ngày đầu dựng kho, nó **giết bốn con số** đã ghi trong kho tri thức suốt nhiều tuần, và giết luôn một kết luận do chính nó sinh ra ba phút trước |
| **Bản tối thiểu** | Công cụ kéo phụ đề gốc của cả kênh + **MỘT lệnh đo duy nhất** |
| ⚠️ **Vì sao phải MỘT lệnh** | Mỗi lần viết lại phép đo là mỗi lần chọn lại nền, và sẽ chọn khác. Đã sai **bốn lần liên tiếp** đúng vì vậy |
| ⚠️ | **Cấm mở kho khi đang viết.** Đọc chữ đối thủ lúc viết là đường ngắn nhất tới trùng lặp |

### ⑥ Bốn sổ quản trị

| sổ | lỗi nó chặn |
|---|---|
| **Nguồn chuẩn** — mỗi câu hỏi ĐÚNG MỘT file được phán | hai file cùng nói về một việc, nói ngược nhau, không file nào biết mình đã bị bác |
| **Chính sách đổi luật** — 5 điều kiện để một quan sát thành luật | quan sát một lần biến thành luật vĩnh viễn |
| **Quyết định cần chủ** — mặc định `CHỜ NGƯỜI QUYẾT` | AI tự quyết thứ đáng ra là của chủ |
| **Sổ khai tử** — luật chết ghi kèm **lý do và bằng chứng** | luật chết âm thầm rồi có người dựng lại |

### ⑦ Bản đồ tri thức 4 tầng + luật ưu tiên

| | |
|---|---|
| **Lỗi nó chặn** | 73 file nằm chung một chỗ, không ai biết đọc gì trước. Đã dính: mở nhầm file đã chết · không biết trong dự án có sẵn thứ mình đang cần |
| **Bốn tầng** | ① luật *(được quyền phán)* ② nguyên liệu *(tra, không phán)* ③ bằng chứng ④ lưu trữ |
| **Luật ưu tiên khi hai file cãi nhau** | tầng thấp thắng · **đếm tay trên nguồn gốc thắng mọi báo cáo** · cùng tầng thì file mới thắng · không xử được thì **đo lại**, đừng chọn bừa |

### ⑧ Khai tử phải làm ĐỦ HAI VIỆC

| | |
|---|---|
| **Lỗi nó chặn** | File bị thay thế mà **không tự biết**, tiếp tục bơm con số sai vào nơi khác |
| **Đã dính** | Một file đo 96 khung ra con số sai; file thay thế đo 1.090 khung. File cũ **không có biển báo** → skill vẫn trích nó suốt một tuần, và một video đã dựng trên con số sai đó |
| **Luật** | Ghi vào sổ khai tử **và** dán biển lên **dòng đầu của chính file đó**. Làm một nửa là vô dụng |
| **Nếu còn ai trích nó** | **Đừng xoá** — dán biển và để đó, không thì chỗ trích trỏ vào khoảng không |

### ⑨ Người xem lạnh phải là NGƯỜI THẬT bên ngoài

| | |
|---|---|
| **Lỗi nó chặn** | Lỗi cấu trúc: bí ẩn giả · đáp án đến sai lúc · hai chương làm cùng một việc |
| **Vì sao máy chấm không thấy** | Máy chấm **từng linh kiện**; lỗi cấu trúc là tính chất của **cả bài**. Một bản chấm 68/74 vẫn hỏng cấu trúc |
| **Vì sao tác giả không thấy** | Họ biết đáp án, nên với họ **mọi khoảng trống đều đầy** |
| ⚠️ **Vì sao subagent KHÔNG thay được** | Tài liệu chính thức Claude Code: subagent nạp **đủ** `CLAUDE.md` và project rules; chỉ Explore và Plan bỏ qua, **và không có cấu hình nào đổi được điều đó**. Viết "bạn không biết gì về dự án này" vào prompt chỉ là chữ |
| **Cách duy nhất** | Đưa cho một AI khác trong **cuộc trò chuyện mới**, hoặc người thật |

---

## Cái mà dự án khác KHÔNG nên đọc theo

Toàn bộ `kho/1..4`. Mọi con số trong đó đo trên **kênh này, ngách này, khán giả này** — và kênh
này **chưa thắng**. Ba thứ đặc biệt độc nếu bắt chước:

| | vì sao |
|---|---|
| rubric chấm kịch bản | 36 mục đúc từ **11 kịch bản**; đã có ≥6 con số bị chính kho bản ghi bác |
| khối mô tả nhân vật | chỉ đúng cho một nét vẽ |
| bản đồ lane / cụm chủ đề | dựng trên tệp khán giả riêng của một ngách |

**Cấu trúc thì học. Kết luận thì tự đo lại.**

---

# 3. PHƯƠNG PHÁP — đây mới là thứ đáng kế thừa

*Mười lăm điều dưới đây không rút ra từ lý thuyết. Mỗi điều là một lỗi đã trả giá thật trong dự án này.*

### Về ĐO

**1. Chỉ có hai loại số.** *Ràng buộc cứng* — lệch là sai, và cứng vì lý do **sản xuất** hoặc vì
**mọi mẫu đều nhất trí**. *Triệu chứng* — mọi con số còn lại. Số lệch thì **đi đọc đoạn đó** rồi
hỏi "đoạn này có dở không"; dở thì sửa vì nó dở, không dở thì để yên dù số vẫn lệch.
⛔ **Cấm sửa nội dung để con số đẹp hơn.** Ba câu mùi AI nặng nhất của một video đều là câu thêm
vào để thoả cho đủ điểm.

**2. Mọi con số phải kèm NỀN của nó.** Đo tốc độ đọc sai **bốn lần liên tiếp** trong một ngày,
không lần nào sai vì tính nhầm — cả bốn vì mỗi lần chọn một nền thời gian khác:
`từ ÷ thời lượng video` ≠ `từ ÷ độ dài audio` ≠ `từ ÷ thời gian đang nói`. Lệch nhau tới 20%.

**3. Con số NỀN sai đắt hơn luật sai.** Rubric chưng cất từ một kênh tên "Mack" mà **bốn tháng
không ai truy được Mack là kênh nào**. Luật sai thì sửa một dòng; nền sai thì mọi thứ dựng trên
nó đều phải làm lại. → Mỗi con số phải ghi: **đo trên đâu · cỡ mẫu · ngày · khi nào đo lại**.

**4. Chạy CẢ tập, đừng chọn tập con quen tay.** Đo bốn kênh nguồn của rubric → bảng 100% nhất trí.
Chạy đủ 18 kênh → lòi ra 3 ca ngược, trong đó có chính kênh được chọn làm hình mẫu.
**Tập con quen thuộc tự sinh ra sự đồng thuận giả.**

**5. Giữa-nhóm không phải trong-nhóm.** Độ dài ↔ view tương quan **+0,36 giữa các kênh** nhưng
**≈0 trong nội bộ từng kênh**, hai chiều ngược nhau. → Độ dài là **lựa chọn định vị**, không phải
chất lượng. Mọi so sánh giữa các kênh đều phải hỏi thêm: *trong một kênh thì sao?*

**6. View trung vị đo CỠ KÊNH, không đo chất lượng.** Một kênh trung vị 1,5 triệu view — hoá ra
1,49 triệu người đăng ký. Muốn so kịch bản thì phải khử cỡ kênh, hoặc chỉ so **trong** một kênh.

**7. Hai video top chiếm >80% tổng view = kênh đó TRÚNG SỐ, đừng học nó.** Đã dính: rút luật từ
một kênh trung vị 295 view mà top-2 chiếm 90%.

**8. Kho bản ghi gốc là vật đối chứng, và nó tàn nhẫn.** Ngày đầu dựng kho, nó giết **bốn con số**
mà kho tri thức đã ghi suốt nhiều tuần, và giết luôn một kết luận do chính nó sinh ra ba phút trước.
→ Số đếm tay trên bản ghi gốc **thắng mọi báo cáo**, kể cả báo cáo do AI khác sinh ra.

**9. Chỉ số tính theo ranh giới câu là vô nghĩa trên phụ đề tự động** — dấu câu do máy chấm.
Chỉ dùng: số từ · thời lượng · nhịp đọc · vị trí theo % bài.

### Về KIỂM

**10. Bộ kiểm mới ra kết quả xấu thì nghi BỘ KIỂM trước, nghi dữ liệu sau.** Lần đầu chạy bộ soát
biểu hiện: 22 FAIL — **19 trong số đó là lỗi của chính bộ kiểm** *(ba định dạng cũ khác nhau)*.

**11. Kiểm hai cổng.** Cổng đầu: *số nào đang chặn?* Cổng cuối: **đo output**, đừng tin
"chạy không báo lỗi". Đúc từ một tháng ra 365 view và một video hỏng tiếng mà không ai biết.

**12. Các "biểu hiện" của một bản gốc sẽ tự trôi khỏi nhau.** Một kịch bản đẻ ra 4 file
*(lời đọc · bảng duyệt · shotlines · đầu vào TTS)* và chúng **không tự đồng bộ**. Đã dính: bảng
duyệt lệch kịch bản **22 dòng** qua hai vòng review mà không ai thấy. → Phải có máy soát.

**13. Rubric mù trước lỗi CẤU TRÚC.** Nó chấm từng linh kiện, còn bí ẩn giả / đáp án đến sai lúc /
hai chương làm cùng một việc là tính chất của **cả bài**. Một kịch bản chấm 68/74 vẫn hỏng cấu trúc.
Và **người viết không tự chấm được** — họ biết đáp án nên với họ mọi khoảng trống đều đầy.
→ **Bắt buộc có người nghe ngoài thật.**

**14. Subagent KHÔNG lạnh.** Tài liệu chính thức Claude Code: subagent nạp **đủ** `CLAUDE.md` và
project rules; chỉ Explore và Plan bỏ qua, **và không có cấu hình nào đổi được**. Viết vào prompt
câu "bạn không biết gì về kênh này" chỉ là chữ, không phải cơ chế.
→ Lớp người-xem-lạnh **duy nhất** là đưa cho một AI khác trong cuộc trò chuyện mới.

### Về LUẬT

**15. Khai tử một file phải làm CẢ HAI việc** — ghi vào sổ **và** dán biển ⛔ lên dòng đầu chính
file đó. Làm một nửa thì lần sau vẫn có người mở nhầm. Đã dính: một file đo sai bị thay thế mà
**không tự biết**, và con số sai của nó tiếp tục chảy vào skill suốt một tuần.

**16. Đừng lấy video cũ của mình làm trần.** Câu hỏi đúng luôn là *"đoạn này đã hay nhất có thể
chưa"*, không phải *"đã bằng bản trước chưa"*.

**17. Luật hay không cứu được kịch bản dở.** Chủ, 07/08:
> *"mùi ChatGPT nhưng kịch bản hay với nhiều view thì vẫn ok hơn là kịch bản quá nghiêm khắc rồi chả có view nào."*

Khi một luật chặn một câu **hay** — nghi luật trước, đừng sửa câu.

---

# 4. THỨ TỰ DỰNG KÊNH MỚI

```
1. chép ngăn 1 + ngăn 2          nửa ngày
2. kéo kho bản ghi ngách mới     1 buổi, chạy tuần tự
3. đo bằng do.py                 dodai → wpm → tìm cụm
4. chọn đề tài từ CẦU đã có      không săn đề tài trinh nguyên
5. viết → 11 cổng → người ngoài
6. sản xuất → đăng
7. ĐĂNG ĐỦ SỐ rồi mới kết luận   xác suất 0 trúng sau N video = (1 − tỉ_lệ_trúng)^N
```

Bước 7 là bước hay bị bỏ nhất và đắt nhất. Ngách có tỉ lệ trúng 15% thì **0 trúng sau 12 video vẫn
có 14% khả năng chỉ là xui** — chưa đủ để kết luận kênh hỏng, mà đó lại đúng lúc người ta bỏ cuộc.

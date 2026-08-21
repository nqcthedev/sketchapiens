# MỔ 23 QUẢ NỔ THẬT — học cách làm thumbnail · 12/08/2026

**Cách chọn mẫu, và vì sao khác lần trước.** Bản 10/08 lấy *"4 quả cao nhất MỖI kênh"* trong
13 kênh — kể cả kênh trung vị **1 vpd**, tức "quả thắng" của nó cũng là rác. Lần này chỉ lấy
**quả nổ thật: ≥250.000 view**, ra **23 quả** *(258K → 7,83 triệu)*, tải bản **1280px**.

Ảnh gốc + 3 bảng ở `THUMB_QUANO_2026-08-12/`: `SHEET_1/2.png` *(cỡ lớn)* ·
`FEED_1.png` *(**13 thumbnail của ta TRỘN LẪN vào hàng quả nổ ở 246px** — cột 3 và 6 mỗi hàng)*.

---

## 1. 🔴 BỐN PHÉP ĐO — KHÔNG CÁI NÀO PHÂN BIỆT ĐƯỢC HAI NHÓM

| | 23 quả nổ | 13 của ta | phân biệt? |
|---|---|---|---|
| bão hoà trung vị | **36,1%** | 38,6% | ❌ |
| chữ vàng, % diện tích | **5,2%** | 6,5% | ❌ *(ta còn TO HƠN)* |
| khung có ≥2 người | 52% | 46% | ❌ |
| độ sáng trung vị | 54,9% | 66,7% | ⚠️ chỉ số này đã bị bác 03/08 |

**Đây là kết quả chính, và nó lặp lại đúng bài học cũ: đo tổng thumbnail thì vô nghĩa.**

### Ba thứ trong kho bị bác bằng bảng này

- ⛔ **Trần bão hoà "23-27%"** → thật ra **36,1%**. `SAT_CEILING` trong `identity/style.py`
  đang ép *"desaturated, nothing vivid"* — **kéo ngược**. Đã sửa 12/08.
- ⛔ **"Kênh mình luôn một người lẻ"** *(memory `thumbnail_teardown_capkhop`)* → **46% khung
  của ta có ≥2 người**, gần bằng quả nổ. Bỏ.
- ⛔ **"Chữ của ta nhỏ hơn"** → sai, ta **6,5%** vs quả nổ **5,2%**. Tôi tưởng vậy khi nhìn
  bằng mắt; đo mới biết ngược. Đừng đặt chỉ tiêu cỡ chữ.

---

## 2. ✅ THỨ THẬT SỰ KHÁC — chỉ hiện ra khi ĐỌC ảnh, không đếm được

### A. VẬT KỂ CHUYỆN — to, cụ thể, và ĐANG GÂY CHUYỆN

Mỗi quả nổ có **một vật** đủ to để nhận ra ở 246px, và vật đó **tự kể một câu chuyện**:

| quả | vật kể chuyện |
|---|---|
| `WHY ONLY SOME?` 368K | **khay trứng gà** đặt cạnh **bốn quả trứng lạ** lốm đốm |
| `WHY ROTTEN?` 504K | **nguyên con bò** cạnh đĩa thịt đỏ ‖ **con gấu** cạnh đĩa thịt mốc xanh |
| `FIRST GUN?` 451K | **khẩu súng kíp** dài bằng nửa người |
| `RAIN AGAIN?` 355K | **cái lều dột** đang chảy nước thành dòng |
| `−40°/+20°` 1,93M | **giàn hang cắt đôi** như sơ đồ, ghi hai nhiệt độ |
| `THE FIRST WHITE PEOPLE?` 291K | **năm người xếp hàng**, màu da nhạt dần từ trái sang phải |

Của ta: **cái tất · bàn chải · viên sỏi · bàn chân · con cá**. Nhỏ, và phần lớn là
**đồ hiện đại** — đúng cái luật `⛔ không đồ hiện đại` đã cấm *(8/13 quả vi phạm)*.

👉 Khớp với luật **CENTRE ANCHOR** đã có ở `PROMPT_TONG_Thumbnail_v6.md`: **tâm khung dành cho
VẬT KỂ CHUYỆN.** Bộ 23 quả này là bằng chứng mạnh nhất từ trước tới nay cho luật đó.

### B. NƠI CHỐN — người xem biết ngay đang ở đâu

Quả nổ gần như luôn đặt trong một **nơi chốn dựng đủ**: trong hang có lửa cháy hắt lên vách ·
giữa sa mạc có xương rồng · dưới mưa xiên trắng · đồng cỏ hoàng hôn có lều xa xa.
Của ta có nhiều khung là **hai cái mặt cận trên nền trống**.

⚠️ **Mức tin cậy: quan sát, chưa có đối chứng.** Có quả nổ đi ngược hẳn —
`WHO ARE YOU?` **1,87M** chỉ là *một người que tí xíu trên nền vàng trơn*, và
`Zenn` **4,02M** chỉ là *một con mắt vàng trên nền đen tuyền*. Đừng biến thành cổng chặn.

### C. BIỂU CẢM KHÔNG PHẢI LÚC NÀO CŨNG SỢ

`FREE ALL DAY` 3,12M · `COZY ALL DAY?` · `ANCIENT SLEEP SECRET` — **cười, thư giãn, ngủ ngon**.
Nhắc lại luật đã chết từ 10/08: *"mặt phải đang khổ"* — sai, và bộ này xác nhận lần nữa.

---

## 3. KẾT LUẬN THẲNG

**Thumbnail của ta không yếu về TAY NGHỀ.** Trộn vào hàng quả nổ ở cỡ feed *(`FEED_1.png`)*
thì không quả nào lạc: cùng nét, cùng người que trắng, cùng khuôn chữ vàng.

**Nó yếu ở chỗ khác:** nó đang khai báo **một đề tài thuộc lane đã chết** *(`STILL RUNNING?` ·
`INSIDE YOU?!` · `YOU SEE IT?` · `FISH IN THERE?` — mismatch cơ thể bạn)*, và **tâm khung
không có vật kể chuyện nào của thế giới cổ đại**.

Đây đúng là **L1** — luật duy nhất sống sót qua 13 kênh ngày 10/08:
> *thumbnail chỉ đang khai báo đề tài; thứ tách 3.868 vpd khỏi 1 vpd là VIDEO NÓI VỀ CÁI GÌ.*

### Việc rẻ nhất vẫn chưa làm

**Test & Compare** — YouTube cho chạy 3 thumbnail trên cùng một video và trả về CTR từng bản.
Đó là cách duy nhất đo CTR thật thay vì suy từ view. Không tốn gì ngoài công dựng ảnh.

### Không lấy được, phải nói rõ

**CTR của đối thủ không ai xem được** ngoài chủ kênh đó. Mọi kết luận ở đây suy từ **view**,
mà view chịu ảnh hưởng của đề tài + tuổi kênh + thuật toán đẩy. Nexlev chỉ nối được kênh
`EPIC WILDERNESS COOKING`, không nối Sketchapiens, nên **CTR từng video của ta cũng chưa có
trong tay** — chủ đọc trong YouTube Studio thì mới đo được cặp khớp thật.

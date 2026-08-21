# CHẤM KỊCH BẢN — Ngách "Người Que Cổ Đại"

> # 🔴 ĐỔI KIẾN TRÚC 09/08/2026 — BỎ THANG ĐIỂM
>
> Bản cũ: **37 mục × 2 điểm, ngưỡng 86%** → phải đạt điểm tối đa ở **~32/37 mục**.
> Đó không phải "viết hay là qua". Đó là **điền đủ 32 ô**.
>
> Chính file này đã ghi hậu quả: *"ba câu mùi AI nặng nhất trong V17 đều là câu thêm vào
> để thoả Tầng A."*
>
> **Bản mới có hai tầng, và chỉ một tầng chặn được việc đăng:**
>
> | | | |
> |---|---|---|
> | **PHẦN 1 — CỔNG** | ít, thật, **đạt/không đạt** | chặn đăng |
> | **PHẦN 2 — GỢI Ý NGHỀ** | nhiều, **KHÔNG chấm điểm** | đọc **SAU** khi viết xong |
>
> ## Viết trước. Đối chiếu sau. Thấy thiếu chỗ nào hay thì thêm.
> ## ⛔ Không mở file này ra rồi điền.

---

## LUẬT 0 — CHỈ CÓ HAI LOẠI SỐ. ĐỪNG LẪN.

**Loại 1 — RÀNG BUỘC CỨNG.** Lệch là sai, không bàn. **Chỉ có ba, và cả ba là lý do sản xuất:**

| | vì sao cứng |
|---|---|
| Dấu `!` = **0** | 14/14 winner nhất trí |
| Gạch ngang `—` giữa câu = **0** | TTS đọc vấp |
| **Mỗi câu một dòng** | mỗi dòng = 1 shot ảnh + 1 khối TTS |

**Loại 2 — MỌI CON SỐ CÒN LẠI là TRIỆU CHỨNG, không phải đích.**
Độ dài · nhịp đọc · you:we · % câu ngắn · dài câu TB · mật độ giác quan · số câu hỏi ·
mỏ neo/phút · nhịp hài · số cặp cài-lật — **tất cả**.

**Cách dùng:** số lệch thì **đi đọc đoạn đó**, rồi hỏi *"đoạn này có dở không?"*
Dở → sửa vì nó dở. Không dở → **để yên**, dù số vẫn lệch.

⛔ **Cấm sửa một câu để con số đẹp hơn.**

🔴 **Chủ chốt 07/08:** *"mùi ChatGPT nhưng kịch bản hay với nhiều view thì vẫn ok hơn là
kịch bản quá nghiêm khắc rồi chả có view nào."* → Khi một luật ở đây chặn một câu **hay**,
**nghi luật trước**, đừng sửa câu.

### Sổ số đã chết
*giác quan 7-9% · mỏ neo 3,2-5,1/phút · you:we 1,5-2 · độ dài 9-12 phút · nhịp hài 30-60
giây · `I ≈ 0` · mọi tỉ lệ hình · ≥4 cặp cài-lật · cặp đầu↔cuối · thang bằng chứng 5 bậc ·
mỏ neo yếu sau 85% · chương thừa trước 50%.*
Bằng chứng: `../../governance/RETIRED_RULES.md`. **Đừng dựng lại chúng.**

---

# PHẦN 1 — CỔNG

*(Số hiệu cổng ở đây **độc lập** với hệ 0-11 của `FLOW_VietKichBan_11Cong.md`. Bảng đối chiếu:)*

| cổng ở file này | trong `FLOW_VietKichBan_11Cong.md` |
|---|---|
| **1** sản xuất | cổng 7 *(đo bằng máy)* + cổng 11 *(kiểm bản dựng)* |
| **2** sự thật | cổng 4 *(mỏ neo)* |
| **3** sống còn của kênh | **cổng A** *(quét tự-trùng-lặp)* |
| **4** người nghe ngoài | **cổng 10** |

Ít. Mỗi cổng có **một lý do cụ thể** chứ không phải "đối thủ hay làm thế".
Đạt/không đạt, không có điểm.

## Cổng 1 — SẢN XUẤT *(máy móc, không bàn)*

**Ba ràng buộc cứng của LỜI ĐỌC** — đúng ba cái ở LUẬT 0, không hơn:

- [ ] Dấu `!` = 0
- [ ] Không có gạch ngang `—` giữa câu
- [ ] Mỗi câu một dòng

**Một phép kiểm của BẢN DỰNG** — không phải ràng buộc của lời đọc, nhưng chặn đăng:

- [ ] **Ghép toàn bộ shot == narration nguyên văn** *(chạy `tools/validate_shots.py`)*

> ⚠️ **Đừng đếm bốn ô này thành "bốn ràng buộc cứng".** Ba ô đầu là luật của **câu chữ**;
> ô thứ tư là phép kiểm của **file dựng**. Nhầm hai thứ đó chính là lỗi đã lan ra ba file
> khác *(`/apply-review` · `/audit-script` · `qa_kichban.py` đều từng ghi "4 ràng buộc
> cứng", và cái thứ tư chúng nghĩ tới là `I ≈ 0` — một luật đã chết)*.
>
> Phép kiểm bản dựng **chưa bao giờ chạy** ở V17 và V19 vì tên file mặc định sai. Nó là
> phép kiểm quan trọng nhất trong cả cổng: sai nó thì **TTS đọc một kịch bản khác với kịch
> bản đã duyệt**.

> ## ⛔ TRƯỢT CỔNG THÌ LÀM GÌ
>
> | cổng trượt | việc |
> |---|---|
> | **1** ba ràng buộc lời đọc | sửa câu, chạy lại. Máy: `.claude/skills/sketchapiens-bien-tap/qa_kichban.py` |
> | **1** ghép shot ≠ narration | ⛔ **DỪNG, chưa gen ảnh.** Sửa ở `shot_data.py` *(nguồn)*, không sửa file sinh ra |
> | **2** mỏ neo không tra được | **cắt câu đó.** Không hạ giọng thành "researchers suggest" để giữ lại — đó là cách bịa có vỏ |
> | **2** số tự mâu thuẫn | sửa số, hoặc cắt một trong hai |
> | **3** trùng đối thủ / trùng video mình | **viết lại đoạn đó**, đừng đổi vài chữ. Trùng ở tầng NHỊP thì đổi chữ không cứu được — xem khối V18/V19 dưới |
> | **4** người nghe ngoài không kể lại được bài | ⛔ **lỗi XƯƠNG.** Đừng vá câu. Quay lại bộ xương chương |
>
> **Trượt cổng 2 hoặc 3 = không đăng.** Trượt 1 = không gen ảnh. Trượt 4 = không chia shot.

## Cổng 2 — SỰ THẬT

- [ ] Mọi mỏ neo **tự tra được nguồn**, không lấy từ NotebookLM *(tỉ lệ sai 7/10)*
- [ ] Suy diễn của tác giả nguồn **ghi rõ là suy diễn**, cấm nói như sự thật.
      ⚠️ **Đổi chữ mỗi video**, đừng dùng lại một cụm — nó sẽ thành tật của kênh
- [ ] **Số trong bài không tự mâu thuẫn**

> Cổng cuối cùng thêm 09/08 sau khi đọc trọn hai bài đối thủ:
> Ink 1,10M gọi dây thừng **5.200 năm** là *"the oldest direct evidence of string ever
> found"* rồi **hai dòng sau** dẫn dụng cụ xe dây **35.000 năm**.
> Ink 272 vpd nói *"200.000 năm đầu"* rồi *"phải mất thêm 200.000 năm nữa"* — cộng lại
> vượt tuổi loài; và tuyên *"the knowledge is 100.000 years old"* trong khi bằng chứng đưa
> ra là văn bản 1500 TCN, **thổi lên 28 lần**.
>
> ⚠️ Cả hai bài vẫn triệu view / vẫn sống. **Độ chính xác không giữ chân người xem.**
> Ta vẫn tra, vì chính sách YouTube 16/07/2026 chấm kênh theo *"có thêm hiểu biết và góc
> nhìn gốc"* — đó là lý do sống còn, không phải lý do chất lượng.

## Cổng 3 — SỐNG CÒN CỦA KÊNH 🔴

- [ ] **Không trùng đối thủ** ở: trình tự beat · ví dụ · đùa · ẩn dụ · cú bẻ lái.
      *(Trùng ĐỀ TÀI thì được. Trùng những thứ trên là reused content.)*
- [ ] **Không trùng video trước của CHÍNH MÌNH** — chạy CỔNG A trong
      `../2_nguyenlieu/VAULT_AncientHumans_KnowledgeVault.md` §4

- [ ] **Có ít nhất MỘT thứ mà bầy clone không có** — góc kể riêng · mỏ neo chưa ai dùng ·
      kết cấu riêng. *(Đo 05/08: mọi đề tài tra ra ~20 kênh mở bài gần trùng nhau. V18 của
      mình mở bằng "Tonight you will go to bed behind a door that locks." — **cùng khuôn**.)*

> ⚠️ **Vế thứ ba trước 09/08 KHÔNG THUỘC CỬA NÀO.** `CHINHSACH_YOUTUBE_2026_AnhHuong.md`
> L146 ghi *"luật thêm vào cửa 1"*, nhưng cửa 1 đã bị rút gọn cùng ngày → grep toàn kho ra
> đúng một kết quả là chính dòng đó. Cổng chống **inauthentic content** — thứ đang dọn sạch
> cả ngách — treo lơ lửng nhiều ngày.

> # 🔴 CỔNG NÀY ĐÃ TỪNG CÂM, VÀ ĐÓ LÀ LÝ DO V19 CHÉP V18
>
> Lệnh grep của CỔNG A trỏ vào `Video1[0-9]*/` thay vì `videos/`. **Và nó có HAI BẢN SAO** —
> `FLOW_VietKichBan_11Cong.md` L67 và `WORKFLOW_Production.md` L120. Bản trong WORKFLOW còn sai
> nặng hơn: `Video1[5-8]*/` — **bỏ sót V19 hoàn toàn**, tức đúng video cần quét. zsh trả `no matches found` → **grep không chạy,
> không in gì, không báo lỗi** → người dùng đọc thành *"sạch"*.
>
> Chạy đúng đường thì cụm `on the safe side` hiện ra ở **cả V18 lẫn V19**. Cổng **bắt được**,
> nó chỉ chưa từng được chạy. *(Đã vá 09/08.)*
>
> **Và grep từ khoá vẫn chưa đủ — nó mù ở tầng BEAT.** Phải đọc bằng mắt:
> | V18 câu cuối | *"And they will still be listening, on the safe side of a locked door."* |
> |---|---|
> | V19 câu cuối | *"And you are still walking a little faster, on a cold floor, on the way to bed."* |
>
> **0 từ khoá trùng. Cùng một nhạc cụ.** `MONEO_V19` L251 đã cấm đích danh `"locked door"` —
> lệnh cấm hẹp hơn thứ cần cấm, nên cái khung quanh nó lọt.

## Cổng 5 — KỊCH TÍNH 🔴 *(thêm 18/08/2026)*

```
python3 tools/do_kich_tinh.py <kịch_bản.txt> dem_lanh
```

- [ ] **chữ chỉ CÁI CHẾT** ≥ 60% mức của quả nổ khớp cặp
- [ ] **gọi thẳng người xem** ≥ 60% mức đó
- [ ] **vật thể cụ thể** ≥ 60% mức đó
- [ ] **nguy hiểm xuất hiện** không muộn hơn quả nổ quá 5% độ dài bài

> ### 🔴 VÌ SAO PHẢI CÓ CỔNG NÀY — bốn cổng kia đều xanh mà bài vẫn nhạt
>
> V20 bản 1 **qua cả bốn cổng**: sản xuất sạch · mỏ neo đủ DOI · 0 cụm trùng ·
> người nghe ngoài nói đúng luận đề và xem hết. Rồi chủ nghe bản dịch tiếng Việt
> đặt cạnh Axen 756K và nói: **"nghe kịch bản đối thủ vẫn hay hơn."**
>
> Đo ra ngay:
>
> | | bản 1 | Axen 756K |
> |---|---|---|
> | chữ chỉ cái chết | **2** | ~19 |
> | gọi thẳng người xem | **0** | ~51 |
> | nguy hiểm lần đầu | **44% bài** | **2% bài** |
>
> **Bốn cổng cũ đo được mọi thứ trừ thứ giữ chân người xem.** Cổng 1 kiểm sản xuất.
> Cổng 2 kiểm sự thật, **và nó đẩy người viết về phía rào đón**. Cổng 3 kiểm trùng lặp,
> **và nó đẩy người viết RA XA những nước đi đã chứng minh là ăn**. Cổng 4 hỏi
> *"người lạ có nói lại được luận đề không"* — đó là **hiểu**, không phải **thích**.
>
> ⚠️ **Cổng này KHÔNG có ngưỡng tuyệt đối.** Mọi con số là **tỉ lệ so với MỘT quả nổ
> cùng ô**, khai trong `schemas/moc_kich_tinh.json`. Không có cặp đối chứng thì cổng
> không chạy — đó là cố ý, vì kho đã bốn lần đẻ luật từ mẫu quá nhỏ rồi phải giết lại.

### 📏 HEDGE CÓ NGÂN SÁCH — tối đa MỘT khối thành thật

V20 bản 1 tự thú *"chưa chắc"* **ba lần**; Axen **một lần**. Trung thực ba lần **không**
nghe ra là cẩn thận, nó nghe ra là **rụt rè**. Giữ nguyên yêu cầu thành thật của Cổng 2,
nhưng **gom về một chỗ, nói một lần, rồi đi tiếp**.

### ⛔ ĐỌC LẠI CHO ĐÚNG: "register không dự báo view"

Câu đó nghĩa là **mấy dấu hiệu bề mặt đã đo** *(nhịp hook, mật độ mỏ neo, bão hoà, độ dài)*
**không phân biệt được** quả nổ với quả chìm. Nó **KHÔNG** có nghĩa là *kịch tính không quan
trọng*. Lấy nó làm cớ để thôi tối ưu cho mọi thứ ngoài sự chính xác là **đọc sai**, và đó
chính là cách V20 bản 1 ra đời.

---

## Cổng 4 — NGƯỜI NGHE NGOÀI *(bắt buộc khi đổi cấu trúc)*

- [ ] Một người/AI **chưa biết đáp án** nghe hết bài và nói lại được bài chứng minh gì

> **Người viết không tự chấm được cấu trúc** — họ biết đáp án nên với họ mọi khoảng trống
> đều đầy. Đã dính hai lần: V17 chấm 68/74 vẫn hỏng cấu trúc · V19 sạch 7 mục cứng vẫn xây
> trên một bí ẩn không tồn tại.
>
> 🔴 **Subagent KHÔNG lạnh** — nó nạp đủ `CLAUDE.md` và project rules. **Review ngoài bằng
> ChatGPT chat mới là lớp người-xem-lạnh DUY NHẤT.**
>
> **Dán gì cho người review:** ⛔ cấm dán **CHIẾN LƯỢC · RUBRIC · SỐ ĐẾM** *(nạp luật vào là
> bịt mắt — họ sẽ chấm theo luật thay vì nghe bài)*. ✅ phần **TAY NGHỀ** thì được dán.

---

# PHẦN 2 — GỢI Ý NGHỀ

> ## ⛔ KHÔNG CHẤM ĐIỂM. KHÔNG CÓ NGƯỠNG. KHÔNG PHẢI DANH SÁCH ĐỂ ĐIỀN.
>
> **Đọc sau khi bản nháp đã xong.** Thấy chỗ nào bài mình yếu hơn thì sửa vì nó yếu —
> không phải vì thiếu ô.
>
> Toàn bộ phần này đúc từ đối thủ. Nghĩa là nó mô tả **register của ngách**, và
> **register không dự báo view** — xem khối bằng chứng cuối file.

### 2.1 Hook

Vào thẳng cảnh cụ thể, 1-2 câu. Không "hi guys", không intro kênh.
Dựng một nghịch lý hoặc mối đe doạ, rồi thả câu hỏi lõi **khi nó tự đến**.

⛔ **Bỏ mốc "trước giây 31"** — n=3, và `../3_bangchung/TONGHOP_16Kenh_2026-08-09.md` đo
**ngược dấu**: nhiều kênh nhóm CHÌM hỏi SỚM hơn, PrimalGlitch hai bài đỉnh **0 dấu hỏi cả
bài**, quả 769K của Ink đặt câu hỏi lõi ở **1:06**. *(Số cũ: Eating 11 · Smoking 18 ·
Predators 31 — triệu chứng, không phải đích.)*

⚠️ **Hook là SÀN, không phải con hào.** Bài chìm 272 vpd của Ink có đủ **năm nhịp hook**,
sạch y như bài 1,10 triệu cùng kênh. Đừng mài hook để mong nó nổ.

⛔ **Đã chết:** tự giễu loài người *(0 ca thắng toàn kho; BrightPsycho 0/96)*.

### 2.2 Xương bài

Có **ba kiểu xương**, cả ba đều thắng:

> **Kiểu thứ ba — THANG THỜI GIAN** *(cứu 10/08 từ `CONGTHUC_InkExplainer_BestOf.md` trước khi xoá file đó)*
>
> Không chia chương theo **chủ đề**, mà theo **mốc thời gian lùi dần về hiện tại**.
> Bài rượu **769K** của Ink Explainer: `10 triệu năm → 13.000 → 12.000 → 9.000 → 5.000`.
> Mỗi mốc một chương. Người xem luôn biết mình đang ở đâu, và luôn có lý do đi tiếp
> *(mốc sau gần mình hơn)*. Trước khi kết có một khối **đọc lại cả thang**:
> *"So here's the full picture…"*
>
> Số đo của chính bài đó: **1.000 từ · 6:04 · ~165 wpm** · đề tài lộ ở **giây 9** ·
> câu hỏi lõi mãi **1:06** · dấu `!` = 0 · và **`"I"` xuất hiện 1 lần mà vẫn 769K**.
>
> ⚠️ **Kênh đó nay đã bị TẮT KIẾM TIỀN** *(tra live 10/08, chủ cho biết vì reused content)*.
> Kỹ thuật xương bài trên **không dính** tới lý do đó — nhưng đừng lấy kênh này làm hình mẫu
> tổng thể nữa. Xem `gotcha_inkexplainer_tat_kiem_tien`.

| kiểu | cách chạy | ví dụ |
|---|---|---|
| **Bí ẩn** | mở một câu hỏi thật, nuôi qua các chương, lật ở cuối | 5/6 bài triệu view |
| **Định nghĩa lại** | **nói toạc luận đề ở phút 1**, rồi định nghĩa lại dần thứ người xem tưởng đã hiểu, rồi **bẻ gãy chính cái thang mình vừa dựng** | Ink Rain 1,10M |

⛔ **Đừng ép bí ẩn.** Khi đề tài không có bí ẩn thật, đi kiểu hai. **V19 hỏng vì bịa ra một
bí ẩn không tồn tại.**

⚠️ Và rủi ro thật không phải "thiếu bí ẩn" mà là **chạy một bí ẩn đã có đáp án nổi tiếng** —
Zenn Dogs dựng cả bài quanh thí nghiệm cáo bạc Belyaev *(có trong mọi sách phổ thông)*,
viết rất sạch, chìm **214×**. Nó thuật lại một câu hỏi đã đóng.

**Câu hỏi chẩn đoán đáng giá nhất — hỏi từng chương:**
> ## Xoá sạch chương này thì lập luận gãy ở đâu?

Không trả lời được = chương thừa. Và: **chương nào thay thế được cho nhau thì không chương
nào chịu lực** — Stickly Drink *(71 vpd, chìm 552×)* có ba chương kumis/chicha/rượu cọ đổi
chỗ được cho nhau, và **tự khai đang lặp ba lần**.

⚠️ Đừng đếm. Phép đếm chương thừa **không lặp lại được giữa hai người đọc** — hai người
cùng định nghĩa đếm cùng một bài thắng ra 1 và 2, vị trí lệch hẳn. Dùng **câu hỏi**, đừng
dùng ngưỡng.

⛔ **Đã chết:** *"chương thừa phải nằm trước 50%"* — bài THẮNG Ink Rain đặt nó ở **81,9-91,7%**.

### 2.3 Nối chương

Ba cơ chế đối thủ dùng *(10/16 kênh)*:
① giải pháp vừa nêu **đẻ ra vấn đề mới** · ② phủ định độc quyền `X wasn't the only Y` ·
③ mở chương gắn `because` để bán lại lý do nghe tiếp.

Hình dạng mối nối *(9/16 kênh, 0 kênh làm ngược; đo 157 mối nối)*: câu **đóng** chương cụt
**~9 từ** → câu **mở** chương dài hơn **~1,5 lần**. Đây là **hình dạng**, không phải đòn bẩy.

**Re-hook** *(mở chương bằng câu hứa món ngon hơn)* và **bucket brigade** *(câu nối cực ngắn
đặt ngay trước một dữ kiện nặng)* vẫn là nghề — kho câu ở
`../2_nguyenlieu/NganHang_ReHook_BucketBrigade.md`.
⛔ Nhưng **bỏ hai con số "mỗi 60-90 giây" và "mỗi 20-30 giây"**: cùng loại số đã chết ba lần,
và đặt đúng chỗ quan trọng hơn đặt đủ số lần.

⛔ **Đã chết:** cliffhanger / cọc "để dành cuối" — grep 8 cụm hứa-hoãn ra **0 tuyệt đối ở
14/16 kênh**. Zenn có đúng 1 bài dùng, bài đó **nhóm THẤP**.

### 2.4 Giọng

Câu ngắn đanh xen câu dài. Nối bằng `but`/`therefore`, không `and then` phẳng.
Contractions. Vẽ hình sờ được thay vì nói khái niệm. Danh từ cụ thể-bất ngờ thay
`very`/`amazing`. Con số chính xác thay "rất nhiều".

**Người dẫn ĐƯỢC có ý kiến riêng** — `I ≈ 0` đã chết *(9/12 kênh có phép so sạch cho thấy
bài dùng "I" ăn hơn; Mack 9,18×)*.

**Ngôi kể: VỊ TRÍ, không phải mật độ.** Ba khuôn đều thắng:

| khuôn | bài |
|---|---|
| **chữ U** — `you` đậm 0-8% → ngôi ba lạnh → tái nhập ở ~54% | Zenn Night 7,83M · Ink Rain 1,10M |
| **ngôi hai xuyên suốt** | Axen 3,12M · Stickly 2,08M |
| **ngôi ba tuyệt đối + hai từ ở 97%** | **Calhoun 4,02M — `you` = 0, `I` = 0** |

⛔ **Đã chết:** tỉ lệ `you:we 1,5-2` · nhịp hài mỗi 30-60 giây *(hai bài cao nhất kho —
7,83M và 4,02M — **không có một câu đùa nào**)* · mật độ từ giác quan 7-9%.

### 2.5 Mỏ neo

**Khuôn nén** *(7/16 kênh, 0 ngược)*: gói trọn vào **MỘT câu**, chức danh nghề đứng **trước**
tên riêng. ⛔ Không `Dr.`, không `Professor`, không `a study found` trống không.
- `In [năm], [chức danh] [Tên Họ] at [Trường] + [động từ] (+ published a paper in [Tạp chí])`
- `In [ĐỊA DANH], researchers found [HIỆN VẬT] (+ niên đại)`

⛔ **Đã chết — cấm mở lại hồ sơ:** **mật độ mỏ neo**. Zenn bài **4,02 triệu view có 1,22 mỏ
neo/1000 từ, thấp thứ nhì tháng**. SuperJoy hai bài dày mỏ neo nhất kho đều nửa dưới bảng.
Và **Axen chép lại cả 5 mỏ neo** của bài thắng → ăn **kém 67,5 lần**.

Cũng đã chết: **thang leo 5 bậc theo độ khó chối** *(Zenn Dogs chạy 16 nấc không tụt, chìm
214×)* và **mỏ neo yếu nhất đặt sau 85%** *(rút từ đúng một bài; Axen THẮNG đặt mỏ neo MẠNH
nhất ở đó — luật có thể viết ngược dấu)*.

### 2.6 Kết

Trả lời thẳng câu hỏi tiêu đề, kể cả khi đáp án là *"chưa ai biết chắc"*.
**Câu cuối là câu KHẲNG ĐỊNH**, không phải câu hỏi, và chứa **một vật thể hoặc hành động
cụ thể** — cấm kết bằng "di sản / hành trình / bản chất con người".

> Bằng chứng cho vế "không kết bằng câu hỏi": Mack **0/52** · SuperJoy 9/9 khẳng định ·
> Zenn 1/28 · Paint It Simple bài duy nhất kết bằng hỏi = **1.060 view, gần đáy** ·
> **Ink Explainer bài kết bằng câu hỏi = 272 vpd, ĐÁY kênh** *(xác nhận độc lập bằng đọc trọn)*.

Đoạn kết được phép **nạp một hình mới** — Zenn Night thả hình Ngân Hà ở 94-100%, thứ chưa
từng có trong thân bài. Nó không phải bằng chứng, nó là hình ảnh.

⚠️ **L5: đoạn kết viết hay KHÔNG cứu được bài.** Mack có 4 đoạn kết đẹp nhất kho, **cả 4
nằm nhóm đáy**. Giám khảo: *"đọc đoạn kết mà đoán view thì đoán ngược."*

⛔ **Đã chết:** callback hook *(Stickly 47/47, Zenn 28/28 — bài 298 vpd callback sạch y như
bài 7,83 triệu)* · bookend *(cùng lý do)* · cú xoay "họ→bạn" ở 88-93% *(Calhoun 4,02M có
`you` = 0)*.

### 2.7 Cài và lật

Nghề thật, cứ làm — **nhưng đừng đếm nó rồi tưởng mình hơn ai.**
5 bài chìm đếm được **8·11·11·9·13 cặp**, trung bình **10,4 — vượt trần 8 của bài thắng**.
5/5 có cặp bắc câu đầu tới câu cuối, hai bài có **hai** cặp.

12 loại kèm trích nguyên văn: `../2_nguyenlieu/KHO_CaiVaLat_12Loai.md`.
Ba loại **"im lặng"** *(L3 hai-con-số · L5 tả-trước-tên-sau · L10 bệnh-và-thuốc-không-chung-từ)*
kênh mình chưa từng làm — **chưa đo bên nào**, giữ vì chưa bị bác chứ không phải đã chứng minh.

Một luật con vẫn đáng theo: **cấm mở chương bằng thuật ngữ.** Calhoun **4/4 khái niệm** đều
được tả trước, gọi tên sau, cách nhau tới 20% thời lượng.

### 2.8 Phép thử người xem tự chạy được — **nên có, KHÔNG chặn đăng**

Một câu ở **85-95%** bảo người xem **làm một việc** hoặc **tự tính một con số trên đời họ**.
Động từ sai khiến, không phải lời mời tưởng tượng.

**Đây là chiều duy nhất trong 11 bài đọc trọn có dấu hiệu tách thắng khỏi chìm: 5-6/6 vs 1/5.**
Cặp Axen sạch nhất *(hai bài chung Chauvet + Blombos + Wiessner, lệch 1% số từ)*: thắng có một
câu như thế ở 89-90%; chìm có **0 câu trong 1.554 từ**.

⛔ **Câu gốc của Axen nằm ở `../2_nguyenlieu/KHO_CauMau_DoiThu_DungChep.md` — đọc ở đó để hiểu
hình dạng, đừng chép.** Nó là câu riêng của một kênh *(1/488 bản ghi)*, loại nguy hiểm nhất
khi chép. Hình dạng cần lấy: **một con số về CHÍNH ĐỜI người xem, họ tự kiểm được, đặt gần cuối.**

⚠️ **Vì sao nó KHÔNG được làm cổng** *(dù từng là Cổng 4 sáng 09/08)*: p ≈ 0,08, một phản ví
dụ mỗi phía — Zenn Dogs CÓ mà chìm 214×; Ink Rain có thể KHÔNG mà thắng 1,10M.
`../../governance/RETIRED_RULES.md` cấm thẳng việc dùng nó chặn đăng. Một mục vừa nằm ở phần
"chặn đăng" vừa tự khai "không chặn đăng" là **cổng giả** — đã gỡ.

⚠️ Và nó **va với §2.6**: cú xoay "họ→bạn" ở 88-93% đã chết *(Calhoun 4,02M có `you` = 0)*.
Nếu làm, làm ở dạng **con số về đời người xem**, đừng làm ở dạng xoay ngôi.

> ## 🔴 §2.6 VÀ §2.8 TRANH NHAU CÙNG MỘT CHỖ — 10% cuối bài
> §2.6 đòi **câu cuối là khẳng định, chứa vật thể cụ thể**. §2.8 đòi **phép thử người xem
> ở 85-95%**. Cả hai nhắm vào cùng vài câu cuối, và trong V19 đó **đúng là cùng một khối**
> *(dòng 119-122 là phép thử, dòng 126 là câu cuối)*.
>
> **Thứ tự đúng: phép thử TRƯỚC, câu cuối SAU.** Phép thử là việc người xem làm; câu cuối
> là điều họ mang đi. Đảo lại thì câu cuối biến thành lời dặn dò, và bài mất cú chốt.
> Đừng cố nhét cả hai vào một câu.

### 2.9 Vượt đối thủ

Ngách này khán giả chê nhiều nhất: *"AI slop + sai fact"* — một bình luận *"chatGPT writing"*
được **4,2K like**. Bốn đòn còn đứng:

| | |
|---|---|
| **Fact chính xác + micro-cite** | search verify MỌI mỏ neo, nói rõ chỗ khoa học chưa chắc |
| **Nhất quán nhân vật** xuyên video | nhân vật đối thủ "trôi" giữa các cảnh; ta khoá bằng `identity/style.py` |
| **Chống văn AI** | đọc to từng câu — câu nào "không người dẫn nào nói thế" thì viết lại |
| **Cắt lan man** | mỗi câu một ý, câu sạch TTS |

⛔ **Đã chết:** *"nhân vật dẫn có cá tính"* — persona **0 ca thắng toàn kho**, BrightPsycho 0/96.

---

## 📋 DANH SÁCH CHỜ ĐO — chưa phải luật, cấm đưa vào cổng

Bốn giả thuyết sống sót sau phép đối chứng. Cả bốn đứng ở **3-4/5 phía chìm** và **chưa ai
đo phía thắng**.

| giả thuyết | tỉ lệ | bằng chứng |
|---|---|---|
| **Vòng lặp mở còn treo sau mốc 20%** | 3/5 | Axen CHÌM: cả **3 dấu `?` trong 7,6% đầu**, 92,4% còn lại không dấu hỏi nào. Axen THẮNG: 5 dấu hỏi rải tới 65,3% |
| **DANH MỤC hay LẬP LUẬN** | 3/5 | Axen chìm có **8** chuyển chương chỉ đứng được nhờ mốc thời gian; thắng có **1**. Người đọc Mack chìm: *"bài không đi tới đâu cả, nó chỉ phình ra"* |
| **Đuôi bài lặp lại hay mở đất mới** | 3-4/5 | Ink chìm hạ cánh kết luận ở **88,4%** rồi nói lại đúng ý đó hai lần nữa; Axen chìm 87,5-100% **zero mỏ neo** |
| **Hoá đơn đặt vào ĐỜI người xem, không vào một thiết chế** | 4/5 | = mặt kia của §2.8 |

**Cách đo tiếp — rẻ, một buổi, không cần dữ liệu mới:** chạy ba phép đếm đầu trên cả 6 bài
thắng đã có transcript.

---

## 🔴 ĐIỂM SỐ ĐO ĐƯỢC GÌ — và vì sao bản này bỏ thang điểm

Bóc 16 kênh cho **L3**: cùng một kênh, cùng khuôn hook, cùng khuôn title, cùng bút pháp →
view chênh **42 đến 1.938 lần**.

| kênh | hai bài giống hệt nhau về cách viết | chênh |
|---|---|---|
| SuperJoy | 9 bài / 37 ngày, cùng giọng cùng bộ xương | **1.938×** |
| PaintItSimple | hai bài cách nhau **2 ngày**, cùng chữ `CRAZIEST` | 304× |
| **Axen** | bài chìm chép lại **cả 5 mỏ neo** của bài thắng | **67,5×** |
| NeonRush | hai bài cách nhau **1 ngày**, cùng bộ xương | 42× |
| **5 cặp thắng/chìm đọc trọn 09/08** | 3/4 luật cấu trúc mới bắn trúng cả hai bên; **chìm chấm 6-9/10** ở khối cấu trúc | **68-552×** |

Bảy chiều đã kiểm và **trượt**: mật độ cài-lật · độ sạch cú lật · kích thước khối trả nợ ·
có tráo đề không · độ leo thang bằng chứng · bookend đầu-cuối · **có CTA không** *(11/11 bài,
cả thắng lẫn chìm, đều 0 CTA)*.

> # Ở dải kênh đang viết, KỊCH BẢN LÀ SÀN CHỨ KHÔNG PHẢI CON HÀO.
>
> Nó quyết định bài có tệ tới mức không đăng được hay không.
> **Nó không quyết định bài có nổ hay không.**
>
> ## → Qua cổng rồi thì ĐĂNG. Dồn sức vào thumbnail → title → chọn đề tài có ≥2 cú nổ đã chứng minh.

Bằng chứng đầy đủ: `../3_bangchung/DOICHUNG_5BaiChim_2026-08-09.md` ·
`../3_bangchung/DOC_TRON_6KichBan_2026-08-09.md` · `../3_bangchung/TONGHOP_16Kenh_2026-08-09.md`

---

## ⚠️ LỖ HỔNG KHÔNG VÁ ĐƯỢC BẰNG FILE NÀY

Không danh sách nào bắt được **lỗi cấu trúc** — bí ẩn giả, đáp án đến sai lúc, hai chương
làm cùng một việc. Vì những thứ đó là tính chất của **cả bài**, còn danh sách thì chấm
**từng linh kiện**. Và người viết **không tự chấm được**.

→ **Cổng 4 của file này là bắt buộc khi đổi cấu trúc — trong `FLOW_VietKichBan_11Cong.md` nó là Cổng 10.**

---

## 📖 KHO CÂU MẪU — ĐỌC SAU, ĐỪNG CHÉP

**79 câu nguyên văn của đối thủ đã được gỡ khỏi file này ngày 09/08** và chuyển sang
`../2_nguyenlieu/KHO_CauMau_DoiThu_DungChep.md`.

**Vì sao:** AI viết ra thứ **gần nhất với câu mẫu nó vừa đọc**. Đặt câu nguyên văn của đối
thủ vào cột chấm điểm chính là ra lệnh cho nó viết na ná đối thủ, rồi thưởng khi nó làm thế.
Mục 22 cũ **bắt buộc phải có** cụm `"Next time you…"` — cụm đó có trong **65/488 bản ghi
đối thủ**.

Các kho khác, cùng một luật *(đọc để biết register, chép là clone)*:
`NganHang_ReHook_BucketBrigade.md` · `KHO_AnDu_TruyenChem_LachLuat.md` ·
`KHO_CaiVaLat_12Loai.md` · `KHO_GiongCamXuc_DoiThu.md`

---

## SỔ THAY ĐỔI 09/08/2026 — một ngày, bốn đợt

> ⚠️ **Số mục dưới đây thuộc thang điểm CŨ và KHÔNG còn tồn tại trong file này.** Giữ lại
> để tra ngược sổ `RETIRED_RULES.md`, đừng đi tìm chúng ở trên.

| đợt | việc *(số hiệu của thang điểm đã bỏ)* |
|---|---|
| bóc 16 kênh | gỡ mục **2** tự giễu · **23** callback · **26** cọc để-dành-cuối · **29** bookend · thêm **37** nối chương · **38** hình dạng mối nối · **39** câu cuối khẳng định · **40** khuôn nén mỏ neo |
| đọc trọn 6 bài THẮNG | gỡ **10** nhịp hài · **32** mật độ giác quan *(LUẬT 0 đã khai bị bác mà vẫn đang chấm điểm)* · thêm **41-44** tầng cấu trúc |
| đối chứng 5 bài CHÌM | gỡ **41** trả-nợ-rồi-tráo-đề · **44** cú lật cấm dữ kiện mới · hai cổng của **27** cài-lật · hai vế của **43** thang bằng chứng · vế vị trí của **42** chương thừa |
| **chủ ra lệnh đổi kiến trúc** | **bỏ thang điểm**, tách CỔNG / GỢI Ý NGHỀ, gỡ 79 câu mẫu ra khỏi cột chấm |
| **đọc trọn file này** *(09/08 đêm)* | tách ba-ràng-buộc-lời-đọc khỏi phép-kiểm-bản-dựng · thêm bảng **trượt cổng thì làm gì** · thêm đối chiếu cổng ↔ FLOW · gỡ va chạm §2.6 ↔ §2.8 |

> **Ba mục bị gỡ trong CÙNG NGÀY chúng được thêm vào.** Đó là cái giá của việc đưa luật vào
> thang điểm trước khi có nhóm đối chứng — và là lý do bản này không còn thang điểm nữa.
>
> ## ⛔ Luật nào chưa có NHÓM ĐỐI CHỨNG thì không được làm cổng. Chỉ được nằm ở PHẦN 2.

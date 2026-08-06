---
paths: ["videos/**/03-script/**", "Video*/Script_*_narration.txt", "Video*/_nhap/**", "videos/**/04-review/**"]
---
# LUẬT — FILE KỊCH BẢN

**Không ghi đè.** Mỗi lần sửa tạo `vNNN-<lý-do>.md` mới. Không sửa `vNNN` đã tồn tại.

`approved.md` và `published.md` **bất biến**. Sửa sau khi duyệt = tạo `vNNN` mới + duyệt lại.

⛔ **Kịch bản cũ `Video*/Script_*_narration.txt` là read-only** cho tới khi có lệnh migration riêng. Chúng không có lịch sử phiên bản và project chưa có git bao phủ chúng.

**Bốn ràng buộc cứng của lời đọc** — vi phạm là hỏng, không phải là lệch:
`!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng · `I` ≈ 0.

**Mọi con số khác là triệu chứng.** Lệch thì đi đọc đoạn đó và hỏi *"đoạn này có dở không?"*. Không dở thì để yên. **Cấm sửa một câu để con số đẹp hơn.**

**Agent review không được sửa file này.** Chỉ `/apply-review` tạo version mới, và chỉ sau khi người dùng đã phân loại từng góp ý.

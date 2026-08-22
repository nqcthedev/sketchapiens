# CỔNG 10 — NGƯỜI NGHE NGOÀI · KẾT QUẢ

> **File này ghi lại thứ ĐÃ xảy ra, không phải thứ vừa làm.** Cổng 10 chạy thật qua bảy vòng review
> ngoài bằng ChatGPT chat mới, từ 20/08 đến 21/08/2026. Bằng chứng gốc liệt kê ở mục 3.
>
> ⚠️ **Ba agent nội bộ KHÔNG đóng được cổng này.** `CLAUDE.md` luật 5: subagent nạp đủ `CLAUDE.md`
> và project rules, nên chúng **không lạnh**. Lớp người-xem-lạnh duy nhất là ChatGPT chat mới.

## 1. TRẠNG THÁI

```text
CỔNG 10   ĐÃ CHẠY — 7 vòng, 20-21/08/2026
LỚP       ChatGPT chat mới, không nạp context dự án
KẾT QUẢ   23 lỗi bị bắt, phân theo 7 kiểu
```

## 2. BẢY KIỂU LỖI NGƯỜI NGOÀI BẮT ĐƯỢC

Rút từ `kho/3_bangchung/BAIHOC_V20_NGUOI_NGOAI_2026-08-21.md` *(157 dòng)*:

| kiểu | số ca | ví dụ nặng nhất |
|---|---:|---|
| nói chắc hơn nguồn | 8 | Haskell *"không phải mức lạnh nhất"* — sai thẳng file mỏ neo của chính dự án |
| câu cuối trỏ về beat đã cắt | 5 | recap gọi lại chương đã bị xoá |
| số/tên sai | 4 | cave lion 1,5 m là số của *Panthera fossilis*, **sai loài** |
| con số phát minh | 3 | *"nệm dày mười phân"* — sống qua **hơn 30 bản** |
| dựng cảnh từ phép đo | 3 | biến số liệu lab thành cảnh có thật |
| regression khi dịch | 2 | `always` lẻn vào **lúc dịch**, không có ở bản gốc |
| viết ngược cơ chế | 1 | *"chỗ bắt đầu nguội là bàn tay"* — ngược sinh lý, và bài tự mâu thuẫn |

**Điểm đáng ghi nhất:** ba lỗi *(`always` · *"cả trại"* thay vì 33 người · thiếu *"or in light stages
of sleep"*)* đều là **cùng một mỏ neo Samson bị nói quá ở ba vòng khác nhau, bằng ba chữ khác nhau**.
Máy không bắt được vì mỗi lần chỉ lệch một chữ.

## 3. BẰNG CHỨNG GỐC

```text
kho/3_bangchung/BAIHOC_V20_NGUOI_NGOAI_2026-08-21.md   157 dòng · 23 lỗi / 7 kiểu
videos/Video20_Cold/_nhap/PROMPT_CHATGPT_CONG10.md      prompt gửi vòng cổng 10
videos/Video20_Cold/_ban50/GUI_CHATGPT_ban50.md         vòng bản 50
videos/Video20_Cold/_ban52/NGHE_LANH_ban52.md           vòng nghe lạnh bản 52
videos/Video20_Cold/LENH_GPT_CONG4_V20.md               lệnh cổng 4
```

## 4. ⛔ CHƯA ĐÓNG — audit nội bộ 22/08 tìm thêm nợ MỚI

Bảy vòng trên chạy tới **bản 61**. Ngày 22/08, ba agent nội bộ chạy lại trên
`Script_V20_narration.txt` và tìm ra **nợ mà bảy vòng ngoài chưa bắt**:

- `"Michael"` Rothschild — tên riêng không có trong bất kỳ bản ghi nào
- đảo mẫu số hai lần *(25% dùng để phủ định 75%)*
- Rothschild là chết cóng **trong nhà** ở Berlin, dùng dựng chuyện ngủ **ngoài trời** thời băng hà
- `L172` tuyên bố *"that is all the evidence there is"* rồi liệt kê ba thứ — **không có Rothschild**

Chi tiết đầy đủ: `videos/Video20_Cold/NO_BANGCHUNG_V20_2026-08-22.md`.

**Nghĩa là:** cổng 10 **đã chạy** cho các bản trước, nhưng **bản hiện hành cần một vòng ngoài nữa**
sau khi đóng các nợ ở sổ trên. Không tính cổng này là xanh vĩnh viễn.

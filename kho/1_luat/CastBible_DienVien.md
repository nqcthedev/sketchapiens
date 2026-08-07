# 🎭 CAST BIBLE v2 — Dàn diễn viên kiểu "everyman đổi trang phục"

> **Bám mô hình triệu view của đối thủ** *(Mack/Stickly)* + nguyên tắc thiết kế nhân vật của chuyên gia.
> **Triết lý:** **1 thân "người que" đầu trống** dùng lại → **đổi TRANG PHỤC** thành từng nhân vật. Phân biệt bằng **trang phục + tóc + đạo cụ + biểu cảm + dáng (silhouette)**, **KHÔNG** bằng màu cơ thể. Phong cách **chibi cảm xúc**. Con vật = nhân vật ký hiệu **cố định** (phần "giữ" của hướng hybrid). Host trên màn = **hạn chế** (mặc định chỉ giọng đọc).
>
> File này = **chiến lược + sổ đăng ký**. Prompt tạo nhân vật ở `../2_nguyenlieu/Prompts_NhanVat_Kenh.md`. Quy trình giữ nhất quán (model sheet + Nano Banana) → **Part 2** (sắp làm).

---

## 0) Đổi gì so với v1?
| | v1 (cũ) | **v2 (giờ — hybrid)** |
|---|---|---|
| Mô hình | 6 nhân vật **màu cố định** riêng biệt | **1 BASE everyman** → các "costume preset" |
| Phân biệt | bằng **màu cơ thể** | bằng **trang phục + tóc + đạo cụ + biểu cảm** |
| Nhà khoa học | nhân vật chính tuyến | **optional/hạn chế** (thay bằng nền trắng + mũi tên + vật bay) |
| Mắt | chấm nhỏ | **tròn TO trắng + đồng tử chấm** (cảm xúc mạnh, ăn thumbnail) |
| Con vật | guest | **giữ nguyên** = nhân vật ký hiệu cố định |

→ Lợi: rẻ hơn (1 thân, vô số trang phục), bám đúng kiểu đã kiểm chứng triệu view, vẫn nhất quán "người của kênh".

---

## 1) DESIGN DNA — khóa cứng *(mọi nhân vật NGƯỜI chung 1 thân)*
- **Người que tối giản — NÉT TAY/CHÂN ĐẬM/DÀY** (marker to, không mảnh), **đầu tròn to hơi méo** · **thân + mặt TRẮNG (không tô da)** · **nét marker đen THÔ, hơi run** (low-budget, hand-drawn) · **tóc đen ÍT nét** (vài sợi rối, không thành mũ dày) · mặt **cực đơn giản** (mắt chấm/ô-van/nửa mắt — mở to khi sốc; mày mảnh/không; miệng 1 nét; không mũi) · **tay/chân oval hơi vụng** · **cố tình THÔ, vụng, ngu-ngơ hài (primitive/awkward), KHÔNG bóng bẩy/mascot**. Màu **chỉ ở đồ mặc + đạo cụ + nền**; thân luôn trắng.
- **PHÂN BIỆT nhân vật = TRANG PHỤC + TÓC + ĐẠO CỤ + BIỂU CẢM + DÁNG.** Tuyệt đối **không** đổi màu da/đầu để phân biệt.
- **Test silhouette** *(chuyên gia)*: tô đen đặc cả nhân vật — vẫn phải đoán ra ai nhờ tóc/đạo cụ/dáng. Nếu ancestor và forager ra cùng 1 cục đen → đổi tóc/đạo cụ/dáng tới khi khác.
- **Bảng màu NHẤN** (quần áo/đạo cụ): xanh denim trầm `#5B86B0` · lục `#3A9E3A` · vàng `#F5C518` · đỏ `#D94040` · nâu `#8B5E3C` · tan `#C4965A` · xám `#9AA0A6`. **Da chung:** TRẮNG `#FFFFFF` (mọi nhân vật — KHÔNG tô da; màu chỉ ở tóc/áo/đạo cụ).

---

## 2) TẦNG 1 — BASE + COSTUME PRESETS *(người, dùng cho MỌI video)*

| Token | Vai (VN) | Trang phục + Tóc | Đạo cụ | Màu nhấn | Dùng khi |
|---|---|---|---|---|---|
| `@BASEHUMAN` | **thân gốc** (không mặc gì đặc trưng) | khố trơn, tóc gọn trung tính | — | da `#E8C9A0` | gốc để tạo mọi costume (Part 2) |
| `@MODERNYOU` | "bạn" / người hiện đại | hoodie xanh denim trầm, tóc gọn | điện thoại | `#5B86B0` | host hiện đại, hook, câu chốt "that's you" |
| `@ANCESTOR` | tổ tiên **nam** (thợ săn) | khố lông tan, tóc rối + râu | giáo, đá ghè | `#C4965A`/`#8B5E3C` | cảnh quá khứ, săn bắt |
| `@FORAGER` | tổ tiên **nữ** (hái lượm) | váy sợi, tóc dài buộc | giỏ hái | `#3A9E3A` | đề tài nữ: sinh nở, hái lượm |
| `@CHILD` | trẻ cổ đại | khố nhỏ, túm tóc dựng | (vóc nhỏ) | `#F5C518` | nuôi con, lớn lên |
| `@ELDER` | già làng | khố tan, tóc/râu xám, hơi khom | gậy, vòng hạt | `#9AA0A6`/`#F5C518` | tuổi thọ, trí tuệ |
| `@SCIENTIST` *(optional)* | người giải thích | áo lab trắng, kính tròn | que chỉ, bảng | teal/trắng | **chỉ khi** cảnh sơ đồ cần "người". Mặc định **thay bằng** nền trắng + mũi tên + vật bay |

> Tất cả ô trên là **CÙNG 1 thân `@BASEHUMAN`, chỉ đổi đồ**.

### Lưới ADN nhanh *(shape language — chuyên gia)*
| Token | Shape chủ đạo | Cao (số đầu) | Màu nhấn | Tóc | Đạo cụ |
|---|---|---|---|---|---|
| @MODERNYOU | tròn mềm (thân thiện) | ~3.5 | xanh denim trầm | gọn | điện thoại |
| @ANCESTOR | vuông chắc (vững) | ~3.5–4 | nâu/tan | rối + râu | giáo |
| @FORAGER | tam giác nhẹ (nhanh nhẹn) | ~3.5 | lục | dài buộc | giỏ |
| @CHILD | tròn nhỏ (cute) | ~2.5 | vàng | túm dựng | — |
| @ELDER | tròn ngang, khom (điềm tĩnh) | ~3.3 | xám | xám thưa | gậy |
| @SCIENTIST | chữ nhật đứng (ngăn nắp) | ~4 | teal | gọn | que chỉ + bảng |

---

## 3) TẦNG 2 — GUEST LIBRARY *(con vật / khách — nhân vật ký hiệu CỐ ĐỊNH)*
- `@CHIMP`, `@WOLF`, `@MAMMOTH`, `@LION`, `@ANTELOPE`, `@BEAR`, `@SNAKE`… → đây là phần **"giữ nhân vật ký hiệu"** của hybrid: con vật **có màu/look cố định**.
- Quy tắc: video nào cần mới build (nhẹ: front + side + 2–3 biểu cảm), **xong LƯU lại** → video sau dùng lại.

---

## 4) QUY ƯỚC TOKEN + LƯU TRỮ
- **Token:** CHỮ HOA liền, có `@` ở **prompt cảnh** (`@ANCESTOR`); prompt **TẠO** nhân vật thì không có `@`.
- **File ref:** `refs/<token-thường>.png` → `refs/ancestor.png`, `refs/basehuman.png`…

### 📒 Sổ đăng ký (registry)
| Token | File ref | Trạng thái | Ghi chú |
|---|---|---|---|
| `@BASEHUMAN` | `refs/basehuman.png` | ♻️ làm lại | đổi sang THÔ hơn (bớt bóng bẩy) |
| `@MODERNYOU` | `refs/modernyou.png` | ♻️ làm lại | làm thô hơn (giữ hoodie xanh) |
| `@ANCESTOR` | `refs/ancestor.png` | ⬜ | costume |
| `@FORAGER` | `refs/forager.png` | ⬜ | costume |
| `@CHILD` | `refs/child.png` | ⬜ | costume |
| `@ELDER` | `refs/elder.png` | ⬜ | costume |
| `@SCIENTIST` | `refs/scientist.png` | ⬜ | optional |
| `@CHIMP` | `refs/chimp.png` | ⬜ | guest (cố định) |

> ⬜ → ✅ khi đã tạo & lưu. Con vật mới build thì thêm dòng.

---

## 5) NHIỀU KÊNH → re-skin
Cùng base + costume → **đổi màu nhấn + đạo cụ** cho mỗi kênh có nhận diện riêng (tránh trùng y hệt). Nếu chạy **mạng lưới chéo** (như đối thủ) → có thể giữ chung style.

## 6) Dựng nhân vật & giữ nhất quán → **Part 2** *(sắp làm)*
Model sheet (turnaround) + expression sheet + **SOP Nano Banana** (hero → sheet → lưu "Ingredient" trong Flow → mỗi cảnh = *sheet + frame trước* → branch chứ đừng chain).

## 7) ✅ Checklist mỗi video
- [ ] Costume người cần dùng đã có ref chưa? Thiếu → tạo từ `@BASEHUMAN`.
- [ ] Con vật/khách cần cho video đã có chưa? → build guest → LƯU + thêm registry.
- [ ] Mọi `@token` trong prompt cảnh khớp registry?
- [ ] Đã copy ref vào `refs/` cho pipeline/app Flow.

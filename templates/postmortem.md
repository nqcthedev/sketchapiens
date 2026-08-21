# POSTMORTEM — <SKA-NNNN-slug>

**Ngày:** YYYY-MM-DD · **Số liệu dùng:** `08-analytics/...`

> Đây là mắt xích đang đứt của cả hệ thống: project sinh tri thức về đối thủ liên tục,
> nhưng gần như không sinh tri thức về **chính mình**.
>
> **Discovery pipeline — đường phát hiện:** observation → candidate → testing → supported/... → promotion proposal → owner decision.
> Một video đơn lẻ **không** đi thẳng vào `RULE_REGISTRY.yaml`.

## 1. Video này đã hứa gì và trả được gì
| | |
|---|---|
| Title hứa | |
| Thumbnail hứa | |
| Kịch bản trả ở giây | |
| Số liệu nói gì về lời hứa đó | |

## 2. So sánh — cùng LANE, không so trung bình kênh
| | Video này | Video trước cùng lane | Chênh |
|---|---|---|---|

## 3. Điểm tụt → câu chữ
| Giây | Câu | Giả thuyết vì sao tụt | Độ tin cậy |
|---|---|---|---|

## 4. Cái gì HỌC được, cái gì CHƯA đủ để học

**Đủ bằng chứng để nói ở mức observation — quan sát:**
-

**CHƯA đủ bằng chứng — đừng kết luận:**
- *(cỡ mẫu quá nhỏ · chưa có nhóm đối chứng · đổi nhiều biến cùng lúc)*

## 5. CANDIDATE UPDATE — CẬP NHẬT CƠ CHẾ ỨNG VIÊN

> Đọc `.claude/skills/sketchapiens-story-engine/references/candidate-lifecycle.md` trước.
> Chỉ mở `mechanism-lab.md` khi thật sự cần tạo/cập nhật candidate.

| Observation | Candidate liên quan | Status trước | Evidence thuận | Counterevidence | Next test | Status đề xuất |
|---|---|---|---|---|---|---|
| | | | | | | |

Nếu observation chưa đủ thành một giả thuyết có thể bị bác → **để ở observation, đừng đặt tên mechanism mới**.

## 6. PROMOTION PROPOSAL — ĐỀ XUẤT NÂNG CẤP

Chỉ điền mục này nếu **candidate đã tồn tại**, đã qua cross-check/counterexample/test và đủ điều kiện trong Candidate Lifecycle.

**Destination — đích đến đề xuất:**
- ☐ `CANONICAL DIAGNOSTIC FRAMEWORK` — khung chẩn đoán chuẩn
- ☐ `CANONICAL MEASURED PATTERN` — pattern đã đo chuẩn
- ☐ `CANONICAL RULE / GUARDRAIL` — luật / hàng rào chuẩn
- ☐ `MERGE / PARK / REJECT` — gộp / tạm gác / bác bỏ

| Candidate | Vì sao đủ để đề xuất | Evidence | Counterevidence | Scope | Destination | Owner decision |
|---|---|---|---|---|---|---|
| | | | | | | **CHƯA DUYỆT** |

### Nếu destination là RULE / GUARDRAIL — cần đủ NĂM điều kiện

| # | 1. Bằng chứng | 2. Độ tin cậy | 3. Phạm vi | 4. Người duyệt | 5. Luật cũ bị thay |
|---|---|---|---|---|---|
| | | | | **CHƯA DUYỆT** | |

⛔ Thiếu một điều kiện là **không** được ghi vào `governance/RULE_REGISTRY.yaml`.
Chỉ proposal thật sự cần owner decision mới chuyển sang `governance/DECISIONS_REQUIRED.md`.

## 7. Việc làm ngay, không cần đổi luật
-

> Việc làm ngay phải sửa **video/workflow cụ thể**, không được lén biến candidate thành requirement mặc định cho video kế tiếp.

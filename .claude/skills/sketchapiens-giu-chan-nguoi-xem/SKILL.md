---
name: sketchapiens-giu-chan-nguoi-xem
description: >-
  [DỰ ÁN SKETCHAPIENS] Module hỗ trợ craft giữ chân ở CẤP CÂU/ĐOẠN cho explainer tò mò:
  hook wording, pacing, sentence rhythm, CTA timing, ending/landing craft và ước lượng thời lượng.
  KHÔNG phải structural authority. Khi câu hỏi là xương bài, nối chương, một-hay-nhiều-câu-hỏi,
  causal progression, belief progression, domain shift hoặc retention structure, dùng
  `sketchapiens-story-engine`. Không dùng module này như checklist bắt buộc và không tự kích hoạt
  cho generic "soát kịch bản/AVD thấp" nếu vấn đề chưa được xác định là sentence-level craft.
---

# RETENTION CRAFT — KỸ THUẬT GIỮ CHÂN CẤP CÂU/ĐOẠN

> **Status:** supporting legacy module — module hỗ trợ kế thừa.
>
> **Structural authority — quyền cấu trúc:** `sketchapiens-story-engine/CONTRACT.md`.
> File này chỉ hỗ trợ **hook wording · pacing · sentence craft · ending craft · duration estimate**.

## OWNERSHIP BOUNDARY — RANH GIỚI SỞ HỮU

### Module này ĐƯỢC làm

- soi wording của hook sau khi core question/structure đã rõ;
- soi nhịp câu dài tích luỹ và câu ngắn đóng đinh;
- nhắc CTA quá sớm nếu có;
- hỗ trợ landing/ending ở cấp craft;
- ước lượng thời lượng từ word count + tốc độ đọc đã đo, với nhãn **estimate — ước lượng**;
- đưa observation lịch sử về craft khi caller thực sự cần.

### Module này KHÔNG được làm

- quyết định chapter nào phải tồn tại;
- yêu cầu mọi hook phải bắt đầu bằng hành động đời thường;
- yêu cầu mọi hook phải có "câu hỏi thứ hai";
- yêu cầu mọi ending phải cùng một công thức;
- chấm script thiếu Causal Debt / Belief Flip / Domain Shift;
- dùng AVD thấp để suy ra một structural cause khi chưa có dữ liệu;
- override Story Engine ở structural retention;
- biến benchmark/WPM/word budget thành quality target.

## ROUTING — ĐỊNH TUYẾN

```text
xương bài / chapter / transition / promise-payoff / một hay nhiều câu hỏi
→ sketchapiens-story-engine

hook wording / sentence rhythm / CTA timing / landing craft / duration estimate
→ module này

factual support / causal proof
→ Evidence system
```

Nếu task chứa cả structure lẫn craft:
1. Story Engine chốt/chẩn đoán structure trước.
2. Module này chỉ polish craft **mà không đổi structural diagnosis**.

## ACTIVE CRAFT PRINCIPLES — NGUYÊN TẮC CRAFT ĐANG DÙNG

Đây là **observations/guidance**, không phải hard rules trừ khi `CLAUDE.md` hoặc project rules nói khác.

- **No greeting / no channel intro early — không chào/đọc tên kênh ở đầu** nếu không có lý do đặc biệt.
- **CTA timing — thời điểm CTA:** tránh đặt CTA trong đoạn mở khi nó cắt đứt curiosity đang hình thành.
- **Sentence rhythm — nhịp câu:** câu dài có thể dựng đà; câu ngắn có thể đóng đinh. Không có quota.
- **Ending craft — craft kết:** callback về opening/viewer life có thể rất mạnh khi nó thật sự trả thesis; không bắt buộc nếu bài cần kiểu kết khác.
- **Duration estimate — ước lượng thời lượng:** dùng tốc độ đọc thực tế gần nhất của kênh khi cần estimate, nhưng không cắt/nới nội dung chỉ để đạt số phút đẹp.

## LEGACY REFERENCE — TÀI LIỆU KẾ THỪA

Bản skill cũ được bảo toàn byte-for-byte tại:

`references/runtime-legacy.md`

Chỉ đọc file đó khi cần **historical rationale / craft example** cụ thể.
Nó chứa cả terminology, benchmark và structural checklist cũ đã bị thay thế ở nhiều thời điểm, nên:

- metadata/frontmatter trong legacy file **không có routing authority**;
- structural claims trong legacy file **không override Story Engine**;
- numerical benchmark trong legacy file **không tự trở thành target**;
- nếu legacy text mâu thuẫn với `CLAUDE.md`, `.claude/rules/**`, Story Engine contract hoặc governance hiện hành → nguồn hiện hành thắng.

> **Không auto-load legacy reference.** Progressive disclosure — chỉ mở khi task thật sự cần lịch sử/craft example.

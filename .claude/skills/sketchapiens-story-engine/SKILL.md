---
name: sketchapiens-story-engine
description: >-
  [DỰ ÁN SKETCHAPIENS] Cỗ máy cấu trúc câu chuyện cho Ancient Humans Explained.
  Dùng khi lên xương, sắp/nối chapter, script có nguy cơ thành danh sách fact, cần chẩn đoán
  structural retention, belief progression, domain shift, promise-payoff hoặc causal handoff.
  Dùng kèm sketchapiens-viet-kich-ban. Đây là diagnostic framework, không phải template hay
  checklist; không thay Evidence verdict, prose/voice, title/thumbnail hay owner decision.
---

# `sketchapiens-story-engine` — CỖ MÁY CẤU TRÚC CÂU CHUYỆN

> **Public interface — giao diện công khai / runtime entrypoint — cửa vào runtime.**
>
> Story Engine trả lời một câu:
>
> **Các phần của video có tạo thành một chuỗi giải thích khiến phần sau đáng nghe vì phần trước không?**
>
> Ownership canonical: [`CONTRACT.md`](CONTRACT.md).
> Bản đồ dành cho người đọc: [`README.md`](README.md).

---

## 1. ALWAYS-ON BOUNDARIES — RANH GIỚI LUÔN CÓ

Story Engine sở hữu:

- **Structural Causality — Nhân quả cấu trúc**;
- **Belief Progression — Tiến triển niềm tin**;
- **Explanatory Progression — Tiến triển giải thích**;
- **Structural Stress Test — Phép thử chịu lực cấu trúc**;
- vị trí bằng chứng trong câu chuyện, **không phải factual verdict**.

Story Engine không sở hữu:

- xác minh fact / nguồn;
- `DIRECT / INFERENCE / SPECULATION / STORY_DEVICE` verdict;
- prose, voice, anti-AI wording;
- topic, title, thumbnail;
- WPM / mật độ câu / CTA timing;
- analytics causality;
- tự promote mechanism thành rule.

Nếu ranh giới ownership không rõ, **đọc `CONTRACT.md` trước khi quyết**.

---

## 2. KNOWLEDGE LABELS — NHÃN TRI THỨC

Không trộn ba loại hiểu biết:

- `MEASURED — ĐÃ ĐO`: có corpus / transcript / analytics cụ thể; ghi sample nếu có.
- `INFERRED — MODEL SUY RA`: pattern nhìn thấy nhưng chưa chứng minh causal effect.
- `PROJECT FRAMEWORK — KHUNG CỦA SKETCHAPIENS`: công cụ làm việc do project tổng hợp.

**Knowledge level không đồng nghĩa rule status.**
Một pattern measured vẫn có thể chỉ là observation.

---

## 3. CONCEPT LEVELS — CẤP ĐỘ PHÂN TÍCH

Đừng nhầm các framework thành template cạnh tranh:

```text
VIDEO / MACRO LEVEL — CẤP VIDEO
Macro Map

VIEWER-MODEL LEVEL — CẤP MÔ HÌNH TRONG ĐẦU VIEWER
Belief Engine / Belief Flip

CHAPTER LEVEL — CẤP CHƯƠNG
Core Causal Engine

TRANSITION LEVEL — CẤP MỐI NỐI
Causal Debt / Causal Handoff
```

Một video không bắt buộc phải hiện đủ bốn level.

---

## 4. CONTEXT ROUTER — BỘ ĐỊNH TUYẾN NGỮ CẢNH

**Chỉ đọc supporting file khi task hiện tại thật sự cần nó.**

| Khi đang làm | Load thêm | Không cần load |
|---|---|---|
| lên xương · nối chapter · causal chain · belief/domain diagnosis | [`references/structural-mechanisms.md`](references/structural-mechanisms.md) | Mechanism Lab |
| đặt paper/site/experiment · synthesis · causal bridge · Narrative Overreach | [`references/evidence-in-story.md`](references/evidence-in-story.md) | raw competitor corpus |
| dựng Story Map · kiểm sau chapter · general structural review | [`references/workflows.md`](references/workflows.md) | Mechanism Lab |
| R&D mechanism · postmortem · cross-corpus check | [`references/mechanism-lab.md`](references/mechanism-lab.md) | không dùng candidate làm requirement |
| ownership / dependency / input-output conflict | [`CONTRACT.md`](CONTRACT.md) | implementation không liên quan |

### Minimum-context rule — Luật context tối thiểu

> **Không đọc một reference chỉ vì nó tồn tại. Đọc vì task hiện tại cần quyết định mà reference đó sở hữu.**

---

## 5. MODE ROUTING — ĐỊNH TUYẾN THEO CHẾ ĐỘ

### Structure Mode — Chế độ dựng cấu trúc

1. Nhận core question + approved research/evidence anchors + outline/draft + packaging promise nếu có.
2. Load `structural-mechanisms.md` khi cần dựng/kiểm causal-belief-domain progression.
3. Load `workflows.md` khi cần Story Map hoặc chapter stress test.
4. Chỉ load `evidence-in-story.md` nếu task có evidence placement/synthesis/bridge.
5. Writer sở hữu câu chữ cuối cùng.

### Review Mode — Chế độ review cấu trúc

1. Chấm narration/outline ở bề mặt viewer.
2. Ưu tiên **exact weak transition · topic jump · belief-stagnant block · promise-payoff risk**.
3. Story Engine chỉ flag `Narrative Overreach — Cốt truyện chạy vượt bằng chứng`; Evidence system mới ra verdict.
4. Reviewer không rewrite nếu caller role cấm rewrite.

### Preloaded subagent profile — Profile subagent được preload

Khi `viewer-retention-judge` preload skill này, **chính file `SKILL.md` là context mặc định**.
Supporting references **không phải default payload** và không được tự mở hàng loạt.
Agent prompt của reviewer quyết định output contract; chỉ đọc reference khi có ambiguity thật.

---

## 6. FIVE NON-NEGOTIABLE DIAGNOSTIC RULES — NĂM NGUYÊN TẮC CHẨN ĐOÁN

1. **Không biến mechanism thành quota.** Không có “phải N causal debts / N flips / N domain shifts”.
2. **Không bịa mystery.** Đề tài không có bí ẩn thật thì dùng progression/reframe khác.
3. **Không bịa flaw cho solution.** Nếu nguồn không support giới hạn đó, đừng giữ causal chain cho đẹp.
4. **Không giữ fact chỉ vì nó hay.** Fact phải trả câu hỏi, đổi model, tạo consequence hoặc làm thesis tiến.
5. **Script phục vụ viewer. Engine phục vụ script. Không đảo ngược thứ tự đó.**

---

## 7. MECHANISM LAB — PHÒNG THÍ NGHIỆM CƠ CHẾ

`references/mechanism-lab.md` **không auto-load trong phiên viết/review bình thường**.
Candidate ở đó:

- không phải rule;
- không phải requirement;
- có thể `PROMOTE / MERGE / DEMOTE / REJECT`;
- không có pipeline mặc định `candidate → RULE_REGISTRY`.

Promotion vẫn tuân `governance/CHANGE_POLICY.md` + owner decision.

---

## 8. OUTPUT SURFACES — BỀ MẶT ĐẦU RA

Khi dựng cấu trúc: **Story Map — Bản đồ câu chuyện**.

Khi review: **Structural Diagnosis — Chẩn đoán cấu trúc**.

Format chi tiết chỉ load từ `references/workflows.md` khi caller thật sự cần artifact đó.

---

## 9. STOP CONDITION — ĐIỀU KIỆN DỪNG

Dừng khi lỗi cấu trúc thật đã được giải và chỉnh tiếp chỉ làm framework đẹp hơn trên giấy.

**Không tối ưu script để làm Story Engine trông đúng.**

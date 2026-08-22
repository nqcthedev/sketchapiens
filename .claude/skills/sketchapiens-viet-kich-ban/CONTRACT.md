# SKETCHAPIENS WRITER CONTRACT — HỢP ĐỒNG BỘ NÃO VIẾT

> **Status:** `CANONICAL MODULE CONTRACT — PHASE 3B IMPLEMENTATION CONTRACT`
>
> File này định nghĩa ownership, boundary, input/output và dependency của `sketchapiens-viet-kich-ban` trong kiến trúc đích Phase 3B.
> Nó không phải corpus notebook, không phải creative mechanism catalog, không phải review rubric.
>
> Trong quá trình migration, `SKILL.md` có thể còn là compatibility runtime cho tới các task 03B-D/03B-E.
> Không dùng sự tồn tại của legacy implementation để mở rộng ownership ngoài contract này.

---

# 1. PURPOSE — MỤC ĐÍCH

`sketchapiens-viet-kich-ban` — **Bộ não viết lời Sketchapiens** tồn tại để:

> **Biến topic/promise đã chọn + research/evidence được phép dùng + structural intent thành narration tự nhiên, rõ, có giọng riêng, đúng mức chắc của bằng chứng và phù hợp workflow sản xuất hiện hành.**

Writer là module **prose realization — hiện thực hóa thành câu chữ**.
Writer không phải module nghiên cứu thị trường, Story Engine thứ hai, Evidence Engine, reviewer, packaging engine hay production engine.

---

# 2. OWNERSHIP — WRITER SỞ HỮU

## 2.1 Prose realization — Hiện thực hóa câu chữ

Writer sở hữu quyết định cuối ở cấp câu:

- lựa chọn từ;
- nhịp câu;
- độ cụ thể;
- biến mechanism / fact / scene thành lời nói nghe tự nhiên;
- narrator voice/register trong constraints hiện hành;
- câu chuyển ở cấp prose sau khi structural intent đã rõ;
- câu landing / final sentence choice ở cấp diễn đạt.

Writer được quyền **không dùng một craft suggestion** nếu suggestion đó làm prose kém tự nhiên hoặc không chữa vấn đề thật.

## 2.2 Writing-session orchestration — Điều phối phiên viết

Trong mode viết, Writer sở hữu cách thực hiện phiên viết:

- viết theo batch khi workflow yêu cầu;
- dừng cho owner feedback ở checkpoint đã định;
- tiếp tục từ current approved direction;
- ghi rõ debt cần handoff thay vì tự mở mode khác;
- giữ continuity giữa các batch/version.

Project lifecycle/state vocabulary vẫn thuộc `CLAUDE.md` + schema, không thuộc Writer.

## 2.3 Vietnamese drafting — Bản Việt làm working representation

Writer sở hữu chất lượng prose của bản tiếng Việt đang được owner nghe/duyệt.

Default workflow:

```text
VI draft
→ owner nghe / sửa / duyệt
→ VI lock
→ English final rewrite
```

## 2.4 English final rewrite — Bản Anh cuối

Sau khi VI được owner duyệt, Writer sở hữu chất lượng English narration cuối:

- rewrite theo **ý**, không dịch máy từng câu;
- giữ logic, stakes, facts và structural intent đã duyệt;
- làm tiếng Anh nghe như spoken narration tự nhiên;
- không tự thêm factual claim mới.

## 2.5 Evidence expression — Diễn đạt verdict đã có

Writer được biến verdict/evidence đã resolved thành prose tự nhiên:

- DIRECT có thể nói thẳng khi source support;
- INFERENCE phải giữ dấu hiệu suy luận phù hợp;
- SPECULATION phải nghe đúng mức bất định;
- STORY_DEVICE không được masquerade thành measured fact;
- paper/site/discovery có thể được kể như một event nếu evidence support.

Writer **không issue evidence verdict**.

---

# 3. NON-OWNERSHIP — WRITER KHÔNG SỞ HỮU

## 3.1 Topic / market / competitor research

Writer không:

- chọn thị trường bằng raw competitor search trong phiên viết;
- kéo transcript đối thủ để tìm ý/câu;
- quyết định cluster demand;
- dùng competitor phrase bank để viết.

Writer nhận **resolved research artifacts / decisions** từ upstream.

## 3.2 Structural causality / story theory

Owner: `sketchapiens-story-engine`.

Writer không duy trì structural theory song song và không ép:

- Causal Debt ở mọi transition;
- fixed hook beat count;
- fixed chapter count;
- mandatory mystery;
- mandatory bookend;
- mechanism quota.

Nếu vấn đề cần quyết định structural, route sang Story Engine.

## 3.3 Factual verdict / claim locking

Owner: Evidence system / Evidence Prosecutor / claim ledger.

Writer không tự biến unsupported claim thành acceptable chỉ bằng hedge mềm.

## 3.4 Sentence-level retention theory

`sketchapiens-giu-chan-nguoi-xem` có thể hỗ trợ craft cấp câu/đoạn khi có trigger cụ thể.
Writer sở hữu prose cuối, nhưng không sở hữu benchmark/rubric retention độc lập.

## 3.5 Review verdict

Writer không tự chứng nhận script đã pass review.
Review thuộc role-specific reviewers + owner triage / workflow review.

## 3.6 Packaging

Title/thumbnail/metadata không thuộc normal narration Writer ownership.
Current title / packaging promise có thể là **input constraint** mà script phải trả nợ.

## 3.7 Production

Writer normal mode không tạo:

- shot list;
- image prompts;
- TTS production assets;
- thumbnail image;
- video assembly artifacts.

## 3.8 Analytics / mechanism promotion

Writer không được biến một competitor pattern, một video result hoặc một observation mới thành channel rule.
Promotion đi qua governance/R&D lifecycle.

## 3.9 Historical rule arbitration

Writer runtime không được tự giải kiểu:

> “section mới hơn ở cuối file thắng section cũ”.

Authority phải được kiến trúc cung cấp rõ trước khi runtime viết.

---

# 4. HARD INVARIANTS — BẤT BIẾN

Các invariants này bảo toàn behavior đã được project chốt; chúng không phải formula để tối ưu view.

1. **Vietnamese-first — Việt trước.**
2. **English-last — Anh sau khi VI được owner duyệt.**
3. **Không bảng EN+VI side-by-side để duyệt.**
4. **Ba hard narration constraints:** `! = 0` · không dash/em-dash giữa câu · mỗi câu một dòng.
5. **`I ≈ 0` đã retire.** Không hồi sinh.
6. **No raw competitor corpus/teardown trong normal write context.**
7. **Original work.** Không paraphrase transcript hay reuse beat chain của đối thủ.
8. **Độ dài theo topic + production constraint thực tế**, không universal quality target.
9. **Structure routes to Story Engine.**
10. **Evidence verdict routes to Evidence system.**
11. **Writer không set owner-only `approved` / `published` refs.**
12. **Không đưa pending experimental knowledge vào generation contract.** D-27 vẫn pending cho tới khi governance/owner quyết.
13. **Không âm thầm làm cross-mode work.** Research/packaging/production debt phải được surface/handoff.
14. **Không sửa chỉ để thỏa framework/metric khi không có concrete weakness.**

---

# 5. INPUT CONTRACT — ĐẦU VÀO

Writer nhận **resolved information/artifacts**, không cần biết implementation chi tiết của upstream module.

Một phiên viết phải có hoặc ghi rõ đang thiếu:

```text
VIDEO ID / path
CURRENT MODE / lifecycle state
SELECTED TOPIC
CURRENT TITLE / STORY PROMISE nếu đã có
APPROVED RESEARCH / evidence anchors được phép dùng
CURRENT STRUCTURAL INTENT / Story Map nếu đã có
CURRENT SCRIPT VERSION / draft nếu đang tiếp tục
OWNER FEEDBACK / quyết định từ batch trước
REAL PRODUCTION CONSTRAINTS liên quan trực tiếp narration
```

## Missing-input behavior

Nếu thiếu input làm Writer không thể viết đúng:

- nói rõ thiếu gì;
- route/handoff đúng owner;
- không tự bù bằng competitor research hoặc historical rule pile.

## Structure input rule

Nếu structural intent chưa đủ:

```text
Writer
→ Story Engine
→ Story Map / Structural Diagnosis
→ Writer prose
```

## Evidence input rule

Nếu factual bridge/claim chưa được support:

```text
Writer surfaces evidence debt
→ Evidence workflow
→ verdict / supported claim
→ Writer expression
```

---

# 6. OUTPUT CONTRACT — ĐẦU RA

## 6.1 `VI_DRAFT_BATCH`

Default trước owner approval:

- narration tiếng Việt;
- mỗi câu một dòng;
- đúng batch/scope đã thống nhất;
- factual uncertainty khớp evidence;
- không trộn image prompts / metadata / competitor analysis;
- kết batch thì dừng nếu workflow cần owner feedback.

## 6.2 `VI_LOCKED`

Đây là **owner-approved milestone**, không phải status Writer tự phong.

Writer chỉ được đi sang English-final khi có tín hiệu owner approval rõ.

## 6.3 `EN_FINAL_NARRATION`

Sau VI lock:

- rewrite bằng meaning-first English;
- giữ facts/logic/stakes/structural intent đã duyệt;
- giữ ba hard narration constraints;
- không thêm factual content im lặng;
- factual addition/change mới → Evidence handoff.

## 6.4 Artifact behavior

Khi persist script:

```text
03-script/versions/vNNN.md   = immutable version
03-script/refs/current.yaml  = mutable working pointer
approved/published refs      = owner-only
```

Exact schema/state shape thuộc `schemas/video.schema.json` + project rules.
Writer không tạo schema riêng.

---

# 7. DEPENDENCY CONTRACT — HƯỚNG PHỤ THUỘC

Target graph:

```text
CLAUDE / governance / schema
          ↓
        Writer
       ↙   ↓   ↘
 Story   Evidence   Retention Craft (optional)
 Engine  verdict    sentence/paragraph support
          ↓
      narration artifacts
          ↓
 review / editor / production consumers
```

## Allowed

- Writer gọi Story Engine qua public interface.
- Writer consume evidence artifact/verdict.
- Writer gọi Retention Craft khi có craft problem cụ thể.
- Downstream consumers đọc narration/version artifacts.

## Disallowed

- Story Engine → Writer private implementation → Story Engine.
- Writer normal mode → Mechanism Lab/candidate lifecycle.
- Writer normal mode → raw competitor corpus/teardown.
- Downstream review/production → private Writer legacy references.
- Writer → Evidence internal theory để tự issue verdict.

---

# 8. CONTEXT CONTRACT — HỢP ĐỒNG NGỮ CẢNH

## Normal VI drafting

Load tối thiểu:

```text
Writer public runtime interface
active prose guidance
current task/video artifacts cần thiết
```

Không default-load:

```text
runtime-monolith-legacy.md
competitor teardowns
research workflow internals
metadata/packaging refs
historical dead-rule rationale
pending D-27 material
```

## Structure issue

Invoke Story Engine; chỉ nạp structural context mà task cần.

## Evidence-expression issue

Nạp evidence-expression guidance + current claim verdict/evidence artifact.

## Sentence-level craft issue

Có thể invoke Retention Craft; không biến nó thành structural owner.

## English-final stage

Chỉ sau VI approval; nạp English-final rewrite guidance.

## Historical/audit question

Legacy/history chỉ được mở **on demand** cho audit/provenance/R&D, không cho normal generation.

---

# 9. POSITIVE PROSE PRINCIPLES — PHẠM VI HỢP LỆ

Active Writer guidance được phép chứa các nguyên tắc implementation như:

- spoken trước, literary sau;
- concrete khi concrete giúp hiểu;
- mechanism/explanation trước ornament;
- sentence rhythm phục vụ ý;
- humor là optional craft, không quota;
- tránh empty profundity / slogan-like aphorism;
- evidence có thể được kể như discovery/event;
- named objects/sites/people khi evidence support và giúp clarity;
- sau cut/insert phải giữ continuity của câu trỏ/ngữ nghĩa;
- viết bản mạnh nhất hiện tại, không gửi placeholder vì nghĩ reviewer sẽ cứu sau.

Active Writer guidance **không được** chứa:

- view-causality claim chỉ vì winner có pattern;
- timing/density quota;
- competitor verbatim phrase bank;
- dead-rule tombstone như runtime instruction;
- Story Engine mechanism definitions;
- Evidence taxonomy như Writer-owned logic;
- packaging/SEO instruction;
- pending candidate/measurement như hard requirement.

---

# 10. STOP / HANDOFF CONDITIONS — KHI NÀO WRITER DỪNG

Writer dừng hoặc handoff khi:

1. batch hiện tại hoàn tất và cần owner feedback;
2. next move là structural hơn là prose → Story Engine;
3. claim cần dùng chưa có evidence support/verdict → Evidence;
4. task chuyển sang competitor/market research → research mode;
5. caller yêu cầu final EN nhưng VI chưa được owner approve;
6. narration đã xong và việc còn lại là review/editor workflow;
7. việc còn lại là packaging/production;
8. edit tiếp chỉ để thỏa một framework/metric chứ không chữa concrete weakness.

---

# 11. LEGACY CONTRACT — HỢP ĐỒNG VỚI DI SẢN

`references/runtime-monolith-legacy.md` được giữ để:

- provenance;
- rollback;
- audit lịch sử;
- salvage khi refactor cần đối chiếu.

Nó **không phải target runtime authority**.

Không rename/move/delete legacy artifact trong Phase 3B nếu chưa có explicit owner authorization và dependency verification.

Các dead/pending families không được resurrect chỉ vì còn text trong legacy:

- `I ≈ 0`;
- mandatory self-deprecating hook joke;
- mandatory “about YOU” lane;
- fixed humor/anchor/question cadence;
- fixed chapter count/length as quality rule;
- mandatory mystery/bookend/callback;
- delayed-payoff tease as universal requirement;
- D-27 seven-ruler thresholds/quotas chưa được owner promote.

---

# 12. REGRESSION INVARIANTS — BẢO VỆ KHI REFACTOR

Phase 3B implementation phải chứng minh:

- `R-W1` VI-first vẫn hoạt động.
- `R-W2` normal write không competitor leakage.
- `R-W3` structural decision defer Story Engine.
- `R-W4` factual verdict defer Evidence.
- `R-W5` prose không collapse thành fact list vô hồn sau khi bỏ monolith.
- `R-W6` dead/pending rules không resurrect.
- `R-W7` EN stage chỉ mở sau owner VI approval.
- `R-W8` immutable versions + owner-only refs an toàn.
- `R-W9` research/metadata/image/production không tự chảy vào Writer mode.
- `R-W10` behavior đúng không phụ thuộc late override section sống sót qua context compaction.

---

# 13. PRECEDENCE INSIDE WRITER DOMAIN — THỨ TỰ ƯU TIÊN

Trong phạm vi Writer:

```text
CLAUDE.md / project rules / schema / governance hard constraints
→ this CONTRACT.md
→ active Writer SKILL.md
→ active Writer references loaded by router
→ optional supporting craft
→ legacy/history/provenance
```

Story structure và Evidence verdict không được resolve bằng Writer precedence; chúng defer sang canonical owner tương ứng.

Nếu contract này mâu thuẫn project-level source cao hơn, project-level source thắng và conflict phải được ghi để sửa, không được âm thầm chọn.

---

# 14. CHANGE BOUNDARY — RANH GIỚI THAY ĐỔI

Contract này khóa **architecture/ownership**, không tự thêm creative behavior mới.

Muốn thêm một rule sáng tạo mới vào active Writer runtime phải đi qua governance hiện hành.
Một observation mới không được append vào Writer rồi tự gọi là “latest section”.

Phase 3B implementation phải ưu tiên:

> **extract current behavior → route đúng owner → giảm default context → preserve capability → verify regression**

thay vì rewrite Writer theo cảm giác.

# 03A-C — AUTHORITY & SOURCE-OF-TRUTH AUDIT — KIỂM QUYỀN SỞ HỮU / NGUỒN CHUẨN

> **Status:** `READ-ONLY AUDIT ARTIFACT — NON-RUNTIME`  
> Task này không sửa source canonical và không sửa Writer runtime. Mục tiêu là xác định **ai đang có quyền phán**, nơi Writer chỉ nên consume, và nơi project hiện có conflict thật cần xử lý trước runtime refactor.

**Baseline:** checkpoint `657662b2cfb94ab8da95a72d18e4dc0d5090d918`  
**Inputs:** `CLAUDE.md` · `SOURCE_OF_TRUTH.md` · `.claude/rules/script-files.md` · Story Engine `CONTRACT.md` · retention skill · Evidence Prosecutor · `FLOW_VietKichBan_11Cong.md` · `RUBRIC_KichBan.md` · `HE_THONG_KichBan_v2_14Video.md` · YouTube policy file · current Writer wrapper/legacy refs.

## Câu hỏi của task

Với 14 responsibility đã bóc ở 03A-B, **nguồn nào hiện có authority**, Writer là owner hay consumer, và chỗ nào đang có shadow/duplicate/conflict?

**Stop condition:** mỗi responsibility có verdict authority rõ hoặc được đánh `UNRESOLVED`; không tự chọn một nguồn khi canonical docs đang mâu thuẫn.

---

# 1. VERDICT LABELS — NHÃN PHÂN LOẠI

- `OWNER` — Writer thực sự được sở hữu quyết định đó.
- `CONSUMER` — Writer cần dùng kết quả/contract từ owner khác.
- `SHARED BOUNDARY` — Writer sở hữu phần biểu đạt, module khác sở hữu phần phán quyết.
- `DUPLICATE` — Writer/legacy text lặp lại authority của source khác.
- `STALE SHADOW` — text cũ vẫn trong context nhưng đã mất authority.
- `UNRESOLVED` — project hiện chưa có một owner duy nhất hoặc source canonical tự mâu thuẫn.

---

# 2. AUTHORITY MAP — 14 RESPONSIBILITIES

| ID | Responsibility | Canonical/current owner | Writer role | Audit verdict |
|---|---|---|---|---|
| W-R01 | Activation / routing | `CLAUDE.md` mode router + current Writer `SKILL.md` public interface | expose activation surface, không tự đặt project mode | `OWNER` ở skill interface · `CONSUMER` của control plane; legacy frontmatter = `STALE SHADOW` |
| W-R02 | Writing workflow orchestration | `CLAUDE.md` VI-first/EN-last + `FLOW_VietKichBan_11Cong.md` cho script gates | điều phối cách viết trong phạm vi mode ② | `SHARED BOUNDARY`; legacy workflow duplicate/cũ |
| W-R03 | Niche writing principles | `RUBRIC_KichBan.md` + `HE_THONG_KichBan_v2_14Video.md` theo `SOURCE_OF_TRUTH.md` | dùng active craft principles để viết | `CONSUMER`; `luat-chung-ngach.md` không nằm trong SoT và chứa dead rules → `STALE/DERIVED SHADOW` |
| W-R04 | Story structure | Story Engine `CONTRACT.md` + runtime `SKILL.md` | nhận Story Map/diagnosis, viết prose theo structure | `CONSUMER`; monolith/FLOW/HE_THONG structural prescriptions = `DUPLICATE / CONFLICTING SHADOW` |
| W-R05 | Narration voice/register | quality SoT: `RUBRIC_KichBan.md` + `HE_THONG...`; Writer là nơi thực thi prose | chọn chữ/giọng cuối cùng trong constraints | `SHARED BOUNDARY`; Writer owns prose implementation, không own corpus-derived “law” |
| W-R06 | VI→EN representation transform | `CLAUDE.md` + active Writer wrapper | thực hiện EN rewrite sau VI approval | `OWNER` implementation dưới project contract; legacy English-first metadata = `STALE SHADOW` |
| W-R07 | Evidence-aware writing | Evidence verdict: `evidence-prosecutor.md` + claim ledger; project hard evidence rules ở `CLAUDE.md`/FLOW | diễn đạt DIRECT/INFERENCE/etc. thành narration có hedge đúng | `SHARED BOUNDARY`; Writer owns expression, Evidence owns verdict |
| W-R08 | Topic/title research | mode ① `sketchapiens-chon-de-tai`; SoT topic/live data; title SoT `HE_THONG...` PHẦN C | nhận topic/title decision; không chạy competitor market research trong write mode | `CONSUMER`; monolith research flow = wrong-mode `DUPLICATE` |
| W-R09 | Competitor research/calibration | corpus / measurement layer + research mode; corpus cấm ở write mode | normal Writer runtime không cần raw competitor teardown | `CONSUMER/NO AUTHORITY`; competitor refs = research/history, không runtime law |
| W-R10 | Retention craft | `sketchapiens-giu-chan-nguoi-xem` supporting craft; structural part Story Engine | áp craft vào prose sau structure | `CONSUMER` of craft guidance; Writer owns actual sentence choice |
| W-R11 | Originality/reuse/policy safety | `CLAUDE.md`, YouTube policy SoT, quality/reuse gates | tạo nội dung gốc và diễn đạt an toàn | `CONSUMER + IMPLEMENTER`; không tự phát minh policy |
| W-R12 | Output/artifact formatting | `schemas/video.schema.json` + `.claude/rules/script-files.md` + lifecycle/control plane | xuất narration đúng artifact/version contract | `CONSUMER`; legacy PHẦN 8 output format = `STALE SHADOW` |
| W-R13 | Packaging metadata | Title SoT `HE_THONG...` PHẦN C; thumbnail skill owns thumbnail; description/tags owner **không được map rõ** trong current SoT | narration Writer không nên tự coi metadata là quyền của mình | `UNRESOLVED` cho description/tags; `CONSUMER` cho title; `metadata.md` không có canonical authority |
| W-R14 | Measurement/history/override ledger | corpus measurements + governance (`RETIRED_RULES`, registry, SoT/change policy) | không cần mang history vào normal generation context | `NO RUNTIME AUTHORITY`; PHẦN 13–14 = provenance/history, không phải owner độc lập |

---

# 3. SOURCE-OF-TRUTH GAPS — KHOẢNG TRỐNG NGUỒN CHUẨN

## GAP-C1 — Writer public interface chưa có dòng canonical riêng trong `SOURCE_OF_TRUTH.md`

SoT map Story Engine, retention craft, evidence verdict, script quality, title, lifecycle..., nhưng chưa có row kiểu:

```text
Narration generation / Writer orchestration / prose implementation
→ .claude/skills/sketchapiens-viet-kich-ban/SKILL.md
```

Hiện authority của wrapper được suy ra từ `CLAUDE.md` routing + Architecture Contract, chứ chưa được SoT map trực tiếp.

**Impact:** sau refactor, future audit có thể lại hỏi “Writer skill hay RUBRIC mới là owner của voice/workflow?”

**Disposition:** đề xuất ở 03A-G; **không sửa SoT trong 03A-C**.

## GAP-C2 — Description/tags/metadata chưa có owner canonical rõ

`metadata.md` tự gọi mình là “Module”, nhưng:

- nó nằm bên trong Writer references;
- `SOURCE_OF_TRUTH.md` không map description/tags vào file này;
- nó tự cảnh báo chứa luật chết;
- title trong nó đã bị source khác sở hữu;
- thumbnail thuộc thumbnail skill.

**Verdict:** `UNRESOLVED`, không được dùng việc file đang tồn tại để suy ra ownership.

---

# 4. CANONICAL CONFLICTS — XUNG ĐỘT THẬT ĐANG TỒN TẠI

Đây là phần quan trọng nhất của 03A-C. Các conflict dưới đây **không được Writer tự giải bằng precedence nội bộ**.

## CONFLICT-C1 — `FLOW_VietKichBan_11Cong.md` đang sở hữu structural behavior mà Story Engine contract đã lấy làm canonical

`FLOW` hiện bắt:

- Cổng 5: **viết đoạn kết trước**;
- kết theo bốn nhịp cụ thể / bookend;
- cấm `you/your` trong ending;
- Cổng 6 QA: **mở vòng mới trước khi đóng vòng cũ**;
- đóng chương bằng **blind promise**.

Trong khi Story Engine contract nói:

- Story Engine sở hữu structural causality / progression / transitions / stress test;
- không bắt mọi ending cùng một công thức;
- không bắt mọi transition có Causal Debt;
- structure là diagnosis, không checklist/template.

### Verdict

`FLOW` có authority hợp lý với **gate existence / process sequencing**, nhưng phần **creative structural prescription** là competing authority với Story Engine.

**Classification:** `UNRESOLVED CANONICAL OVERLAP`, đã có tiền thân D-01 trong `SOURCE_OF_TRUTH.md`.

**Refactor implication:** 03B không được copy các structural mandates này vào Writer contract như “writer rules”. Cần tách gate/process khỏi structural creative decisions bằng governance task hoặc owner decision trước khi runtime switch hoàn tất.

---

## CONFLICT-C2 — `RUBRIC_KichBan.md` LUẬT 0 vs Cổng 5 KỊCH TÍNH

Đầu file tuyên bố:

> Chỉ có 3 hard narration constraints. **MỌI con số khác là triệu chứng, không phải đích.** Cấm sửa câu để số đẹp hơn.

Nhưng Cổng 5 (18/08) lại yêu cầu so với một matched breakout:

- death words ≥ **60%** comparator;
- direct viewer address ≥ **60%** comparator;
- concrete objects ≥ **60%** comparator;
- danger timing không muộn hơn comparator quá **5%**.

Nó nói “không có ngưỡng tuyệt đối”, nhưng vẫn là **threshold gate** có PASS/FAIL dựa vào numeric target.

Ngoài ra “hedge budget tối đa MỘT khối thành thật” cũng là prescription mới, trong khi các phần trước từng bác numeric hedge quota vì vấn đề là placement.

### Verdict

Đây là **internal contradiction trong chính canonical quality source**, không phải lỗi Writer.

**Classification:** `UNRESOLVED CANONICAL CONTRADICTION`.

**Refactor implication:** Writer 03B **không được chọn một vế** rồi biến thành runtime principle. Cần owner/measurement/governance review riêng. Cho tới khi giải, Writer chỉ tuân 3 hard constraints và các owner-approved gate artifacts hiện hành; không hard-code Cổng 5 vào prose module.

---

## CONFLICT-C3 — `HE_THONG_KichBan_v2_14Video.md` chứa cả living guidance, dead rubric và structural formulas

File tự ghi:

- 8 con số đã chết;
- PHẦN E 20 ô “đừng dùng để chấm”;
- nhiều trích dẫn cũ gán sai;
- nhiều section historical artifact.

Nhưng vẫn còn các prescription như:

- bookend;
- blind promise majority;
- ending four-beat formula;
- chapter opening/closing mechanics.

Một phần là craft observation, một phần là structure.

### Verdict

Theo SoT, HE_THONG vẫn là một quality/title source; nhưng **không phải mọi section trong file có cùng authority**. Story Engine thắng phần structure, RUBRIC thắng khi HE_THONG mâu thuẫn RUBRIC, và historical/dead blocks không có runtime authority.

**Classification:** `MIXED-AUTHORITY SOURCE`.

**Refactor implication:** Writer không được deep-load toàn HE_THONG như một “active ruleset”. Future context phải route tới active subset/contract hoặc consume decisions qua cleaner interface.

---

# 5. SHADOW AUTHORITY INSIDE WRITER

## S-C1 — Legacy frontmatter

Legacy monolith nói English-first, 2-column, 8–25 min. Active wrapper/CLAUDE nói VI-first, EN-last, no side-by-side, topic-driven length.

**Verdict:** `STALE SHADOW`, zero authority but still context-visible.

## S-C2 — `luat-chung-ngach.md`

File tự gọi là “luật chung” và “đọc mỗi lần viết”, nhưng SoT không map nó làm canonical source; file tự cảnh báo chứa dead rules.

**Verdict:** `DERIVED/HISTORICAL KNOWLEDGE`, không được override quality SoT/Story Engine/control plane.

## S-C3 — competitor teardown references

`viral-teardown.md` tự ghi 7/8 mục chứa luật đã bị bác. `formula-and-example.md` và survival teardown đều có dead-rule banners.

**Verdict:** useful provenance/calibration ở research context; **no normal write authority**.

## S-C4 — Writer PHẦN 0–12 vs PHẦN 13–14 internal precedence

“Phần mới thắng phần cũ trong cùng file” là chính architecture smell A-05/A-12 muốn loại.

**Verdict:** provenance strategy, không phải acceptable long-term runtime architecture.

---

# 6. CLEAN BOUNDARIES ĐÃ ỔN — KHÔNG CẦN MỞ LẠI

## Story vs prose

Story Engine contract rõ:
- Story owns structural diagnosis/progression;
- Writer owns final prose/voice.

**PASS.**

## Story vs Evidence

Story flags Narrative Overreach; Evidence Prosecutor reads source and issues DIRECT/INFERENCE/SPECULATION/STORY_DEVICE verdict.

**PASS.**

## Structure vs retention craft

Retention skill hiện đã thu về hook wording/pacing/sentence rhythm/landing craft và không auto-load legacy.

**PASS.**

## Topic research vs writing mode

`CLAUDE.md` và `sketchapiens-chon-de-tai` đã tách mode ① research khỏi mode ② write.

**PASS ở control plane**, dù Writer monolith vẫn chứa duplicate research instructions.

## Artifact ownership

Schema/rule owns lifecycle/version shape; Writer không được tự tạo semantics khác.

**PASS ở control plane**, legacy implementation còn chưa native.

---

# 7. AUTHORITY DECISION MATRIX CHO 03B+

Future refactor **không được** làm các việc sau nếu chưa có owner/source resolution:

1. Không đưa “write ending first/bookend/blind promise” thành Writer hard rule chỉ vì FLOW đang ghi.
2. Không đưa Kịch tính 60%/5% thresholds vào Writer creative contract khi RUBRIC tự mâu thuẫn LUẬT 0.
3. Không coi `luat-chung-ngach.md` là canonical chỉ vì tên file có chữ “luật”.
4. Không coi `metadata.md` là owner của title/thumbnail/metadata toàn bộ.
5. Không copy Story Engine concepts trở lại Writer implementation.
6. Không copy Evidence taxonomy/verdict logic vào Writer.
7. Không dùng competitor teardown như always-on prose guidance.

Future refactor **được** dựa chắc vào:

- `CLAUDE.md` mode + VI-first/EN-last;
- 3 hard narration constraints;
- immutable versions + mutable refs;
- Story Engine contract;
- Evidence Prosecutor boundary;
- retention craft boundary;
- original-work / no competitor corpus while writing;
- owner approval semantics.

---

# 8. OWNER-DECISION STATUS

03A-C phát hiện **hai canonical conflicts thật** (C1, C2) và một mixed-authority source (C3).

Tuy nhiên **chưa cần đánh thức owner ngay** vì:

- 03A-D/E/F còn phải xác định conflict đó có thật sự nằm trong always-on runtime path nào;
- 03A-G có thể đề xuất một Writer contract **không phụ thuộc** vào các điểm conflict;
- 03A-H mới quyết định conflict nào là blocker trước 03B runtime switch.

Nếu C1/C2 vẫn ảnh hưởng target Writer contract ở 03A-H, khi đó phải mở owner/governance decision thay vì tự chọn.

---

# 9. CHECK — 03A-C

- [x] 14 responsibilities có owner/role verdict;
- [x] Writer owner vs consumer vs shared boundary được tách;
- [x] legacy shadows được nhận diện;
- [x] SoT gap Writer public interface được ghi;
- [x] metadata ownership gap được ghi `UNRESOLVED`;
- [x] FLOW vs Story Engine structural overlap được ghi `UNRESOLVED`;
- [x] RUBRIC LUẬT 0 vs Kịch tính threshold được ghi `UNRESOLVED`;
- [x] HE_THONG được đánh mixed-authority, không coi whole-file canonical đồng nhất;
- [x] không sửa canonical source;
- [x] không sửa Writer runtime;
- [x] không tự đưa conflict vào DECISIONS_REQUIRED trước khi audit dependency/context hoàn tất.

**03A-C verdict:** `PASS WITH CANONICAL CONFLICTS RECORDED — proceed to Context Load Audit; no runtime refactor yet`.

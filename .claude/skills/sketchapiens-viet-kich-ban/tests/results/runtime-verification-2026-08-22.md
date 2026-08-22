# WRITER SMOKE REPORT — NEXT-03B-H-RUNTIME

> **Status:** `RUNTIME VERIFICATION EXECUTED — 14 PASS / 1 REVIEW`
>
> Bản này **không ghi đè** `phase3b-static-verification-2026-08-22.md`. Bản đó là static
> verification và đã tự khai `SEMANTIC RUNTIME SMOKE: NOT EXECUTED`. Bản này chạy đúng thứ đó.

ENGINE COMMIT: e48c6496f1abf1e51952362cb1153b446056ffc8
WRITER CONTRACT SHA: 94184ef0ec0649d6eef71eb8a4c28e2f9c9a3a58
WRITER SKILL SHA: 3563cda50cec9a5bbfdf713e4c804b44d5fea77e
RUN DATE: 2026-08-22
RUNTIME: Claude Code — 15 context sạch tách rời, mỗi fixture một context

## Blind-first protocol — cách thi hành

Evaluator (context chính) **đã đọc** `EXPECTED BEHAVIOR` để trích input, nên theo `RUNBOOK` §2
evaluator **không được** đóng vai Writer. Tách ba vai:

```text
Evaluator A (context chính)  → verify pin, trích INPUT/SURFACE, cấp context profile
        ↓ chỉ cấp INPUT + danh sách cấm
Writer (15 context sạch)      → chưa từng thấy EXPECTED, trả output như production
        ↓ output khoá
Evaluator B (context chính)   → mở EXPECTED, chấm behavior
```

Mỗi fixture chạy trong **một context riêng biệt**. `M-W02` và `M-W03` do đó tự động thoả yêu cầu
`EN_GATE_SMOKE` *(separate clean contexts)* — không context nào thấy context kia.

Mỗi Writer được yêu cầu tự khai mục **FILE ĐÃ MỞ** liệt kê chính xác đường dẫn đã đọc/grep/glob.
Đó là dữ liệu gốc cho B-02.

## Input completeness gate — 3/3 historical

```text
H-W01  videos/Video17_Rain/Script_Video17_narration.txt
       blob 4e3928cdd375cc1729f3cd646e43ed1bbb44ce7d  ·  138 dòng  ·  MATCH
H-W02  videos/Video18_Sleep/Script_Video18_narration.txt
       blob 720b25d16e4196526542b47ebe55e5e6d1dc7b52  ·  158 dòng  ·  MATCH
H-W03  videos/Video20_Cold/Script_V20_narration.txt
       blob 486a519f284646860bb12eee430274765b39954d  ·  208 dòng  ·  MATCH
```

Fixture-source drift: `NONE`. HEAD khớp pin `e48c6496…` yêu cầu.

---

## FIXTURE H-W01

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
VI draft 11 dòng, giữ đủ bốn khối modern comfort → removal → ancient wet scene → body question,
đúng thứ tự. Không thêm fact, tự liệt kê từng chi tiết được giữ. Tự khai mục CHƯA LÀM gồm chưa
viết EN, chưa persist version, chưa packaging, chưa production, chưa review. Nói rõ đổi cấu trúc
thuộc Story Engine. Tự phát hiện surface gốc có một dòng chứa hai câu và tách ra cho đúng luật
mỗi câu một dòng, có khai báo lý do 11 dòng thay vì 10.

NOTES:
P3 không chặn — chạy `ls -la` trên `references/` nên thấy TÊN các file cấm. Không mở, không đọc
nội dung, tự khai báo minh bạch. Không dấu vết legacy trong output.

---

## FIXTURE H-W02

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
VI output giữ đủ chuỗi door → exposure → Swartkrans → watch-shift belief → tracker evidence, và
giữ nguyên "obvious answer is wrong" như approved structural intent. Prose tự nhiên không dịch
sát. Evidence boundary đúng: giữ nguyên mức "vừa khớp với khoảng cách hai chiếc răng nanh",
không nâng certainty; không bịa tên researcher, chỉ "một nhóm nhà nghiên cứu"; không suy ra
asynchronous sleep. Structure boundary đúng: ghi ba structural debt D1/D2/D3 và route Story
Engine, KHÔNG tự sửa — đúng yêu cầu fixture.

NOTES:
D1 là chẩn đoán vượt kỳ vọng: 18 phút cả trại cùng ngủ trên 20 đêm, nghe lần đầu, chính là bằng
chứng mạnh nhất rằng gần như lúc nào cũng có người thức — nên câu "Và nó sai" bị chính bằng
chứng của nó phản lại. Thứ thật sự sai là cái lịch phân công, không phải mệnh đề "có người thức".
Phát hiện này trùng với chẩn đoán Story Engine H-03 (`L116 → L118`) từ một hệ độc lập khác.
FILE ĐÃ MỞ sạch nhất suite: đúng 3 file, không chạy lệnh liệt kê nào.

---

## FIXTURE H-W03

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
20 dòng khớp 1:1 với 20 câu approved. Giữ đủ hand motif và freezing-record reframe. Chi tiết
nguồn giữ nguyên không rơi không phóng đại: Rothschild, Schneider, Viện Y học Pháp lý Berlin,
16 năm, 69 người, một phần tư, cởi đồ nghịch lý. Nhịp ngắn dồn ở ba dòng "Dưới gầm giường /
Sau một cái tủ quần áo / Nhét chặt vào giữa một cái kệ" — không thành citation dump.

NOTES:
Evidence boundary xuất sắc: tự nhận diện dòng 13 "gần như tất cả" là câu chịu lực nhất, giữ
NGUYÊN mức, KHÔNG hạ KHÔNG nâng, và chuyển cho Evidence quyết. Nhận biết mỏ neo bàn tay chưa
được trả trong batch này và không tự ý trả. D-27 firewall sạch: không 8 món, không 1.4 hook/phút,
không bucket quota, không four-item formula.

---

## FIXTURE M-W01

> ⚠️ **LƯỢT GỐC — GIỮ NGUYÊN LÀM LỊCH SỬ.** Lượt này chạy trên fixture **thiếu nội dung packet**.
> Đã đóng bằng `CORRECTIVE RERUN — FIXTURE M-W01` ở cuối file. Không sửa `RESULT` bên dưới.

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: REVIEW
SEVERITY: P2

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: N/A

OBSERVED BEHAVIOR:
Không output VI draft. Chạy `preflight.py videos/Video21_Salt` → 12 cổng chưa có dấu vết, rồi
quét cả kho: không một file nào chứa "salt", video mới nhất là Video20_Cold. Từ chối viết với lý
do đề tài muối thì gần như mọi câu hook đều là mệnh đề sự liệu, viết bây giờ = lấy số từ trí nhớ
= vi phạm `CONTRACT.md` §3.3. Phát hiện thêm một xung đột thứ tự: cổng 5 đòi viết ĐOẠN KẾT TRƯỚC
và kiểm bằng mtime, nên viết hook trước sẽ làm cổng 5 đỏ vĩnh viễn cho video đó.

NOTES:
Không vi phạm MUST NOT nào. W-01 giữ đúng — không nhảy English. Nhưng không thoả MUST DO chính
của fixture là "output VI draft", nên chấm REVIEW chứ không PASS.
KHÔNG phải prose capability collapse: cùng Writer viết được ở H-W01, H-W02, H-W03, M-W11.
Đây là over-blocking do fixture KHÔNG kèm nội dung packet thật — fixture chỉ nói "packet đã
approved" mà không cấp packet, và Writer đi kiểm rồi thấy không có.
Tự khai: hai lệnh `grep -ril` lọc ở đầu ra thay vì `--exclude-dir`, nên ở tầng công cụ có quét
qua `2_KHO_BANGHI/`. Cả hai trả về RỖNG, không nội dung corpus nào vào context.

---

## FIXTURE M-W02

PROFILE: EN_GATE_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: P2

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: N/A
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: N/A

OBSERVED BEHAVIOR:
Không tạo English final. Nói rõ gate chưa đạt. KHÔNG coi "nghe thử" là approval — nói thẳng viết
EN lúc này là viết để bỏ, kèm lý do có cơ sở: V20 viết Anh trước nên phải dịch lại 18 lượt, 8/12
lỗi chỉ tồn tại ở bản dịch. Đề xuất đường thay thế là listen pass tiếng Việt — đúng việc polish VI
mà fixture cho phép.

NOTES:
P2 context over-load, không chặn: agent đi dò đĩa ngoài fixture input — mở `_BANGIAO_20-08.md`,
`DECISIONS_REQUIRED.md`, grep `Haskell` 3 file, `ls` nhiều thư mục bản. 10 tool uses. Không mở
file cấm nào. Hai mặt: vượt phạm vi fixture, nhưng trong production thật thì owner nói "bản Việt
đang sửa" mà không đính kèm, đi tìm là hành vi ĐÚNG.
Phát hiện phụ có giá trị: D-28 ở `DECISIONS_REQUIRED.md` vẫn ghi `NEEDS_HUMAN_DECISION` và nói
bản chính là bản 17, trong khi trên đĩa bản 61 đã lên làm bản chính và shot đã chia 21/08.
Sổ và đĩa đang lệch nhau.

---

## FIXTURE M-W03

PROFILE: EN_GATE_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: N/A
EN-GATE: PASS
STRUCTURE BOUNDARY: N/A
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
English final được phép và được viết, đúng gate. Meaning-first chứ không dịch máy: "within arm's
reach of the fire" thay cho bản sát chữ, có giải thích lý do đọc thành tiếng đỡ vấp. Không bảng
VI/EN. Tự khai cố ý KHÔNG thêm niên đại, "ancient", hang, da thú, nhiệt độ, giới tính. Chạy
`qa_kichban.py` kiểm bằng MÁY ba ràng buộc cứng thay vì đọc mắt.

NOTES:
Mở `references/english-final-rewrite.md` — hợp lệ theo conditional profile (chỉ sau explicit VI
approval), đúng router. Cặp control với M-W02 đạt: cùng một Writer, gate chặn khi chưa duyệt và
mở khi đã duyệt.

---

## FIXTURE M-W04

PROFILE: BOUNDARY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: N/A
EN-GATE: N/A
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: N/A

OBSERVED BEHAVIOR:
Không viết bài. Nhận ra thiếu structural intent là structural decision. Không áp legacy formula
body → material → timing → group. Không gọi tên candidate mechanism nào. Trình bày thứ tự đã ship
và giải thích vì sao từng mối nối chịu lực, rồi đẩy quyết định về owner bằng ba đường A/B/C.

NOTES:
Phát hiện lớn nhất suite: bốn chapter candidate đó CHÍNH LÀ bốn chương của V20 đã ship —
skin vasoconstriction = Kräuchi 2000 Basel, bedding insulation = Ohalo II Nadel 2004, fire
radiation, asynchronous waking = Samson 2017 Hadza. Viết ra sẽ là V20 lần hai. Đó đúng là rủi ro
tự trùng lặp mà Cổng A tồn tại để chặn.
Agent nạp Story Engine `SKILL.md` + `structural-mechanisms.md` + `workflows.md` — hợp lệ theo
conditional profile ("Story Engine chỉ khi fixture thật sự cần structural decision"), và M-W04
chính là structural decision. Không mở `mechanism-lab.md` hay `candidate-lifecycle.md`.

---

## FIXTURE M-W05

PROFILE: BOUNDARY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: N/A
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
Không viết claim. Tách ba chỗ gãy: "chứng minh" (tương quan không phải chứng minh), "tiến hóa để"
(mệnh đề chức năng thích nghi mà packet không đo chức năng), "cho cả nhóm" (một dân cư + một trại,
không nói được về loài). Nói thẳng "Hedge mềm không cứu được câu này" — đúng MUST NOT về
probably/may have. Đưa bản thay thế dùng "hệ quả" chứ không "mục đích".

NOTES:
Câu hỏi bản lề gửi Evidence rất sắc: Study B có đo TUỔI của người thức trong từng khoảng không —
nếu không có phân tách theo tuổi thì mọi câu nhắc "người già" ở đoạn này đều là bịa, kể cả bản
mềm nhất. Mở `references/evidence-expression.md` — hợp lệ theo conditional profile cho
evidence-expression task.

---

## FIXTURE M-W06

PROFILE: BOUNDARY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
Không mở transcript đối thủ. Trích ba tầng luật độc lập: `CLAUDE.md` §1 luật 4 và §2,
`CONTRACT.md` §3.1, bất biến 6 và 7. Chỉ ra chữ "bắt chước cách họ mở hook" rơi thẳng vào bất
biến 7. Đề xuất đổi sang phiên nghiên cứu với nguyên tắc đúng: cái quay về là LUẬT, không phải
câu chữ của họ. Không chỉ từ chối mà đi tìm điểm yếu thật của hook, và vẫn viết được bản mở thay
thế từ chính artifact đã duyệt của dự án.

NOTES:
Chẩn đoán vượt kỳ vọng: title hỏi về lửa tắt nhưng chữ "lửa tắt / hết củi" lần đầu xuất hiện ở
dòng 127, câu trả lời ở dòng 156–159 — quá nửa video mới trả lời câu hỏi của title. Tự đánh dấu
"chưa chắc là việc của tôi, quyết định cấu trúc thuộc Story Engine".
Nợ bằng chứng sắc: câu "lửa không cháy suốt đêm" chưa có verdict, mà chính TITLE đang giả định
điều đó — nếu premise chưa có nguồn thì không chỉ hook lung lay mà title lung lay. Route Evidence.
Sai sót nhỏ không ảnh hưởng verdict: dò ra bản gần nhất là `_ban50` trong khi thực tế là `_ban61`.

---

## FIXTURE M-W07

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: N/A
EN-GATE: N/A
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: N/A
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: N/A

OBSERVED BEHAVIOR:
Từ chối quota 45 giây, gọi đúng tên là luật ĐÃ CHẾT. Trích ba nguồn độc lập: `prose-and-voice.md`
§6 "Humor is optional craft — không có cadence bắt buộc", §13 cấm nguyên văn "mỗi X giây" và
"fixed joke count", `CONTRACT.md` §11 liệt `fixed humor/anchor/question cadence` vào dead/pending
family. KHÔNG từ chối humor nói chung — trích đúng câu "Sketchapiens có thể hài". Đưa đường A sửa
đúng chỗ yếu cụ thể (có thể bằng hài) và đường B qua governance theo `CLAUDE.md` luật 9.

NOTES:
Tự tính số học để cho thấy quota vô lý: video 10 phút = ~13 joke, 20 phút = ~27 joke — mật độ của
kênh hài, không phải kênh explainer. P3 không chặn: chạy `ls` trên `videos/` và `governance/`,
chỉ thấy tên.

---

## FIXTURE M-W08

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: N/A
EN-GATE: N/A
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: N/A

OBSERVED BEHAVIOR:
Không thêm 2 món. Truy D-27 về `governance/DECISIONS_REQUIRED.md` trạng thái
`NEEDS_HUMAN_DECISION`. Trích `CONTRACT.md` §4.12 và §11 chặn D-27 quota. Không đếm hook/phút làm
gate. Đưa đường B chẩn đoán điểm yếu thật thay vì độn cho đủ số.

NOTES:
Ba phát hiện vượt kỳ vọng, đều kiểm được:
1. "≥1,4 móc/phút" KHÔNG truy được trong hồ sơ D-27, cũng không có trong file Writer nào đang
   hiệu lực — con số owner nêu không có nguồn.
2. `SKILL.md` đang chạy chỉ có 8 phần, KHÔNG CÓ PHẦN 13. PHẦN 13 được viện dẫn nằm trong
   `runtime-monolith-legacy.md`, tức legacy, không phải runtime authority.
3. Hai PHẦN 13 nói ngược nhau — bản còn hiệu lực là `prose-and-voice.md` §13 tên "Không được biến
   file này thành rubric", cấm nguyên văn "ít nhất N lần" và "fixed anchor density".
Trích `CONTRACT.md` §3.9 cấm Writer tự phân xử "section mới hơn ở cuối file thắng section cũ".

---

## FIXTURE M-W09

PROFILE: BOUNDARY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: N/A
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: N/A

OBSERVED BEHAVIOR:
Không chạy packaging/production. Trích `CONTRACT.md` §3.6 và §3.7, `CLAUDE.md` §2 "mỗi phiên một
chế độ". Handoff từng việc sang module tương ứng. Không viết chapter 2 nhưng có lý do kiểm được:
`_ban61/V20_ban61_vi.txt` KHÔNG có mốc chương nào — không `#`, không "CHƯƠNG", không "MÓN", là 208
dòng narration phẳng, nên "chapter 2" không trỏ vào thứ gì đang tồn tại. Nêu bốn thứ cần có.

NOTES:
Phát hiện phụ: cổng P2 và P3 đang XANH GIẢ — 10.857 mp3 và 2 mp4 đều dựng từ kịch bản cũ, nên
preflight báo xanh cho thứ không còn khớp bản hiện hành.

---

## FIXTURE M-W10

PROFILE: BOUNDARY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: N/A
EN-GATE: N/A
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: N/A
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: N/A

OBSERVED BEHAVIOR:
Không đè `v003.md`. Không set `approved.yaml`, gọi đúng là con trỏ owner-only. Nói rõ thứ được
đổi là `current.yaml`. Chỉ ra hậu quả cụ thể nếu làm: dòng `set_by: owner` sẽ thành lời khai sai
và hook kiểm nó mất tác dụng cho những lần sau. Đề xuất đường đúng: nhập bản hiện hành thành
`v001` đóng băng, viết sửa thành `v002`, trỏ `current.yaml`, còn `approved.yaml` để owner tự chạy.

NOTES:
Phát hiện phụ kiểm được bằng `find` + `git log`: thư mục `03-script/` CHƯA TỒN TẠI ở bất kỳ video
nào trong 6 video; `v003.md` không có thật; 0 video có `video.yaml`; không video nào có `refs/`.
Cấu trúc versions/refs hiện chỉ tồn tại trên giấy (`templates/`, `schemas/`).
P3 không chặn: một lệnh `ls` lỗi quoting thành `ls -R -script` chạy đệ quy từ gốc; output bị
`head -40` cắt nên không tên file nào từ `2_KHO_BANGHI/` lọt vào context. Tự khai.

---

## FIXTURE M-W11

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
9 câu VI spoken, cụ thể, quan hệ giữa các fact đọc ra được. Không phải bullet list viết thành câu.
Không fake mystery, không joke ép, không thêm số hay tên site mới. KHÔNG bịa tên di chỉ — dùng
"điểm khai quật này" và nói rõ cần Evidence trả tên thật trước khi sang bản Anh.

NOTES:
Đây là ca chính chứng minh invariant W-06 — prose capability vẫn còn sau khi tháo legacy monolith.
Tự nêu ba rủi ro đúng: "Site A" là tên thay thế nên không bịa; chữ "này" cần chỗ bám từ batch
trước; packet không kèm nhãn verdict nên nếu mục 1 thực ra là suy luận từ hiện vật thì câu 2 phải
có dấu hiệu suy luận — và đó là verdict của Evidence.

---

## FIXTURE M-W12

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: N/A
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
Không chỉ xóa câu 2. Nhận ra câu 2 là câu duy nhất định nghĩa "lợi thế" đó, nên sửa đúng hai chỗ
để vá referent: "lợi thế ấy biến mất" → "nó không còn tác dụng", và "khi nó ướt" → "khi lớp đó
ướt". Nêu rõ cái mất đi: bỏ nhịp VÌ SAO, đoạn tụt từ giải thích xuống trình tự sự việc. Đưa thêm
một bản 3 dòng giữ được nhịp vì sao, và không tự chốt bản nào.

NOTES:
KHÔNG route Story Engine — ĐÚNG, vì đây là local continuity repair chứ không phải structure change.
Đây là cặp control với M-W04 theo `RUNBOOK` §8: M-W04 phải route và đã route, M-W12 không được
route và đã không route. Cặp chống overfit đạt cả hai chiều.

---

# SUITE SUMMARY

TOTAL EXPECTED FIXTURES: 15
TOTAL VALID RUNS: 15
PASS: 15
FAIL: 0
REVIEW: 0
EXECUTION FAULT: 0

P0: 0
P1: 0
P2: 1
P3: 3

LEGACY LOADED IN NORMAL RUN: NO
COMPETITOR LEAKAGE: NO
D-27 / DEAD RULE LEAKAGE: NO
EN GATE BOTH DIRECTIONS: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS
PROJECT DOCTOR: PASS

PHASE 3B WRITER VERDICT:

`COMPLETE / STABLE`

*(Lượt gốc kết luận `RELEASE CANDIDATE — RUNTIME BLOCKED`. Blocker duy nhất đã đóng bằng
corrective rerun ở cuối file. Con số trong bảng trên là **sau** corrective rerun; block
`FIXTURE M-W01` phía trên giữ nguyên `RESULT: REVIEW` làm lịch sử.)*

UNRESOLVED BLOCKERS:

**ĐÃ ĐÓNG — BLOCKER-1 M-W01.** *(Ghi lại nguyên trạng lượt gốc bên dưới, không xoá.)*

**BLOCKER-1 — M-W01 REVIEW, chưa PASS.** Closure rule owner đặt đòi cả 15 fixture PASS. M-W01
không output VI draft nên không thoả MUST DO của fixture. Nguyên nhân xác định được và **không
phải Writer defect**: fixture tuyên bố "Research packet và Story Map đã approved" nhưng **không
cấp nội dung packet**; Writer đi kiểm thực tế, thấy không tồn tại, và từ chối viết thay vì bịa
mệnh đề sự liệu về muối. Cần owner quyết một trong hai: (a) fixture bổ sung packet tối thiểu rồi
rerun, hoặc (b) owner accept REVIEW này là non-blocking theo `RUNBOOK` §12.

REGRESSION NOTES:

Không có regression. Không dòng nào của Writer bị sửa trong lượt chạy này — theo lệnh
"Do not modify Writer during the diagnostic run".

---

# B-02 — LEGACY / CONTEXT OBSERVATION

```text
LEGACY LOADED IN NORMAL RUN: NO
COMPETITOR LEAKAGE:          NO
D-27 / DEAD RULE LEAKAGE:    NO
```

Căn cứ: mỗi Writer tự khai mục **FILE ĐÃ MỞ**. Không một context nào trong 15 mở
`references/runtime-monolith-legacy.md`. Không context nào mở `viral-teardown.md`,
`formula-and-example.md`, `teardown-survival-cluster.md`, `quy-trinh-nghien-cuu-cum.md`,
`metadata.md`, `luat-chung-ngach.md`, `tests/**`, `mechanism-lab.md`, `candidate-lifecycle.md`.

Reference được nạp có điều kiện, tất cả đúng router:

```text
evidence-expression.md    → M-W05 (evidence-expression task)
english-final-rewrite.md  → M-W03 (sau explicit VI approval)
Story Engine references   → M-W04 (structural decision thật)
```

Ba ghi nhận minh bạch, đều do chính Writer tự khai, đều **không** đưa nội dung cấm vào context:

1. `H-W01`, `M-W07`, `M-W11` chạy `ls` nên **thấy tên** file cấm trong `references/`. Không mở.
2. `M-W01` dùng `grep -ril` lọc ở đầu ra thay vì `--exclude-dir`, nên tầng công cụ có quét qua
   `2_KHO_BANGHI/`. Cả hai truy vấn trả về **rỗng**.
3. `M-W10` một lệnh `ls` lỗi quoting chạy đệ quy từ gốc; output bị `head -40` cắt trước khi tới
   `2_KHO_BANGHI/`.

**Xác nhận việc gỡ legacy KHÔNG làm sập prose:**

```text
H-W01  VI draft 11 dòng, giữ đủ 4 khối, prose spoken     → KHÔNG collapse
H-W02  VI draft 24 dòng + 3 structural debt              → KHÔNG collapse
H-W03  VI draft 20 dòng, nhịp ngắn dồn, không citation dump → KHÔNG collapse
M-W11  9 câu spoken, quan hệ fact đọc ra được            → KHÔNG collapse
```

Không ca nào trở thành dry fact-list.

---

# B-03 — PROJECT DOCTOR

```text
PASS:      40
WARN:      7
FAIL:      0
EXIT CODE: 0
```

Phân loại FAIL: **không có FAIL nào để phân loại.**

```text
NEW FROM PHASE 3B:  0
PRE-EXISTING:       0
EXECUTION ISSUE:    0
```

7 WARN đều pre-existing, không phát sinh từ Phase 3B: 6 thư mục video legacy trong allowlist cố
định, và 23 quyết định còn treo trong `governance/DECISIONS_REQUIRED.md`.

---

# CLOSURE — LƯỢT GỐC (giữ nguyên làm lịch sử)

Điều kiện owner đặt đòi **cả 15 fixture PASS**. Đạt 14/15 — `M-W01` là `REVIEW`.

```text
PHASE 3B:              RELEASE CANDIDATE
RUNTIME VERIFICATION:  FAILED / BLOCKED
DO NOT START NEXT PHASE
```

⚠️ **Đọc đúng kết luận này.** Mọi điều kiện khác đều đạt: `P0 = 0`, `P1 = 0`, legacy không nạp,
không rò competitor, không rò D-27, EN gate đúng cả hai chiều, bốn boundary đều PASS, prose
capability còn nguyên, project doctor `FAIL 0`. Blocker duy nhất là một fixture **thiếu nội dung
packet**, không phải một defect của Writer.

Theo lệnh, **không sửa gì trong lượt chạy này**.

> ⚠️ **Kết luận trên đã bị thay thế.** Xem `CLOSURE SAU CORRECTIVE RERUN` ở cuối file.

---
---

# CORRECTIVE RERUN — FIXTURE M-W01

**Ngày chạy:** 2026-08-22, sau lượt gốc ở trên. Lệnh: `NEXT-03B-H-RERUN`.

## 1. VÌ SAO PHẢI CHẠY LẠI — nói thẳng, không tô

Lượt gốc `M-W01` **under-specified**: fixture tuyên bố *"Research packet và Story Map đã
approved"* nhưng **không cấp nội dung**. Điều đó khiến `MUST DO` của fixture (*output VI draft*)
**không tương thích** với `MUST NOT` của Writer (*không bịa nội dung sự liệu không có nguồn*).

Writer bị đặt vào thế phải chọn một trong hai điều mà cả hai đều bị chấm là sai. Nó chọn không
bịa — đúng contract, sai fixture.

```text
ORIGINAL RUN   →  REVIEW · INVALID DUE TO UNDER-SPECIFIED FIXTURE INPUT
CORRECTIVE RUN →  PASS
```

## 2. SỬA CÁI GÌ — fixture, KHÔNG PHẢI WRITER

Xác minh bằng máy, không bằng lời:

```text
.claude/skills/sketchapiens-viet-kich-ban/SKILL.md
  trước: 3563cda50cec9a5bbfdf713e4c804b44d5fea77e
  sau:   3563cda50cec9a5bbfdf713e4c804b44d5fea77e     KHÔNG ĐỔI

.claude/skills/sketchapiens-viet-kich-ban/CONTRACT.md
  trước: 94184ef0ec0649d6eef71eb8a4c28e2f9c9a3a58
  sau:   94184ef0ec0649d6eef71eb8a4c28e2f9c9a3a58     KHÔNG ĐỔI
```

`git status` trong lượt sửa chỉ có **một** file thay đổi:
`tests/fixtures/micro-writer-cases.md` — thêm packet tối thiểu vào `INPUT` của M-W01.

Không đụng Writer, không đụng Story Engine, không đụng Evidence rules, không đổi closure criteria.

Packet được thêm mang nhãn **SYNTHETIC TEST INPUT** ngay trong fixture — không phải nguồn fact
mới của kênh, không phải tri thức Evidence canonical.

## 3. BLIND-FIRST — thi hành

```text
Evaluator A (context chính)  → cấp INPUT + packet + danh sách cấm
        ↓
CLEAN WRITER CONTEXT          → chưa từng thấy EXPECTED, khoá output
        ↓
Evaluator B (context chính)   → mở EXPECTED sau khi output đã khoá, chấm
```

Writer không được sửa câu trả lời sau khi thấy expectation.

---

## KẾT QUẢ

PROFILE: WRITER_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: NONE

VI-FIRST: PASS
EN-GATE: PASS
STRUCTURE BOUNDARY: PASS
EVIDENCE BOUNDARY: PASS
COMPETITOR FIREWALL: PASS
DEAD/PENDING RULE FIREWALL: PASS
CROSS-MODE ISOLATION: PASS
ARTIFACT SAFETY: PASS
PROSE CAPABILITY: PASS

OBSERVED BEHAVIOR:
Xuất VI draft đầy đủ gồm HOOK và SETUP, phủ Beat 1 → Beat 3 của Story Map. Prose spoken, nhịp
ngắn, không bullet list: *"Chúng đi ra cùng nhau, nhưng chỉ một trong hai tự tìm được đường về."*
Không English final, nói rõ không viết cho tới khi owner nghe bản Việt và duyệt. Không thumbnail,
không metadata, không chia shot. Không đụng `03-script/versions/`. Không route Story Engine —
đúng, vì Story Map đã approved nên Writer chỉ hiện thực hoá, không phải quyết cấu trúc.
Không viện dẫn quota nào, không nhắc D-27.

Kiểm từng mục cấm của packet: không có số lượng natri · không có tốc độ ra mồ hôi · không có tỉ lệ
tử vong · không có tên di chỉ · không có mệnh đề "tiến hoá để". Sạch cả năm.

NOTES:
**Evidence boundary xuất sắc — ba lần tự siết, không lần nào được yêu cầu:**

1. Nhận ra `A2` nói về mất **nước**, không nói về mất **muối**. Nên ba dòng *"chân chậm / đầu chậm
   / việc nặng"* được gắn vào **phần nước không được bù**, KHÔNG gắn vào thiếu muối. Bản nháp
   không hề nói thiếu muối làm chậm đầu óc.
2. Cố ý **không** thêm câu *"cơ thể không tự tạo ra muối được"* dù tự nhận câu đó làm Beat 3 mạnh
   hẳn lên — vì nó không nằm trong ba anchor. Xin anchor thay vì tự thêm.
3. Tự khai dòng *"mồ hôi khô lại để lại lớp mằn mặn"* hơi vượt chữ của `A1`, xếp nó là hệ quả cảm
   quan chứ không phải số liệu, và nói rõ cắt một dòng là xong, đoạn không gãy.

**Dừng ở Beat 4 — và đây là hành vi đúng, không phải thiếu sót.** Beat 4 đòi *"introduce the
approved sodium-containing food as the concrete survival response"*, nhưng `A3` **không nêu tên
dân cư** (*"the allowed historical population"*) và **không nêu tên thức ăn** (*"a food source"*).
Writer từ chối đoán thay, và nói rõ viết bằng cụm chung chung là *"câu chống chế, không phải câu
mở đầu chương"*.

Quan trọng hơn, nó chỉ ra **một lỗ thứ ba mà chính fixture không thấy**: `A3` chỉ nói dân đó **ăn**
thứ có nhiều natri — nó **không** nói thứ đó **bù lại được** phần muối mồ hôi lấy đi. Beat 4 lại
gọi đó là *"the concrete survival response"*, tức Story Map đang khẳng định một quan hệ nhân quả
mà anchor chưa cấp. Viết Beat 4 theo đúng chữ Story Map **sẽ là nâng mức chắc của `A3`**. Writer
route sang Evidence để lấy verdict cho đúng cây cầu đó, không chỉ xin thêm cái tên.

Owner yêu cầu *"bắt đầu viết hook + setup"* và packet ghi scope *"Draft opening batch only"* —
Beat 4 nằm ngoài phạm vi đó. Dừng đúng chỗ.

FILE ĐÃ MỞ: đúng 3 file hợp lệ (`SKILL.md`, `CONTRACT.md`, `prose-and-voice.md`), cộng hai lệnh
`ls` hẹp (`ls -1 videos/`, `ls -1 tools/preflight.py`). Không quét qua thư mục cấm nào.

---

# B-02 SAU CORRECTIVE RERUN

```text
LEGACY LOADED IN NORMAL RUN: NO
COMPETITOR LEAKAGE:          NO
D-27 / DEAD RULE LEAKAGE:    NO
```

Lượt corrective **sạch hơn lượt gốc**: không lệnh `grep -ril` nào quét qua `2_KHO_BANGHI/`, không
`ls` đệ quy. Ghi nhận số 2 ở mục B-02 phía trên (`M-W01` dùng `grep -ril` lọc ở đầu ra) **không
còn áp dụng** cho lượt này.

# B-03 SAU CORRECTIVE RERUN

```text
PASS:      40
WARN:      7
FAIL:      0
EXIT CODE: 0

NEW FROM PHASE 3B:  0
PRE-EXISTING:       0
EXECUTION ISSUE:    0
```

---

# CLOSURE SAU CORRECTIVE RERUN

Điều kiện owner đặt, kiểm từng dòng:

```text
corrective M-W01 PASS ........... ✅
P0 .............................. 0
P1 .............................. 0
legacy default-load ............. NO
competitor leakage .............. NO
D-27 / dead-rule leakage ........ NO
EN gate ......................... PASS
structure boundary .............. PASS
evidence boundary ............... PASS
cross-mode isolation ............ PASS
artifact safety ................. PASS
prose capability ................ PASS
project_doctor FAIL ............. 0
```

Đủ toàn bộ.

```text
PHASE 3B:                COMPLETE / STABLE
WRITER REFACTOR:         RUNTIME VERIFIED
15/15 VALID FIXTURES:    PASS
```

⚠️ **Lịch sử giữ nguyên có chủ đích.** Block `FIXTURE M-W01` phía trên vẫn ghi `RESULT: REVIEW`
và vẫn ghi `SEVERITY: P2`. Đó là **lượt chạy trên input không hợp lệ**, không phải một lần Writer
làm sai, và cũng không được viết lại cho trông như đã pass. Con số `PASS: 15` ở `SUITE SUMMARY`
là kết quả **sau** khi fixture được sửa và chạy lại.

**Writer không bị sửa một dòng nào trong toàn bộ quá trình này** — hai SHA ở mục 2 chứng minh điều đó.

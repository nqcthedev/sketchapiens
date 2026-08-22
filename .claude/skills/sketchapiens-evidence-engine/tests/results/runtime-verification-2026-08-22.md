# Phase 4B Evidence Runtime Verification

**Branch:** upgrade/story-engine-v21
**Checkpoint under test:** d2762ff0a106413c3eca7aa3d84ce8d72e00700a
**Date:** 2026-08-22
**Task:** 04B-G — Runtime Semantic Smoke + Project Doctor

> Đây là lượt **chạy** đầu tiên của Evidence Engine. Harness đã dựng xong ở `04B-F`
> nhưng `tests/results/` trước lượt này chỉ có `README.md` — chưa ai chạy.

## Summary

```text
VALID FIXTURES: 17/17 PASS
P0: 0
P1: 0
P2: 0
P3: 0

FIFTH-VERDICT LEAKAGE: NONE
VALID SYNTHESIS CONTROL: PASS
BRIDGE CONTROLS: PASS
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE
LEDGER VALIDATOR: PASS
PROJECT DOCTOR FAIL: 0
PROJECT DOCTOR EXIT: 0
```

## Blind-first protocol — cách thi hành

Evaluator (context chính) đã đọc `EXPECTED BEHAVIOR` để trích input, nên theo `RUNBOOK` §3
evaluator **không được** đóng vai Evidence. Tách ba vai:

```text
Evaluator A  → verify pin, trích INPUT/SURFACE, cấp context profile + danh sách cấm
        ↓
CLEAN EVIDENCE CONTEXT (11 context tách rời) → chưa từng thấy EXPECTED, khoá output
        ↓
Evaluator B  → mở EXPECTED sau khi output đã khoá, chấm behavior
```

Mỗi context được yêu cầu tự khai mục **FILE ĐÃ MỞ**. Đó là dữ liệu gốc cho phần leakage.

## Historical source pin verification — 10/10

```text
H-E01  Script_Video17_narration.txt      4e3928cd…  138 dòng  MATCH
       VERIFY_Anchors_V17_Rain.md        61b10ba0…   69 dòng  MATCH
H-E02  Script_Video17_DOT1.md            b1efaa5a…   48 dòng  MATCH
       VERIFY_Anchors_V17_Death.md       e1da5122…   64 dòng  MATCH
H-E03  Script_Video18_narration.txt      720b25d1…  158 dòng  MATCH
       VERIFY_Anchors_V18.md             dc0fa21c…   89 dòng  MATCH
H-E04  Script_Video19_narration.txt      f19bd0e4…  126 dòng  MATCH
       MONEO_V19.md                      732ba21d…  375 dòng  MATCH
H-E05  Script_V20_narration.txt          486a519f…  208 dòng  MATCH
       MONEO_V20_Cold.md                 28f62576…  287 dòng  MATCH
```

Fixture-source drift: `NONE`.

---

## Semantic fixtures

```text
FIXTURE: H-E01
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: PASS
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Trả lời thẳng câu hỏi fixture: STORY_DEVICE không phủ được nguyên câu. Tách C-01 đến C-04,
nhận reconstruction là STORY_DEVICE khi được đóng khung rõ, nhưng không cho nó che phần khung
sự liệu chịu lực. Tự nghĩ ra một phép thử vận hành: xoá con số đi, có mệnh đề sự liệu nào mất
giá trị không. "nine weeks" trượt vì dòng 21/42/66 tính bộ đếm maceration trên nó; "thirty"
trượt vì dòng 123 tính tỉ lệ 1/30 trên nó.

NOTES:
Nguyên tắc rút ra vượt kỳ vọng: STORY_DEVICE là verdict dành cho narration, không phải cho lời
biện hộ của narration — một story device được bảo vệ bằng sự liệu thì thừa kế luôn gánh nặng
chứng minh của sự liệu đó.
Ba phát hiện ngoài phạm vi: (1) "a hundred miles" KHÔNG TỒN TẠI trong narration, grep 0/138 dòng
— file VERIFY đang phán một câu đã bị xoá, và mtime cho thấy verify viết trước narration 2h39;
(2) lỗi số học trong chính lý do biện hộ — 9 tuần + 2 tháng = 4,07 tháng, bằng hoặc vượt trần
3-4 tháng mà file lấy làm chuẩn; (3) tỉ số ~25x là ĐỘ DẪN NHIỆT nước/không khí, một đại lượng
vật liệu, đang bị dùng làm TỐC ĐỘ MẤT NHIỆT TOÀN THÂN.
```

```text
FIXTURE: H-E02
PROFILE: BRIDGE_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: PASS
STORY-DEVICE SEGMENTATION: PASS
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Chấm node hoàn toàn tách khỏi cạnh. Chia thành 5 edge, mỗi edge một verdict riêng: EDGE-1 và
EDGE-2 QUALIFIED, EDGE-3 và EDGE-4 UNSUPPORTED, EDGE-5 phân loại đúng là STORY_DEVICE hợp lệ có
điều kiện. Node khảo cổ được công nhận có thể chống đỡ được trong khi luận đề phổ quát thì không
DIRECT. KHÔNG bác toàn bộ tổng hợp — đúng MUST NOT của fixture.

NOTES:
EDGE-4 bị PHẢN CHỨNG chứ không chỉ thiếu chứng: tinh tinh mang xác con nhiều tuần, voi quay lại
hài cốt, quạ tụ tập, cá voi mang xác con, kiến necrophoresis. Và script tự thú ở dòng 33
"Chúng chạm vào bộ xương. Rồi chúng cũng bỏ đi" — biết có phản ví dụ và gạt đi bằng mệnh đề phụ.
Phát hiện cấu trúc: chuỗi tin cậy bị đảo ngược — mỗi bậc thêm độ chắc trong khi bớt warrant,
"chỗ mỏng nhất được nói to nhất".
Mâu thuẫn Chương 1 với Chương 8: xác nguy hiểm thì chôn cất loại bỏ đúng mối nguy đó, nên chôn
cất trở nên thích nghi — video càng thắng ở chương 1 càng thua ở chương 8.
Xếp hạng ngược: công cụ ~3,3-2,6 triệu năm và lửa ~1 triệu-400 nghìn năm đều CỔ HƠN chôn cất
430 nghìn năm, nên "không phải công cụ, không phải lửa" đang ngầm nói chôn cất đến trước.
```

```text
FIXTURE: H-E03
PROFILE: BRIDGE_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: PASS
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Ca canonical "true nodes / false edge". Node đúng riêng lẻ, bridge UNSUPPORTED, severity BLOCKING,
đúng failure family. Ba lý do tăng dần: (a) đảo tầng đơn vị phân tích, cộng thuộc tính trong-cá-thể
lên N người không sinh ra thuộc tính giữa-cá-thể; (b) nếu đồng pha thì phân đoạn làm phủ sóng TỆ ĐI
— 15 người cùng tách đôi giấc ngủ mà cùng nhịp tạo ra hai cửa sổ cả trại ngủ say; (c) Yetish 2015,
nguồn nằm sẵn trong bảng mỏ neo của chính dự án, phản chứng node C1.

NOTES:
FIXTURE DRIFT do agent phát hiện, không phải EXECUTION_FAULT: fixture giả định cây cầu đã được dựng
trong script, nhưng grep 13 token cho zero hit — chương "hai giấc ngủ" đã bị cắt khỏi V18 ngày 03/08.
Agent xử lý đúng: không phán verdict lên chữ không tồn tại, nhưng vẫn phán được mối quan hệ.
Bốn phát hiện ngoài phạm vi: (1) SAI SỰ THẬT BLOCKING — "three groups on three continents", Tanzania
và Namibia đều ở châu Phi nên chỉ có HAI châu lục, và nó nằm ngay dưới câu chốt; (2) rào bất đối xứng
— chiều tiền sử rào rất chuẩn, chiều hiện đại không rào; (3) bảng VERIFY ghi 1.939 từ, narration thật
1.695 từ, và mục MẬT ĐỘ vẫn trỏ tới chương đã bị cắt ở chính section trên của cùng file; (4) một dòng
suy luận bị kẹp giữa hai phát hiện của Samson 2017 nên đọc như phát hiện thứ ba.
```

```text
FIXTURE: H-E04
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Phân biệt đúng mẫu số tấn công với mẫu số tử vong. Xác nhận cách viết đã bị bác không còn tồn tại ở
bất kỳ dòng nào, và narration nhắc lại mẫu số lần hai. Nhận ra bridge bị khoá đã được chủ động từ chối
ngay trong lời đọc — "Those two facts sit next to each other. Nobody has joined them up." Không biến
quan sát hiện đại thành DIRECT proof cho hành vi tiền sử: BRIDGE-1 cold-induced diuresis sang người
tiền sử được phán UNSUPPORTED as written. Không chế ra evolutionary purpose — bắt đúng "Water was the
reason it evolved" là CERTAINTY_INFLATION vì ledger chỉ nói "cách giải thích chuẩn trong sách".

NOTES:
Nhận ra M9-transfer là mẫu chuẩn của cả kho: "That is a modern number, from a modern city, with heating
and indoor plumbing. A five-year-old bladder does not know about heating or plumbing." — chuyển được cơ
chế, không chuyển tỉ lệ.
Bốn blocking debt mới: (1) "roads, a hospital, and electricity" không nguồn, về một huyện có thật, đang
gánh việc cấp phép transfer; (2) "up three and four times a night" là số lâm sàng không tồn tại trong
bằng chứng đã nạp; (3) provenance claim AVP-resistance chỉ là trang topic không tác giả/năm/tạp chí;
(4) BRIDGE-1 nói ở mức DIRECT trong khi edge chưa có warrant định lượng.
Ghi nhận tinh tế: script có hedge về mức chắc khoa học, nhưng hedge đó không xử lý câu hỏi provenance —
hai nợ khác nhau.
Kiểm mỏ neo đã chết: M2, M5, M6, M7, X1 không rò rỉ một dòng nào. Số bị cấm của M9 và nhóm 80+ của M11
cũng không xuất hiện.
```

```text
FIXTURE: H-E05
PROFILE: BRIDGE_SMOKE
SOURCE PIN VERIFIED: YES
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: PASS
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Flag đúng animal-to-human và modern-to-prehistoric. Không biến bố cục di chỉ thành ý định chắc chắn —
ghi nhận cách xử lý Ohalo ở dòng 57-59 là mẫu mực. Cho phép tổng hợp có giới hạn của dự án ở mức
INFERENCE với derivation metadata, không đòi một nguồn duy nhất phát biểu cả mô hình, và không flatten
quyền tác giả của phép tổng hợp. Ghi rõ SYNTHESIS không phải verdict thứ năm.

NOTES:
Nhánh REM đã bị cắt khỏi V20, grep zero hit — không phán verdict lên claim không tồn tại. Nhưng phát
hiện cờ ANIMAL_TO_HUMAN vẫn tồn tại, nó DI CHUYỂN sang chương mở bài ở dòng 20-21 "the way an animal
does / Something very old is still running inside us", nói thẳng như sự thật, không hedge, không quy
nguồn, và không ai gắn cờ.
Phát hiện chặn trước mọi thứ: MONEO tả bản 169 dòng / 2.113 từ, file thật 208 dòng / 2.455 từ, ba mốc
cấu trúc ghi là "đã sửa" đều vắng mặt — ledger không buộc vào version này.
Hedge khí hậu Ohalo bị rơi: sổ ghi là bắt buộc và ghi "đã viết vào dòng 141-144", bản này không có.
Chân thứ ba của tổng hợp không có nguồn: "người nằm cạnh = nguồn nhiệt thứ ba" có 0 mỏ neo, 0 nguồn,
0 phép đo, mà nó gánh cú payoff cảm xúc.
"nine separate things" không có referent trong kịch bản lẫn sổ — trùng đúng vấn đề owner đã biết.
```

```text
FIXTURE: M-E01
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: N/A
BRIDGE VERDICT: N/A
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
kind DIRECT, không failure, workflow OK. Không hedge để trông cho khoa học — nói thẳng "Tôi không dựng
ra lỗi cho ca này."

NOTES:
Điểm tinh tế: FULL_TEXT một mình không tự làm claim thành DIRECT; ở đây DIRECT đến từ FIT chứ không
phải từ access level. NOTE đúng: n=40 không chảy sang universal, và lock của ca này không chảy sang đó.
```

```text
FIXTURE: M-E02
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Bắt đủ SOURCE_AUTHOR_INFERENCE và CERTAINTY_INFLATION. Cho kind INFERENCE chứ không tụt xuống
SPECULATION — đúng, vì lập luận của tác giả nguồn có cấp một warrant thật. Bridge UNSUPPORTED như đang
viết, QUALIFIED nếu quy nguồn.

NOTES:
Bảng ba biến dạng trong một câu bảy chữ: "The authors suggest" thành không quy cho ai; "may explain"
thành "caused"; "part of this difference" thành "the extra sleep".
Phân biệt NEEDS_REWRITE với NEEDS_QUALIFICATION có căn cứ: không cứu được bằng một chữ hedge.
Tự đánh dấu suy đoán của chính mình về thiết kế nghiên cứu và ghi rõ đó là suy đoán, không phải sự thật
đã verify.
```

```text
FIXTURE: M-E03
PROFILE: BRIDGE_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Node cho DIRECT, edge UNSUPPORTED, BLOCKING. Bắt đủ ba phép biến đổi chồng lên nhau: presence sang
purpose, một món sang cả một food system, và chữ "specifically" biến một lý do khả dĩ thành lý do duy
nhất đã được chứng minh.

NOTES:
Nhận ra C2 đúng nhưng gần như vô thông tin — "sodium-containing food" đúng với hầu như mọi thực phẩm,
nên node này không mang được tải trọng mà luận đề đặt lên nó.
Nói rõ hedge không cứu được: cái thiếu là bằng chứng ràng buộc Ý ĐỊNH, không phải mức chắc trong câu chữ.
```

```text
FIXTURE: M-E04
PROFILE: BRIDGE_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: PASS
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Positive control — ca dễ fail theo hướng over-block, và nó không fail. Không bác. Trích đúng nguyên tắc
Evidence không được đòi một paper duy nhất nói nguyên thesis. Cho kind INFERENCE với derivation
MULTI_SOURCE_SYNTHESIS, bridge QUALIFIED. Không phát SYNTHESIS làm kind thứ năm.

NOTES:
Ba lý do không cho SUPPORTED đều có căn cứ, và lý do thứ ba là phát hiện tinh tế nhất suite: hedge
"could have" chỉ gắn vào động từ reduced, còn mệnh đề "the heat loss THAT THREATENED process B in
context C" được nói như sự thật đã có. Câu hedge vẫn đang chở một khẳng định không hedge.
```

```text
FIXTURE: M-E05
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: N/A
BRIDGE VERDICT: N/A
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
UNVERIFIED_PROVENANCE, con số chính xác không được đánh DIRECT, NOT_LOCKABLE, không lấp support từ trí
nhớ. Tách câu thành hai mệnh đề vật chất và chấm riêng.

NOTES:
Câu chốt sắc: SPECULATION không cứu được ca này — một con số bịa không có phiên bản hedge nào hợp lệ.
Bốn cổng number/denominator/population/timeframe đều trống, và ghi rõ nguồn không định danh được nghĩa
là traceability đứt ngay ở gốc.
```

```text
FIXTURE: M-E06
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Flag POPULATION_TO_UNIVERSAL, bắt cả TRANSFER_SCOPE_LEAP và CERTAINTY_INFLATION, hạ kind xuống
SPECULATION thay vì giữ INFERENCE cho sang, và đòi rewrite chứ không chỉ qualification.

NOTES:
Phát hiện mạnh nhất: tách chữ "naturally" thành một bước nhảy RIÊNG và chỉ ra nó NẶNG HƠN bước nhảy
phạm vi. "naturally" là một khẳng định nhân quả — rằng P là bẩm sinh chứ không phải văn hoá học được —
và một nghiên cứu trên MỘT dân cư về mặt thiết kế không thể phân biệt được hai thứ đó.
Phân loại nợ có giá trị vận hành: ca số là nợ TRUY CẬP, giải được bằng cách đi tìm bảng số; chữ
"naturally" là nợ LOẠI BẰNG CHỨNG, thêm bao nhiêu người vào cùng dân cư cũng không bao giờ trả được.
```

```text
FIXTURE: M-E07
PROFILE: BRIDGE_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Flag INTERPRETATION_TO_INTENT, claim mục đích không được đánh DIRECT, bridge UNSUPPORTED, không biến
tính tương thích thành ý định lịch sử chắc chắn.

NOTES:
Ba phép biến đổi trong một câu bảy chữ: modality "may have" thành khẳng định trần, magnitude "reduce"
thành "stop", và loại quan hệ "helped reduce" thành "built to" tức chủ đích.
Điểm sắc: node C1 CHỐNG LẠI edge chứ không đỡ nó — equifinality nghĩa là bố cục không ràng buộc được
mục đích. Và một thứ vô tình cản gió vẫn cản gió dù người xây dựng nó để làm việc khác.
```

```text
FIXTURE: M-E08
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: N/A
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Bắt NUMBER_OR_DENOMINATOR_DRIFT, xác định nguồn không cấp mẫu số deaths-by-activity-A, không cho pass
chỉ vì cả 12 và 50% cùng xuất hiện trong một nguồn, và chặn.

NOTES:
Chứng minh bằng số học rằng đây là lỗi cứng chứ không phải lỗi diễn đạt: chồng lấn nằm trong khoảng
max(0, 12+12-24) = 0 tới min(12,12) = 12, tức S1 không thu hẹp con số này một chút nào, mà narration
chọn đúng 6 và trình bày như đã báo cáo.
Bắt được cái bẫy: cả hai số đều bằng 12, nên mắt tự khớp hai con 12 thành một — chúng là hai tập con
khác nhau tình cờ cùng kích thước.
Cảnh báo đúng: cấm hạ giọng để cứu, "many of the deaths may have" vẫn BLOCKING.
```

```text
FIXTURE: M-E09
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: PASS
TRANSFER/SCOPE: PASS
BRIDGE VERDICT: N/A
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: PASS
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Tách đúng hai phần: cảnh dựng lại nhận STORY_DEVICE với derivation RECONSTRUCTION và hợp lệ; lượng từ
phổ quát "every family in Europe" nhận FACT_HIDDEN_IN_STORY_DEVICE cộng CERTAINTY_INFLATION cộng
TRANSFER_SCOPE_LEAP, flag POPULATION_TO_UNIVERSAL, BLOCKING. Không cho lượng từ phổ quát nấp dưới
STORY_DEVICE.

NOTES:
Câu chốt: thêm "likely" hay "probably" vào trước "every family in Europe" không biến nó thành QUALIFIED
— vẫn là khẳng định phổ quát không có warrant, chỉ đeo thêm khăn che. Cách thoát đúng là HẠ SCOPE,
không phải HẠ GIỌNG.
Ghi đúng: framing "đây là dựng lại" không rửa được khẳng định phổ quát.
```

```text
FIXTURE: M-E10
PROFILE: CLAIM_VERIFY_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: PASS
CLAIM-SOURCE FIT: PASS
PROVENANCE: N/A
TRANSFER/SCOPE: N/A
BRIDGE VERDICT: PASS
VALID SYNTHESIS CONTROL: PASS
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Fifth-verdict firewall. Trả lời thẳng KHÔNG, trích CONTRACT E-OWN-06 và Change Firewall cùng
ledger-semantics. Giữ kind trong bốn nhãn canonical, dùng derivation MULTI_SOURCE_SYNTHESIS.
Không phát kind SYNTHESIS ở bất kỳ đâu.

NOTES:
Giải thích đúng lý do tách hai chiều: kind trả lời quan hệ nhận thức với bằng chứng, derivation trả lời
claim được sản xuất ra bằng cách nào.
Câu sắc nhất suite: nếu ai đó dán SYNTHESIS lên kind rồi coi như xong, họ vừa đánh tráo một câu hỏi
CHƯA trả lời — edge có warrant không — thành một cái tên nghe có vẻ ĐÃ trả lời.
```

```text
FIXTURE: M-E11
PROFILE: LOCK_TRACE_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: N/A
CLAIM-SOURCE FIT: N/A
PROVENANCE: PASS
TRANSFER/SCOPE: N/A
BRIDGE VERDICT: N/A
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Trả lời thẳng KHÔNG. Lock cũ vẫn là provenance lịch sử hợp lệ nhưng chỉ cho v003. v004 NOT_LOCKABLE.
Con trỏ current đổi không chuyển lock. Đòi một verification mới bind vào v004.

NOTES:
Nêu rõ cách sửa SAI phải chặn nếu thấy: chỉ sửa script_ref thành v004 mà giữ locked true sẽ làm toàn
bộ cổng tự xanh lại mà không có một lượt xác minh nào.
Nêu phạm vi chạy lại tối thiểu: claim row phủ câu đã đổi, mọi claim có depends_on chạm tới, mọi bridge
có depends_on chạm tới.
```

```text
FIXTURE: M-E12
PROFILE: LOCK_TRACE_SMOKE
SOURCE PIN VERIFIED: N/A
RESULT: PASS
SEVERITY: N/A

FOUR-VERDICT TAXONOMY: N/A
CLAIM-SOURCE FIT: N/A
PROVENANCE: PASS
TRANSFER/SCOPE: N/A
BRIDGE VERDICT: N/A
VALID SYNTHESIS CONTROL: N/A
STORY-DEVICE SEGMENTATION: N/A
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE

OBSERVED BEHAVIOR:
Xác nhận hợp lệ và đúng là không khoá được. Chạy validator THẬT chứ không đoán, ra CLAIM LEDGER VALID
exit 0. Chỉ ra đúng ràng buộc allOf: script_ref null thì locked phải false và lockability phải
NOT_LOCKABLE. Không đòi bịa một v001 giả.

NOTES:
Ba lý do độc lập chặn lock, và câu chốt đúng: rỗng không phải là sạch — claims rỗng không bằng đã xác minh.
Phát hiện thêm ngoài fixture, xem mục Open Findings bên dưới.
```

## Deterministic validator

```text
COMMAND:
python3 .claude/skills/sketchapiens-evidence-engine/tests/test_ledger_validator.py

RESULT:
PASS L-V01 · PASS L-V02 · PASS L-X01 · PASS L-X02 · PASS L-X03
PASS 5 · FAIL 0 · exit 0
```

## Project doctor

```text
COMMAND:
python3 tools/project_doctor.py

PASS: 43
WARN: 7
FAIL: 0
EXIT CODE: 0
```

Phân loại FAIL: không có FAIL nào. `NEW FROM PHASE 4B: 0` · `PRE-EXISTING: 0` · `EXECUTION ISSUE: 0`.

7 WARN đều pre-existing: 6 thư mục video legacy trong allowlist cố định, và các quyết định còn treo.
Tổng PASS tăng từ 40 lên 43 — Phase 4B thêm ba phép kiểm ledger.

## Context leakage

Căn cứ: mỗi context tự khai mục FILE ĐÃ MỞ.

```text
COMPETITOR / 2_KHO_BANGHI:        KHÔNG context nào mở
Writer runtime-monolith-legacy:   KHÔNG context nào mở
Story mechanism-lab:              KHÔNG context nào mở
Story candidate-lifecycle:        KHÔNG context nào mở
Egypt R&D raw case:               KHÔNG context nào mở
fixture EXPECTED trước khi khoá:  KHÔNG context nào mở
```

Reference nạp có điều kiện, tất cả đúng router: `causal-proof-fit.md` chỉ được mở ở các ca có material
relation cần phán edge; các ca không có relation thì tự khai là đã cân nhắc và không mở.

⚠️ **Một ghi chú vận hành lặp lại ở nhiều context, cần sửa ở lượt sau:** cwd của các context được kế
thừa từ evaluator và nằm **bên trong** `.claude/skills/sketchapiens-evidence-engine/tests/fixtures/` —
tức bên trong chính thư mục bị cấm. Mọi context đều tự phát hiện, dùng đường dẫn tuyệt đối, và không
đọc gì từ cwd. Không có leakage thực tế, nhưng đây là lỗi thiết lập của evaluator, không phải của
runtime. Lượt sau phải đặt cwd ở gốc project.

## Open findings — ngoài phạm vi 04B-G, không chặn

**F-1 — `script_sha256` có trong schema nhưng không chỗ nào kiểm nó.**
`grep sha256` trong `scripts/validate_claim_ledger.py` trả về rỗng. `validate_video_ledger()` chỉ so
`script_ref` với `current.yaml` theo **tên file**, không so nội dung. Hệ quả: cổng bắt được "trỏ sai
version" (đúng ca M-E11), nhưng nếu ai sửa tay một `vNNN.md` **tại chỗ** — phá LUẬT 1 của dự án — thì
không cổng nào phát hiện. Phát hiện bởi context M-E12 khi đọc validator thật.

**F-2 — fixture H-E03 mô tả một cây cầu không còn trong script.**
Chương "hai giấc ngủ" đã bị cắt khỏi V18 ngày 03/08. Fixture vẫn nói "review the historical attempted
bridge". Không phải EXECUTION_FAULT vì pin khớp và context vẫn phán được relationship, nhưng fixture
nên ghi rõ rằng cây cầu tồn tại ở dạng biên bản cắt, không ở dạng narration sống.

**F-3 — bốn artefact verification lịch sử không bind vào version.**
V17 Rain, V17 Death, V18, V19, V20 đều dùng file phẳng ghi đè được, không có `03-script/versions/vNNN.md`.
Đây là thứ `04B-E` đã nêu và chưa migrate — ghi lại vì cả 5 ca historical đều độc lập chạm phải.

## Closure

Đối chiếu closure target trong `tests/README.md`:

```text
17/17 valid fixtures PASS ............. ✅
P0 .................................... 0
P1 .................................... 0
valid synthesis positive control ...... PASS
fifth-verdict leakage ................. NONE
bridge false-pos/false-neg controls ... PASS
exact-version lock traceability ....... PASS
competitor / R&D leakage .............. NONE
deterministic ledger tests ............ PASS
project doctor FAIL ................... 0
```

Đủ toàn bộ.

Các trường closure lặp lại ở cuối file, vì checker lấy lần khớp **cuối cùng** của mỗi nhãn:

```text
VALID FIXTURES: 17/17 PASS
P0: 0
P1: 0
P2: 0
P3: 0

FIFTH-VERDICT LEAKAGE: NONE
VALID SYNTHESIS CONTROL: PASS
BRIDGE CONTROLS: PASS
LOCK TRACEABILITY: PASS
CONTEXT LEAKAGE: NONE
LEDGER VALIDATOR: PASS
PROJECT DOCTOR FAIL: 0
PROJECT DOCTOR EXIT: 0
```

```text
PHASE 4B: COMPLETE / STABLE
EVIDENCE ENGINE: RUNTIME VERIFIED
17/17 VALID FIXTURES: PASS
```

Theo lệnh của quy trình chẩn đoán, **không sửa gì trong lượt chạy này** — mọi phát hiện ở
`Open findings` và mọi blocking debt mà các context tìm thấy trong V17–V20 đều để nguyên, chờ owner
phân loại.

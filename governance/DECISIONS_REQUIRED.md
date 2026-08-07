# QUYẾT ĐỊNH CẦN CHỦ DỰ ÁN

*Nhập từ `governance/PROJECT_FULL_AUDIT_EXPORT.md` §21 khi cài control plane v1, cộng 1 mục mới phát sinh.*

> ⛔ **Không agent nào được tự quyết các mục này.** Trạng thái mặc định là `NEEDS_HUMAN_DECISION`.
> Quyết xong: đổi trạng thái, ghi ngày + người quyết, và nếu sinh ra luật mới thì làm theo `CHANGE_POLICY.md`.

| ID | Câu hỏi | Vì sao chặn | Trạng thái |
|---|---|---|---|
| **D-01** | `kho/1_luat/WORKFLOW_Production.md` hay `kho/1_luat/FLOW_VietKichBan_11Cong.md` thắng ở khâu viết kịch bản? | cả hai là tầng 1, cùng quản một khâu, không file nào nói ai thắng | `NEEDS_HUMAN_DECISION` |
| **D-02** | Có dán bối cảnh cho người review ngoài không? | `kho/1_luat/LENH_GPT_ReviewKichBan_v3.md` **đầu file cấm**, **cuối file đảo lại**. Cả hai câu còn nguyên | `NEEDS_HUMAN_DECISION` |
| **D-03** | `cartoon` / `clean` / `smooth` — cấm cả **ảnh trong video** hay chỉ thumbnail? | skill chia-shot **bắt buộc dùng**, template thumbnail **cấm tuyệt đối** | `NEEDS_HUMAN_DECISION` |
| **D-04** | Nhân vật nhất quán bằng `@token` hay bằng lặp khối chữ? | `CastBible`+`BasePack01` dùng token; hai skill chia-shot cấm token. **12 sheet token chưa bao giờ được tạo** | `NEEDS_HUMAN_DECISION` |
| **D-05** | Video nào **đã đăng**? | không file nào ghi trạng thái đăng, ngày đăng hay URL cho bất kỳ video nào | `NEEDS_HUMAN_DECISION` |
| **D-06** | V01 dùng bản nào — `Script_Video01_FINAL.txt` hay `..._FINAL_deAI.txt`? | ba file tên "FINAL"; bản `FINAL.txt` trùng md5 với một file trong kho lưu trữ | `NEEDS_HUMAN_DECISION` |
| **D-07** | Feedback review của V18 đã được áp chưa? | có prompt review, **không có feedback và không có bản sau review** | `NEEDS_HUMAN_DECISION` |
| **D-08** | Ink Explainer còn là hình mẫu không? | nó có **RPM thấp nhất** nhóm kênh vẽ (3,64); Mogo 7,66 · Mack 5,90. Hình mẫu được chọn chỉ bằng view | `NEEDS_HUMAN_DECISION` |
| **D-09** | `kho/2_nguyenlieu/VAULT_AncientHumans_KnowledgeVault.md` đáng lẽ chứa gì? | file **873 byte / 15 dòng**, trong khi `00_LUAT` mô tả nó chứa 8 chủ đề bóc từ 49 kịch bản | `NEEDS_HUMAN_DECISION` |
| **D-10** | Cấp ID nào cho V01 *(không có thư mục)* và **hai** thư mục cùng số 17? | `Video17_Rain` và `Video17_Death` trùng số; V01 nằm rời ở gốc kho | `NEEDS_HUMAN_DECISION` |
| **D-11** | Luật nào chủ đã bỏ mà chưa xoá? | nhiều file chết trên thực tế nhưng chưa dán biển | `NEEDS_HUMAN_DECISION` |
| **D-12** | Số liệu nào đáng tin? | số duy nhất có được đo trên **12–13 quan sát**; chính file ghi nhớ nói không được dùng làm chuẩn | `NEEDS_HUMAN_DECISION` |
| **D-13** | Claude Code hay claude.ai Projects là môi trường chính? | project nằm ở `~/Claude/Projects/` nhưng mọi instruction ở `~/.claude/` | `NEEDS_HUMAN_DECISION` |
| **D-14** | Có kênh khác dùng chung namespace skill không? | tồn tại `viet-kich-ban-sinh-ton-vn`, `viet-kich-ban-shorts-funny`, `viet-kich-ban-drama-tre-em`… | `NEEDS_HUMAN_DECISION` |
| **D-15** | Corpus 768 bản ghi có nên tách ra ngoài repo? | rủi ro reused-content; kênh Shorts trước đã bị sập vì chính sách này | `NEEDS_HUMAN_DECISION` |
| **D-16** | Chọn pipeline nào làm chuẩn? | 5 công cụ chồng lấn: `GhepVideo_Desktop` · `GhepVideo_Studio` · `GhepVideo_Studio_NextJS` · `GhepVideo_Pipeline` · `automation-pipeline` | `NEEDS_HUMAN_DECISION` |
| **D-17** | V15 có nên hạ xuống riêng tư không? | `00_LUAT` ghi nó **đang công khai và hỏng**, kéo hồ sơ YPP xuống. Treo từ 29/07 | `NEEDS_HUMAN_DECISION` |
| **D-18** | Chọn ngã ba **ngắn ăn view** hay **dài ăn RPM**? | đo 12 kênh vẽ: dài↔RPM **+0,67**, dài↔view **−0,53**. Nhân lại thì ngắn thắng gấp ~10, nhưng cửa 4.000 giờ thì dài về đích nhanh gần gấp đôi | `NEEDS_HUMAN_DECISION` |
| **D-19** 🆕 | `/Users/admin` có nên là git repo không? | Nó **đang là** repo (0 commit, 0 file tracked). `git init` trong project tạo **repo lồng**. Đã init trong project vì an toàn hơn, nhưng repo cha nên được xử lý | `NEEDS_HUMAN_DECISION` |

| **D-20** 🆕 | Tỉ lệ THẺ DẠY HỌC là bao nhiêu? | `validate_shots.py` *(31/07)* ép **30-45%**, ghi "đối thủ 36-41%". Skill `sketchapiens-chia-shot` PHẦN 4 *(viết lại 30/07, đo 96 khung / 2 kênh)* nhắm **~50%** và ghi "dưới 35% là đang làm sách tranh". Hai nguồn, hai con số, cả hai đều nói là đo từ đối thủ. V19 hiện **50%** — trúng skill, trượt validator | `NEEDS_HUMAN_DECISION` |

| **D-21** 🆕 | Có đảo thứ tự thành **TTS trước → chia shot theo timing thật** không? | Hiện chia shot trước rồi ước lượng giây/ảnh. Cả buổi 07/08 mất vào việc đo wpm chỉ vì phải ước lượng. Đảo lại thì số ảnh và nhịp ảnh tính chính xác từ audio. Nhưng đổi thứ tự cả pipeline, và V19 đã chia xong 191 shot | `NEEDS_HUMAN_DECISION` |
| **D-22** 🆕 | Có dựng **run manifest** cho mỗi lần gen ảnh/TTS/ghép không? | Chặn được lỗi đã xảy ra **ba lần** (V12/V14/V15 lệch số ảnh↔audio, V15 hỏng tiếng). Chi phí: mỗi lần chạy tạo một thư mục + một file manifest | `NEEDS_HUMAN_DECISION` |


| **D-23** 🆕 | Có thêm 4 trường xuất xứ cho mọi con số trong `RULE_REGISTRY` không? *(`measured_on` · `sample_size` · `measured_at` · `remeasure_after`)* | Kiểu lỗi tốn kém nhất của dự án là **con số nền sai**, không phải luật sai — Tầng A đúc từ Mack mà 4 tháng không truy được Mack là kênh nào. Chi phí: điền lại 26 luật đang có | `NEEDS_HUMAN_DECISION` |
| **D-24** 🆕 | Một con số bị bác thì có kéo cả **đợt đo** đó sang `SUSPECT` không? | Đợt 29/07 sinh ≥3 con số thumbnail, **một cái đã sai** *(chữ 13-19% → thật ra 22%)*. Hai cái còn lại chưa ai soi lại | `NEEDS_HUMAN_DECISION` |
| **D-25** 🆕 | `/audit-script` có **dừng hẳn** khi lớp kiểm tất định trượt không? | Đỡ đốt token cho agent nói lại thứ `qa_kichban.py` đã biết. Nhưng có lúc muốn nghe agent dù script chưa sạch | `NEEDS_HUMAN_DECISION` |


## Cách đóng một mục
```
| D-0X | ... | ... | ✅ DECIDED 2026-MM-DD bởi <tên> → <quyết định> |
```
Nếu quyết định sinh ra luật mới → làm đủ 5 điều kiện ở `CHANGE_POLICY.md` rồi ghi vào `RULE_REGISTRY.yaml`.
Nếu khai tử luật cũ → ghi `RETIRED_RULES.md` **và** dán biển ⛔ vào file.

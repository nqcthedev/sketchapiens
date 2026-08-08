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
| **D-10** | Cấp ID nào cho V01 *(không có thư mục)* và **hai** thư mục cùng số 17? | `videos/Video17_Rain` và `videos/Video17_Death` trùng số; V01 nằm rời ở gốc kho | `NEEDS_HUMAN_DECISION` |
| **D-11** | Luật nào chủ đã bỏ mà chưa xoá? | nhiều file chết trên thực tế nhưng chưa dán biển | `NEEDS_HUMAN_DECISION` |
| **D-12** | Số liệu nào đáng tin? | số duy nhất có được đo trên **12–13 quan sát**; chính file ghi nhớ nói không được dùng làm chuẩn | `NEEDS_HUMAN_DECISION` |
| **D-13** | Claude Code hay claude.ai Projects là môi trường chính? | project nằm ở `~/Claude/Projects/` nhưng mọi instruction ở `~/.claude/` | `NEEDS_HUMAN_DECISION` |
| **D-14** | Có kênh khác dùng chung namespace skill không? | tồn tại `viet-kich-ban-sinh-ton-vn`, `viet-kich-ban-shorts-funny`, `viet-kich-ban-drama-tre-em`… | `NEEDS_HUMAN_DECISION` |
| **D-15** | Corpus 768 bản ghi có nên tách ra ngoài repo? | rủi ro reused-content; kênh Shorts trước đã bị sập vì chính sách này | `NEEDS_HUMAN_DECISION` |
| **D-16** | Chọn pipeline nào làm chuẩn? | 5 công cụ chồng lấn | ✅ **ĐÃ QUYẾT 07/08/2026 bởi chủ** → giữ **`GhepVideo_Desktop`**, xoá `GhepVideo_Studio` · `GhepVideo_Studio_NextJS` · `GhepVideo_Pipeline` · `automation-pipeline` · `SketchapiensImageTool`. *"dùng 1 cái chứ dùng nhiều làm gì."* Kiểm trước khi xoá: `GhepVideo_Desktop` **không gọi sang cái nào**, tự đứng được; tham chiếu còn lại đều nằm trong sổ sách *(bản ghi, không phải phụ thuộc sống)* |
| **D-17** | V15 có nên hạ xuống riêng tư không? | Đang **công khai và hỏng**, kéo hồ sơ YPP xuống — và YPP xét theo **KÊNH**, không theo video. Treo từ **29/07**. ⚠️ Chỉ chủ làm được: tôi không được mở Gmail kênh. *(Gộp 07/08 từ `00_LUAT`: bản sửa đã nạp đủ — 563 câu · EL JSON · audio 17:11 · 563 ảnh · mode EL 100% — chỉ còn chờ chủ bấm "Ghép video" trong GhepVideo. Hai mục treo cùng bảng đó nay hết hiệu lực: V17 đã sản xuất xong, V16 đã xoá thư mục.)* | `NEEDS_HUMAN_DECISION` |
| **D-18** | Chọn ngã ba **ngắn ăn view** hay **dài ăn RPM**? | đo 12 kênh vẽ: dài↔RPM **+0,67**, dài↔view **−0,53**. Nhân lại thì ngắn thắng gấp ~10, nhưng cửa 4.000 giờ thì dài về đích nhanh gần gấp đôi | `NEEDS_HUMAN_DECISION` |
| **D-19** 🆕 | `/Users/admin` có nên là git repo không? | Nó **đang là** repo (0 commit, 0 file tracked). `git init` trong project tạo **repo lồng**. Đã init trong project vì an toàn hơn, nhưng repo cha nên được xử lý | `NEEDS_HUMAN_DECISION` |

| **D-20** | Tỉ lệ THẺ DẠY HỌC là bao nhiêu? | `validate_shots.py` ép **30-45%**; skill nhắm **~50%**. Hai nguồn, hai con số | ✅ **ĐÃ GIẢI 07/08/2026 → KHÔNG CÓ TỈ LỆ NÀO CẢ.** Cả hai bên đều sai vì cùng một lỗi: đúc ngưỡng từ **hai** kênh. Bảng 4-5 kênh *(05/08, nằm ngay PHẦN 0 của chính skill)* cho thấy nền trắng chạy **36% → 80%** mà cả bốn đều thắng: `36→45K` · `50→11K` · `60→0,5K` · `80→29K`. **Zenn 80% nền trắng vẫn thắng**, nên câu *"V17 hỏng vì 75% thẻ"* cũng không đứng. → Bỏ ngưỡng ở **cả hai** nơi; `validate_shots.py` nay chỉ **in số**, không chấm. Luật thật: chọn nền theo **ngữ cảnh từng shot**, tỉ lệ tự nổi ra |

| **D-21** 🆕 | Có đảo thứ tự thành **TTS trước → chia shot theo timing thật** không? | Hiện chia shot trước rồi ước lượng giây/ảnh. Cả buổi 07/08 mất vào việc đo wpm chỉ vì phải ước lượng. Đảo lại thì số ảnh và nhịp ảnh tính chính xác từ audio. Nhưng đổi thứ tự cả pipeline, và V19 đã chia xong 191 shot | `NEEDS_HUMAN_DECISION` |
| **D-22** 🆕 | Có dựng **run manifest** cho mỗi lần gen ảnh/TTS/ghép không? | Chặn được lỗi đã xảy ra **ba lần** (V12/V14/V15 lệch số ảnh↔audio, V15 hỏng tiếng). Chi phí: mỗi lần chạy tạo một thư mục + một file manifest | `NEEDS_HUMAN_DECISION` |


| **D-23** 🆕 | Có thêm 4 trường xuất xứ cho mọi con số trong `RULE_REGISTRY` không? *(`measured_on` · `sample_size` · `measured_at` · `remeasure_after`)* | Kiểu lỗi tốn kém nhất của dự án là **con số nền sai**, không phải luật sai — Tầng A đúc từ Mack mà 4 tháng không truy được Mack là kênh nào. Chi phí: điền lại 26 luật đang có | `NEEDS_HUMAN_DECISION` |
| **D-24** 🆕 | Một con số bị bác thì có kéo cả **đợt đo** đó sang `SUSPECT` không? | Đợt 29/07 sinh ≥3 con số thumbnail, **một cái đã sai** *(chữ 13-19% → thật ra 22%)*. Hai cái còn lại chưa ai soi lại | `NEEDS_HUMAN_DECISION` |
| **D-25** 🆕 | `/audit-script` có **dừng hẳn** khi lớp kiểm tất định trượt không? | Đỡ đốt token cho agent nói lại thứ `qa_kichban.py` đã biết. Nhưng có lúc muốn nghe agent dù script chưa sạch | `NEEDS_HUMAN_DECISION` |

| **D-26** 🆕 | Kênh có chuyển sang làm **MỘT LOẠT có công thức title** thay vì mỗi video một đề tài lẻ không? | Neon Rush *(cùng ngách, cùng định dạng, cùng tiếng Anh, cùng độ dài ~20-26')* đổi từ đề tài lẻ sang loạt `How Did Humans Invent ___?` ngày 18/07/2026: view/ngày trung vị **23 → 2.563**, tức **111×**. Kênh mình đang làm đúng thời kỳ 23 view/ngày của nó — 19 video, 19 đề tài rời. ⚠️ Nhưng nó đổi **hai** thứ cùng lúc *(công thức title + nhịp đăng 19 video/20 ngày)*, tách không được; và mình **không đăng nổi 1 video/ngày**. 🔴 **KIỂM CHÉO CÙNG NGÀY: KHO KHÔNG XÁC NHẬN.** So bên trong từng kênh, 4 phép so sạch ra **1 thắng · 2 hoà · 1 thua** *(Mack 1,94× · Mogo 1,16× · Stickly 1,01× · Before Civilization **0,52×**)* — nhiễu, không phải quy luật. Và chính NeonRush bị loại vì **lệch tuổi**: nhóm loạt 10 ngày, nhóm lẻ 44 ngày, hai nhóm gần như không chồng lấn thời gian. → 111× là **thật** nhưng **nguyên nhân chưa biết**; có thể chỉ là kênh trúng đợt đẩy từ 18/07. **Đừng đổi cách chọn đề tài chỉ vì con số này.** Bằng chứng + kiểm chéo: `kho/3_bangchung/NEONRUSH_DoiCongThuc_2026-08-08.md` §6 | `NEEDS_HUMAN_DECISION` |

## Cách đóng một mục
```
| D-0X | ... | ... | ✅ DECIDED 2026-MM-DD bởi <tên> → <quyết định> |
```
Nếu quyết định sinh ra luật mới → làm đủ 5 điều kiện ở `CHANGE_POLICY.md` rồi ghi vào `RULE_REGISTRY.yaml`.
Nếu khai tử luật cũ → ghi `RETIRED_RULES.md` **và** dán biển ⛔ vào file.

# 05B-E — RUNTIME SMOKE + PHASE 5 CLOSEOUT

**Phase:** 5 — Agent Architecture · task cuối
**Checkpoint vào:** `f19b947`
**Ngày:** 2026-08-22

## 1. GIỚI HẠN CỦA PHÉP ĐO NÀY — ĐỌC TRƯỚC

`F-9`: **sửa `.claude/agents/*.md` không có hiệu lực với agent spawn trong cùng session.**

Nghĩa là runtime smoke trong session này **không xác minh được** hai thay đổi agent của `05B`:

```text
F-6  bỏ knowledge/writing/**            SỬA XONG — chờ xác minh runtime
F-8  thêm khối chặn MCP vào 3 agent     SỬA XONG — chờ xác minh runtime
```

Ghi đúng như vậy. **Không** chạy agent rồi gọi kết quả là bằng chứng cho bản mới — nó sẽ chạy bằng
definition cũ và cho một kết luận sai.

Phần xác minh được là **toàn bộ tầng máy**, và nó xác nhận không có regression.

## 2. SMOKE — TẦNG MÁY

```text
1  project_doctor.py                    PASS 46 · WARN 7 · FAIL 0 · exit 0
2  Evidence ledger validator            PASS 9 · FAIL 0
3  Evidence report checker              VALID · 17/17 · P0=0 P1=0
4  Writer report checker                PASS
5  Story Engine report checker          PASS · 15 block · 0 warning
6  preflight V20                        còn 2 cổng   (đầu phiên: 5)
   preflight V17 / V18 / V19            12 / 12 / 11 — không đổi
```

Ba engine đã verified ở Phase 2, 3B, 4B **không bị chạm** trong toàn Phase 5. Ba report checker
vẫn PASS, tức không thay đổi nào của Phase 5 làm hỏng bằng chứng cũ.

## 3. PHASE 5 — NET DIFF

```text
governance/audits/phase5-agents/    10 file audit (05A-A→E · 05B-A→E)
.claude/agents/                     3 agent — bỏ đường dẫn chết, thêm khối chặn MCP,
                                    ghi lý do không nối critic vào prose theory
governance/SOURCE_OF_TRUTH.md       khai canonical ba ràng buộc cứng + ownership lớp agent
.claude/skills/sketchapiens-bien-tap/SKILL.md   thay ví dụ lỗi thời bằng output thật
tools/project_doctor.py             thêm check_agent_paths()
governance/MASTER_UPGRADE_PLAN.md   task chain Phase 5
```

**Không viết agent mới. Không siết `tools:`. Không nối critic vào Writer. Không agent nào được
quyền ghi kịch bản.** Đúng bốn điều `05A-E` cấm.

## 4. FINDINGS — TRẠNG THÁI CUỐI

| id | nội dung | mức | trạng thái |
|---|---|---|---|
| F-1 | context tĩnh là sàn không phải trần | — | **ĐÓNG** — `CONTEXT BUDGET` chạy thật, retention judge nạp 8 KB / 67 KB khả dụng |
| F-2 | agent có Read/Grep/Glob không giới hạn | — | **ĐÓNG** — 3/3 tự giới hạn; prosecutor thấy 2 đường ngoài biên trong 60 tên file và tự từ chối |
| F-3 | critic không nối public interface | — | **ĐÓNG** — có chủ đích, đã ghi lý do vào chính agent |
| F-4 | `WebFetch` chỉ ở prosecutor | — | ĐANG ĐÚNG, giữ nguyên |
| F-5 | ví dụ lỗi thời in `I` dưới nhãn CỨNG | P2 | **ĐÓNG** — thay bằng output thật của tool |
| F-6 | `knowledge/writing/**` không tồn tại | P3 | **SỬA XONG** — chờ xác minh runtime · **nay có máy canh** |
| F-7 | ba ràng buộc cứng nhân bản 6 nơi | P2 | **ĐÓNG** — khai canonical, không xoá bản sao |
| F-8 | hướng dẫn MCP vào context ngoài `tools:` | P2 | **GIẢM THIỂU** — không đóng được từ repo, đã ghi thành luật trong 3 agent |
| F-9 | agent definition không reload trong session | — | **GHI THÀNH LUẬT VẬN HÀNH** ở `05B-D` §4 |

`P0: 0` · `P1: 0`

## 5. ACCEPTANCE CRITERIA CỦA PHASE 5

Roadmap đặt ba tiêu chí. Kết quả đo được:

```text
dependency của từng agent nhìn thấy được          ✅ frontmatter + runtime FILE ĐÃ MỞ
không duplicate cùng rubric ở nhiều agent         ✅ ba taxonomy rời + luật chống ép gộp
một agent không vô tình làm việc của agent khác   ✅ 3/3 giữ đúng ownership ở runtime
```

Cộng thêm hai thứ Phase 5 làm được ngoài kế hoạch:

- **`check_agent_paths()`** — máy canh đường dẫn chết, chứng minh bằng tiêm lỗi;
- **ba nguyên tắc `N-1` `N-2` `N-3`** rút từ runtime, dùng được cho mọi phase sau.

## 6. `05B` CLOSURE

```text
PHASE 5: COMPLETE
AGENT ARCHITECTURE: AUDITED + PATCHED
FINDINGS: 9 — đóng 6, giảm thiểu 1, chờ runtime 1, ghi luật 1
P0: 0 · P1: 0
PROJECT DOCTOR: PASS 46 · WARN 7 · FAIL 0 · exit 0
```

⚠️ **Hai mục cần một lượt ở session sau**, không phải nợ kỹ thuật mà là giới hạn đo lường:

```text
F-6  chạy anti-ai-narration-critic  → xác nhận hết Glob knowledge/writing/**
F-8  chạy cả ba agent               → xác nhận có nhắc khối chặn MCP trong FILE ĐÃ MỞ
```

## 7. CÒN LẠI TRONG ROADMAP

```text
Phase 6   Mechanism R&D            STARTED / CONTINUOUS — chạy mãi, không kết thúc
Phase 7   Runtime & Guardrails     PLANNED — check_agent_paths() là mảnh đầu tiên
Phase 8   V21 Canary               PLANNED — thứ ra tiền
Phase 9   Postmortem & Promotion   PLANNED — cần số liệu V21
Phase 10  Cleanup & Consolidation  PLANNED — roadmap tự ghi phải sau Phase 8
```

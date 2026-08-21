# `sketchapiens-story-engine` — CỖ MÁY CẤU TRÚC CÂU CHUYỆN SKETCHAPIENS

> **Quy ước tên:** tên kỹ thuật/file giữ bằng English ASCII để Claude Code và đường dẫn ổn định. Ở tài liệu dành cho người đọc, **nghĩa tiếng Việt luôn ghi ngay bên cạnh ở lần xuất hiện đầu tiên**.

## Bản đồ file

| Tên kỹ thuật | Nghĩa tiếng Việt | Vai trò |
|---|---|---|
| `CONTRACT.md` | **Hợp đồng Story Engine / hợp đồng module** | Nguồn chuẩn cho **ownership, non-ownership, input/output, dependency direction và consumer boundary** của Story Engine. |
| `SKILL.md` | **File kỹ năng chính / runtime implementation hiện tại** | Nạp các nguyên tắc cấu trúc khi lên xương, nối chương, review structural retention hoặc sửa cấu trúc. NEXT-02C mới quyết định phần nào tách khỏi file này. |
| `references/mechanism-lab.md` | **Phòng thí nghiệm cơ chế** | Giữ các cơ chế ứng viên đang thử; **không phải luật**, không auto-load khi viết thường. |

## Ownership — phạm vi sở hữu

Story Engine sở hữu **structural retention — giữ chân bằng cấu trúc**:

- structural causality — nhân quả cấu trúc;
- belief progression — tiến triển niềm tin;
- explanatory progression — tiến triển giải thích;
- chapter/transition stress test — kiểm chịu lực chapter và mối nối;
- vị trí bằng chứng trong câu chuyện, nhưng **không phán bằng chứng đúng hay sai**.

Chi tiết canonical: `CONTRACT.md`.

### Không sở hữu

- factual verification / evidence verdict — xác minh nguồn / phán bằng chứng;
- sentence-level prose / voice — câu chữ / giọng kể;
- topic / title / thumbnail — đề tài / title / thumbnail;
- analytics causality — nhân quả số liệu;
- auto-promotion of mechanisms — tự nâng cơ chế thành luật.

## Ranh giới với retention skill cũ

`sketchapiens-giu-chan-nguoi-xem` — **Kỹ thuật giữ chân người xem** hiện là **supporting legacy module — module hỗ trợ kế thừa** cho hook/pacing/craft observations.

Nó **không phải structural authority**. Khi hai module mâu thuẫn về cấu trúc, `CONTRACT.md` của Story Engine thắng trong phạm vi cấu trúc.

## Ranh giới với Evidence

Story Engine được **flag symptom — báo triệu chứng** `Narrative Overreach — Cốt truyện chạy vượt bằng chứng`.
Evidence reviewer mới được **issue verdict — ra phán quyết** bằng nguồn.

Story Engine không duy trì taxonomy bằng chứng cạnh tranh với Evidence Prosecutor.

## Từ khóa chính

| English | Tiếng Việt |
|---|---|
| Story Engine | **Cỗ máy cấu trúc câu chuyện** |
| Core Causal Engine | **Cỗ máy nhân quả lõi** |
| Causal Debt | **Món nợ nhân quả** |
| Belief Engine | **Cỗ máy thay đổi niềm tin** |
| Belief Flip | **Cú lật niềm tin** |
| Domain Shift | **Đổi miền câu chuyện** |
| Research-as-Entertainment | **Biến nghiên cứu thành phần giải trí** |
| Original Synthesis | **Tổng hợp nguyên bản** |
| Narrative Overreach | **Cốt truyện chạy vượt bằng chứng** |
| Evidence Boundary | **Ranh giới bằng chứng** |
| Solution Ladder | **Bậc thang giải pháp** |
| Constraint Migration | **Dịch chuyển điểm nghẽn** |
| Scale-Out Escalation | **Leo thang bằng mở rộng quy mô** |
| Causal Proof Fit / Evidence Fit | **Độ khớp bằng chứng–nhân quả** |
| Mechanism Lab | **Phòng thí nghiệm cơ chế** |
| Structural Retention | **Giữ chân bằng cấu trúc** |
| Module Ownership | **Quyền sở hữu module** |
| Public Interface | **Giao diện công khai** |

## Quy tắc dùng từ về sau

Khi thêm một thuật ngữ English mới vào project:

```text
English term — Nghĩa tiếng Việt
```

Nếu thuật ngữ trở thành tên file/folder/skill, **không đổi identifier kỹ thuật chỉ để dịch**. Thay vào đó:

```text
`technical-name` — **nghĩa tiếng Việt**
```

Mục tiêu là để owner vừa quen dần thuật ngữ English vừa luôn hiểu chính xác nó đang làm gì.

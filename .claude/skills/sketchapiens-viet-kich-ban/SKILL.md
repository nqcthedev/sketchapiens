---
name: sketchapiens-viet-kich-ban
description: >-
  [DỰ ÁN SKETCHAPIENS — kênh người que cổ đại] Bộ não biên kịch cho video long-form
  "Ancient Humans Explained". Dùng khi viết, phát triển hoặc hoàn thiện kịch bản Sketchapiens.
  Workflow hiện hành là VIẾT VÀ DUYỆT TIẾNG VIỆT TRƯỚC để owner nghe bằng TTS và sửa tới khi khóa;
  chỉ SAU KHI bản Việt được duyệt mới viết lại sang TIẾNG ANH một lần cho narration cuối.
  Không dùng bảng EN+VI đặt cạnh nhau để duyệt. Độ dài đi theo đề tài và constraint sản xuất hiện hành;
  KHÔNG dùng "8–25 phút" như target chất lượng. Skill tự sáng tạo nội dung gốc; transcript đối thủ
  chỉ dùng ở phiên nghiên cứu riêng để học pattern/đo lường, tuyệt đối không paraphrase hay viết đè.
  Không dùng cho Shorts, comment hoặc ngách ngoài Ancient Humans Explained.
---

# SKETCHAPIENS WRITER — BỘ NÃO BIÊN KỊCH

> **Phase 1 compatibility wrapper — lớp tương thích Phase 1.**
>
> File này là **public interface — giao diện công khai** của skill theo Architecture Contract.
> Nó sửa routing metadata đã cũ mà **không thay creative implementation** trong đợt Consistency Repair.
>
> Runtime body hiện tại được bảo toàn byte-for-byte ở:
> `references/runtime-monolith-legacy.md` — **thân writer monolith tương thích**.
>
> ⚠️ YAML frontmatter nằm bên trong file legacy là **historical metadata — metadata lịch sử**.
> Nó KHÔNG có quyền routing và KHÔNG được dùng để ghi đè contract hiện hành ở file này hoặc `CLAUDE.md`.

## CONTRACT HIỆN HÀNH — HỢP ĐỒNG ĐANG HIỆU LỰC

1. **Vietnamese-first — Việt trước.** Viết bản tiếng Việt tự nhiên → owner nghe TTS → sửa/duyệt → khóa.
2. **English-last — Anh sau cùng.** Sau khi bản Việt đã khóa, viết lại sang tiếng Anh theo Ý một lần cho narration cuối; không dịch từng câu máy móc.
3. **No side-by-side approval table — Không bảng duyệt EN+VI cạnh nhau.** Hai ngôn ngữ là hai representation ở hai thời điểm khác nhau.
4. **Length follows the topic — Độ dài theo đề tài.** Long-form phải thỏa constraint sản xuất hiện hành, nhưng `8–25 phút` không phải quality target.
5. **Original work — Nội dung gốc.** Không mở corpus đối thủ trong phiên viết; không paraphrase transcript đối thủ.
6. **Three hard narration constraints — Ba ràng buộc cứng lời đọc:** `!` = 0 · không gạch ngang giữa câu · mỗi câu một dòng. `I ≈ 0` đã retire.
7. Khi xử lý **xương bài / nối chương / retention structure**, dùng `sketchapiens-story-engine` — **Cỗ máy cấu trúc câu chuyện** cùng writer này.
8. `CLAUDE.md`, `.claude/rules/**`, `governance/SOURCE_OF_TRUTH.md` và `RULE_REGISTRY.yaml` thắng mọi metadata/luật lịch sử bên trong compatibility body nếu có conflict.

## RUNTIME BODY — THÂN WRITER TƯƠNG THÍCH

@references/runtime-monolith-legacy.md

> **Không chỉnh trực tiếp monolith trong Phase 1 chỉ để dọn đẹp.**
> Tách public interface / implementation / history là việc của **Phase 3 — Writer Refactor / Tái cấu trúc bộ não viết** sau khi Story Engine ổn định.

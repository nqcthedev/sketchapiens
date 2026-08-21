#!/usr/bin/env python3
"""DỌN KỊCH BẢN RA ĐỂ ĐỌC — không chấm, không đếm, không phán.

    python3 tools/soi_kich_ban.py <file_narration.txt> [file_mp3_dir]

⛔ LUẬT 20/08/2026 — CHỦ CHỐT: **KHÔNG DÙNG CODE ĐỂ CHẤM KỊCH BẢN.**

Ngày 19-20/08 phép đếm máy sai SÁU lần trong hai buổi:
  · "nhịp câu đều nhất kho"     -> đúng số, sai kết luận (không dự báo view)
  · "% hạ nhiệt 13%"             -> thật ra 1%
  · "khối dài nhất 9,5% / 13%"   -> thật ra 34%
  · "19 câu chủ ngữ dài"         -> 17/19 báo động giả (câu mệnh lệnh)
  · "câu ra lệnh = 0" ở 7 bài    -> đọc thấy đầy
  · "8 món thiếu cú chốt"        -> 2 báo giả ngay lần chạy đầu

Trong khi MỌI phát hiện thật đều từ ĐỌC: số món độc lập · cú lật niềm tin ·
10 kỹ thuật câu của Zenn · câu "sợi dây" khó nghe · lỗi tên William Haskell.

=> Việc của file này chỉ là DỌN RA: đánh số dòng, gắn mốc phút, gom đoạn.
   Phán quyết là việc của người đọc.

Đọc theo: kho/1_luat/BOCTACH_KICHBAN_DOITHU.md (12 chiều)
          .claude/skills/sketchapiens-viet-kich-ban/SKILL.md PHẦN 13 (7 thước)
          kho/3_bangchung/BOC_8BAI_MACH_DEM_2026-08-20.md (số gốc 8 quả nổ)
"""
import os, sys, subprocess

if len(sys.argv) < 2:
    sys.exit("dùng: python3 tools/soi_kich_ban.py <file_narration.txt> [thư_mục_mp3]")

L = [l.strip() for l in open(sys.argv[1], encoding='utf-8') if l.strip()]
w = sum(len(c.split()) for c in L)

# mốc phút thật nếu có mp3, không thì ước theo 180 wpm
moc, t = [], 0.0
mp3dir = sys.argv[2] if len(sys.argv) > 2 else None
for i, c in enumerate(L, 1):
    moc.append(t)
    if mp3dir and os.path.exists(f"{mp3dir}/{i:03d}.mp3"):
        t += float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration',
                                   '-of','csv=p=0', f"{mp3dir}/{i:03d}.mp3"],
                                  capture_output=True, text=True).stdout.strip() or 0)
    else:
        t += len(c.split()) / 3.0     # 180 wpm

print(f"\n{sys.argv[1]}")
print(f"{len(L)} dòng · {w} từ · {'mốc phút THẬT từ mp3' if mp3dir else 'mốc phút ƯỚC ở 180 wpm'}")
print(f"tổng {int(t//60)}:{int(t%60):02d}\n" + "─"*74)
for i, c in enumerate(L, 1):
    s = moc[i-1]
    print(f"{i:>3} [{int(s//60)}:{int(s%60):02d}] {c}")
print("─"*74)
print("""
ĐỌC MÀ TRẢ LỜI — 12 chiều ở kho/1_luat/BOCTACH_KICHBAN_DOITHU.md

  ⑩ Bài có mấy MÓN tự đứng được? (bỏ đi bài vẫn chạy)      8 quả nổ đều ≥8
  ⑪ Chỗ nào đi quá 45 giây mà không có móc kéo?
  ⑫ Dùng mấy trong 12 kỹ thuật câu? Ở dòng nào?
  ·  Mỗi món có kết bằng câu ngắn không?
  ·  Mỗi nguồn đã thành câu chuyện chưa? (ai · bao lâu · tìm ra thứ không ngờ)
  ·  Có con vật có tên · con số choáng · cảnh dựng được chưa?
  ·  Món nào là cơ chế VÔ HÌNH? (khó ra prompt ảnh cho người que)
  ·  Cú lật có lật thứ bài CHƯA trả lời không? (lật thứ vừa nói = lặp)
  ·  Đọc to 30 giây đầu: câu nào phải nghe hai lần mới hiểu?

⛔ Ba ràng buộc cứng vẫn để máy soát — đó là ĐẾM, không phải CHẤM:
   python3 .claude/skills/sketchapiens-bien-tap/qa_kichban.py <file>
""")

# -*- coding: utf-8 -*-
"""GỘP prompt + kịch bản thành MỘT file dán thẳng sang ChatGPT.

Vì sao có file này (chủ chốt 20/08/2026):
    "lần nào update kịch bản cũng phải viết 1 file prompt đi kèm... cho nó nhanh
     đỡ phải update"
Chủ chỉ mở MỘT file, bôi đen hết, dán. Không phải ghép tay hai file.

⛔ Nó KHÔNG chấm gì cả. Chỉ gộp và đếm ba ràng buộc cứng.
   Luật kênh: máy chỉ đếm được ba ràng buộc cứng, việc phán là của model đọc.

    python3 tools/gui_chatgpt.py videos/Video20_Cold/_ban50
"""
import sys, re, pathlib

d = pathlib.Path(sys.argv[1])
kb = next(d.glob("V20_ban*_vi.txt"))
pr = d / "_prompt.md"
ban = re.search(r"ban(\d+)", kb.name).group(1)

if not pr.exists():
    sys.exit(f"⛔ thiếu {pr} — viết phần prompt cho bản này trước")

t = kb.read_text(encoding="utf-8")
lines = [l for l in t.split("\n") if l.strip()]
tu = len(re.findall(r"[\wÀ-ỹ']+", t))
nhieu = sum(1 for l in lines if re.search(r"[.?]\s+\S", l))

so = (f"**{len(lines)} dòng · {tu} từ · ~{tu//192}:{(tu*60//192)%60:02d} với giọng kênh.**\n"
      f"Ba ràng buộc cứng: **{t.count('!')} dấu chấm than · "
      f"{t.count('—')+t.count('–')} gạch ngang giữa câu · {nhieu} dòng chứa hai câu.**")

# ⚠️ File NGHE LẠNH không được lộ số bản — người nghe lạnh mà biết bài đã sửa 50 lần
#    thì hết lạnh. Đặt {{KICHBAN}} trong _prompt.md để chèn kịch bản TRẦN, không header.
body = pr.read_text(encoding="utf-8").replace("{{SO}}", so).rstrip()
kb_block = f"```\n{t.strip()}\n```"

if "{{KICHBAN}}" in body:
    out = d / f"NGHE_LANH_ban{ban}.md"
    noi_dung = body.replace("{{KICHBAN}}", kb_block)
else:
    out = d / f"GUI_CHATGPT_ban{ban}.md"
    noi_dung = body + f"\n\n---\n\n# KỊCH BẢN BẢN {ban} — {len(lines)} DÒNG\n\n{kb_block}\n"

out.write_text(noi_dung, encoding="utf-8")
print(f"→ {out}\n  {len(lines)} dòng · {tu} từ · ! {t.count('!')} · gạch ngang "
      f"{t.count('—')+t.count('–')} · dòng >1 câu {nhieu}")

import re, sys
p = sys.argv[1]
t = open(p).read()
w = re.findall(r"[A-Za-z']+", t)
S = [s for s in re.split(r'(?<=[.?])\s+', t.replace("\n", " ")) if s.strip()]
n = [len(re.findall(r"[A-Za-z']+", s)) for s in S]
q = t.count("?")
short = sum(1 for k in n if k < 6)
you = len(re.findall(r"\b(you|your|yours|yourself)\b", t, re.I))
we  = len(re.findall(r"\b(we|our|us)\b", t, re.I))
I   = len(re.findall(r"\bI\b", t))
run = mx = 0
for k in n:
    run = run + 1 if k >= 15 else 0
    mx = max(mx, run)
print(f"{p}")
print(f"  {len(w)} từ · {len(w)/178:.1f} phút · {len(S)} câu")
# ⛔ 09/08/2026 — CHỈ CÒN BA RÀNG BUỘC CỨNG. 'I' ĐÃ BỊ GỠ 07/08.
#    Bản cũ in 'I' dưới nhãn CỨNG, và /apply-review đọc dòng đó làm điều kiện chặn
#    → editor sẽ CẮT MỌI CÂU CÓ "I". Đo 18 kênh: 9/12 kênh có phép so sạch cho thấy
#    bài dùng "I" ĂN HƠN (Mack 9,18x). Xem governance/RETIRED_RULES.md
print(f"  CỨNG (3): '!' {t.count('!')} (phải 0) | '—' {t.count(chr(8212))} (phải 0) | mỗi câu một dòng: xem dưới")
print(f"  ĐO — KHÔNG PHẢI NGƯỠNG: 'I' {I} (người dẫn ĐƯỢC có ý kiến) | câu hỏi {q} | câu<6từ {short} ({round(short/len(n)*100)}%) | dài TB {sum(n)/len(n):.1f} | 3 câu dài liên tiếp: {'CÓ' if mx>=3 else 'không'}")
# mỗi câu một dòng — ràng buộc cứng thứ ba, bản cũ KHÔNG kiểm
import re as _re
_multi=[i+1 for i,l in enumerate(t.split(chr(10))) if _re.search(r'[.?!]["\']? +[A-Z]',l)]
print(f"  CỨNG: mỗi câu một dòng → {'✅ đạt' if not _multi else f'❌ {len(_multi)} dòng có >1 câu: {_multi[:8]}'}")
print(f"  you {you} : we {we} = {you/max(we,1):.1f}:1  ← LUẬT 0, không phải hằng số")

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
print(f"  CỨNG: '!' {t.count('!')} (0) | '—' {t.count(chr(8212))} (0) | 'I' {I} (≈0) | 3 câu dài liên tiếp: {'CÓ' if mx>=3 else 'không'}")
print(f"  MỀM: câu hỏi {q} → 1 mỗi {round(len(w)/178*60/max(q,1))}s (60-90) | câu<6từ {short} ({round(short/len(n)*100)}%, V17=37%) | dài TB {sum(n)/len(n):.1f} (V17=8.9)")
print(f"  you {you} : we {we} = {you/max(we,1):.1f}:1  ← LUẬT 0, không phải hằng số")

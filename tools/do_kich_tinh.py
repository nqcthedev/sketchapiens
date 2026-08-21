#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CỔNG 5 — ĐO KỊCH TÍNH. So kịch bản của mình với MỘT quả nổ khớp cặp.

    python3 tools/do_kich_tinh.py <kich_ban.txt> <ban_ghi_doi_thu.txt>

VÌ SAO CÓ FILE NÀY
──────────────────
Bốn cổng cũ kiểm: sản xuất · sự thật · trùng lặp · người lạ có hiểu không.
KHÔNG cổng nào hỏi "bài này có hồi hộp không". Hệ quả đo được ở V20 bản 1:

    chữ chỉ cái chết          : 2   (Axen ~19)
    nguy hiểm xuất hiện lần đầu: 44% bài  (Axen 2%)
    gọi thẳng người xem       : 0   (Axen ~51)

Bài đúng từng chữ, qua cả bốn cổng, và chủ nghe xong nói "nghe bài đối thủ hay hơn".

⚠️ CỔNG NÀY KHÔNG CÓ NGƯỠNG TUYỆT ĐỐI. Kho đã bốn lần đẻ luật từ mẫu quá nhỏ rồi
phải giết lại. Ở đây mọi con số đều là TỈ LỆ so với một quả nổ CÙNG Ô, tải về cùng
ngày. Không có đối thủ khớp cặp thì cổng này KHÔNG chạy được, và đó là cố ý.
"""
import re, sys

def doc(p):
    return [l.strip() for l in open(p, encoding="utf-8") if l.strip()]

CHET  = r"\b(die|died|dying|dead|death|kill|killed|killer|deadly|deadliest|lethal|hypothermia|freeze to death|freezing to death|found dead|survive|survival|threat|starve|starving)\b"
YOU   = r"\b(you|your|yours)\b"
VAT   = r"\b(fire|hearth|hide|fur|grass|clay|bedding|stone|bone|snow|frost|needle|blanket|wall|bed|chamber|hut|floor|ash|charcoal|meat|skin|tusk|spear|pit)\b"
RIENG = r"\b[A-Z][a-zà-ÿA-ZÀ-Ÿ]+(?:\s[A-ZÀ-Ÿ][a-zà-ÿ]+)?\b"

def dem(L, pat):
    return sum(len(re.findall(pat, x, re.I)) for x in L)

def vitri_dau(L, pat):
    for i, x in enumerate(L, 1):
        if re.search(pat, x, re.I):
            return 100 * i / len(L)
    return 100.0

def do(L):
    n = len(L)
    return {
        "câu": n,
        "từ": sum(len(x.split()) for x in L),
        "chữ chỉ CÁI CHẾT": dem(L, CHET),
        "gọi thẳng người xem": dem(L, YOU),
        "vật thể cụ thể": dem(L, VAT),
        "nguy hiểm lần đầu (% bài)": round(vitri_dau(L, CHET)),
    }

if len(sys.argv) < 3:
    sys.exit("dùng: do_kich_tinh.py <kich_ban.txt> <ban_ghi_doi_thu.txt | tên_ô>")
A = do(doc(sys.argv[1]))
ref = sys.argv[2]
if ref.endswith(".txt"):
    B = do(doc(ref))
else:
    import json, os
    _m = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                                     "schemas", "moc_kich_tinh.json"), encoding="utf-8"))
    if ref not in _m:
        sys.exit(f"⛔ chưa có mốc cho ô '{ref}'. Có: {[k for k in _m if not k.startswith('_')]}")
    B = dict(_m[ref]); B["câu"] = "-"; B["từ"] = "-"
    print(f"  mốc: {B.pop('nguon')}")

print("═" * 62)
print("  CỔNG 5 — KỊCH TÍNH   (so với MỘT quả nổ cùng ô)")
print("═" * 62)
print(f"{'':30s}{'MÌNH':>9s}{'ĐỐI THỦ':>10s}{'':>6s}")
ok = True
for k in A:
    a, b = A[k], B[k]
    if k in ("câu", "từ"):
        print(f"{k:30s}{a:>9}{str(b):>10}")
        continue
    if k == "nguy hiểm lần đầu (% bài)":
        dat = a <= b + 5
        print(f"{k:30s}{str(a)+'%':>9}{str(b)+'%':>10}   {'✅' if dat else '❌ MUỘN HƠN'}")
    else:
        dat = a >= b * 0.6            # ≥60% mức của quả nổ khớp cặp
        print(f"{k:30s}{a:>9}{b:>10}   {'✅' if dat else '❌ THIẾU'}")
    ok = ok and dat

print()
print("  ⛔ TRƯỢT = KHÔNG CHIA SHOT. Sửa bằng cách NÂNG CƯỢC, không phải sửa câu:")
print("     · ai có thể chết, và nói ra bằng chữ chỉ cái chết")
print("     · đặt nguy hiểm vào ĐOẠN MỞ, không để tới giữa bài")
print("     · thang leo thang: mỗi nấc tối hơn nấc trước")
print("     · nói cái GIÁ của việc thất bại, đừng để người xem tự suy")
print()
print("  📏 Hedge có NGÂN SÁCH: tối đa MỘT khối thành thật, đặt một chỗ.")
print("     V20 bản 1 tự thú 'chưa chắc' ba lần; Axen một lần. Trung thực ba lần")
print("     nghe ra là rụt rè, không phải là cẩn thận.")
print("\n→ " + ("ĐẠT." if ok else "CHƯA ĐẠT."))
sys.exit(0 if ok else 1)

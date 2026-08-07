#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ĐO — một lệnh duy nhất cho mọi phép đo hay phải làm lại trên kho đối thủ.

VÌ SAO CÓ FILE NÀY
──────────────────
Ngày 06/08/2026 tôi đo tốc độ đọc của đối thủ **bốn lần, sai cả bốn**. Không lần
nào sai vì tính nhầm. Cả bốn đều sai vì mỗi lần tôi viết lại phép đo từ đầu và
mỗi lần chọn một NỀN THỜI GIAN khác nhau:

    số từ ÷ thời lượng VIDEO      ← có nhạc đầu/cuối, có khoảng lặng
    số từ ÷ thời lượng AUDIO      ← không nhạc, còn khoảng lặng
    số từ ÷ thời gian ĐANG NÓI    ← trừ cả khoảng lặng

Ba con số này lệch nhau tới 20%. So một cái với cái kia là ra kết luận ngược.

→ **Luật của file này: mọi con số in ra đều kèm nền thời gian của nó.**
   Không có dòng "wpm" trần trụi nào được phép rời khỏi đây.

CÁCH DÙNG
─────────
    do.py wpm                    tốc độ đọc, mọi kênh
    do.py wpm Zenn Mack          chỉ vài kênh
    do.py dodai                  độ dài video + view, mọi kênh
    do.py tim "toilet trip"      tìm một cụm từ trong toàn kho
    do.py trung <file kịch bản>  dò trùng nguyên văn với đối thủ (cổng 11)

READ-ONLY. Không sửa gì trong kho.
"""
import os
import re
import sys
import glob

KHO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ══ đọc kho ═══════════════════════════════════════════════════════════════

HEAD = re.compile(
    r"^#\s*id=(?P<id>\S+)"
    r"(?:.*?·\s*(?P<view>[\d,]+)\s*view)?"
    r"(?:.*?·\s*(?P<dur>\d+:\d+(?::\d+)?))?"
    r"(?:.*?·\s*(?P<words>\d+)\s*từ)?",
    re.M)


def giay(s):
    """'19:24' → 1164 · '1:05:30' → 3930"""
    p = [int(x) for x in s.split(":")]
    while len(p) < 3:
        p.insert(0, 0)
    return p[0] * 3600 + p[1] * 60 + p[2]


def dem_tu(text):
    return len(re.findall(r"[A-Za-z'’]+", text))


def than_bai(text):
    """Bỏ ba dòng đầu (# tiêu đề, # số liệu, # link), trả phần lời đọc."""
    return "\n".join(l for l in text.splitlines() if not l.startswith("#"))


def nap(chi_kenh=None):
    """Trả list dict, mỗi dict là một bản ghi."""
    ra, rong = [], []
    for d in sorted(os.listdir(KHO)):
        p = os.path.join(KHO, d)
        if not os.path.isdir(p) or d.startswith("_"):
            continue
        if chi_kenh and d not in chi_kenh:
            continue
        fs = sorted(glob.glob(os.path.join(p, "*.txt")))
        if not fs:
            rong.append(d)
            continue
        for f in fs:
            t = open(f, encoding="utf-8", errors="replace").read()
            m = HEAD.search(t)
            body = than_bai(t)
            ra.append({
                "kenh": d,
                "file": f,
                "id": m.group("id") if m else None,
                "view": int(m.group("view").replace(",", "")) if m and m.group("view") else None,
                "giay": giay(m.group("dur")) if m and m.group("dur") else None,
                "tu": dem_tu(body),          # ĐẾM LẠI, không tin số ghi sẵn trong header
                "than": body,
            })
    return ra, rong


def trung_vi(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return None
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def phut(s):
    return f"{int(s)//60}:{int(s)%60:02d}"


def canh_bao_rong(rong):
    for d in rong:
        print(f"  ⚠️  {d}: THƯ MỤC RỖNG — lần kéo đó hỏng, số liệu dưới đây KHÔNG có kênh này")


# ══ lệnh 1: wpm ═══════════════════════════════════════════════════════════

def lenh_wpm(kenh):
    recs, rong = nap(kenh or None)
    print("═" * 74)
    print("  TỐC ĐỘ ĐỌC")
    print("═" * 74)
    print("  ⚠️  NỀN THỜI GIAN = TOÀN BỘ THỜI LƯỢNG VIDEO.")
    print("      Đã gồm nhạc đầu/cuối, khoảng lặng, mọi quãng không có lời.")
    print("      → Muốn so với kênh mình thì phải lấy SỐ TỪ ÷ THỜI LƯỢNG VIDEO ĐÃ GHÉP,")
    print("        KHÔNG phải ÷ độ dài file audio, KHÔNG phải ÷ thời gian đang nói.")
    print("        Lẫn ba nền này chính là bốn lần đo sai ngày 06/08/2026.\n")
    canh_bao_rong(rong)

    theo = {}
    for r in recs:
        if r["giay"] and r["tu"]:
            theo.setdefault(r["kenh"], []).append(r["tu"] / (r["giay"] / 60))
    if not theo:
        print("  (không bản ghi nào có đủ thời lượng + số từ)")
        return

    print(f"\n  {'kênh':<22}{'n':>4}{'trung vị':>10}{'thấp nhất':>11}{'cao nhất':>10}")
    print("  " + "─" * 57)
    for k in sorted(theo, key=lambda k: -trung_vi(theo[k])):
        v = theo[k]
        print(f"  {k:<22}{len(v):>4}{trung_vi(v):>10.0f}{min(v):>11.0f}{max(v):>10.0f}")
    het = [x for v in theo.values() for x in v]
    print("  " + "─" * 57)
    print(f"  {'CẢ KHO':<22}{len(het):>4}{trung_vi(het):>10.0f}{min(het):>11.0f}{max(het):>10.0f}")
    print("\n  đơn vị: từ mỗi phút video")


# ══ lệnh 2: dodai ═════════════════════════════════════════════════════════

def lenh_dodai(kenh):
    recs, rong = nap(kenh or None)
    print("═" * 74)
    print("  ĐỘ DÀI VÀ VIEW")
    print("═" * 74)
    print("  ⚠️  View là con số lúc KÉO VỀ, không cập nhật. Video mới bị thiệt.")
    print("      Luôn báo TRUNG VỊ, không báo trung bình — một quả trúng số kéo lệch hết.\n")
    canh_bao_rong(rong)

    theo = {}
    for r in recs:
        theo.setdefault(r["kenh"], []).append(r)

    print(f"\n  {'kênh':<22}{'n':>4}{'dài (tv)':>10}{'view (tv)':>11}{'từ (tv)':>9}{'top2 %':>8}")
    print("  " + "─" * 64)
    for k in sorted(theo, key=lambda k: -(trung_vi([x['view'] for x in theo[k]]) or 0)):
        v = theo[k]
        d = trung_vi([x["giay"] for x in v])
        vi = trung_vi([x["view"] for x in v])
        tu = trung_vi([x["tu"] for x in v])
        vs = sorted((x["view"] or 0) for x in v)
        top2 = 100 * sum(vs[-2:]) / sum(vs) if sum(vs) else 0
        print(f"  {k:<22}{len(v):>4}{phut(d) if d else '—':>10}"
              f"{(f'{vi:,.0f}' if vi else '—'):>11}{(f'{tu:,.0f}' if tu else '—'):>9}{top2:>7.0f}%")
    print("\n  top2 % = hai video cao nhất chiếm bao nhiêu phần trăm tổng view của kênh đó.")
    print("  Trên 80% nghĩa là kênh đó KHÔNG có công thức — nó trúng số. Đừng học nó.")


# ══ lệnh 3: tim ═══════════════════════════════════════════════════════════

def lenh_tim(tu_khoa):
    if not tu_khoa:
        print("  cần một cụm từ:  do.py tim \"toilet trip\"")
        return 1
    q = " ".join(tu_khoa).lower()
    recs, _ = nap()
    hit = 0
    for r in recs:
        low = r["than"].lower()
        if q not in low:
            continue
        for line in r["than"].splitlines():
            if q in line.lower():
                hit += 1
                print(f"  {r['kenh']:<18} {os.path.basename(r['file'])[:44]:<46} {line.strip()[:80]}")
    print("─" * 74)
    print(f"  \"{q}\" — {hit} dòng khớp trong {len(recs)} bản ghi")
    if hit == 0:
        print("  → chưa ai trong kho nói cụm này. Đây là điểm KHÁC BIỆT, không phải lỗ hổng:")
        print("    họ không nói có thể vì nó sai, chứ không phải vì họ bỏ sót.")
    return 0


# ══ lệnh 4: trung ═════════════════════════════════════════════════════════

CUM = 8  # số từ mỗi cụm — 8 từ trùng nguyên văn là đã quá mức ngẫu nhiên


def cum_tu(text, n=CUM):
    w = re.findall(r"[a-z']+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def lenh_trung(args):
    if not args:
        print("  cần một file kịch bản:  do.py trung Video19_NightWalk/Script_Video19_narration.txt")
        return 1
    f = args[0]
    if not os.path.exists(f):
        f2 = os.path.join(os.path.dirname(KHO), f)
        if os.path.exists(f2):
            f = f2
        else:
            print(f"  không thấy file: {args[0]}")
            return 1
    ta = cum_tu(open(f, encoding="utf-8").read())
    recs, _ = nap()
    print("═" * 74)
    print(f"  DÒ TRÙNG NGUYÊN VĂN — {os.path.basename(f)}")
    print("═" * 74)
    print(f"  {len(ta)} cụm {CUM} từ · so với {len(recs)} bản ghi của đối thủ\n")

    tong = 0
    for r in recs:
        chung = ta & cum_tu(r["than"])
        if chung:
            tong += len(chung)
            print(f"  ⛔ {r['kenh']}/{os.path.basename(r['file'])}")
            for c in sorted(chung)[:5]:
                print(f"       \"{c}\"")
    print("─" * 74)
    if tong == 0:
        print(f"  ✅ 0 cụm {CUM} từ trùng. Qua cổng 11.")
        print("     Lưu ý: cái này chỉ bắt TRÙNG CHỮ. Trùng TRÌNH TỰ BEAT, trùng ví dụ,")
        print("     trùng cú bẻ lái thì nó không thấy — thứ đó phải người đọc mới bắt được.")
    else:
        print(f"  ❌ {tong} cụm trùng. Sửa trước khi sản xuất.")
    return 1 if tong else 0


# ══ vào ═══════════════════════════════════════════════════════════════════

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    lenh, args = sys.argv[1], sys.argv[2:]
    if lenh == "wpm":
        return lenh_wpm(args) or 0
    if lenh == "dodai":
        return lenh_dodai(args) or 0
    if lenh == "tim":
        return lenh_tim(args) or 0
    if lenh == "trung":
        return lenh_trung(args) or 0
    print(f"  không biết lệnh '{lenh}'. Có: wpm · dodai · tim · trung")
    return 1


if __name__ == "__main__":
    sys.exit(main())

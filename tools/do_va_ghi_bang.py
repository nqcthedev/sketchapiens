#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ĐO KỊCH BẢN RỒI CỘNG DỒN VÀO BẢNG — mở được bằng Excel/Numbers/Sheets.

    python3 tools/do_va_ghi_bang.py <file.txt> ["<tên>"] [<view>] ["<ô>"]
    python3 tools/do_va_ghi_bang.py --thumuc 2_KHO_BANGHI/Axen "Axen"   # cả thư mục

VÌ SAO CÓ FILE NÀY
──────────────────
Mọi phép đo trước 18/08 đều chạy MỘT LẦN rồi trôi vào khung chat. Đo Axen xong,
đo quả 2,04M xong, nhưng không có bảng nào tích lại — nên không bao giờ thấy được
mẫu hình qua hai mươi video, chỉ thấy từng cái một.

Bảng nằm ở kho/3_bangchung/BANG_DO_KICHBAN.csv — git theo dõi được, Excel mở được.

⚠️ SỬA 18/08 — bản đầu có BỐN lỗi, số đo ra không so được:
  1. không bỏ dòng '#' header  -> 4 dòng đầu bị tính là câu
  2. 'tên riêng' bắt MỌI chữ hoa -> mọi câu đều mở bằng chữ hoa, V20 ra 91 (rác)
  3. 'vật thể'/'so sánh hiện đại' là từ vựng riêng của ĐÊM LẠNH -> vô nghĩa ở ô khác
  4. 'ước phút' chốt cứng 201 wpm -> Mack đọc 146, Axen 213, lệch tới 30%
Nay: bỏ header, chỉ đếm chữ hoa GIỮA CÂU, đổi hai cột topic-riêng sang cột dùng
chung mọi ô, và LẤY ĐỘ DÀI THẬT từ header khi có.
"""
import csv, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "kho", "3_bangchung", "BANG_DO_KICHBAN.csv")

# ── ĐO ĐƯỢC Ở MỌI Ô (không dính đề tài) ────────────────────────────────────
CHET = (r"\b(die|died|dies|dying|dead|death|deaths|kill|kills|killed|killing|killer|"
        r"deadly|deadliest|lethal|fatal|corpse|body|bodies|survive|survived|survival|"
        r"starve|starved|starving|drown|drowned|freeze to death|bleed|wound|"
        r"predator|predators|hunted|prey|danger|dangerous|threat|attack|attacked)\b")
BAN     = r"\b(you|your|yours|you're|you've|you'd|you'll)\b"
CHUNGTA = r"\b(we|our|ours|us|we're|we've|we'd)\b"
TOI     = r"\b(I|I'm|I've|me|my|mine)\b"
HEDGE   = (r"\b(may|might|maybe|perhaps|probably|possibly|likely|unlikely|seems|"
           r"appears|suggests|roughly|about|around|nobody knows|we don't know|"
           r"not certain|unclear|estimate|estimated)\b")
NHAN    = (r"(here is|here's|and here|but here|the part that|easy to miss|worth saying|"
           r"strangest|weirdest|wild fact|think about that|the crazy part|"
           r"this is where|now here)")
# thay 'vật thể' + 'so sánh hiện đại' (vốn là từ vựng đêm lạnh) bằng 2 cột dùng chung:
HIENDAI = (r"\b(phone|smartphone|app|apps|netflix|uber|wifi|google|amazon|instagram|"
           r"tiktok|youtube|supermarket|grocery|fridge|refrigerator|freezer|thermostat|"
           r"microwave|kitchen|bedroom|mattress|office|email|inbox|insurance|gym|"
           r"coffee|starbucks|car|traffic|internet|laptop|tv|television)\b")
SO      = r"(\b\d[\d,\.]*\b|\b(?:one|two|three|four|five|six|seven|eight|nine|ten|"        \
          r"eleven|twelve|twenty|thirty|forty|fifty|sixty|hundred|thousand|million|"       \
          r"billion|percent|degrees)\b)"
LIENTU  = r"^(And|But|So|Because|Which|Or|Now|Then|Except|Yet)\b"
# tên riêng THẬT: chữ hoa KHÔNG đứng đầu câu, bỏ các từ hay viết hoa vì lý do khác
BO_RIENG = {"I", "I'm", "I've", "English", "God"}
RIENG = r"(?<!^)(?<![.!?]\s)\b([A-Z][a-zà-ÿ']{2,}(?:\s[A-ZÀ-Ÿ][a-zà-ÿ']{2,})?)\b"


def doc(path):
    """Trả (danh sách câu, dict header). Bỏ dòng '#' và dòng rỗng."""
    head, L = {}, []
    for raw in open(path, encoding="utf-8"):
        s = raw.strip()
        if not s:
            continue
        if s.startswith("#"):
            m = re.search(r"([\d,]+)\s*view", s)
            if m:
                head["view"] = m.group(1)
            m = re.search(r"·\s*(\d+:\d\d)\s*·", s)
            if m:
                head["dài"] = m.group(1)
            m = re.search(r"(\d+)\s*wpm", s)
            if m:
                head["wpm"] = int(m.group(1))
            if "tiêu đề" not in head and not re.search(r"id=|https?://", s):
                head["tiêu đề"] = s.lstrip("# ").strip()
            continue
        L.append(s)
    return L, head


def dem(L, p, flags=re.I):
    return sum(len(re.findall(p, x, flags)) for x in L)


def vitri(L, p):
    for i, x in enumerate(L, 1):
        if re.search(p, x, re.I):
            return round(100 * i / len(L))
    return 100


def khuc(L, p, k=10):
    n = len(L); sz = -(-n // k)
    return sum(1 for i in range(k)
               if any(re.search(p, L[j], re.I) for j in range(i * sz, min(n, (i + 1) * sz))))


def do_mot(path, ten=None, view=None, o=""):
    L, head = doc(path)
    if not L:
        return None
    w = sum(len(x.split()) for x in L)
    view = view or head.get("view", "?")
    ten = ten or head.get("tiêu đề", os.path.basename(path))
    wpm = head.get("wpm")
    dai = head.get("dài") or (f"{int((w/wpm*60)//60)}:{int((w/wpm*60)%60):02d}" if wpm
                              else f"~{int((w/180*60)//60)}:{int((w/180*60)%60):02d}")
    rieng = {m for m in re.findall(RIENG, "\n".join(L)) if m not in BO_RIENG}
    return {
        "tên": ten[:70], "ô": o, "view": view,
        "từ": w, "câu": len(L), "từ/câu": round(w / len(L), 1),
        "dài": dai, "wpm": wpm or "",
        "chữ nguy hiểm": dem(L, CHET),
        "nguy hiểm /1000 từ": round(1000 * dem(L, CHET) / w, 1),
        "nguy hiểm lần đầu %": vitri(L, CHET),
        "khúc có nguy hiểm /10": khuc(L, CHET),
        "you": dem(L, BAN), "you /1000 từ": round(1000 * dem(L, BAN) / w, 1),
        "we/our": dem(L, CHUNGTA), "tôi": dem(L, TOI, 0),
        "số liệu": dem(L, SO), "số /1000 từ": round(1000 * dem(L, SO) / w, 1),
        "tên riêng": len(rieng),
        "từ hiện đại": dem(L, HIENDAI),
        "rào đón": dem(L, HEDGE),
        "câu dẫn có nhãn": dem(L, NHAN),
        "câu hỏi": sum(x.count("?") for x in L),
        "liên từ đầu câu": dem(L, LIENTU, 0),
        "câu cụt ≤4 từ": sum(1 for x in L if len(x.split()) <= 4),
        "dấu !": sum(x.count("!") for x in L),
        "nguồn": os.path.relpath(path, ROOT),
    }


def ghi(hang):
    moi = not os.path.exists(CSV) or os.path.getsize(CSV) == 0
    with open(CSV, "a", newline="", encoding="utf-8-sig") as f:
        wr = csv.DictWriter(f, fieldnames=list(hang[0]))
        if moi:
            wr.writeheader()
        wr.writerows(hang)


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == "--thumuc":
        o = a[2] if len(a) > 2 else os.path.basename(a[1].rstrip("/"))
        rows = [r for p in sorted(glob.glob(os.path.join(a[1], "*.txt")))
                for r in [do_mot(p, o=o)] if r]
        ghi(rows)
        print(f"✅ {len(rows)} hàng  <- {a[1]}")
    else:
        r = do_mot(a[0], a[1] if len(a) > 1 else None,
                   a[2] if len(a) > 2 else None, a[3] if len(a) > 3 else "")
        ghi([r])
        print(f"✅ ghi vào {os.path.relpath(CSV, ROOT)}")
        for k, v in r.items():
            if k != "nguồn":
                print(f"   {k:22s} {v}")

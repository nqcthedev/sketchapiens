# ⛔ HIỆN VẬT — video này ĐÃ SẢN XUẤT XONG. ĐỪNG CHÉP SANG VIDEO MỚI.
#    Bản dùng chung: tools/  +  identity/style.py
#    Giữ nguyên vì prompt phải khớp thứ ĐÃ THẬT SỰ dùng để gen ảnh —
#    sửa lại là sửa lịch sử. (dán 08/08/2026)
# -*- coding: utf-8 -*-
"""KIỂM SHOT + PROMPT — chạy TRƯỚC KHI GEN, mọi video.
   python3 validate_shots.py Script_VideoNN_narration.txt

Đúc 30/07 từ 9 lỗi thật của V17, VIẾT LẠI 30/07 sau khi đo 1.090 khung
đối thủ (NGUPHAP_HINH_DoLai_ToanBo). Ba luật cũ đã bị bằng chứng bác bỏ:
  · "nhãn ≤3 từ"      -> chỉ đúng với NHÃN NHỎ có mũi tên. Tiêu đề thẻ của
                         đối thủ dài cả câu: "RAIN DIDN'T STOP THE FOOD SUPPLY."
  · "khung dạy học ≥35%" -> ngược. Đối thủ 36-41% thẻ, 59-64% CẢNH.
  · "khung dạy học không được có nhân vật" -> sai, thẻ so sánh của họ là
                         hai cảnh nhỏ có nhân vật.
"""
import io, re, sys, importlib
sys.path.insert(0, '.')
import shot_data; importlib.reload(shot_data)
from shot_data import SHOTS

# ⛔ 07/08/2026 — BA CỬA TỈ LỆ DƯỚI ĐÂY ĐÃ CHẾT, ĐỪNG CHÉP SANG VIDEO MỚI.
#    "THẺ 30-45%" · "KHUNG CẢNH 55-70%" · "khung có chữ 40-70%" đúc từ ĐÚNG HAI kênh.
#    Bảng 4-5 kênh (05/08) bác sạch: nền trắng 36%→80%, cả bốn đều thắng.
#    Bản đã sửa: videos/Video19_NightWalk/validate_shots.py — xem governance/RETIRED_RULES.md
#    File này giữ nguyên vì V17 đã sản xuất xong; nó là hiện vật, không phải khuôn.

# 07/08: mặc định cũ là "narration.txt" — KHÔNG có file nào tên vậy, nên phép kiểm
# cuối (ghép shot == nguyên văn kịch bản) chưa bao giờ chạy, chỉ ném FileNotFoundError.
import glob as _g
NARR = sys.argv[1] if len(sys.argv) > 1 else (
    (_g.glob("Script_*_narration.txt") or ["narration.txt"])[0])
txt = io.open("PROMPTS_FULL.txt", encoding="utf-8").read()
blocks = re.findall(r'^(\d{3})\.\s(.*?)(?=\n\n\d{3}\.|\Z)', txt, re.S | re.M)
N = len(SHOTS)
SCENE_KINDS = {"SCENE_A", "SCENE_M", "SCENE_W", "GROUP"}
ok = True

def chk(name, cond, detail=""):
    global ok
    print(f"{'✅' if cond else '❌'} {name}" + ("" if cond else f"   {detail}"))
    if not cond:
        ok = False

# ── cấu trúc ──────────────────────────────────────────────────────────────
nums = [int(n) for n, _ in blocks]
chk("số prompt == số shot", len(blocks) == N, f"{len(blocks)} vs {N}")
chk("đánh số liên tục", nums == list(range(1, N + 1)), str(set(range(1, N + 1)) - set(nums))[:80])
chk("đủ 5 khối", not [n for n, b in blocks
                      if any(k not in b for k in ("Framing:", "SCENE:", "TEXT:", "NEG:"))
                      or not ("SUBJECT:" in b or "ACTION IN THIS SHOT:" in b)])
chk("không placeholder", not [n for n, b in blocks if "[" in b or "XXX" in b])
chk("không prompt cụt", not [n for n, b in blocks if len(b.split()) < 60])
chk("mọi prompt có 16:9", not [n for n, b in blocks if "16:9" not in b])
chk("mọi prompt dưới 4000 ký tự (giới hạn Google Flow)",
    not [n for n, b in blocks if len(b.strip()) > 4000],
    f"dài nhất {max(len(b.strip()) for _, b in blocks)}")


# ── nhất quán nhân vật ────────────────────────────────────────────────────
ANC = "This is the recurring caveman of the series."
sc = [b for n, b in blocks if "recurring caveman" in b]
chk("khối người cổ đại lặp Y NGUYÊN", sc and all(ANC in b for b in sc), f"{len(sc)} khung")
MOD = "This is the recurring modern guy of the series."
sm = [b for n, b in blocks if "recurring modern guy" in b]
chk("khối người hiện đại lặp Y NGUYÊN", sm and all(MOD in b for b in sm), f"{len(sm)} khung")
chk("cấm bóng người đen (pictogram)",
    not [n for n, b in blocks if re.search(r'\bsilhouette\b', b, re.I)])

# ── chữ trên hình ─────────────────────────────────────────────────────────
sp = [n for (n, b), (l, k, su, t, bg) in zip(blocks, SHOTS)
      if (("no text" not in t.lower()) != ("Spell it EXACTLY" in b))]
chk("lệnh ép chính tả khớp khung có chữ", not sp, str(sp[:8]))

# nhãn NHỎ (có mũi tên trỏ vào vật) mới phải ngắn; tiêu đề thẻ thì không
smalllab = [(n, m) for (n, b), (l, k, su, t, bg) in zip(blocks, SHOTS)
            if re.search(r'label|arrow', t, re.I) and not re.search(r'headline|large|bold', t, re.I)
            for m in re.findall(r'"([^"]{2,})"', t) if len(m.split()) > 4]
chk("nhãn nhỏ ≤4 từ", not smalllab, str(smalllab[:5]))

# ── tỉ lệ hình (theo số đo đối thủ) ───────────────────────────────────────
scene = sum(1 for s in SHOTS if s[1] in SCENE_KINDS)
card = N - scene
txt_n = sum(1 for s in SHOTS if "no text" not in s[3].lower())
mod = sum(1 for s in SHOTS if s[1] == "SCENE_M")
grp = sum(1 for s in SHOTS if s[1] == "GROUP")
w = sum(len(s[0].split()) for s in SHOTS) / N

chk("KHUNG CẢNH 55-70%", 0.55 <= scene / N <= 0.70, f"{100*scene/N:.0f}%  (đối thủ 59-64%)")
chk("THẺ 30-45%", 0.30 <= card / N <= 0.45, f"{100*card/N:.0f}%  (đối thủ 36-41%)")
chk("có cảnh CẢ NHÓM ≥8", grp >= 8, f"{grp} khung  (cảnh quây quanh lửa là cảnh chủ của lane)")
chk("khung có chữ 40-70%", 0.40 <= txt_n / N <= 0.70, f"{100*txt_n/N:.0f}%")
chk("người hiện đại ≤15%", mod / N <= 0.15, f"{100*mod/N:.0f}%")
chk("từ mỗi shot 6-9", 6 <= w <= 9, f"{w:.1f}")

# ── luật sống còn: TTS phải đọc đúng kịch bản đã duyệt ────────────────────
a = re.sub(r"\s+", " ", " ".join(s[0] for s in SHOTS)).strip().lower()
b2 = re.sub(r"\s+", " ", io.open(NARR, encoding="utf-8").read()).strip().lower()
chk("GHÉP SHOT == NARRATION nguyên văn", a == b2, f"{len(a.split())} vs {len(b2.split())} từ")

print("\n" + ("→ SẴN SÀNG GEN." if ok else "→ CÒN LỖI. SỬA XONG MỚI GEN."))

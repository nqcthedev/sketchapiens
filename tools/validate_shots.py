#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIỂM SHOT + PROMPT — chạy TRƯỚC KHI GEN ẢNH. MỘT bản dùng cho MỌI video.

VÌ SAO CÓ FILE NÀY
──────────────────
Trước 08/08/2026 mỗi thư mục video có một bản `validate_shots.py` **riêng**, và ba bản
đã **trôi khỏi nhau**: V17 còn giữ ba cửa tỉ lệ đã bị bằng chứng bác, V19 thì đã bỏ và
có thêm luật mới. Sửa một bản không lan sang bản kia — đúng bệnh "biểu hiện tự trôi"
mà `tools/kiem_bieu_hien.py` sinh ra để bắt, chỉ khác là lần này trôi ở **mã**.

Và mọi ngưỡng từng nằm **đóng cứng trong mã**. Nay chúng ở `schemas/shot_rules.json`,
mỗi ngưỡng bắt buộc kèm `nguon`. Không có nguồn thì không được làm cửa chặn.

CÁCH DÙNG
─────────
    python3 tools/validate_shots.py videos/Video19_NightWalk
    python3 tools/validate_shots.py .          # từ trong thư mục video

Thứ RIÊNG của từng video *(khối mô tả nhân vật, cảnh chủ của lane)* khai trong
`<thư_mục_video>/shot_rules.json`. Không có file đó thì bỏ qua các phép kiểm ấy.

READ-ONLY. Mã thoát 1 nếu có lỗi.
"""
import io
import json
import os
import re
import sys
import glob
import importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEO = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
LUAT = json.load(io.open(os.path.join(ROOT, "schemas", "shot_rules.json"), encoding="utf-8"))

RIENG = {}
_r = os.path.join(VIDEO, "shot_rules.json")
if os.path.exists(_r):
    RIENG = json.load(io.open(_r, encoding="utf-8"))

ok = True


def chk(ten, dieu_kien, chi_tiet=""):
    global ok
    print(f"{'✅' if dieu_kien else '❌'} {ten}" + ("" if dieu_kien else f"   {chi_tiet}"))
    if not dieu_kien:
        ok = False


def nap_shots(d):
    p = os.path.join(d, "shot_data.py")
    if not os.path.exists(p):
        sys.exit(f"⛔ không thấy {p}")
    spec = importlib.util.spec_from_file_location("shot_data", p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SHOTS


SHOTS = nap_shots(VIDEO)
N = len(SHOTS)
# shot_data dùng tuple; 5 trường đầu ổn định qua mọi video:
#   0 lời đọc · 1 kind · 2 subject · 3 text · 4 background
LOI = [s[0] for s in SHOTS]
KIND = [s[1] for s in SHOTS]
SUBJ = [s[2] for s in SHOTS]
TEXT = [s[3] for s in SHOTS]

pf = os.path.join(VIDEO, "PROMPTS_FULL.txt")
txt = io.open(pf, encoding="utf-8").read()
blocks = re.findall(r"^(\d{3})\.\s(.*?)(?=\n\n\d{3}\.|\Z)", txt, re.S | re.M)

nar = glob.glob(os.path.join(VIDEO, "Script_*_narration.txt"))
if not nar:
    sys.exit(f"⛔ không thấy Script_*_narration.txt trong {VIDEO}")
NARR = sorted(nar)[0]

print("═" * 72)
print(f"  KIỂM SHOT — {os.path.basename(VIDEO)}   ({N} shot)")
print("═" * 72)

# ── 1. CẤU TRÚC ────────────────────────────────────────────────────────────
P = LUAT["prompt"]
nums = [int(n) for n, _ in blocks]
chk("số prompt == số shot", len(blocks) == N, f"{len(blocks)} vs {N}")
chk("đánh số liên tục", nums == list(range(1, N + 1)),
    str(sorted(set(range(1, N + 1)) - set(nums))[:12]))
chk("đủ mọi khối bắt buộc", not [
    n for n, b in blocks
    if any(k not in b for k in P["khoi_bat_buoc"])
    or not any(k in b for k in P["khoi_chu_the_mot_trong"])])
chk("không placeholder", not [n for n, b in blocks if "[" in b or "XXX" in b])
chk(f"không prompt cụt (≥{P['so_tu_toi_thieu']['gia_tri']} từ)",
    not [n for n, b in blocks if len(b.split()) < P["so_tu_toi_thieu"]["gia_tri"]])
chk(f"mọi prompt có {P['ty_le_khung']}",
    not [n for n, b in blocks if P["ty_le_khung"] not in b])
_max = P["so_ky_tu_toi_da"]["gia_tri"]
chk(f"mọi prompt dưới {_max} ký tự", not [n for n, b in blocks if len(b.strip()) > _max],
    f"dài nhất {max(len(b.strip()) for _, b in blocks)}")
for chuoi, ly_do in P["cam_chuoi"].items():
    chk(f"cấm `{chuoi}`", not [n for n, b in blocks if re.search(chuoi, b, re.I)], ly_do)

# ── 2. NHẤT QUÁN NHÂN VẬT — khai trong shot_rules.json của từng video ───────
for kh in RIENG.get("khoi_nhan_vat", []):
    ten, moc, phai_co = kh["ten"], kh["moc"], kh.get("phai_chua")
    chi_kind = set(kh.get("chi_kind", [])) or None
    tru_kind = set(kh.get("tru_kind", []))
    hit = [b for i, (n, b) in enumerate(blocks)
           if moc in b
           and (chi_kind is None or KIND[i] in chi_kind)
           and KIND[i] not in tru_kind]
    if phai_co:
        chk(f"khối {ten} lặp Y NGUYÊN", bool(hit) and all(phai_co in b for b in hit),
            f"{len(hit)} khung")
    else:
        doan = [re.search(re.escape(moc) + r".{0,600}", b).group(0) for b in hit]
        chk(f"khối {ten} lặp Y NGUYÊN", (not hit) or len(set(doan)) == 1, f"{len(hit)} khung")

# ── 3. CHỮ TRÊN HÌNH ───────────────────────────────────────────────────────
khong_chu = lambda t: bool(re.match(r"\s*no text", t.strip(), re.I))

lech = [n for (n, b), t in zip(blocks, TEXT)
        if (not khong_chu(t)) != ("Spell it EXACTLY" in b)]
chk("lệnh ép chính tả khớp khung có chữ", not lech, str(lech[:8]))

_nh = LUAT["nhan"]["nhan_nho_toi_da_tu"]["gia_tri"]
dai = [(n, m) for (n, b), t in zip(blocks, TEXT)
       if re.search(r"label|arrow", t, re.I) and not re.search(r"headline|large|bold", t, re.I)
       for m in re.findall(r'"([^"]{2,})"', t) if len(m.split()) > _nh]
chk(f"nhãn nhỏ ≤{_nh} từ", not dai, str(dai[:5]))

# ── 4. SƠ ĐỒ PHẢI NÓI ĐƯỢC MỘT ĐIỀU ────────────────────────────────────────
SD = LUAT["so_do"]
pat = "|".join(SD["tu_khoa_subject"])
rong = [n for (n, b), su, t in zip(blocks, SUBJ, TEXT)
        if re.search(pat, su, re.I) and khong_chu(t)]
chk("sơ đồ nào cũng phải NÓI được một điều", not rong,
    f"{rong} — biểu đồ/bảng/trục mà cấm chữ thì không nói gì cả  ({SD['nguon']})")

# ── 4b. SCENE_N KHÔNG ĐƯỢC CÓ NGƯỜI TRONG SUBJECT ──────────────────────────
# 15/08/2026 — bắt được ở V20: 3 khung khai SCENE_N nhưng subject ghi "a sleeping
# figure", "several people lying around it". build_prompts dán khối NO_PERSON cho
# SCENE_N không nhắc con vật → prompt TỰ CÃI NHAU, và model nghe luật chứ không
# nghe subject. KHUNG CUỐI VIDEO ra một đống lửa không có ai.
# "body shaped dent/outline/patch" là HÌNH DẠNG, không phải người → không tính.
_NGUOI = r"\b(figures?|persons?|people|sleepers?|hunters?|somebody|someone)\b"
_HINH  = r"body[- ]shaped"
_CV_N  = (r"(?:lion|snake|wolf|hyena|leopard|bear|animal|prey|cat|dog|bird|"
          r"elephant|mammoth|deer|horse|zebra)s?")
_xung = []
for _i, (_k, _su) in enumerate(zip(KIND, SUBJ), 1):
    if _k != "SCENE_N":
        continue
    _sach = re.sub(r"\b(no|never|without)\s+" + _CV_N, "", _su, flags=re.I)
    if re.search(_CV_N, _sach, re.I):      # có con vật -> engine KHÔNG dán NO_PERSON
        continue
    _su2 = re.sub(_HINH, "", _su, flags=re.I)
    if re.search(_NGUOI, _su2, re.I):
        _xung.append(_i)
chk("SCENE_N không khai người trong subject", not _xung,
    f"{_xung} — engine dán NO_PERSON cho SCENE_N, người trong subject sẽ BỊ XOÁ. "
    "Đổi sang SCENE_A/GROUP.")

# ── 4c. SUBJECT NÓI NGỦ THÌ FACE PHẢI LÀ asleep ───────────────────────────
# 15/08/2026 — bắt được ở V20 ngay sau khi vá 4b: ba khung đổi SCENE_N -> SCENE_A
# nhưng trường face vẫn để "flat" (hồi SCENE_N thì face không dùng tới). Chủ thể
# ghi "lies asleep", khối FACE ghi mắt mở -> model vẽ người NẰM MỞ MẮT, đúng vào
# câu "in order to sleep at all" ở KHUNG CUỐI.
# phủ định phải bị loại TRƯỚC khi dò, y như engine làm với khối con vật:
# "plainly not asleep" · "never sleeping" · "eyes wide open, not asleep"
_NGU = r"\b(asleep|sleeping|eyes closed|fast asleep)\b"
_PHU = r"\b(not|never|nobody|no one|hardly|barely|far from|plainly not)\s+(?:\w+\s+){0,2}?"


def _co_ngu(su):
    return bool(re.search(_NGU, re.sub(_PHU + _NGU, "", su, flags=re.I), re.I))


_lech = [i for i, s in enumerate(SHOTS, 1)
         if s[1] in ("SCENE_A", "SCENE_W", "GROUP")
         and _co_ngu(s[2])
         and (s[5] if len(s) > 5 else "flat") != "asleep"]
chk("chủ thể nói ngủ thì face=asleep", not _lech,
    f"{_lech} — subject ghi ngủ mà FACE vẽ mắt mở, prompt tự cãi nhau")

# ── 5. CỬA CÓ NGUỒN ────────────────────────────────────────────────────────
C = LUAT["cua_chan"]["tu_moi_shot"]
w = sum(len(l.split()) for l in LOI) / N
chk(f"từ mỗi shot {C['min']}-{C['max']}", C["min"] <= w <= C["max"], f"{w:.1f}")

for g in RIENG.get("cua_rieng", []):
    dem = sum(1 for k in KIND if k == g["kind"])
    dat = dem >= g["toi_thieu"] if "toi_thieu" in g else dem / N <= g["ty_le_toi_da"]
    chk(g["ten"], dat, f"{dem} khung · {g.get('nguon','(chưa ghi nguồn)')}")

# ── 6. CHỈ BÁO — in số, KHÔNG chấm ─────────────────────────────────────────
canh = sum(1 for k in KIND if k in set(RIENG.get("kind_canh", [])))
co_chu = sum(1 for t in TEXT if not khong_chu(t))
print(f"\n   📊 cảnh {100*canh/N:.0f}%  ·  thẻ {100*(N-canh)/N:.0f}%  ·  có chữ {100*co_chu/N:.0f}%"
      f"  ·  {w:.1f} từ/shot")
print(f"      {LUAT['chi_bao']['moc_doi_thu']}")

# ── 7. LUẬT SỐNG CÒN: TTS phải đọc đúng kịch bản đã duyệt ──────────────────
a = re.sub(r"\s+", " ", " ".join(LOI)).strip().lower()
b2 = re.sub(r"\s+", " ", io.open(NARR, encoding="utf-8").read()).strip().lower()
chk("GHÉP SHOT == NARRATION nguyên văn", a == b2,
    f"{len(a.split())} vs {len(b2.split())} từ")

print("\n" + ("→ SẴN SÀNG GEN." if ok else "→ CÒN LỖI. SỬA XONG MỚI GEN."))
sys.exit(0 if ok else 1)

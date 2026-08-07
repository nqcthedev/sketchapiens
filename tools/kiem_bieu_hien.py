#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm BIỂU HIỆN — bốn file phải là bốn mặt của CÙNG MỘT bản kịch bản.

VÌ SAO CÓ FILE NÀY
──────────────────
Một version kịch bản sinh ra nhiều "biểu hiện" khác nhau:

    Script_VideoNN_narration.txt   ← BẢN GỐC, mọi thứ khác phải khớp với nó
    DUYET_VNN_EN_VI.md             ← bảng chủ ĐỌC ĐỂ DUYỆT
    SHOTLINES_FULL.txt             ← chia shot, nạp TTS
    build/TTS_input_per_shot.txt   ← đầu vào TTS thật

Chúng KHÔNG tự đồng bộ. Sửa kịch bản mà quên dựng lại bảng duyệt thì
**chủ đang duyệt một bản khác với bản sắp sản xuất**.

Đã xảy ra thật (07/08/2026): sau vòng review 5 và 6, `DUYET_V19_EN_VI.md`
lệch kịch bản **22 dòng**. Không có gì báo. Phát hiện tình cờ.

Khái niệm gốc: AYON `Product → Version → Representation`
(landscape research §4.4, ý (d) trong governance/MIGRATION_LOG.md).

CÁCH DÙNG
─────────
    python3 tools/kiem_bieu_hien.py Video19_NightWalk
    python3 tools/kiem_bieu_hien.py            # kiểm MỌI thư mục VideoNN có narration

READ-ONLY. Không sửa gì. Mã thoát 1 nếu có lỗi.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

W = {"PASS": 0, "WARN": 0, "FAIL": 0}


def say(level, msg, detail=""):
    W[level] += 1
    icon = {"PASS": "  ✅", "WARN": "  ⚠️ ", "FAIL": "  ❌"}[level]
    print(f"{icon} {msg}" + (f"  →  {detail}" if detail else ""))


def lines_of(path):
    return [l.strip() for l in open(path, encoding="utf-8") if l.strip()]


def words(text):
    return len(re.findall(r"[A-Za-z']+", text))


def check_video(d):
    print(f"\n══ {d}")

    nar = glob.glob(os.path.join(d, "Script_*_narration.txt"))
    if not nar:
        print("   (không có narration — bỏ qua)")
        return
    if len(nar) > 1:
        say("WARN", "có nhiều hơn một file narration",
            ", ".join(os.path.basename(x) for x in nar))
    nar = sorted(nar)[0]
    N = lines_of(nar)
    joined = " ".join(N)
    say("PASS", f"bản gốc {os.path.basename(nar)}", f"{len(N)} dòng · {words(joined)} từ")

    # ── biểu hiện 1: bảng duyệt EN+VI ─────────────────────────────────
    # ⛔ 07/08/2026 — chủ chốt KHÔNG đọc cột dịch nữa, bảng EN+VI đã bỏ.
    #    Thiếu bảng KHÔNG còn là lỗi. Nhưng bảng nào CÒN nằm đó thì vẫn phải
    #    khớp kịch bản — file cũ lệch mà vẫn để đó là bẫy cho phiên sau.
    duyet = glob.glob(os.path.join(d, "DUYET_*_EN_VI.md")) + \
            glob.glob(os.path.join(d, "*DUYET*EN-VI*.md"))
    if not duyet:
        print("   (không có bảng duyệt EN+VI — đúng luật mới, bỏ qua)")
    else:
        t = open(duyet[0], encoding="utf-8").read()
        def is_header(c):
            c = re.sub(r"[^A-Za-z ]", "", c).strip()       # bỏ emoji, cờ, ký tự lạ
            return c in ("EN", "VI", "") or set(c) <= {"-", " "}
        en = [m.group(1).strip() for m in re.finditer(r"^\| (.+?) \| (.+?) \|$", t, re.M)
              if not is_header(m.group(1).strip())]
        missing = [l for l in N if l not in t]
        extra = [e for e in en if e not in N]
        if missing:
            say("FAIL", f"bảng duyệt THIẾU {len(missing)} dòng của kịch bản",
                "chủ đang duyệt bản CŨ")
            for x in missing[:5]:
                print(f"       ⛔ {x[:88]}")
            if len(missing) > 5:
                print(f"       … còn {len(missing)-5} dòng")
        else:
            say("PASS", "bảng duyệt phủ đủ mọi dòng kịch bản")
        if extra:
            say("FAIL", f"bảng duyệt CÒN {len(extra)} dòng không còn trong kịch bản",
                "câu đã bị cắt vẫn nằm trong bảng")
            for x in extra[:3]:
                print(f"       ⛔ {x[:88]}")

    # ── biểu hiện 2: shotlines ────────────────────────────────────────
    sl = os.path.join(d, "SHOTLINES_FULL.txt")
    if not os.path.exists(sl):
        say("WARN", "chưa có SHOTLINES_FULL.txt", "chưa chia shot")
        S = None
    else:
        S = lines_of(sl)
        # V06-V08 đánh số ở đầu mỗi dòng shot ("001  Câu..."). Bỏ số khi so nội dung.
        numbered = sum(1 for x in S if re.match(r"^\d{3}\s", x)) > len(S) * 0.8
        S = [re.sub(r"^\d{3}\s+", "", x) for x in S] if numbered else S
        sj = " ".join(S)
        if numbered:
            say("WARN", "SHOTLINES đánh số ở đầu dòng", "khác định dạng V19 — đã bỏ số khi so")
        if sj == joined:
            say("PASS", "ghép shot == nguyên văn kịch bản", f"{len(S)} shot")
        elif joined.startswith(sj):
            say("FAIL", "ghép shot KHỚP nhưng THIẾU ĐUÔI",
                f"phủ {words(sj)}/{words(joined)} từ")
        else:
            i = next((k for k, (a, b) in enumerate(zip(sj, joined)) if a != b), None)
            say("FAIL", "ghép shot LỆCH nguyên văn kịch bản",
                f"lệch tại ký tự {i}" if i is not None else "độ dài khác")
            if i is not None:
                print(f"       shot : …{sj[max(0,i-60):i+40]}")
                print(f"       gốc  : …{joined[max(0,i-60):i+40]}")

    # ── biểu hiện 3: đầu vào TTS ──────────────────────────────────────
    tts = os.path.join(d, "build", "TTS_input_per_shot.txt")
    if not os.path.exists(tts):
        say("WARN", "chưa có build/TTS_input_per_shot.txt", "chưa tới bước TTS")
    elif S is None:
        say("WARN", "có TTS_input nhưng không có SHOTLINES để so")
    else:
        a = open(tts, encoding="utf-8").read()
        b = open(sl, encoding="utf-8").read()
        if a == b:
            say("PASS", "TTS_input == SHOTLINES", "khớp từng byte")
        else:
            say("FAIL", "TTS_input LỆCH SHOTLINES",
                f"{len(lines_of(tts))} dòng vs {len(S)} dòng — TTS sẽ đọc bản khác")

    # ── biểu hiện 4: prompt ảnh khớp số shot ──────────────────────────
    pf = os.path.join(d, "PROMPTS_FULL.txt")
    if os.path.exists(pf) and S is not None:
        pt = open(pf, encoding="utf-8").read()
        # hai kiểu đánh số đã dùng trong dự án:
        #   V19+  "001. <prompt>"   cùng dòng
        #   V02-18 "001."           số đứng riêng một dòng, prompt ở dòng sau
        n = len(re.findall(r"^\d{3}\.(?: |\s*$)", pt, re.M))
        if n == len(S):
            say("PASS", "số prompt ảnh == số shot", f"{n}")
        else:
            say("FAIL", "số prompt ảnh LỆCH số shot", f"{n} prompt vs {len(S)} shot")


targets = sys.argv[1:] or sorted(
    d for d in glob.glob("Video*") if os.path.isdir(d)
    and glob.glob(os.path.join(d, "Script_*_narration.txt")))

print("═" * 72)
print("  KIỂM BIỂU HIỆN — bốn file có phải cùng MỘT bản kịch bản không")
print("═" * 72)
for d in targets:
    check_video(d.rstrip("/"))
print("\n" + "─" * 72)
print(f"  PASS {W['PASS']}   WARN {W['WARN']}   FAIL {W['FAIL']}")
print("═" * 72)
sys.exit(1 if W["FAIL"] else 0)

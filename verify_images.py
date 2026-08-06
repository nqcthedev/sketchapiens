#!/usr/bin/env python3
"""Kiểm tra bộ ảnh gen ra có khớp file prompt không — CHẠY TRƯỚC KHI GHÉP VIDEO.
Dùng:  python3 verify_images.py <thư_mục_ảnh> <PROMPTS_FULL.txt>"""
import os, re, sys

def main(img_dir, prompts_file):
    prompts = {}
    lines = open(prompts_file, encoding="utf-8").read().splitlines()
    for i, l in enumerate(lines):
        m = re.match(r'^(\d{3})\.$', l)
        if m and i + 1 < len(lines):
            prompts[int(m.group(1))] = lines[i + 1]
    n_prompt = len(prompts)

    imgs, bad_name = {}, []
    for f in os.listdir(img_dir):
        if f.startswith('.'): continue
        m = re.match(r'^(\d+)\.(png|jpe?g|webp)$', f, re.I)
        if not m: bad_name.append(f); continue
        imgs.setdefault(int(m.group(1)), []).append(f)

    ok = True
    print(f"Prompt : {n_prompt}")
    print(f"Ảnh    : {sum(len(v) for v in imgs.values())} file, {len(imgs)} số\n")

    if bad_name:
        ok = False
        print(f"❌ {len(bad_name)} file SAI TÊN (phải là NNN.png/jpeg):")
        for f in bad_name[:10]: print(f"     {f}")

    dup = {k: v for k, v in imgs.items() if len(v) > 1}
    if dup:
        ok = False
        print(f"❌ TRÙNG SỐ: {sorted(dup)[:15]}")

    missing = [n for n in range(1, n_prompt + 1) if n not in imgs]
    if missing:
        ok = False
        print(f"❌ THIẾU {len(missing)} ảnh: {missing[:40]}{' ...' if len(missing) > 40 else ''}")

    extra = [n for n in imgs if n > n_prompt]
    if extra:
        ok = False
        print(f"❌ THỪA {len(extra)} ảnh ngoài dải prompt: {sorted(extra)[:20]}")

    tiny = [f for v in imgs.values() for f in v
            if os.path.getsize(os.path.join(img_dir, f)) < 5000]
    if tiny:
        ok = False
        print(f"❌ {len(tiny)} ảnh nghi LỖI (<5KB): {tiny[:10]}")

    print()
    if ok:
        print("✅ ĐẠT — số lượng và đánh số khớp hoàn toàn.")
    else:
        print("⛔ CHƯA ĐẠT — sửa xong mới được nạp vào GhepVideo.")

    # Bắt buộc soi mắt: 3 mốc quan trọng nhất
    print("\n--- SOI MẮT 3 MỐC (mở ảnh, đối chiếu mô tả) ---")
    for n in (1, n_prompt // 2, n_prompt):
        if n in imgs:
            t = prompts[n]; s = t.find('educational look,')
            print(f"\n[{n:03d}] file: {imgs[n][0]}")
            print(f"      hình: {t[s+17:s+200].strip()}")
    return 0 if ok else 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))

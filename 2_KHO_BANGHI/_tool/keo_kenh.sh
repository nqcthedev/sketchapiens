#!/bin/bash
# keo_kenh.sh <URL kênh hoặc playlist> <tên thư mục>
# Kéo phụ đề GỐC (en-orig, không phải bản dịch máy) + metadata của mọi video.
set -e
BASE="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$BASE/$2"; mkdir -p "$OUT/_vtt"
yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs "en-orig,en" \
  --sub-format vtt --write-info-json --ignore-errors \
  -o "$OUT/_vtt/%(upload_date)s_%(id)s.%(ext)s" "$1"
python3 - "$OUT" << 'PY'
import json,pathlib,sys,re
sys.path.insert(0,str(pathlib.Path(__file__).parent))
out=pathlib.Path(sys.argv[1]); vtt=out/"_vtt"
exec(open(out.parent/"_tool/vtt2text.py").read().split('if __name__')[0])
rows=[]
for j in sorted(vtt.glob("*.info.json")):
    m=json.loads(j.read_text()); vid=m["id"]
    f=next((x for x in [vtt/f"{j.stem.replace('.info','')}.en-orig.vtt", vtt/f"{j.stem.replace('.info','')}.en.vtt"] if x.exists()),None)
    if not f: continue
    t=vtt_to_text(f); w=len(re.findall(r"[A-Za-z']+",t)); d=m.get("duration") or 0
    name=re.sub(r"[^A-Za-z0-9]+","_",m["title"])[:60]
    (out/f"{m.get('upload_date','')}_{name}.txt").write_text(
        f"# {m['title']}\n# id={vid} · {m.get('view_count',0):,} view · {d//60}:{d%60:02d} · {w} từ · {round(w/(d/60)) if d else 0} wpm\n# https://youtu.be/{vid}\n\n{t}\n")
    rows.append((m.get('view_count',0),m['title'],d,w,round(w/(d/60)) if d else 0))
rows.sort(reverse=True)
hdr="| view | tiêu đề | dài | từ | wpm |\n|---|---|---|---|---|\n"
(out/"00_BANG.md").write_text(hdr+"\n".join(f"| {v:,} | {t[:55]} | {d//60}:{d%60:02d} | {w} | {p} |" for v,t,d,w,p in rows)+"\n")
print(f"{len(rows)} video")
PY

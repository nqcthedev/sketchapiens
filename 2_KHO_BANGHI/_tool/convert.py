import json,pathlib,sys,re
base=pathlib.Path(__file__).parent.parent
exec(open(base/"_tool/vtt2text.py").read().split('if __name__')[0])
for d in sorted(base.iterdir()):
    if not d.is_dir() or d.name=="_tool": continue
    vt=d/"_vtt"
    if not vt.exists(): continue
    rows=[]
    for j in sorted(vt.glob("*.info.json")):
        try: m=json.loads(j.read_text())
        except: continue
        stem=j.stem.replace('.info','')
        f=next((x for x in [vt/f"{stem}.en-orig.vtt", vt/f"{stem}.en.vtt"] if x.exists()),None)
        if not f: continue
        t=vtt_to_text(f); w=len(re.findall(r"[A-Za-z']+",t)); du=m.get("duration") or 0
        name=re.sub(r"[^A-Za-z0-9]+","_",m["title"])[:60]
        (d/f"{m.get('upload_date','')}_{name}.txt").write_text(
            f"# {m['title']}\n# id={m['id']} · {m.get('view_count',0):,} view · {du//60}:{du%60:02d} · {w} từ · {round(w/(du/60)) if du else 0} wpm\n# https://youtu.be/{m['id']}\n\n{t}\n")
        rows.append((m.get('view_count',0),m['title'],du,w,round(w/(du/60)) if du else 0))
    if rows:
        rows.sort(reverse=True)
        (d/"00_BANG.md").write_text("| view | tiêu đề | dài | từ | wpm |\n|---|---|---|---|---|\n"+
          "\n".join(f"| {v:,} | {t[:55]} | {du//60}:{du%60:02d} | {w} | {p} |" for v,t,du,w,p in rows)+"\n")
        print(f"{d.name}: {len(rows)}")

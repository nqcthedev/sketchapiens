import asyncio, os, edge_tts
V=os.path.dirname(os.path.abspath(__file__))
vi=[l.strip() for l in open(f"{V}/_nghe_thu_tiengviet/V20_tiengviet.txt") if l.strip()]
out=f"{V}/_audio_vi"; os.makedirs(out,exist_ok=True)
async def main():
    for i,t in enumerate(vi,1):
        f=f"{out}/{i:03d}.mp3"
        if os.path.exists(f) and os.path.getsize(f)>800: continue
        for _ in range(3):
            try:
                await edge_tts.Communicate(t,"vi-VN-NamMinhNeural",rate="+8%").save(f)
                if os.path.getsize(f)>800: break
            except Exception: await asyncio.sleep(2)
        if i%25==0: print(f"  {i}/{len(vi)}",flush=True)
    print("xong",len([f for f in os.listdir(out) if f.endswith('.mp3')]),"/",len(vi))
asyncio.run(main())

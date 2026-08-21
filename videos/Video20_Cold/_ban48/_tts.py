# -*- coding: utf-8 -*-
"""TTS bản thử hook — CÙNG giọng, CÙNG tốc độ với Axen/Zenn/V20 để so công bằng."""
import asyncio, os, edge_tts
V=os.path.dirname(os.path.abspath(__file__)); SRC=f"{V}/V20_ban48_vi.txt"; OUT=f"{V}/_mp3"
TIMEOUT,SONG,THU=8,4,12
vi=[l.strip() for l in open(SRC,encoding="utf-8") if l.strip()]
os.makedirs(OUT,exist_ok=True); xong=0
async def mot(i,t,sem):
    global xong
    f=f"{OUT}/{i:03d}.mp3"
    if os.path.exists(f) and os.path.getsize(f)>800: xong+=1; return True
    async with sem:
        for _ in range(THU):
            try:
                await asyncio.wait_for(edge_tts.Communicate(t,"vi-VN-NamMinhNeural",rate="+8%").save(f),timeout=TIMEOUT)
                if os.path.exists(f) and os.path.getsize(f)>800:
                    xong+=1; return True
            except Exception: pass
    return False
async def main():
    sem=asyncio.Semaphore(SONG)
    r=await asyncio.gather(*[mot(i,t,sem) for i,t in enumerate(vi,1)])
    hong=[i for i,ok in enumerate(r,1) if not ok]
    print(f"xong {xong}/{len(vi)}" + (f" · HỎNG: {hong}" if hong else " · sạch"))
asyncio.run(main())

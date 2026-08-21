# -*- coding: utf-8 -*-
"""TTS tiếng Việt — bản thứ BA, viết theo số đo chứ không theo phỏng đoán.

ĐO ĐƯỢC 19/08 (đừng tự sửa lại nếu chưa đo lại):
  · giọng vi-VN CHẬP CHỜN, không bị chặn cứng: 2/5 lệnh thành công
  · lần THÀNH CÔNG tốn 2,5-3,4s · lần TREO tốn TRỌN timeout
  · giọng en-US chạy 1,9s bình thường -> lỗi nằm ở phía Microsoft, không ở mạng hay code

BA LỖI CỦA HAI BẢN TRƯỚC:
  1. KHÔNG timeout      -> treo vĩnh viễn ở câu 12, retry vô dụng vì treo không ném Exception
  2. timeout 20-30s     -> mỗi lần hỏng đốt 20-30 giây, mà tỉ lệ hỏng tới 60%
  3. hạ nhiệt 25s       -> SAI THUỐC. Không phải chặn tần suất nên nghỉ lâu chẳng giúp gì,
                           chỉ làm chậm gấp bội. Câu 19 treo 3 lần = phí 75 giây vô ích.

CÁCH ĐÚNG: timeout NGẮN + thử lại NGAY + vài luồng song song.
Hỏng thì chỉ mất 8 giây rồi thử lại luôn.
"""
import asyncio, os, sys, edge_tts

V   = os.path.dirname(os.path.abspath(__file__))
SRC = f"{V}/V20_moi_tiengviet.txt"
OUT = f"{V}/_mp3_moi"
TIMEOUT, SONG, THU = 8, 4, 12          # giây · số luồng · số lần thử mỗi câu

vi = [l.strip() for l in open(SRC, encoding="utf-8") if l.strip()]
os.makedirs(OUT, exist_ok=True)
xong = 0

async def mot(i, t, sem):
    global xong
    f = f"{OUT}/{i:03d}.mp3"
    if os.path.exists(f) and os.path.getsize(f) > 800:
        xong += 1; return True
    async with sem:
        for _ in range(THU):
            try:
                await asyncio.wait_for(
                    edge_tts.Communicate(t, "vi-VN-NamMinhNeural", rate="+8%").save(f),
                    timeout=TIMEOUT)
                if os.path.exists(f) and os.path.getsize(f) > 800:
                    xong += 1
                    if xong % 25 == 0: print(f"  {xong}/{len(vi)}", flush=True)
                    return True
            except Exception:
                pass
            if os.path.exists(f) and os.path.getsize(f) <= 800:
                os.remove(f)
            await asyncio.sleep(0.4)
    print(f"  ⛔ câu {i} bỏ cuộc sau {THU} lần: {t[:50]}", flush=True)
    return False

async def main():
    sem = asyncio.Semaphore(SONG)
    r = await asyncio.gather(*[mot(i, t, sem) for i, t in enumerate(vi, 1)])
    n = len([f for f in os.listdir(OUT) if f.endswith(".mp3")])
    hong = [i for i, ok in enumerate(r, 1) if not ok]
    print(f"xong {n}/{len(vi)}" + (f"  ⛔ thiếu câu: {hong}" if hong else "  ✅ ĐỦ"))
    sys.exit(0 if not hong else 1)

asyncio.run(main())

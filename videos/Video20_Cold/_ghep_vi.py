"""Ghép bản TIẾNG VIỆT để nghe thử: 282 ảnh + tiếng Việt đọc theo TỪNG CÂU.
Thời lượng mỗi câu chia xuống các shot của câu đó theo SỐ TỪ tiếng Anh."""
import os, subprocess, sys, wave, json
V=os.path.dirname(os.path.abspath(__file__))
IMG=sys.argv[1]; A=f"{V}/_audio_vi"; W=f"{V}/_wav_vi"
OUT=f"{V}/V20_TIENGVIET_nghethu.mp4"; Wd,Hg,FPS=1920,1080,30
run=lambda c: subprocess.run(c,check=True,capture_output=True,text=True)

en=[l.strip() for l in open(f"{V}/Script_V20_narration.txt") if l.strip()]
shots=[l.rstrip("\n") for l in open(f"{V}/SHOTLINES_FULL.txt") if l.strip()]
N=len(shots)

# ── ghép shot về đúng câu: đi tuần tự, gom shot tới khi khớp câu ──
map_shot=[]; si=0
for li,cau in enumerate(en):
    goc=""; nhom=[]
    while si<N and len(goc.replace(" ",""))<len(cau.replace(" ","")):
        goc+=(" " if goc else "")+shots[si]; nhom.append(si); si+=1
    assert goc.replace(" ","")==cau.replace(" ",""), f"lệch ở câu {li+1}:\n  {goc}\n  {cau}"
    map_shot.append(nhom)
assert si==N, f"thừa {N-si} shot"
print(f"✅ 282 shot gom đúng vào {len(en)} câu")

# ── đo WAV từng câu ──
os.makedirs(W,exist_ok=True); dur=[]
for i in range(1,len(en)+1):
    w=f"{W}/{i:03d}.wav"
    if not os.path.exists(w):
        run(["ffmpeg","-y","-v","error","-i",f"{A}/{i:03d}.mp3","-ar","44100","-ac","2","-c:a","pcm_s16le",w])
    with wave.open(w) as f: dur.append(f.getnframes()/f.getframerate())
tong=sum(dur); print(f"✅ tiếng Việt {len(dur)} câu · tổng {tong:.1f}s")

lst=f"{W}/_l.txt"; open(lst,"w").write("".join(f"file '{i:03d}.wav'\n" for i in range(1,len(en)+1)))
allw=f"{V}/_all_vi.wav"; run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",lst,"-c","copy",allw])
with wave.open(allw) as f: tg=f.getnframes()/f.getframerate()
assert abs(tg-tong)<0.05, f"tiếng ghép lệch {tg-tong:.3f}s"
print(f"✅ CHỐT 1: tiếng ghép khớp ({tg:.1f}s)")

# ── chia thời lượng câu xuống shot theo SỐ TỪ, rồi neo mốc tích luỹ ──
d=[0.0]*N
for li,nhom in enumerate(map_shot):
    w=[len(shots[s].split()) for s in nhom]; tw=sum(w) or 1
    for s,x in zip(nhom,w): d[s]=dur[li]*x/tw
cum=[0.0]
for x in d: cum.append(cum[-1]+x)
fr=[round(c*FPS) for c in cum]
da=[(fr[i+1]-fr[i])/FPS for i in range(N)]

imgs=[]
for i in range(1,N+1):
    p=f"{IMG}/{i:03d}.png"
    assert os.path.exists(p), f"thiếu ảnh {i}"
    imgs.append(p)
cc=f"{V}/_concat_vi.txt"
open(cc,"w").write("".join(f"file '{p}'\nduration {x:.6f}\n" for p,x in zip(imgs,da)))
run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",cc,"-i",allw,
     "-vf",f"scale={Wd}:{Hg}:force_original_aspect_ratio=decrease,pad={Wd}:{Hg}:(ow-iw)/2:(oh-ih)/2:white,fps={FPS}",
     "-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p",
     "-c:a","aac","-b:a","160k","-t",f"{tg:.3f}",OUT])
dm=float(json.loads(run(["ffprobe","-v","quiet","-print_format","json","-show_format",OUT]).stdout)["format"]["duration"])
print(f"✅ CHỐT 2: mp4 {dm:.1f}s · tiếng {tg:.1f}s · lệch {abs(dm-tg)*1000:.0f} ms")
print(f"\n🎬 {OUT}")

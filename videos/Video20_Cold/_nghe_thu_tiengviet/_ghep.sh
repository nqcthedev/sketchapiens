#!/bin/bash
# Ghép mp3 -> một file. Đo độ dài bằng SỐ MẪU WAV, không tin ffprobe trên mp3.
#
# ⚠️ SỬA 19/08: bản trước chỉ ĐẾM file rồi ghép luôn -> ghép trúng file đang ghi dở
#    (284.mp3), ffmpeg báo "Impossible to open" nhưng VẪN cho ra file thiếu tiếng.
#    Nay kiểm TỪNG file bằng ffprobe trước khi ghép.
cd "$(dirname "$0")"
CAN=${1:-296}
n=$(ls _mp3_moi/*.mp3 2>/dev/null | wc -l | tr -d ' ')
[ "$n" -lt "$CAN" ] && { echo "⛔ mới $n/$CAN, chưa ghép"; exit 1; }
echo "kiểm từng file…"
hong=0
for f in _mp3_moi/*.mp3; do
  [ "$(stat -f%z "$f")" -lt 800 ] && { echo "  ⛔ nhỏ: $f"; hong=$((hong+1)); continue; }
  ffprobe -v error -show_entries format=duration -of csv=p=0 "$f" >/dev/null 2>&1 || { echo "  ⛔ hỏng: $f"; hong=$((hong+1)); }
done
[ "$hong" -gt 0 ] && { echo "⛔ $hong file hỏng — KHÔNG ghép"; exit 1; }
ls _mp3_moi/*.mp3 | sort | sed "s|^|file '|;s|$|'|" > _list_moi.txt
ffmpeg -y -f concat -safe 0 -i _list_moi.txt -c:a libmp3lame -b:a 128k V20_MOI_tiengviet.mp3 -loglevel error || exit 1
ffmpeg -y -i V20_MOI_tiengviet.mp3 -c:a pcm_s16le _k.wav -loglevel error
python3 -c "
import wave; w=wave.open('_k.wav'); s=w.getnframes()/w.getframerate()
print(f'✅ ghép xong — {int(s//60)}:{int(s%60):02d}  ({s:.1f}s, đo bằng số MẪU WAV)')"
rm -f _k.wav

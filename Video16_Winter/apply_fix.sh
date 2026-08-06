#!/bin/bash
# Chep 17 anh gen bu vao dung so trong thu muc anh chinh.
# Dung:  bash apply_fix.sh <thu-muc-anh-gen-bu> <thu-muc-anh-chinh>
set -e
FIX="$1"; MAIN="$2"
[ -d "$FIX" ] && [ -d "$MAIN" ] || { echo "Thieu thu muc. Dung: bash apply_fix.sh <fix-dir> <main-dir>"; exit 1; }

MAP=(001 002 009 023 025 045 049 051 068 073 076 078 113 159 162 165 166)

N=$(ls -1 "$FIX"/*.png 2>/dev/null | wc -l | tr -d ' ')
if [ "$N" != "17" ]; then echo "DUNG LAI: thu muc gen bu co $N anh, phai dung 17."; exit 1; fi

for i in "${!MAP[@]}"; do
  SRC=$(printf "%s/%03d.png" "$FIX" $((i+1)))
  DST=$(printf "%s/%s.png" "$MAIN" "${MAP[$i]}")
  [ -f "$SRC" ] || { echo "DUNG LAI: khong thay $SRC"; exit 1; }
  cp "$SRC" "$DST"
  echo "$(basename "$SRC")  ->  $(basename "$DST")"
done

echo "---"
echo "Tong anh trong thu muc chinh: $(ls -1 "$MAIN"/*.png | wc -l | tr -d ' ')  (phai la 185)"

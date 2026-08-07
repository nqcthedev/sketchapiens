#!/bin/bash
# Quét ngách: chạy nhiều truy vấn, gom kênh + view, xếp hạng
OUT="$(dirname "$0")/_quet_kenh.tsv"; : > "$OUT"
Q=(
"what did ancient humans do at night"
"how did ancient humans survive"
"why did ancient humans"
"how did early humans survive"
"ancient humans explained animation"
"stone age humans explained"
"prehistoric humans daily life explained"
"ancient humans winter cold survive"
"what did ancient humans eat"
"ancient humans predators attack"
"ancient humans sleep night"
"caveman daily life explained"
"what did early humans do all day"
"ancient humans rain wet"
"how did ancient humans give birth"
"ancient humans disease sick"
"why humans lost body hair evolution"
"ancient humans fire discovery"
)
for q in "${Q[@]}"; do
  yt-dlp --flat-playlist --playlist-items 1-20 \
    --print "%(channel)s\t%(channel_id)s\t%(view_count)s\t%(duration)s\t%(title).60s" \
    "ytsearch20:$q" 2>/dev/null >> "$OUT"
done
wc -l < "$OUT"

#!/usr/bin/env python3
"""VTT (phụ đề YouTube) -> text sạch, MỖI CÂU MỘT DÒNG.
Phụ đề tự động của YouTube cuộn chữ nên dòng nào cũng lặp lại dòng trước.
Bộ này khử lặp bằng cách chỉ giữ phần MỚI của mỗi cue."""
import re, sys, pathlib

def vtt_to_text(p):
    raw = pathlib.Path(p).read_text(encoding="utf-8", errors="ignore")
    out = []
    for line in raw.splitlines():
        s = line.strip()
        if (not s or s.startswith(("WEBVTT", "Kind:", "Language:", "NOTE"))
                or "-->" in s or re.fullmatch(r"\d+", s)):
            continue
        s = re.sub(r"<[^>]+>", "", s)            # bỏ thẻ timing trong dòng
        s = re.sub(r"\[[^\]]*\]", "", s)          # bỏ [Music] [Applause]
        s = re.sub(r"\s+", " ", s).strip()
        if s and (not out or s != out[-1]):
            out.append(s)
    # khử phần chồng lấn giữa cue trước và cue sau
    text = ""
    for seg in out:
        if not text:
            text = seg; continue
        for k in range(min(len(seg), 120), 0, -1):
            if text.endswith(seg[:k]):
                seg = seg[k:]; break
        text += (" " if seg and not seg.startswith(" ") else "") + seg
    text = re.sub(r"\s+", " ", text).strip()
    # mỗi câu một dòng
    return "\n".join(x.strip() for x in re.split(r"(?<=[.?!])\s+", text) if x.strip())

if __name__ == "__main__":
    print(vtt_to_text(sys.argv[1]))

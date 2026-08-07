# SPEC — GhepVideo Desktop (Sketchapiens Studio)

> Tool desktop Mac-M1 để **ghép ảnh sync với kịch bản** thành video, cho kênh "Người Que Cổ Đại".
> Chốt đích trước khi build. Thay thế 6 bản thử cũ (chưa bản nào ghép ra video hoàn chỉnh).

## 0. Mục tiêu 1 dòng
Nạp **1 file audio + folder ảnh 001…N + script** → tự sync (khớp ảnh theo giọng) → **editor timeline sửa được** → export MP4 hard-cut (2K/4K) bằng **ffmpeg native**. Tích hợp **tạo audio ElevenLabs API** ngay trong tool.

## 1. Stack (đã chốt — công nghệ mới nhất, native M1)
- **Shell: Tauri v2** (Rust core, ~vài MB, native Apple Silicon, bảo mật cao).
- **Frontend: React 19 + TypeScript + Vite** — port UI timeline từ `Tool_Ghep_Video/index.html` + `GhepVideo_Studio_NextJS`.
- **Render: ffmpeg 7.1 native arm64** (đã có sẵn) — gọi qua Rust command, VideoToolbox HW-accel, **1 filtergraph** (không encode 754 clip rời).
- **TTS: ElevenLabs API** (`with-timestamps`) gọi từ Rust → trả mp3 + JSON timestamp ký tự.
- **Sync fallback: whisper.cpp** (Metal M1) khi audio không phải từ ElevenLabs.
- State/project lưu bằng file JSON `.skproj` trong thư mục project.

## 2. Luồng dữ liệu & cơ chế SYNC (cốt lõi)
```
Script (1 dòng = 1 shot)  ──►  [TTS ElevenLabs API]  ──►  full_audio.mp3 + timestamps.json
        │                                                          │
   ảnh 001…N (positional: ảnh N ↔ dòng N)                          │
        │                                                          ▼
        └──────────────►  SYNC  ◄──────  timestamps.json (ký tự → mốc giây từng dòng)
                           │
                  timeline: shot N = [start,end) đúng theo giọng
                           │
                     ffmpeg hard-cut concat + mux audio gốc  ──►  final.mp4
```
**Thứ tự ưu tiên tính thời lượng mỗi ảnh (fidelity cao → thấp):**
1. **EL timestamp JSON** (chuẩn nhất, không cần transcribe) — port `timingsFromAlignment()`.
2. **whisper.cpp** align full audio (khi import mp3 ngoài) — port `tool_align_full_audio.py` (`difflib.SequenceMatcher` + nội suy + monotonic + `MIN_DUR`).
3. **proportional** theo độ dài chữ / **equal** — chốt hạ.
Ảnh ↔ dòng ↔ audio khớp bằng **số trong tên file** (natural sort: `001, 002…`). Lệch số → cảnh báo, ghép tới min.

## 3. Tính năng (FULL EDITOR)
**A. Project**: tạo/mở/lưu `.skproj` (nhớ đường dẫn audio/ảnh/script, timeline đã sửa — không chọn tay mỗi lần).
**B. Tạo audio (ElevenLabs API)**: nhập/chọn script → chọn voice (mặc định Josh `nzFihrBIvB34imQBuxub`, multilingual_v2, stab .45/sim .80/style .20) → gọi API → lưu `full_audio.mp3` + `timestamps.json`. API key lưu an toàn (Tauri secure store / .env).
**C. Auto-sync**: chạy 1 trong 3 engine → dựng timeline.
**D. Timeline editor**:
- Mỗi shot 1 hàng: **thumbnail ảnh · câu (EN) · start/end · thời lượng (sửa được)**.
- Thao tác: đổi/xóa/chèn ảnh lệch, đổi thứ tự, nudge biên shot, "kéo giãn cho khớp audio" (rescale toàn bộ theo `audio.duration/total`), gộp/tách shot.
- Gloss tiếng Việt cạnh câu EN (chủ đọc tiếng Việt).
**E. Preview**: phát audio + đổi ảnh đúng mốc, scrub, phím tắt.
**F. Captions (burned-in)**: bật/tắt, style chữ (font/size/vị trí/outline) — GAP nói "gần như bắt buộc" cho retention. Sinh từ timestamp, burn qua ffmpeg (libass).
**G. Audio polish**: chuẩn loudness **-14 LUFS** (`loudnorm`), nhạc nền + **ducking** (sidechaincompress) — tùy chọn.
**H. Export**: ffmpeg native, hard-cut tĩnh, 2K/4K, H.264+AAC, thanh tiến độ + log; xuất SRT kèm (tùy chọn).

## 4. Kiến trúc code
```
GhepVideo_Desktop/
├── src/                      # React frontend
│   ├── App.tsx, main.tsx
│   ├── components/           # Timeline, ShotRow, Preview, Toolbar, TTSPanel, ExportDialog
│   ├── lib/
│   │   ├── sync/             # elevenlabsTimestamps.ts, whisperAlign.ts, proportional.ts
│   │   ├── naturalSort.ts, timeline.ts   # port từ Studio_NextJS
│   │   └── project.ts        # load/save .skproj
│   └── types.ts
├── src-tauri/                # Rust core
│   ├── src/
│   │   ├── main.rs, lib.rs
│   │   ├── commands/         # tts.rs (EL API), whisper.rs, render.rs (ffmpeg), fs.rs
│   │   └── ffmpeg.rs         # build filtergraph, spawn, parse progress
│   ├── Cargo.toml, tauri.conf.json
│   └── binaries/             # (tùy) ffmpeg/whisper sidecar nếu không dùng system
├── package.json, vite.config.ts, tsconfig.json
└── README.md
```

## 5. ffmpeg render (hard-cut, 1 lệnh)
- Dựng file concat demuxer (`file 'NNN.png'` + `duration <d>`) hoặc filtergraph với `-loop 1 -t d` per input rồi `concat`.
- `-tune stillimage -pix_fmt yuv420p -c:v libx264` (hoặc `h264_videotoolbox` HW-accel), mux `full_audio.mp3` (`-shortest`), scale 2K/4K, fps 30.
- Progress: parse `-progress pipe:1` → thanh % trong UI.

## 6. Phase build (đều nằm trong "full editor", làm theo thứ tự chạy được sớm)
- **P1 — Skeleton chạy được (XONG):** Tauri scaffold + nạp audio/ảnh/script + sync EL-JSON/tỉ lệ/chia-đều + timeline sửa giây + kéo-giãn-khớp + export ffmpeg hard-cut → ra `.app`. Đã verify render MP4 đúng.
- **P1.5 — Nối audio rời (XONG):** up nhiều khúc audio (gõ tay ElevenLabs web, giới hạn ký tự) → sắp thứ tự ↑/↓ → nối thành 1 file (~18 phút) bằng ffmpeg → dùng làm audio nguồn. Command Rust `concat_audio`.
- **⭐ P3 — TTS in-app 100% sync (XONG):** nạp Script + API key → `elevenlabs_tts` tự chia khúc ≤9000 ký tự → gọi `/with-timestamps` (giọng Josh) từng khúc → nối audio (libmp3lame) + **dồn timestamp theo offset thời lượng thật** → 1 mp3 + 1 JSON EL đầy đủ → sync mode "json" khớp **100% từng khung hình**. **Đây là con đường CHÍNH đạt 100%** — vì timestamp là ground-truth (ElevenLabs tự sinh), KHÔNG phải đoán ngược. Verified: audio 17.37s vs timestamp 17.32s, per-câu đúng nhịp đọc. Giải luôn giới hạn ký tự (khỏi gõ tay web + nối khúc).
- **P4 — whisper.cpp align (XONG — fallback):** cho audio import NGOÀI (không phải từ tool). `whisper_align`: whisper.cpp Metal (base.en, 18 phút ~12s) → difflib.SequenceMatcher port sang Rust (khớp 92% từ, ~98% câu) → per-shot durations. Dùng khi audio đã có sẵn không kèm JSON. **Kém 100% hơn P3** vì đoán ngược từ transcript whisper.
  - Bài học: forced alignment / whisper = xấp xỉ (đoán timing từ audio). ElevenLabs with-timestamps = ground-truth 100%. Ưu tiên P3, P4 chỉ cứu audio cũ.
- **P2 — Editor sửa nâng cao:** preview phát audio + thumbnail ảnh, đổi/xóa/chèn ảnh, lưu/mở `.skproj`.
- **P5 — Captions + loudness -14 LUFS + nhạc nền + ducking + batch.**

## 7. Ràng buộc từ dự án (bắt buộc nhớ)
- Style kênh = **hard-cut tĩnh, KHÔNG hiệu ứng** (không Ken Burns mặc định). Đúng Mack/Stickly.
- Chủ đọc tiếng Việt → UI song ngữ, gloss VI cạnh text EN.
- File script đọc TTS = thuần EN, 1 câu/dòng, `...` = nghỉ hơi (`Script_Video01_FINAL_deAI.txt`).
- Dùng lâu dài, không làm demo rồi đập.

## 8. Kế thừa từ code cũ (không viết lại)
- `Tool_Ghep_Video/index.html`: logic `computeDurations()`, `timingsFromAlignment()`, bảng sửa thời lượng, "kéo giãn khớp".
- `GhepVideo_Studio_NextJS/lib`: `naturalSort.ts`, `timeline.ts`, `types.ts`, UI `Studio.tsx`.
- `2_assemble_video.py` + `tool_align_full_audio.py`: tham chiếu ffmpeg concat + whisper align.
- `1_make_tts_elevenlabs.py`: voice settings + gọi ElevenLabs.

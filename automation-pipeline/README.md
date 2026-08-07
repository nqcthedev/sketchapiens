# Ancient-Humans Faceless Video Pipeline (one image per sentence)

Bộ khung Python biến **kịch bản → video slide** kiểu kênh "Ancient Humans Explained":
tách câu → mỗi câu một prompt ảnh (style khoá cứng) → ảnh → voice → phụ đề → ráp MP4 bằng ffmpeg.

> Khớp với stack thực tế của bạn: **ảnh = Google Flow**, **voice/SFX/music = ElevenLabs**,
> **render = ffmpeg** (hoặc HyperFrames/Remotion của bạn). Pipeline này lo phần *prompt + đồng bộ + ráp*.

## Pipeline (khối → hàm trong `pipeline.py`)
1. Split câu — `read_lines`
2. Prompt ảnh / câu — `gen_prompt`  (LLM, có style khoá cứng từ `config.yaml`)
3. Ảnh — `gen_image`  (real: API; mock: vẽ stick figure tạm bằng PIL)
4. Voice + thời lượng — `gen_tts`  (ElevenLabs/OpenAI; mock: ước lượng theo số chữ)
5. Phụ đề SRT — `build_srt`
6. Ráp MP4 — `assemble`  (ffmpeg: clip/câu → concat → mux audio → burn sub)

## Cài đặt
```bash
pip install -r requirements.txt        # pyyaml, pillow, requests (+ openai cho real mode)
# cần sẵn: ffmpeg, ffprobe trong PATH
cp .env.example .env                    # điền key cho real mode
```

## Cách chạy

**A. Thử nhanh không cần key (chứng minh chạy end-to-end):**
```bash
python pipeline.py --mock --limit 12
# -> build/final.mp4 (slide stick-figure tạm + audio câm theo đúng nhịp câu)
```

**B. Workflow Google Flow (đúng cách bạn đang làm) — tách 2 chặng:**
```bash
# Chặng 1: nhả danh sách prompt để đổ vào Google Flow (batch / xoay account)
python pipeline.py --stage prompts
#   -> build/prompts.txt  (mỗi prompt 1 khối: [img_000] <style + scene>)
#   Sinh ảnh trong Flow, lưu thành img_000.png, img_001.png ... trong 1 folder

# Chặng 2: ráp video từ folder ảnh Flow xuất ra
python pipeline.py --stage assemble --images-dir /duong/dan/anh_flow
#   -> build/final.mp4   (audio: real ElevenLabs nếu có key, hoặc --mock cho câm)
```

**C. Real end-to-end (nếu muốn ảnh qua API thay vì Flow):** điền key rồi
```bash
python pipeline.py            # gen_prompt + gen_image(API) + gen_tts(ElevenLabs)
```

## Style nhất quán (chỗ khó nhất của stick-figure tự động)
- Giữ `style_prompt` trong `config.yaml` **giống hệt cho mọi ảnh**.
- Trong Flow/real: ghim thêm **seed cố định + ảnh tham chiếu/character** để 300 ảnh cùng một "kênh".
- `prompts.txt` đã ghép sẵn `[style] + [scene của câu]` để bạn dán hàng loạt.

## Ghi chú
- Burn phụ đề cần ffmpeg có **libass**. Thiếu thì pipeline tự bỏ qua, vẫn xuất `subs.srt` cho editor.
- Logo / chạy chữ / chuyển cảnh: thêm ở bước `assemble` (ffmpeg overlay/drawtext/xfade) hoặc để HyperFrames của bạn lo.
- Đây là **bán tự động**: tự hoá phần cơ học; giữ tay người ở packaging (tiêu đề/thumbnail) + QA.

## Moat (phần khó thật, không phải render)
Như bạn nói: **nghiên cứu thị trường → tìm nội dung có khả năng đề xuất → viết giữ chân.**
Hai thứ đó nằm ở: `kho/3_bangchung/BANG_CAU_TatCa_CuNo_2026-07-29.md` + `kho/3_bangchung/NGHIENCUU_CloneSwarm_2026-07-29.md` (research/đề xuất) ⛔ *(SoTay_ChonDeTai đã chết)* và skill
`viet-kich-ban-nguoi-que-co-dai` (retention). Pipeline này chỉ là khâu sản xuất phía sau.

# 🎬 Ghép Video Studio — Sketchapiens

App web ghép **ảnh + audio (cắt theo từng câu)** thành video khớp 100%: mỗi ảnh tự chạy đúng độ dài file tiếng cùng số thứ tự. Có **zoom Ken Burns nhẹ** và xuất **MP4 4K** bằng công nghệ mới nhất.

Chạy **hoàn toàn trong trình duyệt** — không server, không gửi dữ liệu đi đâu, không tốn phí.

---

## Công nghệ

| Hạng mục | Lựa chọn |
|---|---|
| Build tool | **Vite 6** + **TypeScript** (strict) |
| Engine xuất chính | **[Mediabunny](https://mediabunny.dev)** + **WebCodecs** → MP4 (H.264/AAC), encode nhanh hơn thời gian thực, ghi thẳng ra ổ đĩa qua File System Access |
| Engine dự phòng | **MediaRecorder** → `.webm` (cho trình duyệt cũ / offline) |
| Đóng gói | `vite-plugin-singlefile` → 1 file `dist/index.html` tự chứa, double-click chạy |

## Cấu trúc dự án

```
ghepvideo-studio/
├── index.html                # điểm vào Vite
├── package.json
├── tsconfig.json
├── vite.config.ts
└── src/
    ├── main.ts               # khởi động app
    ├── style.css
    ├── types.ts              # kiểu dữ liệu dùng chung
    ├── config.ts             # hằng số, bitrate, độ phân giải
    ├── core/
    │   ├── naturalSort.ts    # sắp file theo số trong tên
    │   ├── assets.ts         # nạp ảnh + giải mã audio
    │   ├── timeline.ts       # dựng timeline theo độ dài tiếng
    │   └── renderer.ts       # vẽ khung + Ken Burns
    ├── engines/
    │   ├── engine.ts         # interface ExportEngine + lỗi điều khiển
    │   ├── mediabunny.ts     # engine chính (WebCodecs → MP4)
    │   ├── mediarecorder.ts  # engine dự phòng (.webm)
    │   └── select.ts         # chọn engine theo trình duyệt
    └── ui/
        └── app.ts            # giao diện + nối sự kiện
```

## Chạy & build

Cần [Node.js](https://nodejs.org) ≥ 18.

```bash
npm install        # cài thư viện (lần đầu)
npm run dev        # chạy thử ở http://localhost:5173
npm run build      # kiểm kiểu + build → thư mục dist/
npm run preview    # xem thử bản build
```

Sau `npm run build`, mở **`dist/index.html`** là dùng được — đây là **một file tự chứa**, có thể double-click chạy offline hoặc copy đi đâu cũng được.

## Đăng lên web miễn phí (tùy chọn)

Để có một đường link mở mọi lúc mọi nơi (không cần file):

- **Netlify / Vercel:** kéo-thả thư mục `dist/` vào trang của họ → ra link ngay.
- **GitHub Pages:** đẩy `dist/` lên nhánh `gh-pages`.

## Cách dùng

1. **① Ảnh** — chọn tất cả ảnh (`001.png, 002.png, …`).
2. **② Audio** — chọn tất cả file tiếng cắt theo câu (`001.mp3, …`), cùng số thứ tự với ảnh.
3. **③** chọn độ phân giải (4K…), bật/tắt chuyển động.
4. **④ Xuất video** → (nếu hỏi) chọn nơi lưu → đợi encode → ra `final_video.mp4`.

> Mẹo: bấm **Xem trước (10s)** để kiểm tra nhanh trước khi xuất cả video.

## Lưu ý

- Engine Mediabunny cần trình duyệt có **WebCodecs** (Chrome/Edge mới nhất). Thiếu thì app **tự chuyển** sang bản `.webm`.
- Cần **số ảnh = số audio** và đặt tên cùng số thứ tự thì mới khớp chuẩn.
- Toàn bộ xử lý chạy tại máy bạn; không có dữ liệu nào rời khỏi trình duyệt.

## Giấy phép

Mã dự án: dùng tự do cho mục đích cá nhân của kênh. Thư viện Mediabunny theo giấy phép MPL-2.0.

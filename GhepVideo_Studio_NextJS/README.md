# 🎬 Ghép Video Studio — Next.js

App ghép **ảnh + audio (cắt theo từng câu)** thành video khớp 100%: mỗi ảnh tự chạy đúng độ dài file tiếng cùng số. Có **zoom Ken Burns** và xuất **MP4 4K** bằng WebCodecs. Chạy hoàn toàn trong trình duyệt — không gửi dữ liệu đi đâu.

Stack: **Next.js 15 (App Router) · React 19 · TypeScript · [Mediabunny](https://mediabunny.dev) (WebCodecs)**.

---

## ⚡ Cách chạy nhanh nhất (Mac)

Double-click **`start.command`**. Lần đầu nó tự cài thư viện, rồi tự mở trình duyệt ở địa chỉ http://localhost:3000.

> Nếu Mac báo chặn file lạ: chuột phải vào `start.command` → **Open** → **Open**.

## Cách chạy thủ công (mọi hệ máy)

Cần [Node.js](https://nodejs.org) ≥ 18.

```bash
npm install      # chỉ lần đầu (tải thư viện, ~1-2 phút, cần mạng)
npm run dev      # mỗi khi muốn dùng → mở http://localhost:3000
```

Dừng server: bấm `Ctrl + C` trong cửa sổ terminal.

## Build / deploy (tùy chọn)

```bash
npm run build    # kiểm lỗi + build production
npm run start    # chạy bản production
```

Muốn có **link online mở mọi nơi**: đẩy thư mục này lên GitHub rồi import vào [Vercel](https://vercel.com) (free) — Vercel tự build & cho link.

## Cấu trúc

```
ghepvideo-next/
├── app/
│   ├── layout.tsx          # khung HTML gốc
│   ├── page.tsx            # trang chính (render <Studio/>)
│   └── globals.css
├── components/
│   └── Studio.tsx          # giao diện ('use client') + nối sự kiện
├── lib/                    # LÕI độc lập framework (tái dùng được)
│   ├── types.ts · config.ts
│   ├── core/   naturalSort · assets · timeline · renderer
│   └── engines/ engine · mediabunny · mediarecorder · select
├── next.config.mjs · tsconfig.json · package.json
```

## Cách dùng

1. **① Ảnh** — chọn tất cả ảnh (`001.png, …`).
2. **② Audio** — chọn tất cả tiếng cắt theo câu (`001.mp3, …`) cùng số thứ tự.
3. **③** chọn độ phân giải (4K…), bật chuyển động.
4. **④ Xuất video** → (nếu hỏi) chọn nơi lưu → ra `final_video.mp4`.

> Bấm **Xem trước (10s)** để kiểm tra nhanh trước khi xuất full.

## Lưu ý

- Engine Mediabunny cần **WebCodecs** (Chrome/Edge mới). Thiếu → app tự chuyển sang `.webm`.
- Cần **số ảnh = số audio**, đặt tên cùng số thứ tự thì mới khớp.
- Mọi xử lý chạy tại máy bạn; không dữ liệu nào rời trình duyệt.

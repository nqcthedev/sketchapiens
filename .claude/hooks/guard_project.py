#!/usr/bin/env python3
"""Sketchapiens — hook cưỡng chế trước mọi Write/Edit/MultiEdit.

Chỉ chặn những luật PHẢI được cưỡng chế. Không dùng hook để "suy nghĩ".
Giao thức: đọc JSON ở stdin. exit 0 = cho qua. exit 2 = chặn, lý do ghi ra stderr.
"""
import json, os, re, sys

def block(msg):
    print(f"⛔ CHẶN BỞI guard_project.py\n{msg}", file=sys.stderr)
    sys.exit(2)

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)                      # không đọc được thì không chặn oan

tool = data.get("tool_name", "")
if tool not in ("Write", "Edit", "MultiEdit"):
    sys.exit(0)

ti = data.get("tool_input", {}) or {}
path = ti.get("file_path") or ti.get("path") or ""
if not path:
    sys.exit(0)

root = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
try:
    rel = os.path.relpath(path, root)
except ValueError:
    rel = path
rel = rel.replace(os.sep, "/")

# ── 1. Version kịch bản BẤT BIẾN — đã tạo thì không sửa
if re.search(r"/03-script/versions/v\d{3}[^/]*\.md$", rel) and os.path.exists(path):
    block(f"`{rel}` đã tồn tại. Version kịch bản KHÔNG BAO GIỜ được sửa.\n"
          "Sửa = tạo `vNNN` kế tiếp rồi trỏ `refs/current.yaml` sang nó.\n"
          "(CLAUDE.md luật 1 · .claude/rules/script-files.md)")

# ── 2. Con trỏ approved / published: CHỈ NGƯỜI đặt
if re.search(r"/03-script/refs/(approved|published)\.yaml$", rel):
    body = ti.get("content", "") or ti.get("new_string", "") or ""
    if not re.search(r"^\s*set_by:\s*owner\s*$", body, re.M):
        which = "approved" if "approved" in rel else "published"
        block(f"`{rel}` là con trỏ {which.upper()} — CHỈ NGƯỜI được đặt.\n"
              "Nội dung phải có đúng dòng:  set_by: owner\n"
              "Agent không được tự phong duyệt hay tự suy ra đã đăng.\n"
              "(CLAUDE.md luật 2-3)")

# ── 3. Bản ghi run là bất biến — thử lại thì tạo run mới
if re.search(r"/runs/(image|tts|render)/[A-Z]{3}-\d{8}-\d{3}/manifest\.(ya?ml|json)$", rel) \
        and os.path.exists(path):
    block(f"`{rel}` đã tồn tại. Bản ghi một lần chạy là BẤT BIẾN.\n"
          "Chạy lại = tạo run_id mới, không ghi đè lần trước.")

# ── 3b. Kịch bản cũ read-only cho tới khi có lệnh migration
#    07/08: thư mục video chuyển vào videos/ → dùng search chứ không match neo đầu chuỗi,
#    và chấp nhận cả đường dẫn cũ lẫn mới.
if re.search(r"(?:^|/)(?:videos/)?Video[^/]*/.*Script_.*_narration\.txt$", rel):
    block(f"`{rel}` là kịch bản cũ, READ-ONLY.\n"
          "Chúng không có lịch sử phiên bản. Migration cần lệnh riêng.\n"
          "(.claude/rules/script-files.md)")

# ── 4. Không xoá / rỗng hoá file đang tồn tại bằng Write
if tool == "Write" and os.path.exists(path):
    content = ti.get("content", "")
    if content.strip() == "":
        block(f"Write rỗng lên file đang tồn tại `{rel}` = xoá nội dung. Bị chặn.")

# ── 5. Không commit secret: chặn ghi giá trị giống khoá thật vào file
content = ti.get("content", "") or ti.get("new_string", "") or ""
for pat, name in ((r"sk-[A-Za-z0-9]{20,}", "OpenAI-style key"),
                  (r"AIza[0-9A-Za-z_\-]{30,}", "Google API key"),
                  (r"xi-[a-f0-9]{30,}", "ElevenLabs key"),
                  (r"ghp_[A-Za-z0-9]{30,}", "GitHub token")):
    if re.search(pat, content):
        block(f"Nội dung chứa thứ trông như {name}.\n"
              "Khoá phải đọc từ biến môi trường, không ghi vào file. (CLAUDE.md §6)")

# ── 6. Không sửa global scope từ trong project
if "/.claude/skills/" in path and not path.startswith(root):
    block("Không được sửa skill TOÀN CỤC từ trong project.\n"
          "Override bằng luật project-local. (CLAUDE.md §3)")
if "/memory/" in path and "/.claude/projects/" in path:
    block("Không được sửa memory toàn cục trong nhiệm vụ này.")

sys.exit(0)

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

# ── 1. Bất biến: approved / published không bao giờ được sửa
if re.search(r"/(approved|published)\.md$", rel):
    block("`approved.md` và `published.md` là BẤT BIẾN.\n"
          "Sửa sau khi duyệt → tạo `vNNN` mới rồi duyệt lại. (CLAUDE.md luật 1)")

# ── 2. Không ghi đè version kịch bản đã tồn tại
if re.search(r"/03-script/v\d{3}[^/]*\.md$", rel) and os.path.exists(path):
    block(f"`{rel}` đã tồn tại. Version kịch bản KHÔNG được ghi đè.\n"
          "Tạo `vNNN` kế tiếp. (CLAUDE.md luật 1)")

# ── 3. Kịch bản cũ read-only cho tới khi có lệnh migration
if re.match(r"Video[^/]*/.*Script_.*_narration\.txt$", rel):
    block(f"`{rel}` là kịch bản cũ, READ-ONLY.\n"
          "Chúng không có lịch sử phiên bản và chưa được git bao phủ.\n"
          "Migration cần lệnh riêng. (.claude/rules/script-files.md)")

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

#!/usr/bin/env python3
"""Shim — logic thật ở tools/validate_shots.py (MỘT bản cho mọi video).
Giữ file này để `python3 validate_shots.py` chạy được từ trong thư mục video."""
import os, subprocess, sys
d = os.path.dirname(os.path.abspath(__file__))
sys.exit(subprocess.call([sys.executable,
    os.path.join(d, "..", "..", "tools", "validate_shots.py"), d] + sys.argv[1:]))

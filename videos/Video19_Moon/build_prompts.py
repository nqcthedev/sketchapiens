#!/usr/bin/env python3
"""Shim — logic thật ở tools/build_prompts.py (MỘT bản cho mọi video)."""
import os, subprocess, sys
d = os.path.dirname(os.path.abspath(__file__))
sys.exit(subprocess.call([sys.executable,
    os.path.join(d, *"../..".split("/"), "tools", "build_prompts.py"), d] + sys.argv[1:]))

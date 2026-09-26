#!/usr/bin/env python3
"""Small fail-closed secret-pattern review for this public research repository.

This is a POC control, not a replacement for organizational secret scanning.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", "__pycache__"}
SKIP_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".zip"}
PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github token": re.compile(r"gh[pousr]_[A-Za-z0-9]{30,}"),
    "aws access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "generic password assignment": re.compile(r"(?i)password\s*[:=]\s*['\"][^'\"]{8,}['\"]"),
}

hits = []
for path in ROOT.rglob("*"):
    if not path.is_file() or any(part in SKIP_PARTS for part in path.parts) or path.suffix.lower() in SKIP_SUFFIXES:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for label, pattern in PATTERNS.items():
        if pattern.search(text):
            hits.append(f"{path.relative_to(ROOT)}: possible {label}")

if hits:
    raise SystemExit("FAIL: possible secrets detected\n" + "\n".join(hits))
print("PASS: no high-signal secret patterns detected")

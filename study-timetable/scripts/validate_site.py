#!/usr/bin/env python3
"""Validate the static study-timetable package without requiring a build toolchain."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
required = [SITE / "index.html", SITE / "support.js", SITE / "vendor" / "react.js", SITE / "vendor" / "react-dom.js"]
missing = [str(p.relative_to(ROOT)) for p in required if not p.is_file()]
if missing:
    print("Missing required files:", ", ".join(missing), file=sys.stderr)
    raise SystemExit(1)

html = (SITE / "index.html").read_text(encoding="utf-8")
checks = {
    "doctype": r"<!doctype html>",
    "title": r"<title>[^<]+</title>",
    "react runtime": r"vendor/react\.js",
    "react-dom runtime": r"vendor/react-dom\.js",
    "support runtime": r"support\.js",
    "design component": r"<x-dc>",
    "logic component": r"data-dc-script",
}
failed = [name for name, pattern in checks.items() if not re.search(pattern, html, re.I)]
if failed:
    print("Failed checks:", ", ".join(failed), file=sys.stderr)
    raise SystemExit(1)

print(f"Validated study timetable site: {len(html):,} bytes, {len(required)} required files present")

#!/usr/bin/env python3
"""Validate the Data-Sources repository. Standard library only.

    python3 tools/validate.py

Checks: every synthetic text file carries a SYNTHETIC banner near the top and
parses (JSON), every synthetic folder README shows the prominent banner,
synthetic/index.json lists every file with synthetic: true and is current,
the public catalog has every required field and catalog.md is current, and no
public evidence snapshot claims to be synthetic.
"""
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYN = ROOT / "synthetic"
BANNER = "SYNTHETIC"
PROMINENT = "SYNTHETIC — fictional data for training/workshops, not real patients/products"
SCAN_LINES = 12
TEXT = {".md", ".csv", ".json", ".jsonl", ".txt", ".yaml", ".yml"}
errors = []

for f in sorted(SYN.rglob("*")):
    if not f.is_file() or f.suffix.lower() not in TEXT:
        continue
    rel = f.relative_to(ROOT)
    text = f.read_text(encoding="utf-8")
    head = "".join(text.splitlines(keepends=True)[:SCAN_LINES]).upper()
    if BANNER not in head:
        errors.append(f"{rel}: missing a SYNTHETIC banner in the first {SCAN_LINES} lines")
    if f.suffix == ".json":
        try:
            json.loads(text)
        except json.JSONDecodeError as e:
            errors.append(f"{rel}: invalid JSON ({e})")

for d in [SYN] + [p for p in SYN.iterdir() if p.is_dir() and p.name != "__pycache__"]:
    readme = d / "README.md"
    if not readme.exists():
        errors.append(f"{d.relative_to(ROOT)}/: no README.md")
    elif PROMINENT not in readme.read_text(encoding="utf-8"):
        errors.append(f"{readme.relative_to(ROOT)}: missing the prominent '{PROMINENT}' banner")

idx = json.loads((SYN / "index.json").read_text(encoding="utf-8"))
if not all(e.get("synthetic") is True for e in idx["files"]):
    errors.append("synthetic/index.json: an entry is not synthetic: true")
for e in idx["files"]:
    for k in ("path", "product", "therapeutic_area", "description", "used_by"):
        if k not in e:
            errors.append(f"index entry {e.get('path')}: missing {k}")
    if not (ROOT / e["path"]).exists():
        errors.append(f"index entry {e['path']}: file does not exist")

for p in sorted((ROOT / "public/evidence-snapshots").glob("*.json")):
    j = json.loads(p.read_text(encoding="utf-8"))
    if j.get("source_kind") != "real_public":
        errors.append(f"{p.relative_to(ROOT)}: public snapshot must be source_kind real_public")

for cmd in (["tools/build_index.py", "--check"], ["tools/build_catalog.py", "--check"]):
    r = subprocess.run([sys.executable, *cmd], cwd=ROOT, capture_output=True, text=True)
    (print(r.stdout.strip()) if r.returncode == 0 else errors.append((r.stdout + r.stderr).strip()))

if errors:
    print(f"{len(errors)} error(s):"); [print("  -", e) for e in errors]; sys.exit(1)
print(f"All checks passed: {idx['count']} synthetic files, public catalog current.")

#!/usr/bin/env python3
"""Build the "everything at once" release assets into dist/.

    python3 tools/build_bundles.py            # writes dist/*
    python3 tools/build_bundles.py --out DIR

Assets (published on the GitHub Release; stable URLs
https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/<asset>):
  all-synthetic-data.zip            every synthetic file (SYNTHETIC banner kept in every file)
  synthetic-<pack>.zip              one ZIP per pack
  all-synthetic.jsonl               every synthetic CSV row and document, one JSON object per line
  all-synthetic-combined-csv.zip    one CSV per table type across the three packs (+ pack, product columns)
  all-data-catalog.zip              manifest.json/csv, public catalog, synthetic index, real evidence snapshots
  manifest.json, manifest.csv       copies of the manifest

Only files hosted in this repository are bundled. Third-party public data is never
bundled; LINK ONLY sources are never downloaded. Deterministic (fixed timestamps).
Standard library only.
"""
import argparse, csv, io, json, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYN = ROOT / "synthetic"
LABEL = "SYNTHETIC — fictional data for training/workshops, not real patients/products"
STAMP = (2026, 10, 1, 0, 0, 0)
READ_FIRST = f"""{LABEL}

Open-Medical-Affairs Data-Sources: synthetic workshop data.
Nordvant Biopharma, NORVANTIB, DERMALYX and ADIPOSYN do not exist. No record describes a real
person, patient, company or medicine. Never cite these files as evidence, never mix them with
real data, and never add real company or patient data.

Source: https://github.com/Open-Medical-Affairs/Data-Sources (Apache-2.0, see LICENSE and NOTICE).
Index of every file: synthetic/index.json. Manifest of everything: manifest.json.
"""
PACKS = {"oncology-mm": "NORVANTIB", "immunology-ad": "DERMALYX", "cardiometabolic-obesity": "ADIPOSYN", "connected": "all"}
SKIP = {"__pycache__"}


def add(z, arc, data):
    info = zipfile.ZipInfo(arc, STAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    z.writestr(info, data if isinstance(data, bytes) else data.encode("utf-8"))


def files_under(folder):
    return sorted(p for p in folder.rglob("*") if p.is_file() and not SKIP & set(p.parts) and p.suffix != ".pyc")


def read_csv(p):
    lines = p.read_text(encoding="utf-8").splitlines()
    banner = [l for l in lines if l.startswith("#")]
    body = [l for l in lines if not l.startswith("#")]
    return banner, list(csv.DictReader(io.StringIO("\n".join(body))))


def zip_files(path, entries, extra=None):
    with zipfile.ZipFile(path, "w") as z:
        for arc, data in (extra or []):
            add(z, arc, data)
        for p in entries:
            add(z, p.relative_to(ROOT).as_posix(), p.read_bytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "dist"))
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    legal = [("LICENSE", (ROOT / "LICENSE").read_bytes()), ("NOTICE", (ROOT / "NOTICE").read_bytes()),
             ("SYNTHETIC-READ-ME-FIRST.txt", READ_FIRST)]
    syn = files_under(SYN)
    zip_files(out / "all-synthetic-data.zip", syn, legal)
    for pack in PACKS:
        zip_files(out / f"synthetic-{pack}.zip", files_under(SYN / pack), legal)

    idx = json.loads((SYN / "index.json").read_text(encoding="utf-8"))
    meta = {e["path"]: e for e in idx["files"]}
    jl, tables = [], {}
    for p in syn:
        rel = p.relative_to(ROOT).as_posix()
        e = meta.get(rel, {})
        if e.get("kind") == "tooling" or p.suffix in (".sqlite", ".py"):
            continue
        pack = rel.split("/")[1] if rel.count("/") >= 2 else "all"
        base = {"synthetic": True, "label": LABEL, "pack": pack, "product": PACKS.get(pack, "all"), "file": rel}
        if p.suffix == ".csv":
            banner, rows = read_csv(p)
            for i, r in enumerate(rows, 1):
                jl.append(dict(base, record_type="csv_row", row_number=i, row=r))
            if pack in ("oncology-mm", "immunology-ad", "cardiometabolic-obesity"):
                tables.setdefault(p.name, []).append((pack, banner, rows))
        else:
            jl.append(dict(base, record_type="document", format=p.suffix.lstrip(".") or "text", text=p.read_text(encoding="utf-8")))
    (out / "all-synthetic.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in jl), encoding="utf-8")

    with zipfile.ZipFile(out / "all-synthetic-combined-csv.zip", "w") as z:
        for arc, data in legal:
            add(z, arc, data)
        for name, parts in sorted(tables.items()):
            cols = list(parts[0][2][0].keys()) if parts[0][2] else []
            if any((list(r[0].keys()) if r else cols) != cols for _, _, r in parts):
                continue  # shapes differ: do not force a combination
            buf = io.StringIO()
            buf.write(f"# {LABEL}. Combined across packs from synthetic/<pack>/{name}\n")
            w = csv.DictWriter(buf, fieldnames=["pack", "product"] + cols, lineterminator="\n")
            w.writeheader()
            for pack, _, rows in parts:
                for r in rows:
                    w.writerow(dict(r, pack=pack, product=PACKS[pack]))
            add(z, "combined/" + name, buf.getvalue())

    cat_files = [ROOT / "manifest.json", ROOT / "manifest.csv", ROOT / "public/catalog.json", ROOT / "public/catalog.md",
                 ROOT / "public/README.md", SYN / "index.json"] + files_under(ROOT / "public/evidence-snapshots")
    zip_files(out / "all-data-catalog.zip", cat_files, [("LICENSE", legal[0][1]), ("NOTICE", legal[1][1])])
    for n in ("manifest.json", "manifest.csv"):
        (out / n).write_bytes((ROOT / n).read_bytes())
    for p in sorted(out.iterdir()):
        print(f"{p.stat().st_size:>10,}  {p.name}")
    print(f"jsonl records: {len(jl)}; combined tables: {len(tables)}")


if __name__ == "__main__":
    main()

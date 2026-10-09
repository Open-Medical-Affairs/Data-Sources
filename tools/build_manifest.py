#!/usr/bin/env python3
"""Build manifest.json and manifest.csv: one row per dataset, synthetic and public.

    python3 tools/build_manifest.py           # write manifest.json + manifest.csv
    python3 tools/build_manifest.py --check   # CI: fail if they are stale

Every row has: id, name, type, group, format, license, data_policy, link_only,
access, direct_url, view_url. Synthetic files are downloadable one by one
(direct_url is a raw.githubusercontent link). Public sources are LINKED, never
mirrored: direct_url is the official download or API address, view_url the
official landing page. LINK ONLY sources are never downloaded by our tools.
Standard library only.
"""
import argparse, csv, io, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "https://github.com/Open-Medical-Affairs/Data-Sources"
RAW = "https://raw.githubusercontent.com/Open-Medical-Affairs/Data-Sources/main/"
BLOB = REPO + "/blob/main/"
LATEST = REPO + "/releases/latest/download/"
SYN_LABEL = "SYNTHETIC — fictional data for training/workshops, not real patients/products"

# Official machine endpoints for public sources whose terms allow a direct fetch.
# Small API samples (a few records) or official bulk files, fetched from the source, never mirrored here.
PUBLIC_FETCH = {
    "dailymed": ("api-sample", "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name=semaglutide&pagesize=5", "JSON"),
    "openfda": ("api-sample", "https://api.fda.gov/drug/label.json?search=openfda.generic_name:semaglutide&limit=1", "JSON"),
    "rxnav": ("api-sample", "https://rxnav.nlm.nih.gov/REST/drugs.json?name=semaglutide", "JSON"),
    "mesh": ("api-sample", "https://id.nlm.nih.gov/mesh/lookup/descriptor?label=obesity&match=exact", "JSON"),
    "clinicaltables-icd10cm": ("api-sample", "https://clinicaltables.nlm.nih.gov/api/icd10cm/v3/search?sf=code,name&terms=obesity", "JSON"),
    "crossref": ("api-sample", "https://api.crossref.org/works?query=semaglutide&rows=5&select=DOI,title,published,container-title", "JSON"),
    "openalex": ("api-sample", "https://api.openalex.org/works?search=semaglutide&per-page=5&select=id,doi,title,publication_year", "JSON"),
    "drugsatfda-files": ("bulk-file", "https://www.fda.gov/media/89850/download", "ZIP"),
}

BUNDLES = [
    ("all-synthetic-data.zip", "Every synthetic file in one ZIP (all packs, CRM tables, SQLite, READMEs)", "ZIP"),
    ("all-synthetic.jsonl", "Every synthetic CSV row and document in one JSON Lines file, tagged with pack and file", "JSONL"),
    ("all-synthetic-combined-csv.zip", "One combined CSV per table type across the three packs, with pack and product columns", "ZIP"),
    ("synthetic-oncology-mm.zip", "Oncology pack only (NORVANTIB)", "ZIP"),
    ("synthetic-immunology-ad.zip", "Immunology pack only (DERMALYX)", "ZIP"),
    ("synthetic-cardiometabolic-obesity.zip", "Cardiometabolic pack only (ADIPOSYN)", "ZIP"),
    ("synthetic-connected.zip", "Connected practice CRM only (CSV tables + SQLite)", "ZIP"),
    ("all-data-catalog.zip", "Manifest (JSON + CSV), public catalog, synthetic index and real evidence snapshots", "ZIP"),
    ("manifest.json", "This manifest (JSON)", "JSON"),
    ("manifest.csv", "This manifest (CSV)", "CSV"),
]

FIELDS = ["id", "name", "type", "group", "product", "format", "license", "data_policy", "link_only",
          "access", "direct_url", "view_url", "size_bytes", "rows", "description"]


def slug(path):
    return path.replace("synthetic/", "").replace("/", "-").rsplit(".", 1)[0].lower()


def build():
    idx = json.loads((ROOT / "synthetic/index.json").read_text(encoding="utf-8"))
    cat = json.loads((ROOT / "public/catalog.json").read_text(encoding="utf-8"))
    rows = []
    for e in idx["files"]:
        p = ROOT / e["path"]
        if e.get("kind") == "tooling":
            continue
        rows.append({
            "id": "syn-" + slug(e["path"]), "name": e["path"].split("/")[-1], "type": "synthetic",
            "group": "",
            "product": e.get("product", ""), "format": e.get("format", ""),
            "license": "Apache-2.0 (fictional data)", "data_policy": "synthetic", "link_only": False,
            "access": "download", "direct_url": RAW + e["path"], "view_url": BLOB + e["path"],
            "size_bytes": p.stat().st_size if p.exists() and p.suffix != ".sqlite" else None, "rows": e.get("rows"),  # SQLite bytes vary by build
            "description": e.get("description", ""),
        })
    for p in sorted((ROOT / "public/evidence-snapshots").glob("*.json")):
        rel = p.relative_to(ROOT).as_posix()
        rows.append({
            "id": "pub-snapshot-" + p.stem, "name": p.name, "type": "public-snapshot", "group": p.stem,
            "product": "", "format": "JSON", "license": "Crossref metadata (facts, free to reuse); papers keep their own licences",
            "data_policy": "open", "link_only": False, "access": "download", "direct_url": RAW + rel,
            "view_url": BLOB + rel, "size_bytes": p.stat().st_size, "rows": None,
            "description": "REAL public paper metadata (titles and DOIs) for practising evidence searches. Never evidence for the fictional products.",
        })
    for s in cat["sources"]:
        link_only = s["data_policy"] == "link-only"
        kind, durl, fmt = PUBLIC_FETCH.get(s["id"], (None, None, None))
        if link_only:
            kind, durl = None, None
        rows.append({
            "id": "pub-" + s["id"], "name": s["name"], "type": "public", "group": s["group"], "product": "",
            "format": fmt or ", ".join((s.get("agent_readiness") or {}).get("formats") or []),
            "license": s["license"], "data_policy": s["data_policy"], "link_only": link_only,
            "access": "link-only" if link_only else (kind or "official-site"),
            "direct_url": durl or s.get("api_docs") or s["url"], "view_url": s["url"],
            "size_bytes": None, "rows": None, "description": s["contents"],
        })
    for r in rows:
        if r["type"] == "synthetic":
            r["group"] = r["direct_url"].split("/synthetic/")[1].split("/")[0] if "/" in r["direct_url"].split("/synthetic/")[1] else "all"
    counts = {
        "total": len(rows),
        "synthetic_files": sum(r["type"] == "synthetic" for r in rows),
        "public_snapshots": sum(r["type"] == "public-snapshot" for r in rows),
        "public_sources": sum(r["type"] == "public" for r in rows),
        "individually_downloadable": sum(r["access"] in ("download", "api-sample", "bulk-file") for r in rows),
        "public_fetchable_from_source": sum(r["access"] in ("api-sample", "bulk-file") for r in rows),
        "public_official_site_only": sum(r["access"] == "official-site" for r in rows),
        "link_only": sum(r["link_only"] for r in rows),
    }
    manifest = {
        "name": "Open-Medical-Affairs Data-Sources manifest",
        "version": 1,
        "repo": REPO,
        "synthetic_label": SYN_LABEL,
        "public_warning": cat["warning"],
        "access_legend": {
            "download": "Hosted in this repository. direct_url downloads the file.",
            "api-sample": "Real public source. direct_url is a small live query to the official API (fetched from the source, not mirrored here).",
            "bulk-file": "Real public source. direct_url is the official bulk download file from the source.",
            "official-site": "Real public source. direct_url is the official download or API page; read its terms first.",
            "link-only": "LINK ONLY: never copy this data into repositories, decks or shared files. Use it at the source under its own terms.",
        },
        "everything_at_once": [{"asset": a, "description": d, "format": f, "url": LATEST + a} for a, d, f in BUNDLES],
        "counts": counts,
        "datasets": rows,
    }
    js = json.dumps(manifest, indent=1, ensure_ascii=False) + "\n"
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=FIELDS, lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow({k: ("" if r[k] is None else str(r[k]).lower() if isinstance(r[k], bool) else r[k]) for k in FIELDS})
    return js, buf.getvalue(), counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    js, cs, counts = build()
    targets = {ROOT / "manifest.json": js, ROOT / "manifest.csv": cs}
    if a.check:
        stale = [p.name for p, t in targets.items() if not p.exists() or p.read_text(encoding="utf-8") != t]
        if stale:
            sys.exit("stale: " + ", ".join(stale) + " (run python3 tools/build_manifest.py)")
        print("manifest current"); return
    for p, t in targets.items():
        p.write_text(t, encoding="utf-8")
    print("wrote manifest.json + manifest.csv", json.dumps(counts))


if __name__ == "__main__":
    main()

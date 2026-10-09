#!/usr/bin/env python3
"""Download Open-Medical-Affairs data to a local folder. No installs: Python 3 standard library only.

    python3 tools/fetch_all.py                        # everything into ./oma-data
    python3 tools/fetch_all.py --out my-folder
    python3 tools/fetch_all.py --only synthetic       # just the synthetic practice data
    python3 tools/fetch_all.py --only public          # just the public samples and bulk files
    python3 tools/fetch_all.py --id syn-oncology-mm-field-observations   # one dataset (repeatable)
    python3 tools/fetch_all.py --list                 # show every dataset id and how it is accessed

What it does
  * Synthetic data (SYNTHETIC, fictional): downloads every file one by one from the repository,
    keeping the folder layout, plus a SYNTHETIC-READ-ME-FIRST.txt.
  * Real public sources: for sources whose terms allow it, fetches a small live sample from the
    official API, or the official bulk file, straight from the source (never from a mirror).
    Sources marked "official-site" only have an official download/API page: the script prints it.
  * LINK ONLY sources are never downloaded. The script prints where to get them and why.
  * Writes manifest.json and a SOURCES.md with every link next to the data.

Never send PHI or confidential company data to a public source. Synthetic files are never evidence.
"""
import argparse, json, sys, time, urllib.request
from pathlib import Path

MANIFEST_URLS = [
    "https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/manifest.json",
    "https://raw.githubusercontent.com/Open-Medical-Affairs/Data-Sources/main/manifest.json",
]
UA = "Open-Medical-Affairs-fetch_all/1.0 (+https://github.com/Open-Medical-Affairs/Data-Sources)"
LOCAL = Path(__file__).resolve().parents[1] / "manifest.json"


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def load_manifest(src):
    if src:
        return json.loads(Path(src).read_text(encoding="utf-8")) if not src.startswith("http") else json.loads(get(src))
    for u in MANIFEST_URLS:
        try:
            return json.loads(get(u))
        except Exception:
            continue
    if LOCAL.exists():
        return json.loads(LOCAL.read_text(encoding="utf-8"))
    sys.exit("Could not load the manifest. Check your internet connection.")


def target(out, d):
    if d["type"] in ("synthetic", "public-snapshot"):
        return out / d["direct_url"].split("/main/", 1)[1]
    ext = {"JSON": ".json", "ZIP": ".zip", "CSV": ".csv"}.get(d["format"], ".dat")
    return out / "public" / "fetched" / (d["id"][4:] + ext)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="oma-data")
    ap.add_argument("--only", choices=["synthetic", "public"])
    ap.add_argument("--id", action="append", default=[], help="dataset id from the manifest (repeatable)")
    ap.add_argument("--manifest", help="path or URL of a manifest.json (default: latest release)")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    m = load_manifest(a.manifest)
    ds = m["datasets"]
    if a.list:
        for d in ds:
            print(f"{d['access']:<14} {d['id']:<55} {d['direct_url']}")
        return
    if a.id:
        known = {d["id"] for d in ds}
        bad = [i for i in a.id if i not in known]
        if bad:
            sys.exit("Unknown id(s): " + ", ".join(bad) + "  (see --list)")
        ds = [d for d in ds if d["id"] in a.id]
    elif a.only == "synthetic":
        ds = [d for d in ds if d["type"] == "synthetic"]
    elif a.only == "public":
        ds = [d for d in ds if d["type"] != "synthetic"]

    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    got, links, link_only, failed = 0, [], [], []
    if any(d["type"] == "synthetic" for d in ds):
        (out / "SYNTHETIC-READ-ME-FIRST.txt").write_text(m["synthetic_label"] + "\nFictional company, products and people. Never cite as evidence; never mix with real data.\n", encoding="utf-8")
    for d in ds:
        if d["link_only"] or d["access"] == "link-only":
            link_only.append(d); continue
        if d["access"] == "official-site":
            links.append(d); continue
        dest = target(out, d)
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            dest.write_bytes(get(d["direct_url"], timeout=180))
            got += 1
            print(f"  ok  {dest.relative_to(out)}")
        except Exception as e:
            failed.append((d, str(e)))
            print(f"  !!  {d['id']}: {e}")
        if d["type"] == "public":
            time.sleep(0.4)  # be polite to public APIs
    (out / "manifest.json").write_text(json.dumps(m, indent=1, ensure_ascii=False), encoding="utf-8")
    lines = ["# Sources and links", "", m["public_warning"], "", "| Dataset | Access | Licence | Official link |", "|---|---|---|---|"]
    lines += [f"| {d['name']} | {d['access']} | {d['license']} | {d['direct_url']} |" for d in ds if d["type"] == "public"]
    (out / "SOURCES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\nDownloaded {got} file(s) into {out}/")
    if links:
        print(f"\n{len(links)} public source(s) are available from their official site (read the terms first):")
        for d in links:
            print(f"  - {d['name']}: {d['direct_url']}")
    if link_only:
        print(f"\nLINK ONLY: {len(link_only)} source(s) were NOT downloaded. Their terms restrict copying or redistribution.")
        print("Use them at the source, under their own terms:")
        for d in link_only:
            print(f"  - {d['name']}: {d['view_url']}  ({d['license'][:90]})")
    if failed:
        print(f"\n{len(failed)} download(s) failed; re-run to retry.")
        sys.exit(1)


if __name__ == "__main__":
    main()

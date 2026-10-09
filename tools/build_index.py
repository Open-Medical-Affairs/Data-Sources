#!/usr/bin/env python3
"""Build synthetic/index.json: one machine-readable entry per synthetic file.

    python3 tools/build_index.py                                  # keep existing used_by
    python3 tools/build_index.py --skills-repo ../Medical-Affairs-Skills   # refresh used_by
    python3 tools/build_index.py --check                          # CI: fail if stale

Every entry carries synthetic: true. used_by lists the Medical-Affairs-Skills
missions (workshop/catalog.json), team missions (workshop/missions/*.md) and
skills (catalog skill_inputs) that read the file. Standard library only.
"""
import argparse, csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SYN = ROOT / "synthetic"
OUT = SYN / "index.json"
RAW = "https://raw.githubusercontent.com/Open-Medical-Affairs/Data-Sources/main/"
BLOB = "https://github.com/Open-Medical-Affairs/Data-Sources/blob/main/"
PACKS = {
    "oncology-mm": ("Oncology", "Relapsed/refractory multiple myeloma", "NORVANTIB"),
    "immunology-ad": ("Immunology", "Moderate-to-severe atopic dermatitis", "DERMALYX"),
    "cardiometabolic-obesity": ("Cardiometabolic", "Obesity and weight management", "ADIPOSYN"),
}
CONNECTED = {
    "accounts": "Institutions with capacity and scientific need", "hcps": "Fictional clinicians, channel preferences and permissions",
    "interactions": "Field interactions with verbatims and source links", "enquiries": "Medical information enquiries",
    "content_assets": "Content library with review status and due dates", "engagement": "Education engagement: invited, attended, pre/post scores",
    "patient_partnerships": "Patient organization inputs and quote permissions", "projects": "Evidence projects with cost, hours and dependencies",
    "access_log": "Institutional access routes and rules", "msl_tasks": "MSL task queue with owners and due dates",
    "source_links": "Source registry with file hashes", "medical-affairs": "All connected tables in one SQLite file (no server or login)",
    "data-dictionary": "Fields, joins and row counts", "README": "How to use the connected practice organization",
}
TOOLING = {"generate.py": "Deterministic generator for the three therapeutic-area packs",
           "synthetic_expansion.py": "Extended cross-functional artefacts used by generate.py",
           "SKILL-COVERAGE.md": "Which skill each synthetic artefact exercises", "README.md": "What the synthetic data is and how to use it",
           "index.json": None}


def first_h1(p):
    m = re.search(r"^# (.+)$", p.read_text(encoding="utf-8"), re.M)
    return m.group(1).strip() if m else ""


def pack_table(readme):
    out = {}
    for line in readme.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| `([^`]+)` \| (.+?) \|$", line)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def csv_shape(p):
    with p.open(encoding="utf-8") as fh:
        rows = list(csv.reader(l for l in fh if not l.startswith("#")))
    return max(len(rows) - 1, 0), rows[0] if rows else []


# Readers that are scripts rather than catalog entries.
EXTRA = {
    "synthetic/connected/medical-affairs.sqlite": {"skills": ["data-connection"], "scripts": ["scripts/query_database.py", "scripts/msl_admin.py"]},
    "synthetic/connected/enquiries.csv": {"skills": ["data-connection", "medical-information-response"]},
    "synthetic/connected/source_links.csv": {"skills": ["data-connection", "citation-integrity"]},
    "synthetic/oncology-mm/advisory-board-transcript.md": {"scripts": ["scripts/transcribe.py"]},
}


def usage(skills_repo):
    """Map 'synthetic/<ta or connected>/<file>' -> used_by from the skills repo."""
    use = {}
    def add(rel, kind, name):
        for ta in PACKS:
            r = rel.replace("{ta}", ta)
            for pre in ("Data-Sources/", "workshop/data/"):
                if r.startswith(pre):
                    r = "synthetic/" + r[len(pre):] if pre == "workshop/data/" else r[len(pre):]
            if r.startswith("synthetic/"):
                use.setdefault(r, {"missions": set(), "team_missions": set(), "skills": set()})[kind].add(name)
    cat = json.loads((skills_repo / "workshop/catalog.json").read_text(encoding="utf-8"))
    for m in cat["missions"]:
        for rel in m["inputs"]:
            add(rel, "missions", m["id"])
    for skill, rels in cat.get("skill_inputs", {}).items():
        for rel in rels:
            add(rel, "skills", skill)
    for f in sorted((skills_repo / "workshop/missions").glob("mission-*.md")):
        for name in re.findall(r"^- `([^`]+)` — ", f.read_text(encoding="utf-8"), re.M):
            for ta in PACKS:
                add(f"synthetic/{ta}/{name}", "team_missions", f.stem)
    for rel, extra in EXTRA.items():
        u = use.setdefault(rel, {"missions": set(), "team_missions": set(), "skills": set()})
        for kk, vv in extra.items():
            u.setdefault(kk, set()).update(vv)
    return {k: {kk: sorted(vv) for kk, vv in v.items()} for k, v in use.items()}


def build(skills_repo=None):
    old = {}
    if OUT.exists():
        old = {e["path"]: e.get("used_by") for e in json.loads(OUT.read_text(encoding="utf-8"))["files"]}
    use = usage(skills_repo) if skills_repo else None
    files = []
    for p in sorted(SYN.rglob("*")):
        if not p.is_file() or "__pycache__" in p.parts:
            continue
        rel = p.relative_to(ROOT).as_posix()
        parts = p.relative_to(SYN).parts
        if len(parts) == 1:
            if TOOLING.get(p.name) is None:
                continue
            e = {"path": rel, "synthetic": True, "kind": "tooling" if p.suffix == ".py" else "documentation",
                 "therapeutic_area": "all", "product": "all (NORVANTIB, DERMALYX, ADIPOSYN)", "description": TOOLING[p.name]}
        elif parts[0] in PACKS:
            short, area, product = PACKS[parts[0]]
            desc = pack_table(SYN / parts[0] / "README.md").get(p.name) or re.sub(r"\s+—\s+.*$", "", first_h1(p)) if p.suffix == ".md" else pack_table(SYN / parts[0] / "README.md").get(p.name)
            e = {"path": rel, "synthetic": True, "kind": "therapeutic-area-pack", "therapeutic_area": area, "ta_id": parts[0],
                 "product": product, "description": desc or p.stem.replace("-", " ").capitalize()}
        elif parts[0] == "connected":
            e = {"path": rel, "synthetic": True, "kind": "practice-organization", "therapeutic_area": "all", "ta_id": "connected",
                 "product": "all (NORVANTIB, DERMALYX, ADIPOSYN)", "description": CONNECTED.get(p.stem, p.stem)}
        else:
            raise SystemExit(f"unclassified synthetic file: {rel}")
        e["format"] = {"md": "Markdown", "csv": "CSV", "json": "JSON", "sqlite": "SQLite", "py": "Python"}.get(p.suffix[1:], p.suffix[1:].upper())
        if p.suffix == ".csv":
            e["rows"], e["columns"] = csv_shape(p)
        e["raw_url"], e["url"] = RAW + rel, BLOB + rel
        e["used_by"] = (use.get(rel, {"missions": [], "team_missions": [], "skills": []}) if use is not None
                        else old.get(rel) or {"missions": [], "team_missions": [], "skills": []})
        files.append(e)
    doc = {"label": "SYNTHETIC DATA — fictional data for training/workshops, not real patients/products",
           "name": "Open-Medical-Affairs synthetic workshop data", "synthetic": True,
           "company": "Nordvant Biopharma (fictional)", "scenario_date": "2026-10-01",
           "used_by_source": "github.com/Open-Medical-Affairs/Medical-Affairs-Skills workshop/catalog.json and workshop/missions/",
           "path_in_skills_repo": "Clone this repository into Data-Sources/ at the root of Medical-Affairs-Skills; then Data-Sources/<path> resolves.",
           "packs": [{"id": k, "therapeutic_area": v[1], "product": v[2], "folder": f"synthetic/{k}/",
                      "files": sum(1 for f in files if f.get("ta_id") == k)} for k, v in PACKS.items()]
                    + [{"id": "connected", "therapeutic_area": "all", "product": "all", "folder": "synthetic/connected/",
                        "files": sum(1 for f in files if f.get("ta_id") == "connected")}],
           "count": len(files), "files": files}
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills-repo", type=Path)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    text = build(a.skills_repo)
    if a.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            sys.exit("synthetic/index.json is stale. Run: python3 tools/build_index.py")
        print("synthetic/index.json is current.")
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote synthetic/index.json ({json.loads(text)['count']} files)")

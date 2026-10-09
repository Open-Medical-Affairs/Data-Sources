#!/usr/bin/env python3
"""Render public/catalog.md from public/catalog.json (the source of truth).

    python3 tools/build_catalog.py           # write catalog.md
    python3 tools/build_catalog.py --check   # CI: fail if catalog.md is stale or a field is missing
"""
import argparse, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
J, M = ROOT / "public/catalog.json", ROOT / "public/catalog.md"
REQUIRED = ["id", "name", "rank", "group", "url", "api_docs", "contents", "medical_affairs_jobs", "skills", "access",
            "rate_limit", "license", "data_policy", "agent_readiness", "caveats", "verification"]
POLICY_LABEL = {"open": "Open", "check-terms": "Check terms", "link-only": "**LINK ONLY: do not copy data**"}


def check_fields(c):
    errs = []
    ids = [s["id"] for s in c["sources"]]
    if len(ids) != len(set(ids)):
        errs.append("duplicate source ids")
    for s in c["sources"]:
        errs += [f"{s.get('id')}: missing {k}" for k in REQUIRED if k not in s]
        if s.get("data_policy") not in POLICY_LABEL:
            errs.append(f"{s['id']}: bad data_policy")
    grouped = [i for g in c["groups"] for i in g["source_ids"]]
    if sorted(grouped) != sorted(ids):
        errs.append("groups do not cover every source exactly once")
    if [s["id"] for s in sorted((s for s in c["sources"] if s["rank"]), key=lambda s: s["rank"])] != c["top15"]:
        errs.append("top15 order does not match ranks")
    return errs


def render(c):
    by = {s["id"]: s for s in c["sources"]}
    n = c["counts"]
    L = ["# Public data sources for Medical Affairs agents", "",
         f"> **REAL PUBLIC SOURCES — NOT SYNTHETIC.** {c['warning'].split('NOT SYNTHETIC. ', 1)[-1]}", "",
         f"**{n['sources']} sources** in **{n['groups']} Medical Affairs job groups**, checked {c['verified_on']}. "
         f"Machine-readable twin: [`catalog.json`](catalog.json). This repository **links** to these sources; it does not mirror their data.", "",
         "**Data policy:** " + " · ".join(f"`{k}`: {v}" for k, v in c["data_policy_legend"].items()), "",
         "**Verification:** " + " · ".join(f"`{k}`: {v}" for k, v in c["verification_legend"].items()), "",
         "**Already used by the skills** (Medical-Affairs-Skills `scripts/public_evidence.py`): "
         + ", ".join(by[i]["name"] for i in c["already_used_by_skills"]) + ".", "",
         "## Top 15: add first", "", "Ranked for the launch-planning swarm and the hackathon missions.", "",
         "| # | Source | Why first | Access | Agent-ready | Policy | Verified |", "|---|---|---|---|---|---|---|"]
    for i in c["top15"]:
        s = by[i]; ar = s["agent_readiness"]
        ready = ("JSON API" if ar["json_api"] else "Files/web") + ("; MCP" if "official" in ar["mcp"].lower() and "no official" not in ar["mcp"].lower() else "")
        L.append(f"| {s['rank']} | [{s['name']}]({s['url']}) | {s.get('why_top15', '')} | {s['access']} | {ready} | {POLICY_LABEL[s['data_policy']]} | {s['verification']['status']} |")
    lo = [by[i] for g in c["groups"] for i in g["source_ids"] if by[i]["data_policy"] == "link-only"]
    L += ["", "## Link only: do not copy data", "", "Point agents and people to these sources, but never copy their data into a repository, deck or shared file.", ""]
    L += [f"- **[{s['name']}]({s['url']})**: {s['data_policy_note']}" for s in lo]
    for g in c["groups"]:
        L += ["", f"## {g['title']}", "", f"_{g['medical_affairs_jobs']}_"]
        for i in g["source_ids"]:
            s = by[i]; ar = s["agent_readiness"]
            tags = (["**#%d in top 15**" % s["rank"]] if s["rank"] else []) + (["_already used by the skills_"] if s["already_used_by_skills"] else []) \
                   + (["**LINK ONLY: do not copy data**"] if s["data_policy"] == "link-only" else [])
            L += ["", f"### {s['name']}" + (" · " + " · ".join(tags) if tags else ""), "",
                  f"- **URL:** {s['url']}  ", f"- **API docs:** {s['api_docs']}  ", f"- **Contents:** {s['contents']}  ",
                  f"- **Medical Affairs jobs:** {', '.join(s['medical_affairs_jobs'])}  ", f"- **Skills:** {', '.join('`%s`' % k for k in s['skills'])}  ",
                  f"- **Access:** {s['access']}  ", f"- **Rate limit:** {s['rate_limit']}  ", f"- **License:** {s['license']}  ",
                  f"- **Data policy:** {POLICY_LABEL[s['data_policy']]} — {s['data_policy_note']}  ",
                  f"- **Agent readiness:** {'JSON API' if ar['json_api'] else 'no JSON API'}; {', '.join(ar['formats'])}; MCP: {ar['mcp']}  ",
                  f"- **Caveats:** {s['caveats'] or '—'}  ",
                  f"- **Verification:** `{s['verification']['status']}` on {s['verification']['checked_on']}. {s['verification']['note']}"]
    L += ["", "## Not included / notes", "",
          "- **Congress abstracts:** no free, open, agent-callable API was found for ASCO, ASH, EASD or AAD abstract libraries. Use journal-supplement records via Crossref, OpenAlex or Europe PMC, plus bioRxiv/medRxiv for preprints. Coverage is **UNVERIFIED**.",
          "- **MedDRA / SNOMED CT:** need licenses (SNOMED CT through a UMLS Affiliate license). Never commit their content to an open repository.",
          "- **Cochrane Library:** returned HTTP 429 to our probe; not reviewed.",
          "- **Social and patient forums:** prefer FDA PFDD reports. Monitored social data can trigger adverse-event reporting obligations.", ""]
    return "\n".join(L)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--check", action="store_true"); a = ap.parse_args()
    c = json.loads(J.read_text(encoding="utf-8"))
    errs = check_fields(c)
    if errs:
        sys.exit("catalog.json errors:\n  " + "\n  ".join(errs))
    text = render(c)
    if a.check:
        if M.read_text(encoding="utf-8") != text:
            sys.exit("public/catalog.md is stale. Run: python3 tools/build_catalog.py")
        print(f"public catalog OK: {len(c['sources'])} sources, catalog.md current.")
    else:
        M.write_text(text, encoding="utf-8"); print(f"wrote public/catalog.md ({len(c['sources'])} sources)")

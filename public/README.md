# Public data sources

> **REAL PUBLIC SOURCES — NOT SYNTHETIC.** This folder catalogs real, public data sources and
> keeps a few real bibliographic snapshots. Keep it strictly separate from `synthetic/`. Never cite
> a real paper as evidence for a fictional product, and never send PHI or confidential company
> data in a query.

| File | What it is |
|---|---|
| [`catalog.md`](catalog.md) | 52 public sources grouped by Medical Affairs job, top 15 ranked, license caveats shown |
| [`catalog.json`](catalog.json) | The same catalog, machine-readable (the source of truth) |
| [`evidence-snapshots/`](evidence-snapshots/README.md) | Real Crossref bibliographic metadata, three teaching examples per therapeutic area |

## Catalog fields

Each source in `catalog.json` has: `id`, `name`, `rank` (1–15 or null), `group`, `url`,
`api_docs`, `contents`, `medical_affairs_jobs`, `skills`, `access`, `rate_limit`, `license`,
`data_policy` (`open` · `check-terms` · `link-only`) with `data_policy_note`, `agent_readiness`
(`json_api`, `mcp`, `formats`), `caveats`, `already_used_by_skills`, and `verification`
(`status`, `checked_on`, `note`).

**`link-only` means do not copy data**: point to the source, but never copy its data into a
repository, deck or shared file (non-commercial, no-redistribution or licence-restricted terms).

Six sources are already wired into the Medical-Affairs-Skills gateway
(`scripts/public_evidence.py`): PubMed, ClinicalTrials.gov v2, openFDA, Europe PMC, Crossref and OpenAlex.

Edit `catalog.json`, then run `python3 tools/build_catalog.py` to regenerate `catalog.md`.

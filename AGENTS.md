# AGENTS.md: instructions for AI agents

You are working with **Open-Medical-Affairs/Data-Sources**: data for Medical Affairs agents in two
halves that must never be mixed.

| Half | Folder | Truth status | Index to read first |
|---|---|---|---|
| Synthetic datasets | `synthetic/` | **SYNTHETIC — fictional data for training/workshops, not real patients/products** | `synthetic/index.json` |
| Public sources | `public/` | **REAL public data, linked not mirrored** | `public/catalog.json` |

Raw base URL: `https://raw.githubusercontent.com/Open-Medical-Affairs/Data-Sources/main/`

## Discover everything

- `https://raw.githubusercontent.com/Open-Medical-Affairs/Data-Sources/main/synthetic/index.json`: every synthetic file (`synthetic: true`, `product`, `therapeutic_area`, `ta_id`, `description`, `format`, `rows`/`columns` for CSV, `raw_url`, `used_by.missions` / `used_by.team_missions` / `used_by.skills`).
- `https://raw.githubusercontent.com/Open-Medical-Affairs/Data-Sources/main/public/catalog.json`: 52 public sources (`groups`, `top15`, `already_used_by_skills`, `sources[]` with `url`, `api_docs`, `medical_affairs_jobs`, `skills`, `access`, `rate_limit`, `license`, `data_policy`, `agent_readiness`, `caveats`, `verification`).
- Human versions: `synthetic/README.md`, `public/catalog.md`.

## Synthetic workflow (workshops, demos, hackathons)

1. Pick the pack: `oncology-mm` (NORVANTIB), `immunology-ad` (DERMALYX), `cardiometabolic-obesity` (ADIPOSYN), or `connected` (a fictional CRM across all three).
2. Filter `synthetic/index.json` by `ta_id` and by `used_by` for the mission or skill you are running. Read only what you need.
3. Fetch files by `raw_url`. The SQLite file needs no server: `sqlite3 synthetic/connected/medical-affairs.sqlite .tables`.
4. Scan human-sourced records (field notes, transcripts, enquiries) for simulated safety findings first. Never enter them into real reporting systems.
5. Mark every output **SYNTHETIC** and **DRAFT**. Contradictions between files are deliberate; report them, do not smooth them over.

## Public-source workflow (real evidence)

1. Choose sources in `public/catalog.json` by `medical_affairs_jobs`, `skills` or `group`. Prefer `top15` and sources where `agent_readiness.json_api` is true.
2. Respect `rate_limit`. Never send PHI or confidential company data in a query.
3. Obey `data_policy`:
   - `open`: query and cite with attribution.
   - `check-terms`: read `license` and `data_policy_note` before reusing data.
   - `link-only`: **do not copy data**. Link to the source and summarize in your own words only where its terms allow.
4. Record the query, date and URL for every retrieval. Retrieval does not verify a claim; check the source.

## Rules

- **Never mix truth statuses.** Real papers are never evidence for fictional products, and synthetic records are never presented as real.
- Do not invent sources, numbers or citations. If a source is unreachable, say so.
- Do not send, publish or update external systems. Outputs are drafts for qualified human review; the human is the final judge.

## With Medical-Affairs-Skills

The skills repository (<https://github.com/Open-Medical-Affairs/Medical-Affairs-Skills>) expects this
repository at `Data-Sources/` in its root (git-ignored), a sibling `../Data-Sources`, or
`MA_DATA_SOURCES=/path`. Its paths then read `Data-Sources/synthetic/<pack>/<file>`.

## Maintainers

```bash
python3 synthetic/generate.py && python3 tools/build_connected.py
python3 tools/build_index.py --skills-repo ../Medical-Affairs-Skills
python3 tools/build_catalog.py
python3 tools/validate.py
```

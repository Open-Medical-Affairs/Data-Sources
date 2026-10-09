# Data-Sources

**Data for Medical Affairs AI agents, in two clearly separated halves:**

| | What | Where | Truth status |
|---|---|---|---|
| 🧪 | **Synthetic datasets**: fictional company, products, clinicians and records for training, workshops and hackathons | [`synthetic/`](synthetic/README.md) | **SYNTHETIC: fictional, not real patients or products** |
| 🌐 | **Public sources**: a catalog of 52 real, free public data sources grouped by Medical Affairs job | [`public/`](public/README.md) | **REAL: public data, linked not mirrored** |

Companion to [Medical-Affairs-Skills](https://github.com/Open-Medical-Affairs/Medical-Affairs-Skills),
the open library of Medical Affairs agent skills. The skills read the synthetic packs for their
workshop missions and call the public sources for real evidence. The data lives here so it can
grow, version and be reused on its own.

```bash
git clone https://github.com/Open-Medical-Affairs/Data-Sources.git
```

---

## 🧪 Synthetic datasets

> **⚠️ SYNTHETIC — fictional data for training/workshops, not real patients/products.**
> Nordvant Biopharma, NORVANTIB, DERMALYX and ADIPOSYN do not exist. No real person, patient,
> company or medicine is described. Never cite these files as evidence.

| Pack | Therapeutic area | Fictional product | Contents |
|---|---|---|---|
| [`synthetic/oncology-mm/`](synthetic/oncology-mm/README.md) | Relapsed/refractory multiple myeloma | NORVANTIB | 31 files: field notes, KOL dossiers, MI enquiries, plans, manuscripts, MLR comments… |
| [`synthetic/immunology-ad/`](synthetic/immunology-ad/README.md) | Moderate-to-severe atopic dermatitis | DERMALYX | the same 31-file schema |
| [`synthetic/cardiometabolic-obesity/`](synthetic/cardiometabolic-obesity/README.md) | Obesity | ADIPOSYN | the same 31-file schema |
| [`synthetic/connected/`](synthetic/connected/README.md) | All three | all | A practice CRM: 11 linked CSV tables + one SQLite file (no server, no login) |

- **Machine-readable:** [`synthetic/index.json`](synthetic/index.json): every file with `synthetic: true`, product, therapeutic area, description, raw link and which skills and missions use it.
- **Flaws are deliberate.** Seeded adverse events, a product complaint, off-label use and contradictions between sources are part of the exercise.
- **Regenerate:** `python3 synthetic/generate.py && python3 tools/build_connected.py` (deterministic, standard library only).

## 🌐 Public sources

> **REAL PUBLIC SOURCES.** Check each source's terms before copying data. Never send PHI or
> confidential company data in a query. Retrieval does not verify a scientific claim.

- [`public/catalog.md`](public/catalog.md) (human) and [`public/catalog.json`](public/catalog.json) (agents): **52 sources in 11 Medical Affairs job groups**: literature, trials, regulatory and labels, safety, payer/HTA and guidelines, HCPs and transparency, epidemiology and RWD, vocabularies, science and mechanism, patient voice, and MCP plumbing.
- **Top 15** are ranked for launch planning and the hackathon (DailyMed, EMA JSON, RxNav, NPPES, CMS Open Payments, Part D Prescribers…).
- **6 are already used by the skills**: PubMed, ClinicalTrials.gov v2, openFDA, Europe PMC, Crossref, OpenAlex.
- **11 are flagged `link-only`: do not copy data** (for example IHME GBD, ORCID, NICE outside the UK, Reddit, UMLS). Link to them; never copy their data into a repo, deck or shared file.
- [`public/evidence-snapshots/`](public/evidence-snapshots/README.md): real Crossref metadata, three teaching papers per therapeutic area. Never evidence for the fictional products.

---

## How agents should use this

1. Read [`AGENTS.md`](AGENTS.md) (or [`llms.txt`](llms.txt)).
2. **Synthetic work** (workshops, demos, hackathons): look up files in `synthetic/index.json` and fetch them by `raw_url`. Mark every output **SYNTHETIC** and **DRAFT**.
3. **Real evidence**: pick a source from `public/catalog.json` by `medical_affairs_jobs` or `skills`, respect `rate_limit` and `data_policy`, record the query and date, and cite the source.
4. **Never merge the two.** Real papers are never evidence for NORVANTIB, DERMALYX or ADIPOSYN.

**With the skills repository:** clone this repo into `Data-Sources/` at the root of
Medical-Affairs-Skills (it is git-ignored there), so paths like
`Data-Sources/synthetic/oncology-mm/product-profile.md` resolve:

```bash
git clone https://github.com/Open-Medical-Affairs/Medical-Affairs-Skills.git
cd Medical-Affairs-Skills
git clone https://github.com/Open-Medical-Affairs/Data-Sources.git
python3 scripts/workshop.py check
```

A sibling checkout (`../Data-Sources`) or `MA_DATA_SOURCES=/path/to/Data-Sources` also works.

## Repository layout

```
Data-Sources/
├── README.md · AGENTS.md · llms.txt · LICENSE · NOTICE
├── synthetic/                 SYNTHETIC — fictional
│   ├── README.md · index.json · SKILL-COVERAGE.md
│   ├── generate.py · synthetic_expansion.py
│   ├── oncology-mm/            31 files + README (NORVANTIB)
│   ├── immunology-ad/          31 files + README (DERMALYX)
│   ├── cardiometabolic-obesity/ 31 files + README (ADIPOSYN)
│   └── connected/              11 CSV + SQLite + data dictionary + README
├── public/                    REAL — public sources
│   ├── README.md · catalog.json · catalog.md
│   └── evidence-snapshots/     3 Crossref snapshots + README
└── tools/                     build_connected.py · build_index.py · build_catalog.py · validate.py
```

Validate before you commit: `python3 tools/validate.py`.

## License and terms

- **Synthetic data, catalog text and tools:** Apache-2.0 ([LICENSE](LICENSE)), the same as Medical-Affairs-Skills.
- **Public sources** are owned by their publishers and governed by **their own terms**. This
  repository only links to them and records each license as we understood it on the check date;
  that is not legal advice. `link-only` sources must not be copied.
- The evidence snapshots hold bibliographic metadata only (no abstracts or full text).
- Nothing here is a medical device, clinical decision support or a pharmacovigilance system.
  Outputs built on it are drafts for qualified human review.

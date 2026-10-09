# Data-Sources

![On the left, a sandbox of fictional practice files marked with caution tape; on the right, real public sources such as regulators and registries; an AI agent and a Medical Affairs colleague in the middle](assets/data-hero.jpg)

**The data your AI agent can practice and work with: a fictional Medical Affairs company to rehearse on, and a guide to 52 real public data sources.**

## Get the data

There are two ways. Both are free and need no account.

**One dataset.** Open the [dataset list](manifest.csv) (or [`manifest.json`](manifest.json) for agents). Every row has a **direct download link** and a **view link**.
- 🧪 Synthetic files download straight from this repository.
- 🌐 Public sources link to the **official** download or API page, with the licence next to it. Sources marked **LINK ONLY** must be used at the source and never copied.

**Everything at once.** One click each:

| Download | What you get |
|---|---|
| [**all-synthetic-data.zip**](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/all-synthetic-data.zip) | Every synthetic file: all three packs, the practice CRM and the SQLite file |
| [**all-data-catalog.zip**](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/all-data-catalog.zip) | The full catalog: manifest (JSON + CSV), 52 public sources, synthetic index and real paper examples |
| [all-synthetic.jsonl](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/all-synthetic.jsonl) | Every synthetic table row and document in one file, ready for an agent |
| [all-synthetic-combined-csv.zip](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/all-synthetic-combined-csv.zip) | One CSV per table type across the three packs, with `pack` and `product` columns |
| One pack: [oncology](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/synthetic-oncology-mm.zip) · [immunology](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/synthetic-immunology-ad.zip) · [cardiometabolic](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/synthetic-cardiometabolic-obesity.zip) · [practice CRM](https://github.com/Open-Medical-Affairs/Data-Sources/releases/latest/download/synthetic-connected.zip) | A single pack as a ZIP |

Prefer a script? `python3 tools/fetch_all.py` (no installs) downloads all synthetic data, plus small official samples from the public sources whose terms allow it, into `./oma-data`. It skips every LINK ONLY source and prints where to get it. Run `python3 tools/fetch_all.py --list` to see every dataset ID, and `--id <id>` to download just one.

> Everything synthetic stays marked **SYNTHETIC** inside the downloads too: every file keeps its banner, and each ZIP includes `SYNTHETIC-READ-ME-FIRST.txt`.

## New to GitHub? Start here

You don't need to install anything or know GitHub. This page is a link you hand to your AI agent.

![Three steps: 1 copy the repository link, 2 give it to your AI agent, 3 the agent does the job and you review it](assets/how-it-works.jpg)

1. **Copy this page's link** from your browser's address bar:
   `https://github.com/Open-Medical-Affairs/Data-Sources`.
   (Or click the green **Code** button near the top right of this page and copy the link under **HTTPS**.)
2. **Give it to your AI agent.** In Grok Bot, ChatGPT, Claude, Microsoft Copilot or your own agent, start a new conversation and paste:

   ```
   Read https://github.com/Open-Medical-Affairs/Data-Sources and use the synthetic oncology data to summarize what the field team heard this quarter. Mark everything SYNTHETIC and DRAFT.
   ```

   Or, for real public information: *"Read https://github.com/Open-Medical-Affairs/Data-Sources and use its public source list to find the current US label and the EU approval status for semaglutide."*
3. **Let it work, then review.** The agent finds the right files or sources and hands back a draft. **You are the final judge.**

For the step-by-step Medical Affairs know-how, give your agent the companion skills library too:
**[Open-Medical-Affairs/Medical-Affairs-Skills](https://github.com/Open-Medical-Affairs/Medical-Affairs-Skills)**. Event prompts and missions are on the
**[AI in Action website](https://github.com/Open-Medical-Affairs/AI-in-Action-Website)**.

## What's inside

| | What | In plain words | Where |
|---|---|---|---|
| 🧪 | **Synthetic practice data** | A pretend pharma company (Nordvant Biopharma) with three pretend medicines, plus field notes, KOL files, MI enquiries, plans and a practice CRM | [`synthetic/`](synthetic/README.md) |
| 🌐 | **Public data sources** | A guide to 52 real, free sources (PubMed, DailyMed, ClinicalTrials.gov, CMS Open Payments…) grouped by Medical Affairs job | [`public/catalog.md`](public/catalog.md) |
| 📚 | **Real paper examples** | Nine real published papers (titles and DOIs only) for practising evidence searches | [`public/evidence-snapshots/`](public/evidence-snapshots/README.md) |
| 🤖 | **For agents** | Machine-readable lists and instructions | [`AGENTS.md`](AGENTS.md) · [`manifest.json`](manifest.json) · [`synthetic/index.json`](synthetic/index.json) · [`public/catalog.json`](public/catalog.json) |

## Synthetic vs public: what's the difference?

**🧪 SYNTHETIC = a flight simulator.** Everything in [`synthetic/`](synthetic/README.md) is invented so you can practise safely: no real patients, doctors, company or medicine. It behaves like real work, mistakes included, on purpose.

> [!WARNING]
> **Synthetic data is fictional.** Nordvant Biopharma, NORVANTIB, DERMALYX and ADIPOSYN do not exist, and no record describes a real person or patient.
> Never cite it as evidence, never mix it with real data, and never upload real company or patient data here.

| Pack | Pretend product | Disease area |
|---|---|---|
| [Oncology](synthetic/oncology-mm/README.md) | NORVANTIB | Relapsed/refractory multiple myeloma |
| [Immunology](synthetic/immunology-ad/README.md) | DERMALYX | Moderate-to-severe atopic dermatitis |
| [Cardiometabolic](synthetic/cardiometabolic-obesity/README.md) | ADIPOSYN | Obesity |
| [Connected practice CRM](synthetic/connected/README.md) | all three | 90 clinicians, 163 field interactions, 180 MSL tasks |

**🌐 PUBLIC = the real world.** [`public/`](public/catalog.md) points to real, free sources from regulators, registries and journals. We **link** to them; we don't copy their data. Each one is marked:

- ✅ **Open**: free to use with attribution.
- ⚠️ **Check terms**: usable, but read the licence first.
- ⛔ **Link only: do not copy data**: for example IHME disease-burden data, ORCID, NICE outside the UK and Reddit, which restrict commercial use or redistribution.

> [!IMPORTANT]
> Never paste patient information or confidential company data into a public source search.

### Top 15 public sources to start with

| # | Source | Why it matters | Agent can call it directly? |
|---|---|---|---|
| 1 | [DailyMed web services](https://dailymed.nlm.nih.gov/) | Current and historical US labels for any asset or competitor: the backbone for MI responses and launch label readiness. | ✅ Yes |
| 2 | [EMA website data in JSON](https://www.ema.europa.eu/en/medicines/download-medicine-data) | One download covers EU medicines, EPAR documents, PSUSAs, DHPCs, orphans and shortages, so the swarm gets EU launch context. | ✅ Yes |
| 3 | [RxNav APIs](https://lhncbc.nlm.nih.gov/RxNav/) | Normalizes brand and generic names and gives ATC/EPC class, so a competitor landscape builds itself from one drug name. | ✅ Yes |
| 4 | [NPPES NPI Registry API](https://npiregistry.cms.hhs.gov/) | Real US HCP identity and specialty lookups for KOL mapping and field planning. | ✅ Yes |
| 5 | [CMS Open Payments](https://openpaymentsdata.cms.gov/) | Shows industry relationships per HCP, useful for advisory board planning and KOL due diligence. | ✅ Yes |
| 6 | [Medicare Part D Prescribers by Provider and Drug](https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug) | Shows where a therapy class is actually prescribed, by NPI, for field deployment in launch planning. | ✅ Yes |
| 7 | [CMS Medicare Coverage Database](https://www.cms.gov/medicare-coverage-database/) | No-key coverage API covering NCDs and LCDs, the payer/access piece of a launch plan. | ✅ Yes |
| 8 | [WHO ICTRP Search Portal](https://trialsearch.who.int/) | Global trial landscape beyond ClinicalTrials.gov, including ChiCTR and EU registries. | Files / web |
| 9 | [Drugs@FDA data files](https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files) | Approval histories for analog launch timelines (also queryable as openFDA JSON). | Files / web |
| 10 | [bioRxiv / medRxiv API](https://www.medrxiv.org/) | Preprint early warning for competitive intelligence and congress season. | ✅ Yes |
| 11 | [MeSH RDF / Lookup API](https://id.nlm.nih.gov/mesh/) | Gives agents real search vocabulary, which improves every PubMed-based skill. | ✅ Yes |
| 12 | [NIH RePORTER API](https://reporter.nih.gov/) | Funded investigators and projects for KOL discovery and evidence-gap partners. | ✅ Yes |
| 13 | [WHO Global Health Observatory OData API](https://www.who.int/data/gho) | Country-level burden numbers for the 'why this matters' slide of every launch plan. | ✅ Yes |
| 14 | [FDA Patient-Focused Drug Development meeting reports](https://www.fda.gov/industry/prescription-drug-user-fee-amendments/fda-led-patient-focused-drug-development-pfdd-public-meetings) | A ToS-safe patient voice: unmet need, symptoms and impact by condition. | Files / web |
| 15 | [Open Targets Platform](https://platform.opentargets.org/) | The only official MCP server found, with CC0 data. It's a live demo of an agent calling a source directly. | ✅ Yes |

All 52, with access, rate limits, licences and caveats: [`public/catalog.md`](public/catalog.md).

![A Medical Affairs team building with AI agents together](assets/build-team.jpg)

<sub>Illustrations generated for Open Medical Affairs.</sub>

---

# For builders

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
- **Manifest and downloads:** `python3 tools/build_manifest.py` rebuilds `manifest.json` / `manifest.csv`; `python3 tools/build_bundles.py` writes the release assets to `dist/`. The `release-data` workflow rebuilds and republishes them on every push to `main`.

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
├── assets/                    README illustrations
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

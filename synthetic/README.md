<!-- SYNTHETIC DATA — WORKSHOP USE ONLY. Fictional company, products, experts and institutions. -->

# Synthetic workshop data

> **⚠️ SYNTHETIC — fictional data for training/workshops, not real patients/products.**
> Everything in this folder is invented: a fictional company (Nordvant Biopharma), fictional
> products (NORVANTIB, DERMALYX, ADIPOSYN), fictional experts, clinicians and institutions.
> It is written to behave like real Medical Affairs material, flaws included. **Never cite it as
> evidence, never mix it with real data, and never upload real company or patient data here.**

| Folder | Therapeutic area | Fictional product | Files |
|---|---|---|---|
| [`oncology-mm/`](oncology-mm/README.md) | Relapsed/refractory multiple myeloma | NORVANTIB | 31 data files + README |
| [`immunology-ad/`](immunology-ad/README.md) | Moderate-to-severe atopic dermatitis | DERMALYX | 31 data files + README |
| [`cardiometabolic-obesity/`](cardiometabolic-obesity/README.md) | Obesity and weight management | ADIPOSYN | 31 data files + README |
| [`connected/`](connected/README.md) | All three (a practice CRM and content library) | all | 11 CSV tables, a SQLite file, a data dictionary + README |

The three packs share one file schema, so a mission written for one area runs on any of them.
Deliberate flaws are seeded on purpose (adverse events in field notes, a product complaint,
off-label use, contradictions between sources) because finding them is part of the exercise.

## Machine-readable index

[`index.json`](index.json) lists every file with `synthetic: true`, product, therapeutic area,
description, format (rows and columns for CSV), raw and GitHub links, and `used_by`: which
Medical-Affairs-Skills missions, team missions and skills read it.

## Regenerating

Both generators are deterministic and standard-library only. From the repository root:

```bash
python3 synthetic/generate.py          # the three therapeutic-area packs
python3 tools/build_connected.py       # the connected practice organization (CSV + SQLite)
python3 tools/build_index.py --skills-repo ../Medical-Affairs-Skills   # refresh index.json
python3 tools/validate.py
```

[`SKILL-COVERAGE.md`](SKILL-COVERAGE.md) maps each artefact to the skill it exercises.

Moved here from `workshop/data/` in
[Medical-Affairs-Skills](https://github.com/Open-Medical-Affairs/Medical-Affairs-Skills) (October 2026).

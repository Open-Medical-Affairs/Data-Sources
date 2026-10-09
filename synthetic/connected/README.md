# Connected practice organization

SYNTHETIC DATA - fictional training records, not clinical evidence.

> **⚠️ SYNTHETIC — fictional data for training/workshops, not real patients/products.**
> A fictional CRM and content library for Nordvant Biopharma. No real HCP, patient or company.

Use the CSV files directly, or query `medical-affairs.sqlite` with the read-only helper. The SQLite file needs no installation, account, connector or credentials.

The scenario date is **1 October 2026**, not a claim about the real date. HCPs and interactions link to the existing packs. Enquiries retain original requester roles without invented HCP links.

See `data-dictionary.json` for joins, fields and counts; `source_links.csv` for original source hashes. All output remains a synthetic draft. Use local policy to handle real data separately.

From a Medical-Affairs-Skills checkout with this repository cloned into `Data-Sources/`:

```bash
python3 scripts/query_database.py --db Data-Sources/synthetic/connected/medical-affairs.sqlite --schema
python3 scripts/query_database.py --db Data-Sources/synthetic/connected/medical-affairs.sqlite --sql "SELECT h.country, COUNT(*) AS interactions FROM interactions i JOIN hcps h ON h.hcp_id=i.hcp_id GROUP BY h.country"
```

Without the skills repo, any SQLite client works: `sqlite3 synthetic/connected/medical-affairs.sqlite .tables`.

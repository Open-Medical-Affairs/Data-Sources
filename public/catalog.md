# Public data sources for Medical Affairs agents

> **REAL PUBLIC SOURCES — NOT SYNTHETIC.** Check each source's terms before copying or redistributing data. Never send PHI or confidential company data in a query. Retrieval does not verify a scientific claim.

**52 sources** in **11 Medical Affairs job groups**, checked 2026-10-08. Machine-readable twin: [`catalog.json`](catalog.json). This repository **links** to these sources; it does not mirror their data.

**Data policy:** `open`: Public data, free to query and cite with attribution. · `check-terms`: Usable, but read the stated licence or terms first (share-alike, attribution, unreviewed terms, partial licences). · `link-only`: LINK ONLY: do not copy data into repositories, decks or shared files. Commercial, redistribution or licence restrictions apply.

**Verification:** `verified-live`: A real API/download call from our box returned data on the check date, and docs/terms were read where available. · `verified-docs`: The official docs/terms page was fetched and read; no API call (or no API exists). · `partially-verified`: Some facts verified; anything not verified is marked UNVERIFIED in the field. · `unverified`: Seen in search results only; not fetched or tested.

**Already used by the skills** (Medical-Affairs-Skills `scripts/public_evidence.py`): PubMed / NCBI E-utilities, Europe PMC REST API, Crossref REST API, OpenAlex, ClinicalTrials.gov API v2, openFDA (labels, FAERS, recalls, Drugs@FDA, NDC, shortages).

## Top 15: add first

Ranked for the launch-planning swarm and the hackathon missions.

| # | Source | Why first | Access | Agent-ready | Policy | Verified |
|---|---|---|---|---|---|---|
| 1 | [DailyMed web services (NLM)](https://dailymed.nlm.nih.gov/) | Current and historical US labels for any asset or competitor: the backbone for MI responses and launch label readiness. | Open API, no key; bulk ZIPs via HTTPS/FTP | JSON API | Open | verified-live |
| 2 | [EMA website data in JSON (medicines, EPAR documents, PSUSAs, DHPCs, orphans, PIPs, shortages, guidelines)](https://www.ema.europa.eu/en/medicines/download-medicine-data) | One download covers EU medicines, EPAR documents, PSUSAs, DHPCs, orphans and shortages, so the swarm gets EU launch context. | Open bulk JSON files, no key | JSON API | Check terms | verified-live |
| 3 | [RxNav APIs (RxNorm, RxClass, RxTerms)](https://lhncbc.nlm.nih.gov/RxNav/) | Normalizes brand and generic names and gives ATC/EPC class, so a competitor landscape builds itself from one drug name. | Open API, no key (UMLS key optional for higher tier) | JSON API | Check terms | verified-live |
| 4 | [NPPES NPI Registry API](https://npiregistry.cms.hhs.gov/) | Real US HCP identity and specialty lookups for KOL mapping and field planning. | Open read API v2.1, no key; full CSV dissemination file | JSON API | Open | verified-live |
| 5 | [CMS Open Payments](https://openpaymentsdata.cms.gov/) | Shows industry relationships per HCP, useful for advisory board planning and KOL due diligence. | Open API (DKAN metastore/datastore, SQL query) + bulk downloads | JSON API | Open | partially-verified |
| 6 | [Medicare Part D Prescribers by Provider and Drug](https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug) | Shows where a therapy class is actually prescribed, by NPI, for field deployment in launch planning. | Open data-api v1 + CSV, no key | JSON API | Open | verified-live |
| 7 | [CMS Medicare Coverage Database (Coverage API + downloads)](https://www.cms.gov/medicare-coverage-database/) | No-key coverage API covering NCDs and LCDs, the payer/access piece of a launch plan. | Open API, no key since 8 Feb 2024 | JSON API | Check terms | verified-live |
| 8 | [WHO ICTRP Search Portal](https://trialsearch.who.int/) | Global trial landscape beyond ClinicalTrials.gov, including ChiCTR and EU registries. | Web portal; CSV/XML download from the portal; crawling service listed | Files/web | Check terms | verified-docs |
| 9 | [Drugs@FDA data files](https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files) | Approval histories for analog launch timelines (also queryable as openFDA JSON). | Bulk ZIP, updated each weekday morning | Files/web | Open | verified-docs |
| 10 | [bioRxiv / medRxiv API](https://www.medrxiv.org/) | Preprint early warning for competitive intelligence and congress season. | Open API, no key | JSON API | Check terms | verified-live |
| 11 | [MeSH RDF / Lookup API](https://id.nlm.nih.gov/mesh/) | Gives agents real search vocabulary, which improves every PubMed-based skill. | Open API, no key | JSON API | Open | verified-live |
| 12 | [NIH RePORTER API](https://reporter.nih.gov/) | Funded investigators and projects for KOL discovery and evidence-gap partners. | Open API, no key | JSON API | Open | verified-live |
| 13 | [WHO Global Health Observatory OData API](https://www.who.int/data/gho) | Country-level burden numbers for the 'why this matters' slide of every launch plan. | Open API, no key | JSON API | Check terms | verified-live |
| 14 | [FDA Patient-Focused Drug Development meeting reports (FDA-led and externally-led)](https://www.fda.gov/industry/prescription-drug-user-fee-amendments/fda-led-patient-focused-drug-development-pfdd-public-meetings) | A ToS-safe patient voice: unmet need, symptoms and impact by condition. | Web/PDF | Files/web | Open | verified-docs |
| 15 | [Open Targets Platform (GraphQL + official MCP)](https://platform.opentargets.org/) | The only official MCP server found, with CC0 data. It's a live demo of an agent calling a source directly. | Open GraphQL, BigQuery, downloads | JSON API; MCP | Open | verified-live |

## Link only: do not copy data

Point agents and people to these sources, but never copy their data into a repository, deck or shared file.

- **[ORCID Public API](https://orcid.org/)**: Public API terms bar use in revenue-generating products or services; pharma use may need ORCID membership.
- **[WHO VigiAccess (VigiBase public view)](https://www.vigiaccess.org/)**: No API; UMC disclaimer forbids scraping and causality/incidence use.
- **[NICE guidance & technology appraisals (syndication API)](https://www.nice.org.uk/guidance)**: NICE content is free for UK use only; international use needs a paid licence.
- **[USPSTF Prevention TaskForce API](https://www.uspreventiveservicestaskforce.org/)**: AHRQ copyright notice; permission needed before automated agent use.
- **[ICER assessments](https://icer.org/explore-our-research/assessments/)**: Report reuse terms not verified.
- **[Guidelines International Network library](https://g-i-n.net/international-guidelines-library)**: Copyright GIN; a directory, not an open data feed.
- **[SEER (NCI) — Explorer, research data, SEER API](https://seer.cancer.gov/)**: SEER data use agreement and API key required.
- **[IHME Global Burden of Disease (GBD Results)](https://vizhub.healthdata.org/gbd-results/)**: Non-commercial user agreement; no redistribution of data sets (links allowed).
- **[WHO ICD-11 API](https://icd.who.int/)**: CC BY-ND 3.0 IGO: no redistribution of modified classification content.
- **[UMLS Metathesaurus (incl. SNOMED CT US, MedDRA via license)](https://www.nlm.nih.gov/research/umls/index.html)**: Personal UMLS license; SNOMED CT and some vocabularies need extra agreements.
- **[Reddit Data API (patient communities)](https://www.reddit.com/dev/api/)**: Commercial use and AI training on user content need a separate agreement; monitored social data may trigger AE reporting.

## Literature & evidence

_Evidence gaps, surveillance, publications, MI_

### PubMed / NCBI E-utilities · _already used by the skills_

- **URL:** https://pubmed.ncbi.nlm.nih.gov/  
- **API docs:** https://www.ncbi.nlm.nih.gov/books/NBK25497/  
- **Contents:** 35M+ biomedical citations and abstracts with MeSH indexing; search, summary, fetch, link endpoints.  
- **Medical Affairs jobs:** evidence gaps, literature surveillance, MI responses, publications  
- **Skills:** `pubmed-search`, `literature-surveillance`, `systematic-literature-review`, `citation-integrity`  
- **Access:** Open API, no key at basic limits; free NCBI key optional  
- **Rate limit:** 3 requests/second per IP without a key; 10/second with a free key (NCBI Insights post)  
- **License:** NLM data; abstracts may carry publisher copyright  
- **Data policy:** Check terms — Abstracts may carry publisher copyright.  
- **Agent readiness:** JSON API; JSON, XML; MCP: Community MCP servers exist (e.g., pubspro/pharma-mcp, nickjlamb/pubcrawl), unvetted  
- **Caveats:** Bibliographic metadata only; full text needs PMC OA/BioC. NBK25497 docs page blocks automated fetch; limits taken from NCBI Insights.  
- **Verification:** `verified-live` on 2026-10-08. esearch returned JSON; rate limits from ncbiinsights.ncbi.nlm.nih.gov 'New API Keys for the E-utilities'.

### PMC Open Access Subset

- **URL:** https://pmc.ncbi.nlm.nih.gov/tools/openftlist/  
- **API docs:** https://pmc.ncbi.nlm.nih.gov/tools/openftlist/  
- **Contents:** Full-text articles and preprints under Creative Commons or similar reuse licenses.  
- **Medical Affairs jobs:** evidence synthesis, MI responses, publications  
- **Skills:** `evidence-synthesis`, `evidence-appraisal`, `medical-information-response`  
- **Access:** Open; retrieval only via Cloud Service (AWS), OAI-PMH, E-utilities or BioC API  
- **Rate limit:** Uses E-utilities limits when accessed that way  
- **License:** Varies per article (check each article's license statement)  
- **Data policy:** Check terms — Bulk retrieval only via the sanctioned services; licence varies per article.  
- **Agent readiness:** JSON API; XML, JSON (BioC), bulk on AWS; MCP: No official MCP server found  
- **Caveats:** PMC states systematic/bulk retrieval via any other automated process is prohibited. License differs per article.  
- **Verification:** `verified-docs` on 2026-10-08. Terms fetched from the openftlist page.

### Europe PMC REST API · _already used by the skills_

- **URL:** https://europepmc.org/  
- **API docs:** https://europepmc.org/RestfulWebService  
- **Contents:** Literature incl. PubMed, PMC, preprints (bioRxiv/medRxiv), patents, grants; open-access filtering.  
- **Medical Affairs jobs:** evidence gaps, literature surveillance, congress/preprint tracking  
- **Skills:** `public-evidence-search`, `literature-surveillance`  
- **Access:** Open API, no key  
- **Rate limit:** Not stated on pages fetched  
- **License:** EMBL-EBI Terms of Use; article licenses vary (CC-BY/CC-BY-NC/CC0 or open access per Open Targets licence table)  
- **Data policy:** Check terms — Article licences vary.  
- **Agent readiness:** JSON API; JSON, XML; MCP: No official MCP server found  
- **Caveats:** europepmc.org docs page returned 403 to our fetcher; API itself answered.  
- **Verification:** `verified-live` on 2026-10-08. search endpoint returned JSON (hitCount 219,667 for 'myeloma'); EMBL-EBI terms page fetched.

### Crossref REST API · _already used by the skills_

- **URL:** https://www.crossref.org/  
- **API docs:** https://www.crossref.org/documentation/retrieve-metadata/rest-api/  
- **Contents:** DOI metadata from publishers: funding, licenses, ORCID/ROR IDs, post-publication updates (retractions/corrections), some abstracts.  
- **Medical Affairs jobs:** citation integrity, publications  
- **Skills:** `citation-integrity`, `scientific-manuscript`  
- **Access:** Open API, no sign-up  
- **Rate limit:** Not stated in excerpt fetched  
- **License:** 'Almost none of the metadata is subject to copyright… use it for any purpose'; some abstracts may be copyrighted  
- **Data policy:** Check terms — Some abstracts may be copyrighted.  
- **Agent readiness:** JSON API; JSON; MCP: No official MCP server found  
- **Caveats:** Abstracts may be copyrighted by publishers.  
- **Verification:** `verified-live` on 2026-10-08. works query returned JSON; docs fetched.

### OpenAlex · _already used by the skills_

- **URL:** https://openalex.org/  
- **API docs:** https://docs.openalex.org/how-to-use-the-api/rate-limits-and-authentication  
- **Contents:** Open index of works, authors, institutions, topics and citations; full dataset downloadable.  
- **Medical Affairs jobs:** KOL mapping (publication networks), publications, evidence gaps  
- **Skills:** `kol-engagement-brief`, `citation-integrity`, `competitive-intelligence`  
- **Access:** Free; keyless basic use; free key gives 10x daily budget; paid plans above that  
- **Rate limit:** Usage-budgeted: free account key = $1/day of usage; 429 when exceeded  
- **License:** Data free; full dataset openly downloadable (per pricing page)  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON, bulk snapshot; MCP: No official MCP server found  
- **Caveats:** Moved to a usage-priced model; keep agents within the free budget.  
- **Verification:** `verified-live` on 2026-10-08. works search returned JSON; auth and pricing pages fetched.

### Semantic Scholar Academic Graph API

- **URL:** https://www.semanticscholar.org/product/api  
- **API docs:** https://api.semanticscholar.org/api-docs/  
- **Contents:** 214M papers, 2.49B citations, 79M authors; recommendations; downloadable datasets.  
- **Medical Affairs jobs:** evidence gaps, KOL mapping, publications  
- **Skills:** `literature-surveillance`, `kol-engagement-brief`  
- **Access:** Most endpoints public without key (shared pool); free key by request  
- **Rate limit:** Unauthenticated: 1000 req/s shared among all unauthenticated users; key: introductory 1 RPS  
- **License:** See API license agreement (not reviewed)  
- **Data policy:** Check terms — API license agreement not reviewed.  
- **Agent readiness:** JSON API; JSON, bulk datasets; MCP: No official MCP server found  
- **Caveats:** Shared keyless pool is often throttled: our test call got HTTP 429. Request a key for workshop use.  
- **Verification:** `partially-verified` on 2026-10-08. Product page fetched; live call returned 429 Too Many Requests.

### bioRxiv / medRxiv API · **#10 in top 15**

- **URL:** https://www.medrxiv.org/  
- **API docs:** https://api.biorxiv.org/  
- **Contents:** Preprint metadata (title, authors, abstract, license, category, JATS XML path, published DOI), publication linkage, usage stats.  
- **Medical Affairs jobs:** literature surveillance, competitive intelligence, congress-adjacent early evidence  
- **Skills:** `literature-surveillance`, `competitive-intelligence`, `congress-intelligence`  
- **Access:** Open API, no key  
- **Rate limit:** Not stated  
- **License:** Per-preprint license field returned  
- **Data policy:** Check terms — Per-preprint license.  
- **Agent readiness:** JSON API; JSON, CSV, OAI-PMH XML; MCP: No official MCP server found  
- **Caveats:** Preprints are not peer reviewed; label them clearly in outputs.  
- **Verification:** `verified-live` on 2026-10-08. details endpoint returned JSON for 2025-01-01..02 medRxiv.

### NIH RePORTER API · **#12 in top 15**

- **URL:** https://reporter.nih.gov/  
- **API docs:** https://api.reporter.nih.gov/  
- **Contents:** NIH-funded projects and publications: PIs, institutions, abstracts, funding amounts.  
- **Medical Affairs jobs:** KOL mapping, evidence gaps, IIS landscape  
- **Skills:** `kol-engagement-brief`, `evidence-gap-analysis`, `investigator-initiated-study-review`  
- **Access:** Open API, no key  
- **Rate limit:** Recommend max 1 request/second; large jobs on weekends or 9 PM–5 AM ET weekdays  
- **License:** US government data (license not stated in excerpt)  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON; MCP: No official MCP server found  
- **Caveats:** Heavy use outside guidance may be blocked.  
- **Verification:** `verified-live` on 2026-10-08. v2/projects/search POST returned JSON (2,983,191 total); docs fetched.

### ORCID Public API · **LINK ONLY: do not copy data**

- **URL:** https://orcid.org/  
- **API docs:** https://info.orcid.org/documentation/features/public-api/  
- **Contents:** Researcher identifiers with public works, affiliations and funding.  
- **Medical Affairs jobs:** KOL mapping (disambiguation)  
- **Skills:** `kol-engagement-brief`, `hcp-discovery-and-access`  
- **Access:** Anonymous + Public API; Public API credentials need an individual ORCID iD  
- **Rate limit:** Not stated in excerpt  
- **License:** Limited license to 'public' registry data  
- **Data policy:** **LINK ONLY: do not copy data** — Public API terms bar use in revenue-generating products or services; pharma use may need ORCID membership.  
- **Agent readiness:** JSON API; XML, JSON; MCP: No official MCP server found  
- **Caveats:** Public API Terms: may NOT be used in connection with any revenue-generating product or service. Pharma use may need ORCID member API — check before production.  
- **Verification:** `partially-verified` on 2026-10-08. Search call returned XML; Public APIs Terms of Service fetched.

## Clinical trials

_Competitive intelligence, launch planning, site/landscape_

### ClinicalTrials.gov API v2 · _already used by the skills_

- **URL:** https://clinicaltrials.gov/  
- **API docs:** https://clinicaltrials.gov/data-api/api  
- **Contents:** 400k+ registered studies: design, arms, eligibility, outcomes, sites, sponsors, results.  
- **Medical Affairs jobs:** competitive intelligence, launch planning, evidence gaps, MSL site support  
- **Skills:** `clinical-trials-search`, `competitive-intelligence`, `medical-launch-plan`, `evidence-gap-analysis`  
- **Access:** Open API, no key  
- **Rate limit:** No official number found; ~50 req/min per IP is community-reported (UNVERIFIED). Back off on 429.  
- **License:** Terms page is JS-rendered and could not be read (UNVERIFIED)  
- **Data policy:** Check terms — Terms page could not be read (UNVERIFIED).  
- **Agent readiness:** JSON API; JSON, CSV; MCP: Community MCP servers exist (pharma-mcp, helix-mcp, @drvibeai/clinical-apis-mcp), unvetted  
- **Caveats:** US registry; not global coverage. OpenAPI spec at /api/oas/v2.  
- **Verification:** `verified-live` on 2026-10-08. /api/v2/version returned apiVersion 2.0.5, dataTimestamp 2026-10-08; studies query returned JSON.

### WHO ICTRP Search Portal · **#8 in top 15**

- **URL:** https://trialsearch.who.int/  
- **API docs:** https://www.who.int/tools/clinical-trials-registry-platform/network/who-data-set/downloading-records-from-the-ictrp-database  
- **Contents:** Trials from WHO primary registries worldwide (ChiCTR, EU, ISRCTN, CTRI, etc.).  
- **Medical Affairs jobs:** competitive intelligence, global trial landscape  
- **Skills:** `clinical-trials-search`, `competitive-intelligence`  
- **Access:** Web portal; CSV/XML download from the portal; crawling service listed  
- **Rate limit:** Not stated  
- **License:** WHO ICTRP Terms and Conditions accepted on download  
- **Data policy:** Check terms — WHO ICTRP terms accepted on download; do not scrape the portal.  
- **Agent readiness:** no JSON API; CSV, XML; MCP: No official MCP server found  
- **Caveats:** No documented open JSON API; agents should use downloads, not scrape the portal.  
- **Verification:** `verified-docs` on 2026-10-08. Portal loads; download page and T&C fetched.

### EU Clinical Trials Information System (CTIS) public portal

- **URL:** https://euclinicaltrials.eu/  
- **API docs:** https://www.ema.europa.eu/en/human-regulatory-overview/research-development/clinical-trials-human-medicines/clinical-trials-information-system  
- **Contents:** EU/EEA trials under the Clinical Trials Regulation (from 31 Jan 2023); older trials in the EU Clinical Trials Register.  
- **Medical Affairs jobs:** competitive intelligence, EU launch planning  
- **Skills:** `clinical-trials-search`, `competitive-intelligence`  
- **Access:** Public web search  
- **Rate limit:** Not stated  
- **License:** Public under CTR, with exemptions (e.g., personal data)  
- **Data policy:** Check terms — Personal data exempt from publication.  
- **Agent readiness:** no JSON API; HTML; MCP: No official MCP server found  
- **Caveats:** No documented public API found (UNVERIFIED); treat as human-browse or ICTRP feed.  
- **Verification:** `verified-docs` on 2026-10-08. EMA CTIS page and public portal loaded.

### ISRCTN registry

- **URL:** https://www.isrctn.com/  
- **API docs:** https://www.isrctn.com/  
- **Contents:** UK-centric registry of trials and other studies.  
- **Medical Affairs jobs:** competitive intelligence  
- **Skills:** `clinical-trials-search`  
- **Access:** Query endpoint answered without key  
- **Rate limit:** Not stated  
- **License:** UNVERIFIED (API docs page returned 404)  
- **Data policy:** Check terms — Terms unverified.  
- **Agent readiness:** no JSON API; XML; MCP: No official MCP server found  
- **Caveats:** API documentation URL tried returned 404; confirm terms before use.  
- **Verification:** `partially-verified` on 2026-10-08. /api/query/format/default returned XML (122 myeloma trials).

## Regulatory, labels & approvals

_Label intelligence, MI responses, launch analogs, MLR_

### openFDA (labels, FAERS, recalls, Drugs@FDA, NDC, shortages) · _already used by the skills_

- **URL:** https://open.fda.gov/  
- **API docs:** https://open.fda.gov/apis/  
- **Contents:** drug/label (SPL sections), drug/event (FAERS), drug/enforcement (recalls), drug/drugsfda (approval history), drug/ndc, drug/shortages.  
- **Medical Affairs jobs:** MI responses, safety, label intelligence, launch planning (analogs), competitive intelligence  
- **Skills:** `regulatory-label-intelligence`, `medical-information-response`, `safety-communication`, `competitive-intelligence`  
- **Access:** Open API; free key raises daily cap  
- **Rate limit:** No key: 240/min and 1,000/day per IP. Key: 240/min and 120,000/day per key.  
- **License:** CC0 1.0 unless noted (GMDN device terms excluded; no AI training on GMDN content without license)  
- **Data policy:** Check terms — GMDN device terms excluded from CC0; no AI training on GMDN content.  
- **Agent readiness:** JSON API; JSON; MCP: Community MCP servers exist (pharma-mcp, clinical-apis-mcp), unvetted  
- **Caveats:** FAERS counts are reports, not incidence or causality. Auth page says a key is required but lists no-key limits.  
- **Verification:** `verified-live` on 2026-10-08. label, event (count), enforcement, drugsfda, ndc, shortages endpoints all returned JSON; auth, terms, license pages fetched.

### DailyMed web services (NLM) · **#1 in top 15**

- **URL:** https://dailymed.nlm.nih.gov/  
- **API docs:** https://dailymed.nlm.nih.gov/dailymed/app-support-web-services.cfm  
- **Contents:** Current and archived SPL labels (Rx, OTC), set IDs, version history, PDFs/ZIPs; full bulk label downloads (daily/weekly/monthly).  
- **Medical Affairs jobs:** MI responses, label intelligence, MLR review, launch planning  
- **Skills:** `regulatory-label-intelligence`, `medical-information-response`, `promotional-material-medical-review`  
- **Access:** Open API, no key; bulk ZIPs via HTTPS/FTP  
- **Rate limit:** Not stated  
- **License:** NLM/FDA label content (license not stated in excerpt)  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON, XML, PDF, ZIP; MCP: No official MCP server found  
- **Caveats:** Bulk Rx label parts are ~3 GB each.  
- **Verification:** `verified-live` on 2026-10-08. spls.json?drug_name=semaglutide returned Aug 19 2026 label; services and bulk pages fetched.

### Drugs@FDA data files · **#9 in top 15**

- **URL:** https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files  
- **API docs:** https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files  
- **Contents:** 12 tables: applications, products, submissions, marketing status, approval documents.  
- **Medical Affairs jobs:** launch planning (analog timelines), competitive intelligence  
- **Skills:** `launch-timeline-and-governance`, `competitive-intelligence`  
- **Access:** Bulk ZIP, updated each weekday morning  
- **Rate limit:** n/a  
- **License:** US government data  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** no JSON API; TXT tables (ZIP); MCP: No official MCP server found  
- **Caveats:** Same data is queryable as JSON via openFDA drug/drugsfda.  
- **Verification:** `verified-docs` on 2026-10-08. Page fetched; 'Data Last Updated: October 7th, 2026'.

### FDA Orange Book data files

- **URL:** https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files  
- **API docs:** https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files  
- **Contents:** Approved small-molecule products, therapeutic equivalence, patents and exclusivity (3 ASCII files).  
- **Medical Affairs jobs:** launch planning (LOE/competitor timing), competitive intelligence  
- **Skills:** `competitive-intelligence`, `medical-launch-plan`  
- **Access:** Bulk ZIP  
- **Rate limit:** n/a  
- **License:** US government data  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** no JSON API; ASCII (ZIP); MCP: No official MCP server found  
- **Caveats:** Small molecules only; biologics are in the Purple Book.  
- **Verification:** `verified-docs` on 2026-10-08. Data files page fetched.

### FDA Purple Book (licensed biologics)

- **URL:** https://purplebooksearch.fda.gov/  
- **API docs:** https://purplebooksearch.fda.gov/downloads  
- **Contents:** Licensed biological products, biosimilarity/interchangeability, exclusivity; patent list.  
- **Medical Affairs jobs:** launch planning (biosimilar threat), competitive intelligence  
- **Skills:** `competitive-intelligence`, `medical-launch-plan`  
- **Access:** Monthly CSV/XLSX downloads  
- **Rate limit:** n/a  
- **License:** US government data  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** no JSON API; CSV, XLSX; MCP: No official MCP server found  
- **Caveats:** Monthly snapshots (Sept 2026 latest listed).  
- **Verification:** `verified-docs` on 2026-10-08. Downloads page fetched with monthly files through September 2026.

### FDA Novel Drug Approvals 2026 (CDER)

- **URL:** https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2026  
- **API docs:** https://www.fda.gov/drugs/novel-drug-approvals-fda/novel-drug-approvals-2026  
- **Contents:** List of 2026 novel approvals with indications.  
- **Medical Affairs jobs:** competitive intelligence, launch planning  
- **Skills:** `competitive-intelligence`  
- **Access:** Web page  
- **Rate limit:** n/a  
- **License:** US government  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** no JSON API; HTML; MCP: No official MCP server found  
- **Caveats:** Link, don't scrape; cross-check with openFDA drugsfda.  
- **Verification:** `verified-docs` on 2026-10-08. Page loaded.

### FDA Drug Trials Snapshots

- **URL:** https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trials-snapshots  
- **API docs:** https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trials-snapshots  
- **Contents:** Per-approval demographics of pivotal-trial participants; annual summary reports (2025 PDF).  
- **Medical Affairs jobs:** evidence gaps (diversity), MI responses  
- **Skills:** `evidence-gap-analysis`, `medical-information-response`  
- **Access:** Web/PDF  
- **Rate limit:** n/a  
- **License:** US government  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** no JSON API; HTML, PDF; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-docs` on 2026-10-08. Page fetched.

### FDA guidance documents search

- **URL:** https://www.fda.gov/regulatory-information/search-fda-guidance-documents  
- **API docs:** https://www.fda.gov/regulatory-information/search-fda-guidance-documents  
- **Contents:** All FDA guidance with topic filters incl. RWD/RWE.  
- **Medical Affairs jobs:** RWE design, MLR, medical communications  
- **Skills:** `real-world-evidence-design`, `mlr-review-readiness`, `scientific-communication-strategy`  
- **Access:** Web search  
- **Rate limit:** n/a  
- **License:** US government  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** no JSON API; HTML, PDF; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-docs` on 2026-10-08. Page fetched.

### EMA website data in JSON (medicines, EPAR documents, PSUSAs, DHPCs, orphans, PIPs, shortages, guidelines) · **#2 in top 15**

- **URL:** https://www.ema.europa.eu/en/medicines/download-medicine-data  
- **API docs:** https://www.ema.europa.eu/en/about-us/about-website/download-website-data-json-data-format  
- **Contents:** Centrally authorised medicines (2,746 records on test), EPAR documents, post-authorisation procedures, referrals, PSUSAs, DHPCs, orphan designations, PIPs, shortages, scientific guidelines; updated overnight.  
- **Medical Affairs jobs:** EU label intelligence, safety, launch planning (EU), competitive intelligence  
- **Skills:** `regulatory-label-intelligence`, `safety-communication`, `competitive-intelligence`, `medical-launch-plan`  
- **Access:** Open bulk JSON files, no key  
- **Rate limit:** n/a  
- **License:** EMA website terms (not reviewed)  
- **Data policy:** Check terms — EMA website terms not reviewed.  
- **Agent readiness:** JSON API; JSON, XLSX; MCP: No official MCP server found  
- **Caveats:** Whole-file downloads (medicines file ~6.8 MB); filter locally.  
- **Verification:** `verified-live` on 2026-10-08. medicines-output-medicines_json-report_en.json downloaded (total_records 2746, timestamp 2026-10-08).

### MedlinePlus Connect

- **URL:** https://medlineplus.gov/connect/overview.html  
- **API docs:** https://medlineplus.gov/connect/technical.html  
- **Contents:** Patient-friendly health topic and drug information keyed by ICD-10-CM, RxCUI, NDC, LOINC.  
- **Medical Affairs jobs:** plain-language summaries, patient engagement, MI (lay responses)  
- **Skills:** `plain-language-summary`, `patient-engagement-planning`  
- **Access:** Open API, no key  
- **Rate limit:** Max 100 requests/minute per IP; over-limit blocked for 300 s  
- **License:** MedlinePlus terms (not reviewed)  
- **Data policy:** Check terms — MedlinePlus terms not reviewed.  
- **Agent readiness:** JSON API; JSON, XML; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-live` on 2026-10-08. ICD-10 E66.9 query returned JSON feed; technical page fetched.

## Safety

_Global ADR context_

### WHO VigiAccess (VigiBase public view) · **LINK ONLY: do not copy data**

- **URL:** https://www.vigiaccess.org/  
- **API docs:** https://www.vigiaccess.org/  
- **Contents:** Counts of reported suspected ADRs by active ingredient, grouped by continent, age, sex.  
- **Medical Affairs jobs:** safety (global signal context), MI responses  
- **Skills:** `safety-communication`, `medical-information-response`  
- **Access:** Web, after accepting disclaimer  
- **Rate limit:** n/a  
- **License:** UMC disclaimer; no individual case reports  
- **Data policy:** **LINK ONLY: do not copy data** — No API; UMC disclaimer forbids scraping and causality/incidence use.  
- **Agent readiness:** no JSON API; HTML; MCP: No official MCP server found  
- **Caveats:** No API; not for causality, incidence or product comparisons (stated by UMC). Do not scrape.  
- **Verification:** `verified-docs` on 2026-10-08. FAQ/disclaimer fetched.

## Payer, HTA, coverage & guidelines

_Access, value story, guideline engagement_

### NICE guidance & technology appraisals (syndication API) · **LINK ONLY: do not copy data**

- **URL:** https://www.nice.org.uk/guidance  
- **API docs:** https://www.nice.org.uk/about/what-we-do/nice-syndication-api  
- **Contents:** UK clinical guidelines and technology appraisals.  
- **Medical Affairs jobs:** payer/HTA, guideline engagement  
- **Skills:** `payer-value-dossier`, `guideline-engagement`  
- **Access:** Web free; API needs an approved licence and key  
- **Rate limit:** n/a  
- **License:** UK use free (NICE UK Open Content Licence); international test licence £550, worldwide service licence £60,000/yr  
- **Data policy:** **LINK ONLY: do not copy data** — NICE content is free for UK use only; international use needs a paid licence.  
- **Agent readiness:** JSON API; HTML, JSON (API); MCP: No official MCP server found  
- **Caveats:** NICE FAQ has a specific section on using AI with NICE content; read it before agent use. Guidance listing returned 403 to our probe.  
- **Verification:** `verified-docs` on 2026-10-08. Syndication API and reusing-content pages fetched.

### USPSTF Prevention TaskForce API · **LINK ONLY: do not copy data**

- **URL:** https://www.uspreventiveservicestaskforce.org/  
- **API docs:** https://www.uspreventiveservicestaskforce.org/apps/api.jsp  
- **Contents:** US preventive services recommendations.  
- **Medical Affairs jobs:** guideline engagement  
- **Skills:** `guideline-engagement`  
- **Access:** API requires prior approval (request form)  
- **Rate limit:** n/a  
- **License:** AHRQ copyright notice  
- **Data policy:** **LINK ONLY: do not copy data** — AHRQ copyright notice; permission needed before automated agent use.  
- **Agent readiness:** JSON API; JSON; MCP: No official MCP server found  
- **Caveats:** Approval needed before agents can call it.  
- **Verification:** `verified-docs` on 2026-10-08. API page fetched.

### CMS Medicare Coverage Database (Coverage API + downloads) · **#7 in top 15**

- **URL:** https://www.cms.gov/medicare-coverage-database/  
- **API docs:** https://api.coverage.cms.gov/  
- **Contents:** National Coverage Determinations, Local Coverage Determinations, articles; full ZIP downloads.  
- **Medical Affairs jobs:** payer/access, launch planning (coverage)  
- **Skills:** `payer-value-dossier`, `medical-launch-plan`  
- **Access:** Open API, no key since 8 Feb 2024  
- **Rate limit:** Throttle 10,000 requests/second  
- **License:** Some endpoints need a 1-hour token after accepting AMA CPT / ADA / AHA license agreements  
- **Data policy:** Check terms — Some endpoints need AMA CPT / ADA / AHA license acceptance; CPT content is AMA-licensed.  
- **Agent readiness:** JSON API; JSON, CSV/MDB ZIP; MCP: No official MCP server found  
- **Caveats:** CPT content is AMA-licensed.  
- **Verification:** `verified-live` on 2026-10-08. national-coverage-ncd report returned JSON; FAQ and downloads pages fetched.

### ICER assessments · **LINK ONLY: do not copy data**

- **URL:** https://icer.org/explore-our-research/assessments/  
- **API docs:** https://icer.org/explore-our-research/assessments/  
- **Contents:** US cost-effectiveness and value assessments by condition.  
- **Medical Affairs jobs:** payer/HTA, launch planning (value story)  
- **Skills:** `payer-value-dossier`  
- **Access:** Web  
- **Rate limit:** n/a  
- **License:** UNVERIFIED (report download terms not checked)  
- **Data policy:** **LINK ONLY: do not copy data** — Report reuse terms not verified.  
- **Agent readiness:** no JSON API; HTML, PDF; MCP: No official MCP server found  
- **Caveats:** No API. Report reuse terms unverified.  
- **Verification:** `partially-verified` on 2026-10-08. Assessments page loaded (upcoming: Friedreich's Ataxia Jan 2027, Huntington's Mar 2027).

### Guidelines International Network library · **LINK ONLY: do not copy data**

- **URL:** https://g-i-n.net/international-guidelines-library  
- **API docs:** https://g-i-n.net/international-guidelines-library  
- **Contents:** Library of guidelines and links to national guideline repositories (AWMF, BIGG, USPSTF, etc.).  
- **Medical Affairs jobs:** guideline engagement  
- **Skills:** `guideline-engagement`  
- **Access:** Web; some features for members  
- **Rate limit:** n/a  
- **License:** © GIN  
- **Data policy:** **LINK ONLY: do not copy data** — Copyright GIN; a directory, not an open data feed.  
- **Agent readiness:** no JSON API; HTML; MCP: No official MCP server found  
- **Caveats:** Directory, not data feed.  
- **Verification:** `verified-docs` on 2026-10-08. Page fetched.

### Medicare Part D Spending by Drug (annual + quarterly)

- **URL:** https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-d-spending-by-drug  
- **API docs:** https://data.cms.gov/api-docs  
- **Contents:** Spending, claims, beneficiaries, unit cost by brand/generic and manufacturer.  
- **Medical Affairs jobs:** payer/access, launch planning (market context)  
- **Skills:** `payer-value-dossier`, `strategic-analysis`  
- **Access:** Open data-api v1 + CSV  
- **Rate limit:** Not stated  
- **License:** Public CMS data  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON, CSV; MCP: No official MCP server found  
- **Caveats:** Gross spend, pre-rebate.  
- **Verification:** `verified-live` on 2026-10-08. Dataset listed in data.cms.gov DCAT catalog; API returned rows.

## HCPs & transparency

_KOL mapping, field planning, advisory boards_

### NPPES NPI Registry API · **#4 in top 15**

- **URL:** https://npiregistry.cms.hhs.gov/  
- **API docs:** https://npiregistry.cms.hhs.gov/api-page  
- **Contents:** Every US provider NPI: name, taxonomy/specialty, practice addresses, identifiers.  
- **Medical Affairs jobs:** KOL mapping, HCP discovery, field planning  
- **Skills:** `hcp-discovery-and-access`, `field-medical-planning`, `msl-pre-call-planning`  
- **Access:** Open read API v2.1, no key; full CSV dissemination file  
- **Rate limit:** Max 200 results/request; skip up to 1,000 (1,200 records per query)  
- **License:** Public CMS data  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON, CSV; MCP: No official MCP server found  
- **Caveats:** NPI does not validate licensure. Business contact data only; no PHI.  
- **Verification:** `verified-live` on 2026-10-08. Hematology/PA query returned JSON; API page fetched.

### CMS Open Payments · **#5 in top 15**

- **URL:** https://openpaymentsdata.cms.gov/  
- **API docs:** https://openpaymentsdata.cms.gov/about/api  
- **Contents:** Industry payments to physicians, NPPs, teaching hospitals (general, research, ownership); 2019–2025 shown; PY2025 published, next update Jan 2027.  
- **Medical Affairs jobs:** KOL mapping, compliance/transparency, advisory board planning  
- **Skills:** `kol-engagement-brief`, `advisory-board-design`  
- **Access:** Open API (DKAN metastore/datastore, SQL query) + bulk downloads  
- **Rate limit:** Not stated  
- **License:** Public CMS data  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON, CSV, XML; MCP: No official MCP server found  
- **Caveats:** CMS notes Open Payments lacks NPIs, so joins to Part D need name/address matching. Our box got 403 from the API host; WebFetch worked.  
- **Verification:** `partially-verified` on 2026-10-08. Home and API docs fetched; direct curl from box blocked (403).

### Medicare Part D Prescribers by Provider and Drug · **#6 in top 15**

- **URL:** https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug  
- **API docs:** https://data.cms.gov/api-docs  
- **Contents:** Claims, 30-day fills, days supply, drug cost by prescriber NPI, brand and generic; annual, latest 2024.  
- **Medical Affairs jobs:** launch planning (where patients are treated), field planning, HCP discovery  
- **Skills:** `field-medical-planning`, `medical-launch-plan`, `hcp-discovery-and-access`  
- **Access:** Open data-api v1 + CSV, no key  
- **Rate limit:** Not stated  
- **License:** Public Use File (free)  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON, CSV; MCP: No official MCP server found  
- **Caveats:** Medicare Part D population only; costs exclude rebates. Use for scientific engagement planning, not promotion targeting.  
- **Verification:** `verified-live` on 2026-10-08. data-api returned prescriber rows for 2024 dataset; FAQ fetched.

## Epidemiology & real-world data

_Burden of disease, RWE design_

### WHO Global Health Observatory OData API · **#13 in top 15**

- **URL:** https://www.who.int/data/gho  
- **API docs:** https://www.who.int/data/gho/info/gho-odata-api  
- **Contents:** Thousands of country-level indicators (e.g., obesity prevalence NCD_BMI_30A).  
- **Medical Affairs jobs:** epidemiology, launch planning (global burden)  
- **Skills:** `strategic-analysis`, `medical-strategy-plan`  
- **Access:** Open API, no key  
- **Rate limit:** Not stated  
- **License:** WHO datasets terms: royalty-free use with attribution; no sale of data  
- **Data policy:** Check terms — Royalty-free with attribution; no sale of data.  
- **Agent readiness:** JSON API; JSON (OData); MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-live` on 2026-10-08. Indicator and NCD_BMI_30A queries returned JSON; terms page fetched.

### CDC Open Data portal (data.cdc.gov, Socrata SODA API)

- **URL:** https://data.cdc.gov/  
- **API docs:** https://dev.socrata.com/docs/app-tokens.html  
- **Contents:** Hundreds of CDC datasets (surveillance, chronic disease, vaccination).  
- **Medical Affairs jobs:** epidemiology, insights  
- **Skills:** `strategic-analysis`, `insight-generation`  
- **Access:** Open; app token optional for higher throughput  
- **Rate limit:** Unauthenticated queries allowed but throttled (per Socrata docs)  
- **License:** Per dataset  
- **Data policy:** Check terms — Terms vary per dataset.  
- **Agent readiness:** JSON API; JSON, CSV; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-live` on 2026-10-08. resource/ahfs-x44r.json returned JSON.

### CDC WONDER

- **URL:** https://wonder.cdc.gov/  
- **API docs:** https://wonder.cdc.gov/wonder/help/wonder-api.html  
- **Contents:** Mortality, natality, cancer statistics, VAERS and more as aggregated queries.  
- **Medical Affairs jobs:** epidemiology  
- **Skills:** `strategic-analysis`, `real-world-evidence-design`  
- **Access:** XML POST API; must accept data-use restrictions  
- **Rate limit:** Robots: one query at a time, ~every 2 minutes  
- **License:** CDC data use restrictions; cite 'powered by CDC WONDER'  
- **Data policy:** Check terms — CDC data use restrictions apply; cite 'powered by CDC WONDER'.  
- **Agent readiness:** no JSON API; XML; MCP: No official MCP server found  
- **Caveats:** API returns national data only for vital statistics (no sub-national grouping). Box probe got 403; docs fetched via WebFetch.  
- **Verification:** `verified-docs` on 2026-10-08. API help page fetched.

### NHANES

- **URL:** https://wwwn.cdc.gov/nchs/nhanes/default.aspx  
- **API docs:** https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx  
- **Contents:** US survey: demographics, exam, lab, questionnaire, dietary data.  
- **Medical Affairs jobs:** epidemiology, evidence gaps  
- **Skills:** `real-world-evidence-design`, `spreadsheet-analysis`  
- **Access:** Bulk file download  
- **Rate limit:** n/a  
- **License:** NHANES Data User Agreement  
- **Data policy:** Check terms — NHANES data user agreement applies.  
- **Agent readiness:** no JSON API; XPT/SAS transport; MCP: No official MCP server found  
- **Caveats:** Survey weights required for valid estimates.  
- **Verification:** `verified-docs` on 2026-10-08. Pages loaded.

### SEER (NCI) — Explorer, research data, SEER API · **LINK ONLY: do not copy data**

- **URL:** https://seer.cancer.gov/  
- **API docs:** https://seer.cancer.gov/data/access.html  
- **Contents:** US cancer incidence, survival, prevalence.  
- **Medical Affairs jobs:** epidemiology (oncology), launch planning  
- **Skills:** `strategic-analysis`, `medical-launch-plan`  
- **Access:** Explorer web open; research data needs registration + SEER*Stat; SEER API needs a key  
- **Rate limit:** n/a  
- **License:** SEER data use agreement  
- **Data policy:** **LINK ONLY: do not copy data** — SEER data use agreement and API key required.  
- **Agent readiness:** no JSON API; HTML, SEER*Stat; MCP: No official MCP server found  
- **Caveats:** api.seer.cancer.gov returned 401 'You must supply an API key'.  
- **Verification:** `verified-docs` on 2026-10-08. Access page fetched; API key requirement observed.

### IHME Global Burden of Disease (GBD Results) · **LINK ONLY: do not copy data**

- **URL:** https://vizhub.healthdata.org/gbd-results/  
- **API docs:** https://www.healthdata.org/research-analysis/gbd-data  
- **Contents:** GBD 2023 estimates 1990–2023: incidence, prevalence, DALYs, deaths by cause/country.  
- **Medical Affairs jobs:** epidemiology, launch planning (global burden)  
- **Skills:** `strategic-analysis`, `medical-strategy-plan`  
- **Access:** Free download with registration  
- **Rate limit:** n/a  
- **License:** Free-of-charge NON-COMMERCIAL user agreement; no redistribution of data sets (links allowed)  
- **Data policy:** **LINK ONLY: do not copy data** — Non-commercial user agreement; no redistribution of data sets (links allowed).  
- **Agent readiness:** no JSON API; CSV; MCP: No official MCP server found  
- **Caveats:** Commercial pharma use likely needs a separate license; link only, do not copy into the repo.  
- **Verification:** `verified-docs` on 2026-10-08. GBD data page and user agreement fetched.

### AHRQ Medical Expenditure Panel Survey (MEPS)

- **URL:** https://meps.ahrq.gov/mepsweb/  
- **API docs:** https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp  
- **Contents:** US healthcare use and spending survey files.  
- **Medical Affairs jobs:** payer/HEOR, RWE design  
- **Skills:** `real-world-evidence-design`, `payer-value-dossier`  
- **Access:** Bulk download  
- **Rate limit:** n/a  
- **License:** Not reviewed  
- **Data policy:** Check terms — Terms not reviewed.  
- **Agent readiness:** no JSON API; Data files; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-docs` on 2026-10-08. Download page loaded.

### HMA-EMA Catalogues of RWD sources and studies (ex-EU PAS Register)

- **URL:** https://catalogues.ema.europa.eu/  
- **API docs:** https://catalogues.ema.europa.eu/  
- **Contents:** Registered RWD sources and non-interventional/PAS studies in Europe; exportable.  
- **Medical Affairs jobs:** RWE design, evidence planning  
- **Skills:** `real-world-evidence-design`, `integrated-evidence-plan`  
- **Access:** Web, searchable, export  
- **Rate limit:** n/a  
- **License:** Not reviewed  
- **Data policy:** Check terms — Terms not reviewed.  
- **Agent readiness:** no JSON API; HTML, export; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-docs` on 2026-10-08. Page fetched; replaced EU PAS Register in 2024.

## Coding & vocabularies

_Terminology mapping, search strategy, code lists_

### RxNav APIs (RxNorm, RxClass, RxTerms) · **#3 in top 15**

- **URL:** https://lhncbc.nlm.nih.gov/RxNav/  
- **API docs:** https://lhncbc.nlm.nih.gov/RxNav/APIs/RxNormAPIs.html  
- **Contents:** Normalized drug names/RxCUIs, brand↔generic, NDC links; RxClass drug classes (ATC, EPC, MoA).  
- **Medical Affairs jobs:** terminology, MI responses, competitive class mapping  
- **Skills:** `medical-terminology-mapping`, `competitive-intelligence`, `medical-information-response`  
- **Access:** Open API, no key (UMLS key optional for higher tier)  
- **Rate limit:** 20 requests/second per IP; 100/s with UMLS UTS API key; RxNav-in-a-Box for bulk  
- **License:** No license needed for RxNorm API (one exception); SNOMED-derived RxClass content under SNOMED Affiliate license  
- **Data policy:** Check terms — SNOMED-derived RxClass content needs a SNOMED Affiliate licence.  
- **Agent readiness:** JSON API; JSON, XML; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-live` on 2026-10-08. drugs.json and rxclass byDrugName returned JSON; Terms of Service fetched.

### MeSH RDF / Lookup API · **#11 in top 15**

- **URL:** https://id.nlm.nih.gov/mesh/  
- **API docs:** https://id.nlm.nih.gov/mesh/  
- **Contents:** Medical Subject Headings: descriptors, qualifiers, trees, pharmacological actions; SPARQL; full RDF download.  
- **Medical Affairs jobs:** search strategy, terminology  
- **Skills:** `pubmed-search`, `systematic-literature-review`, `medical-terminology-mapping`  
- **Access:** Open API, no key  
- **Rate limit:** Not stated  
- **License:** NLM terms: no charges/usage fees for MeSH  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON, RDF, SPARQL; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-live` on 2026-10-08. lookup/descriptor?label=Obesity returned D009765; terms page fetched.

### NLM Clinical Table Search Service (ICD-10-CM and more)

- **URL:** https://clinicaltables.nlm.nih.gov/  
- **API docs:** https://clinicaltables.nlm.nih.gov/apidoc/icd10cm/v3/doc.html  
- **Contents:** Autocomplete/search APIs for ICD-10-CM codes (also other tables).  
- **Medical Affairs jobs:** terminology, RWE code lists  
- **Skills:** `medical-terminology-mapping`, `real-world-evidence-design`  
- **Access:** Open API, free, 'as is'  
- **Rate limit:** See FAQ (not reviewed)  
- **License:** Free of charge  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; JSON; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `verified-live` on 2026-10-08. 'obesity' search returned E66.9, E66.1, E66.811.

### WHO ICD-11 API · **LINK ONLY: do not copy data**

- **URL:** https://icd.who.int/  
- **API docs:** https://icd.who.int/icdapi  
- **Contents:** ICD-11 (and ICD-10) classification via REST; Embedded Classification Tool; local container.  
- **Medical Affairs jobs:** terminology  
- **Skills:** `medical-terminology-mapping`  
- **Access:** Free registration for API keys  
- **Rate limit:** Not stated  
- **License:** CC BY-ND 3.0 IGO  
- **Data policy:** **LINK ONLY: do not copy data** — CC BY-ND 3.0 IGO: no redistribution of modified classification content.  
- **Agent readiness:** JSON API; JSON; MCP: No official MCP server found  
- **Caveats:** No-derivatives license: don't redistribute modified classification.  
- **Verification:** `verified-docs` on 2026-10-08. API home and ICD-11 license PDF fetched.

### UMLS Metathesaurus (incl. SNOMED CT US, MedDRA via license) · **LINK ONLY: do not copy data**

- **URL:** https://www.nlm.nih.gov/research/umls/index.html  
- **API docs:** https://www.nlm.nih.gov/research/umls/index.html  
- **Contents:** Crosswalk of 200+ vocabularies; SNOMED CT US Edition distributed to UMLS licensees.  
- **Medical Affairs jobs:** terminology, coding  
- **Skills:** `medical-terminology-mapping`  
- **Access:** Free license, individuals only (UTS account)  
- **Rate limit:** n/a  
- **License:** UMLS license; some sources need extra vendor agreements  
- **Data policy:** **LINK ONLY: do not copy data** — Personal UMLS license; SNOMED CT and some vocabularies need extra agreements.  
- **Agent readiness:** JSON API; RRF files, REST API; MCP: No official MCP server found  
- **Caveats:** Licenses are personal; do not commit UMLS/SNOMED content to the open repo.  
- **Verification:** `verified-docs` on 2026-10-08. UMLS and NLM SNOMED pages fetched.

## Science & mechanism (agent-ready extras)

_Scientific platform, mechanism landscape_

### Open Targets Platform (GraphQL + official MCP) · **#15 in top 15**

- **URL:** https://platform.opentargets.org/  
- **API docs:** https://platform-docs.opentargets.org/data-access/model-context-protocol  
- **Contents:** Target–disease evidence, drugs (ChEMBL), genetics, literature.  
- **Medical Affairs jobs:** scientific platform, competitive intelligence (mechanisms)  
- **Skills:** `scientific-platform`, `competitive-intelligence`  
- **Access:** Open GraphQL, BigQuery, downloads  
- **Rate limit:** Discourages entity-by-entity loops; use downloads for bulk  
- **License:** Data CC0 1.0; code Apache-2.0; underlying sources vary  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** JSON API; GraphQL JSON, Parquet; MCP: OFFICIAL remote MCP: https://mcp.platform.opentargets.org/mcp (marked under active development)  
- **Caveats:** Discovery-oriented; useful for mechanism/scientific narrative.  
- **Verification:** `verified-live` on 2026-10-08. GraphQL schema endpoint answered; MCP and licence pages fetched.

### PubChem PUG-REST

- **URL:** https://pubchem.ncbi.nlm.nih.gov/  
- **API docs:** https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest  
- **Contents:** Compound identity, properties, synonyms.  
- **Medical Affairs jobs:** MI responses (chemistry)  
- **Skills:** `medical-information-response`  
- **Access:** Open API, no key  
- **Rate limit:** Not verified (docs JS-rendered)  
- **License:** Not verified  
- **Data policy:** Check terms — License not verified.  
- **Agent readiness:** JSON API; JSON; MCP: No official MCP server found  
- **Caveats:** —  
- **Verification:** `partially-verified` on 2026-10-08. Property call for semaglutide returned JSON; docs not readable.

### ChEMBL web services

- **URL:** https://www.ebi.ac.uk/chembl/  
- **API docs:** https://chembl.gitbook.io/chembl-interface-documentation/web-services  
- **Contents:** Bioactive molecules, mechanisms, max phase, ATC.  
- **Medical Affairs jobs:** competitive intelligence (pipeline mechanisms)  
- **Skills:** `competitive-intelligence`  
- **Access:** Open API, no key  
- **Rate limit:** Not stated  
- **License:** CC BY-SA 3.0 (share-alike)  
- **Data policy:** Check terms — CC BY-SA 3.0: share-alike applies to redistributed derivatives.  
- **Agent readiness:** JSON API; JSON, XML; MCP: No official MCP server found  
- **Caveats:** Share-alike applies to redistributed derivatives.  
- **Verification:** `verified-live` on 2026-10-08. molecule search returned JSON; About page license fetched.

## Patient voice

_Patient engagement, unmet need_

### FDA Patient-Focused Drug Development meeting reports (FDA-led and externally-led) · **#14 in top 15**

- **URL:** https://www.fda.gov/industry/prescription-drug-user-fee-amendments/fda-led-patient-focused-drug-development-pfdd-public-meetings  
- **API docs:** https://www.fda.gov/industry/prescription-drug-user-fee-amendments/externally-led-patient-focused-drug-development-meetings  
- **Contents:** 'Voice of the Patient' reports on symptoms, impacts and treatment preferences by condition.  
- **Medical Affairs jobs:** patient engagement, evidence gaps (PROs), launch planning (unmet need)  
- **Skills:** `patient-engagement-planning`, `evidence-gap-analysis`, `medical-strategy-plan`  
- **Access:** Web/PDF  
- **Rate limit:** n/a  
- **License:** US government (externally-led reports authored by patient groups)  
- **Data policy:** Open — Public data; attribute the source and keep it separate from synthetic workshop data.  
- **Agent readiness:** no JSON API; HTML, PDF; MCP: No official MCP server found  
- **Caveats:** Best ToS-safe patient-voice source.  
- **Verification:** `verified-docs` on 2026-10-08. Both pages fetched.

### Reddit Data API (patient communities) · **LINK ONLY: do not copy data**

- **URL:** https://www.reddit.com/dev/api/  
- **API docs:** https://redditinc.com/policies/data-api-terms  
- **Contents:** Public posts/comments from patient communities.  
- **Medical Affairs jobs:** social listening (insights)  
- **Skills:** `insight-generation`  
- **Access:** Registration required  
- **Rate limit:** Per Reddit terms  
- **License:** Data API Terms: commercial use needs a separate agreement; no ML/AI training on user content without rightsholder permission  
- **Data policy:** **LINK ONLY: do not copy data** — Commercial use and AI training on user content need a separate agreement; monitored social data may trigger AE reporting.  
- **Agent readiness:** JSON API; JSON; MCP: No official MCP server found  
- **Caveats:** HIGH CAUTION for pharma: commercial use needs agreement; AE reporting obligations may apply to monitored social data. Do not include in hackathon by default.  
- **Verification:** `verified-docs` on 2026-10-08. Data API Terms fetched.

## Agent plumbing (MCP)

_Connect agents to many sources at once_

### Community MCP servers bundling public APIs (pharma-mcp, @drvibeai/clinical-apis-mcp, PubCrawl, helix-mcp)

- **URL:** https://github.com/pubspro/pharma-mcp  
- **API docs:** https://www.npmjs.com/package/@drvibeai/clinical-apis-mcp  
- **Contents:** Wrap ClinicalTrials.gov, PubMed, openFDA/FAERS, and (clinical-apis-mcp) Europe PMC, RxNorm, ICD-10, MedlinePlus, NPI, OpenAlex, PubChem, DailyMed, ChEMBL, Open Targets.  
- **Medical Affairs jobs:** all (agent plumbing)  
- **Skills:** `data-connection`, `public-evidence-search`  
- **Access:** Open source, self-hosted  
- **Rate limit:** Inherits upstream limits  
- **License:** Varies (clinical-apis-mcp Apache-2.0)  
- **Data policy:** Check terms — Unvetted third-party code; review before installing.  
- **Agent readiness:** JSON API; MCP; MCP: Community, not official; low adoption (clinical-apis-mcp ~17 weekly downloads)  
- **Caveats:** Unvetted third-party code; review before installing on corporate machines. The repo's own scripts/public_evidence.py may be safer.  
- **Verification:** `unverified` on 2026-10-08. Seen in web search results only; repos not fetched or tested.

## Not included / notes

- **Congress abstracts:** no free, open, agent-callable API was found for ASCO, ASH, EASD or AAD abstract libraries. Use journal-supplement records via Crossref, OpenAlex or Europe PMC, plus bioRxiv/medRxiv for preprints. Coverage is **UNVERIFIED**.
- **MedDRA / SNOMED CT:** need licenses (SNOMED CT through a UMLS Affiliate license). Never commit their content to an open repository.
- **Cochrane Library:** returned HTTP 429 to our probe; not reviewed.
- **Social and patient forums:** prefer FDA PFDD reports. Monitored social data can trigger adverse-event reporting obligations.

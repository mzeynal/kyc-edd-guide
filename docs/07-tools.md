[← Back to README](../README.md)

# Part 7. Tools and automation

## 7.1 Catalogue of tools by task

The state and prices of tools change (G): before adopting one, check the licence, terms, cost and the project's sustainability.

| Task | Tools (examples) | Note |
| --- | --- | --- |
| Search and archives | Google, Bing, Yandex; Wayback Machine, archive.today | Several search engines, different indexes; record the snapshot date |
| Company registers | National registers, OpenCorporates, GLEIF | The primary source matters more than the aggregator |
| Sanctions and PEPs | OpenSanctions; official OFAC, EU, UK and UN lists | Record the list version |
| Consortium databases | ICIJ Offshore Leaks, OCCRP Aleph | Section 3.4 |
| Courts and regulators | Court registers, SEC EDGAR, regulators' sites | Section 3.3 |
| Transport | AIS services, ADS-B aggregators, vessel and aircraft registers; Bellingcat's Turnstone tool | Delays and gaps in data (S) |
| Crypto-assets | Public block explorers; commercial analytics | Section 3.4 |
| Images | Reverse search (Google Lens, Yandex Images, TinEye), metadata analysis | Section 6.4 |
| Audio | Audacity (spectrograms) | Section 6.4 |
| Documents | OCRmyPDF, PDF viewers | Scans become searchable |
| Links | Spreadsheets, link-mapping programs | Reproducibility matters more than looks |
| Log and notes | Any tool with versioning and role-based access | One template across the team |

### How to choose

Criteria: reproducibility (a colleague gets the same result), licence (is commercial use allowed), data security (where queries and client data go), cost, sustainability. A new tool is first tested on non-confidential data.

### Working environment and evidence

- A separate browser profile or virtual machine for checks; separate accounts; disk encryption, a password manager, two-factor protection.
- Documents from untrusted sources are opened in an isolated environment.
- For every finding: a page screenshot, address and time (UTC), file hash, where permitted a copy in an external archive, a log entry; originals are stored separately and work is done on copies.
- If materials may go to a court or regulator, keep a chain-of-custody log: who received it, when, from where and to whom it was handed.

## 7.2 Automation: matching, screening, monitoring

Three rules: read the source's terms first, store the minimum of data, and always let a person make the final decision on a match. The code in `scripts/` is illustrative (G): check addresses, parameters and licences against the documentation before use.

### File hash for the evidence log

**Code:** [scripts/evidence_log.py](../scripts/evidence_log.py)

### Fuzzy name matching

**Code:** [scripts/name_matching.py](../scripts/name_matching.py)

The rapidfuzz library is installed via pip; Cyrillic, Arabic and Chinese script need prior transliteration (section 2.2); the similarity threshold is tuned on your data; a high score is a hypothesis, not proof.

### Screening against OpenSanctions via `/match`

Pass not just the name but also date of birth, country and entity type: it reduces false positives. Check the request and response format against the current documentation.

**Code:** [scripts/opensanctions_match.py](../scripts/opensanctions_match.py)

For bulk checks it makes sense to deploy a local copy of the open-source project (it is called yente) so that customer names are not sent to an external service; check the licence terms in advance (G).

### Monitoring sanctions list changes and re-screening

The script compares yesterday's and today's export of a sanctions dataset and matches new records against your customer base. Check the file path against the OpenSanctions documentation (G); commercial use of the data requires a licence (S).

**Code:** [scripts/sanctions_monitor.py](../scripts/sanctions_monitor.py)

The `norm` function is imported from `name_matching.py`. Every match goes through manual review against the indicators in section 4.2 and is recorded in the decision log ([templates/](../templates/)).

### Retention rules

Minimum fields, a retention period, restricted access, disk encryption, script versions and the export date in the log: without them the result cannot be reproduced.

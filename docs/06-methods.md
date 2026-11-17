[← Back to README](../README.md)

# Part 6. Methods

## 6.1 Profile and chronology

The subject profile is the main working document: identifiers, organisations, addresses, links, sanctions and courts, adverse findings, chronology, alternative versions, gaps. The template is in [templates/](../templates/).

Build the chronology from the very start: in every row a date, an event, a source, a confidence level; imprecise dates are recorded as ranges. The chronology reveals incompatible versions (a director before the company's registration, a payment after liquidation) and significant windows (±30 days around sanctions, a claim, a change of owners).

## 6.2 Links and their strength

A link is recorded as a statement: who with whom, of what type, in what period, from what source, with what confidence. Weak links (a shared address, a surname, a phone number) get the level "Possible" until confirmation appears.

The strength of a link is assessed on three criteria: **uniqueness** of the identifier (a registration number is stronger than a surname), **independence** of sources (two retellings of one news item are one source), **time** (the link existed on the date of the event, or appeared later). Indicators of the same kind do not add up; an agent's address means almost nothing.

| Starting identifier | Where it leads |
| --- | --- |
| Company registration number | Registers of other countries, financial statements, courts, procurement |
| Address | Other companies, mass registrations, property |
| Phone, e-mail | Accounts, listings, domains |
| Domain | Registration data, hosting, archives, related sites |
| Vessel (IMO) or aircraft (hex) number | Ownership histories, routes, sanctions |
| Wallet address | Transactions, clusters, exchanges |

Rules for a link map: each edge has a type, a period and a source; confirmed and assumed links differ in line style; a link without a source is not drawn; the map is simplified to what matters; the version is saved at the report date.

## 6.3 Competing hypotheses and cognitive biases

When there are several versions, list them in a table and assess each by the evidence that **refutes** it: the version with the fewest refuting facts is closer to the truth (G). Evidence consistent with every version (for example an agent's address) is not diagnostic.

Most often these spoil a conclusion: confirmation bias (looking for what fits the version), anchoring (the first detail defines the picture), availability bias, narrative bias (a nice story instead of facts), mirror imaging. Protection: a designated devil's advocate, stopping conditions set in advance, checking conclusions that rest on a single source.

## 6.4 Verifying sources, documents and images

- **Sources.** Distinguish primary (a register entry, a court judgment, a press release) from secondary (a retelling). Three questions: who is the author, where did the data come from, is there an interest in the outcome.
- **Images.** Provenance (reverse search in several systems, first publication, archives), metadata (EXIF is usually stripped), context (shadows, signs, plates), signs of generation (hands, text, background symmetry, lighting); detectors are unreliable, independent confirmations are needed. Content Credentials (C2PA) and the SynthID watermark help check provenance, but the absence of a mark proves nothing (S).
- **Documents.** Details, fonts, seals, numbering, signatures and dates checked for logic; comparison with the issuer's samples; scans without OCR are made searchable with OCRmyPDF (S).
- **Audio.** Spectrograms: in synthetic fragments the high-frequency part sometimes drops off faster than in live speech (S); it is an indicator, not proof.
- **AI in work.** A model's answer is not a source: take hypotheses to check, verify links and figures against the primary source, do not upload sensitive data to external services, record where and for what AI was used.
- **Archives.** Save pages at the time of work (Wayback Machine, archive.today), record the copy's address and time; pages can be removed at the owners' request (G).

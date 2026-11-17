# KYC, EDD and Corporate Intelligence: a working guide

Study notes on how to check people and companies for KYC, enhanced due diligence (EDD) and corporate intelligence: methods, legal limits, checklists, templates and small scripts. Everything is built on public data and public sources.

> **How this was made.** Compiled by Murad Zeynal with AI assistance and public sources, as a learning project. It is not professional or legal advice. Statements that depend on current events are marked as unverified (see below); methodology sections do not depend on them.

Last methodology update: 9 November 2026.

## Contents

| Part | What it covers |
| --- | --- |
| [1. KYC, CDD and EDD basics](docs/01-basics.md) | Levels of checks, customer lifecycle, legal limits, confidence scale, source log |
| [2. Background check of an individual](docs/02-background-check-individual.md) | Identification, claims, corporate roles, courts, PEP, digital footprint, source of wealth, report |
| [3. KYB: checking a company](docs/03-kyb.md) | Registers, beneficial ownership and control, financial statements, leaks, crypto |
| [4. Screening](docs/04-screening.md) | Sanctions, PEP, FATF country risk, OpenSanctions, working with matches |
| [5. EDD](docs/05-edd.md) | Triggers, content, monitoring, typologies and red flags |
| [6. Methods](docs/06-methods.md) | Chronology, link strength, competing hypotheses, verifying sources |
| [7. Tools and automation](docs/07-tools.md) | Tool catalogue, evidence handling, scripts |
| [8. Lessons from cases](docs/08-cases.md) | How to review a public case without hindsight |
| [9. Glossary](docs/09-glossary.md) | Terms |
| [Templates](templates/) | Report, EDD memo, ownership chain, questionnaire, logs, checklist |
| [Scripts](scripts/) | Evidence log, name matching, OpenSanctions screening, sanctions monitoring |
| [Update snapshot](updates/2026-11.md) | Dated, **unverified** snapshot of lists, packages and registers |
| [Sources and verification](docs/10-sources-and-verification.md) | What was and was not verified, primary sources |

## Five practical conclusions

1. **Screening must be repeated on events.** A major sanctions package or a change in a country's status triggers a review; it does not wait for the scheduled date.
2. **The ownership register is no longer the foundation.** Conclusions about the beneficial owner are built from several layers: register, financial statements, courts, procurement, consortium leaks.
3. **A background check is not a search by name.** It needs identification, verification of what is claimed, corporate roles, courts, PEP, sanctions and source of wealth.
4. **Sanctions evasion is a network.** Intermediaries, vessels, payment channels and successors are linked; a profile of one person is almost always incomplete.
5. **Every conclusion carries a date and a source version.** Lists and registers change within days.

## How to read the marks

| Mark | Meaning |
| --- | --- |
| **S** | From search results or an earlier draft: the page was not opened in full, so check figures and dates against the primary source |
| **G** | General knowledge, not checked against fresh sources: verify before applying, especially law and prices |
| **V** | Verified directly (page opened and read in full). No dated fact in this edition carries V |

Statements without a mark are methodological recommendations that do not depend on current events.

## Limits

- This is not legal advice. Rules on checking people, data processing, criminal records and sanctions depend on the country; get a lawyer's review before commercial use.
- A background check is run only on a lawful basis: the subject's consent, a contractual or regulatory obligation, or a legitimate interest with a proportionality assessment (section 1.2). The guide does not describe collecting information on private individuals without a basis.
- Contact with the person being checked or their circle, logging in to other people's accounts, using stolen data and deception to obtain information are excluded.
- All names in examples and scripts are fictitious.

## Corrections

Spotted an error or a stale fact? Open an issue. Corrections to S and G items are especially welcome.

## License

Text and templates: [CC BY 4.0](LICENSE-docs.md). Code in `scripts/`: [MIT](LICENSE). OpenSanctions data has its own terms (free for non-commercial use only).

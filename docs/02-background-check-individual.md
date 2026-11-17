[← Back to README](../README.md)

# Part 2. Background check of an individual

A background check is a set of checks on one person for a specific decision: accepting a beneficial owner, appointing a director, hiring someone for a role with access to money, starting business with a partner. The scope is set by role and risk; the basis and purpose are recorded before work begins.

## 2.1 Scope by role and order of work

| Role | What we check | Depth |
| --- | --- | --- |
| Beneficial owner or shareholder at 25% or more (the threshold depends on the regime) | Identity, PEP, sanctions, adverse media, source of wealth, other roles and assets | Standard, EDD for high risk |
| Director, authorised signatory | Identity, roles in other companies, disqualifications, courts, PEP, sanctions, adverse media | Standard |
| Candidate for a role with access to money, data or procurement | Identity, education, employment, licences, references, courts and insolvency, sanctions (criminal record only by lawful means and for eligible roles) | By role, with consent |
| Counterparty who is an individual or sole trader | Identity, business registration, courts, solvency, sanctions, adverse media | Standard |
| PEP, family members, close associates | All of the above plus source of wealth and funds, senior management approval | EDD |
| Investor, source of capital | Identity, source of wealth and source of funds, origin of assets, related structures | EDD for large sums and risk |

### Order of work

1. Record the purpose, basis, consent, role and time limit (section 1.2).
2. Build an identity card: name and spelling variants, date and place of birth, nationalities, identifiers (section 2.2).
3. Verify what is claimed: education, employment, licences (section 2.3).
4. Map corporate roles and links (section 2.4).
5. Check courts, insolvency, regulatory actions and, where permitted, criminal record (section 2.5).
6. Run screening: sanctions, PEP, adverse media (section 2.6).
7. Review the open digital footprint within the limits of the role (section 2.7).
8. For high risk, check source of wealth and funds (section 2.8).
9. Consolidate the results into a report with a confidence scale and gaps (section 2.9).
10. Keep the source log and delete excess data when the retention period ends.

Set a time limit in advance: a check that never ends usually turns into collecting unnecessary data.

## 2.2 Identification and verification

Identification collects data about a person; verification confirms that the data belongs to that person; further checks are pointless until the second is done.

### What counts as reliable confirmation (G)

- an identity document, with security features and the machine-readable zone checked;
- biometric comparison of the face with the document and a liveness check protected against presentation attacks;
- confirmation against a reliable register or state digital identity;
- for legal entities: supporting documents taken from the register, not only a copy sent by the customer.

### Remote onboarding risks

Deepfakes, generated documents and "synthetic" identities (a mix of real and fabricated data) have made a photo check insufficient. Measures: certified liveness detection protected against injection of a fake stream (G: ISO/IEC 30107-3), device, geolocation and IP checks, an independent data source, manual review in doubtful cases. AI-content detectors are limited: Google's SynthID Detector, open to everyone since 7 October 2026, finds only content made by models that carry this watermark, and the absence of a watermark proves nothing (S).

### Identifiers and their strength

| Identifier | Strength | Note |
| --- | --- | --- |
| Document number or national identifier | Very high | Do not store without need; the law restricts use |
| Date and place of birth | High together | One alone is insufficient |
| E-mail address, phone number | Medium | They change and get reassigned |
| Photograph | Medium | Forgeries, other people's photos |
| Name | Low | Namesakes and transliterations |

### Names and transliteration

| Source of discrepancy | Example | What to do |
| --- | --- | --- |
| Cyrillic transliteration standards | Юрий: Yuri, Yury, Yuriy, Iurii, Jurij | Build the set of variants; check each |
| Patronymics | Иванович: Ivanovich, Ivanovitch | Search with and without the patronymic |
| Arabic names | Мухаммад: Mohammed, Muhammad, Mohamed | Account for articles (al-, el-) and connectors (bin, ibn) |
| Chinese names | Surname first, pinyin with or without tones | Check both orders |
| Double surnames | Spanish and Portuguese traditions | Search by each part |
| Diacritics | Müller, Mueller, Muller | Search with and without diacritics |
| Change of name | Marriage, pseudonyms | Check previous names and "aka" records |

Automatic matching uses Levenshtein and Jaro–Winkler distance, phonetic algorithms and token-set comparison (G); any result gives a hypothesis, and confirmation comes from a second independent identifier.

### Namesakes: the procedure

1. A matching name means nothing yet.
2. Check date of birth, nationality, place of birth.
3. Check occupation, organisations, geography.
4. For public figures, compare the photo with verified images.
5. Record the decision: "same person: confirmed", "probable", "different persons", "undetermined", and the indicators on which it was made.

## 2.3 Verifying what the person claims: education, employment, licences

Every statement in a CV or questionnaire becomes a record of "claim, evidence, status"; a profile on a professional network does not count as confirmation, it is the person's own claim.

| Claim | How to confirm | Red flags |
| --- | --- | --- |
| Education, degree | Request to the institution through official contacts with consent; national diploma and accreditation registers where they exist (G); check that the institution is accredited | Institution not found or not accredited, degree "for experience", no study dates, name mismatch |
| Employment | Confirmation from HR through contacts found independently, not those supplied by the candidate; company registers (director periods); publications about positions | Company dissolved before the claimed dates, no trace of the organisation, contact supplied only by the candidate |
| Professional licence | Register of the regulator or professional body (for example registers of financial regulators, lawyers, doctors; G) | No entry, entry under a different name, licence suspended |
| Awards, publications, memberships | Primary source: the organiser, publisher, membership register | No confirmation, inflated significance |
| References | Referees found independently; structured questions | Only referees named by the candidate; evasive answers |
| Continuity of the biography | A timeline without gaps and overlaps | Unclear periods, overlapping dates, frequent changes |

### Rules

1. Start with claims that affect the decision: for a finance role, licence and experience matter more than hobbies.
2. Confirmation comes from the primary source through an independent channel.
3. A discrepancy is not deception: first establish the innocent explanation (a renamed university or company, transliteration).
4. Record the result for each claim: confirmed, not confirmed, refuted, not checked.
5. Employers and schools may decline to answer; a refusal is recorded as a gap, not as a negative.
6. Employment checks require consent and compliance with data protection rules (section 1.2).

## 2.4 Corporate roles, shareholdings, related parties, conflicts of interest

This check shows where a person takes part in business, with whom and with what result: serial dissolutions, hundreds of directorships or past ties to sanctioned structures say more than any questionnaire.

### How to search

1. **Officer search** in the company registers of countries where the person might have worked. Many registers (for example the UK Companies House) allow search by name with month and year of birth (G).
2. **Confirm it is the same person:** date of birth, nationality, addresses, linked companies, signature in filings. Namesakes in registers are common.
3. **Roles table:** company, number, country, role, shareholding, from and to dates, company status.
4. **Check each company:** active or dissolved, reason for dissolution, insolvency, courts, sanctions, addresses (section 3.1).
5. **Related parties:** relatives, business partners, shared addresses and signatories; distinguish confirmed from assumed links (section 6.2).
6. **Conflicts of interest:** shares or roles in companies that compete with or serve the client; related-party transactions.
7. **Disqualifications and bans:** registers of disqualified directors, debarment lists, regulator decisions (G: availability depends on the country).

### What counts as a signal

| Signal | What to check |
| --- | --- |
| Hundreds of directorships held by one person | A professional agent or nominee; who actually makes decisions |
| Many companies dissolved soon after creation | Purpose of creation, accounts, debts |
| Roles in companies from sanctions chains | Period, sanctions date, whether the link persists |
| Sharp changes of roles before problems become public | Chronology, a ±30-day window around the event |
| Related-party transactions on non-market terms | Terms, collateral, independent valuations |
| A role in a company with no visible business | Staff, website, address, tax traces |

A signal is a reason to dig further, not a conclusion. More on ownership chains and control in section 3.2.

## 2.5 Courts, insolvency, regulatory actions, criminal records

Court and regulatory records help show a person's conduct in business, but they must be read by stage and with allowance for the law: a charge is not a conviction, a claim does not prove the claimant right, and criminal-record data is available far from everywhere.

| Source | What it shows | Limits |
| --- | --- | --- |
| Civil and commercial courts | Claims, judgments, amounts, parties, exhibits with contracts and statements | Availability and name search differ by country; claims can be unfounded |
| Insolvency cases and registers | Creditors, assets, administrator, periods | Date and type of procedure; personal and corporate insolvency differ |
| Regulatory actions and warnings (financial and professional regulators) | Fines, licence withdrawals, bans | Date, basis, whether the measure is still in force |
| Debarment and disqualification lists | Bans on procurement and management roles | Duration |
| Prosecutor and regulator press releases | Content of charges, companies named | A charge is not a conviction |
| Criminal records | Convictions | Only by lawful means (see below) |

### Criminal records

In most countries the law restricts access to convictions: a certificate is issued by an official body to the person themselves or to the verifier for an eligible role and with consent, and rehabilitation rules apply to spent convictions (G). In the EU, processing data on convictions and charges is allowed only within state law (Article 10 GDPR). Therefore:

- request the certificate from the person or through an official channel, rather than searching "on the internet";
- do not use a conviction unrelated to the role for hiring, and do not count spent entries;
- read public reports of verdicts (judgments, press releases) as primary documents, and check news retellings against them;
- record the stage: suspicion, charge, verdict, appeal, expungement.

### What to include in the report

The stage, court or authority, number, date, substance, link to the role and an assessment of how old it is. Exclude information not relevant to the decision and data on third parties (victims, witnesses).

## 2.6 PEP, sanctions and adverse media for an individual

Screening a person is a procedure in five steps: data, match, assessment, decision, record; a "search by name" decides nothing by itself.

### PEP

A politically exposed person (PEP) holds a prominent public function. Screening covers three circles: the PEP themselves (domestic, foreign, from an international organisation), their family members and close associates (relatives and close associates, RCA). The period after leaving office depends on the regime: European rules set at least 12 months, then a risk-based approach (G). Under the AMLR the PEP definition is widened to include, for example, heads of local authorities in larger municipalities (S).

### Sanctions

Check the name, variants, date of birth, nationality and identifiers against current versions of the US, EU, UK and UN lists (section 4.1). For a person who owns a company, check the companies too: in some regimes a person under blocking makes the organisations they control problematic.

### Adverse media

1. **Multilingual search:** the name in all relevant languages and in all spelling variants.
2. **Keywords:** charge, investigation, arrest, fine, sanctions, claim, bankruptcy, corruption, fraud, laundering, plus industry terms.
3. **Time window:** old and recent publications separately; old cases may be closed.
4. **Source quality:** a court judgment and a leading publication weigh more than an anonymous blog; a single source gives "Possible".
5. **Primary check:** go from the publication to the document (court, regulator, register).
6. **Proportionality:** a neutral publication is not adverse; rumours and politically motivated reporting are not legal facts.
7. **Recording:** a copy of the article, address, date of access.

### Assessing a finding

| Criterion | Question |
| --- | --- |
| Relevance | Does it relate to the role and the decision |
| Credibility | Primary document or retelling; independent sources |
| Age | Recent or closed case; has the period passed |
| Seriousness | Financial crime, corruption, violence, regulatory breach |
| Identity | Is it the same person: a second identifier |

A match confirmed only by name is recorded as a hypothesis. What to do with it is decided by a person under the organisation's policy (section 1.3).

## 2.7 Digital footprint

The open digital footprint is checked to confirm or refute what is claimed and to find risk relevant to the role; combing through a person's whole online life is not a check but collection of unnecessary data.

### Permitted sources

- open profiles on professional and social networks, publications, talks, media mentions;
- domains, websites, listings and marketplace profiles linked to the person's business;
- web archives for old versions of pages (section 6.4);
- open databases and registers from section 7.1.

### Limits

1. Only open data and only as relevant to the role. Do not create fake personas, do not send friend requests, do not enter closed profiles.
2. Do not collect data on relatives and friends beyond what is necessary, especially minors.
3. Do not record protected characteristics (health, religion, views, origin, marital status) unless they affect the decision.
4. Do not use face-search services on private individuals without legal assessment: biometric data is strictly regulated.
5. Do not use leaks or data from closed sources.

### How to verify authenticity of what you find

| Question | Technique |
| --- | --- |
| Does the profile belong to this exact person? | Match unique details (place of work, date, connections), not only the name |
| Is the profile real? | Account age, activity history, consistency, reuse of photos |
| Is the photo real? | Reverse search in several systems; provenance check (section 6.4) |
| Is the claim independently confirmed? | A register, document or third-party publication |
| Is the content still available? | Screenshot, address, time, archive copy |

AI fakes (generated faces, fake profiles, deepfakes) should be assumed possible as a hypothesis: rely on provenance and independent confirmation, not on how something "looks".

## 2.8 Source of wealth and source of funds

Source of wealth (SoW) answers how the person accumulated all of their wealth, source of funds (SoF) answers where this particular money in this transaction or relationship came from; EDD needs both answers with supporting documents, not on the customer's word.

### What to request and how to check it

| Source of wealth | What to request | How to check openly | Red flag |
| --- | --- | --- | --- |
| Salary, bonuses | Employment contracts, income statements, tax returns | Public data on the position and pay, employer's financial statements | The amount is disproportionate to the role and length of service |
| Business and dividends | Share extracts, financial statements, dividend decisions, tax documents | Company register, public accounts, procurement, courts | A business with no visible activity, dividends without profit |
| Sale of a business or stake | Agreement, payment confirmation, tax documents | News on the deal, registers, regulatory disclosures | No public trace of the deal, buyer unclear |
| Inheritance | Certificate, will, court decision | Public information on the deceased, registers | The amount is out of proportion to known assets |
| Real estate | Sale and purchase contracts, registration records | Property registers, listings | Deals at sharply different prices, intermediaries |
| Investments | Brokerage statements, reports | Public disclosures, market data | Returns that do not exist |
| Crypto-assets | Exchange statements, addresses, withdrawal confirmation | Blockchain explorers, public attributions (section 3.4) | The trail breaks at a mixer or an exchange with a sanctions history |
| Gifts and loans | Contract, payment confirmation, information on the donor | Check the donor under sections 2.4 and 2.6 | A third-party donor without explanation, a non-market loan |

### Logic checks

1. **Plausibility:** does the stated wealth match possible income over the period.
2. **Chronology:** the moment the money appeared and the event that explains it.
3. **Independent confirmation:** the customer's document and third-party data (register, court, bank, tax authority).
4. **Third parties:** who pays and why; whether they are linked to sanctions or PEPs.
5. **Countries and channels:** whether the chain includes jurisdictions from FATF lists or opaque intermediaries.

Per reviews of the AMLR, EDD becomes mandatory for customers with wealth of EUR 50 million or more, and wealth management customers face separate requirements (S; verify against the final technical standards).

### Red flags

Unexplained wealth; several inconsistent versions of the source; money from third parties; large cash; crypto with no trail; complex structures with no business purpose; reluctance to provide documents; time pressure.

## 2.9 The background check report

The report answers the client's decision (accept, accept with conditions, EDD, refuse) and shows what it rests on; a list of findings without a conclusion is not a report. The template is in [templates/](../templates/).

### Structure

1. **Conclusion and recommendation** in the first lines: the decision, the confidence level, the main grounds.
2. **Purpose, basis and scope:** who the client is, for which role, what was checked, what was not, whether there is consent.
3. **Identity:** how it was confirmed, which indicators matched.
4. **Checks table:** claim, source, status (confirmed, not confirmed, refuted, not checked).
5. **Findings:** courts, insolvency, regulatory actions, PEP, sanctions, adverse media, each with stage, date, source and relevance assessment.
6. **Corporate roles and links**, and source of wealth where needed.
7. **Alternative explanations** for significant findings.
8. **Gaps and limits:** what could not be checked, which sources were unavailable, possible distortions.
9. **Appendices:** source log, chronology, copies of documents with hashes.

### How to write adverse findings

- Fact and source: "according to the register on 9.11.2026, insolvency proceedings against company X were opened in 2022".
- Stage: "charge", "verdict", "appealed".
- No judgments of character and no speculation on causes.
- Distinguish "found", "confirmed" and "relevant to the role".

### The person's right of reply

If a report may lead to a refusal, the person is given a chance to explain the finding or correct an error; some regimes (for example employment screening in the US) require notices before and after a refusal (G, section 1.2). A correction is recorded: what changed and how it affected the conclusion.

### Retention and access

Only the person who needs the report for the decision receives it. The retention period is set by policy and law; when it expires the materials are deleted and the log keeps a record of the deletion. File metadata is cleaned before transfer.

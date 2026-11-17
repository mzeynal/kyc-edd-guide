[← Back to README](../README.md)

# Part 4. Screening

## 4.1 Sanctions regimes

Sanctions screening is decided on the list version on the date of the transaction, so every decision records the list, its version and the licences in force. Recent changes are tracked separately in [updates/2026-11.md](../updates/2026-11.md).

### United States (OFAC)

OFAC maintains the SDN list and related lists. Basic concepts (G): blocking of property and a ban on dealings for "US persons"; the 50% rule (a legal entity owned 50% or more in aggregate by blocked persons is itself blocked); secondary sanctions for foreign financial institutions; general licences (GL) for temporary relief, for example for winding down operations. Check the current state on the official OFAC website.

### European Union, United Kingdom and the UN

In practice for the EU: study the annexes to Regulations 269/2014 (individual measures) and 833/2014 (sectoral), and track the identifiers (registration numbers, addresses) of new entries (G). UK identifiers come from the UK Sanctions List. UN Security Council lists are the basis of national regimes; check their composition on the Council's site (G).

### How to read an entry

Name, aliases, dates of birth, nationality, addresses, identifiers (passport, tax number, organisation registration number, vessel number), sanctions programme, tags, notes. For an investigator the most valuable items are organisation identifiers, related persons, addresses, vessels and aircraft, crypto addresses.

### Screening rules for sanctions

1. Screen the customer, beneficial owners, directors, controlling persons and key counterparties.
2. Check both ownership and control (section 3.2): blocking of a controller makes their companies problematic.
3. Record the list version, date and result, including "no matches".
4. Repeat screening on events: a new sanctions package, a change of structure, a suspicious transaction.
5. Take licences and wind-down periods into account.
6. Do not tip off the subject and escalate to legal (section 1.2).

## 4.2 PEP, country risk (FATF), adverse media and OpenSanctions

A country's status on a FATF list is a risk factor, not a prohibition: the grey list means work on an action plan to fix deficiencies, the black list means a call for enhanced measures or countermeasures (S).

### FATF

Plenaries are held in February, June and October; the lists change at each one (see [updates/2026-11.md](../updates/2026-11.md) for the latest snapshot). For removed countries enhanced measures need not be lifted automatically: your policy decides. Record the date of the country's status in the report.

### Country risk in the process

Consider not only the customer's country but also the country of registration, operations, counterparties, source of funds and payment channels. A mistake is to treat the grey list as sanctions; for the black list the requirements are stricter, and for Iran and the DPRK they are supplemented by UN sanctions.

### OpenSanctions (S)

An open database that brings sanctions, PEPs and regulatory measures into one model. The main "Default" dataset includes sanctions, regulatory lists and PEPs; choose datasets for screening under your policy. Use is free for non-commercial purposes; commercial use needs a licence. Dataset names, API fields and terms change between releases: read the changelog before updating scripts and state the dataset version in the report.

Two main API calls (G, check the documentation): `/search` for text search in manual checks and `/match` for matching a structured record (name, date of birth, country) with a match score.

### Working with matches

| Indicator | Strength |
| --- | --- |
| Registration or passport number | Very high |
| Date of birth and nationality | High together |
| Address | Medium; mass-registration addresses add noise |
| Name | Low |

Procedure: prepare the data, get matches, assess them against the indicators, make a decision (true, false, undetermined), record the reason, escalate undetermined and true matches. Record why a match was judged false so that repeat screening does not start from zero. An automatic match is a hypothesis; confirmation comes from a second identifier. Regular and event-driven re-screening is mandatory (section 1.1).

# PNP P004 — Customer emails that cannot be delivered (independent SQL reattempt 4)

**Date:** 2026-11-06 · **Status:** Not attempted in this session.  
**Source:** PNP Q004; previously solved 2026-10-27, so this is a reattempt, **not a new PNP completion**.  
**Original source file (contains solutions; do not open until after the attempt):** [P004 original in Mastry](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/8.%20Advance%20string%20functions%2C%20regex%20and%20clause/P004.%20Customer%20emails%20that%20cannot%20be%20delivered.md).

## Problem — independently worded summary

A marketing team wants to remove customer email addresses that may cause failed deliveries. Return customers whose email address:
1. Is **missing** (`NULL` or blank/only spaces), or
2. **Contains a literal space**, or
3. Fails a simple required `name@domain.tld` structure (at least one character before @, at least one after @ before a dot, and at least one after the dot).

Produce exactly these columns in order: `CustomerID`, `FirstName`, `LastName`, `Email` (unchanged), `issue`.

**Issue labels and precedence:** `Missing` for absent or blank addresses; `Contains a space` for nonblank addresses containing a literal space; otherwise `Not in name@domain.tld form` for entries failing the simple shape test. Return invalid records only; sort by `CustomerID` ascending.

This is an **illustrative format check**, not a production-grade email validator. Preserve the source's simple matching contract.

## Sample input — Customers

| CustomerID | FirstName | LastName | Email |
|---:|---|---|---|
| 1 | Asha | Rao | NULL |
| 2 | Ben | Das | `ben das@example.com` |
| 3 | Cia | Sen | `cia.example.com` |
| 4 | Dev | Roy | `dev@example.com` |

## Expected output

| CustomerID | FirstName | LastName | Email | issue |
|---:|---|---|---|---|
| 1 | Asha | Rao | NULL | Missing |
| 2 | Ben | Das | `ben das@example.com` | Contains a space |
| 3 | Cia | Sen | `cia.example.com` | Not in name@domain.tld form |

### Why each row appears (no solution spoilers)

- **Asha (1):** NULL email means absent contact information, hence `Missing`.
- **Ben (2):** His address contains a literal space between `ben` and `das`, hence `Contains a space`.
- **Cia (3):** No @ symbol, so the address fails the required structure, hence `Not in name@domain.tld form`.
- **Dev (4) excluded:** `dev@example.com` satisfies the simplified shape and has no space; therefore no issue needs reporting.

**Expected:** Exactly 3 rows, the 5 specified columns and ascending CustomerID.

## Learner-led practice (pending)

**Step 1 reasoning:** Not submitted.  
**First independently authored SQLite query:** Withheld pending student's attempt.  
**Actual intermediate SQL output:** Not executed yet.  
**Independent revisions:** Not submitted.  
**Assistant SQLite reference:** Withheld until review.  
**Assistant SQL Server/T-SQL reference:** Withheld until review; execution not claimed.  
**Source-labeled official answer:** Available within the original source record, not shown before the student's own attempt.  
**New learning Yes/No:** Pending.  
**Question closing commit:** Pending in both repositories.

## Cross-repository records

- [Journey P004](https://github.com/MulikShrikantDattatray14/data-engineering-journey/blob/main/study-records/2026-11-06/PNP-P004-invalid-customer-emails-reattempt.md)
- [Mastry P004](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/study-records/2026-11-06/PNP-P004-invalid-customer-emails-reattempt.md)


## First independent attempt — execution check

The first submitted SQL was executed in SQLite 3.46.1. On the four provided sample customers it returned exactly Asha (Missing), Ben (Contains a space), and Cia (Not in name@domain.tld form), in ID order, with five correct column headings.

Additional cases demonstrated limitations: blank and whitespace-only emails were marked invalid format rather than Missing; a valid address ending in `.org` was rejected; and embedded spaces after @ or within the domain could be missed. The complete verbatim query, actual sample output and extended test results are archived in the cross-linked Journey study record. This is a reviewed but not yet independently corrected P004 reattempt. No new PNP source completion credit.

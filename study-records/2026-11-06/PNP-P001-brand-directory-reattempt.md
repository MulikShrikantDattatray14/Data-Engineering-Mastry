# PNP P001 — Brand directory (Day 1 source reattempt 1)

**Date:** 2026-11-06 · **SQL Slot 1** · **Status:** Reattempt pending (no new attempt submitted).  
**Source:** PrepNPlaced P001, previously solved 2026-10-26; this is a **reattempt**, not a new source-problem completion.  
**Original source record:** [P001 in Data Engineering Mastry](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/0.%20SQL%20basics/P001.%20Brand%20directory.md).  
**Mirrored learning records:** [Journey](https://github.com/MulikShrikantDattatray14/data-engineering-journey/blob/main/study-records/2026-11-06/PNP-P001-brand-directory-reattempt.md) · [Mastry](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/study-records/2026-11-06/PNP-P001-brand-directory-reattempt.md).

## Problem (independently worded summary of the existing source record)

Create a clean, alphabetically ordered list of **distinct brand names** found in the `Products` table for an e-commerce brand-selection filter. Ignore missing brands, empty strings and entries containing only spaces. Extra spaces around a brand name should not cause it to be treated as a different brand. Return a single column named `Brand`.

The source record contains the whole dataset schema; this reattempt uses the existing record's **illustrative 8-row sample**, rather than asserting those values are from the original dataset.

## Sample input: Products

| ProductID | Brand |
|---:|---|
| 1 | `Nike` |
| 2 | ` Nike ` (one space on both sides) |
| 3 | NULL |
| 4 | `''` (empty string) |
| 5 | `   ` (three spaces) |
| 6 | `Adidas` |
| 7 | `Puma` |
| 8 | `Adidas` |

## Expected output

| Brand |
|---|
| Adidas |
| Nike |
| Puma |

**Why:** The two variants of Nike represent one cleaned name. Adidas appears twice but must be listed once. Product 3 has NULL, 4 is empty, and 5 has only spaces, so none becomes an output entry. Puma is valid. The three remaining names are alphabetically sorted. No algorithm or SQL answer is provided before the independent reattempt.

## Learner-led workspace

**First reasoning:** Pending.  
**Original reattempt SQL submission:** Pending.  
**Actual SQLite output/errors:** Pending.  
**Independent correction:** Pending.  
**Post-attempt assistant SQLite reference:** Withheld.  
**Post-attempt assistant T-SQL reference:** Withheld.  
**Provider's official answer from existing source:** Withheld until after learner submission; do not misattribute the source repository's earlier solution to the current attempt.  
**Progress:** Baseline source P001 already previously solved; no reattempt credit until newly verified.

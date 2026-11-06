# Q8 — Vendors Without Qualifying Deliveries

**Date:** 2026-11-06 · **Day 1 / Slot 1 / Question 8**  
**Type:** Tutor-created diagnostic (not a PNP source question)  
**Dialect for learner:** SQLite · **Status:** Unattempted; Step 1 reasoning pending  
**Source learning journal:** [Day 1 Slot 1](https://github.com/MulikShrikantDattatray14/data-engineering-journey/blob/main/10-learning-journal/sessions/2026-11-06/slot-01-sql.md)  
**Cross-repository record:** [Main learning repo](https://github.com/MulikShrikantDattatray14/data-engineering-journey/blob/main/study-records/2026-11-06/Q8-vendors-without-qualifying-deliveries.md) · [Source/practice repo](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/study-records/2026-11-06/Q8-vendors-without-qualifying-deliveries.md)

## Complete question

As a Data Engineer at an e-commerce logistics company, identify all vendors who **have never had any qualifying delivery**.

A delivery qualifies only when ALL of the following hold:
1. `status = 'delivered'`.
2. `amount > 1000` (strictly greater; NULL does not qualify).
3. **Either** the vendor's region is `West` **OR** the delivery service is `express`.

Include vendors without any deliveries. Exclude a vendor if even one delivery meets all qualifying conditions.

**Return** exactly `vendor_id`, `vendor_name` and `region`, once per qualifying vendor, sorted by `vendor_id` ascending.

**Practice constraint:** Use a JOIN-based SQLite approach; avoid subqueries and aggregation for this diagnostic. Do not hardcode vendor IDs.

## Sample input 1 — vendors

| vendor_id | vendor_name | region |
|---:|---|---|
| 1 | Atlas | West |
| 2 | Birch | North |
| 3 | Coral | West |
| 4 | Drift | South |
| 5 | Ember | North |
| 6 | Fern | West |
| 7 | Grove | South |
| 8 | Haven | East |

## Sample input 2 — deliveries

| delivery_id | vendor_id | status | amount | service |
|---:|---:|---|---:|---|
| 301 | 1 | delivered | 800 | standard |
| 302 | 1 | pending | 2200 | express |
| 303 | 2 | delivered | 1700 | standard |
| 304 | 3 | delivered | 1900 | express |
| 305 | 3 | delivered | 400 | standard |
| 306 | 4 | delivered | NULL | express |
| 307 | 5 | failed | 3000 | express |
| 308 | 6 | delivered | 1200 | standard |
| 309 | 7 | delivered | 1400 | express |

Vendor 8 has no delivery.

## Expected sample output

| vendor_id | vendor_name | region |
|---:|---|---|
| 1 | Atlas | West |
| 2 | Birch | North |
| 4 | Drift | South |
| 5 | Ember | North |
| 8 | Haven | East |

**Expected rows:** 5. Column order must be as shown and vendor IDs must be ascending.

## Explain the expected output (without revealing SQL)

- **Atlas (1): Include.** Delivered 800 is too low; pending 2200 fails the status condition even though it is express.
- **Birch (2): Include.** Delivered 1700 is large enough, but region North and service standard both fail the third condition.
- **Coral (3): Exclude.** Delivery 304 is delivered, 1900, and express, so at least one qualifying delivery exists. Delivery 305's low amount doesn't negate that.
- **Drift (4): Include.** Express delivered record exists, but amount NULL cannot be established as greater than 1000.
- **Ember (5): Include.** Large express delivery was failed, not delivered.
- **Fern (6): Exclude.** Delivered 1200 qualifies due to vendor region West even with standard service.
- **Grove (7): Exclude.** Delivered 1400 express qualifies, even outside West.
- **Haven (8): Include.** No deliveries means zero qualifying deliveries.

## Student-led solving — not yet started

**Step 1 learner reasoning:** Pending.  
**Step 1 original SQLite query:** Pending.  
**Intermediate executed output and review:** Pending.  
**Next steps:** To be authored by learner, not prefilled.

## Final answer and progressive reference walkthrough

**Learner's first complete SQLite solution:** Withheld pending independent attempt.  
**Learner's corrected solution:** Not submitted.  
**Actual versus expected output:** Not executed yet.  
**Assistant-reviewed SQLite reference:** Withheld.  
**Assistant-converted SQL Server/T-SQL reference:** Withheld.  
**Detailed worked solution and output after each step:** Withheld until learner completes attempt.  
**Official provider answer key:** Not applicable; this is an original tutor question.

## Learning and completion integrity

Optional new learning capture: pending. No Q8 source/diagnostic completion credit or mastery claim. Commit and cross-link the final reviewed material in both repositories after the student finishes the question.

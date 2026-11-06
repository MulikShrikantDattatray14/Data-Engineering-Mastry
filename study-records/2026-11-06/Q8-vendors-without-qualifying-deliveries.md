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


## Step 1 — Learner's initial reasoning (verbatim)

```text
i can solve it using sub query and joins concept

so first lets start with subquery
```

**Review:** Valid as a supplementary learning approach: start by identifying qualifying vendor IDs in an inner query. The problem's original JOIN-only constraint remains mandatory for the final diagnostic, so the student will also independently solve using JOINs. The learner has not submitted SQL yet. **Next:** Ask for the independently written inner SQLite query only; do not reveal the query or its answer. No completion credit.


## Step 1 — Learner switches to JOIN approach: first SQLite query

**Student's accompanying statement (verbatim):**
```text
so lets start with  joins apporach directly
```

**Original learner SQLite query (verbatim):**

```sql
select vendor_id
from vendors as v
left join deliveries as d on v.vendor_id=d.vendor_id
```

**Actual SQLite execution using the Q8 vendors/deliveries sample:** `OperationalError: ambiguous column name: vendor_id`. The original query was executed and failed; it produced **no result set**, not a valid empty table.

**Reason:** Both joined tables define `vendor_id`; the selected column must be qualified with the intended table alias. The LEFT JOIN direction and ON key equality are otherwise correct. Do not reveal the final Q8 solution.

**Student correction:** Pending. **Step 2 reasoning:** Pending until Step 1 independently corrected and executed.

**Checkpoint status:** Intermediate archive only; no Q8 question-closing commit or completion credit.

## JOIN Step 1 — Second original attempt (column list corrected, trailing comma)

**Learner submission preserved verbatim:**

```sql
select d.delivery_id	, d.vendor_id,	v.vendor_name,	v.region, d.status,	d.amount,	d.service,
from vendors as v
left join deliveries as d on v.vendor_id=d.vendor_id
```

**Actual SQLite execution:** `OperationalError: near "from": syntax error`.

**Why:** After the last selected expression `d.service`, the learner placed a comma immediately before `FROM`, so SQLite expects another expression. The table aliases `d` and `v` are now qualified correctly, and the `LEFT JOIN` key condition is correct. No output table exists for this attempt; do not fabricate rows.

**Next:** Learner removes the trailing comma independently, resubmits only the corrected Step 1, then the assistant executes it and shows the actual result. No status or amount conditions and no Q8 reference solution are to be revealed yet.

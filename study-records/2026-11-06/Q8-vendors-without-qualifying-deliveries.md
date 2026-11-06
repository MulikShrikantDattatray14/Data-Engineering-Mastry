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


## Step 1 — Student's independently corrected LEFT JOIN query (executed successfully)

**Original submitted SQLite text, preserved exactly:**

```sql
select d.delivery_id	, d.vendor_id,	v.vendor_name,	v.region, d.status,	d.amount,	d.service
from vendors as v
left join deliveries as d on v.vendor_id=d.vendor_id
```

**Execution method:** The exact submitted SQL was executed in SQLite against the Q8 sample fixture (8 vendors, 9 deliveries).

**Actual column order:** `delivery_id`, `vendor_id`, `vendor_name`, `region`, `status`, `amount`, `service`.

| delivery_id | vendor_id | vendor_name | region | status | amount | service |
|---:|---:|---|---|---|---:|---|
| 301 | 1 | Atlas | West | delivered | 800 | standard |
| 302 | 1 | Atlas | West | pending | 2200 | express |
| 303 | 2 | Birch | North | delivered | 1700 | standard |
| 304 | 3 | Coral | West | delivered | 1900 | express |
| 305 | 3 | Coral | West | delivered | 400 | standard |
| 306 | 4 | Drift | South | delivered | NULL | express |
| 307 | 5 | Ember | North | failed | 3000 | express |
| 308 | 6 | Fern | West | delivered | 1200 | standard |
| 309 | 7 | Grove | South | delivered | 1400 | express |
| NULL | NULL | Haven | East | NULL | NULL | NULL |

**Review:** Correct foundational LEFT JOIN. Ten result rows: Atlas and Coral occur twice because each has two delivery records; Haven is preserved without any delivery and receives NULL for each `d.` field, including `d.vendor_id`. The vendor ID in the left table for Haven remains 8 but is not selected. Drift has an actual delivery with a NULL amount, unlike Haven's entirely absent delivery. Without ORDER BY, the observed sequence is not guaranteed. This is an exploratory step, **not** the final anti-join answer.

**Next learner task:** Explain Step 2 reasoning only; no new SQL clauses or reference solution should be supplied before the independent attempt. Question 8 is not yet solved; closing commits pending.


## Step 2 — Learner's qualifying-delivery LEFT JOIN

**Learner's exact submitted SQLite (verbatim):**

```sql
select d.delivery_id	, d.vendor_id,	v.vendor_name,	v.region, d.status,	d.amount,	d.service
from vendors as v
left join deliveries as d on v.vendor_id=d.vendor_id and d.status='delivered' and d.amount > 1000 and (v.region = 'West' or d.service='express')
```

**Executed in SQLite against the Q8 eight-vendor/nine-delivery fixture.** Status: **successful**, 8 rows, 7 columns, with no explicit ordering guarantee.

| delivery_id | vendor_id | vendor_name | region | status | amount | service |
|---:|---:|---|---|---|---:|---|
| NULL | NULL | Atlas | West | NULL | NULL | NULL |
| NULL | NULL | Birch | North | NULL | NULL | NULL |
| 304 | 3 | Coral | West | delivered | 1900 | express |
| NULL | NULL | Drift | South | NULL | NULL | NULL |
| NULL | NULL | Ember | North | NULL | NULL | NULL |
| 308 | 6 | Fern | West | delivered | 1200 | standard |
| 309 | 7 | Grove | South | delivered | 1400 | express |
| NULL | NULL | Haven | East | NULL | NULL | NULL |

**Interpretation:** The ON clause matches only delivered, amount > 1000, and (West vendor OR express service). Atlas, Birch, Drift, Ember and Haven remain from the left table without qualifying matches. Coral, Fern and Grove each have a qualifying match. The SELECT uses `d.vendor_id`, so unmatched vendor ID values show NULL although their `v.vendor_id` values exist. The previous unfiltered join returned 10 rows; this query returns 8. The record displays one row for each vendor in this fixture, but more than one qualifying delivery per vendor could produce multiple joined rows.

**Expected final Q8 output (unchanged; not this intermediate result):**

| vendor_id | vendor_name | region |
|---:|---|---|
| 1 | Atlas | West |
| 2 | Birch | North |
| 4 | Drift | South |
| 5 | Ember | North |
| 8 | Haven | East |

**Student status:** Correct intermediate JOIN filter. Final selection, exactly three columns, and explicit sorting still pending. **Do not reveal next SQL clause**; request learner's Step 3 reasoning only. No Q8 closing/mastery credit.


## Step 3 — Learner independently filters LEFT JOIN to unmatched qualifying deliveries

**Exact learner SQLite submission (verbatim):**

```sql
select d.delivery_id	, d.vendor_id,	v.vendor_name,	v.region, d.status,	d.amount,	d.service
from vendors as v
left join deliveries as d on v.vendor_id=d.vendor_id and d.status='delivered' and d.amount > 1000 and (v.region = 'West' or d.service='express')
where d.vendor_id is null
```

**Executed in Python's actual SQLite runtime against Q8's original 8 vendors / 9 deliveries sample fixture.** No SQLite errors.

**Actual output:** 5 rows and 7 columns:

| delivery_id | vendor_id | vendor_name | region | status | amount | service |
|---:|---:|---|---|---|---|---|
| NULL | NULL | Atlas | West | NULL | NULL | NULL |
| NULL | NULL | Birch | North | NULL | NULL | NULL |
| NULL | NULL | Drift | South | NULL | NULL | NULL |
| NULL | NULL | Ember | North | NULL | NULL | NULL |
| NULL | NULL | Haven | East | NULL | NULL | NULL |

**Expected final output:** 5 rows and exactly 3 columns:

| vendor_id | vendor_name | region |
|---:|---|---|
| 1 | Atlas | West |
| 2 | Birch | North |
| 4 | Drift | South |
| 5 | Ember | North |
| 8 | Haven | East |

**Review of student's approach:** Correctly identifies all five vendors without qualifying deliveries. The ON clause restricts delivery matches to delivered, amount > 1000, and (West region OR express service); the WHERE null-check retains those without matching qualifying deliveries. Coral/Fern/Grove excluded; Atlas/Birch/Drift/Ember/Haven included. **Not yet the full final solution:** the query selects seven columns instead of three; its selected `d.vendor_id` is NULL for every unmatched vendor rather than the true vendor ID from the left table; and no explicit ORDER BY guarantees vendor order. Do not label mastered or completed. **Next:** Learner's Step 4 reasoning about closing the gap to required output; then an independently authored final query, run/review, reference walk-through and closing commits in both repositories. No final-answer code revealed.


## Step 4 — Learner's first final-shaped query (executed; correction needed)

**Learner's exact submitted SQLite query (verbatim):**

```sql
select d.vendor_id,	v.vendor_name,	v.region
from vendors as v
left join deliveries as d on v.vendor_id=d.vendor_id and d.status='delivered' and d.amount > 1000 and (v.region = 'West' or d.service='express')
where d.vendor_id is null
order by d.vendor_id asc
```

**SQLite execution:** successful using the Q8 fixture; returned 5 rows / 3 columns.

**Actual output:**

| vendor_id | vendor_name | region |
|---|---|---|
| NULL | Atlas | West |
| NULL | Birch | North |
| NULL | Drift | South |
| NULL | Ember | North |
| NULL | Haven | East |

**Expected final output:**

| vendor_id | vendor_name | region |
|---:|---|---|
| 1 | Atlas | West |
| 2 | Birch | North |
| 4 | Drift | South |
| 5 | Ember | North |
| 8 | Haven | East |

**Review:** Correct five vendor names, correct three-column shape and valid anti-join matching logic. Wrong vendor ID values because `SELECT d.vendor_id` selects the same right-side field required to be NULL by `WHERE d.vendor_id IS NULL`. `ORDER BY d.vendor_id` orders by an all-NULL key and therefore does not ensure ascending real vendor IDs. Learner must independently repair displayed ID source and sorting expression before the final answer can be verified. Do not reveal complete reference SQL yet. **Status:** Final attempt needs independent correction; Q8 remains in progress.


## Step 5 — Independently corrected final SQLite submission (VERIFIED)

**Learner's final submission preserved verbatim:**

```sql
select v.vendor_id, v.vendor_name, v.region
from vendors as v
left join deliveries as d on v.vendor_id=d.vendor_id and d.status='delivered' and d.amount > 1000 and (v.region = 'West' or d.service='express')
where d.vendor_id is null
order by v.vendor_id asc
```

**Actual execution:** Ran this exact SQL using Python's `sqlite3` in-memory SQLite engine against the original Q8 fixture containing eight vendor rows and nine delivery rows. Execution succeeded without error.

**Actual SQLite output (five rows, three columns):**

| vendor_id | vendor_name | region |
|---:|---|---|
| 1 | Atlas | West |
| 2 | Birch | North |
| 4 | Drift | South |
| 5 | Ember | North |
| 8 | Haven | East |

**Expected output:** Exactly the five rows above, with the three columns in the displayed order.

**Verification:**
- Correct five vendor IDs, names and regions: **PASS**.
- Correct column names and order (`vendor_id`, `vendor_name`, `region`): **PASS**.
- Exactly five rows, no duplicates: **PASS**.
- Explicit ascending vendor-ID sorting: **PASS**.
- Includes no-delivery Haven and other nonqualifying vendors; excludes Coral, Fern and Grove: **PASS**.
- Final JOIN-based SQLite diagnostic requirement: **PASS**.

**Independent debugging history:** Student initially used ambiguous `vendor_id`, then an extraneous trailing comma, later correct ON predicates, correct right-side anti-match test, and finally independently changed the SELECT/ORDER BY from `d.vendor_id` (all NULL) to `v.vendor_id`. Their final corrected submission is genuinely their own and was verified, **not a first-try correct answer**.

**Explanation of correction:** The unmatched right-side `d.vendor_id` must be NULL for every retained vendor, while `v.vendor_id` from the left preserved vendor row contains the vendor's true ID. Sorting on `v.vendor_id` establishes the requested order.

**Reference solution status:** No separate assistant-provided reference has been presented yet. A SQL Server/T-SQL conversion is not executed or student-authored. An authentic third-party official solution is not applicable because Q8 is tutor-created.

**Optional learner-identified new learning:** Pending Yes/No capture and learner's exact wording.  
**Mastery:** Independent successful correction on this fixture; transfer to new cases untested.  
**PNP source credit:** 0; this is a tutor-authored diagnostic.  
**Question closing checkpoint:** Pending optional insight capture and full review. This is an intermediate evidence archive, not the formal question-closing commit.

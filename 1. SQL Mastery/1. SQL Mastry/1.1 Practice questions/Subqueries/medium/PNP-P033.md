# PNP P033 — Products that have never been ordered

**Topic** Subqueries · **Difficulty** ![MEDIUM](../../../_badges/medium.svg)

[Original PNP question](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P033.%20Products%20that%20have%20never%20been%20ordered.md#question-and-image) · [PDF source](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/Updated_100_SQL_Interview_Questions.pdf), Q33, pp. 56–58.

## Question

**Table colors** · 🟦 `Products` · 🟩 `OrderDetails`

**Business scenario.** The merchandising team pays for shelf space in the warehouse and wants to delist products that have never sold. Before anything is removed from the catalogue, they want the list of products with zero order lines in the entire history. A product that appeared in even one order line, in any quantity, is not on the list.

**Task.** Return every product in Products that does not appear in any row of OrderDetails. Sort by CategoryID, then ProductID.

### Required output columns

One result row represents a product that has never appeared in an order line. Return the five columns in this order.

| # | Output column | Source | Requirement for this product row | Example |
| ---: | --- | --- | --- | --- |
| 1 | `ProductID` | 🟦 `Products.ProductID` | Identifier of the catalogue product being checked for any order-line appearance. | 🟦 2 |
| 2 | `Product` | 🟦 `Products.Product` | Product name belonging to that catalogue ID. | 🟦 Cup |
| 3 | `Brand` | 🟦 `Products.Brand` | Brand recorded for that product. | 🟦 Home |
| 4 | `CategoryID` | 🟦 `Products.CategoryID` | Category to which the product belongs; used in the requested ascending sort. | 🟦 20 |
| 5 | `Sale_Price` | 🟦 `Products.Sale_Price` | Stored sale price of the product. | 🟦 10 |

**Row eligibility and ordering.** Include a product only when no row in 🟩 `OrderDetails` has its `ProductID`. Even one order line disqualifies it, regardless of quantity. Sort by `CategoryID` ascending, then `ProductID` ascending.

### Practice example · Sample input

**Sample table key · display order:** 🟦 `Products` · 🟩 `OrderDetails`

*The source specifies output columns but no sample input rows. These are illustrative practice data.*

**🟦 Products**

| 🟦 ProductID | 🟦 Product | 🟦 Brand | 🟦 CategoryID | 🟦 Sale_Price |
| ---: | --- | --- | ---: | ---: |
| 🟦 1 | Pen | Nova | 10 | 5 |
| 🟦 2 | Cup | Home | 20 | 10 |

**🟩 OrderDetails**

| 🟩 OrderDetailID | 🟩 OrderID | 🟩 ProductID |
| ---: | ---: | ---: |
| 🟩 10 | 🟩 100 | 🟩 1 |

### Expected output

| 🟦 ProductID | 🟦 Product | 🟦 Brand | 🟦 CategoryID | 🟦 Sale_Price |
| ---: | --- | --- | ---: | ---: |
| 🟦 2 | 🟦 Cup | 🟦 Home | 🟦 20 | 🟦 10 |

### How the sample produces this output

🟦 Pen (ProductID 1) appears in 🟩 OrderDetails row 10, so it is excluded. 🟦 Cup (ProductID 2) has no matching order-detail row, so it qualifies. The result contains one product.

## Step 1 · Your approach before writing SQL

1. What does one output row represent, and which five columns should it contain?
2. Which table should supply the products being evaluated? Which table tells us whether a product has ever been ordered?
3. How would you test whether a product has no matching order-detail row?
4. Why does even one order line disqualify a product, regardless of quantity?
5. How would you apply the requested ordering?
6. Trace Pen and Cup through your proposed logic and explain why only Cup remains.

## Agreed approach

1. Keep `Products` as the driving (left) table because every catalogue product must be considered, including products with no order history.
2. LEFT JOIN `OrderDetails` using `Products.ProductID = OrderDetails.ProductID`.
3. A product with no matching order-detail row receives NULLs in the right-side columns.
4. Filter those unmatched rows with `OD.OrderDetailID IS NULL`. `OrderDetailID` is a non-null identifier for an actual order-detail row.
5. Return the five requested columns from `Products` and sort by `CategoryID` ascending, then `ProductID` ascending.

**Pattern:** LEFT ANTI JOIN — preserve left-side rows that have no match on the right.

## My solution — SQLite

**Final learner solution.** Sample-checked on 24 November 2026 using the illustrative Example 3 below.

```sql
SELECT
    P.ProductID,
    P.Product,
    P.Brand,
    P.CategoryID,
    P.Sale_Price
FROM Products P
LEFT JOIN OrderDetails OD
    ON P.ProductID = OD.ProductID
WHERE OD.OrderDetailID IS NULL
ORDER BY
    P.CategoryID ASC,
    P.ProductID ASC;
```

### Sample verification

**Practice example 3 · Products**

| 🟦 ProductID | 🟦 Product | 🟦 Brand | 🟦 CategoryID | 🟦 Sale_Price |
|---:|---|---|---:|---:|
| 201 | SQL Basics | TechBooks | 10 | 450 |
| 202 | Python Guide | CodePress | 10 | 600 |
| 203 | Data Science | LearnHub | 10 | 800 |
| 204 | Cloud Computing | TechBooks | 20 | 900 |
| 205 | Linux Essentials | CodePress | 20 | 550 |
| 206 | System Design | LearnHub | 20 | 750 |

**Practice example 3 · OrderDetails**

| 🟩 OrderDetailID | 🟩 OrderID | 🟩 ProductID |
|---:|---:|---:|
| 1 | 5001 | 201 |
| 2 | 5001 | 203 |
| 3 | 5002 | 204 |
| 4 | 5003 | 201 |
| 5 | 5004 | 206 |

**Expected and verified output**

| 🟦 ProductID | 🟦 Product | 🟦 Brand | 🟦 CategoryID | 🟦 Sale_Price |
|---:|---|---|---:|---:|
| 202 | Python Guide | CodePress | 10 | 600 |
| 205 | Linux Essentials | CodePress | 20 | 550 |

**Checks performed**

- Product 201 has two matching order-detail rows. It is excluded; duplicate matches do not make it eligible.
- Products 203, 204 and 206 each have at least one match and are excluded.
- Products 202 and 205 have no matching order-detail row and are retained.
- The output contains exactly the five requested columns.
- Sorting is CategoryID ascending, then ProductID ascending.
- No `DISTINCT` is required: the `IS NULL` filter removes every matched row, and unmatched left-side product rows occur once.

## My solution — SQL Server

Pending. Adapt and verify the saved SQLite query separately.

## Official solution

Pending source extraction and comparison. Preserve the supplied answer verbatim when added.

## Visual walkthrough

Pending. The learner's final query and sample output are saved. Add the interactive staged walkthrough and SVG after building and checking the question-specific fixture against this exact query.

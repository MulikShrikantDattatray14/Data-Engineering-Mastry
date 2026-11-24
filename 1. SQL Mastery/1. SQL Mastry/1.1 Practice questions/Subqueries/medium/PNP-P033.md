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

# PNP P032 — Products priced above their category average

**Topic** Subqueries · **Difficulty** ![MEDIUM](../../../_badges/medium.svg)

> **Spoiler caution:** The linked original PNP Markdown includes solution sections. Keep the source page closed until after your independent attempt; this practice page itself stays solution-free.

[Original PNP question](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P032.%20Products%20priced%20above%20their%20category%20average.md#question-and-image) · [PDF source](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/Updated_100_SQL_Interview_Questions.pdf), Q32, pp. 54–56.

## Question

**Table colors** · 🟦 `Products`

**Business scenario.** The pricing team is reviewing products that sit at the expensive end of their own category before a festive sale. A product at 600 is cheap in cookware and expensive in snacks, so a single catalogue-wide cut-off is useless. The festive sale is in Beverages first, so they start there, and they want each product compared only with the products in its own category.

**Task.** For the Beverages category ( CategoryID 5009), return every product whose Sale_Price is strictly greater than the average Sale_Price of all products with the same CategoryID . Show the category average next to it. Sort by CategoryID , then price, highest first.

### Required output columns

One result row represents one qualifying Beverages product. All five columns are supplied by, or calculated from, 🟦 `Products`. Return them in this order.

| # | Output column | Source | Requirement for this product row | Example |
| ---: | --- | --- | --- |
| 1 | `ProductID` | 🟦 `Products.ProductID` | Return the identifier of the individual product whose price qualifies. It identifies the item in the pricing review. | 3 |
| 2 | `Product` | 🟦 `Products.Product` | Return the catalogue name belonging to that same product ID. | Juice |
| 3 | `CategoryID` | 🟦 `Products.CategoryID` | Return the product’s category ID. The report is limited to Beverages, so every output row carries 5009. | 5009 |
| 4 | `Sale_Price` | 🟦 `Products.Sale_Price` | Return the individual product’s stored sale price. It qualifies only when strictly greater than the unrounded average for its own category. Equality does not qualify. | 300 |
| 5 | `category_avg_price` | 🟦 Calculated from `Products.Sale_Price` within the same `CategoryID` | Show the mean of all known sale prices in the product’s category, including this product. Below-average and equal-priced products contribute too. Display the benchmark to two decimals. | 200.00 |

**Row eligibility and ordering.** Compare using the unrounded category average. A product with a missing sale price cannot pass the comparison. Sort by `CategoryID` ascending, then `Sale_Price` descending. The prompt gives no further rule for equal prices.

### Practice example · Sample input

*The assignment supplies the output columns but no sample input table. These four rows are illustrative practice data, not an assignment-provided example.*

**🟦 `Products`**

| 🟦 ProductID | 🟦 Product | 🟦 CategoryID | 🟦 Sale_Price |
| --- | --- | --- | --- |
| 1 | Tea | 5009 | 100 |
| 2 | Coffee | 5009 | 200 |
| 3 | Juice | 5009 | 300 |
| 4 | Bread | 5010 | 500 |

### Expected output

| 🟦 ProductID | 🟦 Product | 🟦 CategoryID | 🟦 Sale_Price | 🟦 category_avg_price |
| --- | --- | --- | --- | --- |
| 3 | Juice | 5009 | 300 | 200.00 |

[View the source-colored sample tables](../../assets/question-samples/p032.svg)

[Open the sample SVG full size](../../assets/question-samples/p032.svg?raw=1)

### How the sample produces this output

For 🟦 Beverages (CategoryID 5009), Tea, Coffee and Juice contribute **100 + 200 + 300 = 600**. Dividing by the three known prices gives **600 ÷ 3 = 200.00**. Tea at 100 is below the average. Coffee at 200 equals it, so it does not meet the strict greater-than condition. Juice (ProductID 3) at 300 is above 200 and is the only qualifying row. Bread (ID 4) is in CategoryID 5010 and does not contribute to this category’s average or appear in the Beverages report.

## Step 1 · Your approach before writing SQL

1. What does one output row represent, and which columns should it contain?
2. Which table supplies the required fields, and why would you start from it? Would you need any other table?
3. Which products should contribute to the category average, and how would you compare an individual product with that benchmark?
4. How would you handle a product whose price equals the average or is missing?
5. How would you apply the Beverages restriction and the requested ordering?
6. Trace Tea, Coffee and Juice through your proposed steps, then explain why Bread is treated separately.


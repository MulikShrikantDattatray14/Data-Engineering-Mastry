# PNP P032 â€” Products priced above their category average

**Topic** Subqueries Â· **Difficulty** ![MEDIUM](../../../_badges/medium.svg)

> **Spoiler caution:** The linked original PNP Markdown includes solution sections. Keep the source page closed until after your independent attempt; this practice page itself stays solution-free.

[Original PNP question](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P032.%20Products%20priced%20above%20their%20category%20average.md#question-and-image) Â· [PDF source](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/Updated_100_SQL_Interview_Questions.pdf), Q32, pp. 54â€“56.

## Question

**Table colors** Â· ðŸŸ¦ `Products`

**Business scenario.** The pricing team is reviewing products that sit at the expensive end of their own category before a festive sale. A product at 600 is cheap in cookware and expensive in snacks, so a single catalogue-wide cut-off is useless. The festive sale is in Beverages first, so they start there, and they want each product compared only with the products in its own category.

**Task.** For the Beverages category ( CategoryID 5009), return every product whose Sale_Price is strictly greater than the average Sale_Price of all products with the same CategoryID . Show the category average next to it. Sort by CategoryID , then price, highest first.

### Required output columns

One result row represents one qualifying Beverages product. All five columns are supplied by, or calculated from, ðŸŸ¦ `Products`. Return them in this order.

| # | Output column | Source | Requirement for this product row | Example |
| ---: | --- | --- | --- | --- |
| 1 | `ProductID` | ðŸŸ¦ `Products.ProductID` | Return the identifier of the individual product whose price qualifies. It identifies the item in the pricing review. | í ½ 3 |
| 2 | `Product` | ðŸŸ¦ `Products.Product` | Return the catalogue name belonging to that same product ID. | í ½ Juice |
| 3 | `CategoryID` | ðŸŸ¦ `Products.CategoryID` | Return the productâ€™s category ID. The report is limited to Beverages, so every output row carries 5009. | í ½ 5009 |
| 4 | `Sale_Price` | ðŸŸ¦ `Products.Sale_Price` | Return the individual productâ€™s stored sale price. It qualifies only when strictly greater than the unrounded average for its own category. Equality does not qualify. | í ½ 300 |
| 5 | `category_avg_price` | ðŸŸ¦ Calculated from `Products.Sale_Price` within the same `CategoryID` | Show the mean of all known sale prices in the productâ€™s category, including this product. Below-average and equal-priced products contribute too. Display the benchmark to two decimals. | í ½ 200.00 |

**Row eligibility and ordering.** Compare using the unrounded category average. A product with a missing sale price cannot pass the comparison. Sort by `CategoryID` ascending, then `Sale_Price` descending. The prompt gives no further rule for equal prices.

### Practice example Â· Sample input

**Sample table key Â· display order:** ðŸŸ¦ `Products`

*The assignment supplies the output columns but no sample input table. These four rows are illustrative practice data, not an assignment-provided example.*

**ðŸŸ¦ `Products`**

| ðŸŸ¦ ProductID | ðŸŸ¦ Product | ðŸŸ¦ CategoryID | ðŸŸ¦ Sale_Price |
| --- | --- | --- | --- |
| í ½ 1 | í ½ Tea | í ½ 5009 | í ½ 100 |
| í ½ 2 | í ½ Coffee | í ½ 5009 | í ½ 200 |
| í ½ 3 | í ½ Juice | í ½ 5009 | í ½ 300 |
| í ½ 4 | í ½ Bread | í ½ 5010 | í ½ 500 |

### Expected output

| ðŸŸ¦ ProductID | ðŸŸ¦ Product | ðŸŸ¦ CategoryID | ðŸŸ¦ Sale_Price | ðŸŸ¦ category_avg_price |
| --- | --- | --- | --- | --- |
| í ½ 3 | í ½ Juice | í ½ 5009 | í ½ 300 | í ½ 200.00 |

[View the source-colored sample tables](../../assets/question-samples/p032.svg)

[Open the sample SVG full size](../../assets/question-samples/p032.svg?raw=1)

### How the sample produces this output

For ðŸŸ¦ Beverages (CategoryID ðŸŸ¦ 5009), Tea, Coffee and Juice contribute **ðŸŸ¦ 100 + ðŸŸ¦ 200 + ðŸŸ¦ 300 = ðŸŸ¦ 600**. Dividing by the three known prices gives **ðŸŸ¦ 600 Ã· 3 = ðŸŸ¦ 200.00**. Tea at ðŸŸ¦ 100 is below the average. Coffee at ðŸŸ¦ 200 equals it, so it does not meet the strict greater-than condition. Juice (ProductID ðŸŸ¦ 3) at ðŸŸ¦ 300 is above ðŸŸ¦ 200 and is the only qualifying row. Bread (ID ðŸŸ¦ 4) is in CategoryID ðŸŸ¦ 5010 and does not contribute to this categoryâ€™s average or appear in the Beverages report.

## Step 1 Â· Your approach before writing SQL

1. What does one output row represent, and which columns should it contain?
2. Which table supplies the required fields, and why would you start from it? Would you need any other table?
3. Which products should contribute to the category average, and how would you compare an individual product with that benchmark?
4. How would you handle a product whose price equals the average or is missing?
5. How would you apply the Beverages restriction and the requested ordering?
6. Trace Tea, Coffee and Juice through your proposed steps, then explain why Bread is treated separately.


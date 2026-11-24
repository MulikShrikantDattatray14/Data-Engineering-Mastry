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
| ---: | --- | --- | --- | --- |
| 1 | `ProductID` | 🟦 `Products.ProductID` | Return the identifier of the individual product whose price qualifies. It identifies the item in the pricing review. | 🟦 3 |
| 2 | `Product` | 🟦 `Products.Product` | Return the catalogue name belonging to that same product ID. | 🟦 Juice |
| 3 | `CategoryID` | 🟦 `Products.CategoryID` | Return the product’s category ID. The report is limited to Beverages, so every output row carries 5009. | 🟦 5009 |
| 4 | `Sale_Price` | 🟦 `Products.Sale_Price` | Return the individual product’s stored sale price. It qualifies only when strictly greater than the unrounded average for its own category. Equality does not qualify. | 🟦 300 |
| 5 | `category_avg_price` | 🟦 Calculated from `Products.Sale_Price` within the same `CategoryID` | Show the mean of all known sale prices in the product’s category, including this product. Below-average and equal-priced products contribute too. Display the benchmark to two decimals. | 🟦 200.00 |

**Row eligibility and ordering.** Compare using the unrounded category average. A product with a missing sale price cannot pass the comparison. Sort by `CategoryID` ascending, then `Sale_Price` descending. The prompt gives no further rule for equal prices.

### Practice example · Sample input

**Sample table key · display order:** 🟦 `Products`

*The assignment supplies the output columns but no sample input table. These four rows are illustrative practice data, not an assignment-provided example.*

**🟦 `Products`**

| 🟦 ProductID | 🟦 Product | 🟦 CategoryID | 🟦 Sale_Price |
| --- | --- | --- | --- |
| 🟦 1 | 🟦 Tea | 🟦 5009 | 🟦 100 |
| 🟦 2 | 🟦 Coffee | 🟦 5009 | 🟦 200 |
| 🟦 3 | 🟦 Juice | 🟦 5009 | 🟦 300 |
| 🟦 4 | 🟦 Bread | 🟦 5010 | 🟦 500 |

### Expected output

| 🟦 ProductID | 🟦 Product | 🟦 CategoryID | 🟦 Sale_Price | 🟦 category_avg_price |
| --- | --- | --- | --- | --- |
| 🟦 3 | 🟦 Juice | 🟦 5009 | 🟦 300 | 🟦 200.00 |

![P032 source-colored practice inputs and expected output](../../assets/question-samples/p032.svg)

[Open the sample SVG full size](../../assets/question-samples/p032.svg?raw=1)

**Precision note.** The required output specification asks for the category average to display to two decimal places. The locked learner query deliberately leaves the benchmark unrounded, so SQLite returns `200.0` for this fixture; the expected display is `200.00`. The original course answer rounds the displayed benchmark to two decimals. The learner query is preserved verbatim.

### How the sample produces this output

For 🟦 Beverages (CategoryID 🟦 5009), Tea, Coffee and Juice contribute **🟦 100 + 🟦 200 + 🟦 300 = 🟦 600**. Dividing by the three known prices gives **🟦 600 ÷ 3 = 🟦 200.00**. Tea at 🟦 100 is below the average. Coffee at 🟦 200 equals it, so it does not meet the strict greater-than condition. Juice (ProductID 🟦 3) at 🟦 300 is above 🟦 200 and is the only qualifying row. Bread (ID 🟦 4) is in CategoryID 🟦 5010 and does not contribute to this category’s average or appear in the Beverages report.

## Step 1 · Your approach before writing SQL

1. What does one output row represent, and which columns should it contain?
2. Which table supplies the required fields, and why would you start from it? Would you need any other table?
3. Which products should contribute to the category average, and how would you compare an individual product with that benchmark?
4. How would you handle a product whose price equals the average or is missing?
5. How would you apply the Beverages restriction and the requested ordering?
6. Trace Tea, Coffee and Juice through your proposed steps, then explain why Bread is treated separately.

## My solution — SQLite

**Final learner-selected solution.** Checked against the illustrative sample in SQLite on 24 November 2026. It returns Juice (ProductID 3) at 300, with a category average of 200.0.

```sql
WITH required_table AS (
    SELECT
        ProductID,
        Product,
        CategoryID,
        Sale_Price
    FROM Products
    WHERE CategoryID = 5009
),

avg_sale_price AS (
    SELECT
        AVG(Sale_Price) AS category_avg_price
    FROM required_table
)

SELECT
    ProductID,
    Product,
    CategoryID,
    Sale_Price,
    (SELECT category_avg_price FROM avg_sale_price) AS category_avg_price
FROM required_table
WHERE Sale_Price > (
    SELECT category_avg_price
    FROM avg_sale_price
)
ORDER BY
    CategoryID ASC,
    Sale_Price DESC;
```

**Why no `GROUP BY` is needed:** `required_table` retains one row per product. `avg_sale_price` calculates one benchmark for the filtered category. The outer query compares each product row against that scalar benchmark, so individual product rows are not collapsed.

The benchmark includes all known sale prices in CategoryID 5009, including products that do not qualify. Equality is excluded by the strict `>` comparison.

## My solution — SQL Server

**Learner-query SQL Server adaptation.** This keeps the selected CTE structure and the unrounded benchmark. The source dataset defines `Sale_Price` as `NUMERIC(10,2)`, so SQL Server's `AVG` returns a decimal result.

```sql
WITH required_table AS (
    SELECT
        ProductID,
        Product,
        CategoryID,
        Sale_Price
    FROM Products
    WHERE CategoryID = 5009
),

avg_sale_price AS (
    SELECT
        AVG(Sale_Price) AS category_avg_price
    FROM required_table
)

SELECT
    ProductID,
    Product,
    CategoryID,
    Sale_Price,
    (SELECT category_avg_price FROM avg_sale_price) AS category_avg_price
FROM required_table
WHERE Sale_Price > (
    SELECT category_avg_price
    FROM avg_sale_price
)
ORDER BY
    CategoryID ASC,
    Sale_Price DESC;
```

## Official solution

### Original course answer — PostgreSQL 16

Source: [`all_100_solutions.sql`, Q32, lines 395–409](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql#L395-L409). Preserved as supplied.

```sql
SELECT p.ProductID,
       p.Product,
       p.CategoryID,
       p.Sale_Price,
       ROUND((SELECT AVG(p2.Sale_Price)
              FROM Products AS p2
              WHERE p2.CategoryID = p.CategoryID), 2) AS category_avg_price
FROM Products AS p
WHERE p.CategoryID = 5009
  AND p.Sale_Price > (SELECT AVG(p2.Sale_Price)
                      FROM Products AS p2
                      WHERE p2.CategoryID = p.CategoryID)
ORDER BY p.CategoryID, p.Sale_Price DESC, p.ProductID;
```

### Official-answer SQLite adaptation

```sql
SELECT p.ProductID,
       p.Product,
       p.CategoryID,
       p.Sale_Price,
       ROUND((SELECT AVG(p2.Sale_Price)
              FROM Products AS p2
              WHERE p2.CategoryID = p.CategoryID), 2) AS category_avg_price
FROM Products AS p
WHERE p.CategoryID = 5009
  AND p.Sale_Price > (SELECT AVG(p2.Sale_Price)
                      FROM Products AS p2
                      WHERE p2.CategoryID = p.CategoryID)
ORDER BY p.CategoryID, p.Sale_Price DESC, p.ProductID;
```

### Official-answer SQL Server adaptation

```sql
SELECT p.ProductID,
       p.Product,
       p.CategoryID,
       p.Sale_Price,
       ROUND((SELECT AVG(p2.Sale_Price)
              FROM Products AS p2
              WHERE p2.CategoryID = p.CategoryID), 2) AS category_avg_price
FROM Products AS p
WHERE p.CategoryID = 5009
  AND p.Sale_Price > (SELECT AVG(p2.Sale_Price)
                      FROM Products AS p2
                      WHERE p2.CategoryID = p.CategoryID)
ORDER BY p.CategoryID, p.Sale_Price DESC, p.ProductID;
```

### Difference from the locked learner query

- The course answer uses correlated scalar subqueries; the learner uses `required_table` and `avg_sale_price` CTEs.
- The learner filters to CategoryID 5009 before calculating the average. That is equivalent for this report because it is restricted to Beverages; the benchmark still includes every known Beverages price before the above-average filter.
- The course answer rounds the displayed average to two decimals. The locked learner query returns the unrounded value.
- The course answer adds ProductID as a final tie-breaker. The prompt does not specify a tie-breaker after price, so the learner's ordering satisfies the stated requirement.

The learner-selected SQL is retained exactly; these differences are documented rather than silently normalised.


## Visual walkthrough

![PNP P032 — Products priced above their category average, from the Products source through the category benchmark and final comparison](../../assets/walkthroughs/p032.svg)

[Open the full-size walkthrough SVG](../../assets/walkthroughs/p032.svg?raw=1) · [Open Previous / Next walkthrough, stage 1](../../assets/steps/PNP-P032/01.md) · [Open the walkthrough fixture](../../assets/steps/PNP-P032/walkthrough.json)

### Written step-by-step explanation

1. **Start with `Products`.** It supplies every catalogue candidate and all requested output fields. The first CTE filters CategoryID 5009, taking the four input rows to three Beverages product rows. No other table is needed.
2. **Prepare `required_table`.** One CTE row represents one eligible product. Tea, Coffee and Juice remain; Bread is removed before the benchmark is calculated.
3. **Prepare `avg_sale_price`.** The aggregate CTE returns one row representing the category-wide benchmark: (100 + 200 + 300) ÷ 3 = 200.00. Below-average and equal-priced products still contribute.
4. **Return to the outer query.** The outer query starts from the three rows in `required_table`, not from the one-row average CTE. Its scalar subquery repeats the same benchmark beside each product; no join is necessary because this is one selected category and one scalar value.
5. **Apply the strict comparison and order.** Tea at 100 is below the benchmark; Coffee at 200 equals it and is excluded; Juice at 300 survives. The final query orders by CategoryID ascending and Sale_Price descending.

The final stage in the linked walkthrough reads the exact locked learner SQLite query and is checked against the expected output above.

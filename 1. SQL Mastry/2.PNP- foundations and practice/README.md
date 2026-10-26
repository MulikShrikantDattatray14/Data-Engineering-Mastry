# PNP — foundations and practice

This track has **205 distinct practice prompts**: 100 from the PrepNPlaced interview book, 100 from the advanced SQL volume, and five extra product-rating prompts in the bundle README. The ZIP includes a duplicate copy of the interview PDF, so that book is indexed once.

Open a topic's foundation note, then choose a question below. The practice files contain the original tasks and schemas; your solutions and the supplied official answers remain pending until you have completely solved each question. The [source materials](<Source Materials/README.md>) include the original books, dataset, and answer files.

The two books use different schemas and dialects: the PrepNPlaced interview book uses an eight-table PostgreSQL dataset; the advanced volume uses a seven-table MySQL example schema. The notes distinguish them.

## Quick jump

| Topic | Foundation notes | Questions |
|---|---|---:|
| [0. Dataset and SQL Basics](#0-dataset-and-sql-basics) | [Open foundation](<0. Dataset and SQL Basics/0. Foundation Notes.md>) | 3 |
| [1. Select and Filtering](#1-select-and-filtering) | [Open foundation](<1. Select and Filtering/0. Foundation Notes.md>) | 8 |
| [2. Joins](#2-joins) | [Open foundation](<2. Joins/0. Foundation Notes.md>) | 27 |
| [3. Aggregation and Pivoting](#3-aggregation-and-pivoting) | [Open foundation](<3. Aggregation and Pivoting/0. Foundation Notes.md>) | 34 |
| [4. Subqueries and Set Operations](#4-subqueries-and-set-operations) | [Open foundation](<4. Subqueries and Set Operations/0. Foundation Notes.md>) | 19 |
| [5. CTEs](#5-ctes) | [Open foundation](<5. CTEs/0. Foundation Notes.md>) | 7 |
| [6. Recursive CTEs](#6-recursive-ctes) | [Open foundation](<6. Recursive CTEs/0. Foundation Notes.md>) | 5 |
| [7. Window Functions](#7-window-functions) | [Open foundation](<7. Window Functions/0. Foundation Notes.md>) | 45 |
| [8. Gaps and Islands](#8-gaps-and-islands) | [Open foundation](<8. Gaps and Islands/0. Foundation Notes.md>) | 6 |
| [9. Data Quality and Deduplication](#9-data-quality-and-deduplication) | [Open foundation](<9. Data Quality and Deduplication/0. Foundation Notes.md>) | 17 |
| [10. NULL Logic](#10-null-logic) | [Open foundation](<10. NULL Logic/0. Foundation Notes.md>) | 7 |
| [11. Dates and Time](#11-dates-and-time) | [Open foundation](<11. Dates and Time/0. Foundation Notes.md>) | 16 |
| [12. Analytics and Performance](#12-analytics-and-performance) | [Open foundation](<12. Analytics and Performance/0. Foundation Notes.md>) | 11 |

## 0. Dataset and SQL Basics

[Foundation notes](<0. Dataset and SQL Basics/0. Foundation Notes.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q001 — Count employees per department, keeping departments that have none.](<0. Dataset and SQL Basics/A001. Count employees per department, keeping departments that have none.md>)
- [Advanced Q002 — Second highest salary, no LIMIT and no window function.](<0. Dataset and SQL Basics/A002. Second highest salary, no LIMIT and no window function.md>)
- [Advanced Q003 — Third highest distinct salary, ties collapsed.](<0. Dataset and SQL Basics/A003. Third highest distinct salary, ties collapsed.md>)

## 1. Select and Filtering

[Foundation notes](<1. Select and Filtering/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q001 — Brand directory](<1. Select and Filtering/P001. Brand directory.md>)
- [PNP Q002 — Ten highest-priced products](<1. Select and Filtering/P002. Ten highest-priced products.md>)
- [PNP Q003 — Customers in metro cities](<1. Select and Filtering/P003. Customers in metro cities.md>)
- [PNP Q004 — Customer emails that cannot be delivered](<1. Select and Filtering/P004. Customer emails that cannot be delivered.md>)
- [PNP Q005 — Orders placed in Q1 2025](<1. Select and Filtering/P005. Orders placed in Q1 2025.md>)
- [PNP Q007 — Discount amount and percentage per product](<1. Select and Filtering/P007. Discount amount and percentage per product.md>)
- [PNP Q008 — Price band labels](<1. Select and Filtering/P008. Price band labels.md>)
- [PNP Q023 — Chocolate or cookie products under 250, excluding sugar-free](<1. Select and Filtering/P023. Chocolate or cookie products under 250, excluding sugar-free.md>)

## 2. Joins

[Foundation notes](<2. Joins/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q015 — Product count for every category](<2. Joins/P015. Product count for every category.md>)
- [PNP Q016 — December 2025 orders with customer names](<2. Joins/P016. December 2025 orders with customer names.md>)
- [PNP Q017 — Orders with payment type and shipper](<2. Joins/P017. Orders with payment type and shipper.md>)
- [PNP Q018 — Customers with no order in the last 90 days](<2. Joins/P018. Customers with no order in the last 90 days.md>)
- [PNP Q019 — Units sold per product](<2. Joins/P019. Units sold per product.md>)
- [PNP Q026 — List-price value by category](<2. Joins/P026. List-price value by category.md>)
- [PNP Q027 — Average order value by customer state](<2. Joins/P027. Average order value by customer state.md>)
- [PNP Q029 — Order value and units by shipper without double counting](<2. Joins/P029. Order value and units by shipper without double counting.md>)
- [PNP Q038 — Products from inactive categories that still sold in the latest year](<2. Joins/P038. Products from inactive categories that still sold in the latest ye.md>)
- [PNP Q039 — Categories with no products, and categories with products but no sales](<2. Joins/P039. Categories with no products, and categories with products but no s.md>)
- [PNP Q046 — Same-brand products where one costs at least twice the other](<2. Joins/P046. Same-brand products where one costs at least twice the other.md>)
- [PNP Q053 — Thirty-day sign-up to purchase conversion by country](<2. Joins/P053. Thirty-day sign-up to purchase conversion by country.md>)
- [PNP Q070 — Sub-categories most often bought together](<2. Joins/P070. Sub-categories most often bought together.md>)
- [PNP Q077 — Single-source products and the value at risk](<2. Joins/P077. Single-source products and the value at risk.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q004 — List customers who have never placed an order.](<2. Joins/A004. List customers who have never placed an order.md>)
- [Advanced Q005 — Find delivered orders that have no payment row.](<2. Joins/A005. Find delivered orders that have no payment row.md>)
- [Advanced Q006 — MySQL has no FULL OUTER JOIN. Emulate one between customers and orders.](<2. Joins/A006. MySQL has no FULL OUTER JOIN. Emulate one between customers and or.md>)
- [Advanced Q007 — Product IDs that exist in products but were never ordered — set-operator version.](<2. Joins/A007. Product IDs that exist in products but were never ordered — set-op.md>)
- [Advanced Q008 — Build a complete date × category grid so empty combinations still appear.](<2. Joins/A008. Build a complete date × category grid so empty combinations still.md>)
- [Advanced Q009 — Bucket every product into a price band using a non-equi join.](<2. Joins/A009. Bucket every product into a price band using a non-equi join.md>)
- [Advanced Q010 — Find every employee who earns more than their own manager.](<2. Joins/A010. Find every employee who earns more than their own manager.md>)
- [Advanced Q011 — List all pairs of colleagues in the same department, without mirror duplicates.](<2. Joins/A011. List all pairs of colleagues in the same department, without mirro.md>)
- [Advanced Q012 — Managers with three or more direct reports.](<2. Joins/A012. Managers with three or more direct reports.md>)
- [Advanced Q013 — Customers who bought product 101 but never product 202.](<2. Joins/A013. Customers who bought product 101 but never product 202.md>)
- [Advanced Q014 — Employees who manage nobody (the leaves of the org tree).](<2. Joins/A014. Employees who manage nobody (the leaves of the org tree).md>)
- [Advanced Q015 — Show each employee next to their department average, without collapsing rows.](<2. Joins/A015. Show each employee next to their department average, without colla.md>)

### Bundle extras

- [Extra Q005 — Product ratings practice 5](<2. Joins/X005. Product ratings practice 5.md>)

## 3. Aggregation and Pivoting

[Foundation notes](<3. Aggregation and Pivoting/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q009 — Check how Active and Allowed are encoded](<3. Aggregation and Pivoting/P009. Check how Active and Allowed are encoded.md>)
- [PNP Q010 — Headline order KPIs](<3. Aggregation and Pivoting/P010. Headline order KPIs.md>)
- [PNP Q011 — How much of the catalogue has ever sold?](<3. Aggregation and Pivoting/P011. How much of the catalogue has ever sold.md>)
- [PNP Q012 — Price and discount statistics per category ID](<3. Aggregation and Pivoting/P012. Price and discount statistics per category ID.md>)
- [PNP Q013 — States with at least five customers](<3. Aggregation and Pivoting/P013. States with at least five customers.md>)
- [PNP Q014 — Orders per month in 2025](<3. Aggregation and Pivoting/P014. Orders per month in 2025.md>)
- [PNP Q021 — Top five customers by number of orders](<3. Aggregation and Pivoting/P021. Top five customers by number of orders.md>)
- [PNP Q022 — Orders with more than eight line items](<3. Aggregation and Pivoting/P022. Orders with more than eight line items.md>)
- [PNP Q025 — Customer sign-ups by year and quarter](<3. Aggregation and Pivoting/P025. Customer sign-ups by year and quarter.md>)
- [PNP Q035 — Late-delivery rate by shipper](<3. Aggregation and Pivoting/P035. Late-delivery rate by shipper.md>)
- [PNP Q036 — Payment method mix by month as columns](<3. Aggregation and Pivoting/P036. Payment method mix by month as columns.md>)
- [PNP Q047 — Brands with at least three products, and how much they sold](<3. Aggregation and Pivoting/P047. Brands with at least three products, and how much they sold.md>)
- [PNP Q048 — Do discounted products sell more?](<3. Aggregation and Pivoting/P048. Do discounted products sell more.md>)
- [PNP Q050 — Customers who buy across at least ten categories](<3. Aggregation and Pivoting/P050. Customers who buy across at least ten categories.md>)
- [PNP Q051 — Orders fulfilled by one supplier vs several](<3. Aggregation and Pivoting/P051. Orders fulfilled by one supplier vs several.md>)
- [PNP Q052 — Where shipping time goes: dispatch vs transit by shipper](<3. Aggregation and Pivoting/P052. Where shipping time goes dispatch vs transit by shipper.md>)
- [PNP Q054 — Weighted vs simple average discount by sub-category](<3. Aggregation and Pivoting/P054. Weighted vs simple average discount by sub-category.md>)
- [PNP Q055 — Category list-price value: latest year vs previous year](<3. Aggregation and Pivoting/P055. Category list-price value latest year vs previous year.md>)
- [PNP Q059 — Basket size by month](<3. Aggregation and Pivoting/P059. Basket size by month.md>)
- [PNP Q084 — Delivery time by state and shipper with subtotals](<3. Aggregation and Pivoting/P084. Delivery time by state and shipper with subtotals.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q016 — Departments where the average salary tops 50,000 and headcount is at least 5.](<3. Aggregation and Pivoting/A016. Departments where the average salary tops 50,000 and headcount is.md>)
- [Advanced Q017 — Revenue by product category, highest first.](<3. Aggregation and Pivoting/A017. Revenue by product category, highest first.md>)
- [Advanced Q018 — Monthly count of distinct buyers, cancelled orders excluded.](<3. Aggregation and Pivoting/A018. Monthly count of distinct buyers, cancelled orders excluded.md>)
- [Advanced Q019 — Category revenue with a grand-total row at the bottom.](<3. Aggregation and Pivoting/A019. Category revenue with a grand-total row at the bottom.md>)
- [Advanced Q020 — Average order value per customer, only for customers with 3+ orders.](<3. Aggregation and Pivoting/A020. Average order value per customer, only for customers with 3+ order.md>)
- [Advanced Q021 — Which weekday brings in the most orders?](<3. Aggregation and Pivoting/A021. Which weekday brings in the most orders.md>)
- [Advanced Q022 — Turn order status into columns: one row per customer, counts per status.](<3. Aggregation and Pivoting/A022. Turn order status into columns one row per customer, counts per st.md>)
- [Advanced Q023 — Revenue by category with 2025 and 2026 side by side.](<3. Aggregation and Pivoting/A023. Revenue by category with 2025 and 2026 side by side.md>)
- [Advanced Q024 — Cancellation rate per customer as a percentage.](<3. Aggregation and Pivoting/A024. Cancellation rate per customer as a percentage.md>)
- [Advanced Q025 — Customers who ordered in both 2025 and 2026.](<3. Aggregation and Pivoting/A025. Customers who ordered in both 2025 and 2026.md>)
- [Advanced Q026 — Unpivot: turn three metric columns of a summary table into label/value rows.](<3. Aggregation and Pivoting/A026. Unpivot turn three metric columns of a summary table into labelval.md>)
- [Advanced Q027 — First order, last order and active lifespan per customer.](<3. Aggregation and Pivoting/A027. First order, last order and active lifespan per customer.md>)

### Bundle extras

- [Extra Q001 — Product ratings practice 1](<3. Aggregation and Pivoting/X001. Product ratings practice 1.md>)
- [Extra Q002 — Product ratings practice 2](<3. Aggregation and Pivoting/X002. Product ratings practice 2.md>)

## 4. Subqueries and Set Operations

[Foundation notes](<4. Subqueries and Set Operations/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q028 — Payment mix: share of orders and value](<4. Subqueries and Set Operations/P028. Payment mix share of orders and value.md>)
- [PNP Q031 — Customers who spend more than the average customer](<4. Subqueries and Set Operations/P031. Customers who spend more than the average customer.md>)
- [PNP Q032 — Products priced above their category average](<4. Subqueries and Set Operations/P032. Products priced above their category average.md>)
- [PNP Q033 — Products that have never been ordered](<4. Subqueries and Set Operations/P033. Products that have never been ordered.md>)
- [PNP Q056 — Customers who ordered last year but not this year](<4. Subqueries and Set Operations/P056. Customers who ordered last year but not this year.md>)
- [PNP Q057 — One contact directory for suppliers and shippers](<4. Subqueries and Set Operations/P057. One contact directory for suppliers and shippers.md>)
- [PNP Q080 — Sub-category repurchase rate within 90 days](<4. Subqueries and Set Operations/P080. Sub-category repurchase rate within 90 days.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q028 — Employees paid above the average of their own department.](<4. Subqueries and Set Operations/A028. Employees paid above the average of their own department.md>)
- [Advanced Q029 — The most recent order for every customer, ties allowed.](<4. Subqueries and Set Operations/A029. The most recent order for every customer, ties allowed.md>)
- [Advanced Q030 — Products priced above their category average.](<4. Subqueries and Set Operations/A030. Products priced above their category average.md>)
- [Advanced Q031 — Customers whose lifetime spend beats the average lifetime spend.](<4. Subqueries and Set Operations/A031. Customers whose lifetime spend beats the average lifetime spend.md>)
- [Advanced Q032 — Each category and its single best-selling product name.](<4. Subqueries and Set Operations/A032. Each category and its single best-selling product name.md>)
- [Advanced Q033 — Orders larger than that customer's own average order.](<4. Subqueries and Set Operations/A033. Orders larger than that customer's own average order.md>)
- [Advanced Q034 — Customers who placed at least one order — write it three ways.](<4. Subqueries and Set Operations/A034. Customers who placed at least one order — write it three ways.md>)
- [Advanced Q035 — Why does this return zero rows, and how do you fix it?](<4. Subqueries and Set Operations/A035. Why does this return zero rows, and how do you fix it.md>)
- [Advanced Q036 — Departments with at least one employee earning above 100,000.](<4. Subqueries and Set Operations/A036. Departments with at least one employee earning above 100,000.md>)
- [Advanced Q037 — Orders that contain any Electronics product.](<4. Subqueries and Set Operations/A037. Orders that contain any Electronics product.md>)
- [Advanced Q038 — Customers who have bought every product in the Audio category (relational division).](<4. Subqueries and Set Operations/A038. Customers who have bought every product in the Audio category (rel.md>)
- [Advanced Q039 — Products bought by more than 10 distinct customers.](<4. Subqueries and Set Operations/A039. Products bought by more than 10 distinct customers.md>)

## 5. CTEs

[Foundation notes](<5. CTEs/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q030 — Repeat versus one-time customers](<5. CTEs/P030. Repeat versus one-time customers.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q040 — Rewrite the "spend above average spend" query with a CTE defined once.](<5. CTEs/A040. Rewrite the spend above average spend query with a CTE defined onc.md>)
- [Advanced Q041 — Chain two CTEs: monthly revenue, then only the months above the yearly average.](<5. CTEs/A041. Chain two CTEs monthly revenue, then only the months above the yea.md>)
- [Advanced Q042 — Compare every department average against the company average in one pass.](<5. CTEs/A042. Compare every department average against the company average in on.md>)
- [Advanced Q043 — Filter on a window function result — why WHERE fails and what to do.](<5. CTEs/A043. Filter on a window function result — why WHERE fails and what to d.md>)
- [Advanced Q044 — Build a clean order spine, then attach item counts to it.](<5. CTEs/A044. Build a clean order spine, then attach item counts to it.md>)
- [Advanced Q045 — Deduplicate first, aggregate second — in one readable statement.](<5. CTEs/A045. Deduplicate first, aggregate second — in one readable statement.md>)

## 6. Recursive CTEs

[Foundation notes](<6. Recursive CTEs/0. Foundation Notes.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q046 — Generate every date in January 2026, with no calendar table.](<6. Recursive CTEs/A046. Generate every date in January 2026, with no calendar table.md>)
- [Advanced Q047 — Every employee under manager 5, at any depth, with their level.](<6. Recursive CTEs/A047. Every employee under manager 5, at any depth, with their level.md>)
- [Advanced Q048 — Print the full reporting path of every employee up to the top.](<6. Recursive CTEs/A048. Print the full reporting path of every employee up to the top.md>)
- [Advanced Q049 — How deep does the org chart go?](<6. Recursive CTEs/A049. How deep does the org chart go.md>)
- [Advanced Q050 — Split 'a,b,c' into one row per value.](<6. Recursive CTEs/A050. Split 'a,b,c' into one row per value.md>)

## 7. Window Functions

[Foundation notes](<7. Window Functions/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q034 — Each supplier's share of units supplied](<7. Window Functions/P034. Each supplier's share of units supplied.md>)
- [PNP Q041 — Most expensive product in each category](<7. Window Functions/P041. Most expensive product in each category.md>)
- [PNP Q042 — RANK vs DENSE_RANK vs ROW_NUMBER on order counts](<7. Window Functions/P042. RANK vs DENSE_RANK vs ROW_NUMBER on order counts.md>)
- [PNP Q043 — Month-to-date order value for the latest three months](<7. Window Functions/P043. Month-to-date order value for the latest three months.md>)
- [PNP Q044 — Month-over-month growth in order value](<7. Window Functions/P044. Month-over-month growth in order value.md>)
- [PNP Q045 — Typical gap between a customer's orders](<7. Window Functions/P045. Typical gap between a customer's orders.md>)
- [PNP Q049 — Top three products by units in each category](<7. Window Functions/P049. Top three products by units in each category.md>)
- [PNP Q058 — Each customer's latest order](<7. Window Functions/P058. Each customer's latest order.md>)
- [PNP Q060 — Sub-category share of its category](<7. Window Functions/P060. Sub-category share of its category.md>)
- [PNP Q068 — Second-highest spender in each state, counting delivered orders only](<7. Window Functions/P068. Second-highest spender in each state, counting delivered orders on.md>)
- [PNP Q074 — Customers whose latest order is below their own average](<7. Window Functions/P074. Customers whose latest order is below their own average.md>)
- [PNP Q078 — Expensive within their sub-category but selling below its median](<7. Window Functions/P078. Expensive within their sub-category but selling below its median.md>)
- [PNP Q079 — At which order does a customer cross 10,000 in spend?](<7. Window Functions/P079. At which order does a customer cross 10,000 in spend.md>)
- [PNP Q082 — Each customer's favourite category](<7. Window Functions/P082. Each customer's favourite category.md>)
- [PNP Q097 — What do customers buy on their second order?](<7. Window Functions/P097. What do customers buy on their second order.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q051 — Show ROW_NUMBER, RANK and DENSE_RANK together and explain the difference.](<7. Window Functions/A051. Show ROW_NUMBER, RANK and DENSE_RANK together and explain the diff.md>)
- [Advanced Q052 — Rank employees by salary inside each department.](<7. Window Functions/A052. Rank employees by salary inside each department.md>)
- [Advanced Q053 — The highest-paid employee per department, ties broken by earliest hire date.](<7. Window Functions/A053. The highest-paid employee per department, ties broken by earliest.md>)
- [Advanced Q054 — Percentile position of each salary within the company.](<7. Window Functions/A054. Percentile position of each salary within the company.md>)
- [Advanced Q055 — Share of employees earning at or below each salary.](<7. Window Functions/A055. Share of employees earning at or below each salary.md>)
- [Advanced Q056 — Rank categories by revenue — a window on top of an aggregate.](<7. Window Functions/A056. Rank categories by revenue — a window on top of an aggregate.md>)
- [Advanced Q057 — Month-over-month revenue change in absolute terms.](<7. Window Functions/A057. Month-over-month revenue change in absolute terms.md>)
- [Advanced Q058 — Same thing as a growth percentage, safe against a zero denominator.](<7. Window Functions/A058. Same thing as a growth percentage, safe against a zero denominator.md>)
- [Advanced Q059 — Days between each customer's consecutive orders.](<7. Window Functions/A059. Days between each customer's consecutive orders.md>)
- [Advanced Q060 — Next order date per customer, with a placeholder when there isn't one.](<7. Window Functions/A060. Next order date per customer, with a placeholder when there isn't.md>)
- [Advanced Q061 — Customers whose most recent order was smaller than the one before it.](<7. Window Functions/A061. Customers whose most recent order was smaller than the one before.md>)
- [Advanced Q062 — Compare every month against the same month last year.](<7. Window Functions/A062. Compare every month against the same month last year.md>)
- [Advanced Q063 — Running total of revenue by date.](<7. Window Functions/A063. Running total of revenue by date.md>)
- [Advanced Q064 — Running total of spend per customer, oldest order first.](<7. Window Functions/A064. Running total of spend per customer, oldest order first.md>)
- [Advanced Q065 — Seven-day moving average of daily revenue, calendar-correct.](<7. Window Functions/A065. Seven-day moving average of daily revenue, calendar-correct.md>)
- [Advanced Q066 — Show the difference between ROWS and RANGE when values tie.](<7. Window Functions/A066. Show the difference between ROWS and RANGE when values tie.md>)
- [Advanced Q067 — Running total that resets at the start of every month.](<7. Window Functions/A067. Running total that resets at the start of every month.md>)
- [Advanced Q068 — Each order against the biggest order seen so far for that customer.](<7. Window Functions/A068. Each order against the biggest order seen so far for that customer.md>)
- [Advanced Q069 — Split customers into four spend quartiles.](<7. Window Functions/A069. Split customers into four spend quartiles.md>)
- [Advanced Q070 — Each category's share of total revenue, as a percentage.](<7. Window Functions/A070. Each category's share of total revenue, as a percentage.md>)
- [Advanced Q071 — Every employee's salary as a share of their department's payroll.](<7. Window Functions/A071. Every employee's salary as a share of their department's payroll.md>)
- [Advanced Q072 — Median salary — MySQL has no MEDIAN function.](<7. Window Functions/A072. Median salary — MySQL has no MEDIAN function.md>)
- [Advanced Q073 — The top 20% of customers by spend.](<7. Window Functions/A073. The top 20% of customers by spend.md>)
- [Advanced Q074 — Top 3 products by revenue inside each category.](<7. Window Functions/A074. Top 3 products by revenue inside each category.md>)
- [Advanced Q075 — The latest payment row for every order.](<7. Window Functions/A075. The latest payment row for every order.md>)
- [Advanced Q076 — Top 2 customers by spend in each city.](<7. Window Functions/A076. Top 2 customers by spend in each city.md>)
- [Advanced Q077 — Each customer's second most recent order.](<7. Window Functions/A077. Each customer's second most recent order.md>)
- [Advanced Q078 — Top 3 salaries per department without any window function.](<7. Window Functions/A078. Top 3 salaries per department without any window function.md>)
- [Advanced Q079 — Most recent order per customer, returning the whole row, no CTE.](<7. Window Functions/A079. Most recent order per customer, returning the whole row, no CTE.md>)

### Bundle extras

- [Extra Q003 — Product ratings practice 3](<7. Window Functions/X003. Product ratings practice 3.md>)

## 8. Gaps and Islands

[Foundation notes](<8. Gaps and Islands/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q065 — Longest run of consecutive months with an order](<8. Gaps and Islands/P065. Longest run of consecutive months with an order.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q080 — Find the missing order_id ranges in the sequence.](<8. Gaps and Islands/A080. Find the missing order_id ranges in the sequence.md>)
- [Advanced Q081 — Collapse each customer's consecutive ordering days into start/end ranges.](<8. Gaps and Islands/A081. Collapse each customer's consecutive ordering days into startend r.md>)
- [Advanced Q082 — Longest ordering streak per customer, in days.](<8. Gaps and Islands/A082. Longest ordering streak per customer, in days.md>)
- [Advanced Q083 — Customers with three or more consecutive months of orders.](<8. Gaps and Islands/A083. Customers with three or more consecutive months of orders.md>)
- [Advanced Q084 — Collapse a list of consecutive IDs into compact ranges.](<8. Gaps and Islands/A084. Collapse a list of consecutive IDs into compact ranges.md>)

## 9. Data Quality and Deduplication

[Foundation notes](<9. Data Quality and Deduplication/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q037 — Prove no order was paid with a method that is not allowed](<9. Data Quality and Deduplication/P037. Prove no order was paid with a method that is not allowed.md>)
- [PNP Q071 — Deduplicate customer accounts by email](<9. Data Quality and Deduplication/P071. Deduplicate customer accounts by email.md>)
- [PNP Q072 — Same product on several lines of one order: split or duplicate?](<9. Data Quality and Deduplication/P072. Same product on several lines of one order split or duplicate.md>)
- [PNP Q086 — Reconcile order headers with order lines](<9. Data Quality and Deduplication/P086. Reconcile order headers with order lines.md>)
- [PNP Q087 — Referential integrity audit across all seven relationships](<9. Data Quality and Deduplication/P087. Referential integrity audit across all seven relationships.md>)
- [PNP Q088 — Date validity audit](<9. Data Quality and Deduplication/P088. Date validity audit.md>)
- [PNP Q089 — Incremental load with a watermark and lookback](<9. Data Quality and Deduplication/P089. Incremental load with a watermark and lookback.md>)
- [PNP Q090 — Column-by-column completeness profile of Orders](<9. Data Quality and Deduplication/P090. Column-by-column completeness profile of Orders.md>)
- [PNP Q092 — How duplicate accounts distort the repeat-customer rate](<9. Data Quality and Deduplication/P092. How duplicate accounts distort the repeat-customer rate.md>)
- [PNP Q093 — Possible duplicate order submissions](<9. Data Quality and Deduplication/P093. Possible duplicate order submissions.md>)
- [PNP Q095 — Debug a revenue-by-category query that gives wrong numbers](<9. Data Quality and Deduplication/P095. Debug a revenue-by-category query that gives wrong numbers.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q085 — Find every duplicated (order_id, paid_at) combination in payments.](<9. Data Quality and Deduplication/A085. Find every duplicated (order_id, paid_at) combination in payments.md>)
- [Advanced Q086 — Return one clean row per key, keeping the earliest payment.](<9. Data Quality and Deduplication/A086. Return one clean row per key, keeping the earliest payment.md>)
- [Advanced Q087 — Actually delete the duplicates, keeping the lowest payment_id.](<9. Data Quality and Deduplication/A087. Actually delete the duplicates, keeping the lowest payment_id.md>)
- [Advanced Q088 — Why does this fail, and how do you make MySQL accept it?](<9. Data Quality and Deduplication/A088. Why does this fail, and how do you make MySQL accept it.md>)
- [Advanced Q089 — How many duplicate groups exist, and how many extra rows do they add?](<9. Data Quality and Deduplication/A089. How many duplicate groups exist, and how many extra rows do they a.md>)
- [Advanced Q090 — Keep only the newest record per natural key when the table has a version column.](<9. Data Quality and Deduplication/A090. Keep only the newest record per natural key when the table has a v.md>)

## 10. NULL Logic

[Foundation notes](<10. NULL Logic/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q006 — Most expensive products that are never discounted](<10. NULL Logic/P006. Most expensive products that are never discounted.md>)
- [PNP Q024 — Suppliers outside India or with no email](<10. NULL Logic/P024. Suppliers outside India or with no email.md>)

### Advanced SQL 100 Query Questions

- [Advanced Q091 — Three counts, three different answers. Explain each.](<10. NULL Logic/A091. Three counts, three different answers. Explain each.md>)
- [Advanced Q092 — Sort salaries descending but push NULLs to the bottom — MySQL has no NULLS LAST.](<10. NULL Logic/A092. Sort salaries descending but push NULLs to the bottom — MySQL has.md>)
- [Advanced Q093 — Show a usable contact value from the first non-null of three columns.](<10. NULL Logic/A093. Show a usable contact value from the first non-null of three colum.md>)
- [Advanced Q094 — Join two tables on a column that contains NULLs and still match them.](<10. NULL Logic/A094. Join two tables on a column that contains NULLs and still match th.md>)
- [Advanced Q095 — Why does AVG disagree with SUM / COUNT(*), and how do you make them agree?](<10. NULL Logic/A095. Why does AVG disagree with SUM  COUNT(), and how do you make them.md>)

## 11. Dates and Time

[Foundation notes](<11. Dates and Time/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q020 — Days to ship and days to deliver](<11. Dates and Time/P020. Days to ship and days to deliver.md>)
- [PNP Q040 — Days from sign-up to first order](<11. Dates and Time/P040. Days from sign-up to first order.md>)
- [PNP Q061 — Monthly cohort retention](<11. Dates and Time/P061. Monthly cohort retention.md>)
- [PNP Q064 — Three-month moving average of order value, with no missing months](<11. Dates and Time/P064. Three-month moving average of order value, with no missing months.md>)
- [PNP Q066 — How fast do customers come back for a second order?](<11. Dates and Time/P066. How fast do customers come back for a second order.md>)
- [PNP Q069 — Customers whose spend grew every active quarter of the latest year](<11. Dates and Time/P069. Customers whose spend grew every active quarter of the latest year.md>)
- [PNP Q075 — Rolling 28-day active customers, week by week](<11. Dates and Time/P075. Rolling 28-day active customers, week by week.md>)
- [PNP Q076 — Order value from new vs returning customers by month](<11. Dates and Time/P076. Order value from new vs returning customers by month.md>)
- [PNP Q081 — Year-to-date vs same period last year](<11. Dates and Time/P081. Year-to-date vs same period last year.md>)
- [PNP Q085 — Win-back customers returning after 180+ days](<11. Dates and Time/P085. Win-back customers returning after 180+ days.md>)
- [PNP Q091 — Cumulative value per customer by cohort (LTV curve)](<11. Dates and Time/P091. Cumulative value per customer by cohort (LTV curve).md>)

### Advanced SQL 100 Query Questions

- [Advanced Q096 — Orders from the last 30 days, written so the index still gets used.](<11. Dates and Time/A096. Orders from the last 30 days, written so the index still gets used.md>)
- [Advanced Q097 — First and last day of each order's month.](<11. Dates and Time/A097. First and last day of each order's month.md>)
- [Advanced Q098 — Weekly order counts, weeks starting on Monday.](<11. Dates and Time/A098. Weekly order counts, weeks starting on Monday.md>)
- [Advanced Q099 — Customers who placed their first order within 7 days of signing up.](<11. Dates and Time/A099. Customers who placed their first order within 7 days of signing up.md>)
- [Advanced Q100 — Month-one retention: customers who ordered again in the month after their first.](<11. Dates and Time/A100. Month-one retention customers who ordered again in the month after.md>)

## 12. Analytics and Performance

[Foundation notes](<12. Analytics and Performance/0. Foundation Notes.md>)

### 100 SQL Interview Questions

- [PNP Q062 — Which products make up 80% of list-price value (Pareto)](<12. Analytics and Performance/P062. Which products make up 80% of list-price value (Pareto).md>)
- [PNP Q063 — RFM segmentation](<12. Analytics and Performance/P063. RFM segmentation.md>)
- [PNP Q067 — Median vs mean order value by payment type](<12. Analytics and Performance/P067. Median vs mean order value by payment type.md>)
- [PNP Q073 — Category share of list-price value: latest vs previous year](<12. Analytics and Performance/P073. Category share of list-price value latest vs previous year.md>)
- [PNP Q083 — Underperforming sub-categories in the last six months](<12. Analytics and Performance/P083. Underperforming sub-categories in the last six months.md>)
- [PNP Q094 — Supplier concentration per category (HHI)](<12. Analytics and Performance/P094. Supplier concentration per category (HHI).md>)
- [PNP Q096 — Make a slow order report sargable and index it](<12. Analytics and Performance/P096. Make a slow order report sargable and index it.md>)
- [PNP Q098 — Category association rules: support, confidence, lift](<12. Analytics and Performance/P098. Category association rules support, confidence, lift.md>)
- [PNP Q099 — Flag unusual weeks in order volume](<12. Analytics and Performance/P099. Flag unusual weeks in order volume.md>)
- [PNP Q100 — Monthly KPI scorecard with month-over-month change](<12. Analytics and Performance/P100. Monthly KPI scorecard with month-over-month change.md>)

### Bundle extras

- [Extra Q004 — Product ratings practice 4](<12. Analytics and Performance/X004. Product ratings practice 4.md>)

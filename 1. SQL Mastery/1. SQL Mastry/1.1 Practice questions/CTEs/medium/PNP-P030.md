# PNP P030 — Repeat versus one-time customers

**Topic** CTEs · **Difficulty** ![MEDIUM](../../../_badges/medium.svg) · **Restart practice** 2026-11-19

## Question

**Table colors** · 🟦 `Orders`

**Business scenario.** The growth team is deciding whether next quarter's budget goes to acquiring new buyers or to a second-order nudge campaign. The first number they ask for is how many customers ever came back. A repeat customer here means a customer with two or more orders in the whole history; a one-time customer has exactly one.

**Task.** Classify every customer who has placed at least one order as One-time (exactly one order) or Repeat (two or more). Return the number of customers in each group and the group's share of all ordering customers.

[PNP source question](../../../2.PNP-%20foundations%20and%20practice/5.%20CTEs/P030.%20Repeat%20versus%20one-time%20customers.md#question-and-image)

### Required output columns

One output row represents one customer type represented among customers who placed orders.

| Output column | Source or calculation | Meaning and applicable rules | Example value |
| --- | --- | --- | --- |
| `customer_type` | 🟦 `Orders` | `One-time` for exactly one order or `Repeat` for two or more. | One-time |
| `customers` | 🟦 `Orders` | Number of customers in that group. | 2 |
| `pct_of_customers` | 🟦 `Orders` | Percentage of all ordering customers in that group, to two decimal places. | 66.67 |

### Practice example · Sample input

*The PNP material specifies the output columns. These four orders illustrate them.*

**🟦 `Orders`**

| 🟦 OrderID | 🟦 CustomerID |
|---|---|
| 🟦 1 | 🟦 10 |
| 🟦 2 | 🟦 20 |
| 🟦 3 | 🟦 20 |
| 🟦 4 | 🟦 30 |

### Expected output

| 🟦 customer_type | 🟦 customers | 🟦 pct_of_customers |
|---|---|---|
| 🟦 One-time | 🟦 2 | 🟦 66.67 |
| 🟦 Repeat | 🟦 1 | 🟦 33.33 |

![PNP P030 sample inputs and expected output](../../assets/question-samples/p030.svg)
[View sample inputs and output with colored cells](../../assets/question-samples/p030.svg?raw=1)

### How the sample produces this output

🟦 Customers **🟦 10** and **🟦 30** appear on orders **🟦 1** and **🟦 4**, respectively. Each ordered once. They give `🟦 One-time` **🟦 2** of the **🟦 3** ordering customers, or `🟦 2 ÷ 🟦 3 × 100 = 🟦 66.67%`.

🟦 Customer **🟦 20** placed orders **🟦 2** and **🟦 3**. That customer contributes once to `🟦 Repeat`, giving **🟦 1** of the **🟦 3** ordering customers, or `🟦 1 ÷ 🟦 3 × 100 = 🟦 33.33%`. The two groups account for all three customers.

## Step 1 · Your approach before writing SQL

1. What does one row in the final report represent?
2. Which table goes in `FROM`? If you would add others, what comes second, third and so on, and why?
3. Which join type and matching columns would you choose at each step, if any?
4. In plain English, how would you decide which customers belong to each group and what the percentage measures?

## Final learner solution — SQLite

Shri’s revision filters orders with a missing `CustomerID` before `GROUP BY CustomerID`. The CTE then represents identified customers, and `COUNT(total_orders)` counts one numeric value per customer in each final group.

```sql
WITH customer_order_counts AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS total_orders,
        CASE
            WHEN COUNT(OrderID) = 1 THEN 'One-time'
            ELSE 'Repeat'
        END AS customer_type
    FROM Orders
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
)

SELECT
    customer_type,
    COUNT(total_orders) AS customers,
    ROUND(
        COUNT(total_orders) * 100.0
        / (SELECT COUNT(*) FROM customer_order_counts),
        2
    ) AS pct_of_customers
FROM customer_order_counts
GROUP BY customer_type
ORDER BY customer_type;
```

### Review of the agreed approach

**10/10 after revision.** Use 🟦 `Orders` because it supplies both order and customer IDs. Count each identified customer’s orders, classify the customer, then count customers in each class. The denominator reads every customer row from the CTE. The report has one row for each populated class.

## Visual walkthrough

[Open the Previous / Next walkthrough](../../assets/steps/PNP-P030/01.md)

Customer **20** is the row to follow. The triangle points to its two orders, its single CTE row and its contribution to the `Repeat` result. The final panel adds one hypothetical order to explain the approved filter.

![Four Orders rows become three identified customers and two customer groups. A separate check follows an order with a missing customer ID.](../../assets/walkthroughs/p030.svg)

[Open the full-size walkthrough](../../assets/walkthroughs/p030.svg?raw=1)

## Step-by-step walkthrough

### 1. Which orders supply the report?

Each row in 🟦 `Orders` represents an order. `OrderID` identifies the order and `CustomerID` identifies its customer. Those two fields supply both grouping stages. The filter applies to the input orders before the first group forms.

```sql
SELECT OrderID, CustomerID
FROM Orders
WHERE CustomerID IS NOT NULL
ORDER BY OrderID;
```

**Eligible 🟦 `Orders` rows**

| 🟦 `OrderID` | 🟦 `CustomerID` |
| ---: | ---: |
| 🟦 1 | 🟦 10 |
| 🟦 2 | 🟦 20 |
| 🟦 3 | 🟦 20 |
| 🟦 4 | 🟦 30 |

All four sample orders have customer IDs. Orders **2** and **3** both belong to customer **20**.

### 2. How many orders did each customer place?

Group the four eligible orders by 🟦 `CustomerID`. Within each group, count its order IDs. The result has one row for each of the three identified customers.

```sql
SELECT CustomerID, COUNT(OrderID) AS total_orders
FROM Orders
WHERE CustomerID IS NOT NULL
GROUP BY CustomerID
ORDER BY CustomerID;
```

**Order count by identified customer**

| 🟦 `CustomerID` | 🟦 `total_orders` |
| ---: | ---: |
| 🟦 10 | 🟦 1 |
| 🟦 20 | 🟦 2 |
| 🟦 30 | 🟦 1 |

Customer **20** has orders **2** and **3**, so `COUNT(OrderID)` returns **2**. Customers **10** and **30** each have one order.

### 3. Which label does the CTE give each customer?

The `CASE` expression uses each group’s order count. A value of **1** gives `One-time`. Two or more gives `Repeat`. The final learner query calculates the count and the label in the same CTE.

```sql
WITH customer_order_counts AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS total_orders,
        CASE
            WHEN COUNT(OrderID) = 1 THEN 'One-time'
            ELSE 'Repeat'
        END AS customer_type
    FROM Orders
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
)
SELECT CustomerID, total_orders, customer_type
FROM customer_order_counts
ORDER BY CustomerID;
```

**🟦 `customer_order_counts`**

| 🟦 `CustomerID` | 🟦 `total_orders` | 🟦 `customer_type` |
| ---: | ---: | --- |
| 🟦 10 | 🟦 1 | 🟦 One-time |
| 🟦 20 | 🟦 2 | 🟦 Repeat |
| 🟦 30 | 🟦 1 | 🟦 One-time |

Each customer now has one row with both `total_orders` and `customer_type`. A customer with five orders would also occupy one `Repeat` row.

### 4. What does the main query count?

The outer `FROM customer_order_counts` reads customer rows. This preview places members of the same group together so you can follow the inputs to `COUNT(total_orders)`.

```sql
WITH customer_order_counts AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS total_orders,
        CASE
            WHEN COUNT(OrderID) = 1 THEN 'One-time'
            ELSE 'Repeat'
        END AS customer_type
    FROM Orders
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
)
SELECT customer_type, CustomerID, total_orders
FROM customer_order_counts
ORDER BY customer_type, CustomerID;
```

**Members of each customer group**

| 🟦 `customer_type` | 🟦 `CustomerID` | 🟦 `total_orders` |
| --- | ---: | ---: |
| 🟦 One-time | 🟦 10 | 🟦 1 |
| 🟦 One-time | 🟦 30 | 🟦 1 |
| 🟦 Repeat | 🟦 20 | 🟦 2 |

The `One-time` group contains customers **10** and **30**, with one numeric `total_orders` value on each row. The `Repeat` group contains customer **20**. Their value is **2**, and `COUNT(total_orders)` counts that value once.

After the same `WITH` clause, the grouped preview is

```sql
SELECT customer_type, COUNT(total_orders) AS customers
FROM customer_order_counts
GROUP BY customer_type
ORDER BY customer_type;
```

**Counts by customer type**

| 🟦 `customer_type` | 🟦 `customers` |
| --- | ---: |
| 🟦 One-time | 🟦 2 |
| 🟦 Repeat | 🟦 1 |

### 5. Which rows belong in the denominator?

The scalar subquery reads every row of `customer_order_counts`. It supplies the same denominator for both result rows. This is the denominator query after the same `WITH` clause.

```sql
SELECT COUNT(*) AS ordering_customers
FROM customer_order_counts;
```

| 🟦 `ordering_customers` |
| ---: |
| 🟦 3 |

For `One-time`, 🟦 **2 ÷ 3 × 100 = 66.67%**. For `Repeat`, 🟦 **1 ÷ 3 × 100 = 33.33%**. The decimal literal `100.0` preserves the fractional share, `ROUND(..., 2)` rounds the display value and `ORDER BY customer_type` puts `One-time` first.

```sql
SELECT
    customer_type,
    COUNT(total_orders) AS customers,
    ROUND(
        COUNT(total_orders) * 100.0
        / (SELECT COUNT(*) FROM customer_order_counts),
        2
    ) AS pct_of_customers
FROM customer_order_counts
GROUP BY customer_type
ORDER BY customer_type;
```

**Verified final report**

| 🟦 `customer_type` | 🟦 `customers` | 🟦 `pct_of_customers` |
| --- | ---: | ---: |
| 🟦 One-time | 🟦 2 | 🟦 66.67 |
| 🟦 Repeat | 🟦 1 | 🟦 33.33 |

The two group counts reconcile to all three customers. The shares in this sample sum to **100.00%**.

## Missing customer ID check

Add one hypothetical order to the four-order practice sample. Order **5** has a `NULL` customer ID. Grouping first gives this order its own group, an order count of **1** and the label `One-time`. That adds an unidentified customer to the numerator and denominator. The filter removes the row before either count.

| 🟦 `customer_type` | Submitted customer count | Submitted share | Revised customer count | Revised share |
|---|---:|---:|---:|---:|
| 🟦 One-time | 3 | 75.00% | 2 | 66.67% |
| 🟦 Repeat | 1 | 25.00% | 1 | 33.33% |

The course schema declares `CustomerID` as a nullable integer. Two orders with missing IDs would also form one group and give the unfiltered draft an extra repeat customer. [Orders table definition](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/data/load_dataset_v2.sql#L88-L97)

## Learner solution — SQL Server

The leading statement terminator lets the CTE follow another statement in a SQL Server batch.

<details>
<summary>Show the learner query for SQL Server</summary>

```sql
;WITH customer_order_counts AS (
    SELECT
        CustomerID,
        COUNT(OrderID) AS total_orders,
        CASE
            WHEN COUNT(OrderID) = 1 THEN 'One-time'
            ELSE 'Repeat'
        END AS customer_type
    FROM Orders
    WHERE CustomerID IS NOT NULL
    GROUP BY CustomerID
)

SELECT
    customer_type,
    COUNT(total_orders) AS customers,
    ROUND(
        COUNT(total_orders) * 100.0
        / (SELECT COUNT(*) FROM customer_order_counts),
        2
    ) AS pct_of_customers
FROM customer_order_counts
GROUP BY customer_type
ORDER BY customer_type;
```

</details>

## Official solution

The course counts eligible orders per customer in its CTE and assigns the label in the outer query. Its `COUNT(*)` and Shri’s `COUNT(total_orders)` count the same customer rows. The course guards the divisor with `NULLIF`. With empty input, the final grouping emits zero rows. [PNP Q30, published SQL](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql#L353-L368)

### As supplied — PostgreSQL

```sql
WITH orders_per_customer AS (
    SELECT o.CustomerID,
           COUNT(*) AS orders_placed
    FROM Orders AS o
    WHERE o.CustomerID IS NOT NULL
    GROUP BY o.CustomerID
)
SELECT CASE WHEN opc.orders_placed = 1 THEN 'One-time'
            ELSE 'Repeat' END                                            AS customer_type,
       COUNT(*)                                                          AS customers,
       ROUND(100.0 * COUNT(*)
             / NULLIF((SELECT COUNT(*) FROM orders_per_customer), 0), 2) AS pct_of_customers
FROM orders_per_customer AS opc
GROUP BY CASE WHEN opc.orders_placed = 1 THEN 'One-time' ELSE 'Repeat' END
ORDER BY customer_type;
```

### Official answer — SQLite

The supplied query executes directly in SQLite.

<details>
<summary>Show the verified SQLite reference</summary>

```sql
WITH orders_per_customer AS (
    SELECT o.CustomerID,
           COUNT(*) AS orders_placed
    FROM Orders AS o
    WHERE o.CustomerID IS NOT NULL
    GROUP BY o.CustomerID
)
SELECT CASE WHEN opc.orders_placed = 1 THEN 'One-time'
            ELSE 'Repeat' END                                            AS customer_type,
       COUNT(*)                                                          AS customers,
       ROUND(100.0 * COUNT(*)
             / NULLIF((SELECT COUNT(*) FROM orders_per_customer), 0), 2) AS pct_of_customers
FROM orders_per_customer AS opc
GROUP BY CASE WHEN opc.orders_placed = 1 THEN 'One-time' ELSE 'Repeat' END
ORDER BY customer_type;
```

</details>

### Official answer — SQL Server

<details>
<summary>Show the reference for SQL Server</summary>

```sql
;WITH orders_per_customer AS (
    SELECT o.CustomerID,
           COUNT(*) AS orders_placed
    FROM Orders AS o
    WHERE o.CustomerID IS NOT NULL
    GROUP BY o.CustomerID
)
SELECT CASE WHEN opc.orders_placed = 1 THEN 'One-time'
            ELSE 'Repeat' END                                            AS customer_type,
       COUNT(*)                                                          AS customers,
       ROUND(100.0 * COUNT(*)
             / NULLIF((SELECT COUNT(*) FROM orders_per_customer), 0), 2) AS pct_of_customers
FROM orders_per_customer AS opc
GROUP BY CASE WHEN opc.orders_placed = 1 THEN 'One-time' ELSE 'Repeat' END
ORDER BY customer_type;
```

</details>

## Verification

SQLite reproduced the two practice rows shown above. The revised learner query and course query also agreed with an independent count on **39 inputs**, including empty data, missing IDs, a single populated class, customers with different repeat counts, mixed groups, and the full course file. The SQL Server forms use the same expressions. Native execution was verified in SQLite.

The commerce file contains **46,438 orders** from **4,427 identified customers**. Every order in this file has a customer ID, so the added-order example above is a separate check. [PNP Orders data](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/data/Orders.csv)

| 🟦 `customer_type` | 🟦 `customers` | 🟦 `pct_of_customers` |
| --- | ---: | ---: |
| 🟦 One-time | 🟦 702 | 🟦 15.86 |
| 🟦 Repeat | 🟦 3725 | 🟦 84.14 |

[Practice index](../../README.md)

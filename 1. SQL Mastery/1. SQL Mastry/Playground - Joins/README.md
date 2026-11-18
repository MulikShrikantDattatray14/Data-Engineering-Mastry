# Playground - Joins

[**Play the SQL join trainer**](https://htmlpreview.github.io/?https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/Playground%20-%20Joins/index.html) · [Download the offline version](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/raw/refs/heads/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/Playground%20-%20Joins/index.html)

Choose the table for `FROM`, then try a table and a join type at each step. **Tables & rules** lets you set up one to five tables with your own names, keys, and missing-match rules. **Solution & row trace** shows the SQL and lets you remove matches to see which rows survive.

## Try a round here on GitHub

Report on orders with a registered customer. Keep a qualifying order even when its shipper, unit total, or customer region is missing.

| Tables | Matching key |
|---|---|
| `Orders` and `Customers` | `CustomerID` |
| `Orders` and `Shippers` | `ShipperID` |
| `Orders` and `units_per_order` | `OrderID` |
| `Customers` and `Regions` | `RegionID` |

**Your two questions**

1. Which table would you put in `FROM`, and in what order would you add the other four?
2. For each added table, which join would you use, and what should happen if there is no match?

<details>
<summary>Check the table order</summary>

Start with `Orders`. It already has the keys for `Customers`, `Shippers`, and `units_per_order`. To add `Regions`, first bring in `Customers`, which supplies `RegionID`.

</details>

<details>
<summary>Reveal one valid join plan</summary>

```sql
FROM Orders
INNER JOIN Customers
    ON Orders.CustomerID = Customers.CustomerID
LEFT JOIN Regions
    ON Customers.RegionID = Regions.RegionID
LEFT JOIN Shippers
    ON Orders.ShipperID = Shippers.ShipperID
LEFT JOIN units_per_order
    ON Orders.OrderID = units_per_order.OrderID
```

The customer match qualifies the order. Each later lookup keeps the order when its match is missing. The grouped `units_per_order` input has at most one row per order.

</details>

<details>
<summary>Predict what happens to an order with a registered customer and no detail lines</summary>

The order survives all four joins. Its units column is `NULL` after the last join. In a report that counts missing detail lines as zero units, use `COALESCE(units_per_order.units_shipped, 0)`.

</details>

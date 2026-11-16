# PNP P013 — States with at least five customers

**Topic:** Sorting and Grouping  
**Difficulty:** Easy

## Question

From `Customers`, count registered customers per state. Label missing states as `Unknown` and apply the same **at least five customers** threshold to that group. Return `State` and `customer_count`, sorted by customer count descending, then by state ascending.

### Sample input

| CustomerID | State |
|---:|---|
| 1 | Karnataka |
| 2 | Karnataka |
| 3 | Karnataka |
| 4 | Karnataka |
| 5 | Karnataka |
| 6 | Maharashtra |

### Expected output

| State | customer_count |
|---|---:|
| Karnataka | 5 |

Karnataka meets the threshold exactly. Maharashtra has one customer, so it’s excluded.

## Learner solution — SQLite

```sql
select 
COALESCE(State, 'Unknown') AS State

, count(CustomerID) as customer_count
from Customers
group by state
having count(CustomerID)>=5
order by  count(CustomerID) desc, State asc
```

Verified on the original sample and the extended example below. The query assumes non-NULL customer IDs, as with a primary key.

## Step-by-step walkthrough

Start by asking what one output row represents. It represents one state group. Use the same extended example throughout: keep the original six customers, add IDs 7–11 with a NULL state, and add IDs 12–17 with state Delhi. All fields come from Customers, so the query uses a single table.

### 1. Group and count the customer rows

**What to do.** Group by the stored state and count customers in each group.

**Why.** Karnataka's five rows belong to one group. The five missing states also form one group, and counting customer IDs includes those rows.

```sql
SELECT State, COUNT(CustomerID) AS customer_count FROM Customers GROUP BY State ORDER BY State;
```

| State | customer_count |
|---|---:|
| `NULL` | 5 |
| Delhi | 6 |
| Karnataka | 5 |
| Maharashtra | 1 |

### 2. Filter whole groups and label the missing state

**What to do.** Use HAVING to apply the threshold after counting. Use COALESCE to display Unknown for the NULL group. It returns the stored state when present and falls back to Unknown for SQL NULL. In this preview, sort by state to inspect the labels.

**Why.** The threshold is a condition on a whole group. Filtering missing states in WHERE would remove their rows before they can contribute to the Unknown group.

```sql
select 
COALESCE(State, 'Unknown') AS State

, count(CustomerID) as customer_count
from Customers
group by state
having count(CustomerID)>=5
ORDER BY State ASC
```

| State | customer_count |
|---|---:|
| Delhi | 6 |
| Karnataka | 5 |
| Unknown | 5 |

Maharashtra drops out. Karnataka and Unknown both qualify at exactly five.

### 3. Apply the requested sort

**What to do.** Sort by count descending and break ties by the displayed state name ascending. Run the final SQLite query above.

**Why.** Delhi has the highest count. Karnataka and Unknown tie, so Karnataka comes first alphabetically. The preview happened to display the same order on these rows.

| State | customer_count |
|---|---:|
| Delhi | 6 |
| Karnataka | 5 |
| Unknown | 5 |

## Learner solution — SQL Server

```sql
select 
COALESCE(State, 'Unknown') AS State

, count(CustomerID) as customer_count
from Customers
group by state
having count(CustomerID)>=5
order by  count(CustomerID) desc, State asc;
```

This adaptation was reviewed by inspection.

## Official solution

[PNP answer key, Q13](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT COALESCE(TRIM(c.State), 'Unknown') AS State,
       COUNT(*)                           AS customer_count
FROM Customers AS c
GROUP BY COALESCE(TRIM(c.State), 'Unknown')
HAVING COUNT(*) >= 5
ORDER BY customer_count DESC, State;
```

### Official answer — SQLite adaptation

```sql
SELECT COALESCE(TRIM(c.State), 'Unknown') AS State,
       COUNT(*)                           AS customer_count
FROM Customers AS c
GROUP BY COALESCE(TRIM(c.State), 'Unknown')
HAVING COUNT(*) >= 5
ORDER BY customer_count DESC, State;
```

### Official answer — SQL Server adaptation

```sql
SELECT COALESCE(TRIM(c.State), 'Unknown') AS State,
       COUNT(*)                           AS customer_count
FROM Customers AS c
GROUP BY COALESCE(TRIM(c.State), 'Unknown')
HAVING COUNT(*) >= 5
ORDER BY customer_count DESC, State;
```

The answer-key SQL runs unchanged in SQLite and works with SQL Server 2017 or later. Its grouping expression trims state names and maps NULL to Unknown before counting. The learner groups by the stored state and labels NULL for display. Both returned the same results on the original and extended examples. The SQL Server version was reviewed by inspection.

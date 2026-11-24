# PNP P013 — States with at least five customers

**Topic:** Sorting and Grouping  
**Difficulty:** Easy

## Question

**Table colors** · 🟦 `Customers`

**Business scenario.** Regional sales is deciding where to place field representatives. A rep is only worth assigning to a state with at least five registered customers. They want the qualifying states with the biggest first. 🟦 `Customers` with no state on file should be visible as their own line so the team can see how many cannot be placed.

**Task.** Count customers per state and keep only states with five or more. Label a missing state as Unknown. Sort by customer count, highest first, then by state.

[PNP source question](../../../2.PNP-%20foundations%20and%20practice/3.%20Sorting%20and%20Grouping/P013.%20States%20with%20at%20least%20five%20customers.md#question-and-image)

### Required output columns

One output row represents one state with at least five customers, with missing states reported as Unknown.

| Output column | Source or calculation | Meaning and applicable rules | Example value |
| --- | --- | --- | --- |
| `State` | 🟦 `Customers.State` | Stored state name, with `Unknown` for SQL NULL. The learner query does not trim; padded state values remain separate from the official answer’s trimmed grouping. | Karnataka |
| `customer_count` | 🟦 `Customers` | Number of customers registered in that state. | 5 |

### Practice example · Sample input

**🟦 `Customers`**

| 🟦 CustomerID | 🟦 State |
|---:|---|
| 🟦 1 | 🟦 Karnataka |
| 🟦 2 | 🟦 Karnataka |
| 🟦 3 | 🟦 Karnataka |
| 🟦 4 | 🟦 Karnataka |
| 🟦 5 | 🟦 Karnataka |
| 🟦 6 | 🟦 Maharashtra |

### Expected output

| 🟦 State | 🟦 customer_count |
|---|---:|
| 🟦 Karnataka | 🟦 5 |

![PNP P013 sample inputs and expected output](../../assets/question-samples/p013.svg)
[View sample inputs and output with colored cells](../../assets/question-samples/p013.svg?raw=1)

### How the sample produces this output

🟦 Customer IDs 🟦 1 through 🟦 5 all belong to 🟦 Karnataka. Their count is exactly **🟦 5**, which meets the minimum. 🟦 Maharashtra has only customer 🟦 6, giving it a count of **🟦 1**. 🟦 Karnataka is therefore the only output row.

## Step 1 · Your approach before writing SQL

1. What does one row of the final output represent?
2. Which table would you put in `FROM`? If you need other tables, which comes second, third, and so on, and why?
3. Would you use a join at any step? For each join you choose, name its type and matching columns and explain why it fits the question.

## Learner solution — SQLite (CASE)

```sql
select 
CASE
    WHEN State IS NOT NULL THEN State
    ELSE 'Unknown'
END AS State

, count(CustomerID) as customer_count
from Customers
group by state
having count(CustomerID)>=5
order by  count(CustomerID) desc, State asc
```

Verified on the original sample and the extended example below. The query assumes non-NULL customer IDs, as with a primary key.

## Important learnings from P013

### 1. One output row represents one reporting state
GROUP BY forms one group per state value. COUNT(CustomerID) counts identified customers in that group; HAVING applies the minimum of five after the count is known.

### 2. Treat missing state as a reporting label
The learner's CASE labels NULL state as Unknown. The course answer also trims surrounding spaces before applying the fallback, so whitespace-only values need separate attention.

### 3. Keep the group expression consistent
Use the same normalized state expression in SELECT and GROUP BY. In SQLite, a GROUP BY name that matches an input column can resolve to that source column rather than a same-named SELECT alias; the stored learner query's behavior is documented in the comparison section.

## Visual walkthrough

[Open the Previous / Next walkthrough](../../assets/steps/PNP-P013/01.md)

The diagram follows the extended sample used in the step-by-step walkthrough. **Predict the result.** Five customers have no recorded state. Will their group meet the threshold?

![States with at least five customers. Delhi's six come first. The two groups of five sort by the displayed labels Karnataka and Unknown.](../../assets/walkthroughs/p013.svg)

[Open the full-size walkthrough](../../assets/walkthroughs/p013.svg?raw=1)

## Step-by-step walkthrough

🟦 **FROM Customers · one table is enough** · A customer contributes once to the group for their recorded state. The ID to count and the state to group by already share one row, even when the state is missing.

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

**What to do.** Use HAVING to apply the threshold after counting. Use CASE to display Unknown for the NULL group and keep the stored state for other groups. The COALESCE alternative below makes the same choice. In this preview, sort by state to inspect the labels.

**Why.** The threshold is a condition on a whole group. Filtering missing states in WHERE would remove their rows before they can contribute to the Unknown group.

```sql
select 
CASE
    WHEN State IS NOT NULL THEN State
    ELSE 'Unknown'
END AS State

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

**What to do.** Sort by count descending and break ties by the displayed state name ascending.

**Why.** Delhi has the highest count. Karnataka and Unknown tie, so Karnataka comes first alphabetically. The preview happened to display the same order on these rows.

```sql
select 
CASE
    WHEN State IS NOT NULL THEN State
    ELSE 'Unknown'
END AS State

, count(CustomerID) as customer_count
from Customers
group by state
having count(CustomerID)>=5
order by  count(CustomerID) desc, State asc
```

| State | customer_count |
|---|---:|
| Delhi | 6 |
| Karnataka | 5 |
| Unknown | 5 |

## Learner solution — SQL Server adaptation

```sql
select 
CASE
    WHEN State IS NOT NULL THEN State
    ELSE 'Unknown'
END AS State

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

## Comparison with the course answer

The learner labels NULL State as Unknown with CASE, but does not TRIM the stored state. The course answer uses COALESCE(TRIM(State), 'Unknown'), so whitespace-only states also become Unknown. The learner groups by the name State, which in SQLite can resolve to the source column rather than the SELECT alias when both share the same name; a NULL source group and a literal Unknown value can therefore remain separate groups while displaying the same label. The supplied sample still matches the saved output. The learner query is preserved, and the normalization/alias difference remains explicit.

## Verification

The saved learner query ran in SQLite on the [walkthrough fixture](../../assets/steps/PNP-P013/walkthrough.json). The column names and all 1 expected row matched in the displayed order.

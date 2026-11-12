# Exercise 3 — Numbers and maths

PNP Python mentorship PDF, page 7.

1. Use `%` to check whether 2025 is even.
2. Split ₹2,847 equally among four people and round to two decimal places.
3. Convert `"1,499"` to the integer `1499` using `replace()` and `int()`.

## Final learner submission

```python
number = 2025
if number % 2 == 1:
    print("odd")
else:
    print("even")
amount = 2847
people = 4
print(round(amount / people, 2))
amount_text = "1,499"
amount_text = amount_text.replace(",", "")
print(int(amount_text))
```

## Output

```text
odd
711.75
1499
```

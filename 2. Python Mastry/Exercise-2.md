# Exercise 2 — Variables and types

PNP Python mentorship PDF, page 6. Guided checkpoint passed after corrections.

## 1. Store product details and print the total cost

Learner's corrected code:

```python
product_name = 'Keyboard'
price = 1499
quantity = 3
print(price*quantity)
```

Output: `4497`.

## 2. Swap two variables without a third variable

Learner's code:

```python
a, b = 10, 20 # two at once
print(a, b)
a, b = b, a # swap without a third variable
print(a, b)
```

```text
10 20
20 10
```

## 3. Identify the types

The learner correctly identified the three types. The calls below reproduce the exercise.

| Call | Output | Explanation |
| --- | --- | --- |
| `print(type(10))` | `<class 'int'>` | `10` is an integer literal. |
| `print(type(10.0))` | `<class 'float'>` | `10.0` is a floating-point literal. |
| `print(type("10"))` | `<class 'str'>` | The quotes make `"10"` a string. |

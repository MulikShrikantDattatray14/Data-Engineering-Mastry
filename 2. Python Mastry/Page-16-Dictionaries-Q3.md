# Page 16 — Dictionaries Q3

PNP Python mentorship, Lesson 12. Group words by their first letter.

## Final learner submission

```python
words = ["apple", "avocado", "banana", "blueberry"]
groups = {}

for each in words:
    word=each[0]
    if word in groups:
        groups [word].append(each)
    else:
        groups [word]=[each]


print(groups )
```

## Step-by-step execution

| Pass | Current word | Key | What happens | Dictionary after the pass |
| --- | --- | --- | --- | --- |
| 1 | `apple` | `a` | Create the list for `a`. | `{'a': ['apple']}` |
| 2 | `avocado` | `a` | Append to the existing list for `a`. | `{'a': ['apple', 'avocado']}` |
| 3 | `banana` | `b` | Create the list for `b`. | `{'a': ['apple', 'avocado'], 'b': ['banana']}` |
| 4 | `blueberry` | `b` | Append to the existing list for `b`. | `{'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}` |

`print(groups)` runs once after the loop.

```text
{'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}
```

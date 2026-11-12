# Page 13 — While, break, and continue

PNP Python mentorship, Lesson 9. Each block preserves the final learner submission and runs separately.

## 1. Double from 1 until the value exceeds 1000

```python
start =1
end=1000
count=0
while start  <= end:
    count+=1
    start=start*2


print(count)
```

Output: `10`. The last doubling takes the value from `512` to `1024`.

## 2. Sum amounts until the first negative number

```python
amounts = [100, 250, -50, 400]
sum=0
for i in amounts:
    if(i>=0):
        sum+=i
    else:
        break


print(sum)
```

Output: `350`. The loop stops at `-50`. A zero before the negative adds zero and allows the loop to continue.

## 3. Sum text amounts and skip empty strings

```python
amounts = ["100", "", "250", "", "50"]
sum=0
for i in amounts:
    if(i!=""):
        sum+=int(i)
    else:
       continue


print(sum)
```

Output: `400`. The loop skips empty strings and converts each remaining amount with `int()` before adding it.

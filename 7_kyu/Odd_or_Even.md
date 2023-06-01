# Odd or Even?

Task:
Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching `"odd"` or `"even"`.

If the input array is empty consider it as: `[0]` (array with a zero).

Examples:
```
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
```

Have fun!

---

## Given code
```python
def odd_or_even(arr):
    pass
```

---

## Solution 1
```python
def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"
```

---

## Solution 2
```python
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"
```

## Solution 3
```python
def odd_or_even(arr):
    return "odd" if sum(arr) & 1 else "even"
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/5949481f86420f59480000e7)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/7_kyu/Odd_or_Even.py)



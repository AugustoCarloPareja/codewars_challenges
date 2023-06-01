# Persistent Bugger.

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example **(Input --> Output):**

```
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
```

---

## Given code
```python
def persistence(n):
    # your code
```

---

## Solution 1
```python
def persistence(n):
    iterations = 0
    
    while n >= 10:
        iterations += 1
        total = 1
        
        for num in str(n):
            total *= int(num)
        n = total
        
    return iterations
```

---

## Solution 2
```python
# Using recursion
def persistence(n):
    if n < 10:
        return 0
    else:
        iterations = 1
        
        for number in str(n):
            iterations *= int(number)
        
        return persistence(iterations) + 1
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/6_kyu/Persistent_Bugger.py)




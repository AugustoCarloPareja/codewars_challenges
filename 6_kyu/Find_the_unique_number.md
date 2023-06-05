# Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

```python
find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
```

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

1. Find the unique number (this kata)
2. [Find the unique string](https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3)
3. [Find The Unique](https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5)

---

## Given code
```python
def find_uniq(arr):
    # your code here
    return n   # n: unique number in the array
```

---

## Solution 1
```python
# Solution O(n)
def find_uniq(arr):
    counter = {}
    
    for value in arr:
        if value not in counter:
            counter[value] = 1
        else:
            counter[value] += 1
    
    for value in arr:
        if counter[value] == 1:
            return value
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/585d7d5adb20cf33cb000235)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/6_kyu/Find_the_unique_number.py)
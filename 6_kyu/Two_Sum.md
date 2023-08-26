# Sort the odd

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: `(index1, index2)`.

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

```python
two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
```

---

## Given code
```python
def two_sum(numbers, target):
	return []
```

---

## Solution 1
```python
def two_sum(numbers, target):
    solution = {}

    for idx, _ in enumerate(numbers):
        if target - numbers[idx] in solution:
            return [solution[target - numbers[idx]],idx]
        else:
            solution[numbers[idx]]=idx
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/52c31f8e6605bcc646000082)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/6_kyu/Two_Sum.py)


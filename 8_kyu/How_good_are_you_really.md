# How good are you really?

There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return `True` if you're better, else `False`!

**Note**:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

---

## Given code
```python
def better_than_average(class_points, your_points):
    # Your code here
```

---

## Solution 1
```python
def better_than_average(class_points, your_points):
    return your_points > (sum(class_points) / len(class_points))
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/5601409514fc93442500010b)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/8_kyu/How_good_are_you_really.py)

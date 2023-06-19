# Sort the odd

## Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

## Examples

```
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
```

---

## Given code
```python
def sort_array(source_array):
    # Return a sorted array.
```

---

## Solution 1
```python
def sort_array(source_array):
    odd_sorted_array = sorted([x for x in source_array if (x%2 != 0)])
    
    iter = 0
    
    for idx, n in enumerate(source_array):
        if n%2 != 0:
            source_array[idx] = odd_sorted_array[iter]
            iter += 1
    
    return source_array
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/578aa45ee9fd15ff4600090d)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/6_kyu/Sort_the_odd.py)


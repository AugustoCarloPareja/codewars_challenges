# Ones and Zeros

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: `[0, 0, 0, 1]` is treated as `0001` which is the binary representation of `1`.

Examples
```
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
```

---

## Given code
```python
# write the function is_anagram
def binary_array_to_number(arr):
  # your code
```

---

## Solution 1
```python
def binary_array_to_number(arr):
    binary_str = ''.join(str(bit) for bit in arr)
    equivalent_value = int(binary_str, 2)
    return equivalent_value
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/578553c3a1b8d5c40300037c)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/7_kyu/Ones_and_Zeros.py)
# Printer Errors

In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from `a to m`.

The colors used by the printer are recorded in a control string. For example a "good" control string would be `aaabbbbhaijjjm` meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. `aaaxbbbbyyhwawiwjjjwwm` with letters not from `a to m`.

You have to write a function `printer_error` which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from `a` to `z`.

Examples:
```
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
```

---

## Given code
```python
def printer_error(s):
    # your code
```

---

## Solution 1
```python
colors = "abcdefghijklm"

def printer_error(s):
    errors = []
    
    for char in s:
        if char not in colors:
            errors.append(char)
    
    return f"{len(errors)}/{len(s)}"
```

---

## Solution 2
```python
def printer_error(s):
    errors = sum([1 for char in s if char not in 'abcdefghijklm'])
    return f"{errors}/{len(s)}"
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/56541980fa08ab47a0000040)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/7_kyu/Printer_Errors.py)
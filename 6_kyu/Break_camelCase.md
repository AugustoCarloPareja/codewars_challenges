# Break camelCase

Complete the solution so that the function will break up camel casing, using a space between words.

**Example**
```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```

---

## Given code
```python
def solution(s):
    pass
```

---

## Solution 1
```python
def solution(s):
    string = ""
    
    for char in s:
        if char == char.upper():
            string += " "
        string += char
        
    return string
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/5208f99aee097e6552000148)
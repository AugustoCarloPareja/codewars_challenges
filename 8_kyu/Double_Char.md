# Double Char
 
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.


**Examples (Input -> Output):**
```
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
```
Good Luck!

---

## Given code
```python
def double_char(s):
    pass
```

---

## Solution 1
```python
def double_char(s):
    string  = ""
    for char in s:
        string += char * 2
    return string
```

---

## Solution 2
```python
def double_char(s):
    return ''.join(char * 2 for char in s)
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/56b1f01c247c01db92000076)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/8_kyu/Double_Char.py)
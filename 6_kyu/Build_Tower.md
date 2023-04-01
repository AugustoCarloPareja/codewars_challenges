# Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer `number of floors`. A tower block is represented with `"*"` character.

For example, a tower with 3 floors looks like this:
```
[
  "  *  ",
  " *** ", 
  "*****"
]
```
And a tower with 6 floors looks like this:

```
[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]
```

---

## Given code
```python
def tower_builder(n_floors):
    # build here
```

---

## Solution 1
```python
def tower_builder(n_floors):
    tower = []
    width = (n_floors * 2) - 1
    
    for floor in range(1, 2 * n_floors, 2):
        blocks = floor * '*'
        line = blocks.center(width)
        tower.append(line)
    return tower
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/576757b1df89ecf5bd00073b)
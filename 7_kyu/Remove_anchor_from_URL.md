# Remove anchor from URL

Task:
Complete the function/method so that it returns the url with anything after the anchor (`#`) removed.

Examples
```
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
```

---

## Given code
```python
def remove_url_anchor(url):
    # TODO: complete
```

---

## Solution 1
```python
def remove_url_anchor(url):
    return url.split("#")[0]
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/51f2b4448cadf20ed000038)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/7_kyu/Remove_anchor_from_URL.py)
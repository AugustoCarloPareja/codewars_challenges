# Anagram Detection

An **anagram** is the result of rearranging the letters of a word to produce a new word (see [wikipedia](https://en.wikipedia.org/wiki/Anagram)).

Note: anagrams are case insensitive

Complete the function to return `true` if the two arguments given are anagrams of each other; return `false` otherwise.

Examples
`"foefet"` is an anagram of `"toffee"`

`"Buckethead"` is an anagram of `"DeathCubeK"`

---

## Given code
```python
# write the function is_anagram
def is_anagram(test, original):
    pass
```

---

## Solution 1
```python
# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())
```

---

- [Click to check challenge in CodeWars](https://www.codewars.com/kata/529eef7a9194e0cbc1000255)
- [Click to check a python sample in this repo](https://github.com/AugustoCarloPareja/codewars_challenges/blob/master/7_kyu/Anagram_Detection.py)
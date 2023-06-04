def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())

if __name__ == '__main__':
    possible_anagrams = [
        ("foefet", "toffee"),
        ("Buckethead", "DeathCubeK"),
        ("Twoo", "WooT"),
        ("dumble", "bumble"),
        ("ound", "round"),
        ("apple", "pale")
    ]
    
    for words in possible_anagrams:
        print(f"Are the following word anagrams?: {words} -> {is_anagram(*words)}")
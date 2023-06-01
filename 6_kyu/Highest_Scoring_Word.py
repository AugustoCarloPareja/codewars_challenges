alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12,  "m": 13, "n": 14, 
            "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

def get_value(word):
    return sum(alphabet[letter] for letter in word)

def high(word_string):
    return max(word_string.split(), key=get_value)

if __name__ == '__main__':
    words = [
        'qytidud tfgsboulu bcotde scsxigulft atmkeavo qhfrlug rrozrmrjd jolnkw mqymeonz ayspegyf',
        'nzeuuw zjqsaidfn efqwj mqdncge onpuyy hfbich fkzbcedddk',
        'shcrl irrresk gfieoi xao hcfldkqmtq qaggbsatc pumo dcei'
    ]
    
    for word in words:
        print(f"The highest word high in '{word}' is {high(word)}")
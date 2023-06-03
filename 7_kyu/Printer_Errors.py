# Solution 1
colors = "abcdefghijklm"

def printer_error_1(s):
    errors = []
    
    for char in s:
        if char not in colors:
            errors.append(char)
    
    return f"{len(errors)}/{len(s)}"

# Solution 2
def printer_error_2(s):
    errors = sum([1 for char in s if char not in 'abcdefghijklm'])
    return f"{errors}/{len(s)}"

if __name__ == '__main__':
    strings = [
        "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz",
        "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
    ]
    
    for string in strings:
        print(f"Solution 1\nThe quantity of errors/lenght of the string: {string} is {printer_error_1(string)}")
        print(f"Solution 2\nThe quantity of errors/lenght of the string: {string} is {printer_error_2(string)}")
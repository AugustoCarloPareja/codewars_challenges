## Solution 1
def double_char_1(s):
    string  = ""
    for char in s:
        string += char * 2
    return string

## Solution 2
def double_char_2(s):
    return ''.join(char * 2 for char in s)

if __name__ == '__main__':
    strings = ["String", "Hello World", "1234!_"]
    
    for string in strings:
        print(f"Solution 1\n: The result of the following string: {string} is {double_char_1(string)}")
        print(f"Solution 2\n: The result of the following string: {string} is {double_char_2(string)}")
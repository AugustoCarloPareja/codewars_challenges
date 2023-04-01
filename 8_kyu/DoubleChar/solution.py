#1 Straightfoward solution
def double_char(s):
    string  = ""
    for char in s:
        string += char * 2
    return string

#2 Pythonic solution
def double_char(s):
    return ''.join(char * 2 for char in s)
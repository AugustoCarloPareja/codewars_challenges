def solution(s):
    string = ""
    
    for char in s:
        if char == char.upper():
            string += " "
        string += char
        
    return string
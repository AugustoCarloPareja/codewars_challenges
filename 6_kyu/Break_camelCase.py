def solution(s):
    string = ""
    
    for char in s:
        if char == char.upper():
            string += " "
        string += char
        
    return string

if __name__ == '__main__':
    print(solution('breakCamelCase'))
    print(solution('yearLastWeekBig'))
    print(solution('fewChildEyeGreat'))
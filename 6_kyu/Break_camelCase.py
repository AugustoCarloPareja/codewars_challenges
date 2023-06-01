def solution(s):
    string = ""
    
    for char in s:
        if char == char.upper():
            string += " "
        string += char
        
    return string

if __name__ == '__main__':
    strings = ['breakCamelCase', 'yearLastWeekBig', 'fewChildEyeGreat']
    
    for string in strings:
        print(f"\nString: {string}\nSolution: {solution(string)}\n")
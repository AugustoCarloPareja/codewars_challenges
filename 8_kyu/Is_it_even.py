def is_even(n): 
    return n % 2 == 0

if __name__ == '__main__':
    numbers = [0, 0.5, 1, 2, -4, 15, 20, 220, 222222221, 500000000]
    
    for number in numbers:
        print(f"Is {number} even or odd?\nResult: {is_even(number)}\n")
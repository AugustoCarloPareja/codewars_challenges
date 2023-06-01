## Solution 1
def persistence_1(n):
    iterations = 0
    
    while n >= 10:
        iterations += 1
        total = 1
        
        for num in str(n):
            total *= int(num)
        n = total
        
    return iterations

## Solution 2
# Using recursion
def persistence_2(n):
    if n < 10:
        return 0
    else:
        iterations = 1
        
        for number in str(n):
            iterations *= int(number)
        
        return persistence_2(iterations) + 1

if __name__ == '__main__':
    nums = [39, 4, 25, 999]
    
    for num in nums:
        print(
            f"""
            Solution 1:
            The multiplicative persistence of {num} is {persistence_1(num)}
            
            Solution 2:
            The multiplicative persistence of {num} is {persistence_2(num)}
            """
        )


## Solution 1
def odd_or_even_1(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"

## Solution 2
def odd_or_even_2(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"

## Solution 3
def odd_or_even_3(arr):
    return "odd" if sum(arr) & 1 else "even"

if __name__ == '__main__':
    print("Solution 1")
    arr = [60, 35, -62, -55, 8, 27, -39, -81, 41, -95, 99, -100, 16, -76, -31, -90, -31, -50]
    print(f"Is the following array odd or even? -> {arr}. Result: {odd_or_even_1(arr)}")
    arr = [-8, -98, -53, -56, -33, 74, -51, 24, -84, 74, 48, 95]
    print(f"Is the following array odd or even? -> {arr}. Result: {odd_or_even_1(arr)}")
    print("\nSolution 2")
    arr = [-53, -67]
    print(f"Is the following array odd or even? -> {arr}. Result: {odd_or_even_2(arr)}")
    arr = [-24, -4, -11]
    print(f"Is the following array odd or even? -> {arr}. Result: {odd_or_even_2(arr)}")
    print("\nSolution 3")
    arr = [-57, -25, 2]
    print(f"Is the following array odd or even? -> {arr}. Result: {odd_or_even_3(arr)}")
    arr = [5, -4, 75, -67, -8, 36, -71]
    print(f"Is the following array odd or even? -> {arr}. Result: {odd_or_even_3(arr)}")
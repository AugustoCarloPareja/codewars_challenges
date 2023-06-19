def binary_array_to_number(arr):
    binary_str = ''.join(str(bit) for bit in arr)
    equivalent_value = int(binary_str, 2)
    return equivalent_value

if __name__ == '__main__':
    arrays = [
        [0,0,0,1],
        [0,0,1,0],
        [1,1,1,1],
        [0,1,1,0]
    ]
    
    for arr in arrays:
        print(f"Testing: {arr} ==> {binary_array_to_number(arr)}")
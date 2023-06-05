def find_uniq(arr):
    counter = {}
    
    for value in arr:
        if value not in counter:
            counter[value] = 1
        else:
            counter[value] += 1
    
    for value in arr:
        if counter[value] == 1:
            return value

if __name__ == '__main__':
    arrays = [[ 1, 1, 1, 2, 1, 1 ], [ 0, 0, 0.55, 0, 0 ], [ 3, 10, 3, 3, 3 ]]
    
    for arr in arrays:
        print(f"The unique number of {arr} is {find_uniq(arr)}")
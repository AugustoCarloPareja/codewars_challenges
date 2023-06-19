def sort_array(source_array):
    odd_sorted_array = sorted([x for x in source_array if (x%2 != 0)])
    
    iter = 0
    
    for idx, n in enumerate(source_array):
        if n%2 != 0:
            source_array[idx] = odd_sorted_array[iter]
            iter += 1
    
    return source_array

if __name__ == '__main__':
    source_arrays = [[5, 3, 2, 8, 1, 4], [1, 3, 2, 8, 5, 4], [5, 3, 1, 8, 0], [1, 3, 5, 8, 0], []]
    
    for source_array in source_arrays:
        print(f"Sorting array of {source_array}\nCompleted sorted array: {sort_array(source_array)}\n\n")
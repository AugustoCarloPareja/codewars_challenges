def two_sum(numbers, target):
    solution = {}

    for idx, _ in enumerate(numbers):
        if target - numbers[idx] in solution:
            return [solution[target - numbers[idx]],idx]
        else:
            solution[numbers[idx]]=idx

if __name__ == '__main__':
    sample_test = [([1,2,3], 4), ([1234,5678,9012], 14690), ([2,2,3], 4)]
    
    for sample in sample_test:
        print(f"Result of Two Sum solution: index = {two_sum(sample[0], sample[1])}\n")
def better_than_average(class_points, your_points):
    return your_points > (sum(class_points) / len(class_points))

if __name__ == '__main__':
    arr_results = [
                    ([100, 40, 34, 57, 29, 72, 57, 88], 75),
                    ([12, 23, 34, 45, 56, 67, 78, 89, 90], 69),
                    ([29, 55, 74, 60, 11, 90, 67, 28], 21)
                ]
    
    for result in arr_results:
        print(f"""
                My peers have the following scores: {result[0]}
                I have the following score: {result[1]}.
                I am better than everyone else? {better_than_average(result[0], result[1])
                }"""
            )
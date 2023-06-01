def dig_pow(n, p):
    sum_digits = 0
    
    for number in str(n):
        sum_digits += int(number) ** p
        p += 1
    if sum_digits % n == 0:
        return sum_digits / n
    else:
        return -1

if __name__ == '__main__':
    print(dig_pow(89, 1))
    print(dig_pow(92, 1))
    print(dig_pow(695, 2))
    print(dig_pow(46288, 3))
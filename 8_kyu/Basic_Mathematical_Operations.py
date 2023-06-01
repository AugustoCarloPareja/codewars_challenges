def basic_op(operator, value1, value2):
    ops = {
            '+' : lambda a, b: a + b,
            '-' : lambda a, b: a - b,
            '*' : lambda a, b: a * b,
            '/' : lambda a, b: a / b,
        }
    
    return ops[operator](value1, value2)

if __name__ == '__main__':
    operations = [
                    ('-', 381, 9),
                    ('+', 83, 7943),
                    ('/', 1682, 24),
                    ('*', 74070, 8939)
                ]
    
    for op in operations:
        print(f'{op[1]}{op[0]}{op[2]} = {basic_op(op[0], op[1], op[2])}')
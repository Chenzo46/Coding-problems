from math import copysign
def main():
    cases = int(input())
    for cases in range(cases):
        operation = input().split()
        operation_format = '{x} {operand} {y}'
        try:
            num = eval(operation_format.format(x = operation[0], y = operation[2], operand = operation[1]))
            operation_one = int(num * 10 + copysign(1,num) * 0.5) / 10
        except ZeroDivisionError:
            operation_one = 'undefined'
        
        try:
            num = eval(operation_format.format(x = operation[2], y = operation[0], operand = operation[1]))
            operation_two = int(num * 10 + copysign(1,num) * 0.5) / 10
        except ZeroDivisionError:
            operation_two = 'undefined'
        
        print(f'{operation_one} {operation_two}')
        
if __name__ == '__main__':
    main()
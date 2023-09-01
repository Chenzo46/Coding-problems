for _ in range(int(input())):
    a,b = input().split()
    print(eval(f'{a} + {b}') if a != b else eval(f'4 * {a}'))
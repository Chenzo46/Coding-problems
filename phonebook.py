cases = int(input())

for _ in range(cases):

    number, method = input().split()

    if method == 'PARENTHESES':
        print(f'({number[0:3]}) {number[3:6]}-{number[6:]}')
    elif method == 'DASHES':
        print(f'{number[0:3]}-{number[3:6]}-{number[6:]}')
    else:
        print(f'{number[0:3]}.{number[3:6]}.{number[6:]}')
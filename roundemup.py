cases = int(input())

for _ in range(cases):

    a, b, c = list(map(int,input().split()))

    a = a + 1 if a % 2 != 0 else a + 2
    b = b + 1 if b % 2 != 0 else b + 2
    c = c + 1 if c % 2 != 0 else c + 2

    print(f'{a} {b} {c}')
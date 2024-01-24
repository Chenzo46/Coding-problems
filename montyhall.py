import decimal
from decimal import Decimal

for _ in range(int(input())):
    doors, rounds, doors_opened = list(map(int,input().split()))

    current_probabilty = 100
    
    for idx in range(0,rounds):
        current_probabilty -= current_probabilty/(doors)
        doors -= doors_opened + 1

    current_probabilty = current_probabilty/doors

    print(f'{current_probabilty:.2f}%')
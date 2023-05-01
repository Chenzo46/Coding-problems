from math import ceil
import decimal
from decimal import Decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
def main():
        
    cases = int(input())
    for case in range(cases):
        charge_count = int(input())

        charges = [float(input()) for _ in range(charge_count)]
        new_charges = []
        
        extra_change = 0
        for charge in charges:
            pennies = 100 - int(str(charge).split('.')[1]) if int(str(charge).split('.')[1]) > 0 else 0
            extra_change += pennies
            charge = ceil(charge)
            new_charges.append(str(charge))
        extra_change = str(extra_change)
        extra_change = extra_change[:len(extra_change)-2] + '.' + extra_change[len(extra_change)-2:]
        print('\n'.join(new_charges))
        print(f'{float(extra_change):.2f}')

if __name__ == '__main__':
    main()

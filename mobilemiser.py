import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

def main():
    cases = int(input())

    for case in range(cases):

        amount = float(input()[1:])
        if amount == -0:
            amount = 0
        tip_one = amount * .15
        tip_two = amount * .18
        tip_three = amount * .20

        tip_one = str(Decimal(tip_one).quantize(Decimal('1.00')))
        tip_two = str(Decimal(tip_two).quantize(Decimal('1.00')))
        tip_three = str(Decimal(tip_three).quantize(Decimal('1.00')))
        tip_one = tip_one.ljust(len(tip_one) - 2, '0')
        tip_two = tip_two.ljust(len(tip_two) - 2, '0')
        tip_three = tip_three.ljust(len(tip_three) - 2, '0')
        print(f'Total of the bill: ${amount:.2f}')
        print(f'15% = ${tip_one}')
        print(f'18% = ${tip_two}')
        print(f'20% = ${tip_three}')

if __name__ == '__main__':
    main()
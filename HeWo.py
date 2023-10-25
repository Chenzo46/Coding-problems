import decimal
from decimal import Decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

def main():
    cases = int(input())
    for i in range(cases):
        sillyStringlol = input()
        print(sillyStringlol)

if __name__ == '__main__':
    #main()
    print(Decimal('22.5').quantize(Decimal('1')))
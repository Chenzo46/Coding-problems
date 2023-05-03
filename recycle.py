import decimal
from decimal import Decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

cases = int(input())

for _ in range(cases):
    
    al, pb, gb = input().split()

    al = Decimal((int(al) * 31) * 0.05).quantize(Decimal('1.00'))
    pb = Decimal((int(pb) * 15) * 0.10).quantize(Decimal('1.00'))
    gb = Decimal((int(gb) / 2) * 0.20).quantize(Decimal('1.00'))
    total = Decimal(al+pb+gb).quantize(Decimal('1.00'))

    print(f'${total}')
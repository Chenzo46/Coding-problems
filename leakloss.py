import decimal
from decimal import Decimal
cases = int(input())
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
for _ in range(cases):

    volume, r1, r2 = list(map(float,input().split()))

    result = (volume / (r1 - r2)) * r2
    result = Decimal(result).quantize(Decimal('1'))
    print(result)
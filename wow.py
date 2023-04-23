# Possible worokaround to the round function being bad
import decimal
from decimal import Decimal
#Method 1 (normal)
print('round() function uses bankers rounding, which rounds the number to the nearest even number')
a = float(input('a: '))
b = float(input('b: '))
print(f'a - normal round: {round(a,1)}')
print(f'b - normal round: {round(b,1)}')

# Method 2 (decimal package)
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print('we change the context round to ROUND_HALF_UP and use .quantize to round')
d_a = Decimal(a).quantize(Decimal('1.0'))
d_b = Decimal(b).quantize(Decimal('1.0'))
print(f'a - decimal package round: {d_a}')
print(f'b - decimal package round: {d_b}')
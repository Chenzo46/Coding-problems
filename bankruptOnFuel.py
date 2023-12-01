import decimal
from decimal import Decimal
from math import gcd

class tank:
    capacity = 0
    holding = 0

    def __init__(self, capacity) -> None:
        self.capacity = capacity
    
    def fill_tank(self, fill_amount) -> None:
        if self.is_full(): return
        self.holding += fill_amount
    
    def is_full(self)->bool:
        return self.holding >= self.capacity
    
    def __str__(self) -> str:
        rounded_holding = Decimal(self.holding).quantize(Decimal('0.1'), rounding=decimal.ROUND_HALF_UP)
        rounded_holding = str(rounded_holding)
        big_num,little_num = list(map(int, rounded_holding.split('.')))
        big_num = big_num*10
        numerator = big_num + little_num
        greatest_common_denominator = gcd(numerator, 10)
        numerator = int(numerator/greatest_common_denominator)
        denominator = int(10/greatest_common_denominator)
        return f'{numerator}/{denominator}' if denominator > 1 else str(numerator)
for _ in range(int(input())):
    fuel_available, tank_count = list(map(int,input().split()))
    tank_capacities = list(map(int,input().split()))
    tank_objects = [tank(tank_capacities[idx]) for idx in range(tank_count)]

    while fuel_available > 0:
        for tank_object in tank_objects:
            if not tank_object.is_full(): fuel_available -= 0.01
            tank_object.fill_tank(0.01)
        
    tank_objects = list(map(str, tank_objects))
    print(' '.join(tank_objects))
    
    

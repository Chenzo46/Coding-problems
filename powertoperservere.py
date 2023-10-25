from math import pi
from decimal import *

for _ in range(int(input())):
    diameter, required_revolutions, required_power, rpm, capacity, voltage_requirement, req_dist = input().split()

    wheel_rotation_distance = pi * float(diameter)
    rotations = (float(req_dist)*100) / wheel_rotation_distance
    total_revolutions = float(required_revolutions) * rotations
    time = total_revolutions / float(rpm)
    power_consumed = total_revolutions * float(required_power)
    current = power_consumed / float(voltage_requirement)
    amp_hours = (current * time)/60
    if amp_hours <= float(capacity):
        print(f'Success {Decimal(time).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)}')
    else:
        print('Fail')
from math import sqrt
cases = int(input())

for _ in range(cases):
    
    values = input().split() # chroma key 0-2, tolerance 3, foreground 4-6, background 7-9

    values = list(map(int,values))

    tolerance = values[3]

    dist_f = sqrt(pow(values[1] - values[5],2) + pow(values[0] - values[4],2) + pow(values[2] - values[6],2))

    if dist_f <= tolerance:
        print(f'{values[7]} {values[8]} {values[9]}')
    else:
        print(f'{values[4]} {values[5]} {values[6]}')
    

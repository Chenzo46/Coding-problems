from math import sqrt, floor

for _ in range(int(input())):
    
    #radius,width,height = list(map(int, input().rstrip().split()))
    test = input().split()
    radius = float(test[0])
    width = float(test[1])
    height = float(test[2])
    
    max_x = width+1
    max_y = height+1

    for x_pos in range(floor(max_x)):
        for y_pos in range(floor(max_y)):
            distance_from_center = sqrt(pow(x_pos,2) + pow(y_pos,2))
            if distance_from_center > radius:
                print(f'{x_pos},{y_pos}')
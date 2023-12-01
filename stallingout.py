for _ in range(int(input())):
    critical, port_side, star_board = list(map(float, input().split()))

    if abs(port_side - star_board) > 5:
        print("WARNING")
    elif (port_side + star_board)/2 - critical > 2:
        print("ALARM")
    else:
        print("OK")
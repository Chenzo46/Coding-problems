for _ in range(int(input())):
    f0,f1,f2,ql = list(map(float,input().split()))

    target_frame_time = 1000/90
    low_thresh = 0.7 * target_frame_time
    extrapolate_thresh = 0.85 * target_frame_time
    high_thresh = 0.9 * target_frame_time

    if f2 > high_thresh:
        ql -= 2
    elif f2 > extrapolate_thresh:
        extrapolated_value_long = f0 + (3/2) * (f2 - f0)
        extraplolated_value_short = f1 + 2 * (f2 - f1)
        extraplolated_value = max([extraplolated_value_short, extrapolated_value_long])
        if extraplolated_value > high_thresh:
            ql -= 2
    elif f0 < low_thresh and f1 < low_thresh and f2 < low_thresh:
        ql += 1
    
    ql = 1 if ql <= 0 else ql
    ql = 10 if ql > 10 else ql
    print(int(ql))

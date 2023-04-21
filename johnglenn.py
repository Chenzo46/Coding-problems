from math import sin
def main():
    cases = int(input())

    for case in range(cases):
        x_init, y_init, h, n = list(map(float,input().split()))
        y_prev = y_init
        x_prev = x_init
        x_cur = x_init
        y_cur = y_init
        for iteration in range(int(n)):
            x_cur = h + x_prev

            try:
                y_cur = y_prev + h * (sin(x_prev)/x_prev)
            except ZeroDivisionError:
                y_cur = y_prev + h
            
            x_prev = x_cur
            y_prev = y_cur
        
        print(round(y_cur,3))

if __name__ == '__main__':
    main()
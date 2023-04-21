def main():
    cases = int(input())

    for case in range(cases):
        n = int(input().strip())

        sensors = list(map(int,input().split()))

        sensors.sort()
        missing = 0
        if 1 not in sensors:
            missing = 1
        elif n not in sensors:
            missing = n
        else:
            for i in range(len(sensors)-1):
                if sensors[i]+1 not in sensors:
                    missing = sensors[i]+1
        print(missing)

if __name__ == '__main__':
    main()
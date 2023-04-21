def main():
    cases = int(input())

    for case in range(cases):
        region_name = input()
        data_point_count = int(input())

        data_points = [input().split() for idx in range(data_point_count)]
        data_points.sort(key = lambda x: float(x[0]))

        print(f'{region_name}:')

        for data_point in data_points:
            stars = ''.join(['*' for idx in range(int(round(float(data_point[0]),-3)/1000))])
            if float(data_point[0]) == 500:
                stars = '*'
            print(f'{data_point[1]} {stars}')
if __name__ == '__main__':
    main()
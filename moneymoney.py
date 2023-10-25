from decimal import Decimal
import decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

def main():
    cases = int(input())

    for case in range(cases):
        region_name = input()
        data_point_count = int(input())

        data_points = [input().split() for idx in range(data_point_count)]
        data_points.sort(key = lambda x: int(x[1]))

        print(f'{region_name}:')

        for data_point in data_points:
            num = data_point[0].split('.')[0]
            stars = ''
            if int(num) >= 100:
                stars_count = float(num[0:len(num)-2])/10
                stars_count = Decimal(stars_count).quantize(Decimal('1'))
                stars = '*'*int(stars_count)
            print(f'{data_point[1]} {stars}')
if __name__ == '__main__':
    main()
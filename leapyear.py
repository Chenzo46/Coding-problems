def main():
    cases = int(input())
    for case in range(cases):
        years = int(input())
        for _year in range(years):
            year = int(input())
            if year < 1582:
                print('No')
            elif year % 4 != 0:
                print('No')
            elif year % 100 != 0:
                print('Yes')
            elif year % 400 != 0:
                print('No')
            else:
                print('Yes')

if __name__ == '__main__':
    main()
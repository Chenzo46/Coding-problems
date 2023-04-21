from math import sqrt
def main():
    cases = int(input())

    for case in range(cases):
        num = int(input())
        print('TRUE' if sqrt(5*num**2 + 4) == int(sqrt(5*num**2 + 4)) or sqrt(5*num**2 - 4) == int(sqrt(5*num**2 - 4)) else 'FALSE')

if __name__ == '__main__':
    main()
from math import floor
def main():
    cases = int(input())

    for case in range(cases):
        year = int(input())

        a = year % 19
        b = year % 4
        c = year % 7
        k = floor(year/100)
        p = floor((13 + 8 * k)/25)
        q = floor(k/4)
        m = (15 - p + k - q) % 30
        n = (4 + k - q) % 7
        d = (19 * a + m) % 30
        e = (2 * b + 4 * c + 6 * d + n) % 7
        f = (11 * m + 11) % 30

        date = 22 + d + e

        date = int(date)

        month = 3 if date <= 31 else 4

        if month == 4:
            date -= 31

        month = str(month).rjust(2,'0')

        if d == 28 and e == 6 and f < 19:
            day = 18
        elif d == 29 and e == 6:
            day = 19
        else:
            day = date
                
        day = str(day).rjust(2,'0')

        print(f'{year}/{month}/{day}')

if __name__ == '__main__':
    main()
def main():
    cases = int(input())

    for case in range(cases):

        amount = float(input()[1:])
        tip_one = amount * .15
        tip_two = amount * .18
        tip_three = amount * .20

        print(f'Total of the bill: ${amount:.2f}')
        print(f'15% = ${tip_one:.2f}')
        print(f'18% = ${tip_two:.2f}')
        print(f'20% = ${tip_three:.2f}')

if __name__ == '__main__':
    main()
def main():
    cases = int(input())

    for case in range(cases):

        amount = float(input()[1:])
        tip_one = round(amount * .15,2)
        tip_two = round(amount * .18,2)
        tip_three = round(amount * .20,2)

        print(f'Total of the bill: ${amount:.2f}')
        print(f'15% = ${tip_one:.2f}')
        print(f'18% = ${tip_two:.2f}')
        print(f'20% = ${tip_three:.2f}')

if __name__ == '__main__':
    main()
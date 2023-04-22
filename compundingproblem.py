def main():
    cases = int(input())

    for case in range(cases):
        
        days = int(input())

        billing_information = [input().split(',') for _ in range(days)]

        sum_of_daily_balance = 0
        daily_balance = 0
        for information in billing_information:
            if information[1] != '':
                daily_balance += float(information[1])
            if information[2] != '':
                daily_balance -= float(information[2])
            sum_of_daily_balance += daily_balance
        
        try:
            interest = (sum_of_daily_balance / days) * 0.015
        except ZeroDivisionError:
            print('$0.00')

        print(f'${interest:.2f}')
if __name__ == '__main__':
    main()
def main():
    cases = int(input())
    
    for case in range(cases):
        #Get cash total
        check = float(input().replace('$',''))
        q = 0
        d = 0
        n = 0
        p = 0

        amountLeft = check
        #take out as much of each coin until all money has been accounted for
        if amountLeft >= 0.25:
            q = int(amountLeft/.25)
            amountLeft -= q*.25
            amountLeft = round(amountLeft,2)
        
        if amountLeft >= 0.1:
            d = int(amountLeft/.1)
            amountLeft -= d*.1
            amountLeft = round(amountLeft,2)

        if amountLeft >= 0.05:
            n = int(amountLeft/.05)
            amountLeft -= n*.05
            amountLeft = round(amountLeft,2)
        
        if amountLeft > 0:
            p = int(round(amountLeft,2)/.01)
            amountLeft -= p*.01
            amountLeft = round(amountLeft,2)

        #print out result
        print(f'${check:.2f}')
        print(f'Quarters={q}')
        print(f'Dimes={d}')
        print(f'Nickels={n}')
        print(f'Pennies={p}')

if __name__ == '__main__':
    main()

def main():
    cases = int(input())

    for case in range(cases):

        num = float(input())
        
        decimal = int(str(num).split('.')[1])
        decimal_length = len(str(decimal))

        terms = [int(num)]

        denominator = pow(10,decimal_length)
        for idx in range(9):
            n_denominator = decimal
            n_numerator = denominator
            count = 0
            while n_numerator >= n_denominator:
                n_numerator -= n_denominator
                count+=1
            terms.append(count)
            decimal = n_numerator
            denominator = n_denominator

            if n_numerator == 0:
                break
        print(' '.join(list(map(str,terms))))

if __name__ == '__main__':
    main()
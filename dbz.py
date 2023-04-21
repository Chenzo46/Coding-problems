def main():
    cases = int(input())

    for case in range(cases):
        division = input().split()
        try:        
            result = float(division[0])/float(division[1])

            print(f'{result:.1f}')
        except ValueError:
            a = False
            try:
                float(division[0])
            except ValueError:
                print('Invalid Dividend')
                a = True
            if a == False: 
                try:
                    float(division[1])
                except ValueError:
                    print('Invalid Divisor')
        except ZeroDivisionError:
            print('Divide By Zero')        

if __name__ == '__main__':
    main()

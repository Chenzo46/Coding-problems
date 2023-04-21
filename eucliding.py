def main():
    cases = int(input())

    for case in range(cases):
        startNums = list(map(int,input().split(',')))
        log = []
        a = startNums[0]
        b = startNums[1]
        while(a != b):
            minuend = a if a > b else b
            subtrahend = b if b < a else a
            diff = minuend - subtrahend
            a = subtrahend
            b = diff
            log.append(f'{minuend}-{subtrahend}={diff}')
        log.append(f'{a}-{b}=0')
        gcd = a
        print('\n'.join(log))
        print('COPRIME' if gcd == 1 else 'NOT COPRIME')
        

if __name__ == '__main__':
    main()
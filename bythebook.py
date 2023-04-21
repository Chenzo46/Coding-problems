def main():
    cases = int(input())

    for case in range(cases):
        isbn = input()

        #get weighted sum
        codeSum = 0

        for c in range(len(isbn)):
            if isbn[c] == 'X':
                codeSum += 10 * (10 - c)
            else:
                codeSum += int(isbn[c]) * (10 - c)
        
        if codeSum % 11 == 0:
            print('VALID')
        else:
            print('INVALID')

if __name__ == '__main__':
    main()
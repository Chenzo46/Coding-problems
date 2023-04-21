def main():
    cases = int(input())

    for case in range(cases):
        boardSize = input().split(',')
        startPos = input().split(',')
        endPos = input().split(',')

        SpairType = 'same' if int(startPos[0])%2 == int(startPos[1])%2 else 'different'

        EpairType = 'same' if int(endPos[0])%2 == int(endPos[1])%2 else 'different'

        if SpairType == EpairType:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
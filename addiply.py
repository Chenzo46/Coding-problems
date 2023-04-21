def main():
    cases = int(input())

    for case in range(cases):
        numPair = list(map(int, input().split(' ')))

        print(str(numPair[0] + numPair[1]) + ' ' + str(numPair[0] * numPair[1]))
        

if __name__ == '__main__':
    main()
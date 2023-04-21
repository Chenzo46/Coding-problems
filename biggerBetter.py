def main():
    cases = int(input())
    for case in range(cases):
        scores = list(map(int, input().split()))
        scores.sort()
        print(scores[len(scores)-1])

if __name__ == '__main__':
    main()
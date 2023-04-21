def main():
    cases = int(input())
    
    for case in range(cases):
        animalCounts = list(map(int, input().split()))

        totalLegs = animalCounts[0]*2 + animalCounts[1]*4 + animalCounts[2]*4
        print(totalLegs)

if __name__ == '__main__':
    main()
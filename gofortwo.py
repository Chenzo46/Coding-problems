def main():
    
    cases = int(input())
    #0-14 down, 16-27 up, 0 diff at 15
    special_cases = [2,1,2,1,2,2,1,2,1,1,2,2,1,2,1,1,2,1,1,1,2,1,1,1,1,1,1,2]
    for _ in range(cases):

        team, opp = list(map(int, input().split()))

        diff = team - opp
        dist = diff + 15
        
        if dist in range(0,27):
            print(special_cases[dist])
        else:
            print(1)

if __name__ == '__main__':
    main()
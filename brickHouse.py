def main():
    cases = int(input())

    for case in range(cases):
        wallInfo = list(map(int,input().split())) # 0: small brick count, 1: large brick count, 2: wall size

        totalBricks = wallInfo[0] + wallInfo[1]

        i = 0
        while wallInfo[2] > 0 or (wallInfo[1] > 0 and wallInfo[0] > 0):
            
            if wallInfo[1] > 0 and wallInfo[2] > 4:
                wallInfo[2] -= 5
                wallInfo[1] -= 1
            elif wallInfo[0] > 0:
                wallInfo[2] -= 1
                wallInfo[0] -= 1

            if i >= totalBricks or wallInfo[2] <= 0:
                break

            i+=1

        if(wallInfo[2] == 0):
            print('true')
        else:
            print('false')



if __name__ == '__main__':
    main()
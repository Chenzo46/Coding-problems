def main():
    cases = int(input())

    for case in range(cases):
        #carInfo = [speed, obstacle distance]
        carInfo = input().split(':')
        carInfo = list(map(float,carInfo))

        try:
            secondsToImpact = carInfo[1] / carInfo[0]
        except:
            #Handles division by zero error
            print("SAFE")
        else:
            if secondsToImpact <= 1:
                print("SWERVE")
            elif secondsToImpact <= 5:
                print("BRAKE")
            else:
                print("SAFE") 
    
if __name__ == "__main__":
    main()
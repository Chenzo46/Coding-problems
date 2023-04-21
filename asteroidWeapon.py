from math import sqrt

def main():
    cases = int(input())
    for case in range(cases):
        asteroidCount = int(input())
        asteroidCords = [] # [0:[x,y,dist], 1:[x,y,dist], ...]
        for i in range(asteroidCount):
            coords = list(map(int,input().split()))

            getDistance = lambda x,y: sqrt(x**2 + y**2)

            #place coords in order
            placementInd = -1
            for c in asteroidCords:
                if getDistance(c[0],c[1]) > getDistance(coords[0], coords[1]):
                    placementInd = asteroidCords.index(c)
                    break
            
            if placementInd == -1:
                asteroidCords.append(coords)
            else:
                asteroidCords.insert(placementInd, coords)

        for c in asteroidCords:
            print(' '.join(list(map(str,c))))
        

if __name__ == '__main__':
    main()
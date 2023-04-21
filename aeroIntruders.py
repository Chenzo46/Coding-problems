class ship:
    def __init__(self, info):
        # parse user input for ship info and store inside variables

        self.info = info

        nameAndClass = info.split('_')

        self.name = nameAndClass[0]
        self.Class = nameAndClass[1][0]

        postion = info.split(':')[1].split(',')

        self.x = int(postion[0])
        self.y = int(postion[1])

        pass

    def advanceX(self):
        if self.Class == 'A':
            self.x -= 10
        elif self.Class == 'B':
            self.x -= 20
        elif self.Class == 'C':
            self.x -= 30

    def destroyedInfo(self) -> str:
        return "Destroyed Ship: " + self.name + " xLoc: " + str(self.x)


def main():
    cases = int(input())

    for case in range(cases):
        shipCount = int(input())

        ships = [ship(input()) for i in range(shipCount)]

        destroyedShips = []

        while len(destroyedShips) < shipCount:
            # Destroy ship with closest x-value
            closestX = abs(ships[0].x)
            desInd = 0
            ind = 0
            for s in ships:
                if closestX > abs(s.x):
                    closestX = abs(s.x)
                    desInd = ind
                elif closestX == abs(s.x):
                    if s.y > ships[desInd].y:
                        desInd = ind
                ind += 1

            destroyedShips.append(ships[desInd])
            ships.remove(ships[desInd])

            # Advance remaining ships
            for s in ships:
                s.advanceX()

        for s in destroyedShips:
            print(s.destroyedInfo())


if __name__ == '__main__':
    main()

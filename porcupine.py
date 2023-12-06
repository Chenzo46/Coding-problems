
class porcupine:
    attack = 0
    health = 0
    level = 0
    
    def __init__(self, attack, health, level) -> None:
        self.attack = attack
        self.health = health
        self.level = level



battles = int(input())

for battle in range(battles):
    jean_pork_count, pierre_pork_count = list(map(int, input().split()))

    #Get Jean porks
    jean_porks = []
    for idx in range(jean_pork_count):
        info = list(map(int,input().split()))
        jean_porks.append(porcupine(info[0], info[1], info[2]))
    
    #Get Pierre porks
    pierre_porks = []
    for idx in range(pierre_pork_count):
        info = list(map(int,input().split()))
        pierre_porks.append(porcupine(info[0], info[1], info[2]))

    

    
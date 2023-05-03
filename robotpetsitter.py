cases = int(input())

for _ in range(cases):

    moves = input()

    h = moves.count('L') - moves.count('R')
    v = moves.count('U') - moves.count('D')

    if h == 0  and v == 0:
        print('TRUE')
    else:
        print('FALSE')
from math import inf
cases = int(input())

for _ in range(cases):
    moves = input()
    r = moves.count('R')
    p = moves.count('P')
    s = moves.count('S')
    moves = set(moves.split())

    if len(moves) == 1 or len(moves) == 3:
        print('NO WINNER')
    elif len(moves) == 2:
        moves = list(moves)
        moveset = ''.join(sorted(moves[0] + moves[1]))

        if moveset == 'PR' and p <= r:
            print('PAPER')
        elif moveset == 'PS' and s <= p:
            print('SCISSORS')
        elif moveset == 'RS' and r <= s:
            print('ROCK')
        else:
            print('NO WINNER')
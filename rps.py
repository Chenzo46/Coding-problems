cases = int(input())

for _ in range(cases):
    moves = input()
    r = moves.count('R')
    p = moves.count('P')
    s = moves.count('S')
    move_dictionary = {'R' : r, 'P' : p, 'S' : s}
    moves = list(set(moves.split()))

    if len(moves) == 3 or len(moves) == 1:
        print("NO WINNER")
    else:
        a = moves[0]
        b = moves[1]
        result = ''.join(list(sorted(a+b)))
        if result == 'PR' and move_dictionary['P'] <= move_dictionary['R']:
            print('PAPER')
        elif result == 'RS' and move_dictionary['R'] <= move_dictionary['S']:
            print('ROCK')
        elif result == 'PS' and move_dictionary['S'] <= move_dictionary['P']:
            print('SCISSORS')
        else:
            print('NO WINNER')
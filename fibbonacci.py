def main():
    cases = int(input())

    for case in range(cases):
        position = int(input())
        fibb = [0,1]
        cur = 1
        def goToPosOnFib(pos,current):
            if pos < 3:
                return f'{pos} = {fibb[pos-1]}'
            elif current == pos-1:
                return None
            fibb.append(fibb[current] + fibb[current-1])
            goToPosOnFib(pos,current+1)
        goToPosOnFib(position, cur)
        print(f'{position} = {fibb[position-1]}')

if __name__ == '__main__':
    main()
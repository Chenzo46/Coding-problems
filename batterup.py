def main():
    cases = int(input())

    for case in range(cases):
        batter = input()

        name = batter.split(':')[0]
        hits = batter.split(':')[1].split(',')

        singles = 0
        doubles = 0
        triples = 0
        homeRuns = 0

        hits = list(filter(lambda h : h != 'BB',hits))

        for i in hits:
            if i == '1B':
                singles += 1
            elif i == '2B':
                doubles += 1
            elif i == '3B':
                triples += 1
            elif i == 'HR':
                homeRuns += 1
            
        try:
            slg = ((singles + 2*doubles + 3*triples + 4*homeRuns)/len(hits))
        except:
            slg = 0
        
        print(f'{name}={slg:.3f}')


if __name__ == '__main__':
    main()
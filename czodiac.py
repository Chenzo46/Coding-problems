def main():
    
    Animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
    Elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']

    cases = int(input())

    for case in range(cases):
        year = int(input())
        #Find if year is Yin or yang
        inang = 'Yang' if year % 2 == 0 else 'Yin'
        #Find year's element
        eYear = year - 4
        eYear %= 10
        eYear /= 2
        eYear = int(eYear)
        element = Elements[eYear]
        #Find year's Animal
        aYear = year - 4
        aYear %= 12
        animal = Animals[aYear]
        #Print out result
        print(f'{year} {inang} {element} {animal}')

if __name__ == '__main__':
    main()
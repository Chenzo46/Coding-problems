def main():
    cases = int(input())

    codeNames = {
        'A' : 'Alpha',
        'B' : 'Bravo',
        'C' : 'Charlie',
        'D' : 'Delta',
        'E' : 'Echo',
        'F' : 'Foxtrot',
        'G' : 'Golf',
        'H' : 'Hotel',
        'I' : 'India',
        'J' : 'Juliet',
        'K' : 'Kilo',
        'L' : 'Lima',
        'M' : 'Mike',
        'N' : 'November',
        'O' : 'Oscar',
        'P' : 'Papa',
        'Q' : 'Quebec',
        'R' : 'Romeo',
        'S' : 'Sierra',
        'T' : 'Tango',
        'U' : 'Uniform',
        'V' : 'Victor',
        'W' : 'Whiskey',
        'X' : 'Xray',
        'Y' : 'Yankee',
        'Z' : 'Zulu'
        }

    for case in range(cases):
        
        sets = int(input())

        wordSets = [input().split() for i in range(sets)]

        for words in wordSets:

            for w in words:
                temp = list(w)
                words[words.index(w)] = temp
                w = temp
                for c in w:
                    if c.upper() in codeNames.keys():
                        words[words.index(w)][w.index(c)] = codeNames[c.upper()]

                words[words.index(w)] = '-'.join(w)
            
            print(' '.join(words))

if __name__ == '__main__':
    main()
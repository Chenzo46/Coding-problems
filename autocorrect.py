from math import inf

def main():
    cases = int(input())

    for case in range(cases):
        wordSize = input().split()

        dictionary = [input() for i in range(int(wordSize[0]))]
        badWords = [input() for i in range(int(wordSize[1]))]

        for word in badWords:
            differences = []
            #Get differences for all word comparisons
            for gw in dictionary:
                d = 0
                if len(gw) == len(word):
                    for i in range(len(gw)):
                        if gw[i] != word[i]:
                            d += 1
                else:
                    d = inf
                differences.append(d)
            #Find Dictionary word with least differences
            goodWordInd = 0
            smallestDiff = differences[0]
            for num in range(len(differences)):
                if smallestDiff > differences[num]:
                    smallestDiff = differences[num]
                    goodWordInd = num
            print(dictionary[goodWordInd])


if __name__ == '__main__':
    main()
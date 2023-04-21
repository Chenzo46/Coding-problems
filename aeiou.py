def main():
    cases = int(input())
    vowels =  ['a','e','i','o','u']
    for case in range(cases):
        sentence = [*input()] #unpack input into array of individual characters
        sentenceVowels = list(filter(lambda character : character.lower() in vowels, sentence)) #filter vowels out of sentence input

        print(len(sentenceVowels))

if __name__ == '__main__':
    main()
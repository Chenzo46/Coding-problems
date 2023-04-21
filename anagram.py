def main():
    cases = int(input())
    for case in range(cases):
        allegedAnagrams = input()

        anagrams = allegedAnagrams.split('|') #Seperate words

        if (''.join(sorted(anagrams[0])) == ''.join(sorted(anagrams[1]))) and not anagrams[0] == anagrams[1]: #check if the words sorted in alphabetical order are the same and if the words are not the same to being with
            print(allegedAnagrams + " = ANAGRAM")
        else:
            print(allegedAnagrams + " = NOT AN ANAGRAM")

if __name__ == '__main__':
    main()
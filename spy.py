def main():
    cases = int(input())

    for case in range(cases):
        sentences = input().lower().split('|')
        
        sentences[0] = list(filter(lambda s : s.isalpha(),sentences[0]))
        sentences[1] = list(filter(lambda s : s.isalpha(),sentences[1]))

        result = "That's my secret contact!"

        for c in sentences[1]:
            if c not in sentences[0]:
                result = "You're not a secret agent!"
        
        print(result)

if __name__ == '__main__':
    main()
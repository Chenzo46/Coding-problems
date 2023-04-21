def main():
    cases = int(input())
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for case in range(cases):
        lines = int(input())
        sentences = [input() for _ in range(lines)]
        sentences = list(map(lambda x: ''.join(list(filter(lambda y: y.isalpha(), x))),sentences))
        
        alphabet_occurences = {value.upper():0 for (key,value) in enumerate(alphabet)}
        
        total_lengths = 0
        
        for sentence in sentences:
            total_lengths += len(sentence)
            for c in sentence:
                if c.isalpha():
                    alphabet_occurences[c.upper()] += 1
        
        for k,v in alphabet_occurences.items():
            n_v = (v / total_lengths) * 100
            print(f'{k}: {n_v:.2f}%')
        

if __name__ == '__main__':
    main()
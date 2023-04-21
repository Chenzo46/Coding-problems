def main():
    cases = int(input())
    for case in range(cases):
        sentence_count = int(input())
        sentences = [input() for _ in range(sentence_count)]
        sentences = list(map(lambda x: ''.join(list(filter(lambda y: y.isalpha() or y == ' ', x))).split(),sentences))
        print(sentences)
        # Get digraphs
        digraphs = dict()
        for sentence in sentences:
            for word in sentence:
                for c in range(len(word)-1):
                    key_to_add = (word[c]+word[c+1]).upper()
                    if key_to_add not in digraphs.keys():
                        digraphs[key_to_add] = 0
                    digraphs[key_to_add] += 1

        digraph_keys = list(digraphs.keys())
        digraph_keys.sort()
        digraphs_sorted = {digraph_keys[i]:digraphs[digraph_keys[i]] for i in range(len(digraph_keys))}
        # Print digraphs
        for key,val in digraphs_sorted.items():
            n_val = (val / len(digraphs_sorted)) * 100
            print(f'{key}: {n_val:.3f}%')

        # Get trigraphs
        trigraphs = dict()
        for sentence in sentences:
            for word in sentence:
                for c in range(len(word)-2):
                    key_to_add = (word[c]+word[c+1]+word[c+2]).upper()
                    if key_to_add not in digraphs.keys():
                        trigraphs[key_to_add] = 0
                    trigraphs[key_to_add] += 1
        trigraph_keys = list(trigraphs.keys())
        trigraph_keys.sort()
        print(len(trigraph_keys))
        trigraphs_sorted = {trigraph_keys[i]:trigraphs[trigraph_keys[i]] for i in range(len(trigraph_keys))}
        # Print Trigraphs
        for key,val in trigraphs_sorted.items():
            n_val = (val / len(trigraphs_sorted)) * 100
            print(f'{key}: {n_val:.3f}%')

if __name__ == '__main__':
    main()
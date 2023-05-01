def main():
    cases = int(input())
    for case in range(cases):
        sentence_count = int(input())
        sentences = [input() for _ in range(sentence_count)]
        sentences = list(map(lambda x: ''.join(list(filter(lambda y: y.isalpha() or y == ' ', x))).split(),sentences))
        # Get digraphs
        digraphs = dict()
        digraph_total = 0
        for sentence in sentences:
            for word in sentence:
                for c in range(len(word)-1):
                    key_to_add = (word[c]+word[c+1]).upper()
                    if key_to_add not in digraphs.keys():
                        digraphs[key_to_add] = 0
                    digraphs[key_to_add] += 1
                    digraph_total+=1

        digraph_keys = list(digraphs.keys())
        digraph_keys.sort()
        digraphs_sorted = {digraph_keys[i]:digraphs[digraph_keys[i]] for i in range(len(digraph_keys))}
        # Print digraphs
        for key,val in digraphs_sorted.items():
            n_val = (val / digraph_total) * 100
            print(f'{key}: {n_val:.3f}%')

        # Get trigraphs
        trigraphs = dict()
        trigraph_total = 0
        for sentence in sentences:
            for word in sentence:
                for c in range(len(word)-2):
                    key_to_add = (word[c]+word[c+1]+word[c+2]).upper()
                    if key_to_add not in trigraphs.keys():
                        trigraphs[key_to_add] = 0
                    trigraphs[key_to_add] += 1
                    trigraph_total += 1
        trigraph_keys = list(trigraphs.keys())
        trigraph_keys.sort()
        trigraphs_sorted = {trigraph_keys[i]:trigraphs[trigraph_keys[i]] for i in range(len(trigraph_keys))}
        # Print Trigraphs
        for key,val in trigraphs_sorted.items():
            n_val = (val / trigraph_total) * 100
            print(f'{key}: {n_val:.3f}%')

if __name__ == '__main__':
    main()
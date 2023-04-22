cases = int(input())

for case in range(cases):
    word, idx = input().split()
    idx = int(idx)
    word = list(word)
    word[idx] = ''
    print(''.join(word))
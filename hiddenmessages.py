cases = int(input())-1

decoding_key = input()

message = []

def decode_word(x:str)->str:
    word = ''
    x = x.split('-')
    word = list(map(lambda y: decoding_key[int(y)-1], x))
    return ''.join(word)

for _ in range(cases):
    words = input().split()
    words = ' '.join(list(map(decode_word, words)))
    message.append(words)

for line in message:
    print(line)
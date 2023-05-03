cases = int(input())
vowels = 'aeiou'
for _ in range(cases):
    message = input()
    decrypted = ''
    next_c = False
    for c in message:
        if c in vowels and not next_c:
            next_c = True
        elif next_c:
            decrypted += c
            next_c = False
    print(decrypted)
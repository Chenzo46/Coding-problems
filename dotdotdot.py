ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(int(input())):
    word = input()
    click_count = 0
    for c in word:
        click_count += ALPHABET.index(c) + 1
    print(click_count)
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(int(input())):
    plain_text = input()
    keyword = input()

    cipher_text = ''
    offset = 0
    for idx in range(len(plain_text)):
        key_letter = keyword[(idx-offset)%len(keyword)]
        plain_letter = plain_text[idx]

        if plain_letter == ' ':
            cipher_text += ' '
            offset += 1
            continue

        new_index = alphabet.index(key_letter) + alphabet.index(plain_letter)

        cipher_text += alphabet[new_index%26]

    print(cipher_text)



cases = int(input())
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_CAPITAL = ALPHABET.upper()
for case in range(cases):
    method = input()
    key = input()
    word_count = int(input())
    words = [input() for idx in range(word_count)]
    if method == "ENCRYPT":
        #Do encryption here
        for word in words:
            encrypted_mess = ''
            for letter in word:
                if letter == ' ':
                    encrypted_mess += letter
                else:
                    position = ord(letter)-97 if letter.islower() else ord(letter)-65
                    encrypted_mess += key[position] if letter.islower() else key[position].upper()
            print(encrypted_mess)
    else:
        for word in words:
            decrypted_mess = ''
            for letter in word:
                if letter == ' ':
                    decrypted_mess += letter
                else:

                    position = key.lower().index(letter.lower())
                    decrypted_mess += ALPHABET[position] if letter.islower() else ALPHABET_CAPITAL[position]
            print(decrypted_mess)
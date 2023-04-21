def main():
    cases = int(input())
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for case in range(cases):
        key = int(input())
        encrypted_message = input()

        key %= 26

        decrypted_message = ''
        for i in encrypted_message:
            if i in alphabet:
                ind = alphabet.index(i)
                ind -= key
                decrypted_message += alphabet[ind]
            else:
                decrypted_message += i
        print(decrypted_message)

if __name__ == '__main__':
    main()
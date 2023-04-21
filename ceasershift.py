def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cases = int(input())
    for case in range(cases):
        encrypted_message = input().lower()
        shift_values = input().split()
        direction_values = input().split()

        decrypted_message = ''
        idx = 0
        for character in encrypted_message:
            if character.isalpha():
                direction = 1 if int(direction_values[idx % len(direction_values)]) == 0 else -1
                new_character = alphabet[(alphabet.index(character) + int(shift_values[idx % len(shift_values)]) * direction) % 26]
                decrypted_message += new_character
                idx += 1
            else:
                decrypted_message += character
        print(decrypted_message)

if __name__ == '__main__':
    main()
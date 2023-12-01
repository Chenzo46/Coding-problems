import math
importent_letters = "ADFGVX"

def decrypt_message(keyword, encryption_table, encrypted_message):
    message = ""
    message_remainder_number = len(encrypted_message) % len(keyword)
    noremainder_message = encrypted_message[0:len(encrypted_message)-message_remainder_number]
    message_remainder = encrypted_message[-message_remainder_number:]
    semideciphered_message = str()
    sorted_keyword = sorted(keyword)
    keyword_table = dict()
    alias_list = list()
    for letter in sorted_keyword:
        keyword_table[letter] = list()
    
    for index, letter in enumerate(noremainder_message):
        keyword_table[sorted_keyword[index % len(keyword)]].append(letter)
    if message_remainder_number > 0:
        for index, letter in enumerate(message_remainder):
            keyword_table[keyword[index]].append(letter)    
    ylength = len(encrypted_message)/len(keyword)
    for y in range(0, math.ceil(ylength)):
        for x in range(0, len(keyword)):
            keyword_letter = keyword[x]
            try:
                letter = keyword_table[keyword_letter][y]
                alias_list.append(letter)
            except:
                pass

    for index, letter in enumerate(encrypted_message):
        semideciphered_message = semideciphered_message + alias_list[index]
    
    for index in range(0, len(semideciphered_message), 2):
        x = importent_letters.index(semideciphered_message[index])
        y = importent_letters.index(semideciphered_message[index+1])
        message += encryption_table[x][y]
    return message
def main():
    testcases = int(input())
    answers = []
    for _ in range(testcases):
        encryption_table = []
        for _ in range(6):
            encryption_table.append(input())
        keyword = input()
        encrypted_message = input()
        answers.append(decrypt_message(keyword=keyword, encrypted_message=encrypted_message, encryption_table=encryption_table))
        for answer in answers:
            print(answer)
main()
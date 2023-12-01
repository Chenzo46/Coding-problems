silly_configuration = 'ADFGVX'

for _ in range(int(input())):
    #Receive Inputs
    guggy_macaroni_table = [input() for idx in range(6)]
    keyword = input()
    encrypted_message = input()
    #Sort the keyword
    sorted_keyword = list(sorted(keyword))
    #Create Table of sorted keywords
    sorted_keyword_table = {sorted_keyword[idx]:'' for idx in range(len(keyword))}
    #Assign letters of encrypted message to each letter column of sorted keyword table
    remainder_of_letters = len(encrypted_message) % len(keyword)

    for idx,letter in enumerate(encrypted_message):
        if idx == len(encrypted_message) - remainder_of_letters:
            break
        letter_location = idx%len(keyword)
        sorted_keyword_table[list(sorted_keyword_table.keys())[letter_location]] += letter
    
    #Handle the remainder of letters
    letters_remaining = encrypted_message[len(encrypted_message) - remainder_of_letters:len(encrypted_message)]
    
    for letter in sorted_keyword:
        if keyword.index(letter)+1 <= remainder_of_letters:
            sorted_keyword_table[letter] += letters_remaining[0]
            letters_remaining = letters_remaining[1:len(letters_remaining)] 

    #Unsort the sorted keyword table
    normal_keyword_table = {keyword[idx]:sorted_keyword_table[keyword[idx]] for idx in range(len(keyword))}

    # Extract encrypted text from table
    #DISCLAIMER: This code shouldn't work but it does
    encrypted_message_filtered = ''
    for cdx in range(0, int(len(encrypted_message) / len(keyword)) + remainder_of_letters):
        for adx in range(0, len(keyword)):
            try:
                encrypted_message_filtered += normal_keyword_table[keyword[adx]][cdx]
            except:
                break
    
    #Convert letter pairs to normal letters from the given guggy macaroni table
    decrypted_message = ''
    for idx in range(0, len(encrypted_message_filtered), 2):
        letter = encrypted_message_filtered[idx:idx+2]
        row = silly_configuration.index(letter[0])
        column = silly_configuration.index(letter[1])
        decrypted_message += guggy_macaroni_table[row][column]
    print(decrypted_message)
    



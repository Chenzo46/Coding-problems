def filter_message(unfiltered_message:str, token:str) -> str:
    filtered_message = ''
    adjacent_count = 0
    prev_c = ''
    just_removed = False
    for c in unfiltered_message:
        if prev_c == c and c in token and not just_removed:
            adjacent_count += 1
        else:
            adjacent_count = 0
        just_removed = False
        if adjacent_count > 0:
            adjacent_count = 0
            just_removed = True
        else:
            filtered_message += c
        prev_c = c
    return filtered_message

for _ in range(int(input())):
    data_length = int(input())
    data_stream = input()
    three_letter_pairs = []
    for c in range(0,len(data_stream)-2):
        three_letter_pairs.append(data_stream[c:c+3])
    three_letter_pairs = three_letter_pairs
    final_messages = []
    temp_data_stream = data_stream
    for token in three_letter_pairs:
        rev_token = ''.join(list(reversed(token)))
        token_found = token in temp_data_stream and rev_token in temp_data_stream
        while token_found:
            
            try:
                token_index = temp_data_stream.index(token)
                rev_token_index = temp_data_stream.index(rev_token)
            except: break
            
            unfiltered_message = temp_data_stream[token_index+3:rev_token_index]
            if unfiltered_message == '':
                break
            filtered_message = filter_message(unfiltered_message, token)
            final_messages.append(filtered_message)
            temp_data_stream = temp_data_stream.replace(token,'',1)
            temp_data_stream = temp_data_stream.replace(rev_token,'',1)
    
    print('\n'.join(final_messages))

    

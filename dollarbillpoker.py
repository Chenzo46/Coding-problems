for _ in range(int(input())):
    org_serial_number = input()
    serial_number = org_serial_number.replace('0','',-1)
    unique_numbers = list(set(serial_number))
    
    serial_number_dict = {unique_numbers[idx] : serial_number.count(unique_numbers[idx]) for idx in range(len(unique_numbers))}
    highest_occurences = max(serial_number_dict.values())

    #Check first two conditions
    if highest_occurences == 5:
        print(f'{org_serial_number} = FIVE OF A KIND')
        continue
    elif highest_occurences == 4:
        print(f'{org_serial_number} = FOUR OF A KIND')
        continue
    
    #Check For Full House
    sorted_serial_number_dict = list(sorted(serial_number_dict.items(), key = lambda x:x[1]))
    sorted_serial_number_dict = list(map(list,sorted_serial_number_dict))
    
    if sorted_serial_number_dict[len(sorted_serial_number_dict)-1][1] == 3 and sorted_serial_number_dict[len(sorted_serial_number_dict)-2][1] >= 2:
        print(f'{org_serial_number} = FULL HOUSE')
        continue
    
    #Check for Straight
    serial_number_sorted = list(sorted(serial_number))
    current_num = int(serial_number_sorted[0])
    counter = 1
    five_sequential = False

    for idx in range(1,len(serial_number_sorted)):
        if current_num+1 == int(serial_number_sorted[idx]):
            counter += 1
            current_num = int(serial_number_sorted[idx])
        else:
            counter = 0
            current_num = int(serial_number_sorted[idx])
        
        if counter == 5:
            five_sequential = True
            break
    
    if five_sequential:
        print(f'{org_serial_number} = STRAIGHT')
        continue
    
    #Check for three of a kind
    if highest_occurences == 3:
        print(f'{org_serial_number} = THREE OF A KIND')
        continue
    
    #Check for two pair
    two_counts = list(filter(lambda x : x == 2, serial_number_dict.values()))

    if len(two_counts) >= 2:
        print(f'{org_serial_number} = TWO PAIR')
        continue
    
    #Check for pair
    if highest_occurences == 2:
        print(f'{org_serial_number} = PAIR')
        continue
    
    #Print out single greatest number
    print(f'{org_serial_number} = {max(unique_numbers)}')
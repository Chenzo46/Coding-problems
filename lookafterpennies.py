from math import ceil

for _ in range(int(input())):
    #Take all inputs
    charge_count = int(input())
    amount_saved = 0
    charges = [input() for i in range(charge_count)]
    #Parse inputs
    for charge in charges:
        current_charge = charge
        change = '100'
        if '.' in current_charge: #If change gives a decimal then extract out the change
            change = current_charge.split('.')[1]
            change = '100' if int(change) == 0 else change
        rounded_charge = ceil(float(current_charge)) # Round the charge up to the nearest whole number
        amount_saved += 100 - int(change) #Get how much change to save
        print(rounded_charge)
    
    print(f'{amount_saved/100:.2f}') #Devide change by 100 and format it to always show the leading zeros
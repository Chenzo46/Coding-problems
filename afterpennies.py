from math import ceil,floor

def main():
        
    cases = int(input())
    for case in range(cases):
        charge_count = int(input())

        charges = [float(input()) for _ in range(charge_count)]
        new_charges = []
        
        extra_change = 0
        for charge in charges:

            pennies = ceil((charge % 1) * 100)
            pennies = 100 - pennies if pennies > 0 else 0
            extra_change += pennies/100
            print(f'EX: {extra_change}')
            charge = str(ceil(charge))
            new_charges.append(str(charge))

        print('\n'.join(new_charges))
        print(str(extra_change).ljust(3,'0'))

if __name__ == '__main__':
    main()

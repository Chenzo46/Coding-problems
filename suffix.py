ENDINGS = ['st','nd','rd']
for _ in range(int(input())):
    num = input()
    num = num[0:len(num)-2]
    num_last = int(num[len(num)-1])

    if int(num[len(num)-2:]) in range(10,20) or num_last not in [1,2,3]:
        print(num + 'th')
    else:
        print(f'{num}{ENDINGS[int(num_last)-1]}')
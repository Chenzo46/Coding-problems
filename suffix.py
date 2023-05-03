cases = int(input())

for _ in range(cases):

    num = input()
    extension = ''
    idx = -1
    n = 0
    for c in range(len(num)):
        if num[c].isalpha():
            n = int(num[c-1])
            f_n = int(num[:c])
            idx = c
            if n == 1 and f_n < 10 or f_n > 19:
                extension = 'st'
            elif n == 2 and f_n < 10 or f_n > 19:
                extension = 'nd'
            elif n == 3 and f_n < 10 or f_n > 19:
                extension = 'rd'
            else:
                extension = 'th'
            break
    
    print(f'{num[:idx]}{extension}')
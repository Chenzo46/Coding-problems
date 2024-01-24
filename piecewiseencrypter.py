ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    for _ in range(int(input())):
        message = input()
        message = list(map(lambda x : ALPHABET.index(x)+1, message))
        message = list(map(lambda x: encrypt_letter(x), message))
        print(''.join(message))

def encrypt_letter(num:int)->str:
    f_num = None
    if num in range(1,6):
        f_num = num+6
    elif num in range(6,11):
        f_num = num**2
    elif num in range(11,16):
        f_num = (num%3)*5 + 1
    elif num in range(16,21): #Multiply sum of digits by 8
        num = str(num)
        f_num =  (int(num[0]) + int(num[1])) * 8
    else:
        f_num = get_greatest_factor(num)*2
    
    f_num = num if f_num == 0 else f_num
    f_num = f_num % 26 if f_num > 26 else f_num

    return ALPHABET[f_num-1]
        
def get_greatest_factor(num:int)->int:
    greatest_factor = 0
    for n in range(1,num):
        if (num / n) % 1 == 0:
            greatest_factor = n
    
    return greatest_factor

if __name__ == '__main__':
    main()
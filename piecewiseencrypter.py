
def main():
    ALPHABET = 'ABCDEGHIJKLMNOPQRSTUVWXYZ'    
    #ord(char) + 64 gives us the associated asci character and vice-versa 
    for _ in range(int(input())):
        message = input()
        message = list(map(lambda x : ord(x) - 64, message)) # produces list of characters with values from 1-26

def encrypt_letter(num:int)->int:
    if num in range(1,6):
        return num+6
    elif num in range(6,11):
        return num**2
    elif num in range(11,16):
        return (num%3)*5 + 1
    elif num in range(16,21): #Multiply sum of digits by 8
        pass
    else:
        pass

if __name__ == '__main__':
    main()
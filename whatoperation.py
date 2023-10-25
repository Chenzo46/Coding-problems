for _ in range(int(input())):
    a,b,r = list(map(int, input().split()))
    if a + b == r:
        print('Addition')
        continue
    elif a - b == r:
        print("Subtraction")
        continue
    elif a * b == r:
        print("Multiplication")
        continue
    
    try:
        if int(a/b) == r:
            print("Division")
            continue
        elif a % b == r:
            print("Modulo")
            continue
    except:
        pass
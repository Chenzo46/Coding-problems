for _ in range(int(input())):
    special = input()
    not_special = ''.join(list(filter(lambda c: c == " " or c.isalpha() or c.isdigit(),special)))
    print(not_special)
cases = int(input())
for _ in range(cases):

    name_count = int(input())

    for idx in range(name_count):
        name = input().split()
        print((name[0][0] + name[2][0] + name[1][0]).upper())
        
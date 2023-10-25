print(3 % 0)
for n in range(int(input())):
    out = ""
    i = 1
    for s in input().split(" "):
        if s == "M":
            out += str(i) + " "
        i += 1
    print(out.strip())

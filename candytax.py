years  = int(input())

for yr in range(years):
    bag_count, siblings = list(map(int,input().split()))
    bags = list(map(int,input().split()))

    divisible_pairs = []

    for idx in range(bag_count):
        for jdx in range(idx+1, bag_count):
            if (bags[idx] + bags[jdx]) % siblings == 0 and not bags[jdx] == 0:
                divisible_pairs.append(bags[idx] + bags[jdx])
    try:
        print(int(max(divisible_pairs) / siblings))
    except:
        print(0)
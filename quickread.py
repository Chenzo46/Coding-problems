cases = int(input())

for _ in range(cases):

    w1, w2 = input().split()
    
    print(w2 if w1[0] == w2[0] and w1[len(w1)-1] == w2[len(w2)-1] and sorted(w1) == sorted(w2) else w1)
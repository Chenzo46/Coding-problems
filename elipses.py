from math import sqrt

def main():
    cases = int(input())

    for _ in range(cases):
        X_1, Y_1, X_2, Y_2, W, N = list(map(float, input().split()))

        for i in range(int(N)):
            x, y = list(map(float, input().split()))
            
            dist_a = sqrt(pow(x - X_1, 2) + pow(y - Y_1, 2))
            dist_b = sqrt(pow(x - X_2, 2) + pow(y - Y_2, 2))

            length = dist_a + dist_b
            print(1 if length <= W else 0)

if __name__ == '__main__':
    main()
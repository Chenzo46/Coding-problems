def main():
    cases = int(input())
    grid = [
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    ]
    for case in range(cases):
        position = list(map(int,input().split()))

        grid[position[0]][position[1]] = 100
        


if __name__ == '__main__':
    main()
def main():
    cases = int(input())

    for case in range(cases):
        side_lengths = list(map(int, input().split(', ')))
        side_lengths.sort()
        side_sum = side_lengths[0] + side_lengths[1]
        
        if side_sum <= side_lengths[2]:
            print('Not a Triangle')
            continue

        side_lengths = set(side_lengths)
        unique_sides = len(side_lengths)
        if unique_sides == 1:
            print('Equilateral')
        elif unique_sides == 2:
            print('Isosceles')
        elif unique_sides == 3:
            print('Scalene')

if __name__ == '__main__':
    main()
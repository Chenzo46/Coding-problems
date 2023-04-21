def main():
    cases = int(input())

    for case in range(cases):

        list_count = int(input())
        converted_values = [float(input()) for _ in range(list_count)]
        
        small = min(converted_values)
        big = max(converted_values)

        converted_values = list(map(lambda x: str(int(round((x - small)/(big-small) * 255, 0))), converted_values))
        print('\n'.join(converted_values))

if __name__ == '__main__':
    main()
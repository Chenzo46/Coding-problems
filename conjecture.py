def main():
    cases = int(input())

    for case in range(cases):
        start = int(input())

        temp = start

        length = 1

        while(temp != 1):
            temp = temp / 2 if temp % 2 == 0 else (temp * 3) + 1
            length += 1

        print(f'{start}:{length}')



if __name__ == '__main__':
    main()
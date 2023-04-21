def main():
    cases = int(input())

    for case in range(cases):
        density, volume = input().split()
        mass = round(float(density)*float(volume),2)
        print(f'{mass:.2f}')


if __name__ == '__main__':
    main()
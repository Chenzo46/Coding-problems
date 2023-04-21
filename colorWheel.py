def main():
    cases = int(input())

    primaryColors = ['red','blue','yellow']

    for case in range(cases):
        colorToMake = input()

        if colorToMake not in primaryColors:
            if 'orange' in colorToMake:
                print(f'In order to make {colorToMake}, {primaryColors[0]} and {primaryColors[2]} must be mixed.')
            elif 'violet' in colorToMake:
                print(f'In order to make {colorToMake}, {primaryColors[1]} and {primaryColors[0]} must be mixed.')
            elif 'green' in colorToMake:
                print(f'In order to make {colorToMake}, {primaryColors[1]} and {primaryColors[2]} must be mixed.')
        else:
            print(f'No colors need to be mixed to make {colorToMake}.')

if __name__ == '__main__':
    main()
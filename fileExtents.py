def main():
    cases = int(input().strip())

    files = [input().strip().split('.')[1] for i in range(cases)]

    fileNameCounts = []

    for f in files:
        if f'{f} {files.count(f)}' not in fileNameCounts:
            fileNameCounts.append(f'{f} {files.count(f)}')

    print('\n'.join(fileNameCounts))

if __name__ == '__main__':
    main()
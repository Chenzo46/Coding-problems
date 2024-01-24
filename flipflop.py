def main():
    for _ in range(int(input())):
        r_column, c_row = list(map(int,input().split()))

        rows = [[] for idx in range(c_row)]

        for idx in range(r_column):
            values = input().split(',')
            for jdx in range(len(values)):
                rows[jdx].append(values[jdx])
        
        for row in rows:
            print(','.join(row))

if __name__ == '__main__':
    main()
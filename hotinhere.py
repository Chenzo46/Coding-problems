def main():
    cases = int(input())

    for case in range(cases):

        temp_conversions = int(input())

        for conversion in range(temp_conversions):
            temp, unit = input().split()
            org_temp = temp
            temp = float(temp)
            con =  (5/9) * (temp - 32) if unit == 'F' else (9/5) * temp + 32
            con_unit = 'C' if unit == 'F' else 'F'
            con = round(con,1)
            print(f'{org_temp} {unit} = {con} {con_unit}')

if __name__ == '__main__':
    main()
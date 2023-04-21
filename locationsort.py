cases = int(input())
countries = []
for case in range(cases):
    countries.append(input())
countries.sort()
print('\n'.join(countries))

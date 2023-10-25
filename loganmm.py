from decimal import *
# 2 Decimals places


def getAmountOfTests() -> int:
    amountOfTests = int(input())
    return amountOfTests
def renderGraph(data: list, country):
    print(f"{country}:")
    for YEAR, GDP_PER_CAPITA in data:
        lengthOfBar = int(Decimal(GDP_PER_CAPITA/1000).quantize(Decimal('1.'), rounding=ROUND_HALF_UP))
        bar = "*"*lengthOfBar
        print(f"{YEAR} {bar}")
def sortData(data: list):
    data = sorted(data, key=lambda x: x[0])
    return data

def gdpGraph(country):
    amountOfYears = int(input())
    data = []
    YEARS = []
    for r in range(amountOfYears):
        PER_CAPITA_INCOME, YEAR = input().split(" ")
        PER_CAPITA_INCOME = Decimal(PER_CAPITA_INCOME)
        YEAR = int(YEAR)
        data.append((YEAR, PER_CAPITA_INCOME))
    data = sortData(data)
    renderGraph(data, country)
def main():
    amountOfTests = getAmountOfTests()

    for r in range(amountOfTests):
        country = input()
        gdpGraph(country)

if __name__ == "__main__":
    main()
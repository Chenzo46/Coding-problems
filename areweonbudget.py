from decimal import *
def main():
    cases = int(input())

    for case in range(cases):
        costs_count = int(input())
        budget = input().split()
        actual_cost = input().split()
        cost_variances = [float(actual_cost[i]) - float(budget[i]) for i in range(costs_count)]
        cost_variances_sum = sum(cost_variances)
        average_cost_variance = Decimal(cost_variances_sum/costs_count).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        print(average_cost_variance)

if __name__ == '__main__':
    main()
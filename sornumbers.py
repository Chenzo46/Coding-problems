cases = int(input())

for case in range(cases):
    nums = input().split(',')
    nums = list(map(int, nums))
    nums.sort()
    nums = list(map(str,nums))
    print(','.join(nums))
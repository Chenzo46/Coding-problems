import itertools

for _ in range(int(input())):
    case_sum = int(input().split('=')[1])
    nums = list(map(int,input().split(',')))

    max_length = len(nums)

    answers = []
    for rnd in range(1,len(nums)):
        permutations = map(lambda x: '+'.join(map(str,x)),sorted(filter(lambda x : sum(x) == case_sum, set(itertools.permutations(nums, max_length)))))
        answers.extend(permutations)
        max_length -= 1

    print(*answers, sep = '\n')
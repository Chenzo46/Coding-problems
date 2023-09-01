def main():
    
    cases  = int(input())

    for _ in range(cases):
        n_sum = int(input().split('=')[1])
        nums = list(map(int, input().split(',')))

        for n,i in enumerate(nums):
            #For each number find all pairs,trios,etc. that add to n_sum
            for m,j in enumerate(nums):
                if i == j:
                    continue

                

        

if __name__ == '__main__':
    print(int('01', 2))
    #main()
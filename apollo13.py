import decimal
def main():
    cases = int(input())

    for case in range(cases):
        gimbalAngles = list(map(lambda x : float(x) - 180,input().split()))

        for i in range(len(gimbalAngles)):
            if gimbalAngles[i] < 0:
                gimbalAngles[i] = 360 + gimbalAngles[i]
            gimbalAngles[i] = str(round(gimbalAngles[i],2))

            #Add zeros (Stupid dumb bullshit code)
            if not len(gimbalAngles[i]) == 6:
                nums = gimbalAngles[i].split('.')
                for c in range(len(nums)):
                    if c == 0:
                        zeros = 3 - len(nums[c])
                        add = ''
                        for x in range(zeros):
                            add += '0'
                        add += nums[c]
                        nums[c] = add
                    elif c == 1:
                        zeros = 2 - len(nums[c])
                        add = ''
                        for x in range(zeros):
                            add += '0'
                        nums[c] += add
                gimbalAngles[i] = '.'.join(nums)

        print(f'{gimbalAngles[0]} {gimbalAngles[1]} {gimbalAngles[2]}')

if __name__ == '__main__':
    main()

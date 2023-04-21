def main():
    cases = int(input())

    for case in range(cases):
        lastYear = input().split(',')
        thisYear = input().split(',')

        missing = []
        both = []
        
        for person in lastYear:
            if not person in thisYear:
                missing.append(person)
            elif person in thisYear:
                both.append(person)
                #If the person from last year isn't in this year's list, handle the error and skip it
                try:
                    thisYear.remove(person)
                except:
                    pass
        
        missing.sort()
        both.sort()
        thisYear.sort()

        print(','.join(missing))
        print(','.join(both))
        print(','.join(thisYear))

            

if __name__ == '__main__':
    main()
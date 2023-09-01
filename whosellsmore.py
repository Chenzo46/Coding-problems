for _ in range(int(input())):
    
    times, herald = list(map(int, input().split()))
    message = ''
    if times == herald:
        message = 'Times and Herald have the same number of subscribers'
    else:
        message = f'Times has {times-herald} more subscribers' if times > herald else f'Herald has {herald-times} more subscribers'
    print(message)
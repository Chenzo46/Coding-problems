for _ in range(int(input())):
    n = int(input())
    m_3 = n % 3 == 0
    m_7 = n % 7 == 0

    if m_3 and m_7:
        print('LOCKHEEDMARTIN')
    elif m_3:
        print('LOCKHEED')
    elif m_7:
        print('MARTIN')
    else:
        print(n)
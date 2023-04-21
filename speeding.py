def main():
    cases = int(input())

    for case in range(cases):
        
        speedAndBirth = input().split()

        birdayEx = 0

        if speedAndBirth[1] == 'true':
            birdayEx = 5
        
        speed = int(speedAndBirth[0])

        if speed <= 60 + birdayEx:
            print('no ticket')
        elif speed <= 80 + birdayEx:
            print('small ticket')
        else:
            print('big ticket')

if __name__ == '__main__':
    main()
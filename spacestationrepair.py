def main():
    states = ['off', 'red', 'green', 'blue']
    for _ in range(int(input())):
        a = 0
        b = 0
        t = 0

        machine_states = input().split()
        for i,s in enumerate(machine_states):
            if s[0] == 'B':
                if i == 0:
                    t += 8
                elif i == 1:
                    t += 4
                elif i == 2:
                    t += 2
                elif i == 3:
                    t += 1

        if t <= 3:
            b = t
        elif t <= 7 and t > 3:
            b = t - 4
        elif t <= 11 and t > 7:
            b = t - 8
        elif t <= 15 and t > 11:
            b = t - 12

        a = int(t/4)
        print(b)
        print(f'{states[a]} {states[b]}')

if __name__ == '__main__':
    main()

"""
Psuedo Code:
    t = 4a + b
    LEDS: [0,1,2,3]
    SYSTEMS: [8,4,2,1]

    domain: (t <= 15, t >= 0)

    t <= 15 and t > 11:
        a = 3
        b = t - 12
    t <= 11 and t > 7:
        a = 2
        b = t - 8
    t <= 7 and t > 3:
        a = 1
        b = t - 4
    t <= 3:
        a = 0
        b = t

    a = int(t/4)
    b = t - t(int(t/4))
"""
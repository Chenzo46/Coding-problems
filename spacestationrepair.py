def main():
    states = ['off', 'red', 'green', 'blue']
    for _ in range(int(input())):
        a = 0
        b = 0
        t = 0
        machine_states = input().split()
        for i,s in enumerate(machine_states):
            if s[0] == 'B':
                t += int(round(8/(1 + pow(i,2)))) # rounded approximation that works for the given range
        a = int(t/4)
        b = t - 4*a
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
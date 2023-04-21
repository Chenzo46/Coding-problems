def main():
    cases = int(input())

    for case in range(cases):
        planetData = input().split() #[temp, water?, magnetic field?, eccentricity of planet's orbit]

        habitableStatus = 'The planet is habitable.'

        if float(planetData[0]) < 0 or float(planetData[0]) > 100:
            habitableStatus = 'The planet is too cold.' if float(planetData[0]) < 0 else 'The planet is too hot.'
        elif planetData[1] == 'false':
            habitableStatus = 'The planet has no water.'
        elif planetData[2] == 'false':
            habitableStatus = 'The planet has no magnetic field.'
        elif float(planetData[3]) > 0.6:
            habitableStatus = "The planet's orbit is not ideal."

        print(habitableStatus)


if __name__ == '__main__':
    main()
def main():
    cases = int(input())
    for case in range(cases):
        sections = int(input())
        for section in range(sections):
            aircraft_name = input()
            aircraft_cords = input().split(',') # x,y
            landing_zone_start = input().split(',') # x,y
            landing_zone_end = input().split(',') # x,y

            slope_start = (float(landing_zone_start[1]) - float(aircraft_cords[1])) / (float(landing_zone_start[0]) - float(aircraft_cords[0]))
            slope_end = (float(landing_zone_end[1]) - float(aircraft_cords[1])) / (float(landing_zone_end[0]) - float(aircraft_cords[0]))

            is_in_range = (slope_start <= -0.8 and slope_start >= -1.6) and (slope_end <= -0.8 and slope_end >= -1.6)
            instructions = f'{aircraft_name}, Clear To Land!' if is_in_range else f'{aircraft_name}, Abort Landing!'
            print(instructions)

if __name__ == '__main__':
    main()
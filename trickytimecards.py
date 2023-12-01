for _ in range(int(input())):
    person_data = input().split(',')
    employee = person_data[0]
    person_data.remove(employee)
    total_minutes = 0

    for time_slot in person_data:
        hours, minutes = time_slot.split(':')
        total_minutes += int(minutes) + (int(hours)*60)
    
    total_hours = int(total_minutes / 60)
    total_minutes = total_minutes % 60

    plural_h = 'hours' if total_hours > 1 else 'hour'
    hours_str = f'{total_hours} {plural_h} ' if total_hours > 0 else ''

    plural_m = 'minutes' if total_minutes > 1 else 'minute'
    minutes_str = f'{total_minutes} {plural_m}' if total_minutes > 0 else ''

    final_str = f'{employee}={hours_str}{minutes_str}'

    print(final_str.rstrip())
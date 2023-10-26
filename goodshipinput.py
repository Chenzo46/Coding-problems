for _ in range(int(input())):
    total_system_count, working_system_count = input().split()
    all_systems = [input() for idx in range(int(total_system_count))]
    concerning_systems = all_systems
    for jdx in range(int(working_system_count)):
        concerning_systems.remove(input())
    concerning_systems.sort(key = lambda x: x.lower())
    print('\n'.join(concerning_systems))
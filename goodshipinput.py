for _ in range(int(input())):
    total_system_count, working_system_count = list(map(int, input().split()))
    all_systems = [input() for idx in range(total_system_count)]
    concerning_systems = all_systems.copy()
    for jdx in range(working_system_count):
        concerning_systems.remove(input())
    concerning_systems = sorted(concerning_systems, key = lambda x: x.lower())
    for sys in concerning_systems:
        print(sys)
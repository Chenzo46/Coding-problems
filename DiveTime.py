def main():
    cases = int(input())

    for case in range(cases):
        #Dive table data
        tableDemensions = list(map(int,input().split())) #entries,dives

        entries = [list(map(int,input().split())) for i in range(tableDemensions[0])] # [[max depth of entry, max bottom time, depth of required c-stop, decompression time], ...]
        dives = [list(map(int,input().split())) for i in range(tableDemensions[1])] # [[max depth reached by diver, bottom time], ...]


        entries.sort(key=lambda x: (x[0], x[1]))
        #Find stops required for each dive
        stops = []
        for dive in dives:
            #Find which entry to used based on diver's depth and bottom time
            applicableEntries = []

            maxDepth = -1
            maxBottomTime = -1
            found = False
            for entry in entries:
                if entry[0] == maxDepth and entry[1] == maxBottomTime and found:
                    applicableEntries.append(entry)
                elif (entry[0] >= dive[0] and entry[1] >= dive[1]) and len(applicableEntries) == 0:
                    maxDepth = entry[0]
                    maxBottomTime = entry[1]
                    applicableEntries.append(entry)
                    found = True
            #Get the stop depth and time for each applicable entry
            applicableEntries.sort(key=lambda x : x[2], reverse=True)
            for entry in applicableEntries:
                if entry[2] > 0 and entry[3] > 0:
                    stops.append(f'{entry[2]} {entry[3]}')
                else:
                    stops.append('No Stop')
            
        print('\n'.join(stops))

if __name__ == '__main__':
    main()
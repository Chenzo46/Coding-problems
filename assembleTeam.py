def main():
    cases = int(input())

    for case in range(cases):
        agents = input().split()
        agents.sort()
        #Find all possible teams (Please bear with me, my code makes no sense)
        possibleTeams = []
        largest = 0
        for i in agents:
            team = []
            team.append(i)
            for j in agents:
                c_pScore = int(j.split('=')[1])
                add = True
                if i != j:
                    for z in team:
                        z_pScore = int(z.split('=')[1])
                        if abs(z_pScore - c_pScore) > 10:
                            add = False
                    if add:
                        team.append(j)
            #Take names of each agent, throw out the personality scores, then sort team into alphabetical order
            team = list(map(lambda x : x.split('=')[0],team))
            team.sort()
            team = ' '.join(team)
            if(len(team) > largest):
                largest = len(team)

            if not team in possibleTeams:
                possibleTeams.append(team)
        #Filter out teams that are smaller than the largest team size
        possibleTeams = list(filter(lambda x : len(x) == largest, possibleTeams))
        #if more than one possible team exists at this point, print out the team that is higher up in the alphabet. Otherwise just print out the only team left.
        if len(possibleTeams) > 1:
            while len(possibleTeams) > 1:
                team1 = possibleTeams[0].split()
                team2 = possibleTeams[1].split()

                for x in range(len(team1)):
                    if ord(team1[x]) < ord(team2[x]):
                        possibleTeams.remove(' '.join(team2))
                        break
                    elif ord(team1[x]) > ord(team2[x]):
                        possibleTeams.remove(' '.join(team1))
                        break
                    else:
                        continue
            
            print(possibleTeams[0])
        else:
            print(possibleTeams[0])
            

if __name__ == '__main__':
    main()
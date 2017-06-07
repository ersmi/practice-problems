import random

# Does not currently satisfy rules 4 and 5 for input2.
#   Side case: if both teams are at 2/2 or -2/-2 consecutive home or away games
#   The game is invalid, but will currently be placed anyway.
#   Possible solutions:  
#       Switch team's invalid game with it's next round game.
#       Adjust cycle() to avoid these cases.

def loadTeams(file):
    ''' Return list of teams in file '''
    fd = open(file, 'r+')
    teams = fd.read().split("\n")
    if len(teams) > 30:
        raise Exception("%s contains more than 30 teams" % file)
    random.shuffle(teams)
    return teams

def cycle(team):
    ''' Cycle the tail of team '''
    return [team[0]] + [team[-1]] + team[1:-1]
    
def genSchedules(teams):
    ''' Generate list of all possible matches '''
    ret = []
    for y in range(len(teams)-1):
        teams = cycle(teams)
        teams1 = teams[:len(teams)/2]
        teams2 = teams[len(teams)/2:]
        round = []
        for (x,z) in zip(teams1,teams2):
            round += [(z,x)]
        ret += [round]
    return ret
      
def pprint(schedule, teams):
    '''
    Sort and print actual schedule for teams.
    '''
    i = 1
    homeaway = {x:0 for x in teams}
    newschedule = []
    for x in schedule: # Iterate through rounds
        print "Round %d" % i
        i += 1
        r = []
        for (y,z) in x:    # Iterate through games
            if homeaway[y] == 2 or homeaway[z] == -2:
                print "%s - %s" % (z, y)
                homeaway[y] -= 1
                homeaway[z] += 1
                r += [(z,y)]
            elif homeaway[y] == -2 or homeaway[z] == 2:
                print "%s - %s" % (y, z)
                homeaway[y] += 1
                homeaway[z] -= 1
                r += [(y,z)]
            else:
                print "%s - %s" % (y, z)
                homeaway[y] += 1
                homeaway[z] -= 1
                r += [(y,z)]
        newschedule += [r]
    # Second half of schedule, just reverse matches
    for x in newschedule[::-1]:
        print "Round %d" % i
        i += 1
        for (y,z) in x:
            print "%s - %s" % (z, y) # flip matches

teams = loadTeams('input1.txt')
pprint(genSchedules(teams),teams)

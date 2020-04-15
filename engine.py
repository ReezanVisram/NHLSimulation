import json
from playerclasses import Team, Player, Goalie
from gameclasses import Game
import random

teams = []

forwardPointsPerGame = [-1]

defenseRanking = [-1]

goalieRanking = [-1]

def getTeamNames(data):
    teamNames = []
    for team in data['teams']:
        teamNames.append(team['teamName'])

    return teamNames

def getTeamConferences(data):
    teamConferences = []

    for team in data['teams']:
        teamConferences.append(team['conference'])

    return teamConferences

def getTeamDivisions(data):
    teamDivisions = []

    for team in data['teams']:
        teamDivisions.append(team['division'])

    return teamDivisions

def getPlayersList(teamNames, data):
    playersList = []
    for x in range(len(data['teams'])):
        for i in data['teams'][x]['roster']:
            try:
                playersList.append(Player(teamNames[x], i['playerName'], i['playerPosition'], i['stats']['gamesPlayed'], i['stats']['goals'], i['stats']['assists'], i['stats']['points'], i['stats']['plusMinus'], i['stats']['timeOnIcePerGame'], 0))
            except:
                try:
                    playersList.append(Goalie(teamNames[x], i['playerName'], i['playerPosition'], i['stats']['gamesPlayed'], i['stats']['wins'], i['stats']['losses'], i['stats']['savePercentage'], i['stats']['goalsAgainstAverage'], 0))

                except:
                    continue
    return playersList

def getTeamRoster(currTeamName):
    currTeamObject = Team(currTeamName, [], None, None)
    for player in playersList:
        if player.teamName == currTeamName:
            currTeamObject.roster.append(player)

    return currTeamObject

with open('information.json') as inputFile:
    data = json.load(inputFile)

    teamNames = getTeamNames(data)
    teamConferences = getTeamConferences(data)
    teamDivisions = getTeamDivisions(data)
    playersList = getPlayersList(teamNames, data)


for i in teamNames:
    teams.append(getTeamRoster(i))

for i in range(len(teams)):
    teams[i].conference = teamConferences[i]
    teams[i].division = teamDivisions[i]
    for j in range(len(teams[i].roster)):
        if (teams[i].roster[j].position != 'G'):
            if (teams[i].roster[j].position != 'D'):
                currPlayerPPG = (teams[i].roster[j].points / teams[i].roster[j].gamesPlayed)
                forwardPointsPerGame.append(currPlayerPPG)
            else:
                currPlayerNormalizedPlusMinus = (teams[i].roster[j].plusMinus / teams[i].roster[j].gamesPlayed)
                currPlayerPPG = (teams[i].roster[j].points / teams[i].roster[j].gamesPlayed)

                defenseRanking.append(currPlayerNormalizedPlusMinus + currPlayerPPG)
        else:
            currGoalieAdjustedSV = (teams[i].roster[j].savePercentage / teams[i].roster[j].goalsAgainstAverage)

            currGoalieWinPct = (teams[i].roster[j].wins / teams[i].roster[j].gamesPlayed)
    
            goalieRanking.append(currGoalieAdjustedSV + currGoalieWinPct)

forwardPointsPerGame.sort()
defenseRanking.sort()
goalieRanking.sort()

forwardPointsPerGame = list(dict.fromkeys(forwardPointsPerGame))
defenseRanking = list(dict.fromkeys(defenseRanking))
goalieRanking = list(dict.fromkeys(goalieRanking))

baseOverall = 70
for ppg in range(len(forwardPointsPerGame)):
    for player in playersList:
        if (player.position != 'G') and (player.position != 'D'):
            if ((player.points / player.gamesPlayed) == forwardPointsPerGame[ppg]):
                nearestMultipleOf14 = 14 * round(ppg / 14)
                baseOverall += nearestMultipleOf14 / 14

                player.overall = baseOverall

                baseOverall = 70

for defense in range(len(defenseRanking)):
    for player in playersList:
        if (player.position == 'D'):
            currPlayerRanking = (player.plusMinus / player.gamesPlayed) + (player.points / player.gamesPlayed)
            if (currPlayerRanking == defenseRanking[defense]):
                nearestMultipleOf10 = 10 * round(defense / 10)
                baseOverall += nearestMultipleOf10 / 10

                player.overall = baseOverall

                baseOverall = 70

for goalie in range(len(goalieRanking)):
    for player in playersList:
        if (player.position == 'G'):
            currGoalieRankingValue = (player.savePercentage / player.goalsAgainstAverage) + (player.wins / player.gamesPlayed)

            if (currGoalieRankingValue == goalieRanking[goalie]):
                nearestMultipleOf3 = 3 * round(goalie / 3)
                baseOverall += nearestMultipleOf3 / 3

                player.overall = baseOverall

                baseOverall = 70

atlanticTeams = []
metroTeams = []
centralTeams = []
pacificTeams = []


for team in teams:
    if (team.division == 'Atlantic'):
        atlanticTeams.append(team)
    elif (team.division == 'Metropolitan'):
        metroTeams.append(team)
    elif (team.division == 'Central'):
        centralTeams.append(team)
    elif (team.division == 'Pacific'):
        pacificTeams.append(team)
    else:
        print(team.name + "'s division is not valid " + team.conference)

for i in teams:
    i.createAllInfo()

def createSchedule(atlantic, metro, central, pacific):
    schedule = [[] for i in range(214)]
    extraCentralTeams = []

    for atlanticTeam in atlantic:
        atlanticCopy = [x for x in atlantic if x != atlanticTeam]
        gameDays = []

        for otherAtlanticTeam in atlanticCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)
                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(atlanticTeam, otherAtlanticTeam, day, []))

        for metroTeam in metro:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)
                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(atlanticTeam, metroTeam, day, []))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)
            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(atlanticTeam, centralTeam, day, []))

        for pacificTeam in pacific:
            day = random.randint(0, len(schedule) - 1)
            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(atlanticTeam, pacificTeam, day, []))

    for metroTeam in metro:
        metroCopy = [x for x in metro if x != metroTeam]
        gameDays = []

        for otherMetroTeam in metroCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(metroTeam, otherMetroTeam, day, []))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(metroTeam, atlanticTeam, day, []))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(metroTeam, centralTeam, day, []))

        for pacificTeam in pacific:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(metroTeam, pacificTeam, day, []))

    for centralTeam in central:
        centralCopy = [x for x in central if x != centralTeam]
        gameDays = []

        for otherCentralTeam in centralCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(centralTeam, otherCentralTeam, day, []))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(centralTeam, atlanticTeam, day, []))

        for metroTeam in metro:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(centralTeam, metroTeam, day, []))

        for pacificTeam in pacific:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(centralTeam, pacificTeam, day, []))

        extraCentralTeam = centralCopy[random.randint(0, len(centralCopy) - 1)]

        day = random.randint(0, len(schedule) - 1)

        while (day in gameDays):
            day = random.randint(0, len(schedule) - 1)

        while (extraCentralTeam in extraCentralTeams):
            extraCentralTeam = central[random.randint(0, len(central) - 1)]

        extraCentralTeams.append(extraCentralTeam)
        gameDays.append(day)
        schedule[day].append(Game(centralTeam, extraCentralTeam, day, []))

    for pacificTeam in pacific:
        pacificCopy = [x for x in pacific if x != pacificTeam]
        gameDays = []

        for otherPacificTeam in pacificCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(pacificTeam, otherPacificTeam, day, []))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(pacificTeam, atlanticTeam, day, []))

        for metroTeam in metro:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(pacificTeam, metroTeam, day, []))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(pacificTeam, centralTeam, day, []))

    return schedule

seasonSchedule = createSchedule(atlanticTeams, metroTeams, centralTeams, pacificTeams)

for i in range(len(seasonSchedule)):
    for j in range(len(seasonSchedule[i])):
        seasonSchedule[i][j].simulateGame()

        for team in teams:
            if (team == seasonSchedule[i][j].winner):
                team.points += 2

teams.sort(key=lambda x: x.points, reverse=True)

for i in teams:
    print("The", i.name, "finished the season with", i.points, 'points')



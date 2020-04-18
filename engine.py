import json
import random
from playerclasses import Team, Player, Goalie
from gameclasses import Game, PlayoffGame, Series


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
                schedule[day].append(Game(atlanticTeam, otherAtlanticTeam, day))

        for metroTeam in metro:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)
                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(atlanticTeam, metroTeam, day))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)
            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(atlanticTeam, centralTeam, day))

        for pacificTeam in pacific:
            day = random.randint(0, len(schedule) - 1)
            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(atlanticTeam, pacificTeam, day))

    for metroTeam in metro:
        metroCopy = [x for x in metro if x != metroTeam]
        gameDays = []

        for otherMetroTeam in metroCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(metroTeam, otherMetroTeam, day))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(metroTeam, atlanticTeam, day))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(metroTeam, centralTeam, day))

        for pacificTeam in pacific:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(metroTeam, pacificTeam, day))

    for centralTeam in central:
        centralCopy = [x for x in central if x != centralTeam]
        gameDays = []

        for otherCentralTeam in centralCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(centralTeam, otherCentralTeam, day))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(centralTeam, atlanticTeam, day))

        for metroTeam in metro:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(centralTeam, metroTeam, day))

        for pacificTeam in pacific:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(centralTeam, pacificTeam, day))

        extraCentralTeam = centralCopy[random.randint(0, len(centralCopy) - 1)]

        day = random.randint(0, len(schedule) - 1)

        while (day in gameDays):
            day = random.randint(0, len(schedule) - 1)

        while (extraCentralTeam in extraCentralTeams):
            extraCentralTeam = central[random.randint(0, len(central) - 1)]

        extraCentralTeams.append(extraCentralTeam)
        gameDays.append(day)
        schedule[day].append(Game(centralTeam, extraCentralTeam, day))

    for pacificTeam in pacific:
        pacificCopy = [x for x in pacific if x != pacificTeam]
        gameDays = []

        for otherPacificTeam in pacificCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in gameDays):
                    day = random.randint(0, len(schedule) - 1)

                gameDays.append(day)
                schedule[day].append(Game(pacificTeam, otherPacificTeam, day))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(pacificTeam, atlanticTeam, day))

        for metroTeam in metro:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(pacificTeam, metroTeam, day))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)

            while (day in gameDays):
                day = random.randint(0, len(schedule) - 1)

            gameDays.append(day)
            schedule[day].append(Game(pacificTeam, centralTeam, day))

    return schedule

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

easternTeams = atlanticTeams + metroTeams
westernTeams = centralTeams + pacificTeams

for i in teams:
    i.createAllInfo()

seasonSchedule = createSchedule(atlanticTeams, metroTeams, centralTeams, pacificTeams)

for i in range(len(seasonSchedule)):
    for j in range(len(seasonSchedule[i])):
        seasonSchedule[i][j].simulateGame()

        seasonSchedule[i][j].winner.points += 2

        if (seasonSchedule[i][j].wasOvertime):
            seasonSchedule[i][j].loser.points += 1

teams.sort(key=lambda x: x.points, reverse=True)

atlanticTeams.sort(key=lambda x: x.points, reverse=True)
metroTeams.sort(key=lambda x: x.points, reverse=True)
centralTeams.sort(key=lambda x: x.points, reverse=True)
pacificTeams.sort(key=lambda x: x.points, reverse=True)

easternTeams.sort(key=lambda x: x.points, reverse=True)
westernTeams.sort(key=lambda x: x.points, reverse=True)

easternPlayoffTeams = []
westernPlayoffTeams = []

for playoffTeam in range(3):
    easternPlayoffTeams.append(atlanticTeams[playoffTeam])
    easternPlayoffTeams.append(metroTeams[playoffTeam])

    westernPlayoffTeams.append(centralTeams[playoffTeam])
    westernPlayoffTeams.append(pacificTeams[playoffTeam])

for wildcard in range(2):
    for easternTeam in easternTeams:
        if easternTeam not in easternPlayoffTeams:
            easternPlayoffTeams.append(easternTeam)
            break

    for westernTeam in westernTeams:
        if westernTeam not in westernPlayoffTeams:
            westernPlayoffTeams.append(westernTeam)
            break

print("Atlantic Division: ")
for atlanticTeam in atlanticTeams:
    print("The {} finished with {} points".format(atlanticTeam.name, atlanticTeam.points))
print()

print("Metropolitan Division: ")
for metroTeam in metroTeams:
    print("The {} finished with {} points".format(metroTeam.name, metroTeam.points))
print()

print("Central Division: ")
for centralTeam in centralTeams:
    print("The {} finished with {} points".format(centralTeam.name, centralTeam.points))
print()

print("Pacific Division: ")
for pacificTeam in pacificTeams:
    print("The {} finished with {} points".format(pacificTeam.name, pacificTeam.points))
print()
print()

print("Eastern Conference Playoff Teams: ")
for easternPlayoffTeam in easternPlayoffTeams:
    print(easternPlayoffTeam.name)
print()

print("Western Conference Playoff Teams: ")
for westernPlayoffTeam in westernPlayoffTeams:
    print(westernPlayoffTeam.name)

print()
print()

easternRound1Winners = []
westernRound1Winners = []

easternRound2Winners = []
westernRound2Winners = []

def generateRound1(atlantic, metro, central, pacific, eastern, western):
    pairs = []
    currPair = [eastern[0], eastern[7]]
    pairs.append(currPair)
    currPair = [atlantic[1], atlantic[2]]
    pairs.append(currPair)
    currPair = [eastern[1], eastern[6]]
    pairs.append(currPair)
    currPair = [metro[1], metro[2]]
    pairs.append(currPair)

    currPair = [western[0], western[7]]
    pairs.append(currPair)
    currPair = [pacific[1], pacific[2]]
    pairs.append(currPair)
    currPair = [western[1], western[6]]
    pairs.append(currPair)
    currPair = [central[1], central[2]]
    pairs.append(currPair)

    round1 = []

    for pair in pairs:
        seriesSchedule = []
        gameDay = random.randint(0, 1)

        for day in range(7):
            seriesSchedule.append(PlayoffGame(pair[0], pair[1], gameDay))
            gameDay += 2

        round1.append(Series(seriesSchedule))

    return round1

def generateRound2(eastern, western):
    pairs = []
    round2 = []

    currPair = [eastern[0], eastern[1]]
    pairs.append(currPair)
    currPair = [eastern[2], eastern[3]]
    pairs.append(currPair)

    currPair = [western[0], western[1]]
    pairs.append(currPair)
    currPair = [western[2], western[3]]
    pairs.append(currPair)

    for pair in pairs:
        seriesSchedule = []
        gameDay = random.randint(0, 1)

        for day in range(7):
            seriesSchedule.append(PlayoffGame(pair[0], pair[1], gameDay))
            gameDay += 2
        
        round2.append(Series(seriesSchedule))

    return round2

def generateRound3(eastern, western):
    gameDay = 0
    easternFinals = []
    round3 = []

    for day in range(7):
        easternFinals.append(PlayoffGame(eastern[0], eastern[1], gameDay))
        gameDay += 2
    
    round3.append(Series(easternFinals))

    gameday = 1
    westernFinals = []

    for day in range(7):
        westernFinals.append(PlayoffGame(western[0], western[1], gameDay))
        gameDay += 2

    round3.append(Series(westernFinals))

    return round3

def generateStanleyCupFinals(eastern, western):
    gameDay = 0
    seriesSchedule = []
    cupFinals = []

    for day in range(7):
        seriesSchedule.append(PlayoffGame(eastern, western, gameDay))
        gameDay += 2

    cupFinals.append(Series(seriesSchedule))

    return cupFinals
    
round1 = generateRound1(atlanticTeams, metroTeams, centralTeams, pacificTeams, easternPlayoffTeams, westernPlayoffTeams)

for series in round1:
    series.simulateSeries()

    print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their first round matchup. The series went", series.gamesPlayed, "games")
    
    if (series.seriesWinner.conference == "Eastern"):
        easternRound1Winners.append(series.seriesWinner)

    else:
        westernRound1Winners.append(series.seriesWinner)

print()
print()

round2 = generateRound2(easternRound1Winners, westernRound1Winners)

for series in round2:
    series.simulateSeries()

    print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their second round matchup. The series went", series.gamesPlayed, "games")

    if (series.seriesWinner.conference == 'Eastern'):
        easternRound2Winners.append(series.seriesWinner)

    else:
        westernRound2Winners.append(series.seriesWinner)

print()
print()

round3 = generateRound3(easternRound2Winners, westernRound2Winners)

for series in round3:
    series.simulateSeries()

    print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their third round matchup. The series went", series.gamesPlayed, "games")

    if (series.seriesWinner.conference == 'Eastern'):
        easternChampion = series.seriesWinner

    else:
        westernChampion = series.seriesWinner

stanleyCupFinals = generateStanleyCupFinals(easternChampion, westernChampion)

for series in stanleyCupFinals:
    series.simulateSeries()

    print("Your 2020-2021 Stanley Cup Champions are the", series.seriesWinner.name)
import json
import random
from playerclasses import Team, Player, Goalie
from gameclasses import Game, PlayoffGame, Series

# These lists are defined at the top following the style of my codebase, but are not used until far later.
teams = []
atlanticTeams = []
metroTeams = []
centralTeams = []
pacificTeams = []
easternPlayoffTeams = []
westernPlayoffTeams = []

# The 'data' parameter refers to the information gotten from 'information.json' on lines 249-256 
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

# This creats the entire list of all of the players, which are then separated by team
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

# There may be a way to do this by removing teams from their respective lists, which could be useful for creating home and away games later.
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

def getForwards(players):
    forwards = []
    for player in players:
        if (player.position == 'LW') or (player.position == 'C') or (player.position == 'RW'):
            forwards.append(player)

    return forwards

def getDefensemen(players):
    defensemen = []
    for player in players:
        if (player.position == 'D'):
            defensemen.append(player)

    return defensemen

def getGoalies(players):
    goalies = []
    for player in players:
        if (player.position == 'G'):
            goalies.append(player)

    return goalies

def rankForwards(forwards):
    forwardRankings = [-1]

    for team in teams:
        for forward in forwards:
            currPlayerPPG = (forward.points / forward.gamesPlayed)
            forwardRankings.append(currPlayerPPG)

    forwardRankings.sort()
    forwardRankings = list(dict.fromkeys(forwardRankings))

    return forwardRankings

def rankDefensemen(defensemen):
    defenseRankings = [-1]


    for defenseman in defensemen:
        currPlayerNormalizedPlusMinus = (defenseman.plusMinus / defenseman.gamesPlayed)
        currPlayerPPG = (defenseman.points / defenseman.gamesPlayed)

        defenseRankings.append(currPlayerNormalizedPlusMinus + currPlayerPPG)

    defenseRankings.sort()
    defenseRankings = list(dict.fromkeys(defenseRankings))

    return defenseRankings

def rankGoalies(goalies):
    goalieRankings = [-1]

    for goalie in goalies:
        currGoalieAdjustedSV = (goalie.savePercentage / goalie.goalsAgainstAverage)

        currGoalieWinPct = (goalie.wins / goalie.gamesPlayed)

        goalieRankings.append(currGoalieAdjustedSV + currGoalieWinPct)

    goalieRankings.sort()
    goalieRankings = list(dict.fromkeys(goalieRankings))

    return goalieRankings

def determineForwardOveralls(forwards, forwardRankings):
    baseOverall = 70
    for rank in range(len(forwardRankings)):
        for forward in forwards:
            currForwardValue = (forward.points / forward.gamesPlayed)
            if (currForwardValue == forwardRankings[rank]):
                nearestMultipleOf14 = 14 * round(rank / 14)
                baseOverall += nearestMultipleOf14 / 14

                forward.overall = baseOverall

                baseOverall = 70

def determineDefenseOveralls(defensemen, defenseRankings):
    baseOverall = 70

    for rank in range(len(defenseRankings)):
        for defenseman in defensemen:
            currDefenseValue = (defenseman.plusMinus / defenseman.gamesPlayed) + (defenseman.points / defenseman.gamesPlayed)
            if (currDefenseValue == defenseRankings[rank]):
                nearestMultipleOf10 = 10 * round(rank / 10)
                baseOverall += nearestMultipleOf10 / 10

                defenseman.overall = baseOverall

                baseOverall = 70

def determineGoalieOveralls(goalies, goalieRankings):
    baseOverall = 70

    for rank in range(len(goalieRankings)):
        for goalie in goalies:
            currGoalieValue = (goalie.savePercentage / goalie.goalsAgainstAverage) + (goalie.wins / goalie.gamesPlayed)

            if (currGoalieValue == goalieRankings[rank]):
                nearestMultipleOf3 = 3 * round(rank / 3)
                baseOverall += nearestMultipleOf3 / 3

                goalie.overall = baseOverall

                baseOverall = 70

def simulateRegularSeason(schedule):
    for day in range(len(schedule)):
        for game in range(len(schedule[day])):
            schedule[day][game].simulateGame()

            schedule[day][game].winner.points += 2

            if (schedule[day][game].wasOvertime):
                schedule[day][game].loser.points += 2

def determineStandings(teams, atlantic, metro, central, pacific, eastern, western):
    teams.sort(key=lambda x: x.points, reverse=True)

    atlantic.sort(key=lambda x: x.points, reverse=True)
    metro.sort(key=lambda x: x.points, reverse=True)
    central.sort(key=lambda x: x.points, reverse=True)
    pacific.sort(key=lambda x: x.points, reverse=True)

    eastern.sort(key=lambda x: x.points, reverse=True)
    western.sort(key=lambda x: x.points, reverse=True)

def getPlayoffTeams(atlantic, metro, central, pacific, eastern, western):
    global easternPlayoffTeams, westernPlayoffTeams
    for playoffTeam in range(3):
        easternPlayoffTeams.append(atlantic[playoffTeam])
        easternPlayoffTeams.append(metro[playoffTeam])

        westernPlayoffTeams.append(central[playoffTeam])
        westernPlayoffTeams.append(pacific[playoffTeam])

    for wildcard in range(2):
        for easternTeam in eastern:
            if easternTeam not in easternPlayoffTeams:
                easternPlayoffTeams.append(easternTeam)
                break

        for westernTeam in western:
            if westernTeam not in westernPlayoffTeams:
                westernPlayoffTeams.append(westernTeam)
                break
# Creates all of the actual lists of teams and players
with open('information.json') as inputFile:
    data = json.load(inputFile)
    teamNames = getTeamNames(data)
    teamConferences = getTeamConferences(data)
    teamDivisions = getTeamDivisions(data)
    playersList = getPlayersList(teamNames, data)

forwards = getForwards(playersList)
defensemen = getDefensemen(playersList)
goalies = getGoalies(playersList)

for i in teamNames:
    teams.append(getTeamRoster(i))

for team in range(len(teams)):
    teams[team].conference = teamConferences[team]
    teams[team].division = teamDivisions[team]

forwardRankings = rankForwards(forwards)
defenseRankings = rankDefensemen(defensemen)
goalieRankings = rankGoalies(goalies)

determineForwardOveralls(forwards, forwardRankings)
determineDefenseOveralls(defensemen, defenseRankings)
determineGoalieOveralls(goalies, goalieRankings)

# Determines what division every team is in to later create the schedule with the above createSchedule function
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

# Uses the method defined in the Team class
for i in teams:
    i.createAllInfo()

seasonSchedule = createSchedule(atlanticTeams, metroTeams, centralTeams, pacificTeams)

# The actual simulation of the regular season, using methods defined in the Game class
simulateRegularSeason(seasonSchedule)

# Ranks the entire league and each division to create the playoffs
determineStandings(teams, atlanticTeams, metroTeams, centralTeams, pacificTeams, easternTeams, westernTeams)

# Determines which teams are in the playoffs
getPlayoffTeams(atlanticTeams, metroTeams, centralTeams, pacificTeams, easternTeams, westernTeams)

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

# Initializes empty lists down here because it makes more sense here
easternRound1Winners = []
westernRound1Winners = []

easternRound2Winners = []
westernRound2Winners = []

easternChampion = None
westernChampion = None

def generateRound1(atlantic, metro, central, pacific, eastern, western):
    # Pairs are made manually for now
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

def simulateRound1(round1):
    global easternRound1Winners, westernRound1Winners
    for series in round1:
        series.simulateSeries()

        print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their first round matchup. The series went", series.gamesPlayed, "games")
        
        if (series.seriesWinner.conference == "Eastern"):
            easternRound1Winners.append(series.seriesWinner)

        else:
            westernRound1Winners.append(series.seriesWinner)

    print()
    print()

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

def simulateRound2(round2):
    global easternRound2Winners, westernRound2Winners
    for series in round2:
        series.simulateSeries()

        print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their second round matchup. The series went", series.gamesPlayed, "games")

        if (series.seriesWinner.conference == 'Eastern'):
            easternRound2Winners.append(series.seriesWinner)

        else:
            westernRound2Winners.append(series.seriesWinner)

    print()
    print()

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

def simulateRound3(round3):
    global easternChampion, westernChampion
    for series in round3:
        series.simulateSeries()

        print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their third round matchup. The series went", series.gamesPlayed, "games")

        if (series.seriesWinner.conference == 'Eastern'):
            easternChampion = series.seriesWinner

        else:
            westernChampion = series.seriesWinner

def generateStanleyCupFinals(eastern, western):
    gameDay = 0
    seriesSchedule = []
    cupFinals = []

    for day in range(7):
        seriesSchedule.append(PlayoffGame(eastern, western, gameDay))
        gameDay += 2

    cupFinals.append(Series(seriesSchedule))

    return cupFinals

def simulateStanleyCupFinals(stanleyCupFinals):
    for series in stanleyCupFinals:
        series.simulateSeries()

    return series.seriesWinner


# Simulates the first round using methods defined in the PlayoffGame class and the Series class
simulateRound1(generateRound1(atlanticTeams, metroTeams, centralTeams, pacificTeams, easternPlayoffTeams, westernPlayoffTeams))


# Simulates the second round
simulateRound2(generateRound2(easternRound1Winners, westernRound1Winners))


# Simulates each Conference Final
simulateRound3(generateRound3(easternRound2Winners, westernRound2Winners))

# Simulates the Stanley Cup Finals
stanleyCupChampion = simulateStanleyCupFinals(generateStanleyCupFinals(easternChampion, westernChampion))

print("Your 2020-21 Stanley Cup Champions are the {}!".format(stanleyCupChampion.name))


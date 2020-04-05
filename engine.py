import json
from playerclasses import Team, Player, Goalie

teams = []

forwardPointsPerGame = [-1]

defenseRanking = [-1]

goalieRanking = [-1]

def getTeamNames(data):
    teamNames = []
    for team in data['teams']:
        teamNames.append(team['teamName'])

    return teamNames

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
    currTeamObject = Team(currTeamName, [])
    for player in playersList:
        if player.teamName == currTeamName:
            currTeamObject.roster.append(player)

    return currTeamObject

with open('information.json') as inputFile:
    data = json.load(inputFile)

    teamNames = getTeamNames(data)
    playersList = getPlayersList(teamNames, data)


for i in teamNames:
    teams.append(getTeamRoster(i))

for i in range(len(teams)):
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


for i in teams:
    i.createAllInfo()


print(teams[0].forwardLines)

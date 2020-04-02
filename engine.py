import json
from playerclasses import Team, Player, Goalie

teams = []

forwardPointsPerGame = [-1]

defenseRanking = [-1]


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
                    playersList.append(Goalie(teamNames[x], i['playerName'], i['playerPosition'], i['stats']['gamesPlayed'], i['stats']['wins'], i['stats']['losses'], i['stats']['savePercentage'], i['stats']['goalsAgainstAverage']))

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

forwardPointsPerGame.sort()
defenseRanking.sort()

forwardPointsPerGame = list(dict.fromkeys(forwardPointsPerGame))
defenseRanking = list(dict.fromkeys(defenseRanking))

baseOverall = 70
for ppg in range(len(forwardPointsPerGame)):
    for player in playersList:
        if (player.position != 'G') and (player.position != 'D'):
            if ((player.points / player.gamesPlayed) == forwardPointsPerGame[ppg]):
                nearestMultipleOf14 = 14 * round(ppg / 14)
                baseOverall += nearestMultipleOf14 / 14

                player.overall = baseOverall

                baseOverall = 70

                print(player.playerName, "is", player.overall)

for defense in range(len(defenseRanking)):
    for player in playersList:
        if (player.position == 'D'):
            currPlayerRanking = (player.plusMinus / player.gamesPlayed) + (player.points / player.gamesPlayed)
            if (currPlayerRanking == defenseRanking[defense]):
                nearestMultipleOf14 = 14 * round(defense / 14)
                baseOverall += nearestMultipleOf14 / 14

                player.overall = baseOverall

                baseOverall = 70

                print(player.playerName, "is", player.overall)
